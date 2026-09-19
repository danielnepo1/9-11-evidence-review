# Phase C — Competing Narratives and Independent Evidence

> **Status: open, defined, partially executed.** Opened 19 September 2026 under [`04-controlling-methodology.md`](04-controlling-methodology.md).
>
> Phase C is not a replacement for Phases 2A, 2B, 3 and 4 in [`../NEXT-STEPS.md`](../NEXT-STEPS.md). It runs **across** them. Phases 2A–4 say *which documents to read*; Phase C says *what has to be true before anything read in them may be treated as established*.

---

## 1. Why this phase exists

Phase A (documents `01`–`03`) read official documents and recorded what they say. That work is preserved and is not repeated here. What it cannot do — by construction, and regardless of how carefully it was done — is validate itself: see the baseline axiom, [`04` §0.2](04-controlling-methodology.md).

Phase C exists to supply the three things Phase A structurally could not:

1. an **independence test** for every corroboration Phase A recorded;
2. a **symmetric registry** for critical and alternative claims, held to the same standard as official ones;
3. a **discriminating-evidence discipline** — for each discrepancy, what observation would separate the competing explanations.

---

## 2. Scope

| In scope | Out of scope |
|---|---|
| Any claim already in [`../registry/claims.md`](../registry/claims.md) | Broad re-narration of 9/11 |
| Any claim in the C-series (critical / alternative) | Adjudicating authors, communities or documentaries as wholes |
| Provenance roots of documents already read | Corpus expansion outside [`../registry/source-policy.md`](../registry/source-policy.md) |
| Version history of official wording | Numerical probability assignment |

---

## 3. Entry conditions (all met as of this commit)

| # | Condition | State |
|---|---|---|
| C-E1 | Controlling methodology adopted | ✅ [`04`](04-controlling-methodology.md) |
| C-E2 | Atomic claim registry exists | ✅ [`../registry/claims.md`](../registry/claims.md) |
| C-E3 | Provenance / source-dependency structure exists | ✅ [`../registry/provenance.md`](../registry/provenance.md) |
| C-E4 | Version-history ledger exists | ✅ [`../registry/version-history.md`](../registry/version-history.md) |
| C-E5 | Discrepancy ledger and controlled taxonomy exist | ✅ [`../registry/discrepancies.md`](../registry/discrepancies.md) |
| C-E6 | Competing-hypothesis fields (EC1–EC5) present in the matrix | ✅ [`../registry/claims.md`](../registry/claims.md) §4 |
| C-E7 | Source-inclusion / preservation / dedup policy defined **before** corpus expansion | ✅ [`../registry/source-policy.md`](../registry/source-policy.md) |
| C-E8 | B1 quarantine and B2-ref/B2-rely separation recorded | ✅ [`../registry/instruments-b1-b2.md`](../registry/instruments-b1-b2.md) |

---

## 4. Workstream execution order

Phase C work is pulled, not pushed: a document is read because a registry row needs it, never because it is available.

### C-W1 — Official baseline reconstruction (per body, per date)

For each body that spoke on a claim, record the statement, its date, its cited source, its expressed certainty, and every later change of wording. Bodies are **never merged** into "the government said". Output: rows in [`../registry/version-history.md`](../registry/version-history.md).

### C-W2 — Independent and contemporaneous records

For each consequential proposition, walk the provenance chain to the earliest recoverable source and record where it stops and why. Output: rows in [`../registry/provenance.md`](../registry/provenance.md), including every `independence: unknown` verdict.

Current highest-value targets, all derived from documents already read (not from speculative search):

