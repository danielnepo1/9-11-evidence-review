# Anomaly Register

> Working register of anomalies identified in the 9/11 record — in the official account and in alternative accounts alike. Methodology, status vocabulary and the mirror test are defined in [`04-methodology-symmetric-skepticism.md`](04-methodology-symmetric-skepticism.md) §5, which governs this file.

**Created: 19 September 2026.** The register is **empty of substantive entries at creation.** It is populated only by phases that read primary sources. Entries may not be created from prior knowledge, from search snippets, or from secondary reporting.

> **An anomaly is a research lead. By itself it is not evidence of intent, foreknowledge, complicity, or intervention.**

---

## 1. Field definitions

Every entry carries all fields below. A field that cannot be filled reads `not determined` — never blank.

| Field | Definition | Admissible values |
|---|---|---|
| **ID** | Stable identifier, `A-001`, `A-002`, … Never reused, never renumbered. | `A-<nnn>` |
| **Short label** | Four to ten words naming the anomaly, neutral in wording. A label that presupposes an explanation is non-compliant. | free text |
| **Status** | Exactly one value from the closed vocabulary in §2. | see §2 |
| **Domain** | Which track the anomaly belongs to. | `intelligence` · `FAA/NORAD` · `commission process` · `foreign support / financing` · `evidence custody` · `structural / forensic` · `other` |
| **Description** | What was observed, stated without inference. Names the specific passages, times or measurements in tension. | free text |
| **Event date** | When the underlying event occurred. | date or `not determined` |
| **Document date(s)** | When each record involved was produced. | dates |
| **Declassification / publication date(s)** | When each record became public. | dates |
| **Sources** | Every source involved, each with read status per `04` §2.4 (`read in full`, `read in part`, `located, not read`, `cited, not located`). | list |
| **Linked claims** | The atomic propositions in [`claim-decomposition-register.md`](claim-decomposition-register.md) this anomaly bears on. | `C-<id>`, … |
| **M1 Official prediction** | What the official account predicts should be observed. | free text |
| **M2 Alternative predictions** | What each relevant alternative hypothesis predicts, hypothesis by hypothesis. | keyed by `H1`–`H7` |
| **M3 Discriminating observation** | The observation that would separate M1 from M2. Named specifically. | free text |
| **M4 Ordinary-explanation test** | Whether error, memory, classification, bureaucracy, incomplete records or ordinary forensic uncertainty accounts for it — and on what basis that was assessed. | free text |
| **M5 Conclusion not justified** | Written as an explicit prohibition. Mandatory. | free text |
| **Discriminating power** | Derived from M3. | `high` · `medium` · `low` |
| **Escalation level** | Position on the ladder in §2.1, **plus the specific item that permitted the level**. Levels may not be skipped. | `1`–`5` |
| **Priority** | Research value: centrality × source quality × discriminating power. Not probability of conspiracy. | `P0`–`P3` |
| **Source genealogy** | Whether the accounts involved are genealogically independent, or share an ancestor (one MFR, one briefing, one press account, one institutional reconstruction). | `independent` · `possibly dependent` · `shared source` · `unknown` |
| **Hypotheses touched** | Which of H0–H7 the anomaly is relevant to. For each, whether it *predicts* the observation, merely *accommodates* it, or is *weakened* by it. Relevance is not support. | list |
| **Burden note** | What each hypothesis in "hypotheses touched" would additionally need to be established. Enforces `04` §3 S2–S6. | free text |
| **Opened** | Date the entry was created. | date |
| **Last reviewed** | Date the entry was last re-examined against new material. | date |
| **Resolution** | How it was closed, if closed; `open` otherwise. | free text or `open` |

### 1.1 Rules

1. **Symmetry.** Anomalies in alternative accounts — unsupported premises, misquoted sources, non-replicable analyses, arithmetic that does not survive checking — are registered with the same fields and the same rigour as anomalies in the official account. The register is not a list of grievances against institutions.
2. **No promotion.** Moving an anomaly from `unresolved anomaly` to any conclusion about intent requires a separate, evidenced entry in the claim register. The anomaly register never itself concludes intent.
3. **Resolved entries stay.** `apparent anomaly with adequate explanation` is a result and is retained permanently. Deleting resolved anomalies would bias the register toward the unresolved.
4. **No entry without a mirror test.** M1–M5 must be answered before a final status is assigned. An entry awaiting the mirror test carries status `unresolved anomaly` and an explicit note that the mirror test is pending.
5. **`low` discriminating power is non-probative.** Such entries may not be cited in any synthesis as support for any hypothesis.

