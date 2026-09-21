#!/usr/bin/env python3
"""B7 - retrospective-only support census over the Commission Report endnotes.

For each endnote, find the EARLIEST cited *document* date. A note whose every
cited document date is 2002 or later supports its claim with post-event
evidence only. Pre-registered in docs/prereg/B7.md; the metric, the
citation-context rule and the hand-check gate are fixed there and are not
adjusted here.

Reads the validated note segmentation (corpus/analysis/endnotes.jsonl). Never
touches the withdrawn B1 classifier.

THIS PRODUCES NO RESULT UNTIL THE HAND-CHECK SAMPLE IS SCORED. The summary
file carries that caveat until a scored sample is recorded beside it.

Usage:
    python3 tools/note_dates.py [--corpus DIR] [--sample 40] [--seed N]

Outputs:
    <corpus>/analysis/note_dates.jsonl   one record per note (gitignored)
    <corpus>/analysis/b7_summary.json    per-chapter table, with caveat
    <corpus>/analysis/b7_sample.txt      hand-check sample, to be scored
"""

import argparse
import json
import pathlib
import random
import re
import sys
from collections import Counter, defaultdict

MONTH = r"(?:Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)\.?"
# A full or partial date, capturing the year.
DATE = re.compile(
    rf"(?:{MONTH}\s+\d{{1,2}}(?:[–-]\d{{1,2}})?,?\s*|{MONTH}\s+|"
    rf"(?:spring|summer|fall|autumn|winter)\s+)?((?:19|20)\d\d)\b", re.I)

# Citation-context rule, prereg/B7.md section 3, implemented as written.
#
# FIRST IMPLEMENTATION (scored 2026-09-21, seed 20260921: 45% disagreement,
# gate failed) accepted a date only after a closing quote, a closing paren or
# a listed document-type noun. The pre-registration also names AUTHOR and
# INSTITUTION as valid contexts; that omission threw person names, case names,
# unit designations and subject lines ("Cohen,Aug. 27, 1998"; "Battalion 1
# (Jan. 29, 2004)") into "no-date" - 41% of notes. See
# corpus/analysis/b7_sample_seed20260921_scored.txt.
#
# CURRENT RULE: a date is a document date UNLESS (a) it sits inside a quoted
# title, or (b) the token immediately before it - with no comma or open paren
# between - is a narrative word. Citation dates are preceded by a comma, an
# open paren, or a name/noun; narrative dates by a preposition or qualifier.
NARRATIVE_WORD = re.compile(
    r"(?:\b(?:in|on|since|by|until|before|after|during|of|the|from|to|at|"
    r"around|about|between|through|early|late|mid|year|fiscal|summer|spring|"
    r"fall|autumn|winter|and|or|than|into|over|under|per|as|was|were|is|"
    r"circa|ca)\.?)\s*$", re.I)

# Dates inside a quoted title are event mentions, not document dates.
QUOTE_SPANS = re.compile(r"[“\"][^”\"]{0,300}[”\"]")

IBID = re.compile(r"^\s*(?:see\s+)?ibid\.?", re.I)
HYPHEN = re.compile(r"(\w)[‐-―-]\s+(\w)")

YEAR_MIN, YEAR_MAX = 1900, 2010  # outside this range a 4-digit token is not a year


def document_years(text: str):
    """Years of document dates in a note, applying the citation-context rule."""
    text = HYPHEN.sub(r"\1\2", text)
    inside_quotes = set()
    for m in QUOTE_SPANS.finditer(text):
        inside_quotes.update(range(m.start(), m.end()))
    years, rejected = [], []
    for m in DATE.finditer(text):
        y = int(m.group(1))
        if not (YEAR_MIN <= y <= YEAR_MAX):
            rejected.append((y, "out-of-range"))
            continue
        if m.start() in inside_quotes:
            rejected.append((y, "inside-title"))
            continue
        before = text[max(0, m.start() - 40):m.start()]
        # A comma or open paren immediately before the date marks a citation
        # boundary; only when neither is present can a narrative word reject.
        if re.search(r"[,(]\s*$", before):
            years.append(y)
        elif NARRATIVE_WORD.search(before):
            rejected.append((y, "narrative-context"))
        else:
            years.append(y)
    return years, rejected


