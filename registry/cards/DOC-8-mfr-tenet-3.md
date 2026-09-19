# DOC-8 — Memorandum for the Record: George Tenet, 28 January 2004

> Document card under [`../../docs/04-controlling-methodology.md`](../../docs/04-controlling-methodology.md) §7.
> Read and carded: **19 September 2026**. Read in full (13 of 13 PDF pages). Page images inspected independently for 7 of 13 pages — see §4.

---

## 1. Identification and the four dates

| Field | Value |
|---|---|
| Title | *Memorandum for the Record* — Event: Interview of George Tenet; Type of Event: Interview |
| Issuing body | National Commission on Terrorist Attacks Upon the United States, Team Three |
| Prepared by | Alexis Albion |
| Reviewed by | Gordon Lederman |
| **Event date** | 28 January 2004, DCI Conference Room, CIA HQs |
| **Document date** | 28 January 2004 |
| **Annotation date** | None detected. Unlike DOC-7, this document contains no internal cross-reference postdating itself |
| **Declassification date** | 8 September 2026 — ISCAP, E.O. 13526 sec. 5.3(b)(3), NSC-directed ISCAP Review, Document 11 |
| Classification as released | TOP SECRET // 25X1 // NOFORN, struck through. One passage additionally marked **25X1, X4** (printed p.9) |
| **Procedural status** | `oath: carried over, image-verified` — see §2 |
| Archival control marking | Handwritten, top right of printed p.1: **"MFR 04017364"**. DOC-7 carries **"MFR 04017365"** in the same position. Consecutive numbers, assigned in the reverse order of the sessions |
| URL | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-11-release-508.pdf |
| Retrieved | 19 September 2026, HTTP 200 |
| Bytes | 1,406,317 |
| SHA-256 | `f8b42694b3a7ea3fd149bd8047cb11ffdb6e9734d47e2a24bf9feb3dfbfeeb2e` |
| Extent | 13 PDF pages / printed pages 1–13. **Read in full** |

**Distance event → facts described: 3 to 8 years.** The facts described run from 1998 to September 2001, plus commentary on the state of affairs in 2004. Under the three-dates rule ([`../../docs/03` §1.1](../../docs/03-phase2a-mfr-verification.md)), **this document is not a contemporaneous record of anything it describes.**

---

## 2. Procedural status — an oath carried, not administered

Printed p.1, **image-verified**:

> "Additional notes: The witness was placed under oath at the start of his first interview on January 22, 2004. At the start of this interview, he was reminded that he was still under oath"

Three observations, recorded because they bear on how much the oath adds here:

