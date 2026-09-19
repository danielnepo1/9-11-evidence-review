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

Targets: contemporaneous communications, cables, emails, logs and memoranda; operational records; aviation, radar, ATC, emergency-response and communications records; photographs, video, audio and technical records with verifiable provenance; court exhibits, discovery records, testimony given under oath and litigation files (a *class* of record — the procedural status of any specific document is established per document, §7.4); FOIA releases and post-report declassifications; drafts, edits, redlines and recorded internal disagreement; foreign investigations, court proceedings, intelligence reviews or official records; contemporaneous journalism **that provides or links to underlying primary material**; testimony recorded close to the event, kept distinct from later memory.

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

### 4.1 Six-track timeline (MD-019)

The four-date rule (§7.2, as extended) is a *provenance* instrument. It cannot represent a chronology. Every consequential event is recorded in [`../registry/timeline.md`](../registry/timeline.md) on six tracks, never merged:

**event time · observation time · communication time · record creation time · later recollection time · declassification-publication time**

Plus, per entry: time zone, clock source, precision, synchronisation evidence, and whether the timestamp was **`automatic`** (machine-generated at the time) or **`reconstructed`** (assigned later by a person).

> **Never combine "approximately", rounded media times and synchronised system logs without uncertainty bounds.** A witness's "around 9:40" and a log's `09:40:12` are different data and are never averaged or matched.

A record creation time is not an event time. Conflating them is the commonest source of false precision in a reconstructed chronology.

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

### 6.1 Anomaly register: escalation ladder and priority (MD-020)

The discrepancy ledger classifies *what kind* of discrepancy exists. It cannot say how far the evidence permits escalation, or what is worth chasing. Both live in [`../registry/anomalies.md`](../registry/anomalies.md), which carries one row per discrepancy.

**Escalation ladder — levels may not be skipped:**

| Level | Name | What permits escalation to it |
|---|---|---|
| 1 | Discrepancy | Records or claims do not align |
| 2 | Unresolved anomaly | Ordinary reconciliation has been **tested** and remains inadequate |
| 3 | Structured pattern | Multiple **substantially independent** anomalies point the same way |
| 4 | Evidence of concealment | Affirmative acts or records support deliberate withholding |
| 5 | Evidence of foreknowledge or participation | Evidence connects an actor to specific operational knowledge or material conduct |

Each row records **exactly what permits its level**. A large collection of dependent, low-quality discrepancies does not become a structured pattern: level 3 requires substantial independence, and anomalies sharing a provenance root count once.

**Priority P0–P3 measures research value — explicitly not probability of conspiracy.** A row may be P0 while its most likely explanation is entirely ordinary. P0 = a documented fracture on a central claim, capable of separating major hypotheses; P1 = material unresolved tension with obtainable discriminating evidence; P2 = a real anomaly with several viable ordinary explanations; P3 = low-centrality curiosity or weakly sourced allegation.

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

**Dates, extended twice.** The three-date rule (`docs/03` §1.1) became four with DISC-006 (annotation date). Two further slots are now required, because a staged public release of a classified report is neither a declassification nor a document date:

| Slot | What it records |
|---|---|
| Event date | When the reported fact occurred |
| Document date | When the record was produced |
| Annotation date | When a later hand added to it (or `none detected`) |
| **Staged redacted publication** | Each partial public release, with what it omitted |
| **Web re-render** | When a publisher re-rendered the text for the web, which is a derivative artifact, not a release |
| Declassification date | When the classified record was declassified |

A 2006 public release of a 2004 report is a **derivative publication**, not a declassification date, and does not go in that field.

