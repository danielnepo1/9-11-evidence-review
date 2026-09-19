> ## 🌐 English companion translation
>
> | | |
> |---|---|
> | **Source (authoritative)** | [`../README.md`](../README.md) (Portuguese) |
> | **Source SHA-256 at translation** | `f3974518c00feb978acd984937631868356dcd2adb90874c2dbe610e7552a024` |
> | **Translated** | 19 September 2026 |
> | **Status** | Faithful complete translation |
> | **Banner note** | The source carries a one-line English navigation banner pointing here. It is navigation, not content, and is not reproduced in the body below. The hash above is of the source **including** that banner |
>
> The Portuguese original is the authoritative record. Any disagreement is a **translation defect, to be corrected here and never in the original**. See [`TRANSLATION-POLICY.md`](TRANSLATION-POLICY.md). Sections of the source already written in English are reproduced verbatim.

---

# 9/11 Evidence Review

> Adversarial, document-based audit of the official 9/11 narrative — WTC structural engineering and pre-9/11 intelligence timeline, primary sources cited.

A systematic review of primary sources (NIST, the 9/11 Commission, CIA, NARA) across two tracks: (1) the physical plausibility of the Twin Towers and WTC 7 collapses, and (2) pre-9/11 intelligence failures. Method: steelman the official account → challenge it with primary evidence → judge without a fixed prior conclusion. Every claim is tagged with a confidence level, and every source is logged with access date, extent read, and known limitations.

---

## ⚠️ Controlling framework (added 19 September 2026)

*(Reproduced verbatim from the source, where it is already in English.)*

**The methodology of this project changed on 19 September 2026.** A permanent framework for provenance, source independence, competing-hypothesis testing and symmetric treatment of official and alternative narratives was adopted and now governs everything below.

**Read these first. Where they conflict with anything else in this repository, they prevail.**

| Document | What it is |
|---|---|
| [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) | **Controlling methodology.** The baseline axiom, the three workstreams, explanation classes EC1–EC5, closure gates, document-card language, preservation and language rules, and the register of methodological decisions MD-001 … MD-014 |
| [`../docs/05-phase-c-competing-narratives.md`](../docs/05-phase-c-competing-narratives.md) | **Phase C — Competing Narratives and Independent Evidence.** Runs across Phases 2A–4, not after them |
| [`../registry/`](../registry/) | The living instruments: atomic claim registry, provenance graph, version-history ledger, discrepancy ledger, source policy, witness-status register, B1/B2 instruments, document cards |
| [`../corpus/manifest.md`](../corpus/manifest.md) | Retrieved artifacts, hashes, extraction tooling |

Two rules from that framework that change how everything in this README should be read:

1. **Reading official documents establishes the baseline. It cannot independently validate the baseline.** A claim appearing in an official document is thereby established as *officially asserted*, not as true. Corroboration requires a source whose provenance root is independent — and repeated publications sharing one root are not independent.
2. **Equal procedural treatment; evidentiary weight proportional to provenance, independence, contemporaneity, auditability and corroboration.** Alternative and critical claims are held to exactly this standard — no lower, and no higher.

**Language.** All artifacts added from 19 September 2026 onward are written in English. The Portuguese documents (`01`–`03`, the source README, `SOURCES.md`, `NEXT-STEPS.md`) are **preserved verbatim as the Phase A historical record**, and complete English companions live in [`./`](.) — see [`TRANSLATION-POLICY.md`](TRANSLATION-POLICY.md).

**Status of the hypotheses.** H0–H7 are **unchanged** by the adoption of this framework. Building the instrument is not evidence (MD-009).

---

## About this project

This repository documents an ongoing audit, made in two passes, of the official narrative of the attacks of 11 September 2001. The aim is neither to confirm nor to refute the official version, but to subject it — and the alternative hypotheses — to the same evidentiary standard, with full source traceability.

**The honesty standard adopted:** no conclusion is presented without indicating whether the underlying document was read in full, in part, or known only through a summary/FAQ/press release. Where that was not possible within a session, the repository records the fact explicitly rather than filling the gap with unverified prior knowledge.

## Structure

