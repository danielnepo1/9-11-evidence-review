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

---

## D-006 — Reorientation: directed search against the official account (2026-09-20)

**Decision.** The project's objective changes from a symmetric audit to a directed search that actively prioritizes evidence weakening the official account. Resources are no longer split evenly across H0–H7; the mandatory "findings that weaken alternative accounts" section becomes optional; H1–H7 mirror testing is de-prioritized.

**User's exact instruction**, given after the tradeoff was stated explicitly and three options were offered: "Reorientar para busca dirigida" — reorient toward directed search, explicitly accepting that this relaxes the requirement to treat H1–H7 with the same standard and that the result is a thesis, not an audit.

**What this does and does not touch.** It changes objective and resource priority only. It does **not** relax any evidentiary-verification mechanism: the document-card standard, image verification, the closed status vocabulary, the evidence-matrix's four-cell requirement, the mirror test, and conclusion ceilings all remain in force, because they are what make a finding resistant to rebuttal — which the new objective needs more, not less. Full record: [`08-reorientation-directed-search.md`](08-reorientation-directed-search.md).

**Consequence.** `NEXT-STEPS.md` execution order is re-prioritized toward T-2.1, T-3.1, T-4.2, T-7.1, T-7.2. `README.md`'s governing-principle framing is banner-updated to point to `08`, with `04` kept as historical record per this log's standing rule against silent edits. No prior finding changes: both document cards read so far recorded no conclusion, and that stands unaltered.

**Invalidates.** The symmetry-based framing in `04` and `README.md` as the *current* governing objective (both are kept as historical/reference documents, not deleted). The register-balance health check in `anomaly-register.md` §6 item 1 is no longer a correction trigger — a one-sided register is now the expected shape of the work.

---

## D-007 — B7 validated at 5.0% after one failed gate; the corrected rule is the pre-registered rule (2026-09-21)

**Decision.** The B7 retrospective-only support census ([`09`](09-b7-retrospective-support-census.md)) is validated and its counts may be cited, each with "5.0% measured label error, floor direction" beside it.

**What happened.** The first extractor run failed its hand-check at **45.0%** (seed 20260921). Diagnosis: the code accepted a date as a document date only after a closing quote, a closing paren or a listed document noun; the pre-registration ([`prereg/B7.md`](prereg/B7.md) §3) also names *author* and *institution* as valid contexts. The omission was an implementation error against the pre-registered rule, not a defect in the rule, and 17 of 18 disagreements traced to it. The rule was implemented as written (accept unless inside a quoted title or preceded, with no comma or paren between, by a narrative word) and re-scored on a **fresh seed** (20260922): **5.0%**.

**Why this is not tuning to the sample.** The correction moved the code *toward* the text committed before any run, not toward the sample; and the validation seed had never been drawn before the correction. Both scored samples are committed.

**Known residual errors, left unfixed and disclosed.** (a) Parenthesised event dates inside citations; (b) full month names before a bare year. Both bias the earliest date *earlier*, so every retrospective-only share is a floor. Fixing them would require a third sample; the measured 5.0% is reported instead.

**Does not touch.** D-001 stands: the B1 *type* classifier remains withdrawn. B7 measures *when*, not *what kind*.

---

## D-008 — a live instance of B7's known residual error found during B2's mandatory spot-check; denominator not amended (2026-09-21)

**What happened.** While image-verifying the B2 chapter-5 spot-check sample (see `11-b2-ch5-census.md`), chapter 5 note 25 was checked incidentally. It reads: "…whereas Hazmi and Mihdhar were on the first leg of their travel from Karachi to Los Angeles, where they would arrive **on January 15, 2000**. Intelligence report, interrogation of KSM, July 31, 2003…" B7 classified this note `contemporaneous-capable` with `min_doc_year=2000`. That is wrong: "January 15, 2000" is a narrative **event** date (when Hazmi and Mihdhar arrived), not a document date; the earliest actual document cited in the note is "Intelligence report, interrogation of detainee, Jan. 22, 2002." Correctly classified, note 25 is `retrospective-only`.

