# 07 — Phase A and B1 First Pass: Execution Report

> Phase A (instrumentation) executed and verified. Phase B1 (citation genealogy) partially verified: **the note-segmentation layer passed its checks; the source-classification layer failed its hand-check and its counts are therefore not reported as results.**

Session date: **19 September 2026**. Reporting format per [`04`](04-methodology-symmetric-skepticism.md) §6.

**No claim status changed and no register entry was created.** Documents were retrieved and machine-extracted; extraction is not reading (`04` §2.4), and none of the sixteen documents has yet been read under a document card.

---

## 1. What was built

| Component | File | State |
|---|---|---|
| Seed corpus definition, with the three dates per document | [`../tools/seed_corpus.json`](../tools/seed_corpus.json) | 16 documents |
| Harvest with provenance and change detection | [`../tools/harvest.py`](../tools/harvest.py) | **16/16 retrieved** |
| Extraction, OCR and per-page quality scoring | [`../tools/extract.py`](../tools/extract.py) | **1,649 pages** |
| Citation-genealogy parser | [`../tools/endnotes.py`](../tools/endnotes.py) | parsing verified; classification not |
| Provenance database | `corpus/pages.db` | one row per page |
| Reproducibility record | [`../REPRODUCIBILITY.md`](../REPRODUCIBILITY.md) | scripts + hashes committed |

### 1.1 Corpus as built

| Metric | Value |
|---|---|
| Documents retrieved | 16 of 16 |
| Pages extracted | 1,649 |
| Characters of text | 4,349,282 |
| Pages requiring OCR | 82 (5.0%) |
| Page images retained for verification | every OCR'd page |
| Raw PDFs | 37 MB |

Every document carries URL, retrieval timestamp, HTTP status, byte count and SHA-256 in `corpus/manifest.jsonl`. A re-fetch yielding a different hash is logged as a `source_change` event rather than silently overwriting, because a primary source changing under the audit is itself evidence.

### 1.2 The OCR blocker is retired

The 6 August 2001 PDB carried **2 characters** of embedded text across the whole file — the original diagnosis in `02` (DOC-6) was correct. Rasterised at 300 dpi and OCR'd, both pages scored `good` for 2,962 characters. Page images are retained so that decisive passages can be checked against the image before any quotation.

`JI-2002` needed OCR on 79 of 838 pages; 69 pages scored `poor` and are flagged in `pages.db` as requiring image verification before use.

---

## 2. Findings that challenge or weaken the official account

**None. No source was read.**

This section is empty by design, not by omission. Phase A is instrumentation; it produces no evidentiary findings and cannot. Recording the emptiness explicitly is required by `04` §6 and is a guard against a phase quietly presenting machinery as results.

One **structural** observation, which is a fact about the project rather than about the record: the nine ISCAP memoranda that three prior sessions recorded as blocked and unread total **454 pages and 494,000 characters, all with intact text layers**. `MFR-TENET-20031223` — the first interview of the most central witness in the intelligence track — is **three pages**. What was recorded as a blocked phase was a few hours of reading behind a network policy and a missing OCR tool.

---

## 3. Findings that challenge or weaken alternative accounts

**None. No source was read.** Same reasoning as §2.

---

## 4. What remains unresolved

### 4.1 The B1 classification layer failed verification

This is the substantive result of the session, and it is a negative one.

**What passed.** Note segmentation is sound, on three independent checks:

| Check | Result |
|---|---|
| Notes parsed | **1,657** across **13 chapters** |
| Sequence completeness — endnotes run 1..N without gaps, so `count == max` per chapter | **zero gaps in all 13 chapters** |
| Agreement between the section ordinal (derived from note numbering) and the running head (derived from the page image) — two independent signals | **92.5%**; the residual is fully accounted for by chapter boundaries falling mid-page |

Getting there required fixing three real defects, each of which had silently destroyed data:

1. Notes pages whose running head did not survive extraction were being **dropped**, removing four chapters from the output entirely.
2. Chapter boundaries fall **in the middle of pages**, so a head-driven note counter rejected every note of each new chapter and never recovered. Chapter 2 came out with 7 notes instead of 93.
3. A **numbered list inside a note** (enumerated muscle-hijacker candidates in the chapter 7 notes) parsed as a 14th chapter. It is now folded back, and the fold is recorded in the output rather than applied silently.

**What failed.** Fragment-level source classification. Scored by hand against two independent random samples of 40 citation fragments each:

| Sample | Disagreement with the machine label |
|---|---|
| Development sample (seed 911) | **16/40 — 40.0%** |
| Held-out sample (seed 2001), after fixes | **15/40 — 37.5%** |

