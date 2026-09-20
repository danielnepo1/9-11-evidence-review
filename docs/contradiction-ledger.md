# Contradiction Ledger

> Working ledger of tested contradictions between accounts. Governed by [`04-methodology-symmetric-skepticism.md`](04-methodology-symmetric-skepticism.md); targeting and priorities in [`05-stress-test-execution-plan.md`](05-stress-test-execution-plan.md).

**Created: 19 September 2026. Empty of substantive entries at creation.** Entries are created only from primary sources read at the extent recorded in their document card.

A contradiction is a **lead**. It is not, by itself, an explanation of why the accounts differ, and never evidence of intent.

---

## 1. Gate — before anything is entered

Two statements contradict only if they concern the **same proposition, the same time interval, the same meaning, the same organizational level and compatible uncertainty**. Test all of the following and record the answers; failing any one of them, the item is not a contradiction:

1. Semantic equivalence — do the two statements assert the same thing, or merely sound opposed?
2. Matching date range.
3. Matching organizational level — "the CIA knew" and "this officer knew" are different propositions.
4. Compatible uncertainty — a hedged claim and a flat claim may both be honest.
5. Is one statement simply **narrower** than the other?
6. Do clocks, time zones or reference points differ?
7. **Could both be true simultaneously?**

Most apparent contradictions in this record are expected to be scope mismatches. Establishing that is a result and is recorded as one.

---

## 2. Relationship classification (closed vocabulary)

| Relationship | Definition |
|---|---|
| `direct contradiction` | Both cannot be true under the same definitions. |
| `material tension` | Reconciliation is possible but requires an additional assumption, which must be named. |
| `scope mismatch` | The statements refer to different periods, people, levels or meanings. |
| `revision` | A source changed or corrected its own account. Record what prompted the change. |
| `unresolved` | Source quality or wording prevents classification. |

For every `direct contradiction`, at least one possible resolution must be stated, together with the evidence that would choose between the resolutions.

---

## 3. Entry template

```
### X-<nnn> — <neutral short name>

**Proposition being tested:**

**Account A:** exact wording · source · date · page · scope · oath status
**Account B:** exact wording · source · date · page · scope · oath status

**Gate results:** semantic equivalence / date range / org level / uncertainty / narrower statement / clock reference / could both be true — answered individually

**Relationship:** direct contradiction | material tension | scope mismatch | revision | unresolved

**Source genealogy:** independent | possibly dependent | shared source | unknown — with the basis for the judgement

**Most plausible ordinary reconciliation:**

**Implications by hypothesis:** H0 … H7, stating for each whether it *predicts* this, merely *accommodates* it, or is *weakened* by it

**Discriminating evidence needed:**

**Escalation level:** 1–5, with the specific item permitting the level
**Priority:** P0–P3

**Conclusion ceiling:** the strongest claim this evidence cannot support

**Linked:** C-<id> · A-<id>
**Opened / Last reviewed:**
```

Quotations are preserved verbatim in the source language, followed by a clearly labelled working translation where needed. Evidentiary text is never silently translated, repaired or modernised.

---

## 4. Index

| ID | Short name | Relationship | Workstream | Escalation | Priority | Status |
|---|---|---|---|---|---|---|
| X-001 | Cable asserting documents passed to FBI vs. records showing they were not | `direct contradiction` | ST-2 / T-2.1 | 2 | P0 | open |

---

## 5. Entries

### X-001 — Cable asserting documents passed to FBI vs. records showing they were not

**Proposition being tested:** In January 2000, Khalid al-Mihdhar's travel documents, including his multiple entry U.S. visa, were copied and passed to the FBI.

**Account A:** A CIA internal operational cable of January 2000 — the fifth CIA cable to discuss Mihdhar's U.S. visa — stated that Mihdhar's travel documents, including a multiple entry U.S. visa, "had been copied and passed **'to the FBI for further investigation.'**"
· Source: quoted by DOJ OIG, *A Review of the FBI's Handling of Intelligence Information Related to the September 11 Attacks*, PDF p. 253 / printed p. 243 (`cards/DOJOIG-2004.md` G5).
· Scope: assertion of completed action, no by-whom, to-whom or how (G6).
· Oath status: n/a — contemporaneous operational record.

