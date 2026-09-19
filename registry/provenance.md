# Provenance and Source-Independence Graph

> Living instrument. Governed by [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) §3.
> Opened 19 September 2026.

For every consequential proposition: **claim → document publishing it → source that document cites → earliest recoverable source.**

Repeated publications that share a provenance root are **not** independent corroboration. Where independence cannot be established it is recorded as `unknown`; it is never assumed.

---

## 1. Independence verdict vocabulary

| Verdict | Meaning |
|---|---|
| `independent` | The two sources' provenance roots are demonstrably different, and neither derives from the other |
| `shared root` | Both trace to the same interview, report, cable or person |
| `derivative` | One is a restatement or summary of the other |
| `unknown` | Independence has not been established. **Default.** Never upgraded without evidence |
| `circular` | A cites B, B cites A, or both cite a third source that cites one of them |

## 2. Chain-stop reasons

`primary reached` · `cited document not located` · `source fully redacted` · `source identity redacted` · `liaison reporting, origin unevaluable` · `institutional assertion, no source given` · `inaccessible repository` · `not yet attempted`

---

## 3. Provenance chains

### PR-001 — The sub-30% estimate for the May 1998 capture operation
`A3.1`, `T-02`

| Step | Item | Date | Note |
|---|---|---|---|
| 1 | Claim: an estimate at or below ~30% existed | — | — |
| 2a | DOC-3, MFR Scheuer #1 | 11 Dec 2003 | Scheuer, recollection. Oath recorded in the document, **not image-verified**. States 30% |
| 2b | DOC-7, MFR Tenet #2, printed p.3 | 22 Jan 2004 | Tenet, recollection. Oath **image-verified**. States "less than 30%" |
| 3 | Source cited by 2b | — | "(the figure agreed upon **[REDACTED 25X1]**" — the attribution is redacted |
| 4 | Earliest recoverable source | — | **Not reached** |

**Independence:** `independent` as between DOC-3 and DOC-7 at the level of *witness* — two different people, interviewed separately, neither present at the other's session. **But** both are recollections of the same 1998 internal CIA discussion, so they may share an underlying briefing without either being derivative of the other. Independence of the *underlying estimate* is `unknown`.
**Chain stop:** `source identity redacted`.
**Consequence:** A3.1 can rise no higher than `parcialmente corroborada` until the redaction is lifted or the originating estimate is located.

### PR-002 — The reason for the May 1998 cancellation
`A5.2`, `T-01`, `T-03`

| Step | Item | Date | Note |
|---|---|---|---|
| 1 | Claim: why the operation was cancelled | — | — |
| 2a | DOC-3 (Scheuer): a Saudi offer was among the reasons | 11 Dec 2003 | Stated as the witness's **belief**, no document |
| 2b | DOC-7 (Tenet): unanimous operational recommendation of DDO/C/CTC/C-NE; Saudi trip "entirely unrelated" | 22 Jan 2004 | Decision-maker's own account |
| 3 | Contemporaneous record cited by either | 1998 | **None.** DOC-7 p.4: Tenet "did not recall whether there was a memorandum memorializing his decision or the three CIA officers' recommendation" |
| 4 | Earliest recoverable source | — | **Not reached** |

**Independence:** `independent` as between witnesses.
**Chain stop:** `cited document not located` — and, more precisely, the decision-maker states he does not know whether the document exists.
**Consequence:** the strongest available evidence on a documented operational decision by the DCI is two mutually inconsistent recollections given 5½ years later by two men with opposing institutional interests. **Neither side of this is a contemporaneous record.** T-03 is therefore one of the highest-value open items in the registry: establishing that the memorandum exists, or that a records search finds none, changes what every other row here can be worth.

### PR-003 — Saudi access difficulties
`A4.1`, `A4.5`

