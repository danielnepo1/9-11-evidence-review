# Audit Program v2 — Execution Sequence

> **Status: controlling execution document.** Supersedes [`../NEXT-STEPS.md`](../NEXT-STEPS.md) under the repository's precedence rule (higher document number prevails). `NEXT-STEPS.md` is preserved frozen as the historical roadmap.
>
> Adopted **19 September 2026**, under [`04-controlling-methodology.md`](04-controlling-methodology.md), which remains the controlling *methodology*. This document programs *what is done next*, not *what is true*.

---

## 1. Why the roadmap was re-programmed

Three reasons, in descending order of importance.

**The published queue was falsified by its own execution.** `NEXT-STEPS.md` ordered Tenet #3 second on two stated premises: that DOC-7's footnote named it as the session covering the February 1999 MON, and that it was the first place DOC-7's 27 declared follow-up items could have been answered. Reading it as DOC-8 **falsified both** — zero occurrences of `February 1999` or `1999 MON`, and no follow-up list at all. That falsification is what produced [DISC-007](../registry/discrepancies.md#disc-007). The queue was never updated, leaving two live conflicting queues in the repository.

**The binding constraint flipped.** `NEXT-STEPS.md` and `docs/03` §3/§8 were written under a total network egress block, when every primary repository returned 403. Every one of them is now reachable. The limit is no longer *access*; it is **verification attention per page**. An order fixed when nothing was reachable cannot be the right order now.

**The ledger carried 34 internal defects**, found by an independent adversarial pass and corrected in the two preceding commits. Reading further onto a defective ledger compounds the error.

## 2. Ordering principle

> **Discriminating power per unit of verification cost** — and, before that, **debts already owed on documents already retrieved.**

Work already paid for comes first: a page image from a file that is downloaded and hashed costs minutes and unblocks rows that are otherwise half-built. Only then does new retrieval begin, and each retrieval is **pulled by a named registry row** ([`../registry/source-policy.md`](../registry/source-policy.md) I1), never by availability.

Every step below is specified as: **pulling row · instrument exercised · expected output · closure condition · stop condition.**

---

## 3. The program

### Step 1 — Image-verify DOC-7 printed p.12

