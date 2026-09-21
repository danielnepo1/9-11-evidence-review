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
| X-001 | Cable asserting documents passed to FBI vs. records showing they were not | `direct contradiction` | ST-2 / T-2.1 | 2 | P0 | open — genealogy upgraded 2026-09-21 |
| X-002 | Who directed the hold: "a CIA desk officer" (Commission) vs. "per [the Deputy Chief]" (OIG notation) | `material tension` | ST-2 / T-2.1b | 1 | P1 | open |
| X-003 | CIA's stated position on the transfer: "unable to confirm" (2002) → "sent through another cable" (2004) | `revision` | ST-2 / T-2.1b | 1 | P1 | open |

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

**Source genealogy:** `independent`. Account A is a January 2000 operational cable. Account B rests on separate contemporaneous records (the CIR's status in the cable system; the drafter's mid-January e-mail; a contemporaneous e-mail written expressly to document what the FBI was told, which omits the visa — G18; the FBI recipient's contemporaneous note, which also omits it — G19). These are not the same record and do not share an ancestor.

**Genealogy amended 2026-09-21 (T-2.1b), after reading the two other reconstructions:**
- **`JI-2002` is a genuinely independent second channel.** In 2002, before the OIG review existed, a CIA CTC Supervisor testified that the CIA "was unable to 'confirm either passage or receipt of the information'", and **"The Joint Inquiry found no record of the visa information at FBI Headquarters"** — its own search, its own witnesses (`cards/JI-2002.md` J1–J2, PDF p. 178 / pr. 146, image-verified). Account B is now attested by two bodies with separate access.
- **`CR-2004` is NOT independent of the OIG on this episode.** Its note 44 cites "DOJ Inspector General report … July 2, 2004, p. 282" and two OIG interviews (`cards/CR-2004.md` C6). The Commission's account is a summary of the OIG's draft and adds no separate channel, though it does cite the 5 January 2000 cable directly.
- Transmission to this audit is therefore **two-channel** (OIG; JI), not single-channel. The underlying cable itself remains unread by this audit.

**Wording across the three bodies, same record:** JI 2002 — CIA "unable to confirm"; OIG 2004 — "we found no evidence that this cable was correct"; Commission 2004 — "Contemporaneous documents **contradict** the claim that they were shared." In this project's vocabulary: `inconclusive` → `unsupported statement` → `contradicted`. Recorded as a fact about the reconstructions.

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

**Linked:** `cards/DOJOIG-2004.md` · `cards/JI-2002.md` · `cards/CR-2004.md` · `A-001` · `X-002` · `X-003`
**Opened / Last reviewed:** 2026-09-20 / 2026-09-21

---

### X-002 — Who directed the hold: "a CIA desk officer" (Commission) vs. "per [the Deputy Chief]" (OIG notation)

**Proposition being tested:** Who directed that the draft CIR not be sent to the FBI in January 2000.

**Account A:** "A CIA desk officer instructed him not to send the cable with this information."
· Source: `CR-2004`, ch. 6 note 44, PDF p. 520 / printed p. 502, image-verified (`cards/CR-2004.md` C4). Scope: attribution of the instruction; no supervisory level mentioned.

**Account B:** "Around 4:00 p.m. on the same day, Michelle added a note to the CIR in the CIA's computer system: 'pls hold off on CIR for now **per [the CIA Deputy Chief of Bin Laden Unit]**.'" And: "A notation added to the CIR **suggested** that it was held at the request of the CIA's Deputy Chief of the Bin Laden Unit." And: "The evidence indicates that the CIA did not provide permission for the CIR to be sent."
· Source: `DOJOIG-2004`, PDF pp. 250, 366 / printed pp. 240, 356, image-verified (`cards/DOJOIG-2004.md` G4, p. 366). Scope: the notation names the desk officer as author and the Deputy Chief as authority.

**Gate results:** semantic equivalence — partial (both concern who stopped the CIR; A names an actor, B names an actor *and* an authority) · date range — same · org level — **differs**: A places the decision at desk-officer level, B at deputy-chief level via the desk officer · compatible uncertainty — B is hedged ("suggested"), A is flat · **narrower statement — yes: A is a compression of B** · clocks — n/a · **could both be true — yes**, straightforwardly: the desk officer instructed him, citing the Deputy Chief.

**Relationship:** `material tension` — reconcilable with one added assumption (that "instructed him" summarises "added a note saying hold off per the Deputy Chief"), but the Commission's version drops the supervisory attribution entirely, and a reader of note 44 alone would not learn that the hold was recorded as coming from above the desk officer.

**Source genealogy:** `shared source` — the Commission cites the OIG's July 2004 draft for this very passage. This is a divergence between a summary and the source it summarises, not between two independent reconstructions.

**Most plausible ordinary reconciliation:** Editorial compression in a footnote. The Commission had the OIG draft and chose to name the proximate actor. Nothing read suggests the omission was deliberate, and the OIG's own hedge ("suggested") shows the Deputy Chief attribution rests on the notation alone, not on any witness — every participant is recorded as not recalling it.

**Implications by hypothesis:** H0/H4 accommodate either version. H1 (post-event institutional self-protection) is not engaged — this is a *Commission* summary, not a CIA statement. H5 — nothing; the identity of who directed the hold, at whichever level, says nothing about why.

**Discriminating evidence needed:** the OIG's July 2004 draft, p. 282, to see whether the Deputy Chief attribution was present in what the Commission was summarising; and the notation itself.

**Escalation level:** 1 — discrepancy. **Priority:** P1 — it matters because the Deputy Chief attribution is the only thread in the record leading above the desk officer, and one of the three reconstructions cut it.

**Conclusion ceiling:** A footnote's compression of its source is not evidence about January 2000. It is evidence about how the Commission wrote note 44.

**Linked:** `cards/CR-2004.md` · `cards/DOJOIG-2004.md` · `X-001` · `A-001`
**Opened / Last reviewed:** 2026-09-21 / 2026-09-21

---

### X-003 — CIA's stated position on the transfer: "unable to confirm" (2002) → "sent through another cable" (2004)

**Proposition being tested:** What the CIA, as an institution, has said about whether Mihdhar's visa information reached the FBI in January 2000.

**Account A (2002, under oath):** A CTC Supervisor testified that a cable "noted that al-Mihdhar's passport information had been 'passed to the FBI,' but the CIA was unable to 'confirm either passage or receipt of the information' and, thus, could not identify 'the exact details . . . that were passed.'" The CTC Chief testified: "We were in the business of providing information to the FBI, not withholding it."
· Source: `JI-2002`, PDF pp. 178, 181 / printed pp. 146, 149; p. 178 image-verified (`cards/JI-2002.md` J1, J8).

**Account B (2003–04, to the DOJ OIG):** "The CIA has asserted that the information in the CIR was sent to the FBI through another cable, which may be why the CIR was not sent."
· Source: `DOJOIG-2004`, PDF p. 366 / printed p. 356, fn. 274, image-verified (`cards/DOJOIG-2004.md` G17).

**Gate results:** semantic equivalence — yes (both are the CIA's position on whether the information was passed) · date range — same underlying events; statements two years apart · org level — A is an individual supervisor under oath plus the CTC Chief; B is "the CIA" as an institution responding to an IG · compatible uncertainty — **no**: A concedes non-confirmation; B asserts transmission · narrower — no · clocks — n/a · **could both be true — only if** the CIA learned something between 2002 and 2004 that let it confirm what it could not confirm in 2002. The OIG found no such thing: "we found no evidence that this cable was correct."

**Relationship:** `revision` — an institutional position moved, over two years, from non-confirmation to affirmative assertion, in the direction of the institution's interest, while both investigating bodies that examined the record in 2004 moved the opposite way (OIG: no evidence it was correct; Commission: contemporaneous documents contradict it).

**Source genealogy:** `independent` — 2002 sworn testimony recorded by the Joint Inquiry, versus 2003–04 institutional statements recorded by the DOJ OIG. No shared ancestor.

**Most plausible ordinary reconciliation:** **Different speakers, different postures.** A working supervisor under oath in 2002 answered a factual question; "the CIA" in 2004 was responding to an Inspector General's adverse draft, and institutional responses to IG findings routinely advance the most favourable available reading. This is live and untested — the CIA's written response to the OIG draft has not been read.

**Implications by hypothesis:**

| Hypothesis | Relationship |
|---|---|
| H0 | Accommodates — institutions defend themselves |
| H4 | Accommodates |
| **H1** | **Predicts.** This is the first item in the register that H1 (post-event self-protection / narrative management) actually predicts rather than merely accommodates: an institution's account of its own conduct hardening in its own favour after the fact, against the evidence found by two investigating bodies |
| H5 | Not engaged — the shift is about 2002–04 statements, not January 2000 knowledge |

**Note on H1, held to the ceiling:** that H1 predicts this does not make H1 more likely than the ordinary explanation, which predicts the same observation. What distinguishes them is *whether the 2004 assertion was made with knowledge that it was unsupported*, and nothing read bears on that.

**Discriminating evidence needed:** (1) the CIA's written response to the DOJ OIG draft, which would show the basis the CIA gave for the 2004 assertion; (2) the CIA OIG's own accountability report on 9/11, which examined the same episode from inside the agency; (3) the full Joint Inquiry testimony of the CTC Supervisor and CTC Chief, for context around the 2002 concession.

**Escalation level:** 1 — discrepancy. Ordinary reconciliation is live and untested. **Priority:** P1.

**Conclusion ceiling:** *The CIA's stated position on this transfer changed between 2002 and 2004, from "unable to confirm" to "was sent through another cable," and the later position was rejected by the DOJ OIG for want of evidence.* That is all. It does not establish that the 2004 assertion was made in bad faith, and it says nothing about January 2000.

**Linked:** `cards/JI-2002.md` · `cards/DOJOIG-2004.md` · `cards/CR-2004.md` (C9 — a separate, same-shaped episode in 2001) · `X-001`
**Opened / Last reviewed:** 2026-09-21 / 2026-09-21