| Step | Item | Date | Note |
|---|---|---|---|
| 2a | DOC-3 (Scheuer) citing his own memo of 3 May 1996 and a Spot Report of 24 Jun 1997 | 11 Dec 2003 | Documents **not located** |
| 2b | DOC-7 (Tenet), printed p.5 | 22 Jan 2004 | Recollection, no document cited |
| 3 | Underlying contemporaneous records | 1996–1997 | Not located |

**Independence:** `independent` (two witnesses, no shared cited document).
**Chain stop:** `cited document not located`.

### PR-004 — Saudi sanctuary for Madani al-Tayyib — **possible circularity**
`A4.3`

| Step | Item | Date | Note |
|---|---|---|---|
| 2a | DOC-3 (Scheuer), oath not image-verified | 11 Dec 2003 | Asserts the sanctuary |
| 2b | DOC-7 (Tenet), printed p.5 | 22 Jan 2004 | The assertion appears as an **unattributed parenthetical written by the Commission staff drafter**, inside a sentence reporting that Tenet had *no recollection* of the issue |
| 3 | Source of the parenthetical | — | **Not given** |

**Independence:** `unknown`, with `circular` as a live possibility. The Commission staff who drafted DOC-7 had taken Scheuer's testimony six weeks earlier. If the parenthetical restates Scheuer, then DOC-7 does not corroborate DOC-3 — it repeats it, in a document that otherwise records the witness *not* confirming it.
**Chain stop:** `institutional assertion, no source given`.
**Rule applied:** A4.3 does **not** move. This is the canonical example of the closed evidentiary loop described in [`../docs/04` §0](../docs/04-controlling-methodology.md).

### PR-005 — The 6 August 2001 PDB
`A10.1`, `A10.2`, `A16.1`

| Step | Item | Date | Note |
|---|---|---|---|
| 2a | DOC-2 (Rice): no current information; UAE contact looked like a hoax | 7 Feb 2004 | Recollection. **Commission interview record — no oath recorded** |
| 2b | DOC-1 (PDB Review Team): 70 FBI field investigations; contact under investigation; bolded non-corroboration caveat | 9 Feb 2004 | 2004 **characterization** of the PDB |
| 3 | The PDB itself | 6 Aug 2001 | Located (cia.gov) — **scanned without a text layer; not read** |

**Independence:** `unknown`. DOC-1 and DOC-2 are two Commission products two days apart, and both describe the same underlying document; neither is the document.
**Chain stop:** the primary is located but unread — a technical barrier (OCR), not an access barrier.
**Consequence:** the only rows in the registry where the primary source is in hand and unread. Highest cost-to-benefit ratio of any open item.

### PR-006 — The three post-August-1998 TLAM opportunities — **narrative laundering risk**
`T-06`, `T-07`

| Step | Item | Date | Note |
|---|---|---|---|
| 2 | DOC-7, printed p.8 | 22 Jan 2004 | Tenet "read from a CIA staff paper prepared to brief him for this interview (which will be provided to the Commission)" |
| 3 | The CIA staff paper | Jan 2004 | **Not located.** Listed by the document itself under "TO OBTAIN FROM CIA", item 2 |
| 4 | The underlying strike packages and cables | 1998–1999 | Not located |

**Independence:** `derivative`. What reads as the recollection of a witness under oath is in substantial part a **2004 CIA institutional reconstruction, read aloud by the witness.** The MFR itself says so, on the same page; the reader of a summary that omits this sentence would not know.
**Chain stop:** `cited document not located`.
**Rule applied:** T-06 is recorded as `declaração não corroborada` with the derivation flagged. Testimony under oath read from an agency briefing paper is the agency's account with the witness's oath attached to it — the oath attests to his reading, not to the paper's accuracy.

### PR-007 — The February 1999 MON
`T-08`

| Step | Item | Date | Note |
|---|---|---|---|
| 2 | DOC-7, printed p.11 | 22 Jan 2004 | Tenet read the original and the President's replacement language **aloud**; the MFR quotes both |
| 3 | The MON | Feb 1999 | **Not located** |
| 4 | CIA transmittal letter and internal papers on the draft | 1999 | Not located; listed on the document's own follow-up list, item 9 |