| | |
|---|---|
| **Pulling row** | [DISC-007](../registry/discrepancies.md#disc-007) footnote 1; [DISC-004](../registry/discrepancies.md#disc-004) (the Pakistan quotation, A7.2) |
| **Instrument** | [`04`](04-controlling-methodology.md) §7.2 image-verification standard |
| **Expected output** | The exact reading of footnote 1's session date; verification or correction of Q14 |
| **Closure condition** | Both quotations transcribed from the page image and recorded on the DOC-7 card |
| **Stop condition** | If the footnote digit is illegible on the image, record it as illegible and **do not infer** — `04` §7.7 |

Owed twice, costs one page render, and the file is already retrieved and hashed. `discrepancies.md` names it as the required next step.

### Step 2 — Render and verify DOC-8 printed pp. 2, 11, 12

| | |
|---|---|
| **Pulling row** | U-04, U-05, U-06, U-18 |
| **Instrument** | §7.2 |
| **Expected output** | Q15–Q18 image-verified or corrected |
| **Closure condition** | The four rows cease to carry the "may not move another row" flag |
| **Stop condition** | A redaction void invisible in the text layer, as on DOC-7 p.4 — record it and re-scope the affected rows |

**U-04 (CIA asked NSA to watchlist al-Midhar) is the most H5-relevant *process* claim anywhere in the corpus**, and it is stalled for want of one page image from a file already on disk.

### Step 3 — Read DOC-9, MFR George Tenet #1 (23 December 2003), in full

| | |
|---|---|
| **Pulling row** | [DISC-007](../registry/discrepancies.md#disc-007), [DISC-008](../registry/discrepancies.md#disc-008) — both **P0** in [`anomalies.md`](../registry/anomalies.md) |
| **Instrument** | Full card under §7; [`witness-status.md`](../registry/witness-status.md) §2 procedural status; MD-011 variant search |
| **Expected output** | Whether an MFR omits content from its own session; whether "his first interview on January 22, 2004" is accurate |
| **Closure condition** | DISC-007 and DISC-008 resolved or their EC analysis narrowed, **and the silence-calibration result recorded explicitly** |
| **Stop condition** | If DOC-9 is a briefing rather than an interview, DISC-008's EC1 is confirmed and DISC-007 still needs another MFR pair — say so rather than stretching the finding |

276,335 bytes. At this release's observed 79–108 KB/page that is **2–4 pages** — full image verification of every page in one pass. Against that, it resolves the two P0 rows, and DISC-007 **prices every silence in the corpus**: T-N1, U-N1, U-N2 and every future negative finding are worth whatever this answer says they are worth. DOC-8's `oath: carried over` also rests on the disputed front matter, a contingency **18 U-rows inherit**.

### Step 4 — Re-carding gate: DOC-1, DOC-2, DOC-3 against page images

| | |
|---|---|
| **Pulling row** | C-D4; A8.2, A9.1, A10.1, A10.2, A15.1–A15.4, A16.1 |
| **Instrument** | §7.2, §7.3; `witness-status.md` for DOC-3's unverified oath |
| **Expected output** | Three cards in the current format; DOC-3's oath image-verified or downgraded |
| **Closure condition** | The gate lifts for the eight rows — subject to §9.1: lifting a gate permits closure, it does not perform it |
| **Stop condition** | A redaction or OCR defect that changes a Phase A reading — record it as a correction event, **do not edit `docs/02` or `docs/03`** (Tier 1) |

~42 pages. **The only blocking gate in the repository that requires no retrieval at all.** Deferred twice; dated here. It does not gate steps 1–3, 5 or 6, so it may run in parallel — but it may not be deferred a third time without an explicit recorded reason.

### Step 5 — Read DOC-10, MFR Sandy Berger (14 January 2004)

| | |
|---|---|
| **Pulling row** | A3.2 **and** U-09 ([DISC-010](../registry/discrepancies.md#disc-010)) |
| **Instrument** | Full card; PR-013 |
| **Expected output** | Berger's own account of the May 1998 cancellation notification and of the *Cole* judgment |
| **Closure condition** | PR-013 stops being a staff paraphrase inside another witness's MFR |
| **Stop condition** | If Berger's MFR is itself silent, that is a DISC-007-class finding and is recorded as one |

2.97 MB. Two independent rows need it.

### Step 6 — DOJ OIG admission, under the pre-registered constraints in §4

| | |
|---|---|
| **Pulling row** | T-12 (its closure condition names "DOJ IG reports"); U-02, U-04, U-06; the PR-012 chain-stop |
| **Instrument** | Full I1–I4 admission record; MD-022 institutional-failure taxonomy; MD-021 negative-evidence test |
| **Expected output** | The FBI-side handling record; a Priority 6 answer in the eleven-category taxonomy; harvested citations to contemporaneous instruments |
| **Closure condition** | Priority 6 answered in category terms, **not** Priority 1 — see §4 |
| **Stop condition** | Any decisive quotation that cannot be located in the PDF at a printed page — §7.7 |

**After step 3**, with the silence-calibration result in hand.

### Step 7 — Harvest citations; pull the contemporaneous instruments

| | |
|---|---|
| **Pulling row** | New PR rows created by step 6 |
| **Instrument** | `provenance.md` §4; `source-policy.md` D1–D5 |
| **Expected output** | Named, dated 2000–2001 instruments pulled from the **already-admitted** court-exhibit and FBI Vault repositories |
| **Closure condition** | At least one chain reaches a contemporaneous record rather than stopping in 2004 |
| **Stop condition** | A cited instrument that exists only inside the OIG report's footnotes — record the chain-stop |

The contemporaneous instrument outranks the 2004 synthesis ([`04`](04-controlling-methodology.md) §0.1). These repositories are already admitted under `source-policy.md` §2.2 and need no fresh I1–I4 pass.

---

## 4. Pre-registered constraints on the DOJ OIG admission

Written **before** retrieval, so they cannot be relaxed afterwards. The report is *A Review of the FBI's Handling of Intelligence Information Related to the September 11 Attacks*, DOJ Office of the Inspector General, November 2004, publicly released June 2006.

**An earlier draft of this program proposed reading it first, on three grounds. Adversarial review verified all three against the live sources and all three are false.** Recorded here rather than deleted:

| Claimed | Actual |
|---|---|
| "Partially breaks the closed evidentiary loop" | The review was commissioned by the FBI Director — head of the investigated body. Its 14,000-page base *includes* Joint Inquiry material. CIA material arrived through CIA OIG, pre-selected and redacted. The report states it **could not independently verify that all relevant documents had been provided**. And OIG supplied its report **to** the 9/11 Commission, making it partly *upstream* — so `circular` is a live verdict against U-03 |
| "Where H5 is decided" | Priority 1's pre-registered positive criterion needs a **contemporaneous CIA-side** record. DOJ OIG has no jurisdiction there |
| "Native text, so no image-verification bottleneck" | The HTML chapters have **no pagination**, so under §7.2 a decisive quotation cannot be carded from them at all; two `[Image Not Available Electronically]` placeholders are precisely the *Hazmi and Mihdhar timeline* graphics; and 51,434 words yield exactly **one** `[redacted]` marker although the report states classified material was deleted — deletions unmarked by construction |

What survives is the diagnosis, not the inference: PR-012 is right that no remaining MFR will move Priority 1 past "touched, inconclusive". The report's value is **Priority 6 / T-12** and **citation harvesting**.

### Binding constraints

- **Artifact of record is the PDF** (9,436,763 bytes), not the HTML; both serving paths as one artifact under D5. The HTML is admitted **only** as a search and location aid, tagged `publisher HTML re-rendering` (§7.2) — with one real advantage: exhaustive MD-011 variant searching across 51,434 words is trivial and reproducible in it.
- **Precondition before any quotation:** a sampled HTML-vs-PDF diff — at least ten passages, including the single `[redacted]` marker, two footnotes, and both missing timeline figures — recorded as a finding either way.
- **Version discipline.** Three texts exist: November 2004 (classified); **June 2005** (omitted Chapter 4 *and other Moussaoui references throughout*, so Chapters 3 and 5 differ between releases); **19 June 2006** (full unclassified). Open a version-ledger row for the 2005→2006 delta before quoting Chapter 3 or 5 on anything touching Moussaoui. Disambiguate from the near-identically titled sibling report at `/archive/special/0506/`.
- **Independence pre-registered `unknown`**, `derivative` on the CIA limb, `circular` flagged against the Commission. **No row may reach `corroborada` on OIG-and-Commission agreement** — that is republication, not corroboration (D1, D2).
- **The objective is not the node.** **No OIG finding can satisfy Priority 1's positive or negative criterion — only a contemporaneous document that OIG quotes can**, on the T-08 / PR-007 pattern.
- **Atomization is the auditor's act.** Do not adopt OIG's "five junctures" as row IDs. Derive propositions from the pre-registered Priority 1 question in `docs/03` §4 and map the junctures onto them as evidence. Adopting the investigated body's own decomposition would make anything it did not name **structurally unrepresentable**.
- **Chapter scope.** Chapter 5 (rows named) and Chapter 4 (via U-18) only. **Chapter 3 (Phoenix) is refused under I1** — "Phoenix" exists in this repository only as a string in a negative finding. Create the row first or do not retrieve it.
- **`oig.justice.gov` is not a standing admitted repository** (`source-policy.md` §2.2). Full I1–I4 pass required, including the I4 symmetry statement.
- **Budget the B2 pass** or scope the read to document-derived sections. C-D6 records that B2 has never been applied to anything.
- **Tag every decisive passage `document-derived` or `interview-derived`.** The report mixes 14,000 pages of records with 225 interviews conducted 2002–2004 on a single page; the MFRs do not.
- **The negative finding.** *"We found no evidence indicating the FBI or any other member of the Intelligence Community had specific intelligence regarding the September 11 plot."* It may take **only** `document_attested`, `independence: none (self-description of its own search)`. It may **not** move H5 and may **not** mark any row `contradita`. Its clause "or any other member of the Intelligence Community" is **scope-exceeding on the report's own face** — the same chapter states OIG lacked independent access to CIA databases. Apply MD-021's five conditions before treating it as probative; conditions 2, 3 and 4 fail on the report's own text.

---

## 5. Errata — errors in Tier 1 files, recorded and not corrected

`docs/01`, `docs/02` and `docs/03` are **inviolate** ([`04`](04-controlling-methodology.md) §11). Errors found in them are recorded here and never fixed in place, because the Phase A record is evidence of how the audit actually proceeded.

| # | Location | Error | Correct reading |
|---|---|---|---|
| E1 | `docs/02:121` | Cites "`03`, seção 2.5" | **`docs/03` has no §2.5.** The four determinations 5a–5d are at **§4, priority 5**, as `docs/03` §1.5 itself says ("ver seção 4, prioridade 5"). Flagged in the English companion as translator's note ⁽ᵇ⁾ |
| E2 | `README.md:134` | Phase 2B marked ⛔ with the reason "Mesmo bloqueio (`intelligence.senate.gov`)" | **The stated reason expired.** That host returned HTTP 200 on 19 September 2026, recorded in `SOURCES.md` and `version-history.md` §3.1. Phase 2B is **not executed**, not blocked. `git log -L 134,134:README.md` shows the line was authored in `f0007b5`, a Phase A commit, so it is Tier 1 despite living in a Tier 2 file |
| E3 | `NEXT-STEPS.md:50` | "Fase 2A — Status: aberta, não executada (bloqueio de acesso)" | Contradicts "Phase 2A is open and in progress" earlier in the same file. Authored in `f0007b5` — Tier 1. Superseded by this document; the contradiction is left visible |

**E2 and E3 were planned as in-place corrections and were reclassified during execution.** Per-line `git log -L` showed both lines predate this session. The tier rule caught two edits that would have altered the Phase A record — which is the rule working as designed.

---

## 6. What this program does not do

- It reads no document in the commit that creates it.
- It moves no hypothesis H0–H7.
- It does not open the C-series of critical and alternative claims, still gated on applying `source-policy.md` §2–§3 to a defined candidate set.
- It does not apply the B2 instrument; the custodial-source corpus is unread.
- It does not begin Phase 3 (NCSTAR) or Phase 4 (FAA/NORAD). The six-track timeline exists for Phase 4 but no Phase 4 reading is performed.
- It asserts no structured pattern. [`anomalies.md`](../registry/anomalies.md) §4 records that no anomaly sits above level 2 and why.
