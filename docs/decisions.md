# Methodological Decisions Log

Dated record of decisions that change how the audit works. Each entry states what was decided, why, and what it invalidates. Entries are append-only; a superseded decision is marked, never deleted.

---

## D-001 — B1 is an unvalidated instrument and stays that way (2026-09-19)

**Decision.** The B1 citation-classification layer is registered as **not validated**. Its numeric distributions may not be reused, republished, cited or quoted anywhere in this project, including in passing.

**Basis.** Hand-scored against two independent random samples of 40 citation fragments: 40.0% disagreement (seed 911) and 37.5% (seed 2001, held out, after two rounds of fixes). Failure modes in [`07`](07-phase-a-b1-first-pass.md) §4.1.

**What remains valid.** Only the note **segmentation**: 1,657 notes, 13 chapters, zero sequence gaps, 92.5% agreement with the independent running-head signal. Segmentation may be relied on; classification may not.

**Invalidates.** Every count in `corpus/analysis/b1_summary.json` under `fragments_by_kind`, `notes_resting_on_a_single_kind` and `by_chapter`. The file retains them only so the failure is inspectable, and carries a caveat field saying so.

---

## D-002 — B2 re-scoped to a note-level binary, then split in two (2026-09-19)

**Decision as approved.** The B2 unit is the complete note, and the question is binary: *does this note cite or reference interrogation- or detention-derived reporting, yes or no?* Every positive is hand-verified and carries an exact page/note citation.

**Amendment arising from the first two readings.** A single binary conflates two different things and would produce a misleading census. Reading `MFR-TENET-20031223` made this concrete: the document discusses detainee access at length and draws **no factual conclusion** from detainee reporting. A one-column binary would score it identically to a claim about the plot sourced entirely to a detainee.

The census therefore keeps **two columns, never totalled together**:

| Column | Definition |
|---|---|
| **B2-ref** | The text mentions or discusses interrogation/detention-derived reporting |
| **B2-rely** | A factual proposition in the text **rests** on interrogation/detention-derived reporting |

**Third distinction, also mandatory.** Source subtype is recorded and never merged:

| Subtype | Example found |
|---|---|
| CIA detention-and-interrogation programme | none yet |
| Custodial / cooperating-witness statement to the FBI | `PDB-20010806` P5 — Ahmed Ressam's statements to the FBI |
| Foreign-service report of a detained person's statements | none yet |

A convicted defendant's statements to the FBI under domestic legal process and a detainee's statements under the CIA programme have different reliability problems and different legal postures. Totalling them would destroy the census's meaning in the direction of overstatement.

**Status so far.** `PDB-20010806`: B2-ref yes, B2-rely **yes** (custodial/cooperating-witness). `MFR-TENET-20031223`: B2-ref yes, B2-rely **no**.

---

## D-003 — `text-layer` does not mean verified text (2026-09-19)

**Problem found.** `corpus/pages.db` records an extraction method of `text-layer` for every ISCAP memorandum, which was read as meaning born-digital text needing no image check. It does not. The ISCAP PDFs ship with a text layer that is **itself OCR, produced by the releasing agency**, with visible character errors — in `MFR-TENET-20031223`: "Lwicheon" for Luncheon, "infonnation" for information, "fmn" for firm, "rivc:lcd" for riveted, "S to l 5" for 5 to 15.

**Decision.** Image verification of decisive passages is required for agency-OCR'd text layers exactly as for text this project OCRs itself. The absence of `method='ocr'` in the database is **not** a licence to quote without checking.

**Consequence for the tooling.** `extract.py`'s quality model must distinguish born-digital text from an embedded OCR layer — detectable by PDF producer metadata, by the presence of a scanned image on the page, and by character-error signatures. Until it does, **every** quotation from any document in this corpus is image-verified, and the cards record that it was.

**What this does not invalidate.** Nothing already read: both documents read to date were verified against page images before quotation.

---

## D-004 — Corpus-state correction, recorded as such and nothing more (2026-09-19)

**Fact.** Material previously recorded in this repository as inaccessible — the nine ISCAP memoranda and the 6 August 2001 PDB — was available and readable. The memoranda total 148 pages with text layers; the PDB required OCR that this environment can now perform.

**Decision.** This is registered **solely as a correction to the state of the corpus record**. It is a fact about this project's prior constraints and about a network policy, and it is not evidence of anything about the 9/11 record, the documents' contents, or any hypothesis. It may not be cited in any substantive context, and neither the existence, the size, nor the unblocking of these documents is to be treated as a finding.

Superseded entries: the ⚫ access markings for these documents in `SOURCES.md`, and the blockade notes in `03` §3 and `NEXT-STEPS.md`.

---

## D-005 — Reading order follows evidentiary value, not document size (2026-09-19)

**Decision.** The reading queue is ordered by what a document can settle, not by how quickly it can be processed. Page counts are recorded in the log for planning only and are never reported as progress.

**Basis.** Rule 6 of the standing instruction: the criterion is quality of evidence, not quantity processed. `MFR-TENET-20031223` is three pages and bears on ST-4 and the B2 design; `MFR-TENET-20040122` is twenty-four pages and may bear on nothing in the current target set. Neither fact is known before reading, and neither is a result.
