# Controlling Methodology (v2) — Provenance, Symmetry, and Competing Hypotheses

> **Status: controlling.** Where this document conflicts with `01`, `02`, `03`, `README.md`, `SOURCES.md` or `NEXT-STEPS.md`, this document prevails, in accordance with the repository's existing precedence rule (higher document number prevails). It does not repeal the framing corrections in [`03-phase2a-mfr-verification.md`](03-phase2a-mfr-verification.md) §1; it subsumes and extends them.
>
> Adopted: **19 September 2026**. This is a permanent governing framework, not a session instruction.

---

## 0. The core epistemic problem

An audit built only on official publications risks becoming a **closed evidentiary loop**. Several official documents may appear to corroborate one another while all deriving from a single interview, agency statement, interrogation report, intelligence cable, or inaccessible source.

Official reports are synthesized narratives produced under mandates, deadlines, access restrictions, redactions, editorial choices, institutional incentives and political pressure. They are therefore **objects of investigation**, not automatically neutral descriptions of reality.

This does **not** license the assumption that the official account was engineered to deceive. The following remain competing hypotheses throughout, none privileged:

- deliberate narrative construction;
- institutional concealment;
- defensive omission;
- bureaucratic error;
- incomplete access;
- good-faith analytical failure;
- **the possibility that the official account is substantially correct.**

Alternative and critical narratives are subject to exactly the same scrutiny. Opposition to an official account is not evidence of independence, accuracy, or good faith.

### 0.1 Governing principle

> **Equal procedural treatment; evidentiary weight proportional to provenance, independence, contemporaneity, auditability, and corroboration.**

### 0.2 Baseline axiom (MD-002)

> **Reading official documents establishes the baseline. It cannot independently validate the baseline.**

A claim that appears in an official document is thereby established as *officially asserted*. Establishing it as *true* requires evidence whose provenance root is independent of that document. This axiom applies retroactively to every row already recorded in [`03` §5](03-phase2a-mfr-verification.md) and to every row in [`../registry/claims.md`](../registry/claims.md).

### 0.3 Project objective

For each material claim, determine whether the surviving evidentiary record:

- corroborates it;
- partially corroborates it;
- materially qualifies it;
- contradicts it;
- fails to resolve it;
- or provides insufficient evidence for a responsible conclusion.

The goal is not to confirm the official narrative, prove a conspiracy, or manufacture suspicion. It is to find which claims survive when authority, repetition, institutional prestige and rhetoric are removed, leaving traceable evidence and explicit uncertainty.

**"The official version" is not one stable account.** Reconstruct how each claim changed across agencies, publications, hearings, drafts, testimony, declassifications, litigation and time. **"Alternative versions" are not one coherent account either.** Decompose each into atomic, testable propositions.

---

## 1. Three parallel workstreams

These run in parallel and are connected only through the registries. A finding in one never migrates into another without passing the provenance test in §3.

| # | Workstream | What it reconstructs | Instrument |
|---|---|---|---|
| **W1** | **Official narrative baseline** | Exactly what each official body stated, when, citing what source, with what expressed certainty, and whether the wording later changed | [`registry/version-history.md`](../registry/version-history.md) |
| **W2** | **Independent, contemporaneous or non-narrative records** | Evidence not created primarily to support the final public narrative | [`registry/provenance.md`](../registry/provenance.md) |
| **W3** | **Critical and alternative claims** | Material claims by critics, researchers, witnesses, family groups, journalists, technical specialists and alternative-narrative proponents | [`registry/claims.md`](../registry/claims.md) (C-series) |

### 1.1 W1 — Official narrative baseline

Reconstruct per body, never merged into a single "government position" when the bodies differ. In scope where relevant: early public statements; the Joint Congressional Inquiry; the 9/11 Commission Report and staff materials; Commission MFRs, interviews, hearing records and internal memoranda; CIA, FBI, FAA, NORAD, DoD and Inspector General records; later declassified documents; later statements, testimony, memoirs or corrections by relevant officials.

### 1.2 W2 — Independent / contemporaneous / non-narrative records

Targets: contemporaneous communications, cables, emails, logs and memoranda; operational records; aviation, radar, ATC, emergency-response and communications records; photographs, video, audio and technical records with verifiable provenance; court exhibits, discovery records, sworn testimony and litigation files; FOIA releases and post-report declassifications; drafts, edits, redlines and recorded internal disagreement; foreign investigations, court proceedings, intelligence reviews or official records; contemporaneous journalism **that provides or links to underlying primary material**; testimony recorded close to the event, kept distinct from later memory.

> A book, article, documentary, interview, website or critical essay may identify a lead. It is **never** the terminal evidentiary source when an underlying primary record exists.

### 1.3 W3 — Critical and alternative claims

Build a structured registry of material claims. **Do not classify an author, community or documentary as true or false.** Extract each claim separately and trace it to the best available underlying evidence.

The same fields are recorded for every side: exact quotation; source identity; date; contemporaneity; chain of custody; source independence; possible incentives; direct knowledge vs. hearsay; whether the cited source actually supports the claim attributed to it; contrary evidence; unresolved limitations.