**Root cause, confirmed by direct reproduction.** `tools/note_dates.py`'s `MONTH` pattern only matches abbreviated month names (`Jan`, `Feb`, …). "January" is not matched as a unit, so the date regex falls through to bare-year matching with `m.start()` landing on "2000" itself, preceded immediately by a comma ("January 15, ​2000"). The comma-precedes-date rule fires before the narrative-word rule is checked, so the narrative word "on" three tokens earlier is never seen. **This is the same residual-error class already disclosed in `09` §2** ("full month names before a bare year bypass the abbreviation-based month pattern") — this is a concrete instance of it, not a new bug.

**Decision — the B2 chapter-5 denominator is NOT amended.** The 84-note list was fixed and SHA-256 hashed in `prereg/B2-ch5.md` before any note was classified. Adding note 25 now, after confirming by hand that it would move to the favourable side of the split, is exactly the after-the-fact adjustment pre-registration exists to prevent — regardless of which direction "favourable" points. The census proceeds on the pre-registered 84.

**Consequence for B7.** `09-b7-retrospective-support-census.md`'s published totals are not re-run in this session. They already carried the disclosed floor-direction caveat for exactly this error class; this finding does not change that disclosure, it confirms it with a real example. **Queued as its own future task** (`NEXT-STEPS.md`): fix `MONTH` to match full month names, re-run `note_dates.py`, re-validate with a **fresh** hand-check sample (the existing two samples are spent), and only then republish corrected B7/B2 totals as a dated revision — not a silent edit.

---

## D-009 — EIT-timing cross-reference: a fifth status added mid-classification, and why that is not a pre-registration violation (2026-09-21)

**What happened.** `prereg/B2-ch5-EIT-timing.md` fixed a four-way status vocabulary (DURING-EIT / POST-EIT / NEVER-SUBJECTED / INCONCLUSIVE) before any SSCI-2014 date was read. On classifying the 54 notes (`12-b2-eit-timing-crossref.md`), a case the vocabulary did not anticipate appeared: for Hambali, SSCI documents a **gap between capture and first EIT use** ("approval to use the CIA's enhanced interrogation techniques...approximately a month after transfer") — so a citation dated in that gap (e.g., "Sept. 4, 2003" against an August 2003 capture and an EIT-approval floor no earlier than mid-September 2003) is neither DURING (the window had not yet opened) nor a case of NEVER-SUBJECTED (the same detainee was subjected to EITs later) nor genuinely INCONCLUSIVE in the pre-registered sense (identity and general timeline are pinned; only the fine boundary is not).

**Decision.** A fifth label, **PRE-EIT** ("falls after capture but before the earliest documented EIT use for that detainee"), is added and used in `12`, defined and justified in that document rather than silently folded into an existing category. This is disclosed as a **vocabulary gap found during classification**, not a retroactive change to how any note was scored under the original four — no note classified DURING, POST or NEVER-SUBJECTED under the original rule is reclassified. Six of 160 individual date-citations (all Hambali) received the new label.

**Second limitation, disclosed rather than forced into a box.** SSCI states no explicit cessation date for Hambali's EIT use (unlike KSM, Abu Zubaydah, Nashiri and bin al-Shibh, each of which has one, quoted and image-verified in `12`). The latest documented EIT-context questioning found is November 30, 2003. Citations at or before that date are classified DURING-EIT; citations after it are labeled **INCONCLUSIVE (no stated cessation)** rather than POST-EIT, because calling them POST-EIT would assert a cessation date SSCI does not state — the conservative direction is to under-claim, not over-claim, consistent with `prereg/B2-ch5-EIT-timing.md` §5's ceiling.

**Why this is not the D-001/D-008 pattern.** D-001 and D-008 concern a tool producing numbers that fail a hand-check, or a denominator being adjusted after the fact for favourability. Here the pre-registered categories were applied exactly as written to every citation; the addition is a **new, named category for a case the original four did not cover**, added before any count was finalized and reported with its own count, not merged into a more favourable existing bucket.
