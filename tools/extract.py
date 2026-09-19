#!/usr/bin/env python3
"""Phase A2/A3 - extraction, OCR and provenance database.

Per page: try the embedded text layer; if it is below threshold, rasterise and
OCR. Every OCR'd page keeps its rendered image so that a decisive passage can
later be checked against the image, which docs/04 section 2.4 requires before
anything extracted by machine may be quoted as evidence.

Usage:
    python3 tools/extract.py [--corpus DIR] [--only ID ...] [--dpi 300]

Outputs:
    <corpus>/text/<id>/p0001.txt   extracted text, one file per page
    <corpus>/images/<id>/p0001.png rendered page image (OCR'd pages only)
    <corpus>/pages.db              one row per page, with method and quality
"""

import argparse
import datetime as dt
import json
import pathlib
import re
import sqlite3
import subprocess
import sys

# Below this many characters a page is treated as having no usable text layer.
TEXT_LAYER_MIN_CHARS = 100

SCHEMA = """
CREATE TABLE IF NOT EXISTS pages (
    doc_id        TEXT NOT NULL,
    page          INTEGER NOT NULL,
    method        TEXT NOT NULL,      -- 'text-layer' | 'ocr' | 'empty'
    chars         INTEGER NOT NULL,
    alpha_ratio   REAL,               -- letters / non-space chars
    word_ratio    REAL,               -- plausible-word tokens / all tokens
    quality       TEXT,               -- 'good' | 'check' | 'poor'
    image_path    TEXT,               -- rendered page, when OCR was used
    text_path     TEXT NOT NULL,
    image_verified INTEGER DEFAULT 0, -- set by a human, never by this script
    extracted_utc TEXT NOT NULL,
    PRIMARY KEY (doc_id, page)
);
CREATE TABLE IF NOT EXISTS documents (
    doc_id      TEXT PRIMARY KEY,
    title       TEXT, institution TEXT, type TEXT, oath TEXT,
    event_date  TEXT, doc_date TEXT, release_date TEXT,
    url         TEXT, sha256 TEXT, bytes INTEGER, pages INTEGER,
    retrieved_utc TEXT, role TEXT
);
"""

WORDISH = re.compile(r"^[A-Za-z][A-Za-z'’\-]{1,}$")


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


def page_count(pdf: pathlib.Path) -> int:
    out = run(["pdfinfo", str(pdf)]).stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return int(m.group(1)) if m else 0


def score(text: str) -> tuple:
    """Crude but honest quality signals. Not a substitute for image checking."""
    chars = len(text.strip())
    dense = [c for c in text if not c.isspace()]
    alpha_ratio = (sum(c.isalpha() for c in dense) / len(dense)) if dense else 0.0
    tokens = text.split()
    wordish = sum(1 for t in tokens if WORDISH.match(t.strip(".,;:()[]\"'")))
    word_ratio = (wordish / len(tokens)) if tokens else 0.0
    if chars < TEXT_LAYER_MIN_CHARS:
        q = "poor"
    elif alpha_ratio >= 0.75 and word_ratio >= 0.60:
        q = "good"
    elif alpha_ratio >= 0.60 and word_ratio >= 0.40:
        q = "check"
    else:
        q = "poor"
    return chars, round(alpha_ratio, 3), round(word_ratio, 3), q


def text_layer_pages(pdf: pathlib.Path, n: int) -> list:
    """Extract the whole document once; pdftotext separates pages with \\f."""
    out = run(["pdftotext", "-layout", str(pdf), "-"]).stdout
    pages = out.split("\f")
    if pages and pages[-1].strip() == "":
        pages = pages[:-1]
    while len(pages) < n:
        pages.append("")
    return pages[:n]


def ocr_page(pdf: pathlib.Path, page: int, img_dir: pathlib.Path, dpi: int) -> tuple:
    img_dir.mkdir(parents=True, exist_ok=True)
    stem = img_dir / f"p{page:04d}"
    run(["pdftoppm", "-png", "-r", str(dpi), "-f", str(page), "-l", str(page),
         "-singlefile", str(pdf), str(stem)])
    img = stem.with_suffix(".png")
    if not img.exists():
        return "", None
    res = run(["tesseract", str(img), "stdout", "--dpi", str(dpi)])
    return res.stdout, img


def latest_manifest_records(corpus: pathlib.Path) -> dict:
    recs = {}
    mf = corpus / "manifest.jsonl"
    for line in mf.read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            if r.get("ok"):
                recs[r["id"]] = r
    return recs


def main() -> int:
    ap = argparse.ArgumentParser()
    here = pathlib.Path(__file__).resolve().parent
    ap.add_argument("--corpus", default=str(here.parent / "corpus"))
    ap.add_argument("--only", nargs="*", default=None)
    ap.add_argument("--dpi", type=int, default=300)
    args = ap.parse_args()

    corpus = pathlib.Path(args.corpus)
    db = sqlite3.connect(corpus / "pages.db")
    db.executescript(SCHEMA)

    recs = latest_manifest_records(corpus)
    ids = args.only or list(recs)

    for did in ids:
        rec = recs.get(did)
        if not rec:
            print(f"[skip] {did}: no successful fetch in manifest")
            continue
        pdf = corpus / rec["path"]
        n = page_count(pdf)
        db.execute(
            "INSERT OR REPLACE INTO documents VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (did, rec["title"], rec["institution"], rec["type"], rec.get("oath"),
             rec.get("event_date"), rec.get("doc_date"), rec.get("release_date"),
             rec["url"], rec["sha256"], int(rec["bytes"]), n,
             rec["retrieved_utc"], rec.get("role")))

        txt_dir = corpus / "text" / did
        img_dir = corpus / "images" / did
        txt_dir.mkdir(parents=True, exist_ok=True)

        layer = text_layer_pages(pdf, n)
        ocr_used = 0
        for i in range(1, n + 1):
            body = layer[i - 1]
            method = "text-layer"
            img = None
            if len(body.strip()) < TEXT_LAYER_MIN_CHARS:
                body, img = ocr_page(pdf, i, img_dir, args.dpi)
                method = "ocr" if body.strip() else "empty"
                ocr_used += 1
            chars, alpha, wordr, q = score(body)
            tp = txt_dir / f"p{i:04d}.txt"
            tp.write_text(body, encoding="utf-8")
            db.execute(
                "INSERT OR REPLACE INTO pages VALUES (?,?,?,?,?,?,?,?,?,0,?)",
                (did, i, method, chars, alpha, wordr, q,
                 str(img.relative_to(corpus)) if img else None,
                 str(tp.relative_to(corpus)), utcnow()))
        db.commit()
        row = db.execute(
            "SELECT SUM(chars), SUM(method='ocr'), SUM(quality='good'), "
            "SUM(quality='check'), SUM(quality='poor') FROM pages WHERE doc_id=?",
            (did,)).fetchone()
        print(f"[done] {did:28} pages={n:4}  ocr={row[1] or 0:4}  "
              f"chars={row[0] or 0:8}  good/check/poor={row[2] or 0}/{row[3] or 0}/{row[4] or 0}")

    db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