```
9-11-evidence-review/
├── README.md                              ← this file (Portuguese source)
├── docs/
│   ├── 01-wtc-engineering-audit-v1.md     ← first audit (WTC structural engineering)
│   ├── 02-adversarial-audit-phase1.md     ← second audit (adversarial, multi-hypothesis, Phase 1)
│   ├── 03-phase2a-mfr-verification.md     ← framing correction + verification instrument (Phase 2A)
│   ├── 04-controlling-methodology.md      ← CONTROLLING framework (EN, 19/09/2026) — prevails over everything
│   └── 05-phase-c-competing-narratives.md ← Phase C: Competing Narratives and Independent Evidence (EN)
├── en/                                    ← English companion translations of the Portuguese documents
├── registry/                              ← living instruments (EN)
│   ├── claims.md                          ← atomic claim registry (A<n>.<k>, T-nn, U-nn, C-nn)
│   ├── provenance.md                      ← provenance / source-independence graph
│   ├── version-history.md                 ← version ledger + repository change events
│   ├── discrepancies.md                   ← discrepancy ledger + controlled taxonomy
│   ├── source-policy.md                   ← inclusion / provenance / preservation / dedup rules
│   ├── witness-status.md                  ← procedural status per witness document
│   ├── instruments-b1-b2.md               ← B1 quarantine; B2-ref / B2-rely
│   └── cards/                             ← document cards (DOC-n)
├── corpus/
│   ├── manifest.md                        ← retrieved artifacts, hashes, extraction tooling
│   └── text/                              ← preserved extracted text
├── SOURCES.md                             ← consolidated bibliography of both audits
└── NEXT-STEPS.md                          ← roadmap of the next phases (2A, 2B, 3, 4)
```

### Reading order

The numbering of the documents is chronological **and** hierarchical: each later document corrects the earlier one, and where there is conflict **the higher number always prevails**.

| Order | File | Role | How to read it |
|---|---|---|---|
| 1 | [`README.md`](../README.md) | Method, hypotheses H0–H7, confidence scale | Entry point — defines the vocabulary used in the rest |
| 2 | [`docs/01-wtc-engineering-audit-v1.md`](../docs/01-wtc-engineering-audit-v1.md) | First pass, engineering | **Historical record.** Do not cite in isolation: several points were retracted |
| 3 | [`docs/02-adversarial-audit-phase1.md`](../docs/02-adversarial-audit-phase1.md) | Phase 1, documentary | Section 2 lists what was retracted from `01`; sections 3–6 are the substantive finding. **Read it together with the corrections in `03` §1** |
| 4 | [`docs/03-phase2a-mfr-verification.md`](../docs/03-phase2a-mfr-verification.md) | **Current framing + verification instrument** | §1 corrects five formulations in `02`; §5 is the claim-by-claim status table; §7 is the current state of H1–H5 |
| 5 | [`SOURCES.md`](../SOURCES.md) | Consolidated bibliography with reading status | Consult before giving weight to any assertion |
| 6 | [`NEXT-STEPS.md`](../NEXT-STEPS.md) | Execution roadmap (Phases 2A, 2B, 3, 4) | Starting point of any new session |

**Reference vs. next step:** items 1–5 are **reference** material (what is established and on what basis); item 6 is the **execution** queue. A new session starts by reading 1, 4 and 6 — `01` is needed only when the work touches structural engineering, and then always together with section 2 of `02`; `02` always read with the erratum in `03` §1 to hand.

**Precedence rule on framing:** where `02` and `03` diverge in classifying a hypothesis or a claim, **`03` prevails**.

## Methodology

The audit follows three explicitly declared passes:

1. **Official steelman** — build the best possible version of the official explanation (NIST, the 9/11 Commission).
2. **Red team** — build the strongest possible critique using primary documents, internal contradictions and later-released data.
3. **Judge** — compare the two without starting from a desired conclusion.

### Hypotheses kept separate

For the intelligence/institutional-response dimension, eight hypotheses are treated as distinct categories, each requiring its own evidence (evidence for one is never automatically treated as evidence for another):

| # | Hypothesis |
|---|---|
| H0 | Attack planned by al-Qaeda; institutional failures and the structural explanation essentially correct |
| H1 | H0 + self-protection/misleading statements/subsequent cover-up of incompetence, without operational prior knowledge |
| H2 | H0 + conscious logistical support by individuals linked to a foreign government, without proof of higher authorisation |
| H3 | Broader foreign institutional support or protection |
| H4 | US authorities had sufficient warnings but failed through negligence/fragmentation/political priorities |
| H5 | Segments of the US authorities had specific operational knowledge and deliberately did not prevent the attack |
| H6 | The mechanism of one or more collapses was significantly different from that presented by NIST |
| H7 | Additional deliberate intervention in the buildings |

