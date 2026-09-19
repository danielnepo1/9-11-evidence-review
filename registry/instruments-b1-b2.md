# Instruments B1 and B2 — Quarantine Record and Definitions

> Living instrument. Governed by [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) §8.
> Opened 19 September 2026.

---

## 1. Repository-state notice — read this first

**No B1 artifact and no B2 artifact exist in this repository as of this commit.**

A search of the full repository history (`2e19844`, `f0007b5`) and of every tracked file finds no B1 instrument, no B1 versions, no hand-checks, no failure analysis, no held-out results, no B2 instrument and no B2 coding. The Phase A work that **is** present is: [`../docs/01`](../docs/01-wtc-engineering-audit-v1.md), [`../docs/02`](../docs/02-adversarial-audit-phase1.md), [`../docs/03`](../docs/03-phase2a-mfr-verification.md), [`../SOURCES.md`](../SOURCES.md), [`../NEXT-STEPS.md`](../NEXT-STEPS.md) and [`../README.md`](../README.md).

This file therefore does two things and does not pretend to do a third:

1. It records the **quarantine rule for B1** prospectively and permanently, so that the rule binds whenever a B1 artifact is introduced or recovered.
2. It records the **B2-ref / B2-rely instrument** as a definition, ready to apply.
3. It does **not** reconstruct B1 results or B2 codings from memory. Doing so would fabricate the very record the preservation rule exists to protect.

If B1/B2 artifacts exist outside this repository, they must be **committed as-is**, with their original hashes and failure record intact, before anything in this file is treated as applied.

---

## 2. B1 — invalidated instrument, permanent quarantine

**Status: INVALIDATED. Quarantined, not pending.**

| Rule | |
|---|---|
| **B1-Q1** | B1's numerical distributions are **never reused and never published**, in any document, table, summary or chart in this project |
| **B1-Q2** | B1's versions, hand-checks, failure analysis and held-out results are **preserved** wherever they exist. They are never deleted, edited in place, or quietly superseded |
| **B1-Q3** | Preservation is not rehabilitation. A preserved B1 artifact is evidence about the instrument's failure, not evidence about 9/11 |
| **B1-Q4** | Any future instrument that reuses B1's coding scheme, sampling frame or output scale inherits the quarantine until it is separately validated against a held-out set with its validation recorded |
| **B1-Q5** | The quarantine has no expiry and is not lifted by the passage of time, by new data, or by the absence of a better instrument |

**Why an invalidated instrument is preserved rather than removed.** A deleted failure cannot be audited, and its results cannot be traced if they have already propagated into downstream text. Preservation is what makes propagation detectable.

---

## 3. B2 — custodial-source instrument

The purpose of B2 is to make visible how much of a narrative rests on information obtained from people in custody — a provenance category with distinctive reliability problems and distinctive incentives on all sides.

### 3.1 The two tags

| Tag | Definition | What it measures |
|---|---|---|
| **B2-ref** | The note or document **mentions** detention, interrogation, or a custodial source | Visibility of the custodial channel in the record |
| **B2-rely** | A factual proposition **materially relies** on information derived from such a source | Evidentiary dependence on the custodial channel |

### 3.2 The non-summation rule

> **B2-ref and B2-rely are never summed, averaged, combined into a single index, or presented in one column as though they measured the same thing.**

They do not. A document may mention interrogation ten times while relying on it for nothing; another may mention it once while its central factual claim rests on it entirely. Any figure that adds them is meaningless, and any chart that stacks them is misleading.

### 3.3 Subtypes — never collapsed

Each tagged item carries exactly one subtype. Collapsing these into one "interrogation-derived" category destroys the distinctions that make the instrument worth having.

| Subtype | Distinguishing features |
|---|---|
| `cooperating-witness-in-custody` | Cooperation agreement, counsel typically present, testimony often subject to cross-examination |
| `fbi-302` | FBI interview record; a summary written by an agent, not a transcript |
| `commission-interview` | 9/11 Commission interview; MFR is a staff note, not a transcript; oath sometimes administered, sometimes not |
| `cia-detention-program-interrogation` | Produced inside the detention and interrogation programme. Coercion is a live variable per report |
| `foreign-liaison-interrogation` | Conditions of the interrogation and identity of the service frequently unevaluable |
| `ig-summary` | Inspector General summary of underlying material; derivative by construction |

### 3.4 Mandatory per-item fields

| Field | Notes |
|---|---|
| Tag | `B2-ref` or `B2-rely` |
| Subtype | From §3.3 |
| Detainee / source identity | Or `redacted` / `unknown` |
| Date of the statement | Distinguished from the date of the report |
| Coercion status | `documented` · `alleged` · `not indicated` · `unknown`. **`unknown` is the default** |
| Independent corroboration | Named, or `none` |
| Downstream dependents | Which registry rows would move if this source were withdrawn |

### 3.5 Application status

**Not applied.** The custodial-source corpus — the KSM, bin al-Shibh and Abu Zubaydah material, the SSCI report `CRPT-113srpt288`, the relevant FBI 302s — has not been read by this project. It is listed as a background item in [`../NEXT-STEPS.md`](../NEXT-STEPS.md) and is gated on [`source-policy.md`](source-policy.md).

Deliverable C-D6 in [`../docs/05` §5](../docs/05-phase-c-competing-narratives.md) tracks it.
