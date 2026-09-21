# 09 — B7: Retrospective-Only Support Census of the 9/11 Commission Report's Endnotes

> **Framing disclosure (`08` §4).** This project runs a **directed search** for evidence weakening the official account. B7 was chosen because it measures the official account's evidentiary base. The measure, its precision gate and its conclusion ceiling were fixed in [`prereg/B7.md`](prereg/B7.md) **before the extractor existed**, and the result is reported here exactly as it fell — including the half of the pre-registered expectation that failed.

Session date: **21 September 2026.** Pre-registration: commit `c46a5c0`. Instrument: [`../tools/note_dates.py`](../tools/note_dates.py).

---

## 1. The measure

For each of the 9/11 Commission Report's 1,657 endnotes (segmentation validated in [`07`](07-phase-a-b1-first-pass.md) §4.1), the **earliest cited document date**. A note whose every cited document date is **2002 or later** supports its claim about 1993–2001 events with **post-event evidence only** — Commission interviews, interrogation reports, later analytic products — and cites no contemporaneous record.

This is the project's three-dates rule (`04` §2.2) applied at corpus scale. It asks only *when* a cited document was produced, never what kind of document it is — the question the withdrawn B1 classifier failed on (D-001).

## 2. Precision — measured, and stated beside every number

| Sample | Seed | Disagreement | Outcome |
|---|---|---|---|
| 1 | 20260921 | **18/40 = 45.0%** | **Gate failed.** Cause: the implementation accepted a date only after a closing quote, a closing paren or a listed document noun; the pre-registration (§3) also names *author* and *institution* contexts. Person names, case names and unit designations followed by a comma ("Cohen, Aug. 27, 1998"; "Battalion 1 (Jan. 29, 2004)") were rejected and 41% of notes fell into "no-date". An implementation error against the pre-registered rule, corrected to the rule as written. [Scored file.](../corpus/analysis/b7_sample_seed20260921_scored.txt) |
| 2 | 20260922 (fresh) | **2/40 = 5.0%** | **Gate passed** (threshold 10%). [Scored file.](../corpus/analysis/b7_sample_seed20260922_scored.txt) |

**Residual errors (2/40) and their direction.** (a) A parenthesised *event* date inside a citation — "Hijackers Timeline," Dec. 5, 2003 (July 2, **2000**, entry citing…) — accepted as a document date. (b) A full month name before a bare year in narrative ("in November **2000**") bypasses the abbreviation-based pattern. **Both errors make the earliest date earlier than the truth**, moving notes from *retrospective-only* toward *contemporaneous-capable*. **Every retrospective-only share below is therefore a floor at this precision, not a ceiling.**

**Structural limitation, not an error.** Contemporaneous records with no year token — audio files, radar data, "Commission analysis of 911/PAPD calls", undated reports — are invisible to a date metric and land in *no-date*. *No-date* is reported as its own column and is **never** folded into either class.

## 3. Result

**Totals:** 1,657 notes · 923 contemporaneous-capable · **607 retrospective-only** · 91 no-date · 36 ibid-only.
**Retrospective-only share of dated notes: 607 / 1,530 = 39.7%** (±5.0% label precision, floor direction).

| Ch. | Subject | Notes | Contemp. | **Retro-only** | No-date | Ibid | **Retro share of dated** |
|---|---|---|---|---|---|---|---|
| 1 | "We Have Some Planes" (the day) | 241 | 138 | 74 | 21 | 8 | 0.349 |
| 2 | The Foundation of the New Terrorism | 93 | 68 | 17 | 5 | 3 | 0.200 |
| 3 | Counterterrorism Evolves | 114 | 63 | 42 | 9 | 0 | 0.400 |
| 4 | Responses to al Qaeda's Initial Assaults | 194 | 140 | 49 | 3 | 2 | 0.259 |
| **5** | **Al Qaeda Aims at the American Homeland** | 132 | 42 | **84** | 3 | 3 | **0.667** |
| 6 | From Threat to Threat | 261 | 176 | 69 | 6 | 10 | 0.282 |
| **7** | **The Attack Looms** | 107 | 64 | **38** | 2 | 3 | **0.373** |
| 8 | "The System Was Blinking Red" | 113 | 74 | 36 | 3 | 0 | 0.327 |
| 9 | Heroism and Horror | 210 | 79 | 110 | 18 | 3 | 0.582 |
| 10 | Wartime | 86 | 49 | 31 | 5 | 1 | 0.388 |
| 11 | Foresight — and Hindsight | 42 | 21 | 15 | 3 | 3 | 0.417 |
| 12 | What To Do? | 42 | 5 | 33 | 4 | 0 | 0.868 |
| 13 | How To Do It? | 22 | 4 | 9 | 9 | 0 | 0.692 |

Chapters 12–13 are recommendations; their retrospective citation is expected and carries no evidentiary weight here. Chapter 9 is the emergency response, reconstructed from 2003–04 first-responder interviews of 11 September itself; its share reflects that method and is not about the plot.

