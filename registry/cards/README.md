# Document Cards

> Governed by [`../../docs/04-controlling-methodology.md`](../../docs/04-controlling-methodology.md) §7.

One card per document read. A card records what the document **is** — identification, the four dates, participants, source layer, redaction profile, decisive quotations with their verification state, and the gaps the document declares about itself. A card does not draw conclusions; conclusions live in [`../claims.md`](../claims.md).

---

## 1. Card index

| ID | Document | Date | Read | Card | Image-verified |
|---|---|---|---|---|---|
| DOC-1 | *Report on Review of PDB Articles* (PDB Review Team) | 9 Feb 2004 | in full | [`../../docs/02` §1.1](../../docs/02-adversarial-audit-phase1.md) — inline, pre-card format | **no** |
| DOC-2 | MFR — Condoleezza Rice | 7 Feb 2004 | in full | [`../../docs/02` §1.1](../../docs/02-adversarial-audit-phase1.md) — inline | **no** |
| DOC-3 | MFR — Mike Scheuer #1 | 11 Dec 2003 | in full | [`../../docs/02` §1.1](../../docs/02-adversarial-audit-phase1.md) — inline | **no** |
| DOC-4 | PIDB blog post, NARA | 11 Sep 2026 | in full (short) | [`../../docs/02` §1.2](../../docs/02-adversarial-audit-phase1.md) — inline | n/a |
| DOC-5 | ISCAP 2026-201 index page | — | index only | [`../../docs/02` §1.2](../../docs/02-adversarial-audit-phase1.md) — inline | n/a |
| DOC-6 | CIA page, 71 declassified PDBs | 11 Sep 2026 | index only; PDFs unreadable | [`../../docs/02` §1.2](../../docs/02-adversarial-audit-phase1.md) — inline | n/a |
| **DOC-7** | **MFR — George Tenet #2** | **22 Jan 2004** | **in full, 24/24 pp.** | [`DOC-7-mfr-tenet-2.md`](DOC-7-mfr-tenet-2.md) | **partial — pp. 3, 4, 5, 12, 19 (21%)** |
| **DOC-8** | **MFR — George Tenet #3** | **28 Jan 2004** | **in full, 13/13 pp.** | [`DOC-8-mfr-tenet-3.md`](DOC-8-mfr-tenet-3.md) | **partial — pp. 1, 2, 3, 5, 8, 9, 10, 11, 12 (69%)** |
| **DOC-9** | **MFR — luncheon meeting with DCI Tenet** | **23 Dec 2003** | **in full, 3/3 pp.** | [`DOC-9-mfr-tenet-luncheon.md`](DOC-9-mfr-tenet-luncheon.md) | **full — 3/3 (100%)** |

## 2. Cards not yet written — documents not yet read

DOC-10 … DOC-15 are reserved for the six remaining MFRs of the ISCAP 2026-201 release. The reading order was revised by what DOC-8 produced, and is revised again by what DOC-9 produced:

| Next | Document | Why |
|---|---|---|
| **DOC-10** | **MFR Berger, 14 Jan 2004** | Required by **two independent rows**: A3.2 and U-09 ([DISC-010](../discrepancies.md#disc-010)). It is also the discriminator named by DISC-002, the highest-priority remaining row in [`../anomalies.md`](../anomalies.md). Scheduled as step 5 of [`../../docs/06-audit-program-v2.md`](../../docs/06-audit-program-v2.md) |
| DOC-11–13 | Clarke ×3 | Priorities 1, 2, 6 |
| DOC-14–15 | Scheuer #2 and #3 | Internal consistency of DOC-3's witness |

**Before any of them:** the re-carding gate at §3 below. It requires no retrieval, has been deferred twice, and blocks nine rows. It is step 4 of the audit program and is dated there.

### 2.1 What the DOC-9 reading changed about reading order

DOC-9 was read out of size order and out of subject order, because the anomaly register said it was the only reachable document that tested the two **P0** rows. Both are now spent — [DISC-008](../discrepancies.md#disc-008) resolved, [DISC-007](../discrepancies.md#disc-007)'s EC1 excluded — and **no row in the project sits at P0 any more**.

The register's recommendation therefore moves to the P1 group, where MFR Berger is the discriminator for two rows at once. That is not a dramatic result and it is the correct one: the highest-value read was a three-page lunch memo that told the project how much its own silences are worth.

---

## 3. Re-carding requirement — a blocking gate

**DOC-1, DOC-2 and DOC-3 were read in Phase A before the image-verification standard existed.** Their metadata was recorded inline in [`../../docs/02` §1.1](../../docs/02-adversarial-audit-phase1.md) in a pre-card format, and DOC-1's own record states that its OCR is poor and that sense was "reconstructed by context".

Under [`../../docs/04` §7.3](../../docs/04-controlling-methodology.md) these three **must be re-carded** against page images, in this format, before the following may be closed:

- **A10.1, A10.2** — Rice on the 6 Aug 2001 PDB
- **A16.1** — the bolded non-corroboration caveat
- **A8.2, A9.1, A15.1–A15.4** — every row whose evidence is a quotation from DOC-1, DOC-2 or DOC-3
- any conclusion depending on the above

**The Phase A records are not altered by re-carding.** A new card is added; the inline Phase A record stands as written, and the version-history ledger records the relationship. That is the preservation rule, not a formality: if a re-carding changes a reading, the change must be visible as a change.

### 3.1 Why this is not a paperwork exercise

DOC-7's p.4 carries a redaction block covering roughly 60% of the page that is **entirely invisible in the extracted text layer**. Three documents were read in Phase A by the same method, one of them with acknowledged bad OCR. There is no reason to assume they contain no comparable void, and no way to find out except by looking at the images.

The DOC-8 reading added a second kind of evidence for the same requirement. Independent inspection of 7 of its 13 page images corrected the extracted text in at least five places, one of them a date: the text layer reads "On March lilt" where the page reads **"On March 12th"**. A chronology assembled from the text layer alone would have carried a fabricated date.

The 19 September 2026 verification of DOC-8 p.2 added a third and worse kind. The page image showed that a passage the registry carried under one speaker is **split between two on the page**, the second being a redacted speaker, and that the whole passage was given *in response to an adverse finding put to the witness's side* rather than volunteered. Neither fact is recoverable from the text layer. A **speaker attribution** and the **pragmatic status of a statement** are not marginal details: they are what decides whether a row is corroboration or rebuttal, and who can be asked about it. See [`../claims.md`](../claims.md) §5A.0.
