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

**Fidelity warning.** The committed text is the **agency OCR as extracted**, unedited. It is preserved verbatim, corruption included, because correcting it would destroy the record of what the release actually contains. It is a search and location aid. **It is not a transcription**: it silently omits redaction voids (see the card, §3), and its character-level accuracy is unreliable near redactions and in headers. Every decisive quotation must be taken from the page image, not from this file.

## 3. Hash-change events

None recorded.
