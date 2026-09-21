# 10 — B8: Staff-Interpolation Census of the Eleven ISCAP Memoranda

> **Framing disclosure (`08` §4):** directed-search project. B8 was run because interpolations by the Commission's own note-takers bear on how much weight any MFR-based claim can carry — in this project and in the official account that rests on the same MFRs. Reported as found.

Session date: **21 September 2026.** Instrument: a multi-line bracket matcher (`[Capital … ]`, ≥25 characters, across page breaks) over the eleven ISCAP 2026-201 memoranda. **Every hit was read; the six quoted verbatim below were verified against the page image** (the memoranda carry agency-produced OCR, D-003). Hits not image-verified are summarised, not quoted.

## 1. Result

**21 bracketed interpolations in 8 of 11 memoranda.** Zero in Clarke #2, Scheuer #1, Scheuer #3.

| Type | Count | Memoranda |
|---|---|---|
| **A. Note-taker uncertainty about the witness's meaning** | 1 | Tenet #1 p.2–3 |
| **B. Unresolved drafting queries between staff, left in the released text** | 5 | Clarke #3 p.2 (×3), p.5; Rice p.9 |
| **C. Staff-supplied context, cross-reference or correction of the witness** | 13 | Berger p.5, p.14; Clarke #1 p.11, p.18; Clarke #3 p.9, p.21; Rice p.2 (×2), p.6 (×2), p.8; Scheuer #2 p.8; Tenet #2 p.20 (×2); Tenet #3 p.5, p.11 |
| **D. Executive Director's own knowledge inserted where the witness had none** | 1 | Tenet #3 p.7 |
| **E. Procedural note on a conflict of interest** | 1 | Berger p.25 |

(Type C is 13 after splitting the two interpolations on Tenet #2 p.20 that the matcher had merged with a redaction block; total 21.)

## 2. The verified instances

**E — Berger p.25** *(image-verified)*:
> "[Commission note: Commission General Counsel Dan Marcus took over the questioning for this section, noting that Executive Director Philip Zelikow had worked for the Bush transition team. Zelikow remained in the room; no objection to his presence was raised by Berger or Commissioners Gorelick, Roemer, or Ben-Veniste.]"

The section is "The Clinton-Bush Transition." A conflict was recognised in the room, handled by a change of questioner, and recorded — with the Executive Director remaining present. This is a contemporaneous, first-hand record bearing on **T-4.3** (Commission independence). It establishes that the conflict was known and partially managed; it establishes nothing about the content of anything Zelikow did.

**B — Clarke #3 p.2** *(image-verified)*, three queries on one page of the released memorandum:
> "They also added INS to the JTTFs [CK—Alexis, is this right?] out of concern that al-Qa'ida associates might be exportable [Alexis: that's what I've got in my notes; presume it means 'might come into America,' but lemme know what you have…]"
> "They tried this at least twice, Clarke said. [AA: do I have this right?]"
> "[Alexis: my notes also have 'and Amcits show ID too'—can you make sense of that point?]"

**B — Clarke #3 p.5** *(image-verified)*: "When the Taliban's air defenses spotted one Predator, the CIA wanted to stop the flights [AA: do I have that right? Notes are murky]."

**B — Rice p.9** *(image-verified)*: "she called Rumsfeld [CK that in Kojm/Zelikow notes] and the issue got resolved."

**D — Tenet #3 p.7** *(image-verified)*:
> "Tenet had no recollection of a conversation with the President about the PDB item on January 25th 2001. [According to Zelikow, this PDB item flagged current view on responsibility for the Cole attack and is said to have prompted the President to ask a question about what the consequences might be of killing UBL]. He could not talk to either the content or context of the conversation…"

The witness had no recollection; the Executive Director's account of the same item — hedged, "is said to have," source unstated — was written into the witness's memorandum.

**C — Tenet #2 p.20** *(image-verified)*: "[This was in reference to the complaint made by C/Alec Mike Scheuer that NSA was not responding to CTC's requests for raw SIGINT]" and "[Rousseau noted that he would research this issue for the Commission]". Also on this page, Tenet: "no one brought to his attention complaints from CTC about non-disseminated NSA material" — incidental to claim A1's family, logged for the Tenet #2 card.

**A — Tenet #1 p.2–3**: the known divergence, already carded (`cards/MFR-TENET-20031223.md` §6.1).

## 3. What the census establishes

- **The released memoranda are working drafts.** Five unresolved staff-to-staff queries ("do I have this right?", "Notes are murky", "CK that in Kojm/Zelikow notes") survive in the text as declassified. The MFRs cited by the Commission Report as "interview (date)" are, at least in these cases, documents whose own authors had not finished checking them. This is a fact about the record's condition, not about its accuracy.
- **Interpolation is common, not exceptional.** 21 instances across 148 pages, in 8 of 11 documents. A reader of an MFR is reading the witness *and* the staff, and the released text does not always mark which is which beyond brackets.
- **Two instances go beyond annotation.** Type D (Zelikow's knowledge inserted where Tenet had none) and Type E (the transition-team conflict) are the two that a reader of the Commission's *citations* would never learn of.

## 4. Incidental capture — claim A9, verbatim

Rice p.9, image-verified, under "The Summer of Threat":
> "During the summer 2001 threat spike, we responded to the intel that was there, which pointed to the Gulf, Israel, or other foreign locations, Rice said. … But there was no threat-reporting stream about attacks inside the United States."

This project has carried A9 since `03` as *"all of the reporting pointed abroad."* **That paraphrase is broader than the witness's words.** Rice's claim is scoped to (i) the summer 2001 spike and (ii) a *threat-reporting stream* — not "all reporting," and not all periods. This is quantifier drift inside the project's own ledger (`05` §3.1), in the direction that made the claim easier to contradict. **A9's wording is corrected in the evidence matrix; its status (inconclusive) does not change**, because the four items in `03` §1.4 are still missing — but the test is now against the narrower proposition.

## 5. What this does not permit us to conclude

That any interpolation altered what a witness said. That the drafts are unreliable — a query left in a draft is a note-taker being careful, not careless. That the Zelikow interpolations reflect anything beyond the Executive Director's presence and knowledge, which the Commission never concealed. B8 measures the *condition* of the record on which MFR-based claims rest; it changes no claim's status.

## 6. Reproducibility

Matcher: `re.compile(r"\[([A-Z][^\[\]]{25,900}?)\]", re.S)` over the concatenated page text of each memorandum in `corpus/text/MFR-*/`. Image verification recorded in `corpus/pages.db` for Berger 25; Clarke #3 2, 5; Rice 9; Tenet #2 20; Tenet #3 7.