1. **No oath is administered at this session.** What is recorded is a reminder that an oath administered six days earlier still applied.
2. **Commissioner Roemer, who administered the 22 January oath, is not among the Commission participants listed for 28 January.** The listed Commission participants are Ben-Veniste, Zelikow, Marcus, Hurley, Albion and Lederman. No one is named as giving the reminder.
3. **The document calls 22 January 2004 the witness's "first interview".** The ISCAP 2026-201 index lists a Tenet MFR dated **23 December 2003**. Either that earlier event was not an "interview" in the Commission's own usage, or the front matter here is inaccurate. Recorded at [`../discrepancies.md`](../discrepancies.md#disc-008) — **not resolved**, and a direct reason to read DOC-9 (Tenet #1).

Registered in [`../witness-status.md`](../witness-status.md) §3. Permitted label: **"under oath (carried over from 22 Jan 2004; reminded, not re-administered)"**.

---

## 3. Participants — who is speaking

| Non-Commission | Commission |
|---|---|
| George Tenet (DCI, under oath, carried over) | Commissioner Richard Ben-Veniste |
| John Moseman (CIA Chief of Staff) | Philip Zelikow |
| Scott Muller (CIA General Counsel) | Dan Marcus |
| **Rudy Russo**, Ben Bonk, [REDACTED 25X1] | Mike Hurley, Alexis Albion, Gordon Lederman |
| The DCI's assistant [REDACTED 25X1] | |

**Name discrepancy across the two MFRs.** DOC-7 p.1 (image-verified) lists "Rudy Rousseau"; DOC-8 p.1 (image-verified) lists "Rudy Russo". The same participant appears under two spellings in two Commission documents six days apart. Recorded because attribution of the passages at DOC-7 pp. 9 and 20 and DOC-8 pp. 2 and 10 depends on identifying the speaker.

**Statements by Russo, Bonk, Moseman and Muller are not covered by the witness's oath.** The document itself makes the point at printed p.11, where the staff insert: *"[Note: Bonk was not present at the September 4th meeting]"* — immediately after recording Bonk's recollection of it.

---

## 4. Source layer and verification coverage

| Field | Value |
|---|---|
| Text layer | Present — agency OCR embedded in the 508-compliant release |
| OCR quality | Mediocre. Examples of corruption confirmed against the page images: "On March lilt" for "On March 12th"; "Ben Book" for "Ben Bonk"; "rcdnndancy" for "redundancy"; "arugments" for "arguments"; "he issue" for "the issue" |
| Extraction tool | `pypdf` 6.19.0, `PdfReader.extract_text()` |
| Extracted text | [`../../corpus/text/DOC-8-mfr-tenet-3.txt`](../../corpus/text/DOC-8-mfr-tenet-3.txt) |
| Page images | JBIG2; extracted with `pypdf` 6.19.0 + `jbig2dec` 0.20 and **inspected independently of the text layer** |

### 4.1 Page-level verification coverage

| Printed page | Image inspected | Subject |
|---|---|---|
| 1 | ✅ | Front matter, oath, the Kuala Lumpur story |
| 2 | ❌ | KL continued; CTC hub-and-spoke |
| 3 | ✅ | Millennium after-action review correction; Predator |
| 4 | ❌ | Predator funding and weaponisation |
| 5 | ✅ | Cole; the Berger conflict |
| 6 | ❌ | Blue Sky memo; the transition |
| 7 | ❌ | PDBs; the new administration's CT policy |
| 8 | ✅ | The March 2001 draft MON and Finding |
| 9 | ✅ | Predator command and control; funding; summer of threat |
| 10 | ✅ | Summer 2001; focus overseas; CTC post-9/11 review |
| 11 | ✅ | 4 September 2001 Principals' meeting; a new MON; Moussaoui |
| 12 | ❌ | Moussaoui continued; lessons learned |
| 13 | ❌ | TTIC; organising for the GWOT |

**Coverage: 7 of 13 printed pages = 54%.** Every quotation in §5 marked ✅ is transcribed from the page image. Quotations from unverified pages are marked and **may not move a registry row** until verified.

### 4.2 Redaction profile — as seen on the page images

Redactions in DOC-8 render as **grey shaded blocks** on the page image, unlike DOC-7, where at least one large redaction is a **white void** invisible in both the text layer and a casual reading. DOC-8's style is more visible — but the text layer still does not represent them, so the same rule applies.

| Location | Extent | Bears on |
|---|---|---|
| p.1 | Two participant identities | Attribution of §3 |
| p.2 | The retrieval-system name; the date range of the file review; a speaker's identity | U-04, U-05 |
| p.9 | A block marked **25X1, X4** — a different exemption category from the 25X1 used elsewhere | U-11 |
| pp. 3, 4, 9, 10, 11, 12 | Programme names, dollar figures, partner services, reporting streams | U-05, U-09, U-11, U-13 |

No redaction in DOC-8 approaches the scale of the block on DOC-7 printed p.4.

---

## 5. Decisive quotations

| # | Page | Image-verified | Source layer | Assertion type | Quotation |
|---|---|---|---|---|---|
| Q1 | 1 | ✅ | native text + image | access/process statement | "Tenet noted that he had not reviewed the material on this story, (and Zelikow acknowledged that the DCI is not a first hand witness for this episode)." |
| Q2 | 1 | ✅ | native text + image | analytical judgment | "In Tenet's opinion, the Joint Inquiry's report misinterpreted all of this; there is a misconception that CIA and FBI were not talking to each other, but FBI was, in fact, far more aware of the Kuala Lumpur meeting than has previously been made public." |
| Q3 | 1 | ✅ | native text + image | **editorial interpretation, Commission staff** | "[Zelikow noted that the Commission had evidence that FBI was informed of this matter by CIA, former FBI Director Freeh has briefed the Commission on this subject twice, and the Commission noted this in its staff statement at its January 2004 public hearing]." |
| Q4 | 3 | ✅ | native text + image | **correction of the witness's own earlier statement** | "Tenet noted that he wished to correct his statement from his earlier interview with the Commission (January 22, 2004) that no homeland security mechanism was part of the Millennium after-action review. The March 10th, 2000 after-action report at NSC had four issues on its agenda, one of which was immigration, and another US-Canadian border security." |
| Q5 | 5 | ✅ | native text + image | recollection / **access-to-record statement** | "The DCI said that his recollection of the CIA's investigation into the attack was entirely dependent on the documents in his briefing book…" |
| Q6 | 5 | ✅ | native text + image | **third-party report of another witness's testimony** | "Tenet was surprised at the notion that the NSC was awaiting his conclusive judgment on responsibility for the Cole attack before taking action against al Qaeda. [*Note: In his interview with the Commission, National Security Adviser Sandy Berger said that the USG was essentially waiting for such a judgment from his DCI before taking responsive action*]." |
| Q7 | 8 | ✅ | native text + image | access/process statement | "Tenet himself did not review the new authorities before handing them over to NSC. Reading the cover note to the MON and Finding written by EXDIR Krongard (from his briefing binder), Tenet observed that the note said this was an expansion of CIA's authorities, as well as registering that the preparation of these documents was backwards (that CIA should not be driving a policy initiative but responding to one)." |
| Q8 | 8 | ✅ | native text + image | **internal disagreement** | Tenet: "having been asked to consolidate the MONs, CIA interpreted this as an opportunity to write a clearer document". Bonk: "he never saw their tasking as consolidating previous MONs." |
| Q9 | 8 | ✅ | native text + image | analytical judgment (Bonk, not under oath) | "The document needed to authorize direct kill authority in order to make use of armed Predator, Bonk noted. (Moseman agreed with this reading of what authority the MON was looking for)." |
| Q10 | 10 | ✅ | native text + image | recollection / analytical judgment | "He noted that throughout the threat period the focus was almost exclusively overseas based on the reporting CIA was receiving." |
| Q11 | 10 | ✅ | native text + image | recollection | "There was a feeling of great frustration at the Agency at that time: an attack was delayed, but no one knew where it was going; there was a sense that the attack might be coming to the United States, but no one knew for sure." |
| Q12 | 10 | ✅ | native text + image | institutional finding, reported | "[REDACTED] noted that, after September 11th, CTC looked back to see if any of the information CIA was picking up during the summer of 2001 related to the 9-11 attacks, and concluded that it was a separate and unrelated stream of intelligence…" |
| Q13 | 11 | ✅ | native text + image | recollection | "No decision was made on the question of who fired the armed UAV, however." |
| Q14 | 11 | ✅ | native text + image | access/process statement | "Tenet did not recall his September 5th meeting with Rice, and there appears to be no memo capturing the meeting." |
| Q15 | 2 | ❌ **text layer only** | agency OCR | third-party report (Russo, not under oath) | "CIA asked NSA to put Midhar on a watchlist… having put individuals on the NSA tipper, CIA would have been counting on NSA to pass on additional undisseminated information without CIA having to ask for it." |
| Q16 | 2 | ❌ **text layer only** | agency OCR | **editorial interpretation, Commission staff** | "Zelikow noted that the Commission's perspective on the KL story is to see it less in terms of a watchlisting blunder and more as a failed intelligence operation that opens a window onto systemic problems at CIA in managing transnational operations." |
| Q17 | 2 | ❌ **text layer only** | agency OCR | recollection | "Tenet does not recall the KL case being highlighted for him; the case did not leap out at him." |
| Q18 | 12 | ❌ **text layer only** | agency OCR | access/process statement | "Russo noted that the sequence of events for this case [Moussaoui] (what CIA knew when) can be documented, and CIA will go back recreate this story for the Commission." |

**Open verification tasks:** Q15, Q16, Q17 (printed p.2) and Q18 (printed p.12). Q15 and Q17 are the two most consequential statements in the document about the al-Mihdhar node and **must** be image-verified before they move anything.

---

## 6. What this document does and does not address

### Addressed

The Kuala Lumpur meeting and watchlisting · CTC hub-and-spoke management · the Millennium after-action review (and a correction to the previous session) · Predator, reconnaissance and weaponisation · the USS *Cole* response · the Blue Sky memo · the 2000–2001 transition · the PDB process under two presidents · the March 2001 draft MON and Finding · the 4 September 2001 Principals' meeting · Hadley's 10 September 2001 memo · Moussaoui · TTIC and post-9/11 organisation.

### Not addressed — recorded as a negative finding

Exhaustive string search of the full extracted text of all 13 pages, **including transliteration variants**:

| Term searched | Hits |
|---|---|
| `Midhar` | 2 (printed pp. 1, 2) |
| `Mihdhar` | 0 |
| `Kuala` / `KL` | present throughout printed pp. 1–2 |
| `watchlist` (any form) | 6 |
| `Moussaoui` | present, printed pp. 11–12 |
| **`Hazmi` / `Hamzi` / `Alhazmi`** | **0** |
| **`February 1999`** / **`1999 MON`** | **0** |
| **`Phoenix`** | **0** |
| `Masood` | 1 (his murder, printed p.10 — unrelated to the 1999 covert-action discussion) |

**U-N1.** DOC-8 discusses the Kuala Lumpur meeting and al-Mihdhar, but **never mentions Nawaf al-Hazmi**, under any spelling. The node is addressed in half.

**U-N2.** DOC-8 contains **no discussion of the February 1999 MON or of President Clinton's handwritten edits to it** — although DOC-7 footnote 1 (printed p.12) states: *"In the DCI's follow-up session with the Commission, on January 28[th], 2004, Tenet again spoke to the President's edits to the February 1999 MON…"* See [`../discrepancies.md`](../discrepancies.md#disc-007). This is a finding about the completeness of MFRs as records, and it is the reason the reading queue was ordered as it was.

---

## 7. Evidentiary gaps the document declares about itself

Unlike DOC-7, DOC-8 carries no consolidated follow-up list. The commitments and gaps are scattered through the text:

| Page | Item | Type |
|---|---|---|
| 2 | "CIA is now reviewing every file going back [REDACTED] to see if the people involved in this meeting can be identified" | Commitment; outcome unknown |
| 3 | On a CT supplemental: "I don't know what happened." Refers the Commission to the Director of OMB | Declared gap in the witness's own knowledge |
| 3 | "[*The Commission's General Counsel, Dan Marcus, remarked that Team 2's Kevin Scheid is investigating this matter at CIA*]" | Referred elsewhere within the Commission |
| 5 | "(CIA will check to see if there are MFRs for these meetings)" — Rumsfeld meetings of 4 May and 27 July 2001 | Commitment; outcome unknown |
| 7 | "(He said that CIA would hunt down information on these Powell meetings for the Commission)" | Commitment; outcome unknown |
| 8 | "Muller added that CIA has not been able to find a MFR for this meeting" — Rice, 15 or 17 March 2001 | **Declared absence of a record** |
| 8 | "He does have the paper that came to him from CIA's Executive Director on the tasking for the MON and Finding" | Document identified, not produced |
| 11 | "Tenet did not recall his September 5th meeting with Rice, and there appears to be no memo capturing the meeting" | **Declared absence of a record** |
| 12 | "CIA will go back recreate this story for the Commission" — the Moussaoui timeline | Commitment; outcome unknown |

> **Pattern worth recording.** Two of the nine items are declared absences of records for meetings between the DCI and the National Security Adviser in 2001, and four more are undertakings by CIA to reconstruct or supply material. Whether any of the four was fulfilled is **unknown to this project**. That is a statement about this corpus, not about CIA's conduct.

---

## 8. A structural observation about this witness's evidence

Across DOC-7 and DOC-8 the same pattern appears four times: the witness's account is read aloud from CIA-prepared 2004 material rather than recalled.

| Document | Page | What was read from |
|---|---|---|
| DOC-7 | 8 | "a CIA staff paper prepared to brief him for this interview" — the three TLAM opportunities |
| DOC-7 | 11 | The February 1999 MON text, read out |
| DOC-8 | 5 | "his recollection … was entirely dependent on the documents in his briefing book" — the *Cole* investigation |
| DOC-8 | 8 | "Reading the cover note to the MON and Finding written by EXDIR Krongard (from his briefing binder)" |

**This is not an accusation of anything.** A witness preparing with his agency's records is ordinary and arguably responsible. What it changes is the **provenance** of the resulting testimony: for those passages, the underlying source is a 2004 CIA document, not the witness's memory, and the oath attaches to his reading of it. Recorded at [`../provenance.md`](../provenance.md) PR-011. The briefing binder is named on DOC-7's "TO OBTAIN FROM CIA" list, item 2, and has not been located.

---

## 9. Reading log

| Date | Action | Result |
|---|---|---|
| 19 Sep 2026 | HTTP GET of the NARA URL | 200 |
| 19 Sep 2026 | Text extraction, `pypdf` 6.19.0 | 13 pages. **Extracted page text: 43,781 characters** (sum of `extract_text()` across pages, excluding project-inserted page markers). Committed artifact: **44,044 characters / 44,252 bytes** — the difference is 13 `=== PDF PAGE n ===` delimiters inserted by this project's script. Text layer present on every page |
| 19 Sep 2026 | Full read, printed pp. 1–13 | Complete |
| 19 Sep 2026 | String search incl. transliteration variants | U-N1, U-N2 |
| 19 Sep 2026 | Page-image extraction, `jbig2dec` 0.20 | pp. 1, 3, 5, 8, 9, 10, 11 rendered |
| 19 Sep 2026 | Independent inspection of those 7 page images | Q1–Q14 verified; OCR errors in §4 identified; the March 10 / March 15 conflict (DISC-009) found |
| — | Image verification of pp. 2, 4, 6, 7, 12, 13 | **Open** |
