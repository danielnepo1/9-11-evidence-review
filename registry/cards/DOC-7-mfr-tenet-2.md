# DOC-7 — Memorandum for the Record: George Tenet, 22 January 2004

> Document card under [`../../docs/04-controlling-methodology.md`](../../docs/04-controlling-methodology.md) §7.
> Read and carded: **19 September 2026**. Read in full (24 of 24 PDF pages). Partially image-verified — see §4.

---

## 1. Identification and the four dates

| Field | Value |
|---|---|
| Title | *Memorandum for the Record* — Event: Interview of George Tenet; Type of Event: Interview |
| Issuing body | National Commission on Terrorist Attacks Upon the United States, Teams Two and Three |
| Prepared by | Gordon Lederman and Alexis Albion |
| Reviewed by | Mike Hurley |
| **Event date** | 22 January 2004, DCI Conference Room, CIA HQs |
| **Document date** | 22 January 2004 — **but see §6: the document carries at least one annotation dated later** |
| **Annotation date** | Unknown. At least one bracketed note refers to a December 2004 interview |
| **Declassification date** | 8 September 2026 — ISCAP, E.O. 13526 sec. 5.3(b)(3), NSC-directed ISCAP Review, Document 10 |
| Classification as released | TOP SECRET // 25X1 // NOFORN, struck through |
| Oath | `oath: administered, image-verified`. Printed p.1, checked against the page image: "Additional notes: The witness was under oath"; "(U) Commissioner Roemer administered the oath to DCI Tenet at the start of the interview." See [`../witness-status.md`](../witness-status.md) |
| URL | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-10-release-508.pdf |
| Retrieved | 19 September 2026. HTTP 200 — access restored since the 403 recorded in [`../../docs/03` §3](../../docs/03-phase2a-mfr-verification.md) |
| Bytes | 1,906,620 |
| SHA-256 | `7434ad300a474e06672fc450dd2ae129e2b9b04636a01b1bf9cea7848bc38e28` |
| Extent | 24 PDF pages / printed pages 1–24. **Read in full** |

**Distance event → facts described: 3 to 8 years.** Facts described run from 1995–1996 to 2001. Under [`../../docs/03` §1.1](../../docs/03-phase2a-mfr-verification.md), **this document is not a contemporaneous record of anything it describes.** It is recollection given under oath in 2004, and in one significant passage (§3, T-07) it is not even that.

---

## 2. Participants — who is speaking matters

Statements in this MFR are **not all the witness's**. Four other CIA officials speak in it, **not under oath**, and Commission staff insert bracketed editorial notes. Attribution must be read per passage.

| Non-Commission | Commission |
|---|---|
| George Tenet (DCI, **under oath**) | Commissioner Richard Ben-Veniste |
| John Moseman (CIA Chief of Staff) | Commissioner Tim Roemer |
| Scott Muller (CIA General Counsel) | Philip Zelikow, Chris Kojm, Ernest May, Dan Marcus |
| Rudy Rousseau, Ben Bonk, [REDACTED 25X1] | Mike Hurley, Alexis Albion, Gordon Lederman |

Passages attributed to Bonk (pp. 2, 5, 14, 22), Rousseau (pp. 9, 20) and Muller (pp. 11, 12) are **third-party statements, not under oath, inside the MFR of a witness who was**. They carry the document's authority, not the oath's.

---

## 3. Source layer and text-extraction record

| Field | Value |
|---|---|
| Text layer | Present — agency OCR embedded in the 508-compliant release |
| OCR quality | Mediocre. Systematic corruption of classification markings, footnote numerals and passages adjacent to redactions. Examples: "Dace: January 22, 2004"; "TOP S.ECll£T"; "SONY" for "SDNY"; "Denmta" for "Derunta" |
| Extraction tool | `pypdf` 6.19.0, `extract_text()` |
| Extracted text | [`../../corpus/text/DOC-7-mfr-tenet-2.txt`](../../corpus/text/DOC-7-mfr-tenet-2.txt), SHA-256 in [`../../corpus/manifest.md`](../../corpus/manifest.md) |
| Page images | JBIG2-encoded, one per page; extracted with `pypdf` + `jbig2dec` 0.20 for image verification |