---

## 2. Status, escalation and priority

### 2.1 Escalation ladder — levels may not be skipped

| Level | Name | What permits entry |
|---|---|---|
| 1 | Discrepancy | Records or claims do not align. |
| 2 | Unresolved anomaly | Ordinary reconciliation has been **tested** and remains inadequate. |
| 3 | Structured pattern | Multiple **substantially independent** anomalies point in the same direction. Independence must be demonstrated, not assumed. |
| 4 | Evidence of concealment | Affirmative acts or records support deliberate withholding or deception. |
| 5 | Evidence of foreknowledge or participation | Evidence connects a named actor to specific operational knowledge or material conduct. |

Every entry records the level **and the specific item that permitted it**. A large collection of dependent, low-quality discrepancies does not become a level 3. Most entries are expected to remain at level 1 or 2 permanently; that is the normal outcome, not a failure of the audit.

### 2.2 Research priority

| Priority | Criterion |
|---|---|
| `P0` | Documented fracture on a central claim, capable of separating major hypotheses. |
| `P1` | Material unresolved tension whose discriminating evidence is obtainable. |
| `P2` | Real anomaly with several viable ordinary explanations. |
| `P3` | Low-centrality curiosity, or weakly sourced allegation. |

Priority measures research value, not probability of conspiracy. A P0 entry is one worth resolving, in whichever direction it resolves.

### 2.3 Status vocabulary (closed)

| Status | Meaning |
|---|---|
| `documentary contradiction` | Two documents assert incompatible things about the same fact. |
| `timeline discrepancy` | Two records place the same event at incompatible times, or an interval is inconsistent with a stated sequence. |
| `conflicting testimony` | Two or more accounts by people conflict on a material point. |
| `unexplained procedural deviation` | A documented departure from an established rule, routine or standard practice, with no explanation on the record. |
| `missing or destroyed evidence` | Material known to have existed that is now absent, withheld, or destroyed. |
| `chain-of-custody limitation` | Material exists but its handling record is incomplete enough to limit what can be concluded from it. |
| `model assumption or non-replicability issue` | A technical result depends on unverified assumptions or unreleased inputs, or cannot be reproduced. |
| `physical or forensic anomaly` | An observation about physical evidence not accounted for by the stated explanation. |
| `apparent anomaly with adequate explanation` | Examined and resolved by an ordinary explanation. |
| `unresolved anomaly` | Examined, not resolved, not yet assignable to a more specific status. |

---

## 3. Entry template

Copy verbatim for each new entry.

```
### A-<nnn> — <short label>

| Field | Value |
|---|---|
| Status | |
| Domain | |
| Description | |
| Event date | |
| Document date(s) | |
| Declassification / publication date(s) | |
| Sources (with read status) | |
| Linked claims | C-<id>, … |
| M1 — Official account predicts | |
| M2 — Alternative hypotheses predict | H1: … · H2: … · … |
| M3 — Discriminating observation | |
| M4 — Ordinary-explanation test | |
| M5 — Conclusion NOT justified | |
| Discriminating power | high / medium / low |
| Escalation level | 1–5 — and the item permitting it |
| Priority | P0 / P1 / P2 / P3 |
| Source genealogy | independent / possibly dependent / shared source / unknown |
| Hypotheses touched | H_: predicts / accommodates / weakened |
| Burden note | |
| Opened | |
| Last reviewed | |
| Resolution | open |
```

---

## 4. Index

No entries yet. Populated from Phase 2A onward.

| ID | Short label | Status | Domain | Escalation | Priority | Discriminating power | Opened |
|---|---|---|---|---|---|---|---|
| A-001 | Uncorroborated cable assertion of FBI transfer, January 2000 | `documentary contradiction` | intelligence | 2 | P0 | high | 2026-09-20 |
| A-002 | CR-2004 note 20 dates a Hambali interrogation report seven months before his documented capture | `apparent anomaly with adequate explanation` | intelligence | 1 | P2 | medium | 2026-09-21 |

---