| Target | Which row it would move | Why it is independent of the reading corpus |
|---|---|---|
| Memorandum memorializing the May 1998 cancellation decision, or its absence established by records search | A3.1, A3.2, A5.2, T-01, T-03 | Contemporaneous 1998 record vs. 2003–2004 recollection |
| **The DCI's January 2004 briefing binder** (DOC-7 "TO OBTAIN FROM CIA" item 2) | T-06, T-07, U-08, U-10 | Converts four recollection rows into rows testable against a dated document — see [`../registry/provenance.md`](../registry/provenance.md) PR-011 |
| The 2000–2001 operational record on the Kuala Lumpur meeting (Joint Inquiry, DOJ IG, PENTTBOM) | U-01, U-02, U-04, U-06, Priority 1 | **Every step of the DOC-8 chain for this node stops in 2004** — PR-012 |
| MFR Berger, 14 Jan 2004 | A3.2, U-09 | Two independent rows now require it |
| February 1999 MON with the President's handwritten edits | T-08 | Primary instrument, quoted aloud but not in the corpus |
| June 1999 Berger→Clinton memo (likely drafted by Clarke) | T-11 | Contemporaneous 1999 record summarising CT state |
| State Department / diplomatic cable traffic on the UAE hunting-camp warning | T-09 | Contemporaneous cable vs. participants' recollection |
| Scheuer memoranda of 28 Jun 1999, 3 May 1996; Spot Report 24 Jun 1997 | A1.2, A1.3, A4.1, A4.5 | The documents the DOC-3 claims rest on |
| Situation Room log and Presidential Diary, 11 Sep 2001 | A12.1 | Contemporaneous timestamped record |

### C-W3 — Critical and alternative claim registry (C-series)

Not yet populated. **This is deliberate.** Populating it requires the source-inclusion rules in [`../registry/source-policy.md`](../registry/source-policy.md) to be applied to a defined candidate set; doing it from memory or from unconstrained search would violate [`04` §10](04-controlling-methodology.md) and would import exactly the provenance failures the phase exists to detect.

The C-series opens when, and only when:

1. a candidate-source list is assembled under [`../registry/source-policy.md`](../registry/source-policy.md) §2;
2. each candidate is scored on the §3 provenance fields **before** any claim is extracted from it;
3. every extracted claim is decomposed atomically and carries a named claimant, date and cited underlying record.

> Symmetry note, binding: a C-series row identifying a real inconsistency in the official account is thereby established only as *an identified inconsistency*. It is not thereby evidence for any alternative account. The inconsistency and the explanation of the inconsistency are two propositions.

---

## 5. Deliverables

| ID | Deliverable | State |
|---|---|---|
| C-D1 | Every A-series container decomposed into atomic propositions | ✅ |
| C-D2 | EC1–EC5 columns populated for every discrepancy in the ledger | ⏳ **partial.** DISC-001, DISC-002, DISC-003, DISC-005, DISC-006, DISC-007, DISC-010 meet the six-field specification of [`../docs/04`](04-controlling-methodology.md) §5. **DISC-004, DISC-008, DISC-009 and DISC-011 do not** — their EC analysis is prose, not the six fields. Downgraded 19 Sep 2026 (defect #34) |
| C-D3 | Provenance root recorded for every proposition with `status ≠ declaração não corroborada` | ⏳ partial |
| C-D4 | Re-carding of DOC-1, DOC-2, DOC-3 under the image-verification standard | ⛔ **blocking gate** for A10, A16 and dependents — still closed as of 19 Sep 2026 |
| C-D5 | C-series populated under the source policy | ⛔ not started — gated on §4 C-W3 |
| C-D6 | B2-ref / B2-rely instrument applied to the custodial-source corpus | ⛔ not started — corpus not read |
| C-D7 | Complete English companion translations of every Portuguese document | ✅ [`../en/`](../en/) |
| C-D8 | Repository-wide audit of evidentiary wording ("under oath" / "sworn") | ✅ [`../registry/witness-status.md`](../registry/witness-status.md) |

---

## 6. Exit conditions

Phase C does not "complete". It is a standing discipline. It reaches **steady state** when every row in [`../registry/claims.md`](../registry/claims.md) carries: a provenance root or an explicit `unknown`; an independence verdict; an EC analysis where a discrepancy exists; and an explicit closure condition.

---

## 7. What this phase must not be used to do

- Not to argue that the official narrative has been broken. At this stage the project is building the machinery capable of testing official **and** alternative narratives without granting either side automatic authority.
- Not to promote an identified inconsistency into an alternative explanation.
- Not to treat an inaccessible or redacted source as evidence of concealment.
- Not to treat the absence of a document as proof of its destruction.