> **The extracted text layer does not represent redaction voids.** A block covering roughly 60% of printed p.4 produces *no* marker in the extracted text: the paragraph before it and the paragraph after it appear adjacent. A reader working from the text layer alone would not know the block exists. This is the empirical basis for the image-verification standard at [`../../docs/04` §7.2](../../docs/04-controlling-methodology.md).

---

## 4. Decisive quotations

All quotations below are transcribed from the page image. Printed page and PDF page coincide throughout this document.

| # | Page | Image-verified | Source layer | Assertion type | Quotation |
|---|---|---|---|---|---|
| Q1 | 3 | **yes** | native text + image | recollection | "Tenet recalled talking about this issue for a long time—he 'probed on the operations side,' and noted that the operation's prospect of success as described to him was less than 30% (the figure agreed upon **[REDACTED 25X1]**." |
| Q2 | 3 | **yes** | native text + image | recollection | "it was the strong and unanimous recommendation of Deputy Director of Operations (DDO) Jack Downing, Chief of the Counterterrorist Center (CTC) Geoff O'Connell, and Chief of Near East Division **[REDACTED 25X1]** that the operation be cancelled due to all kinds of operational impediments and the risk of collateral damage." |
| Q3 | 4 | **yes** | native text + image | recollection | "Tenet then called National Security Adviser Samuel 'Sandy' Berger to relay the news that he had cancelled the operation. He did not ask for Berger's opinion as to whether to proceed but rather called Berger to inform him of his operational decision—not to debate the issue, (that is, he did not offer Berger a choice)." |
| Q4 | 4 | **yes** | native text + image | access/process statement | "He did not recall whether there was a memorandum memorializing his decision or the three CIA officers' recommendation." |
| Q5 | 4 | **yes** | native text + image | recollection | "Tenet remarked that his contemporaneous trip to Saudi Arabia (May 1998) was entirely unrelated to the cancellation of the capture operation." |
| Q6 | 4 | **yes** | native text + image | recollection | "In the summer of 1998, Tenet did not think the USG was putting much faith in the Saudi initiative to persuade the Taliban to give up UBL—at least no more faith than in any other opportunities that presented themselves." |
| Q7 | 5 | **yes** | native text + image | analytical judgment | "It was certainly no secret that Saudi Arabia was a veritable 'aircraft carrier' for terrorist financing, but while many Saudi individuals are prominent fundraisers, does this mean that the Saudis in general are financing terrorism?" |
| Q8 | 5 | **yes** | native text + image | recollection / **unattributed parenthetical** | "Tenet had no recollection on the issue of U.S. access to the al Qaeda treasurer Madani al-Tayyiib (to whom the Saudis had given sanctuary), but noted that getting direct access to people used to be a constant problem with the Saudis (though no longer)." |
| Q9 | 5 | **yes** | native text + image | analytical judgment | "Overall, Tenet saw the Saudis as very concerned about UBL, but he was not always convinced that they gave the U.S. everything they knew about him. Saudi societal elite must have known that donations to charities were going to UBL, but Tenet cannot prove it." |
| Q10 | 19 | **yes** | native text + image | recollection / analytical judgment | "Looking back now, Tenet recognizes that at this time the country was absolutely unprotected. Although the U.S. was under attack, border, visas, and watchlists were not thought about, because all of the focus was on reporting and disrupting abroad with little thought for the connection back to the homeland." |
| Q11 | 19 | **yes** | native text + image | **editorial interpretation, Commission staff** | "[*Note: Tenet noted for the record in his December 28, 2004 interview with the Commission that the March 2000 Principals Committee meeting on lessons from the Millennium Threat did, in fact, address homeland security issues*]." |
| Q12 | 8 | no — **text layer only** | agency OCR | access/process statement | "Tenet read from a CIA staff paper prepared to brief him for this interview (which will be provided to the Commission) to describe these three occasions…" |
| Q13 | 11 | no — **text layer only** | agency OCR | quotation of a contemporaneous instrument | CIA's draft February 1999 MON: "if a successful capture operation is not feasible, we would request that you undertake offensive operations to kill Bin Ladin with his principal lieutenants." Replaced in the President's hand by: "We understand that capture may not be possible and that Bin Ladin and his lieutenants may be killed in the confrontation." |
| Q14 | 12 | no — **text layer only** | agency OCR | analytical judgment | "Tenet commented that the Pakistanis could have delivered ½ of UBL's lieutenants if they had wanted to, but were cooperating with UBL." |