**Independence:** the MFR is `derivative` of the MON, but the derivation is a quotation of a contemporaneous instrument — a far stronger link than recollection. **This is the strongest contemporaneous-text link produced by this reading session.**
**Chain stop:** `cited document not located`.
**Note:** the same passage records Commissioner Ben-Veniste stating on the record that he reads the accompanying NSC note differently. A disagreement about a primary instrument, recorded inside the official document — filed at [`discrepancies.md`](discrepancies.md) DISC-005.

### PR-008 — The UAE hunting-camp warning
`T-09`

| Step | Item | Date | Note |
|---|---|---|---|
| 2 | DOC-7, printed p.9 | 22 Jan 2004 | Rousseau (CIA, **not the witness under oath**) reports diplomatic cable traffic and a State reporting cable written by the Ambassador |
| 3 | The cables | 1999 | **Not located** |

**Independence:** `unknown`. Note the assertion type: this is a **third party in the room**, not the witness under oath, characterizing documents not before the Commission at that moment.
**Chain stop:** `cited document not located`.

### PR-009 — The June 1999 Berger → Clinton memo
`T-11`

| Step | Item | Date | Note |
|---|---|---|---|
| 2 | DOC-7, printed p.17 | 22 Jan 2004 | **Zelikow** (Commission staff) summarizes the memo in five numbered points and attributes probable drafting to Clarke; Tenet agrees it fairly states the period |
| 3 | The memo | Jun 1999 | **Not located** |

**Independence:** `derivative`, and doubly so — a Commission staff paraphrase, agreed to by a witness, of a document neither of them is quoting. Tenet's agreement attaches to Zelikow's summary, not to the memo.
**Chain stop:** `cited document not located`.
**Priority:** high. A contemporaneous 1999 assessment stating that more attacks were a certainty and could occur in the US is squarely a W2 (independent/contemporaneous) target under [`../docs/05` §4](../docs/05-phase-c-competing-narratives.md).

### PR-010 — The PDB corpus structure
`A15.1`–`A15.4`

| Step | Item | Date | Note |
|---|---|---|---|
| 2 | DOC-1 | 9 Feb 2004 | The memorandum describes its own review |
| 3 | Source | — | Itself |

**Independence:** `none (self-description)`. Per MD-002 this establishes *officially asserted*, not *independently corroborated*.
**Chain stop:** `primary reached` — the primary *is* the assertion.

### PR-011 — The witness's evidence read from CIA-prepared 2004 material — **a pattern, not an incident**
`T-06`, `T-07`, `U-08`, `U-10`

| Instance | Document / page | What was read from |
|---|---|---|
| 1 | DOC-7 p.8 | "a CIA staff paper prepared to brief him for this interview" — the three TLAM opportunities |
| 2 | DOC-7 p.11 | The February 1999 MON text, read aloud |
| 3 | DOC-8 p.5 | "his recollection of the CIA's investigation into the attack was **entirely dependent on the documents in his briefing book**" — the *Cole* investigation |
| 4 | DOC-8 p.8 | "Reading the cover note to the MON and Finding written by EXDIR Krongard (**from his briefing binder**)" |

**Independence:** `derivative` for every passage so sourced. **Chain stop:** `cited document not located` — the binder is item 2 on DOC-7's own "TO OBTAIN FROM CIA" list and has not been produced to this project.

**What this establishes.** For these passages the provenance root is a **2004 CIA document**, not the witness's memory. Two testimonies six days apart, by the same witness, on four different subjects, are in substantial part a reading of material his own agency prepared for the occasion. Treating them as four independent recollections would be a counting error of exactly the kind [`../docs/04` §3](../docs/04-controlling-methodology.md) exists to prevent.

