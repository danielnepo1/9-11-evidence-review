# Corpus Manifest

> Governed by [`../registry/source-policy.md`](../registry/source-policy.md) §4.
> Opened 19 September 2026.

## 1. Preservation model (P1)

Source binaries are **not committed**. What is committed is, for each artifact:

- the retrieval URL and date;
- the byte size and **SHA-256 of the retrieved file**;
- the extraction tool and version;
- the **extracted text**, under `text/`, with its own SHA-256.

The hash makes re-verification exact: anyone can re-retrieve the file from its stated repository and confirm byte-identity, or detect that the published file has changed. Committing multi-megabyte scans would bloat the repository without adding auditability the hash does not already provide.

**P2 applies:** if a re-retrieval yields a different hash, **both** hashes are recorded here with their dates, and the difference is investigated before either file is used. A source is never silently replaced.

## 2. Artifacts

### DOC-7 — MFR George Tenet #2

| Field | Value |
|---|---|
| Card | [`../registry/cards/DOC-7-mfr-tenet-2.md`](../registry/cards/DOC-7-mfr-tenet-2.md) |
| Source URL | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-10-release-508.pdf |
| Retrieved | 19 September 2026, HTTP 200 |
| File | `2026-201-document-10-release-508.pdf` (not committed) |
| Bytes | 1906620 |
| SHA-256 (PDF) | `7434ad300a474e06672fc450dd2ae129e2b9b04636a01b1bf9cea7848bc38e28` |
| Pages | 24 |
| Text layer | Present (agency OCR), all 24 pages |
| Extraction tool | `pypdf` 6.19.0, `PdfReader.extract_text()` |
| Extracted text | [`text/DOC-7-mfr-tenet-2.txt`](text/DOC-7-mfr-tenet-2.txt) |
| Bytes (text) | 69528 |
| SHA-256 (text) | `fb08e708910981eb040bd2dcc51dad0bbbd49f933e9b7a995ca7f54740f64326` |
| Page images | JBIG2; extracted with `pypdf` 6.19.0 + `jbig2dec` 0.20 for image verification. Not committed |

**Fidelity warning (amended 19 Sep 2026, defect #32).** The committed text is the **agency OCR as extracted, plus page delimiters inserted by this project's extraction script** — it is therefore *not* raw extraction output, and the earlier description of it as "as extracted, unedited" was inaccurate. The OCR itself is preserved verbatim, corruption included, because correcting it would destroy the record of what the release actually contains. It is a search and location aid. **It is not a transcription**: it silently omits redaction voids (see the card, §3), and its character-level accuracy is unreliable near redactions and in headers. Every decisive quotation must be taken from the page image, not from this file.

| Figure | Value |
|---|---|
| Extracted page text (sum of `extract_text()`) | 68,572 characters |
| Committed artifact | 69,066 characters / 69,528 bytes |
| Inserted `=== PDF PAGE n ===` delimiters | 24 |

### DOC-8 — MFR George Tenet #3

| Field | Value |
|---|---|
| Card | [`../registry/cards/DOC-8-mfr-tenet-3.md`](../registry/cards/DOC-8-mfr-tenet-3.md) |
| Source URL | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-11-release-508.pdf |
| Retrieved | 19 September 2026, HTTP 200 |
| File | `2026-201-document-11-release-508.pdf` (**not committed** — see §3) |
| Bytes | 1406317 |
| SHA-256 (PDF) | `f8b42694b3a7ea3fd149bd8047cb11ffdb6e9734d47e2a24bf9feb3dfbfeeb2e` |
| Pages | 13 |
| Text layer | Present (agency OCR), all 13 pages |
| Extraction tool | `pypdf` 6.19.0, `PdfReader.extract_text()` |
| Extracted text | [`text/DOC-8-mfr-tenet-3.txt`](text/DOC-8-mfr-tenet-3.txt) |
| Bytes (text) | 44252 |
| SHA-256 (text) | `18a44ecbbd1c586ca6ebd0ba447a9ac3a6a2a9e273be58ea5b518b37c3dff9a8` |
| Page images | JBIG2; rendered with `pypdf` 6.19.0 + `jbig2dec` 0.20 for independent inspection of pp. 1, 3, 5, 8, 9, 10, 11. **Not committed** — see §3 |

**Fidelity warning (amended 19 Sep 2026, defect #32).** As with DOC-7, the committed text is the **agency OCR as extracted, plus project-inserted page delimiters** — not raw extraction output. Independent inspection of the page images corrected it in at least five places, including a date (text layer "On March lilt" vs. page image "On March 12th"). It is a search and location aid, **not a transcription**. Every decisive quotation is taken from the page image.

| Figure | Value |
|---|---|
| Extracted page text (sum of `extract_text()`) | 43,781 characters |
| Committed artifact | 44,044 characters / 44,252 bytes |
| Inserted `=== PDF PAGE n ===` delimiters | 13 |

## 3. Publication status of source files, and why binaries are not committed

Every artifact in §2 is a **United States federal government record**, declassified by the Interagency Security Classification Appeals Panel under E.O. 13526 sec. 5.3(b)(3) with a declassification date of 8 September 2026, and published by the National Archives and Records Administration at the `archives.gov` URL recorded for it. That publication status is documented on the face of each document (the ISCAP declassification stamp, reproduced in each card's §1) and by the NARA URL from which it was retrieved.

Notwithstanding that status, **this repository commits no source PDF and no page image.** The reasons are recorded so the choice is auditable rather than assumed:

1. **Preservation is served by the hash.** The SHA-256 of the retrieved file permits exact re-verification against the publishing repository, and detects any change to the published file. Committing the bytes adds no auditability the hash does not already provide.
2. **Redistribution is not this project's function.** The artifacts are one HTTP request from their official source. The project's contribution is the analysis, the provenance chain and the verification record — not a mirror.
3. **Page images are derived artifacts of this project's tooling**, not published records in the form extracted, and their publication status as reproduced is therefore less clean than that of the PDFs.

What **is** committed is the extracted text: a derived, reproducible artifact whose generation is fully specified above (tool, version, method), and which any reader can regenerate from the hashed source and compare byte for byte.

**Standing rule.** No source PDF, page image or other binary is committed unless its publication status is explicitly documented **and** a reason to commit it is recorded here. Neither condition is met by convenience.

## 4. Hash-change events

None recorded.