Two rounds of correction moved precision by 2.5 points. **The aggregate counts are therefore not reported here as results**, and nothing in this repository may cite them. Publishing a distribution of source types at ~62% label precision would be exactly the failure mode pre-registered in [`06` §5](06-research-program.md): quantified nonsense wearing the authority of a computation.

**Characterised failure modes**, which is what makes the negative result useful:

| Failure | Effect |
|---|---|
| `ibid.` classified as *Commission analysis* | `ibid.` is a back-reference to the previous citation. It must be **resolved** to that citation, not labelled |
| FBI reports of investigation ("interview of X", i.e. a 302) merged with *Commission interview* | Conflates a contemporaneous investigative record with a 2003–04 Commission recollection — the exact distinction `04` §2.2 exists to preserve |
| DOJ Inspector General interviews merged with *Commission interview* | Another investigation's work counted as the Commission's |
| Mixed fragments | The splitter does not isolate one source per fragment, so first-match-wins picks arbitrarily among two or three cited sources |
| Press and journals not on the outlet list | Fall through to *unclassified* or, worse, to *contemporaneous_document* |
| Date-only fragments (e.g. "Sept. 25, 2003") not folded | The orphan rule missed four-letter month abbreviations |
| **False positives in `detainee_report`** | The most consequential category in the whole design, and it is over-matching as well as under-matching |

One fix was substantive rather than cosmetic and is worth recording: **line-break hyphenation in the source PDF** ("interro- gation", "inter- view") defeated every keyword pattern. Before repair, detainee-derived citations were being systematically **undercounted**. Had the first-pass numbers been published, they would have understated precisely the quantity the B2 census exists to measure.

### 4.2 The design correction this implies

Multi-class labelling of fragments is the wrong instrument. The question the audit actually needs answered is binary and note-level:

> Does this note cite a detainee interrogation report — yes or no?

A high-recall detector over whole notes, with **every positive hand-verified**, gives a defensible count. A nine-way classifier over imperfectly split fragments does not. B1 is re-scoped accordingly before it runs again.

### 4.3 Still open from earlier phases

Unchanged: claims A1–A16 in [`03` §5.1](03-phase2a-mfr-verification.md); determinations 5a–5d; every T-item in [`05`](05-stress-test-execution-plan.md). The corpus now sits under them, but nothing has been read.

---

## 5. What evidence would change the assessment

| Item | What it would settle | Availability |
|---|---|---|
| The nine ISCAP memoranda, read under document cards | Claims A1–A5 and targets T-2.2, T-2.5 | **In the corpus, text extracted, 454 pages** |
| The 6 August 2001 PDB, OCR checked against page images | A10, A16, T-1.1, T-1.2 — stuck for three sessions | **In the corpus, OCR'd, images retained** |
| `ISCAP-PDBREVIEW` re-read for signatures, addressee, distribution list | Determinations 5a and 5b | **In the corpus** |
| A hand-verified note-level detainee-citation detector | Whether the B2 census is feasible at all | Needs §4.2 rebuild |
| Joint Inquiry Part Four under the `03` §6.2 instrument | T-5.1, and H2/H3 | **In the corpus, 34 pages** |

---

## 6. Register health checks

| Check | Result |
|---|---|
| Anomaly register balance | 0 official / 0 alternative — both registers empty, as expected for an instrumentation phase |
| Mirror tests pending | 0 |
| Promotion check | No synthesis text cites any register entry; none exists |
| Resolution rate | n/a |
| Escalation discipline | n/a |
| Targeting audit | No entries created, so no post-hoc target selection was possible |

---

## 7. Reproducibility record

```
python3 -m venv .venv && .venv/bin/pip install pypdf pdfplumber
apt-get install -y tesseract-ocr poppler-utils
.venv/bin/python tools/harvest.py
.venv/bin/python tools/extract.py
.venv/bin/python tools/endnotes.py --sample 40 --seed 2001
```

`corpus/manifest.jsonl` carries a SHA-256 for every file, so a third party can verify they hold the same bytes this audit read. The corpus itself is not committed (37 MB of raw PDFs, 48 MB of page images); it is reconstructible from the scripts and the manifest. Environment: tesseract 5.3.4, poppler 24.02, pypdf 6.19, Python 3.11.

---

## 8. What this session does not permit us to conclude

- Nothing about 9/11. No source was read as evidence.
- Nothing from the B1 counts. They are unpublished for cause, and the cause is measured, not asserted.
- Nothing from the fact that the nine memoranda proved short and readable. That is a fact about this project's prior constraints, not about their contents.
- The note-segmentation checks establish that the parser recovers the report's citation structure. They say nothing whatever about whether the cited sources support what the report says — which is the actual question, and remains untouched.
