#!/usr/bin/env python3
"""Phase B1 (first pass) - citation genealogy of the 9/11 Commission Report.

Parses the report's endnotes, splits each note into its cited sources, and
classifies every source by type. The output is the evidentiary structure of the
official account: which claims rest on contemporaneous documents, which on
Commission interviews, which on detainee interrogation reports, and which on
the Commission's own analysis.

THIS IS A MEASURING INSTRUMENT, NOT A FINDING. A thin citation chain shows
that a claim rests on a thin evidentiary base. It does not show the claim is
false and is not evidence for any alternative hypothesis (docs/06 section 3,
B1 conclusion ceiling).

Classification is by regular expression and is therefore approximate. Precision
is measured by hand-checking a random sample; the disagreement rate is reported
with the results and must be published alongside any use of them.

Usage:
    python3 tools/endnotes.py [--corpus DIR] [--sample N]

Outputs:
    <corpus>/analysis/endnotes.jsonl   one record per note
    <corpus>/analysis/citations.jsonl  one record per cited source
    <corpus>/analysis/b1_summary.json  aggregate counts
    <corpus>/analysis/b1_sample.txt    random sample for hand-checking
"""

import argparse
import json
import pathlib
import random
import re
import sys
from collections import Counter, defaultdict

DOC_ID = "CR-2004"
HEADER = re.compile(r"NOTES?\s+TO\s+(?:CHAPTERS?\s+(\d+)|(APPENDIX)\w*)", re.I)
# A note starts at line-begin with "12." or "12 ." possibly indented.
NOTE_START = re.compile(r"^\s{0,12}(\d{1,3})\s?\.\s*(?=\S)")

# Source-type patterns, applied in order; first match wins for a fragment.
# Ordering matters: detainee reporting must be tested before generic
# "intelligence report", and interviews before generic "report".
PATTERNS = [
    # Detainee reporting is tested first and deliberately broadly: a false
    # negative here understates the most consequential category in the audit.
    ("detainee_report", re.compile(
        r"interrogation|debriefing of|"
        r"(Khalid Sheikh Mohammed|KSM|Ramzi Binalshibh|Bin al-Shibh|Khallad|"
        r"Abu Zubaydah|Hambali|Riduan Isamuddin|al-?Nashiri|al Nashiri|"
        r"Ammar al-?Baluchi|Zubaydah)\b", re.I)),
    ("commission_interview", re.compile(
        r"\binterviews?\b[^.;]{0,40}\(\s*\w+\.?\s*\d|"
        r"\binterviews?\s*\(|\binterview,|"
        r"(?:FDNY|FBI|Civilian|Port Authority|PAPD|NYPD)\s+interview|"
        r"interview (?:of|with) [A-Z]", re.I)),
    ("public_testimony", re.compile(
        r"\btestimony\b|prepared statement|joint inquiry hearing|"
        r"\bhearing (?:of|before|transcript)\b", re.I)),
    ("agency_briefing", re.compile(
        r"\bbriefing\b|briefed the Commission|briefing materials", re.I)),
    ("court_record", re.compile(
        r"United States v\.|\bF\.3d\b|\bF\. Supp\b|trial transcript|"
        r"indictment|government exhibit|evidentiary proffer", re.I)),
    ("contemporaneous_document", re.compile(
        r"\bcable\b|\bmemo\b|memorandum|\be-?mail\b|\bletter\b|\bfax\b|"
        r"talking points|\blog\b|transcript of|electronic communication|"
        r"\bSEIB\b|\bNID\b|\bPDB\b|President's Daily Brief|"
        r"reports? of investigation|\brecord,|computer-aided dispatch|"
        r"video footage|\breport,|\breport\b.{0,40}\b(19|20)\d\d", re.I)),
    ("press_or_book", re.compile(
        r"New York Times|Washington Post|Wall Street Journal|Los Angeles Times|"
        r"Associated Press|\bCNN\b|\bABC\b|\bNBC\b|\bCBS\b|Newsweek|"
        r"The Atlantic|\(McGraw-Hill|\(Random House|\(Simon|\(Free Press|"
        r"Press,\s*\d{4}\)|University Press", re.I)),
    ("commission_analysis", re.compile(
        r"Commission analysis|Commission staff (?:analysis|review|report)|"
        r"see chapter|\bibid\b|\bsee above\b", re.I)),
]

