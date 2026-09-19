# 9/11 Evidence Review

> Adversarial, document-based audit of the official 9/11 narrative — WTC structural engineering and pre-9/11 intelligence timeline, primary sources cited.

A systematic review of primary sources (NIST, the 9/11 Commission, CIA, NARA) across two tracks: (1) the physical plausibility of the Twin Towers and WTC 7 collapses, and (2) pre-9/11 intelligence failures. Method: steelman the official account → challenge it with primary evidence → judge without a fixed prior conclusion. Every claim is tagged with a confidence level, and every source is logged with access date, extent read, and known limitations.

---

## Impartiality rule (permanent, applies retroactively and prospectively)

> "The official account and every alternative account are competing hypotheses. No hypothesis receives a presumption of truth, falsity, credibility, or implausibility because it is official, institutional, popular, politically inconvenient, or labeled conspiratorial. All hypotheses must be tested against the same evidentiary standards, alternative explanations, predicted observations, and burden of proof."

This rule governs every document in this repository, past and future. The official narrative is not treated as a true baseline that alternative hypotheses must overcome; it is one hypothesis among several, tested against the same standard as the others. Evidentiary gaps, redactions, or unresolved questions are never themselves treated as proof of an alternative hypothesis — a gap is a gap, not a finding.

The rule requires strict differentiation between six distinct propositions, none of which automatically proves the next:

- institutional failure;
- bureaucratic self-protection;
- incomplete investigation;
- deliberate suppression;
- prior operational knowledge;
- material intervention.

Where earlier wording in this repository (including in `docs/01` and `docs/02`) treated the official account as a default baseline, or implied that a gap in the record supported a specific alternative hypothesis, that wording is superseded by this rule. See `docs/03-phase2a-mfr-verification.md` §1 for the standing framework corrections this rule reinforces.

## About this project

This repository documents an audit in progress, conducted in two passes, of the official narrative of the September 11, 2001 attacks. The goal is neither to confirm nor to refute the official version, but to subject it — and the alternative hypotheses — to the same evidentiary standard, with full source traceability.

**Honesty standard adopted:** no conclusion is presented without indicating whether the underlying document was read in full, read partially, or only known through a summary/FAQ/press release. Where this was not possible within a session, the repository records that explicitly rather than filling the gap with unverified prior knowledge.

## Structure

```
9-11-evidence-review/
├── README.md                              ← this file
├── docs/
│   ├── 01-wtc-engineering-audit-v1.md     ← first audit (WTC structural engineering)
│   ├── 02-adversarial-audit-phase1.md     ← second audit (adversarial, multi-hypothesis, Phase 1)
│   └── 03-phase2a-mfr-verification.md     ← framework correction + verification instrument (Phase 2A)
├── SOURCES.md                             ← consolidated bibliography for both audits
└── NEXT-STEPS.md                          ← roadmap for upcoming phases (2A, 2B, 3, 4)
```

### Reading order

Document numbering is both chronological **and** hierarchical: each later document corrects the previous one, and wherever there is a conflict, **the higher-numbered document always prevails**.

| Order | File | Role | How to read it |
|---|---|---|---|
| 1 | [`README.md`](README.md) | Method, hypotheses H0–H7, confidence scale | Entry point — defines the vocabulary used in the rest |
| 2 | [`docs/01-wtc-engineering-audit-v1.md`](docs/01-wtc-engineering-audit-v1.md) | First pass, engineering | **Historical record.** Do not cite in isolation: several points were retracted |
| 3 | [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md) | Documentary Phase 1 | Section 2 lists what was retracted from `01`; sections 3–6 are the substantive finding. **Read together with the corrections in `03` §1** |
| 4 | [`docs/03-phase2a-mfr-verification.md`](docs/03-phase2a-mfr-verification.md) | **Governing framework + verification instrument** | §1 corrects five formulations from `02`; §5 is the claim-by-claim status table; §7 is the current state of H1–H5 |
| 5 | [`SOURCES.md`](SOURCES.md) | Consolidated bibliography with reading status | Consult before assigning weight to any statement |
| 6 | [`NEXT-STEPS.md`](NEXT-STEPS.md) | Execution roadmap (Phases 2A, 2B, 3, 4) | Starting point for any new session |

**Reference vs. next step:** items 1–5 are **reference** material (what is already established, and on what basis); item 6 is the **execution** queue. A new session starts by reading 1, 4, and 6 — `01` is only needed when the work touches structural engineering, and in that case always alongside section 2 of `02`; `02` is always read together with the errata in `03` §1.

**Precedence rule on framing:** where `02` and `03` diverge on the classification of a hypothesis or a claim, **`03` prevails**.

## Methodology

The audit follows three explicitly declared passes:

1. **Official steelman** — build the strongest possible version of the official explanation (NIST, the 9/11 Commission).
2. **Red team** — build the strongest possible critique using primary documents, internal contradictions, and later-released data.
3. **Judge** — compare the two without starting from a desired conclusion.

See the impartiality rule above: neither the official account nor any alternative hypothesis is granted a presumption in this process.