**What this does not establish.** Nothing improper. A witness preparing from his agency's records before sworn testimony about events five years earlier is ordinary and arguably responsible. The oath attaches to his reading; it does not attach to the accuracy of the binder.

**Consequence:** the briefing binder is promoted in §4 below. It would convert four `declaração não corroborada` rows into rows testable against a dated document.

### PR-012 — The Kuala Lumpur episode
`U-01`, `U-02`, `U-04`, `U-06`

| Step | Item | Date | Note |
|---|---|---|---|
| 1 | Claim: what CIA knew and did about the Kuala Lumpur meeting and al-Midhar | — | — |
| 2 | DOC-8 printed pp. 1–2 | 28 Jan 2004 | **The witness is expressly disqualified as first-hand by the Commission's own Executive Director** (U-01, image-verified) |
| 3 | Sources cited within | — | The Joint Inquiry report (Tenet disputes it); the Commission's January 2004 staff statement; two Freeh briefings; an NSA watchlist request; a CIA file review then under way |
| 4 | Earliest recoverable source | 2000–2001 | **Not reached.** No 2000–2001 record appears anywhere in DOC-8 |

**Independence:** `unknown`, tending to `derivative`. Tenet's account is a 2004 reading of a 2002 report he disputes; Zelikow's bracketed note is the Commission's own prior work product; Russo's NSA-tipper account is a third party's recollection, not under oath, on a page **not image-verified**.
**Chain stop:** `not yet attempted` for the underlying 2000–2001 cable traffic — that material is in the Joint Inquiry, the DOJ IG reports and PENTTBOM, none read.

> **This is the first provenance chain the project has drawn for Priority 1, and every step of it stops in 2004.** The node cannot be resolved from MFRs. It requires the 2000–2001 operational record.

### PR-013 — Berger's position on the *Cole*, as it reaches this project
`U-09`

| Step | Item | Date | Note |
|---|---|---|---|
| 2 | DOC-8 printed p.5, bracketed staff note | 28 Jan 2004 | "In his interview with the Commission, National Security Adviser Sandy Berger said that the USG was essentially waiting for such a judgment from his DCI…" |
| 3 | MFR Berger (14 Jan 2004) | 14 Jan 2004 | **Located, not read.** ISCAP 2026-201 document 1 |
| 4 | Contemporaneous NSC record of the expectation | 2000 | Not located |

**Independence:** `derivative`. Berger's account reaches this project only as one staff member's paraphrase inside another witness's MFR.
**Rule applied:** U-09 is recorded as the **conflict between the two accounts**, not as a finding about what Berger said. Given DISC-007 — where an MFR demonstrably omits content from its own session — a paraphrase of one MFR inside another is a weak link, and is marked as such.

---

### PR-014 — Detainee-derived information, as it reaches this project — **a chain with no accessible root**
`B2 scope`, `../docs/05` C-D6, `V-01`, `V-02`, `V-04`, `V-05`

DOC-9 p.1, image-verified, records the terms on which the Commission obtained information from the people it considered most central to the plot. It is the clearest statement in the corpus of a provenance chain the project cannot walk.

| Link | What it is | Independence |
|---|---|---|
| 1 | The detainee's statement, under interrogation, in custody | not assessable — conditions, questions and verbatim content all unavailable |
| 2 | The interrogator's record of it | not assessable |
| 3 | CIA's summary supplied to the Commission | `derivative` |
| 4 | The Commission's use of it in its report and staff statements | `derivative`, and `circular` as against any CIA-supplied claim |

**Three access limitations, all declared by the record-holder himself on the page.**

1. **Physical access refused.** "There were seven individuals so central to the plot that the Commission might need to question them directly. **The DCI's answer was no.**"
2. **Questions relayed, not asked.** The offered substitute is "if we can get your questions, we will make sure they get asked" — i.e. the Commission could not put a follow-up, could not observe the answer being given, and could not test an evasion.
3. **The questioners were not plot experts.** Zelikow's contention on the same page is that the Commission "had the comparative advantage of having people who were experts in the 9/11 plot, **which the Agency had conceded they were not using for the interrogations**."