def main() -> int:
    ap = argparse.ArgumentParser()
    here = pathlib.Path(__file__).resolve().parent
    ap.add_argument("--corpus", default=str(here.parent / "corpus"))
    ap.add_argument("--sample", type=int, default=40)
    ap.add_argument("--seed", type=int, default=20260921)
    args = ap.parse_args()
    corpus = pathlib.Path(args.corpus)
    src = corpus / "analysis" / "endnotes.jsonl"
    notes = [json.loads(l) for l in src.read_text(encoding="utf-8").splitlines() if l.strip()]

    out, prev_years = [], {}
    for n in notes:
        ch, text = n["chapter"], n["text"]
        rec = {"chapter": ch, "note": n["note"], "pages": n["pages"]}
        if IBID.match(text) and len(text) < 80:
            rec.update(cls="ibid-only", min_doc_year=None,
                       inherited=prev_years.get(ch), doc_years=[], rejected=[])
        else:
            ys, rej = document_years(text)
            # a note that opens with ibid. inherits, then may add its own
            if IBID.match(text) and prev_years.get(ch):
                ys = ys + prev_years[ch]
            rec["doc_years"] = sorted(set(ys))
            rec["rejected"] = rej
            if ys:
                mn = min(ys)
                rec["min_doc_year"] = mn
                rec["cls"] = "retrospective-only" if mn >= 2002 else "contemporaneous-capable"
                prev_years[ch] = ys
            else:
                rec["min_doc_year"] = None
                rec["cls"] = "no-date"
        rec["text"] = text[:600]
        out.append(rec)

    (corpus / "analysis" / "note_dates.jsonl").write_text(
        "\n".join(json.dumps(r, ensure_ascii=False) for r in out) + "\n", encoding="utf-8")

    table = defaultdict(Counter)
    for r in out:
        table[r["chapter"]][r["cls"]] += 1
    rows = {}
    for ch in sorted(table, key=int):
        c = table[ch]
        dated = c["retrospective-only"] + c["contemporaneous-capable"]
        rows[ch] = {
            "notes": sum(c.values()),
            "contemporaneous_capable": c["contemporaneous-capable"],
            "retrospective_only": c["retrospective-only"],
            "no_date": c["no-date"],
            "ibid_only": c["ibid-only"],
            "retrospective_share_of_dated": round(c["retrospective-only"] / dated, 3) if dated else None,
        }
    tot = Counter()
    for c in table.values():
        tot.update(c)
    dated = tot["retrospective-only"] + tot["contemporaneous-capable"]
    summary = {
        "metric": "earliest cited DOCUMENT date per note (prereg/B7.md section 2)",
        "hand_check": {"status": "NOT YET SCORED", "sample": args.sample, "seed": args.seed,
                       "disagreement_rate": None,
                       "gate": "counts are not results until scored; withheld if >10% disagreement"},
        "totals": {"notes": len(out), **{k.replace('-', '_'): v for k, v in tot.items()},
                   "retrospective_share_of_dated": round(tot["retrospective-only"] / dated, 3) if dated else None},
        "by_chapter": rows,
        "caveat": ("NOT A RESULT. The hand-check gate in docs/prereg/B7.md section 4 has not "
                   "been scored. No number here may be cited until it is."),
    }
    (corpus / "analysis" / "b7_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    rnd = random.Random(args.seed)
    dated_notes = [r for r in out if r["cls"] in ("retrospective-only", "contemporaneous-capable", "no-date")]
    picks = rnd.sample(dated_notes, min(args.sample, len(dated_notes)))
    with (corpus / "analysis" / "b7_sample.txt").open("w", encoding="utf-8") as fh:
        fh.write(f"B7 hand-check sample (seed {args.seed}). Question per note: is min_doc_year\n"
                 "correctly identified? Mark AGREE or DISAGREE and give the correct value if\n"
                 "DISAGREE. Score BEFORE any number from b7_summary.json is used anywhere.\n\n")
        for i, r in enumerate(picks, 1):
            fh.write(f"[{i:02d}] ch{r['chapter']} n{r['note']}  MACHINE min_doc_year={r['min_doc_year']}  "
                     f"cls={r['cls']}  doc_years={r['doc_years']}\n"
                     f"     rejected={r['rejected'][:6]}\n     {r['text'][:420]}\n     SCORE: \n\n")
    print(json.dumps({"totals": summary["totals"], "hand_check": summary["hand_check"]}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
