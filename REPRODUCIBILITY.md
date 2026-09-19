# Reproducibility

Every machine-derived result in this repository must be reproducible from the
scripts in `tools/` and the provenance record in `corpus/manifest.jsonl`. The
corpus itself is not committed: 37 MB of raw PDFs and 48 MB of page images are
reconstructible, and their SHA-256 hashes are committed so a third party can
verify they hold the same bytes this audit read.

## Environment

- Python 3.11, virtualenv with `pypdf` and `pdfplumber`
- `tesseract-ocr` 5.3.4
- `poppler-utils` 24.02 (`pdftotext`, `pdftoppm`, `pdfinfo`)

```
python3 -m venv .venv && .venv/bin/pip install pypdf pdfplumber
apt-get install -y tesseract-ocr poppler-utils
```

## Rebuild the corpus

```
.venv/bin/python tools/harvest.py     # fetch, hash, log provenance
.venv/bin/python tools/extract.py     # text layer, OCR fallback, quality score
```

`harvest.py` never overwrites silently. A re-fetch producing a different
SHA-256 is written to the manifest as a `source_change` event: a primary
source changing under the audit is itself evidence and must be investigated
before the new version is used.

## Rebuild the citation analysis

```
.venv/bin/python tools/endnotes.py --sample 40 --seed 2001
```

## Standing rules

1. **Extraction is not reading.** A document that has been harvested and
   extracted has not been read. Only a reading under a document card, with
   decisive passages checked against the page image, supports a claim status.
2. **OCR text is never quoted without image verification** of the passage
   quoted. `corpus/pages.db` records which pages were OCR'd and their quality
   score; `image_verified` is set by a human and never by a script.
3. **No machine-derived count is published before its hand-check is scored**,
   and the disagreement rate is published alongside the count. A count whose
   precision has not been measured is not a result. See
   `docs/07-phase-a-b1-first-pass.md` §4.1 for a worked example where the
   hand-check failed and the counts were withheld.
4. **Samples for scoring are drawn with a recorded seed.** A classifier tuned
   against a sample is re-scored on a fresh seed, because tuning against the
   scoring sample measures nothing.
