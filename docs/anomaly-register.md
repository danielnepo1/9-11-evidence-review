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
| **Hypotheses touched** | Which of H0–H7 the anomaly is relevant to. Relevance is not support. | list |
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

## 2. Status vocabulary (closed)

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
| Hypotheses touched | |
| Burden note | |
| Opened | |
| Last reviewed | |
| Resolution | open |
```

---

## 4. Index

No entries yet. Populated from Phase 2A onward.

| ID | Short label | Status | Domain | Discriminating power | Hypotheses touched | Opened |
|---|---|---|---|---|---|---|
| — | *(empty at creation)* | — | — | — | — | — |

---

## 5. Entries

*(none)*

---

## 6. Register health checks

Run at the end of every phase and record the result in that phase's document:

1. **Balance check.** How many entries concern the official account, and how many concern alternative accounts? A register with entries in only one direction is evidence of one-sided reading, not of one-sided reality — investigate the reading, not the conclusion.
2. **Mirror-test completeness.** Count entries with a pending mirror test. That count is reported, not hidden.
3. **Promotion check.** Confirm that no synthesis text cites a `low` discriminating-power entry, or any entry, as support for intent, foreknowledge, complicity or intervention.
4. **Resolution rate.** Count entries moved to `apparent anomaly with adequate explanation` during the phase. A rate of zero over several phases suggests the ordinary-explanation test (M4) is not being applied seriously.
