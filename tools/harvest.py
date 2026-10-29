#!/usr/bin/env python3
"""Phase A1 - corpus harvest.

Fetches every document in seed_corpus.json, records provenance, and never
overwrites silently: a re-fetch that yields a different SHA-256 is logged as an
event, because a primary source changing under us is itself evidence.

Usage:
    python3 tools/harvest.py [--corpus DIR] [--seed FILE] [--only ID ...]

Outputs:
    <corpus>/raw/<id>.pdf          the file as served
    <corpus>/manifest.jsonl        one provenance record per fetch attempt
"""

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import subprocess
import sys

UA = "9-11-evidence-review/0.1 (research audit; contact via repository)"


def utcnow() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def prior_hashes(manifest: pathlib.Path) -> dict:
    """Most recent recorded hash per document id."""
    seen = {}
    if not manifest.exists():
        return seen
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        if rec.get("sha256"):
            seen[rec["id"]] = rec["sha256"]
    return seen


def fetch(url: str, dest: pathlib.Path) -> dict:
    """curl is used rather than a Python HTTP client so the proxy config,
    TLS bundle and redirect behaviour of the environment apply unchanged."""
    fmt = "%{http_code} %{content_type} %{size_download} %{url_effective}"
    proc = subprocess.run(
        ["curl", "-sSL", "--max-time", "600", "-A", UA,
         "-w", fmt, "-o", str(dest), url],
        capture_output=True, text=True,
    )
    out = (proc.stdout or "").strip().split(" ", 3)
    while len(out) < 4:
        out.append("")
    return {
        "http_status": out[0],
        "content_type": out[1],
        "bytes": out[2],
        "final_url": out[3],
        "curl_rc": proc.returncode,
        "curl_stderr": (proc.stderr or "").strip()[:500],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    here = pathlib.Path(__file__).resolve().parent
    ap.add_argument("--seed", default=str(here / "seed_corpus.json"))
    ap.add_argument("--corpus", default=str(here.parent / "corpus"))
    ap.add_argument("--only", nargs="*", default=None)
    args = ap.parse_args()

    seed = json.loads(pathlib.Path(args.seed).read_text(encoding="utf-8"))
    corpus = pathlib.Path(args.corpus)
    raw = corpus / "raw"
    raw.mkdir(parents=True, exist_ok=True)
    manifest = corpus / "manifest.jsonl"
    known = prior_hashes(manifest)

    docs = seed["documents"]
    if args.only:
        docs = [d for d in docs if d["id"] in set(args.only)]

    failures = 0
    with manifest.open("a", encoding="utf-8") as log:
        for doc in docs:
            did = doc["id"]
            dest = raw / f"{did}.pdf"
            res = fetch(doc["url"], dest)

            ok = res["http_status"] == "200" and dest.exists() and dest.stat().st_size > 0
            digest = sha256(dest) if ok else None

            # A served HTML error page can be 200. Sniff the magic bytes.
            magic = ""
            if ok:
                with dest.open("rb") as fh:
                    magic = fh.read(5).decode("latin-1", "replace")
                if not magic.startswith("%PDF"):
                    ok = False

            change = None
            if digest and did in known and known[did] != digest:
                change = {"previous_sha256": known[did], "note":
                          "SOURCE CHANGED between fetches - investigate before use"}

            rec = {
                "id": did,
                "title": doc["title"],
                "institution": doc["institution"],
                "type": doc["type"],
                "oath": doc.get("oath"),
                "event_date": doc.get("event_date"),
                "doc_date": doc.get("doc_date"),
                "release_date": doc.get("release_date"),
                "url": doc["url"],
                "retrieved_utc": utcnow(),
                "ok": ok,
                "magic": magic,
                "sha256": digest,
                "path": str(dest.relative_to(corpus)) if ok else None,
                "role": doc.get("role"),
                **res,
            }
            if change:
                rec["source_change"] = change

            log.write(json.dumps(rec, ensure_ascii=False) + "\n")
            log.flush()

            if ok:
                print(f"[ok]   {did:28} {res['bytes']:>10} B  {digest[:16]}")
                if change:
                    print(f"       !! SOURCE CHANGED vs previous fetch: {change['previous_sha256'][:16]}")
            else:
                failures += 1
                print(f"[FAIL] {did:28} status={res['http_status']} "
                      f"type={res['content_type']} magic={magic!r}")
                if dest.exists() and not digest:
                    dest.unlink(missing_ok=True)

    print(f"\n{len(docs) - failures}/{len(docs)} retrieved. Manifest: {manifest}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
