# Witness Procedural-Status Register

> Living instrument. Governed by [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) §7.4 (MD-012).
> Opened 19 September 2026 as the output of a repository-wide audit of the words "under oath", "sworn" and `sob juramento`.

---

## 1. Why this register exists

"Sworn testimony" and "interview record" are not the same evidentiary object. An oath changes the legal exposure of the speaker and therefore, arguably, the weight of the statement. Using the language of sworn testimony for a document that records no oath inflates the record — and doing so is easy, because Commission MFRs of both kinds look identical on the page.

**The rule (MD-012):**

> The words "under oath", "sworn testimony" and any equivalent are used **only** where the source document itself, or a directly linked procedural record, establishes that status. Everywhere else the narrower label applies: **"Commission interview record"** or **"interview memorandum"**.

A second requirement follows from the image-verification standard: a procedural status read from an extracted text layer is recorded as such. The text layer of these releases is demonstrably imperfect, and "the witness was under oath" is exactly the kind of one-line front-matter entry that OCR mangles.

## 2. Controlled vocabulary for procedural status

| Token | Meaning |
|---|---|
| `oath: administered, image-verified` | The document records an oath being administered at this session, and the page image has been checked |
| `oath: administered, text layer only` | The document records it; the reading has not been checked against the page image |
| `oath: carried over, image-verified` | The document records the witness being reminded of an oath administered at an **earlier** session; no fresh administration at this one |
| `no oath recorded` | The document records no oath. Default label: **Commission interview record** |
| `procedural status unknown` | Not determined. Default label: **interview memorandum** |

## 3. Register

| Doc | Document | Procedural status | Exact basis | Permitted label |
|---|---|---|---|---|
| **DOC-2** | MFR — Condoleezza Rice, 7 Feb 2004 | `no oath recorded` | [`../docs/02` §1.1](../docs/02-adversarial-audit-phase1.md) records: "**reunião, não depoimento sob juramento.** O documento não registra juramento." Not image-verified | **Commission interview record.** Never "testimony", never "sworn" |
| **DOC-3** | MFR — Mike Scheuer #1, 11 Dec 2003 | `oath: administered, text layer only` | [`../docs/02` §1.1](../docs/02-adversarial-audit-phase1.md) records the oath as administered by Commissioner Ben-Veniste at the start and "registrado explicitamente no documento". **The page image has not been checked.** DOC-3 is under the re-carding gate | "Under oath (recorded in the document; **not image-verified**)". The qualifier is not optional |
| **DOC-7** | MFR — George Tenet #2, 22 Jan 2004 | `oath: administered, image-verified` | Printed p.1, checked against the page image: "Additional notes: The witness was under oath" and "(U) Commissioner Roemer administered the oath to DCI Tenet at the start of the interview." | "Under oath", unqualified |
| **DOC-8** | MFR — George Tenet #3, 28 Jan 2004 | `oath: carried over, image-verified` | Printed p.1, checked against the page image: "Additional notes: The witness was placed under oath at the start of his first interview on January 22, 2004. At the start of this interview, he was reminded that he was still under oath" | "Under oath (carried over from 22 Jan 2004; **reminded, not re-administered**)". See §4 |
| DOC-1, DOC-4, DOC-5, DOC-6 | Institutional documents and index pages | not applicable | No witness | — |

## 4. Two qualifications that matter

**DOC-8's oath is carried, not fresh.** The 28 January session records no administration of an oath — it records a reminder that an oath administered six days earlier still applied. No commissioner is recorded as administering anything, and Commissioner Roemer, who administered the 22 January oath, is **not** among the Commission participants listed for 28 January. Whether a reminder by staff carries the same procedural weight as administration by a commissioner is a question this project does not answer; it records the distinction and stops.

**Third parties in the room are never covered by the witness's oath.** In both DOC-7 and DOC-8, statements are attributed to CIA officials other than the witness — Moseman, Muller, Bonk, Rousseau/Russo — and to Commission staff. These are unsworn, and are labelled by speaker, never folded into "the witness said". DOC-8 makes the point unusually clearly at printed p.11, where the staff insert a bracketed note that a CIA official's recollection of a meeting is offered although "**Bonk was not present at the September 4th meeting**".

## 5. Changes made by this audit

| Location | Before | After |
|---|---|---|
| [`claims.md`](claims.md) A1–A7 container headings | "(Scheuer, sworn)" | "(Scheuer, DOC-3 — oath recorded in document, not image-verified)" |
| [`claims.md`](claims.md) A3.1 change note | "a second sworn witness" | "a second witness under oath (DOC-7, image-verified), independent of Scheuer" |
| [`claims.md`](claims.md) §5 preamble | "Witness under oath" | Retained — DOC-7's oath is image-verified |
| [`provenance.md`](provenance.md) PR-001, PR-002, PR-004 | "Scheuer, sworn" | "Scheuer, DOC-3, oath not image-verified" |
| [`provenance.md`](provenance.md) PR-006 | "sworn eyewitness recollection" | "recollection by a witness under oath" — retained, with the derivation flag that is the actual point of that row |
| [`version-history.md`](version-history.md) VL-001, VL-002 | "Scheuer (sworn)" / "Tenet (sworn)" | "Scheuer (DOC-3, oath not image-verified)" / "Tenet (DOC-7, oath image-verified)" |
| [`discrepancies.md`](discrepancies.md) DISC-001, DISC-003 | "sworn" | Per the register |
| [`../docs/05`](../docs/05-phase-c-competing-narratives.md) §4 | "the sworn claims" | "the claims made under oath in DOC-3 (not image-verified)" |

**Not changed:** the Portuguese Phase A documents. `docs/02` and `docs/03` use `sob juramento` throughout, and that wording is part of the preserved record. The correction reaches readers through this register and through the English companions, which render every occurrence per §1 and footnote it. See [`../en/TRANSLATION-POLICY.md`](../en/TRANSLATION-POLICY.md) §6.

## 6. Standing requirement

Every new document card records procedural status using the §2 vocabulary, with the exact basis quoted. A card that cannot establish status records `procedural status unknown` and the document is labelled an **interview memorandum** until it can.
