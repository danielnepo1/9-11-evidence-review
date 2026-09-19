# 9/11 Evidence Review

> Symmetric, document-based audit of the 9/11 record — the official account and every alternative account tested against the same standard, with full source traceability.

A systematic review of primary sources (NIST, the 9/11 Commission, CIA, NARA, Congress) across two tracks: (1) the physical plausibility of the Twin Towers and WTC 7 collapses, and (2) pre-9/11 intelligence and institutional response. Method: steelman the official account → stress-test it against the primary record → mirror-test every alternative hypothesis against the same record → judge without a fixed prior conclusion. Every claim carries a confidence status; every source is logged with access date, extent read, and known limitations.

---

## Governing principle — symmetric skepticism

> “Every material claim is provisional until supported by traceable evidence. Official status does not make a claim true; institutional inconsistency does not make an alternative claim true. The project applies skepticism symmetrically: it actively tests the official account for contradictions and unexplained anomalies, while applying the same burden of proof, alternative-explanation testing, and falsification criteria to every alternative hypothesis.”

This commits the project to two things at once:

- **It does** actively investigate contradictions, anomalies, unexplained events, evidentiary gaps, changed accounts and unusual procedural decisions within the official account. Declining to look is a methodological failure, not caution.
- **It does not** assume the official account is false, nor assume any alternative account is false. They are competing explanations, tested against the same evidence with the same burden.

The full methodology is [`docs/04-methodology-symmetric-skepticism.md`](docs/04-methodology-symmetric-skepticism.md), which governs every other document in this repository.

## About this project

This repository documents an ongoing audit of the official account of the 11 September 2001 attacks. The goal is neither to confirm nor to refute that account, but to subject it — and the alternatives — to the same evidentiary standard, with full source traceability.

**Honesty standard.** No conclusion is presented without stating whether the underlying document was read in full, read in part, or known only through a summary, FAQ or press release. Where that was not possible within a session, the repository records the gap explicitly instead of filling it with unverified prior knowledge.

**Language.** Repository content is written in English. `docs/01`, `docs/02` and `docs/03` remain in the original Portuguese pending a faithful translation, tracked as a background item in [`NEXT-STEPS.md`](NEXT-STEPS.md); they are the historical findings record, and translating them is kept as its own reviewable change so that no wording shift can be mistaken for a revised finding.

## Structure

```
9-11-evidence-review/
├── README.md                                   ← this file: hypotheses, confidence scale, entry point
├── docs/
│   ├── 01-wtc-engineering-audit-v1.md          ← first audit (WTC structural engineering) [pt-BR]
│   ├── 02-adversarial-audit-phase1.md          ← second audit (adversarial, multi-hypothesis, Phase 1) [pt-BR]
│   ├── 03-phase2a-mfr-verification.md          ← framing corrections + Phase 2A verification instrument [pt-BR]
│   ├── 04-methodology-symmetric-skepticism.md  ← GOVERNING METHODOLOGY
│   ├── 05-stress-test-execution-plan.md        ← targeting plan: where to look, priorities, ceilings
│   ├── claim-decomposition-register.md         ← atomic-proposition register (empty at creation)
│   ├── anomaly-register.md                     ← anomaly register (empty at creation)
│   └── contradiction-ledger.md                 ← contradiction ledger (empty at creation)
├── SOURCES.md                                  ← consolidated bibliography with read status
└── NEXT-STEPS.md                               ← execution queue
```

### Reading order

Document numbering is chronological **and** hierarchical: each later document corrects the earlier ones, and where they conflict **the higher number prevails**.

| Order | File | Role | How to read it |
|---|---|---|---|
| 1 | [`README.md`](README.md) | Governing principle, hypotheses H0–H7, confidence scale | Entry point — defines the vocabulary used everywhere else |
| 2 | [`docs/04-methodology-symmetric-skepticism.md`](docs/04-methodology-symmetric-skepticism.md) | **Governing methodology** | Symmetry requirements, claim decomposition, mirror test, mandatory reporting format |
| 3 | [`docs/05-stress-test-execution-plan.md`](docs/05-stress-test-execution-plan.md) | **Targeting plan** | Where fractures are most likely, P0–P3 priorities, escalation ladder, cross-cutting attack patterns, fixed conclusion ceilings, next reading order |
| 4 | [`docs/03-phase2a-mfr-verification.md`](docs/03-phase2a-mfr-verification.md) | Current framing + verification instrument | §1 corrects five formulations in `02`; §5 is the claim-by-claim status table; §7 is the current state of H1–H5 |
| 5 | [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md) | Phase 1 documentary audit | §2 lists what was retracted from `01`; §§3–6 are the substantive findings. **Read with the `03` §1 errata in hand** |
| 6 | [`docs/01-wtc-engineering-audit-v1.md`](docs/01-wtc-engineering-audit-v1.md) | First pass, engineering | **Historical record.** Not to be cited in isolation: several points were retracted |
| 7 | [`SOURCES.md`](SOURCES.md) | Consolidated bibliography with read status | Consult before assigning weight to any assertion |
| 8 | [`NEXT-STEPS.md`](NEXT-STEPS.md) | Execution queue | Starting point for any new session |

