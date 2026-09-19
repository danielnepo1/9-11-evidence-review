# Anomaly Register

> Living instrument. Governed by [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) §6.1.
> Opened 19 September 2026. Last update **19 September 2026** — DOC-9 read; DISC-007 EC1 excluded, DISC-008 resolved, DISC-004 and DISC-012 revised.

The discrepancy ledger says **what kind** of discrepancy exists. It cannot say **how far the evidence permits escalation**, or **which anomaly is worth chasing next**. This register adds both. Every row in [`discrepancies.md`](discrepancies.md) has a row here.

---

## 1. Escalation ladder — levels may not be skipped

| Level | Name | What permits escalation to it |
|---|---|---|
| **1** | Discrepancy | Records or claims do not align |
| **2** | Unresolved anomaly | Ordinary reconciliation has been **tested** and remains inadequate |
| **3** | Structured pattern | Multiple **substantially independent** anomalies point the same way |
| **4** | Evidence of concealment | Affirmative acts or records support deliberate withholding or deception |
| **5** | Evidence of foreknowledge or participation | Evidence connects an actor to specific operational knowledge or material conduct |

Each row records **exactly what permits its level**. Two rules that do the real work:

- **A large collection of dependent, low-quality discrepancies does not become a structured pattern.** Level 3 requires the anomalies to be *substantially independent* — if they share a provenance root ([`provenance.md`](provenance.md)), they count once.
- **Levels are not skipped.** A level-1 row cannot be described in level-4 language. "Suspicious" is a reason for further testing, not a finding about motive.

## 2. Priority — research value, not probability of conspiracy

> **P0–P3 measures what is worth working on next. It does not measure how likely any hypothesis is.** A P0 row is one where obtainable evidence would separate major hypotheses. A row can be P0 while its most likely explanation is entirely ordinary.

| Priority | Meaning |
|---|---|
| **P0** | Documented fracture affecting a central claim and capable of separating major hypotheses |
| **P1** | Material unresolved tension with obtainable discriminating evidence |
| **P2** | Real anomaly with several viable ordinary explanations |
| **P3** | Low-centrality curiosity or weakly sourced allegation |

## 3. Register

Retrofitted from [`discrepancies.md`](discrepancies.md) on 19 September 2026. Source quality is stated as the weakest link in the chain, not the strongest.

| ID | Observation | Category | Source quality | Ordinary explanation tested? | Level | What permits that level | Priority | Missing discriminator |
|---|---|---|---|---|---|---|---|---|
| **DISC-001** | Scheuer: no strategic analytic product or NIE before mid-1999. Tenet: a strategic framework existed after 1998 and "The Plan" followed in 1999 | documentary contradiction | Two recollections under oath, 4–5 years after the fact; one not image-verified | **Yes.** EC1 (different objects — analytic product vs. operational plan) fits the evidence completely | **1** | Ordinary reconciliation is not merely available, it is the most natural reading. Nothing has been tested that survives it | **P2** | The text of "The Plan"; the NIC production record; Scheuer's 28 Jun 1999 memo |
| **DISC-002** | The sub-30% estimate: who was told, and in which direction it flowed | timeline / conflicting testimony | Image-verified quotation; the deciding attribution is **redacted** | **Yes.** EC1 and EC2 both fit; Tenet's account concedes against interest on one point | **2** | Reconciliation tested and incomplete: the two accounts describe opposite directions of flow and no contemporaneous record exists either way | **P1** | MFR Berger; the 25X1 attribution on DOC-7 p.3 |
| **DISC-003** | Whether a Saudi initiative bore on the May 1998 cancellation | conflicting testimony | Image-verified on both sides; **the discriminating material is classified** | **Partially.** EC2 (Scheuer inferred a link from timing) is live and untested; EC4 **cannot be assessed at all** | **2** | Ordinary explanations tested and none is decisive — but the escalation stops here because the item that would decide it is withheld, and **a withheld document is a limitation, not evidence** | **P1** | The ~60% redaction block on DOC-7 p.4; the cancellation memorandum |
| **DISC-004** | Scheuer calls an instrumental ISI–UBL training relationship "too conspiratorial"; Tenet says the Pakistanis "were cooperating with UBL" | conflicting testimony | **Image-verified 19 Sep 2026** — and the Tenet remark is a *parenthetical staff aside*, not a reported answer | **Yes.** The scope gap (training relationship vs. cooperation generally) dominates | **1** | Two different propositions, not a contradiction. Verification removed the stated limit and the row did **not** rise: the parenthetical form makes the Tenet side weaker, not stronger | **P3** | Contemporaneous ISI–UBL reporting |
| **DISC-005** | The February 1999 MON: Tenet and CIA's General Counsel read the President's edit as narrowing; Commissioner Ben-Veniste reads the NSC note differently | documentary contradiction | Quotation of a contemporaneous instrument, **text layer only** | **Yes.** EC1 fits — they may be reading different instruments | **1** | A recorded disagreement about the meaning of a document neither party is quoting in full | **P1** | The February 1999 MON and the NSC note |
| **DISC-006** | DOC-7 carries a bracketed note citing a "December 28, 2004" interview, 11 months after its own date | possible administrative error | Image-verified on the decisive page | **Yes, and it succeeded.** DOC-8 p.3 contains the correction the note summarises, dated 28 Jan 2004 | **1** | Substantially resolved toward ordinary error. Residual: a scope gap between "Principals Committee meeting" and "after-action report at NSC" | **P3** | Which event the two descriptions denote |
| **DISC-007** | Content DOC-7's footnote attributes to the 28 Jan 2004 session is absent from that session's MFR | material omission | **Both sides now image-verified**; the negative finding is exhaustive and variant-checked | **Yes, performed 19 Sep 2026.** EC1 **excluded** — DOC-7 p.12 fn 1 image-verified as "January 28th, 2004", DOC-9 read in full with zero hits. EC2 (ordinary selective note-taking) is the only live class and fits completely | **2** | Stays at 2: the finding — *an MFR is not a complete record of its session* — is established, and the ordinary explanation for it is untested only in the sense that no second instance has been sought. It does **not** rise: EC3 is contradicted by the omitted passage being favourable to the witness | **P3** *(was P0)* | The Commission's internal drafting records — **not reachable**. The cheap discriminators are spent |
| **DISC-008** | DOC-8 calls 22 Jan 2004 the witness's "first interview"; the index lists a Tenet MFR of 23 Dec 2003 | timeline discrepancy | Image-verified on both sides | **Yes — EC1 confirmed, 19 Sep 2026.** DOC-9's own event-type field reads "Luncheon Meeting"; V-12 records the interviews as still prospective at that date | **RESOLVED** | Not an anomaly. The front matter is accurate; the contingency 18 U-rows inherited is discharged | — | — |
| **DISC-009** | One 13-page document dates the same Millennium after-action review to both 10 and 15 March 2000 | timeline discrepancy | **Both readings image-verified** | **Yes.** EC2 dominates — a staff synthesis of spoken answers, the witness reading from a binder | **1** | Ordinary explanation fits fully. Retained as a **calibration datum** for MFR date reliability, not as a lead | **P3** | The NSC after-action report |
| **DISC-010** | Berger (via a staff note) says the government awaited a DCI judgment on the *Cole*; Tenet has no recollection of being told so | conflicting testimony | Image-verified — but Berger's side is **a staff paraphrase inside another witness's MFR** | **Yes.** EC1 fits: an expectation can exist without being voiced to the person it rests on | **1** | One side of the conflict has not been read in its own document | **P1** | **MFR Berger**, read in full |
| **DISC-011** | The DCI and his own officer disagree, in the same room, about what the March 2001 MON tasking was | internal agency disagreement | Image-verified | **Yes.** EC1 fits — different taskings may have reached different levels | **1** | A recorded disagreement, with the contemporaneous cover note taking one side | **P2** | The CIA Executive Director's tasking paper |
| **DISC-012** | Two Commission staff in the same room record the same DCI recollection as being about two different Presidents, eighteen months apart | ambiguity | **Image-verified**; the disagreement is recorded on the page by the drafter himself | **Yes.** EC1 — ordinary ambiguity in spoken recollection with no verbatim record — fits completely | **1** | An ambiguity of reference, not a conflict of assertion. Nothing is contradicted; the referent is undetermined | **P2** | CTC briefing records for late 1999 and summer 2001; a document carrying the "5 to 15 attacks" figure |