**Independence:** `derivative` at best, `not assessable` at the root. **Chain stop:** `access refused by the holder`.

**What this establishes.** Any proposition in the official account whose provenance root is a detainee statement reaches this project through four links, none of them auditable, with the first three inside the investigated institution. Under [`../docs/04` §3](../docs/04-controlling-methodology.md) such a proposition cannot be corroborated by a second document that shares the same root — and the 9/11 Commission Report and CIA's own products **do** share it.

**What this does not establish.** Nothing about whether any particular detainee statement is true or false, and nothing about the interrogations themselves, which are outside this project's scope and evidence base. The DCI's stated reason — that new faces would disrupt collection of intelligence of current value — is an ordinary operational reason and is recorded as such, not as evasion. It is the *chain* that is unauditable, whatever the motive for its shape.

**Consequence.** This is the concrete case that [`../docs/05` §4](../docs/05-phase-c-competing-narratives.md) C-D6 records as never yet exercised: B2 has not been applied to anything. When it is applied, the detainee-derived limb is where it bites, and this row states the chain it must be applied to. No C-series row is opened here; the source policy gates that.

### PR-015 — "Records will be sparse" — a declared reason, from the record-holder, before the searching began
`U-16`, `U-17`, `T-03`, `MD-021`

DOC-9 p.2, image-verified, Tenet to the Commission on 23 December 2003 — **five weeks before** the sessions in which he would decline to recall whether particular memoranda existed:

> "The DCI noted that records of many periods would be **sparse, because of the fast pace of events, with many meetings conducted by SVTS**, especially in the run-up to the Millenium."

**Independence:** `none (self-description)` — the custodian of the records describing his own holdings. **Chain stop:** none; the statement is what it is. **Provenance root:** this document.

**What it does.** [`../docs/04` §8A](../docs/04-controlling-methodology.md) (MD-021) permits an absence to weaken an official claim only after five conditions hold, of which the fifth is that *non-recording is not equally plausible*. This row supplies a named, ordinary, contemporaneous mechanism for non-recording — meetings held over secure video conferencing rather than on paper, at a fast tempo. It therefore **weakens** the negative-evidence case for U-16, U-17 and T-03 rather than strengthening it.

**What it does not do, and this is the part that matters.** It is **not** proof that any particular memorandum is absent for that reason. It is a statement by the party with the strongest interest in a benign explanation for missing records, made to the body that would go looking for them, and it is not corroborated by anything. It establishes that a benign mechanism **existed and was declared in advance**; it establishes nothing about any specific gap.

Both readings are recorded because the symmetry rule requires it: the statement is simultaneously the best available ordinary explanation for sparse records and exactly what an institution would say if it wished sparse records to go unexamined. Nothing in the corpus discriminates between the two, and the project does not pretend otherwise. **The discriminator would be the SVTS and record-retention policy of the period** — see §4.

---

## 4. Documents the corpus depends on and does not have

Every row below is a point at which the evidentiary chain currently stops. Listed in the order in which locating them would change the most registry rows.