**Reference vs. next step:** items 1–7 are **reference** material (what is established, and on what basis); item 8 is the **execution** queue. A new session starts with 1, 2, 3, 4 and 8 — `01` is only needed when the work touches structural engineering, and then always alongside `02` §2; `02` is always read with the `03` §1 errata.

**Precedence rule.** On method, `04` prevails over everything. On substantive findings, the higher-numbered document prevails: where `02` and `03` differ on the classification of a hypothesis or a claim, **`03` prevails**; `04` and `05` change no finding — `05` contains no findings at all, only pre-registered targets.

## Methodology in brief

The audit runs three explicit passes:

1. **Official steelman** — build the strongest possible version of the official explanation (NIST, 9/11 Commission).
2. **Stress test** — build the strongest possible challenge using primary documents, internal contradictions and later-released material.
3. **Mirror test** — subject every alternative hypothesis to the same evidence, the same burden of proof and the same falsification criteria.
4. **Judge** — compare without starting from a desired conclusion.

### Symmetry requirements

Binding on every inference in every phase (full text in [`docs/04`](docs/04-methodology-symmetric-skepticism.md) §3):

| # | Requirement |
|---|---|
| S1 | H0 is decomposed into atomic propositions, never scored as a single protected narrative |
| S2 | H1–H7 gain no support from gaps, opacity or distrust of institutions |
| S3 | Evidence of institutional failure is not promoted into evidence of deliberate non-intervention |
| S4 | Evidence of a contradiction is not promoted into evidence of material intervention |
| S5 | Absence of a test is a limitation, not a positive result |
| S6 | Burden of proof depends on what a claim asserts, not on whether it is official or alternative |
| S7 | Every phase states what it could be wrong about in **both** directions |

### Hypotheses kept separate

For the intelligence / institutional-response dimension, eight hypotheses are treated as distinct categories, each requiring its own evidence (evidence for one is never automatically treated as evidence for another):

| # | Hypothesis |
|---|---|
| H0 | Attack planned by al-Qaeda; institutional failures and the structural explanation essentially correct |
| H1 | H0 + self-protection / misleading statements / after-the-fact concealment of incompetence, without operational prior knowledge |
| H2 | H0 + knowing logistical support by individuals linked to a foreign government, without proof of authorization from above |
| H3 | Broader foreign institutional support or protection |
| H4 | US authorities had sufficient warnings but failed through negligence, fragmentation or political priorities |
| H5 | Segments of the authorities had specific operational knowledge and deliberately did not prevent the attack |
| H6 | The mechanism of one or more collapses differed significantly from what NIST presented |
| H7 | Additional deliberate intervention in the buildings |

**H0 is not scored as a unit.** Under S1 it is represented by its decomposed atomic propositions; any summary status for H0 is a roll-up, reported with the spread stated.

### Evidentiary framing rule

> Access restriction, generic warning and interested testimony are not — singly or in combination — proof of a cover-up or of prior knowledge.

Three mandatory corollaries, which apply in **both** directions:

1. **New document ≠ new fact.** Every citation distinguishes **event date**, **document date** and **declassification date**. A 2004 record declassified in 2026 is 2004 memory, not a contemporaneous 2001 record.
2. **Each step requires its own evidence.** Process failure → institutional self-protection → deliberate suppression → operational prior knowledge are four distinct propositions; evidence for one is never promoted to evidence for the next.
3. **Reading is reading.** A summary, FAQ, press release, search snippet or third-party news report supports neither `corroborated` nor `contradicted` status.

### Anomaly handling

Anomalies are recorded in [`docs/anomaly-register.md`](docs/anomaly-register.md) under a closed status vocabulary: `documentary contradiction` · `timeline discrepancy` · `conflicting testimony` · `unexplained procedural deviation` · `missing or destroyed evidence` · `chain-of-custody limitation` · `model assumption or non-replicability issue` · `physical or forensic anomaly` · `apparent anomaly with adequate explanation` · `unresolved anomaly`.

> **An anomaly is a research lead. By itself it is not evidence of intent, foreknowledge, complicity, or intervention.**

Every anomaly carries a **mirror test** before any status is fixed: (1) what would the official account predict? (2) what would each relevant alternative hypothesis predict? (3) what observation would discriminate between them? (4) is it explained by error, memory, classification, bureaucracy, incomplete records or ordinary forensic uncertainty? (5) what conclusion is **not** justified by the available evidence?