### Evidentiary framing rule

> Access restriction, generic warning and interested testimony are not — singly or together — proof of cover-up or of prior knowledge.

Three corollaries of mandatory application:

1. **A new document ≠ a new fact.** Every citation distinguishes the **event date**, the **document date** and the **declassification date**. A 2004 record declassified in 2026 is 2004 memory, not a contemporaneous 2001 record.
2. **Each step requires its own evidence.** Process failure → institutional self-protection → deliberate suppression → operational prior knowledge are four distinct propositions; evidence of one is never promoted to evidence of the next.
3. **Reading is reading.** A summary, FAQ, press release, search excerpt or third-party report does not sustain a status of `corroborada` (corroborated) or `contradita` (contradicted).

### Confidence classifications used

`proven` · `strongly supported` · `more likely than not` · `plausible` · `genuinely unresolved` · `unlikely` · `contradicted` · `not testable on the public record`

The generic phrase "no evidence" is deliberately avoided in favour of more precise formulations: insufficient evidence, indirect evidence, contested evidence, document unavailable, absence of testing, non-replicable result.

For individual witness claims the scale is different and closed (see [`docs/03`](../docs/03-phase2a-mfr-verification.md) §5):

`declaração não corroborada` · `documento citado, não localizado` · `documento localizado, não lido` · `parcialmente corroborada` · `corroborada` · `contradita` · `inconclusiva`

*(uncorroborated statement · document cited, not located · document located, not read · partially corroborated · corroborated · contradicted · inconclusive — kept in Portuguese as identifiers.)*

## Current status

- ✅ **Phase 1 — Technical audit v1** (`docs/01`): energy and kinetic analysis of the collapse of the Towers and WTC 7 from NIST's technical FAQs and peer-reviewed literature (Bažant & Verdure, Bažant & Le). Its own methodological limitations identified in the following review.
- ✅ **Phase 2, first tranche — Adversarial documentary audit** (`docs/02`): explicit correction of the Phase 1 limitations; full reading of three primary documents declassified in September 2026 (PDB Review Team memo, MFRs of Condoleezza Rice and Michael Scheuer); first H0–H7 matrix; first contradiction ledger.
- ✅ **Framing correction + Phase 2A instrument** (`docs/03`): five formulations in `02` corrected (H1, H5, Rice's "all reporting pointed abroad", the Commission's access structure, the three-dates rule); claim-by-claim verification table with 16 classified rows; Phase 2A priorities pre-registered.
- 🔄 **Phase 2A — in execution.** Network access restored on 19/09/2026 (`archives.gov` returns HTTP 200; the record of the earlier failure is preserved in [`docs/03` §3](../docs/03-phase2a-mfr-verification.md)). **DOC-7 — MFR George Tenet #2 (22/01/2004) — read in full (24/24 pp.) and carded**, with image verification of pp. 3, 4, 5 and 19: [`registry/cards/DOC-7-mfr-tenet-2.md`](../registry/cards/DOC-7-mfr-tenet-2.md). Eight MFRs remain.
- ✅ **Methodological framework v2 + Phase C** (`docs/04`, `docs/05`, `registry/`, `corpus/`): see the block at the top of this file.
- ⛔ **Phase 2B — Part Four of the Joint Inquiry: not executed.** Classification protocol pre-registered in [`docs/03` §6](../docs/03-phase2a-mfr-verification.md).
- ⏳ **Next phases**: see [`NEXT-STEPS.md`](../NEXT-STEPS.md).

## Acknowledged limitations (read before citing this material)

- No source longer than a few dozen pages has been read in full so far — this includes the complete 9/11 Commission Report, NIST's NCSTAR volumes, the Hulsey/UAF report and the Moussaoui exhibits.
- Several of the 71 PDBs released by CIA in September 2026 are scans with no searchable text layer and could not be read in this phase.
- Conclusions about H2, H3, H6 and H7 remain largely untested by the documents read so far.
- **H5 is untested.** The al-Mihdhar/al-Hazmi node, where the hypothesis has its best theoretical case, was not touched by any phase up to that point.
- **H1 does not sustain "cover-up".** What exists are indications of bureaucratic failures and of possible institutional self-protection; deliberate suppression is not corroborated.

## Content licence

This material is original analysis produced for personal research purposes. Citations of governmental and academic sources follow the direct links listed in [`SOURCES.md`](../SOURCES.md); no extensive third-party passage is reproduced — only paraphrase with attribution.