## 4. What this register says about the corpus as a whole

**No row is above level 2. No level-3 structured pattern is asserted**, and none could be on the present record: the candidate anomalies are not substantially independent — DISC-002, DISC-003 and DISC-005 all trace through the same two MFRs and the same witness, and [`provenance.md`](provenance.md) PR-011 shows four of those passages derive from one 2004 CIA briefing binder. Under §1 they count close to once.

### 4.1 The two P0 rows are spent — 19 September 2026

When this register was opened, two rows sat at **P0** and both were about the same thing: **whether a Memorandum for the Record is a complete record of its session.** One reachable, unread document (DOC-9) tested both. It was read, in full, and is the first document in the corpus image-verified at 100%.

| Row | Was | Now | Result |
|---|---|---|---|
| DISC-007 | level 2, **P0** | level 2, **P3** | EC1 excluded. **An MFR is not a complete record of its session** — one confirmed instance. Retained as a calibration datum |
| DISC-008 | level 2, **P0** | **resolved** | The 23 Dec 2003 event was a luncheon meeting, not an interview. DOC-8's front matter is accurate; 18 U-rows discharged |

**No row is at P0 any more, and no row is above level 2.** No level-3 structured pattern is asserted, and the independence objection above is now stronger rather than weaker: the reading that most changed the project was procedural, and it made the corpus's silences *less* informative, not more.

**What the register recommends next, on research value alone.** Four rows sit at **P1** — DISC-002, DISC-003, DISC-005, DISC-010 — and DISC-010's discriminator is a single unread, reachable document (**MFR Berger**, reserved DOC-10) that also bears independently on A3.2. DISC-002's discriminator is partly the same document. That is the highest-leverage next pull, and it is what [`../docs/06-audit-program-v2.md`](../docs/06-audit-program-v2.md) step 5 schedules.

DISC-005's discriminator is the February 1999 MON itself, which is not held and is not reachable by any step in the current program. It stays at P1 and stays unworked, for the same reason DISC-003 does: **a limitation is recorded as a limitation, not converted into a task.**

DISC-003's discriminator is a 60% redaction block on DOC-7 p.4 and is **not obtainable by this project** at all.

### 4.2 A note on how this went

The highest-priority item in the project was not the most dramatic. It was a small procedural question — is an MFR complete? — whose answer changes the value of everything else, and the answer reduced what the corpus can support rather than increasing it. That is the register working as intended, and it is worth recording that the result went in the deflationary direction.