**Account B:** The DOJ OIG and the CIA OIG, both with access to the records and the participants, found no corroboration: "Neither we nor the CIA OIG was able to locate any other witness who said they remembered anything about Mihdhar's travel documents being passed to the FBI, **or any other documents that corroborated the statement that the documents were in fact passed to the FBI**" (G14, same page). The notification vehicle addressed to the FBI — the draft CIR — was put on hold in writing approximately three hours earlier (G4, G8), was still undisseminated eight days later (G9), was still in draft in mid-February (G11), and "was never sent"; the information "was not provided to the FBI until shortly before the September 11 attacks" (G13, PDF p. 366 / printed p. 356).

**Gate results:**

| Test | Result |
|---|---|
| Semantic equivalence | **Yes.** Both concern whether the same documents reached the same recipient |
| Matching date range | **Yes.** January 2000 |
| Matching organizational level | **Yes.** CIA → FBI institutional transfer |
| Compatible uncertainty | **No.** Account A is a flat assertion of completed action; Account B is a documented failure to corroborate it |
| Is one statement narrower? | **No** |
| Clocks / reference points | Not applicable — no timestamp dispute |
| **Could both be true?** | **Only under one reading:** that the documents were passed by some unrecorded means, by an unidentified person, leaving no trace either agency could find. The CIA advanced essentially this (G17). The DOJ OIG rejected it: "we found no evidence that this cable was correct and that this information had actually been provided to the FBI" |

**Relationship:** `direct contradiction` — between a contemporaneous record and the state of affairs it asserts, as established by two investigating bodies with access to the underlying records.

**Source genealogy:** `independent`. Account A is a January 2000 operational cable. Account B rests on separate contemporaneous records (the CIR's status in the cable system; the drafter's mid-January e-mail; a contemporaneous e-mail written expressly to document what the FBI was told, which omits the visa — G18; the FBI recipient's contemporaneous note, which also omits it — G19). These are not the same record and do not share an ancestor. **Caveat:** this audit reads all of them through one secondary source, the DOJ OIG, so their independence *as records* is established, while their transmission to this audit is single-channel.

**Most plausible ordinary reconciliation:** The cable's author relayed in good faith something she had been told. She offered exactly this: the wording "suggested to her that someone else told her that they had already been passed, but she did not know who it was" (G15). **This explanation is live and is not excluded by anything read.** It relocates the error rather than eliminating it — the person who supposedly told her was never identified, and no record of the passage exists — but it is fully consistent with the evidence and requires no intent from anyone.

**Implications by hypothesis:**

| Hypothesis | Relationship to this finding |
|---|---|
| H0 | **Accommodates.** Institutional failure with false internal recording is compatible with the official account, which itself documents the failure through its own inspectors general |
| H4 | **Accommodates and is mildly strengthened.** A false "already handled" record is a concrete mechanism by which fragmentation produces non-action |
| H1 | **Neither predicted nor supported.** The record is from January 2000, twenty months before the attacks. It cannot be post-event self-protection |
| H5 | **Not supported.** Requires evidence of specific operational knowledge and deliberate conduct. Nothing read supplies either; the direction of the hold is documented but its reason is not, and every participant is recorded as not recalling it |

**Discriminating evidence needed:**
1. **The cable itself, in full** — read directly rather than through the OIG's quotation.
2. **The identity of whoever told Michelle the documents had been passed**, or a documented finding that no such person existed.
3. **The reason the Deputy Chief directed the hold** — any contemporaneous record of it. The OIG found none and he did not recall it.
4. The exact calendar date of the drafting, the hold and the fifth cable, which the pages read do not pin down.
5. `CR-2004` and `JI-2002` on the same events, read for divergence from the OIG's reconstruction.

**Escalation level: 2** — `unresolved anomaly`. Ordinary reconciliation *has been tested*, by two inspectors general with access to the records and the people, and did not resolve it. **What permits level 2 and no more:** the good-faith-relay explanation (G15) remains live and unexcluded. Level 4 would require affirmative evidence of deliberate withholding, which nothing read supplies.

**Priority:** P0.

**Conclusion ceiling:** *A contemporaneous CIA record asserted a transfer to the FBI that two investigating bodies could not corroborate, while the vehicle for that transfer sat on hold and was never sent.* That is the whole of it. It does **not** establish that the assertion was knowingly false, that anyone intended the information to be withheld, or that anyone foresaw any consequence. Carried verbatim from the pre-registration at [`prereg/T-2.1.md`](prereg/T-2.1.md) §4, written before the document was opened.

**Linked:** `cards/DOJOIG-2004.md` · `A-001`
**Opened / Last reviewed:** 2026-09-20 / 2026-09-20
