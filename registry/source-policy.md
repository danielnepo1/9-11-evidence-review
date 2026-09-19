# Source Policy — Inclusion, Provenance, Preservation, Deduplication

> Living instrument. Governed by [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) §10.
> Opened 19 September 2026. **This policy is a gate: the corpus is not expanded before it is applied.**

---

## 1. The prohibition this policy implements

> **No indiscriminate internet collection.**

A source enters the corpus because a registry row needs it, not because it exists, not because it is easy to reach, and not because a search returned it. Every admission is pull-driven: name the row first, then the document that would move it, then go get that document.

This applies symmetrically. A critical source is admitted on the same terms as an official one — and refused on the same terms.

---

## 2. Inclusion rules

A candidate is admitted only if **all** of I1–I4 hold.

| # | Rule |
|---|---|
| **I1** | **Named need.** A specific registry row is named that the source could move, before the source is retrieved |
| **I2** | **Terminal-source test.** If the candidate is secondary (book, article, documentary, essay, website, forum post), the underlying primary record is identified. The secondary source enters as a **lead**, tagged `lead`, and never as the terminal evidentiary source while a primary exists |
| **I3** | **Attribution floor.** The candidate has an identifiable author or issuing body, a date, and a retrievable location. Anonymous, undated or unlocatable material may be recorded as a lead but never cited in support of a status |
| **I4** | **Symmetry check.** The stated reason for admitting it would also justify admitting an equally-sourced item advancing the opposite conclusion |

### 2.1 Grounds for refusal

- Retrieved by open-ended search without a named row (violates I1).
- Secondary source offered where the primary is reachable (violates I2).
- Aggregator or compilation reproducing material whose origin it does not state.
- Any item whose admission is justified by the conclusion it supports.

### 2.2 Standing admitted repositories

The repositories already in scope in [`../SOURCES.md`](../SOURCES.md) are admitted for pull-driven retrieval without a fresh I1–I4 pass, because their provenance is established: NARA/ISCAP, CIA, FBI Vault, govinfo, Senate Intelligence Committee, NIST, FEMA, federal court dockets and trial exhibits. **Everything else requires the full pass.**

---

## 3. Provenance fields recorded at admission

Recorded **before** any claim is extracted from the source.

| Field | Notes |
|---|---|
| Issuing body / author | Person or institution |
| Event date · document date · **annotation date** · declassification date | Four now, not three — see [`discrepancies.md`](discrepancies.md#disc-006) |
| Custody chain | How it reached the place it was retrieved from |
| Retrieval URL and date | Exact |
| Byte size and **SHA-256** | Of the file as retrieved |
| Text-layer status | `native text` · `agency OCR` · `none (image only)` |
| Redaction profile | Extent and marking authority, **as seen on the page image** |
| Known incentives of the source | Stated plainly, for official and critical sources alike |
| Direct knowledge or hearsay | Per passage, not per document |

---

## 4. Preservation rules

| # | Rule |
|---|---|
| **P1** | Raw artifacts are preserved by **hash, not by copy**: the SHA-256 of the retrieved file is recorded in [`../corpus/manifest.md`](../corpus/manifest.md), and the extracted text is committed under `corpus/text/`. Large binaries are not committed — they are retrievable from their stated repository, and the hash makes re-verification exact |
| **P2** | A source file is **never silently overwritten**. If a re-retrieval yields a different hash, both hashes are recorded with dates, and the difference is investigated before either is used |
| **P3** | Prior methodological failures are preserved. Invalidated instruments are quarantined, not deleted — see [`instruments-b1-b2.md`](instruments-b1-b2.md) |
| **P4** | Reclassifications and corrections are recorded as **explicit dated events** in [`version-history.md`](version-history.md) §3 |
| **P5** | Extraction is reproducible: the manifest records the tool and version used to derive text from each file |

---

## 5. Deduplication rules

Deduplication here is **evidentiary**, not file-level. Two different files can be one piece of evidence.

| # | Rule |
|---|---|
| **D1** | Items sharing a provenance root are counted **once**, however many documents republish them ([`../docs/04` §3](../docs/04-controlling-methodology.md)) |
| **D2** | Before recording corroboration, the corroborating source's chain is walked to its root and compared with the claim's root. If they meet, it is not corroboration — it is republication |
| **D3** | A document quoting or paraphrasing another is recorded as `derivative` of it, never as a second witness |
| **D4** | Where a single interview, interrogation or cable underlies several documents, the **interview is the unit**, and the several documents are its instances |
| **D5** | File-level duplicates (same SHA-256, different URL) are recorded as one artifact with multiple retrieval locations |

---

## 6. Custodial-source handling

Any source deriving from detention or interrogation is additionally governed by [`instruments-b1-b2.md`](instruments-b1-b2.md): tagged `B2-ref` or `B2-rely`, with its subtype preserved. The two tags are never summed and the subtypes are never collapsed.

---

## 7. What this policy does not do

It does not rank sources by institution. An agency record and a critic's document are admitted or refused on I1–I4 alone. Weight — as distinct from admission — is set afterwards, by provenance, independence, contemporaneity, auditability and corroboration, per the governing principle in [`../docs/04` §0.1](../docs/04-controlling-methodology.md).