# Fragments that are only a date or a page reference are splitting artefacts,
# not sources. They are folded back into the preceding fragment.
ORPHAN = re.compile(
    r"^(?:pp?\.\s*[\d–\-,\s]+|[A-Z][a-z]{2}\.?\s*\d{1,2},?\s*(?:19|20)\d\d[.,)\s]*|"
    r"\(?\s*(?:19|20)\d\d\s*\)?[.,)\s]*|ibid\.?[\d\s,.pp–\-]*)$", re.I)

# A citation carries at least one of: a year, a quoted title, or a source noun.
CITATION_SIGNAL = re.compile(
    r"\b(?:19|20)\d\d\b|[“”\"]|\binterview|\breport|\bmemo|\bcable|"
    r"\btestimony|\bbriefing|\bv\.\s|\bibid\b|Commission analysis", re.I)

FRAGMENT_SPLIT = re.compile(r";\s+|(?<=\.)\s+(?=See\s|see\s)")

DEHYPHEN = re.compile(r"(\w)[‐-―-]\s+(\w)")

# A real chapter's notes run to at least this many. Anything shorter that looks
# like a section is a numbered list inside a note (the report has several, e.g.
# the enumerated muscle-hijacker candidates in the chapter 7 notes), not a new
# chapter. Such runs are merged back into the preceding note.
MIN_SECTION_NOTES = 10


def load_pages(corpus: pathlib.Path):
    d = corpus / "text" / DOC_ID
    pages = []
    for p in sorted(d.glob("p*.txt")):
        pages.append((int(p.stem[1:]), p.read_text(encoding="utf-8", errors="replace")))
    return pages


def notes_region(pages):
    """The contiguous run of pages from the first to the last notes page.

    Pages inside the run that carry no running head are KEPT: they are notes
    pages whose header did not survive extraction, and dropping them silently
    loses their notes. Earlier versions of this parser dropped them, which
    removed four chapters from the output entirely.
    """
    hdr = [num for num, body in pages if HEADER.search(body)]
    if not hdr:
        return []
    lo, hi = min(hdr), max(hdr)
    return [(num, body) for num, body in pages if lo <= num <= hi]


def page_chapters(region):
    """Chapter label per page: the page's own running head, else the previous
    page's. Working at page granularity rather than line granularity stops the
    thrash that facing-page running heads otherwise cause."""
    out, cur = [], None
    for pnum, body in region:
        m = HEADER.search(body)
        if m:
            cur = m.group(1) or "appendix"
        out.append((pnum, cur, body))
    return out


def parse_notes(region):
    """Yield (section, note_number, header_label, text, first_page, last_page).

    Chapter boundaries fall in the MIDDLE of pages, so the running head cannot
    drive the counter: on the page where chapter N ends and N+1 begins, a
    head-driven counter rejects every note of the new chapter and never
    recovers. An earlier version of this parser lost four chapters that way.

    The note numbers themselves are the reliable signal. Endnotes run 1..N
    strictly, so:
      - a line starts a new note if its number is exactly prev + 1;
      - a line numbered 1 after a larger number is a new section.
    `section` is the resulting ordinal (1, 2, 3, ...). The running head seen on
    the page is carried alongside as `header_label` and is used only to check
    the result, never to produce it.
    """
    section = 0
    prev_no = 0
    cur = None  # (section, no, label, lines, pages)

    def flush():
        if cur is None:
            return None
        s, no, lbl, lines, pgs = cur
        return (s, no, lbl, "\n".join(lines).strip(), min(pgs), max(pgs))

    for pnum, label, body in page_chapters(region):
        for ln in body.splitlines():
            if HEADER.search(ln):
                continue  # running head is never note text
            m = NOTE_START.match(ln)
            n = int(m.group(1)) if m else None
            is_next = n is not None and n == prev_no + 1
            is_reset = n == 1 and prev_no > 1
            if is_next or is_reset:
                out = flush()
                if out:
                    yield out
                if is_reset or section == 0:
                    section += 1
                prev_no = n
                cur = (section, n, label, [ln[m.end():]], [pnum])
            elif cur is not None:
                cur[3].append(ln)
                cur[4].append(pnum)
    out = flush()
    if out:
        yield out