## 5. Entries

### A-001 — Uncorroborated cable assertion of FBI transfer, January 2000

| Field | Value |
|---|---|
| Status | `documentary contradiction` |
| Domain | `intelligence` |
| Description | A CIA internal operational cable of January 2000 asserted that Khalid al-Mihdhar's travel documents, including a multiple entry U.S. visa, "had been copied and passed 'to the FBI for further investigation.'" The DOJ OIG and CIA OIG, both with access to the records and participants, located no witness and no document corroborating that the transfer occurred. The draft CIR addressed to the FBI — the vehicle for that transfer — had been put on hold in writing approximately three hours earlier, was never sent, and the information did not reach the FBI until shortly before the attacks |
| Event date | January 2000 (exact calendar date not established from the pages read) |
| Document date(s) | Cable: January 2000. DOJ OIG report: November 2004 |
| Declassification / publication date(s) | DOJ OIG report: June 2005 (redacted public version) |
| Sources (with read status) | `DOJOIG-2004` — **read in part** (9 of 449 pages, PDF pp. 249–253, 255, 366), decisive passages image-verified. The underlying cables and e-mails: **cited, not located** |
| Linked claims | *(claim register rows not yet opened for this target)* |
| **M1 — Official account predicts** | A documented institutional failure, recorded and investigated by the government's own inspectors general, with a false or unverified internal record as one mechanism of that failure. **This is what the official account itself says**, via the DOJ OIG. The observation is fully predicted |
| **M2 — Alternative hypotheses predict** | **H4:** predicts exactly this — fragmentation producing an "already handled" record and consequent non-action. **H1:** predicts nothing here; the record is from January 2000, twenty months pre-attack, so it cannot be post-event self-protection. **H5:** would predict a deliberate suppression leaving either no trace or a trace of decision; what exists is an unexplained hold plus an uncorroborated assertion, which H5 accommodates but does not uniquely predict — and H4 and H0 predict the same artifact |
| **M3 — Discriminating observation** | The identity of whoever told the cable's author the documents had been passed, or a documented finding that no such person existed; and any contemporaneous record of **why** the Deputy Chief directed the hold. Either would separate "error propagating through an institution" from anything stronger. Both are specific and were sought by two inspectors general |
| **M4 — Ordinary-explanation test** | Tested against all five explanations pre-registered at [`prereg/T-2.1.md`](prereg/T-2.1.md) §4. **(1) Workflow artifact:** does not fit — this was a human-written sentence in a substantive operational cable, not a system flag. **(2) Good-faith relay of something the author was told:** **LIVE AND NOT EXCLUDED.** The author offered exactly this and could not name the source. **(3) Transfer via another channel:** asserted by the CIA, tested and rejected by the DOJ OIG for want of evidence; further weakened by a contemporaneous e-mail written expressly to document what the FBI was told, which omits the passport and visa, and by the FBI recipient's contemporaneous note, which also omits it. **(4) Two documents conflated by later reconstruction:** weak — the OIG worked from the cable system itself. **(5) Silent release failure:** applies to the CIR's non-transmission, which is a separate fact, not to the false assertion |
| **M5 — Conclusion NOT justified** | **This does not establish that the assertion was knowingly false. It does not establish that anyone intended the information to be withheld from the FBI. It does not establish that anyone foresaw any consequence. It does not move H1 or H5.** An uncorroborated assertion in an internal record is fully consistent with an error relayed in good faith, which the author herself offered as the explanation and which nothing read excludes |
| Discriminating power | **high** — M3 names specific, previously-sought items, and the records are known to have existed |
| Escalation level | **2** (`unresolved anomaly`). **Permitted by:** ordinary reconciliation was tested by two inspectors general with access to the records and the people, and did not resolve it (G14, G17). **Blocked from 3+ by:** explanation (2) remains live; and a single anomaly cannot be a structured pattern |
| Priority | **P0** |
| Source genealogy | `independent` as to the records (the cable, the CIR's system status, the drafter's e-mail, the documenting e-mail, the recipient's note are five separate records). **Two-channel as to transmission, amended 2026-09-21:** the DOJ OIG (2004) and the Joint Inquiry (2002, independently: "The Joint Inquiry found no record of the visa information at FBI Headquarters", `cards/JI-2002.md` J2). The 9/11 Commission's note 44 is **not** a third channel — it cites the OIG's July 2004 draft (`cards/CR-2004.md` C6). See X-001 |
| Hypotheses touched | H0: *accommodates* (predicts it, via its own IG) · H4: *predicts* · H1: *neither* · H5: *accommodates, does not predict* |
| Burden note | For H5 to gain anything here it would need evidence of **specific operational knowledge** plus **deliberate conduct** (`04` §2.3). The hold is documented; its reason is not. An unexplained instruction is not evidence of its own motive, and every participant is recorded as not recalling it |
| Opened | 2026-09-20 |
| Last reviewed | **2026-09-21** — three-body comparison done (T-2.1b). Escalation unchanged at 2: the JI adds an independent channel for Account B, which strengthens the *documentation* of the anomaly without touching the live ordinary explanation (good-faith relay). Two derived entries opened in the contradiction ledger: X-002 (attribution of the hold) and X-003 (the CIA's 2002→2004 position shift), both level 1 |
| Resolution | open |

---

### A-002 — CR-2004 note 20 dates a Hambali interrogation report seven months before his documented capture

| Field | Value |
|---|---|
| Status | `apparent anomaly with adequate explanation` |
| Domain | `intelligence` |
| Description | `CR-2004` chapter 5, endnote 20, supports the sentence "By 1998, Hambali would assume responsibility for the Malaysia/Singapore region within Sungkar's newly formed terrorist organization, the JI" (PDF p. 169 / printed p. 151) with: "Intelligence reports, interrogations of Hambali, Jan. 14, 2003; Mar. 5, 2004." `SSCI-2014` states, and corroborates independently across at least five passages, that "In August 2003, Hambali was captured and transferred to CIA custody" — seven months **after** the first date cited in note 20. No interrogation report attributed to Hambali by name could have existed on January 14, 2003 if he was not yet in any custody producing CIA interrogation reports until August 2003 |
| Event date | Not applicable — the anomaly concerns a citation date, not an underlying event |
| Document date(s) | `CR-2004`: July 2004. `SSCI-2014`: December 2014 |
| Declassification / publication date(s) | `CR-2004`: born public (GPO). `SSCI-2014`: 2014-12-09 (redacted public release) |
| Sources (with read status) | `CR-2004` — note 20 and its supported sentence, **read**, born-digital (no OCR, D-003 exemption). `SSCI-2014` — p. 137/printed p. 108, **read, image-verified** (decisive quote confirmed against rendered page image, ABBYY OCR, D-003 applies); four further page hits (pp. 279, 285, 422, 511, 631) **located, not image-verified** — not relied on for this entry, cited only as unverified corroboration of the same fact |
| Linked claims | *(claim register rows not yet opened for this target)* |
| M1 — Official account predicts | The Commission's own endnote apparatus should be internally consistent: a citation date for a named detainee's interrogation report should fall within a period in which that detainee was in a custody capable of producing such a report. `CR-2004` and `SSCI-2014` are both parts of "the official account" in this project's usage; this entry tests one against the other, not the official account against an alternative |
| M2 — Alternative hypotheses predict | **H4** (institutional failure through negligence/fragmentation): predicts exactly this — a single-digit transcription error in a 1,657-note apparatus assembled from raw cable citations under a fixed publication deadline, with no operational stake in the error. **H1** (self-protection/narrative management): has no plausible mechanism here — the sentence supported by note 20 is inert, pre-2001 organizational history, and dating the cited report a year earlier neither helps nor harms any account of the Commission's own or the CIA's own conduct. **H5** (specific operational knowledge, deliberately concealed): would require the erroneous date to serve some purpose — e.g., manufacturing an appearance of earlier knowledge of Hambali's role than the record supports — but the sentence it supports needed no such reinforcement (it is uncontested organizational background, not a claim about warning or foreknowledge), so H5 finds nothing to attach to |
| M3 — Discriminating observation | Whether the underlying raw cable (redacted CIA reporting number, not reproduced in `CR-2004`'s endnotes) is dated January 2003 or January 2004. Not available from any source read in this project |
| M4 — Ordinary-explanation test | **Single-digit year transcription error (Jan. 14, 2003 → should read Jan. 14, 2004), tested and found strongly supported.** (1) The same endnote's second citation is "Mar. 5, 2004" — a report on the identical general topic (Hambali's history and role) dated barely seven weeks after the miswritten date, if corrected to 2004. (2) Every other Hambali-attributed citation in the same 84-note set clusters at Sept. 2003 or later (notes 18, 22, 26, 58: Aug.–Sept. 2003; note 22's second citation and note 23: Mar. 2004) — a Jan. 2003 date is the sole outlier in the entire set, while a Jan. 2004 date sits exactly inside that cluster's range. (3) The claim the note supports (pre-2001 organizational history) does not depend on which year is correct — it is not itself evidence for or against any account, only the citation apparatus is at issue. No other ordinary-explanation category from `05` §4 fits as well: this is not a workflow artifact (it is a substantive citation, not a system flag), not a good-faith relay of a stated source (there is no attributed speaker to relay from), and not a scope mismatch (there is no plausible reading under which Jan. 14, 2003 is correct) |
| M5 — Conclusion NOT justified | **This does not establish that Hambali was interrogated, in any custody, on January 14, 2003. It does not establish anything about the reliability of the underlying report once correctly dated. It does not bear on H1 or H5, and it is not evidence that `CR-2004`'s endnote apparatus is unreliable generally — one transcription error in 1,657 notes, found deliberately by cross-referencing against an independent document, is not a base-rate claim about the other 1,656** |
| Discriminating power | **medium** — M3 names a specific, in-principle-available discriminator (the raw cable), but it was not sought in this project and its retrieval is unlikely to be practicable |
| Escalation level | **1** (`discrepancy`). **Not elevated to 2**: the ordinary reconciliation (transcription error) is well-supported by the note's own internal structure and by the surrounding citation cluster, not merely asserted; nothing tested makes it inadequate |
| Priority | **P2** — real, verified anomaly with a strongly favoured ordinary explanation and no bearing on any substantive claim |
| Source genealogy | `independent` — `CR-2004` (2004, Commission staff, GPO) and `SSCI-2014` (2014, Senate committee staff, from CIA operational cables) are separately authored a decade apart from different record sets; the capture-date fact in `SSCI-2014` is itself corroborated across at least five internally distinct passages |
| Hypotheses touched | H0: *neither predicts nor is weakened* — this is a citation-mechanics fact internal to the record-keeping, not a claim about the attacks · H4: *predicts* (exactly the kind of error institutional volume/deadline pressure produces) · H1, H5: *neither* — no mechanism connects a citation-year typo on inert organizational history to either |
| Burden note | Not applicable — no hypothesis gains support from this entry in its current, most-likely resolution |
| Opened | 2026-09-21 |
| Last reviewed | 2026-09-21 |
| Resolution | Not closed formally (the raw cable that would confirm the year was not sought), but assessed as `apparent anomaly with adequate explanation` per M4; recorded open only in the sense that the discriminating cable has not been read |

---

## 6. Register health checks

Run at the end of every phase and record the result in that phase's document:

1. **Balance check — logged, not a correction trigger as of 2026-09-20 (`docs/08` D-006).** How many entries concern the official account, and how many concern alternative accounts? Under the prior symmetric objective, a one-sided register triggered an investigation of the reading. Under the current directed-search objective, a one-sided register is the expected shape of the work; the count is still logged for transparency but no longer treated as a defect by itself.
2. **Mirror-test completeness.** Count entries with a pending mirror test. That count is reported, not hidden.
3. **Promotion check.** Confirm that no synthesis text cites a `low` discriminating-power entry, or any entry, as support for intent, foreknowledge, complicity or intervention.
4. **Resolution rate.** Count entries moved to `apparent anomaly with adequate explanation` during the phase. A rate of zero over several phases suggests the ordinary-explanation test (M4) is not being applied seriously.
5. **Escalation discipline.** For every entry above level 2, re-state the specific item that permitted each step. For every level 3, re-verify that the underlying anomalies are substantially independent (§1 field *source genealogy*) rather than sharing a source, a briefing or an institutional reconstruction.
6. **Targeting audit.** Compare the entries created against the pre-registered targets in [`05-stress-test-execution-plan.md`](05-stress-test-execution-plan.md). Entries that correspond to no pre-registered target are legitimate but are flagged, because post-hoc target selection is the failure mode this plan exists to prevent.