---

## 2. Atomic claim registry

Every target — A1–A16 and everything after — is decomposed into atomic propositions. One broad conclusion must never conceal several propositions of differing evidentiary strength.

Required fields per row are specified and maintained in [`registry/claims.md`](../registry/claims.md) §1. Minimum: stable claim ID; precise proposition; claimant or issuing institution; first known date of the claim; later versions or wording changes; supporting evidence; contrary evidence; evidence that merely contextualizes; primary provenance root; source dependencies; unresolved access/redaction limitations; competing explanations (EC1–EC5); current status; qualitative conservative confidence; closure conditions.

**Decomposition rule (MD-007).** Legacy rows A1–A16 in [`03` §5](03-phase2a-mfr-verification.md) are **never edited in place** — they are the Phase A historical record. They are carried into `registry/claims.md` as *containers*, decomposed into `A<n>.<k>` atomic propositions. A container has no status of its own; only its atomic propositions do.

---

## 3. Provenance and source-independence graph

For every consequential proposition, trace:

> **Claim → document publishing it → source cited by that document → earliest recoverable source.**

**Repeated publications sharing a provenance root are not independent corroboration.** Count them once.

Explicitly detect and record: circular citation; multiple reports relying on one interview; one interrogation report repeated across several documents; unattributed institutional assertions; inaccessible or fully redacted sources; foreign liaison reporting whose origin cannot be evaluated; summaries that materially strengthen or alter the source wording; quotations detached from limiting context; later recollection presented as contemporaneous knowledge.

> **When independence cannot be established, record it as `unknown`. Never assume independence.**

---

## 4. Version-history analysis

For every central claim, maintain a chronological version ledger in [`registry/version-history.md`](../registry/version-history.md) recording: earliest recoverable wording; subsequent wording; additions, removals, narrowing or expansion; changes in certainty; changes in attributed source; new evidence offered for the change; whether an earlier statement was formally corrected; and whether an apparent contradiction is substantive or merely a difference of scope.

> Particular attention: **uncertainty later converted into certainty without new disclosed evidence.**

---

## 5. Competing-hypothesis testing (EC1–EC5)

**Naming decision (MD-001).** This project already uses `H0`–`H7` for substantive hypotheses about the events (see [`README.md`](../README.md)). The explanation classes below are therefore labelled **`EC1`–`EC5`** ("explanation class") to prevent collision. An `EC` is a class of explanation for a *discrepancy*; an `H` is a hypothesis about *what happened*. They are never interchangeable.

| ID | Explanation class |
|---|---|
| **EC1** | No substantive contradiction — the sources address different questions, scopes or times |
| **EC2** | Ordinary error, memory failure, administrative fragmentation, incomplete records, or analytical disagreement |
| **EC3** | Institutional self-protection, defensive omission, inter-agency conflict, or avoidance of embarrassment or liability |
| **EC4** | Deliberate selection, suppression or reframing of evidence to preserve a public narrative |
| **EC5** | A specific alternative explanation advanced by an identified critic or evidentiary source (must name the critic/source) |

Listing the classes is not analysis. For each material discrepancy, state, per class:

1. what observable evidence it predicts;
2. what evidence would weaken it;
3. what evidence would distinguish it from the others;
4. which of those observations are currently available;
5. what remains inaccessible;
6. whether the same evidence is compatible with more than one class.

**Prohibitions.** Do not assign numerical probabilities unless a validated method exists. Do not treat the absence of a document as proof that it was destroyed or concealed.

---

## 6. Discrepancy ledger and controlled taxonomy

Every discrepancy is classified with exactly one primary category from the closed taxonomy in [`registry/discrepancies.md`](../registry/discrepancies.md) §1. Three distinctions are mandatory and are never collapsed:

| Must stay distinct from | | |
|---|---|---|
| "Not found in the reviewed corpus" | ≠ | "did not exist" |
| "Unsupported by disclosed evidence" | ≠ | "false" |
| "Officially asserted" | ≠ | "independently corroborated" |

---

## 7. Document-card language and required fields

### 7.1 Permitted formulations

- "The document states…"
- "The document records…"
- "The author attributes this to…"
- "The disclosed record supports…"
- "The document does not establish…"
- "The available corpus does not resolve…"

Do **not** write that a document "fixes", "proves" or "establishes" anything, unless the proposition being established is only that *the statement appears in that document*.

### 7.2 Required fields for every decisive quotation (MD-004)

| Field | Values |
|---|---|
| Document identifier | `DOC-n` |
| Image/PDF page | integer, as printed **and** as PDF page if they differ |
| Exact quotation | verbatim, with `[REDACTED 25X1]` markers where the page image shows a void |
| Checked against page image? | `yes` / `no` |
| Source layer | `native text` · `agency OCR` · `project OCR` · `manual transcription` |
| Assertion type | `direct observation` · `third-party report` · `analytical judgment` · `institutional denial` · `recollection` · `access/process statement` · `editorial interpretation` |