### Hypotheses kept separate

For the intelligence/institutional-response dimension, eight hypotheses are treated as distinct categories, each requiring its own evidence (evidence for one is never automatically treated as evidence for another):

| # | Hypothesis |
|---|---|
| H0 | Attack planned by al-Qaeda; institutional failures and the structural explanation are essentially correct |
| H1 | H0 + self-protection/misleading statements/after-the-fact cover-up of incompetence, without prior operational knowledge |
| H2 | H0 + conscious logistical support by individuals tied to a foreign government, without proof of higher authorization |
| H3 | Broader foreign institutional support or protection |
| H4 | US authorities had sufficient warnings but failed due to negligence/fragmentation/political priorities |
| H5 | Segments of the authorities had specific operational knowledge and deliberately failed to prevent the attack |
| H6 | The collapse mechanism of one or more buildings was significantly different from what NIST presented |
| H7 | Additional deliberate intervention in the buildings |

### Evidentiary framing rule

> Access restriction, generic warning, and interested testimony are not — alone or combined — proof of cover-up or of prior knowledge.

Three corollaries of mandatory use:

1. **A new document ≠ a new fact.** Every documentary citation distinguishes **event date**, **document date**, and **declassification date**. A 2004 record declassified in 2026 is 2004 memory, not a contemporaneous 2001 record.
2. **Each rung requires its own evidence.** Process failure → institutional self-protection → deliberate suppression → prior operational knowledge are four distinct propositions; evidence for one is never promoted to evidence for the next.
3. **Reading is reading.** A summary, FAQ, press release, search snippet, or third-party news report does not support a `corroborated` or `contradicted` status.

### Confidence classifications used

`proven` · `strongly supported` · `more likely than not` · `plausible` · `genuinely unresolved` · `unlikely` · `contradicted` · `not testable with the public record`

The generic phrase "no evidence" is deliberately avoided in favor of more precise formulations: insufficient evidence, indirect evidence, contested evidence, document unavailable, test not performed, result not replicable.

For individual witness claims, a separate, closed scale is used (see [`docs/03`](docs/03-phase2a-mfr-verification.md) §5):

`uncorroborated statement` · `document cited, not located` · `document located, not read` · `partially corroborated` · `corroborated` · `contradicted` · `inconclusive`

## Current status

- ✅ **Phase 1 — Technical audit v1** (`docs/01`): energy and kinetic analysis of the Towers' and WTC 7's collapse, based on NIST's technical FAQs and peer-reviewed literature (Bažant & Verdure, Bažant & Le). Methodological limitations of its own were identified in the subsequent review.
- ✅ **Phase 2, first tranche — Adversarial documentary audit** (`docs/02`): explicit correction of Phase 1's limitations; full reading of three primary documents declassified in September 2026 (PDB Review Team memo, MFRs of Condoleezza Rice and Michael Scheuer); first H0–H7 matrix; first contradiction ledger.
- ✅ **Framework correction + Phase 2A instrument** (`docs/03`): five formulations from `02` corrected (H1, H5, Rice's "all reporting pointed abroad", the Commission's access structure, the three-dates rule); claim-by-claim verification table with 16 classified lines; Phase 2A priorities pre-registered.
- ⛔ **Phase 2A — reading of the remaining nine MFRs: not executed.** Network egress blocked for `archives.gov` and all other primary repositories, documented in [`docs/03` §3](docs/03-phase2a-mfr-verification.md).
- ⛔ **Phase 2B — Part Four of the Joint Inquiry: not executed.** Same block (`intelligence.senate.gov`). Classification protocol pre-registered in [`docs/03` §6](docs/03-phase2a-mfr-verification.md).
- ⏳ **Next phases**: see [`NEXT-STEPS.md`](NEXT-STEPS.md).

> **Note (language/governance migration pass):** this status list has not been reconciled with the fuller Phase 2A progress recorded in `docs/03` (access was later reopened and the nine MFRs plus the PDB of 08/06/2001 were read in full). That reconciliation is a substantive update to the investigation record, not a language change, and is intentionally left for a separate, dedicated pass rather than folded into this migration commit.

## Acknowledged limitations (read before citing this material)

- No source longer than a few dozen pages has been read in full to date — this includes the complete 9/11 Commission Report, NIST's NCSTAR volumes, the Hulsey/UAF report, and the Moussaoui case exhibits.
- Several of the 71 PDBs released by the CIA in September 2026 are scans without a searchable text layer and could not be read in this phase.
- Conclusions on H2, H3, H6, and H7 remain largely untested by the documents read so far.
- **H5 is not tested.** The al-Mihdhar/al-Hazmi node, where the hypothesis has its strongest theoretical case, has not been touched by any phase so far.
- **H1 does not support "cover-up."** What exists is evidence of bureaucratic failures and possible institutional self-protection; deliberate suppression is not corroborated.

## Content usage license

This material is original analysis produced for personal research purposes. Citations of government and academic sources follow the direct links listed in [`SOURCES.md`](SOURCES.md); no extensive third-party excerpt is reproduced — only attributed paraphrase.