### Confidence classifications

`proven` · `strongly supported` · `more likely than not` · `plausible` · `genuinely unresolved` · `unlikely` · `contradicted` · `not testable with the public record`

The generic phrase "no evidence" is deliberately avoided in favour of more precise formulations: insufficient evidence, indirect evidence, contested evidence, document unavailable, absence of a test, non-reproducible result.

For individual claims by witnesses and institutions the scale is different and closed (see [`docs/04`](docs/04-methodology-symmetric-skepticism.md) §4.2 and [`docs/03`](docs/03-phase2a-mfr-verification.md) §5):

`unsupported statement` · `document cited, not located` · `document located, not read` · `partially corroborated` · `corroborated` · `contradicted` · `inconclusive`

## Current status

- ✅ **Phase 1 — Technical audit v1** (`docs/01`): energy and kinematic analysis of the Towers' and WTC 7's collapse from NIST technical FAQs and peer-reviewed literature (Bažant & Verdure; Bažant & Le). Its own methodological limitations were identified in the following review.
- ✅ **Phase 2, first tranche — Adversarial documentary audit** (`docs/02`): explicit correction of the Phase 1 limitations; three declassified primary documents read in full (PDB Review Team memo; MFRs of Condoleezza Rice and Michael Scheuer); first H0–H7 matrix; first contradiction ledger.
- ✅ **Framing correction + Phase 2A instrument** (`docs/03`): five formulations from `02` corrected (H1, H5, Rice's "all reporting pointed abroad", the Commission's access structure, the three-dates rule); claim-by-claim verification table with 16 classified rows; Phase 2A priorities pre-registered.
- ✅ **Methodology and register update — 19 September 2026** (`docs/04`, `docs/claim-decomposition-register.md`, `docs/anomaly-register.md`): symmetric-skepticism principle adopted verbatim; symmetry requirements S1–S7; twelve-field atomic claim decomposition; anomaly register with mirror test; mandatory four-section phase reporting format. **No source read, no prior conclusion changed.**
- ✅ **Stress-test targeting plan — 19 September 2026** (`docs/05`, `docs/contradiction-ledger.md`): pre-registered targeting hypotheses across ST-1…ST-7 with P0–P3 research priorities; escalation ladder (discrepancy → unresolved anomaly → structured pattern → concealment → foreknowledge, no level skipped); cross-cutting attack patterns; conclusion ceilings fixed **before** reading; contradiction ledger created. **No source read, no conclusion changed.**
- 🔓 **Access restored.** The egress blockade recorded earlier on 19 September 2026 is lifted for `archives.gov`, `cia.gov`, `intelligence.senate.gov`, `nist.gov` and `oig.justice.gov`; `vault.fbi.gov` still refuses. Retrievability confirmed, readability not yet — see [`docs/05` §1](docs/05-stress-test-execution-plan.md).
- ⛔ **Official Account Stress-Test Track (ST-1 … ST-7): not executed.** Now unblocked; reading order in [`docs/05` §6](docs/05-stress-test-execution-plan.md).
- ⛔ **Phase 2B — Joint Inquiry Part Four: not executed.** Now unblocked. Classification protocol pre-registered in [`docs/03` §6](docs/03-phase2a-mfr-verification.md).
- ⏳ **Remaining phases**: see [`NEXT-STEPS.md`](NEXT-STEPS.md).

## Acknowledged limitations (read before citing this material)

- No source longer than a few dozen pages has been read in full so far — this includes the complete 9/11 Commission Report, the NIST NCSTAR volumes, the Hulsey/UAF report and the Moussaoui trial exhibits.
- Several of the 71 PDBs released by the CIA in September 2026 are scans without a searchable text layer and could not be read in this phase.
- Conclusions on H2, H3, H6 and H7 remain largely untested by the documents read so far.
- **H5 is not tested.** The al-Mihdhar / al-Hazmi node, where the hypothesis has its strongest theoretical case, has not been touched by any phase to date.
- **H1 does not support "cover-up".** What exists are indications of bureaucratic failure and possible institutional self-protection; deliberate suppression is not corroborated.
- **All three registers are empty.** The claim-decomposition register, the anomaly register and the contradiction ledger contain no substantive entries. Nothing in this repository should be read as if they were populated.
- **`docs/05` contains no findings.** Its T-items are pre-registered places to look, generated from the shape of the record rather than from reading it. Several are expected to resolve as ordinary. None may be cited as evidence in either direction.

## Content licence

This material is original analysis produced for personal research. Citations of government and academic sources follow the direct links listed in [`SOURCES.md`](SOURCES.md); no extensive third-party passages are reproduced — only paraphrase with attribution.