| Field | Values |
|---|---|
| Document identifier | `DOC-n` |
| Image/PDF page | integer, as printed **and** as PDF page if they differ |
| Exact quotation | verbatim, with `[REDACTED 25X1]` markers where the page image shows a void |
| Checked against page image? | `yes` / `no` |
| Source layer | `native text` · `agency OCR` · `project OCR` · `manual transcription` · **`publisher HTML re-rendering`** (a CMS re-render of a printed report — carries no pagination, and its fidelity to the printed text is untested until diffed) |
| Assertion type | `direct observation` · `third-party report` · `analytical judgment` · `institutional denial` · `recollection` · `access/process statement` · `editorial interpretation` |

> **Image verification is not optional for decisive quotations.** The extracted text layer of a scanned release can silently omit a redaction void: see [`registry/cards/DOC-7-mfr-tenet-2.md`](../registry/cards/DOC-7-mfr-tenet-2.md) §5, where roughly 60% of one page is a redaction block invisible in the text layer.

### 7.3 Re-carding requirement (blocking gate)

**DOC-1** (*Report on Review of PDB Articles*), **DOC-2** (MFR Condoleezza Rice) and **DOC-3** (MFR Mike Scheuer #1) were read in Phase A before the image-verification standard existed, and DOC-1's card records bad OCR with reconstructed sense. They **must be re-carded under §7.2** before **A10**, **A16**, or any conclusion depending on them may be closed. Tracked in [`registry/cards/README.md`](../registry/cards/README.md) §3.

---

### 7.4 Procedural status of a witness document (MD-012)

> The words "under oath", "sworn testimony" and any equivalent are used **only** where the source document itself, or a directly linked procedural record, establishes that status. Everywhere else the narrower label applies: **"Commission interview record"** or **"interview memorandum"**.

A procedural status read from an extracted text layer carries that qualifier, because the text layer of these releases is demonstrably imperfect and the oath notice is a single line of front matter. Every document card records status using the controlled vocabulary in [`../registry/witness-status.md`](../registry/witness-status.md) §2, with the exact basis quoted. Statements by third parties present at an interview are never covered by the witness's oath and are labelled by speaker.

### 7.4A Institutional-failure taxonomy (MD-022)

When a process failed, name **which kind** of failure. Eleven categories:

collection failure · dissemination failure · analytical failure · prioritisation failure · legal or policy barrier · **practice more restrictive than law** · individual error · management decision · recordkeeping failure · public-relations reconstruction · deliberate concealment

Plus the procedural test: when a procedure was not followed, establish whether it was **mandatory, customary, discretionary, obsolete, waived, or practically impossible at the time**.

> An adverse institutional incentive increases the need for corroboration; it does not by itself prove the institution acted on that incentive.

**Supersession, stated precisely.** This taxonomy **supersedes for future work** the three-way split pre-registered at [`../docs/03` §4](../docs/03-phase2a-mfr-verification.md) Priority 6 (legal barrier / institutional practice beyond the barrier / case-by-case decision to withhold). `docs/03` is Tier 1: its wording is **not edited, not replaced, and remains the accurate record of how Priority 6 was pre-registered**. Both remain readable. The three-way split maps onto categories 5, 6 and 11 respectively, and the other eight were unrepresentable under it.

Load-bearing for T-12 ("iron-clad wall") and for anything the Priority 6 reading produces.

### 7.5 Negative findings and transliteration variants (MD-011)

A negative finding — "the document does not mention X" — is only as good as the strings searched. Names in this corpus are transliterated inconsistently, and across releases: the same individual appears as `al Midhar` in the 2026 MFRs and as `al-Mihdhar` in most secondary literature.

> Every negative finding is run over the **transliteration and spelling variants** of each term, and the variant set searched is recorded with the finding. A negative finding recorded before this rule existed is **not trustworthy until re-run**.

This rule exists because the project's own first negative finding (T-N1) was originally run on `Mihdhar` and `Hazmi` only, against documents that spell it `Midhar`. It survived re-running; the next one might not.

### 7.6 Quantifier-drift watchlist (MD-023)

Claims degrade by losing a qualifier. Check every restatement against the original for these five, and for their siblings:

| Original | Drifts to |
|---|---|
| "no **current** intelligence" | "no intelligence" |
| "not corroborated" | "false" |
| "not shared **with this official**" | "not shared" |
| "no **identified** steel sample" | "no steel recovered" |
| "no evidence **found**" | "evidence of absence" |

The drift is usually invisible in a single step and complete after three.

### 7.7 Stop conditions — pause rather than infer

Stop and state the blocker, naming the exact document, datum or test needed, when:

- the primary source is unavailable;
- decisive OCR cannot be checked against the page image;
- a quotation cannot be located;
- the source chain terminates in a snippet or an unattributed summary;
- key definitions differ across the claims being compared;
- the requested conclusion would exceed the evidence ceiling.

### 7.8 Evidence-weighting axes (eight)

Weight evidence across all eight rather than by a single source hierarchy. This supersedes the five named in §0.1, which remain correct but incomplete:

**contemporaneity · proximity · independence · completeness · authenticity · specificity · falsifiability · exposure to institutional or personal incentives**

## 8. Custodial-source instruments: B1 and B2 (MD-005, MD-006)

Governed in full by [`registry/instruments-b1-b2.md`](../registry/instruments-b1-b2.md). Summary of the binding rules:

- **B2-ref** — the note or document *mentions* detention, interrogation, or a custodial source.
- **B2-rely** — a factual proposition *materially relies* on information derived from such a source.
- **B2-ref and B2-rely are never summed.** They do not measure the same thing.
- Source subtypes are never collapsed: a cooperating witness interviewed in custody; an FBI 302; a Commission interview; a CIA detention-program interrogation report; a foreign liaison interrogation report; an Inspector General summary.
- **B1 is an invalidated instrument.** Its versions, hand-checks, failure analysis and held-out results are preserved where they exist; **its numerical distributions are never reused or published.**

---

## 8A. Negative-evidence discipline (MD-021)

Absence is probative **only** when **all five** hold:

1. the item would probably exist if the hypothesis were true;
2. the search or test was capable of finding it;
3. the relevant material was preserved;
4. the search scope is documented;
5. suppression, destruction or non-recording is not equally plausible.

> **Corollary.** An expected record's absence weakens an official claim **only after establishing a duty or a reliable practice to create and retain that record.** Without that, "there is no memo" is a fact about the corpus, not about the world.

Two species of absence, not to be confused:

| Species | Example in this corpus | Strength |
|---|---|---|
| **A record that would ordinarily exist is missing** | U-16, U-17 — no memo for two 2001 meetings between the DCI and the National Security Adviser | Stronger, **conditional on establishing the duty or practice** |
| **A string does not appear in a document** | T-N1, U-N1, U-N2 | Weaker; bounded by MD-011 (variant search) and by what the document was for |

Neither is evidence of concealment. Both are recorded as limitations until the five conditions are met, and the conditions are stated explicitly per row rather than assumed.

**Live items owing this test:** U-16, U-17, T-03, T-N1, U-N1, U-N2.

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

### 9.1 Closure is a separate boolean, and no status token implies it (MD-015)

Blocking gates say that rows "may not be closed", but the registry had no `closed` state and no closure field distinct from "Closure condition". The result was ambiguous: A9.1 held the terminal-looking `contradita` while simultaneously listed as gate-blocked, and nothing said whether assigning that token amounted to closing the row.

> **`closed` is a boolean field on the claim row, separate from `Status`. It is set only when all seven conditions above are satisfied. No status token — not `corroborada`, not `contradita`, not any other — implies closure. A blocking gate blocks the boolean, never the token.**

Three consequences, all load-bearing:

1. A row may carry a terminal-sounding status and still be open. `contradita` records what the evidence did to the proposition; `closed` records that the project has finished with it.
2. A gated row's status may still change on new evidence, because changing a status is not closing a row. What the gate forbids is declaring the matter settled.
3. **A taxonomic migration (§9.2) cannot set `closed`**, and closure cannot be inferred from the absence of an open closure condition.

### 9.2 Taxonomic migration — a status-token change that is not a status change (MD-016)

Occasionally the vocabulary itself is re-partitioned, and rows must move token without any re-decision of the underlying proposition. That is a different act from a status change and is recorded as a different event class in [`../registry/version-history.md`](../registry/version-history.md) §3.

A change of status token may be recorded as a **`taxonomic migration`** only when **all three** hold:

1. the row's `Supporting evidence`, `Contrary evidence`, `Provenance root` and `Independence` fields are **byte-identical** before and after;
2. the old and new tokens are recorded **side by side** in the event;
3. the inferential weight is unchanged — the migration re-partitions the vocabulary, it does not re-decide the proposition.

A taxonomic migration **cannot set the `closed` boolean** and **cannot be cited as evidence anywhere**. Any change failing one of the three conditions is an ordinary status change and is subject to every rule governing those, including the gates.

---

## 10. Corpus expansion gate (MD-010)

> **No indiscriminate internet collection.** Source-inclusion, provenance, preservation and deduplication rules must be satisfied before the corpus is expanded beyond the currently listed primary repositories.

The rules are in [`registry/source-policy.md`](../registry/source-policy.md). Expanding the corpus without them is a methodological failure, not a shortcut.

---

## 11. Repository, language and preservation rules

- **Language (MD-003).** All repository artifacts are written in **English**: documentation, filenames where practical, logs, matrices, code comments, commit messages and methodological decisions. Legacy Phase A documents (`README.md`, `SOURCES.md`, `NEXT-STEPS.md`, `docs/01`, `docs/02`, `docs/03`) are in Portuguese and are **preserved verbatim as the historical record** — translating or rewriting them in place would destroy the Phase A work this framework is required to preserve.

  **Amended 19 September 2026 (MD-013).** Complete English **companion** translations of every Portuguese document live in [`../en/`](../en/), each marked as a translation, linked to its original, and carrying the original's SHA-256 at translation time so drift is detectable. The Portuguese original remains authoritative: a disagreement between an original and its companion is a translation defect, corrected in the companion and never in the original. Governed by [`../en/TRANSLATION-POLICY.md`](../en/TRANSLATION-POLICY.md).
- **Preservation (MD-008, MD-014).** Raw artifacts and prior methodological failures are preserved **by hash and derived text, not by committing binaries** — see [`../corpus/manifest.md`](../corpus/manifest.md) §3 for the publication-status rule. A source is never silently overwritten. Changed hashes, changed source files, reclassifications and corrections are recorded as **explicit events** — in [`corpus/manifest.md`](../corpus/manifest.md) for artifacts and in [`registry/version-history.md`](../registry/version-history.md) for claims.
- **History.** Work proceeds on the current branch. History is not rewritten; prior evidence is not deleted; failed experiments are not erased.

---

## 12. Register of methodological decisions

| ID | Decision | Rationale |
|---|---|---|
| **MD-001** | Explanation classes are `EC1`–`EC5`, not `H1`–`H5` | `H0`–`H7` are already bound to substantive hypotheses; reuse would silently corrupt every existing matrix row |
| **MD-002** | Baseline axiom: official-document reading establishes, never validates, the baseline | Prevents the closed evidentiary loop described in §0 |
| **MD-003** | English for all new artifacts; legacy Portuguese documents preserved verbatim | Preservation requirement outranks retroactive language uniformity. **Amended by MD-013**, which adds complete English companions |
| **MD-004** | Image-verification standard and source-layer taxonomy for decisive quotations | Text layers of scanned releases omit redaction voids (empirically demonstrated, DOC-7 p.4) |
| **MD-005** | B2-ref and B2-rely separated; subtypes never collapsed; never summed | They measure different things |
| **MD-006** | B1 quarantined as an invalidated instrument; distributions never reused | Stated failure of the instrument |
| **MD-007** | A1–A16 preserved verbatim as containers; atomic propositions numbered `A<n>.<k>` | Preserves Phase A record while enabling atomic status |
| **MD-008** | Binaries not committed; SHA-256 + extracted text committed; hash changes recorded as events | Auditability without repository bloat; exact re-verification remains possible |
| **MD-009** | This framework's implementation makes **no** substantive conclusions; `H0`–`H7` are unchanged by it | Instrument construction is a precondition of evidence, not a substitute for it |
| **MD-010** | Corpus expansion gated on [`registry/source-policy.md`](../registry/source-policy.md) | Prevents indiscriminate collection |
| **MD-011** | Negative findings are run over transliteration and spelling variants, and the variant set is recorded | The corpus spells the same name several ways; a negative finding on one spelling is not a negative finding (§7.5) |
| **MD-012** | "Under oath" / "sworn" used only where the source or a directly linked procedural record establishes it, always with its verification state; otherwise "Commission interview record" or "interview memorandum" | An oath changes the weight of a statement, and MFRs with and without one are indistinguishable on the page (§7.4) |
| **MD-013** | Portuguese Phase A documents are preserved unaltered; complete English companion translations live in [`../en/`](../en/), marked as translations, linked to the original, with the source's SHA-256 recorded for drift detection. **The original prevails; a disagreement is a translation defect** | Satisfies the English-for-GitHub requirement without destroying the Phase A record, and makes staleness detectable |
| **MD-014** | No source PDF, page image or other binary is committed unless its publication status is explicitly documented **and** a reason to commit it is recorded in [`../corpus/manifest.md`](../corpus/manifest.md) §3 | Hashes already give exact re-verification; redistribution is not this project's function |
| **MD-015** | `closed` is a boolean field separate from `Status`; **no status token implies closure**; gates block the boolean | A9.1 held a terminal-looking token while gate-blocked, and nothing said whether that counted as closing it (§9.1) |
| **MD-016** | `taxonomic migration` is a distinct event class from `status change`, admitted only on byte-identical evidence fields, side-by-side tokens and unchanged inferential weight; it can never set `closed` | Lets the vocabulary be re-partitioned without any row behind a gate being re-decided (§9.2) |
| **MD-017** | Token **`document_attested`** added: *the proposition is explicitly present in the reviewed artifact and locator, subject to the recorded limitations of version, redaction, missing page and completeness* | `corroborada` was doing two jobs — independently corroborated, and merely present in the artifact. Textual presence is not truth ([`../registry/claims.md`](../registry/claims.md) §2.1) |
| **MD-018** | Three event classes in the change ledger: `status change`, `initial assignment`, `taxonomic migration`. Container→atomic derivation is always `initial assignment`, with the container value recorded **for reference only** | MD-007 gives containers no status, so there was no old status to change from; the ledger was recording one operation two ways and omitting it for six rows |
| **MD-019** | Six-track timeline with clock source, precision, synchronisation evidence and `automatic` vs `reconstructed` | The four-date rule is a provenance instrument and cannot represent a chronology (§4.1) |
| **MD-020** | Anomaly register with a five-level escalation ladder and P0–P3 priority measuring **research value, not probability of conspiracy** | The ledger could say what kind of discrepancy existed but not how far it could be escalated or what to chase (§6.1) |
| **MD-021** | Absence is probative only on five conditions, and an expected record's absence weakens an official claim only after a duty or reliable practice to create and retain it is established | The project records declared absences (U-16, U-17) without any test of whether they are probative (§8A) |
| **MD-022** | Eleven-category institutional-failure taxonomy, superseding for future work the three-way split pre-registered at `docs/03` §4 Priority 6, which is Tier 1 and is not edited | The three-way split left eight kinds of failure unrepresentable (§7.4A) |
| **MD-023** | Quantifier-drift watchlist; stop conditions; eight weighting axes | Claims degrade by losing qualifiers, and the degradation is invisible one step at a time (§7.6–§7.8) |