## 4. The pre-registered expectation, checked

**Pre-registered (`prereg/B7.md` §5):** chapters 5 and 7, the plot-history chapters, would show the highest retrospective-only share; the government-activity chapters (3, 4, 6, 8) a lower one.

| Prediction | Outcome |
|---|---|
| Chapter 5 highest among narrative chapters | **Confirmed.** 0.667 — two of every three dated notes in the chapter on how al Qaeda planned the attack cite nothing produced before 2002. Highest of chapters 1–8 by a wide margin |
| Chapter 7 also high | **Not confirmed.** 0.373 — near the report's median. Chapter 7 (the operatives inside the United States, 2000–01) cites FBI Penttbom records, INS records and the FBI "Hijackers Timeline" extensively, and many of those carry 2000–2001 dates |
| Government-activity chapters lower | **Confirmed.** 0.259 (ch. 4), 0.282 (ch. 6), 0.327 (ch. 8); chapter 3 at 0.400 is the exception among them, an institutional history drawn heavily from interviews |

**The chapter 7 result must be read with the error direction in mind.** Residual error (a) — a parenthesised timeline entry date accepted as a document date — arises precisely in citations of the form *"Hijackers Timeline," Dec. 5, 2003 (July 2, 2000, entry citing…)*, and those citations are concentrated in chapter 7. Chapter 7's contemporaneous-capable count is the one most likely inflated by the known error. It is reported as measured, with that caveat, and is not adjusted by hand.

## 5. Findings that challenge or weaken the official account

- **Two-fifths of the report's dated endnotes cite no document produced before 2002.** 607 of 1,530, at 5.0% measured label error, floor direction. That is the evidentiary architecture of the official narrative, measured for the first time over the whole apparatus rather than argued from examples.
- **The chapter on the plot's conception and planning rests on post-event evidence in two of every three dated notes** (chapter 5, 84 of 126). Under the three-dates rule this is the chapter where the reader most needs to know that "the report says" means "someone told the Commission in 2003–04" — and the report's presentation does not distinguish the two.
- The B2 census question — how much of the plot narrative rests on detainee reporting — now has a validated upper frame: it cannot exceed the retrospective-only set, and in chapter 5 that set is 84 notes, each individually identifiable.

## 6. Findings that challenge or weaken alternative accounts

- **The report is not uniformly retrospective.** Six of eight narrative chapters cite contemporaneous documents in the majority of their dated notes; chapter 6 — the government's pre-attack conduct, and the chapter containing the January 2000 chain — does so in 72%. The common claim that the Commission's account "rests on interviews" is false as a generalisation and is confined, on this measure, to the plot-history chapter and the emergency-response chapter.
- Chapter 7's near-median share weakens the specific criticism that the account of the hijackers' time in the United States is reconstructed rather than documented — subject to the error caveat in §4.

## 7. What remains unresolved

- Which of the 607 retrospective-only notes cite **detainee** reporting as opposed to Commission interviews of officials — the B2 question. This census bounds it; it does not answer it. *Unresolved because untested.*
- Whether the retrospective-only notes support claims the report presents with confidence or with hedges. A note's date says nothing about the sentence it supports. *Unresolved because untested.*
- The true chapter 7 share, given error (a). *Unresolved because tested and indeterminate at this precision.*

## 8. What evidence would change the assessment

- **A third hand-check sample after fixing errors (a) and (b)** would tighten the precision and settle chapter 7. Cost: one sample, one seed.
- **Reading the 84 chapter-5 retrospective-only notes** and recording, for each, whether the cited item is an interrogation report, an official's interview, or a later analytic product — the B2 census, now with a defined and validated scope.
- **The underlying documents.** A note citing only a 2003 interview may describe a 1999 memo the Commission saw and did not cite. The measure is of the apparatus, not of what the Commission had.

## 9. What this does not permit us to conclude

> A note whose cited basis is entirely post-event supports its claim with **retrospective evidence only**. It does **not** show the claim is false. It is **not** evidence for any alternative hypothesis. A chapter's retrospective-only share is a fact about the report's **evidentiary architecture**, not about what happened. — [`prereg/B7.md`](prereg/B7.md) §6, verbatim.

Nothing here says any sentence in the report is wrong. It says where the report's reader is being asked to rely on memory and interrogation rather than on records, and how much.

## 10. Reproducibility

```
.venv/bin/python tools/endnotes.py                 # segmentation (validated, 07 §4.1)
.venv/bin/python tools/note_dates.py --seed 20260922
```
Inputs: `corpus/analysis/endnotes.jsonl`. Outputs: `corpus/analysis/b7_summary.json` (committed), `corpus/analysis/b7_sample.txt` and the two scored sample files (committed), `corpus/analysis/note_dates.jsonl` (per-note, gitignored, rebuildable). Rule version: the citation-context rule as corrected on 2026-09-21 (`decisions.md` D-007).