| # | Document | Rows it would move | Where it is |
|---|---|---|---|
| 1 | Memorandum memorializing the May 1998 cancellation decision (or a records search establishing its absence) | A3.1, A3.2, A5.2, T-01, T-03 | Existence unknown to the decision-maker himself |
| 2 | The 6 Aug 2001 PDB, OCR'd | A10.1, A10.2, A16.1 | cia.gov — in hand, unreadable |
| 3 | June 1999 Berger→Clinton memo | T-11 | Clinton Library / NSC records |
| 4 | February 1999 MON with the President's edits | T-08 | NSC / CIA records |
| 5 | **The DCI's briefing binder prepared for the January 2004 interviews** | T-06, T-07, **U-08, U-10** | Named on DOC-7's own "TO OBTAIN FROM CIA" list, item 2. **Promoted: now four rows, across two documents — see PR-011** |
| 6 | Scheuer memoranda: 28 Jun 1999, 3 May 1996; Spot Report 24 Jun 1997 | A1.2, A1.3, A4.1, A4.5 | NARA, general MFR/records holdings |
| 7 | Internal memorandum on the 25 Mar 1999 PDB | A2.1–A2.4 | Unknown |
| 8 | Situation Room log and Presidential Diary, 11 Sep 2001 | A12.1–A12.3 | NARA / Bush Library |
| 9 | State reporting cable and diplomatic traffic on the UAE warning | T-09 | State Department |
| 10 | **MFR Berger (14 Jan 2004)** | A3.2, **U-09** | archives.gov — accessible, **not read. Now required by two independent rows** |
| 11 | ~~MFR Tenet #1 (23 Dec 2003)~~ | ~~DISC-007, DISC-008~~ | **OBTAINED AND READ, 19 Sep 2026** — DOC-9, image-verified 3/3. DISC-008 resolved; DISC-007's EC1 excluded. Row retained struck through rather than deleted, per the preservation rule |
| 12 | The March 2001 draft MON and Finding, and the EXDIR Krongard cover note and tasking paper | U-10, U-11, U-12, DISC-011 | Named by the witness as in his possession (DOC-8 p.8) |
| 13 | MFRs: Clarke ×3, Scheuer #2 and #3 | A1–A7, T-01, T-04 | **archives.gov — accessible as of 19 Sep 2026** |
| 14 | MFRs of Reno, Freeh, White, Fitzgerald | A3.2, A3.3 | Not in the ISCAP 2026-201 release; NARA general holdings |
| 15 | May 2002 Rice press-conference transcript | A8.1 | Public; unread |
| 16 | **CIA/NSC meeting-record and SVTS retention policy, 1998–2001** | U-16, U-17, T-03 — it is the discriminator for **PR-015** | Unknown. Would test whether a duty or reliable practice to create and retain such records existed, which [`../docs/04` §8A](../docs/04-controlling-methodology.md) requires before an absence counts |
| 17 | The 130-page document prepared for the DCI's public testimony, and the 3–5 DCI letters to other agency principals on terrorism | none yet — **no row depends on them** | Offered to the Commission on DOC-9 p.2; production unknown. Listed because a declared commitment whose outcome is unrecorded is a chain stop, not an absence |
| 18 | Congressional intelligence-committee hearing record on terrorism before 9/11 | V-10 | **Public and trivially checkable, and not checked.** Recorded as an open item rather than treated as common knowledge |

---

## 5. Redaction-dependent rows

Rows whose resolution is gated on material the declassifying authority has withheld. Recorded so that "unresolved" is never confused with "unsupported".

| Row | Redaction | Document / page |
|---|---|---|
| A3.1, T-02 | Attribution of who agreed the sub-30% figure | DOC-7, printed p.3, 25X1 |
| A4.x, A5.x, T-05 | Single block covering roughly 60% of the page in the section headed "The Saudis" | DOC-7, printed p.4, 25X1 — **visible only on the page image** |
| T-06 | Target locations and partner identities | DOC-7, printed pp. 8–9, 25X1 |
| A1.x, A4.x (Phase A) | Extensive 25X1/25X3 across DOC-1 and DOC-3 | Recorded in [`../docs/02` §1.1](../docs/02-adversarial-audit-phase1.md) |
| U-04, U-05 | The CIA retrieval-system name and the date range of the file review | DOC-8, printed p.2, 25X1 |
| U-11 | Predator command-and-control constraints | DOC-8, printed p.9, **25X1, X4** — a different exemption category from the 25X1 used elsewhere in the release |
| U-18 | The Moussaoui passage after the witness's first two sentences | DOC-8, printed pp. 11–12, 25X1 |