def merge_spurious_sections(raw):
    """Fold short pseudo-sections back into the preceding note.

    Returns (notes, merges) where `merges` records every fold so the
    correction is visible rather than silent, and renumbers sections
    consecutively from 1.
    """
    by_section = defaultdict(list)
    for rec in raw:
        by_section[rec[0]].append(rec)
    order = sorted(by_section)

    kept, merges = [], []
    for s in order:
        items = sorted(by_section[s], key=lambda r: r[1])
        if len(items) >= MIN_SECTION_NOTES or not kept:
            kept.append(items)
        else:
            absorbed = " ".join(r[3] for r in items)
            prev = kept[-1]
            last = list(prev[-1])
            last[3] = (last[3] + " " + absorbed).strip()
            last[5] = max(last[5], max(r[5] for r in items))
            prev[-1] = tuple(last)
            merges.append({
                "folded_section_ordinal": s,
                "notes_folded": len(items),
                "pages": [min(r[4] for r in items), max(r[5] for r in items)],
                "into": {"section": prev[-1][0], "note": prev[-1][1]},
                "reason": ("numbered list inside a note, not a chapter "
                           f"(fewer than {MIN_SECTION_NOTES} notes)"),
            })

    out = []
    for i, items in enumerate(kept, 1):
        for r in items:
            out.append((i, r[1], r[2], r[3], r[4], r[5]))
    return out, merges


def classify(fragment: str) -> str:
    if not CITATION_SIGNAL.search(fragment):
        # Explanatory prose inside a note, not a cited source. Counting it as
        # "unclassified" inflated that bucket and hid real classifier failures.
        return "not_a_citation"
    for label, rx in PATTERNS:
        if rx.search(fragment):
            return label
    return "unclassified"