> **Image verification is not optional for decisive quotations.** The extracted text layer of a scanned release can silently omit a redaction void: see [`registry/cards/DOC-7-mfr-tenet-2.md`](../registry/cards/DOC-7-mfr-tenet-2.md) §5, where roughly 60% of one page is a redaction block invisible in the text layer.

### 7.3 Re-carding requirement (blocking gate)

**DOC-1** (*Report on Review of PDB Articles*), **DOC-2** (MFR Condoleezza Rice) and **DOC-3** (MFR Mike Scheuer #1) were read in Phase A before the image-verification standard existed, and DOC-1's card records bad OCR with reconstructed sense. They **must be re-carded under §7.2** before **A10**, **A16**, or any conclusion depending on them may be closed. Tracked in [`registry/cards/README.md`](../registry/cards/README.md) §3.

---

## 8. Custodial-source instruments: B1 and B2 (MD-005, MD-006)

Governed in full by [`registry/instruments-b1-b2.md`](../registry/instruments-b1-b2.md). Summary of the binding rules:

- **B2-ref** — the note or document *mentions* detention, interrogation, or a custodial source.
- **B2-rely** — a factual proposition *materially relies* on information derived from such a source.
- **B2-ref and B2-rely are never summed.** They do not measure the same thing.
- Source subtypes are never collapsed: a cooperating witness interviewed in custody; an FBI 302; a Commission interview; a CIA detention-program interrogation report; a foreign liaison interrogation report; an Inspector General summary.
- **B1 is an invalidated instrument.** Its versions, hand-checks, failure analysis and held-out results are preserved where they exist; **its numerical distributions are never reused or published.**

---

## 9. Publication and closure gates

- No claim closes merely because several official documents repeat it.
- No critical claim is accepted merely because it identifies a real inconsistency.

A material conclusion requires **all** of:

1. traceable primary provenance where available;
2. explicit source-dependency analysis;
3. consideration of contrary evidence;
4. competing-hypothesis analysis (EC1–EC5);
5. separation of contemporaneous evidence from later recollection;
6. documentation of missing, redacted or inaccessible evidence;
7. calibrated language matching the strength of the record.

Where these are not met, the correct result is **INCONCLUSIVE** or **INSUFFICIENT DISCLOSED EVIDENCE**.

---

## 10. Corpus expansion gate (MD-010)

> **No indiscriminate internet collection.** Source-inclusion, provenance, preservation and deduplication rules must be satisfied before the corpus is expanded beyond the currently listed primary repositories.

The rules are in [`registry/source-policy.md`](../registry/source-policy.md). Expanding the corpus without them is a methodological failure, not a shortcut.

---

## 11. Repository, language and preservation rules

- **Language (MD-003).** All repository artifacts are written in **English**: documentation, filenames where practical, logs, matrices, code comments, commit messages and methodological decisions. Legacy Phase A documents (`README.md`, `SOURCES.md`, `NEXT-STEPS.md`, `docs/01`, `docs/02`, `docs/03`) are in Portuguese and are **preserved verbatim as the historical record** — translating or rewriting them would destroy the Phase A work this framework is required to preserve. Content *added* to those files from this point on is in English.
- **Preservation (MD-008).** Raw artifacts and prior methodological failures are preserved. A source is never silently overwritten. Changed hashes, changed source files, reclassifications and corrections are recorded as **explicit events** — in [`corpus/manifest.md`](../corpus/manifest.md) for artifacts and in [`registry/version-history.md`](../registry/version-history.md) for claims.
- **History.** Work proceeds on the current branch. History is not rewritten; prior evidence is not deleted; failed experiments are not erased.

---

## 12. Register of methodological decisions

| ID | Decision | Rationale |
|---|---|---|
| **MD-001** | Explanation classes are `EC1`–`EC5`, not `H1`–`H5` | `H0`–`H7` are already bound to substantive hypotheses; reuse would silently corrupt every existing matrix row |
| **MD-002** | Baseline axiom: official-document reading establishes, never validates, the baseline | Prevents the closed evidentiary loop described in §0 |
| **MD-003** | English for all new artifacts; legacy Portuguese documents preserved verbatim | Preservation requirement outranks retroactive language uniformity |
| **MD-004** | Image-verification standard and source-layer taxonomy for decisive quotations | Text layers of scanned releases omit redaction voids (empirically demonstrated, DOC-7 p.4) |
| **MD-005** | B2-ref and B2-rely separated; subtypes never collapsed; never summed | They measure different things |
| **MD-006** | B1 quarantined as an invalidated instrument; distributions never reused | Stated failure of the instrument |
| **MD-007** | A1–A16 preserved verbatim as containers; atomic propositions numbered `A<n>.<k>` | Preserves Phase A record while enabling atomic status |
| **MD-008** | Binaries not committed; SHA-256 + extracted text committed; hash changes recorded as events | Auditability without repository bloat; exact re-verification remains possible |
| **MD-009** | This framework's implementation makes **no** substantive conclusions; `H0`–`H7` are unchanged by it | Instrument construction is a precondition of evidence, not a substitute for it |
| **MD-010** | Corpus expansion gated on [`registry/source-policy.md`](../registry/source-policy.md) | Prevents indiscriminate collection |