**Open verification tasks:** Q12, Q13 and Q14 must be image-verified before they are used to move any registry row further. Q13 in particular quotes a primary instrument; an OCR error there would corrupt the strongest contemporaneous-text link this reading produced.

---

## 5. Redaction profile — as seen on the page images

| Location | Extent | Bears on |
|---|---|---|
| **Printed p.4, section "The Saudis"** | **A single block covering roughly 60% of the page**, marked 25X1. Produces no marker in the extracted text | A4.x, A5.x, T-05, [DISC-003](../discrepancies.md#disc-003) — it is the discriminating item for EC4 and it is withheld |
| Printed p.3 | Attribution of who agreed the sub-30% figure | A3.1, T-02, [PR-001](../provenance.md) |
| Printed pp. 6–9 | Target sets, partner services, asset descriptions | T-06 |
| Printed pp. 13, 15, 16, 20–22 | Country names, personnel and budget figures, partner services | T-10, T-12 |

Throughout, 25X1 conceals foreign-service identities, sources, locations, personnel and funding figures. Several sentences are truncated mid-clause.

---

## 6. Document-integrity finding — the date is not a single date

DOC-7 is dated 22 January 2004 and contains at least three internal cross-references to other sessions:

| Page | Text | Verification |
|---|---|---|
| 12, fn 1 | "In the DCI's follow-up session with the Commission, on January 28[th], 2004…" | text layer only |
| 13, fn 2 | "In the Commission's January 1[5?]th, 2004 interview with DCI Tenet…" | text layer only; digit uncertain; no such MFR in the ISCAP 2026-201 index |
| 19 | "Tenet noted for the record in his **December 28, 2004** interview with the Commission…" | **image-verified. The printed text does read 2004** |

The p.19 note is therefore not an OCR artifact. Read literally it refers to an interview eleven months **after** the document's own date; the Commission's Tenet interviews in the 2026 index are 23 Dec 2003, 22 Jan 2004 and 28 Jan 2004.

**What this establishes:** the document is a **layered artifact** — drafted on or about 22 January 2004 and annotated later by Commission staff. **What it does not establish:** anything about motive. The most likely explanation is ordinary staff practice plus a typing error ([`../discrepancies.md`](../discrepancies.md#disc-006), EC2), and two of the three annotations add material *against* the witness's own earlier answer. It is recorded because it defeats the assumption that an MFR speaks as of one date — not because it is suspicious.

---

## 7. Coverage — what this document does and does not address

### Addressed

Millennium threat period · the 1998 capture operation and its cancellation · Saudi liaison and terrorist financing · East Africa embassy bombings and Operation Infinite Reach · three post-1998 TLAM opportunities · February and July 1999 MONs · Northern Alliance and Masood · CIA resources and budget · the December 1998 "declaration of war" memo · CIA–FBI and CIA–NSA relations · Khobar Towers · the DCI's role in policymaking.

### **Not addressed — recorded as finding T-N1**

Exhaustive string search of the full extracted text of all 24 pages returns **zero** occurrences of: `Mihdhar`, `Hazmi`, `Malaysia`, `Kuala Lumpur`, `Moussaoui`, `Phoenix`. One occurrence of `watchlist`, at Q10 above, in a general passage about the Millennium period.

**Consequence.** Priority 1 of [`../../docs/03` §4](../../docs/03-phase2a-mfr-verification.md) — the al-Mihdhar / al-Hazmi node — is **not advanced** by this document. H5's best theoretical case remains untouched.

This is a statement about the reviewed corpus, not about the world. "Not found in DOC-7" is not "was not discussed", and is not "did not exist". The redactions above are extensive.

---

## 8. Evidentiary gaps the document declares about itself

The MFR ends with two lists. They are an inventory of gaps, written by the Commission staff who conducted the interview, and they are treated here as primary evidence of what the Commission did not have.

**"Issues that DCI Tenet did not recall and/or said he would look up" — 23 items.** Including: why the U.S. did not retaliate after Khobar Towers (1); whether UBL's possible connection to the OPM/SANG bombing was investigated (2); the sequence of Clarke's call to the UAE and whether CIA cleared it (8); CIA's transmittal letter and internal documents on the draft MON authorizing "offensive operations", and any notes on the Attorney General's position (9); whether the President's handwritten edits actually helped CIA (11); why CIA did not insert anyone into Afghanistan (17); the nature of contacts with the Saudis after Clarke's June 1999 memo (18); two May–June 1999 articles, one entitled "Saudi backsliding on terrorism" and one reporting that the Saudis had been blackmailed into sending [REDACTED] to the Taliban via the UAE (19).

**"TO OBTAIN FROM CIA" — 4 items.** (1) All of the DI products. (2) The binder prepared by the DCI's staff for this interview, including a detailed CIA timeline. (3) Charlie Allen's memo on what he accomplished driving collection after the 1998 declaration-of-war memo. (4) The DCI's correspondence with OMB on resources.

> **Item 19 of the first list and item 2 of the second are registry-relevant.** Item 19 names two 1999 articles on Saudi conduct that the Commission itself flagged and did not resolve — directly relevant to Phase 2B. Item 2 is the briefing paper that Q12 shows the witness reading from: see [`../provenance.md`](../provenance.md) PR-006.

Whether any of the 27 items was ever answered is **unknown**. Tenet MFR #3 (28 January 2004) was the first place to look and has now been read as **DOC-8** — [`DOC-8-mfr-tenet-3.md`](DOC-8-mfr-tenet-3.md). It carries **no consolidated follow-up list of its own** and answers none of the 27 items explicitly; that finding is one of the two premises whose falsification produced [DISC-007](../discrepancies.md#disc-007).

---

## 9. Reading log

| Date | Action | Result |
|---|---|---|
| 19 Sep 2026 | HTTP GET of the NARA URL | 200. Access restored; earlier 403 record preserved |
| 19 Sep 2026 | Text extraction, `pypdf` 6.19.0 | 24 pages. **Extracted page text: 68,572 characters** (sum of `extract_text()` across pages, excluding project-inserted page markers). Committed artifact: **69,066 characters / 69,528 bytes** — the difference is 24 `=== PDF PAGE n ===` delimiters inserted by this project's script. Text layer present on every page |
| 19 Sep 2026 | Full read, pp. 1–24 | Complete |
| 19 Sep 2026 | Exhaustive string search for the al-Mihdhar/al-Hazmi node | Zero hits — T-N1 |
| 19 Sep 2026 | Page-image extraction, `jbig2dec` 0.20 | pp. 3, 4, 5, 19 rendered |
| 19 Sep 2026 | Image verification of pp. 3, 4, 5, 19 | Q1–Q11 verified; p.4 redaction block discovered, absent from the text layer |
| — | Image verification of pp. 8, 11, 12 (Q12–Q14) | **Open** |