def split_fragments(flat: str) -> list:
    """Split a note into cited sources, folding date-only artefacts back.

    Line-break hyphenation in the source PDF ("interro- gation", "inter-
    view") defeats every keyword pattern, so it is repaired first. That defect
    alone produced false negatives in the detainee-report category, which is
    the category the audit is least willing to understate.
    """
    flat = DEHYPHEN.sub(r"\1\2", flat)
    out = []
    for f in FRAGMENT_SPLIT.split(flat):
        f = f.strip()
        if not f:
            continue
        if ORPHAN.match(f) and out:
            out[-1] = (out[-1] + " " + f).strip()
        else:
            out.append(f)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    here = pathlib.Path(__file__).resolve().parent
    ap.add_argument("--corpus", default=str(here.parent / "corpus"))
    ap.add_argument("--sample", type=int, default=40)
    ap.add_argument("--seed", type=int, default=911)
    args = ap.parse_args()

    corpus = pathlib.Path(args.corpus)
    outdir = corpus / "analysis"
    outdir.mkdir(parents=True, exist_ok=True)

    pages = load_pages(corpus)
    region = notes_region(pages)
    if not region:
        print("No notes pages found - has CR-2004 been extracted?", file=sys.stderr)
        return 1

    parsed, merges = merge_spurious_sections(list(parse_notes(region)))

    notes, cites = [], []
    for chap, no, label, text, p0, p1 in parsed:
        flat = re.sub(r"\s+", " ", text).strip()
        if not flat:
            continue
        frags = split_fragments(flat)
        kinds = []
        for f in frags:
            k = classify(f)
            kinds.append(k)
            cites.append({"chapter": chap, "note": no, "kind": k,
                          "fragment": f[:400], "pages": [p0, p1]})
        notes.append({
            "chapter": chap, "header_label": label, "note": no, "pages": [p0, p1],
            "n_fragments": len(frags),
            "kinds": sorted(set(kinds)),
            "kind_counts": dict(Counter(kinds)),
            "sole_kind": kinds[0] if len(set(kinds)) == 1 else None,
            "text": flat[:1200],
        })

    (outdir / "endnotes.jsonl").write_text(
        "\n".join(json.dumps(n, ensure_ascii=False) for n in notes) + "\n",
        encoding="utf-8")
    (outdir / "citations.jsonl").write_text(
        "\n".join(json.dumps(c, ensure_ascii=False) for c in cites) + "\n",
        encoding="utf-8")

    kind_counts = Counter(c["kind"] for c in cites)
    sole = Counter(n["sole_kind"] for n in notes if n["sole_kind"])
    per_chapter = defaultdict(Counter)
    for c in cites:
        per_chapter[c["chapter"]][c["kind"]] += 1

    # Completeness self-check. Endnotes run 1..N without gaps, so for each
    # chapter the count parsed must equal the highest number parsed. Any
    # shortfall is a parser defect and is reported rather than hidden.
    seen = defaultdict(set)
    for n in notes:
        seen[n["chapter"]].add(n["note"])
    completeness, defects = {}, []
    for chap, nums in seen.items():
        hi, cnt = max(nums), len(nums)
        missing = sorted(set(range(1, hi + 1)) - nums)
        completeness[chap] = {"parsed": cnt, "highest": hi,
                              "missing_count": len(missing),
                              "missing_first_20": missing[:20]}
        if missing:
            defects.append(chap)

    # Independent check: the section ordinal is derived from note numbering
    # alone. The running head is derived from the page image. Where they
    # disagree, the parse is suspect. The agreement rate is published.
    agree = sum(1 for n in notes if str(n["chapter"]) == str(n["header_label"]))
    labelled = sum(1 for n in notes if n["header_label"] is not None)

    summary = {
        "document": DOC_ID,
        "notes_region_pages": [region[0][0], region[-1][0]],
        "spurious_sections_merged": merges,
        "section_vs_header_agreement": {
            "notes_with_a_header_label": labelled,
            "agreeing": agree,
            "rate": round(agree / labelled, 3) if labelled else None,
            "note": ("Section ordinal comes from note numbering; header label "
                     "comes from the running head. Disagreement marks a "
                     "mid-page chapter boundary or a misread head."),
        },
        "completeness_by_chapter": dict(
            sorted(completeness.items(), key=lambda x: (x[0] == "appendix", x[0]))),
        "chapters_with_gaps": sorted(defects, key=lambda x: (x == "appendix", x)),
        "notes_parsed": len(notes),
        "citation_fragments": len(cites),
        "chapters_seen": sorted(per_chapter, key=lambda x: (x == "appendix", x)),
        "fragments_by_kind": dict(kind_counts.most_common()),
        "notes_resting_on_a_single_kind": dict(sole.most_common()),
        "single_fragment_notes": sum(1 for n in notes if n["n_fragments"] == 1),
        "by_chapter": {k: dict(v.most_common()) for k, v in
                       sorted(per_chapter.items(), key=lambda x: (x[0] == "appendix", x[0]))},
        "caveat": ("Regex classification, first pass. Precision unmeasured until "
                   "the hand-check sample is scored. No claim may be drawn from "
                   "these counts before that."),
    }
    (outdir / "b1_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    rnd = random.Random(args.seed)
    picks = rnd.sample(cites, min(args.sample, len(cites)))
    with (outdir / "b1_sample.txt").open("w", encoding="utf-8") as fh:
        fh.write("B1 hand-check sample. For each line mark AGREE or DISAGREE with\n"
                 "the machine label, then record the disagreement rate in the\n"
                 "phase report. Do not use the aggregate counts before scoring this.\n\n")
        for i, c in enumerate(picks, 1):
            fh.write(f"[{i:02d}] ch{c['chapter']} n{c['note']}  "
                     f"MACHINE={c['kind']}\n     {c['fragment'][:300]}\n\n")

    print(json.dumps(summary, indent=2)[:2400])
    return 0


if __name__ == "__main__":
    sys.exit(main())
