# Consolidated Bibliography

All sources accessed across the phases of the audit, consolidated by provenance. Access date: **17 September 2026**, unless otherwise noted.

Read-status legend: 🟢 read in full · 🟡 read in part / index or FAQ only · 🔴 verified by summary/abstract only · ⚫ access failed

> **Access-failure record — 19 September 2026.** In an attempt to execute Phases 2A and 2B, **every** primary-source domain in this file was blocked by the environment's network egress policy (403 on CONNECT, both via HTTP client and via fetch tool): `archives.gov` and subdomains, `intelligence.senate.gov`, `cia.gov`, `govinfo.gov`, `vault.fbi.gov`, `9-11commission.gov`, `govinfo.library.unt.edu`, `nist.gov`. The block is not selective — no external host tested responded. The only available channel was search, which returns third-party snippets and does **not** count as reading under this project's standard. No source had its status changed in that session. Details in [`docs/03` §3](docs/03-phase2a-mfr-verification.md).

> **Session of 19 September 2026 (methodology update).** No source was read and no read status was changed. That session produced only methodology and registers — see [`docs/04`](docs/04-methodology-symmetric-skepticism.md).

> **Access re-check — 19 September 2026 (planning session). The blockade recorded above is largely lifted.** `www.archives.gov`, `www.cia.gov`, `www.intelligence.senate.gov`, `www.nist.gov` and `oig.justice.gov` all responded `200`; ranged requests against the ISCAP MFR PDFs and the 6 August 2001 PDB returned `206 application/pdf`, confirming retrievability. `vault.fbi.gov` still returns `403` and appears to be refused site-side rather than by egress policy. **No status in the tables below was changed by this re-check**: retrievability is not reading, and the 6 August 2001 PDB's missing text layer is a separate obstacle that retrieval does not solve. Targets and order of reading: [`docs/05`](docs/05-stress-test-execution-plan.md) §1 and §6.

> **Capability verification — 19 September 2026. Not a reading.** The OCR obstacle recorded since `docs/02` (DOC-6) is solved. `tesseract` 5.3.4, poppler 24.02 and `pypdf`/`pdfplumber` are installed and working. Pipeline test on `08-06-2001-Bin-Ladin-Determined-To-Strike-in-US.pdf` (SHA-256 `dc7e2d7a281726b2262ee7ff3b2c4144cf80a1e5167f330147243a5dd39070af`, 763,998 bytes): embedded text layer contains **2 characters** in the whole file, confirming the original diagnosis; page 1 rasterised and OCR'd cleanly at **2,419 characters**. **No claim, status or register entry derives from this test.** The document is read properly, under a document card and with decisive passages checked against the page image, in Phase C2 of [`docs/06`](docs/06-research-program.md). Its status below therefore remains ⚫ until that reading happens.

---

## Document card — required for every source read from here on

Recorded before any claim is drawn from the source. Governed by [`docs/04`](docs/04-methodology-symmetric-skepticism.md) and [`docs/05`](docs/05-stress-test-execution-plan.md).

```
### [Document ID] — [Exact title]

- Institution / author:
- Event date:
- Creation date:
- Declassification / publication date:
- Document type and oath status:
- URL and retrieval date:
- File hash:
- Extent actually read (pages):
- OCR quality / image verification of decisive passages:
- Redactions, missing attachments, exhibits or errata:
- Provenance limitations (original record or later representation; prepared for whom, under what authority):
- Claims tested:
- Evidentiary ceiling:
```

Stop condition: if a decisive passage's OCR cannot be checked against the page image, that passage is not quotable and no status may rest on it.

---

## NIST — WTC structural engineering

| Source | Status | URL |
|---|---|---|
| Final Reports from the NIST WTC Disaster Investigation (index) | 🟡 | https://www.nist.gov/el/final-reports-nist-world-trade-center-disaster-investigation |
| World Trade Center Investigation (institutional page) | 🟡 | https://www.nist.gov/world-trade-center-investigation |
| FAQs — NIST WTC Towers Investigation | 🟡 | https://www.nist.gov/world-trade-center-investigation/study-faqs/wtc-towers-investigation |
| FAQs — NIST WTC 7 Investigation | 🟡 | https://www.nist.gov/world-trade-center-investigation/study-faqs/wtc-7-investigation |
| NCSTAR 1, 1-2, 1-3, 1-5, 1-6, 1A, 1-9, 1-9A (full primary reports) | 🔴 not accessed | linked from the index above |

## 9/11 Commission

| Source | Status | URL |
|---|---|---|
| Official site archive (govinfo.library.unt.edu mirror) | 🟡 (index only — no structural content) | https://www.9-11commission.gov/report/ |
| Full report (911Report.pdf) | 🔴 not accessed | https://www.9-11commission.gov/report/911Report.pdf |

## Peer-reviewed academic literature — engineering

| Source | Status | URL/DOI |
|---|---|---|
| Bažant, Z. P. & Verdure, M. (2007), "Mechanics of Progressive Collapse", J. Eng. Mech. 133(3):308 | 🔴 abstract | https://doi.org/10.1061/(asce)0733-9399(2007)133:3(308) |
| Bažant, Z. P. & Le, J.-L. (2008), Closure, J. Eng. Mech. 134(10):917 | 🔴 abstract | https://ascelibrary.org/doi/10.1061/(ASCE)0733-9399(2008)134:10(917) |
| Bažant, Z. P., Le, J.-L., Greening, F. R., Benson, D. B. (2008), "What Did and Did Not Cause Collapse", J. Eng. Mech. 134(10):892 | 🔴 abstract | https://ascelibrary.org/doi/10.1061/(ASCE)0733-9399(2008)134:10(892) |

## University of Alaska Fairbanks / technical dissent

| Source | Status | URL |
|---|---|---|
| UAF WTC 7 Study — project page | 🟡 summary | https://ine.uaf.edu/wtc7 |
| AE911Truth — WTC 7 study page | 🟡 summary | https://www.ae911truth.org/wtc7 |
| PRNewswire — final report release (25 March 2020) | 🟡 | https://www.prnewswire.com/news-releases/university-report-on-911-building-collapse-contradicts-official-conclusions-301029854.html |
| Hulsey/UAF report in full | 🔴 not accessed | via ine.uaf.edu/wtc7 |

## NARA / ISCAP — September 2026 declassification

| Source | Status | URL |
|---|---|---|
| PIDB, "Long-Sought 9/11 Records Now Declassified" (11 September 2026) | 🟢 | https://transforming-classification.blogs.archives.gov/2026/09/11/long-sought-9-11-records-now-declassified-and-available-to-the-public/ |
| *Report on Review of PDB Articles* (9 February 2004, declassified 8 September 2026) | 🟢 | https://www.archives.gov/files/declassification/iscap/pdf/2022-008-document-release-508.pdf |
| ISCAP 2026-201 index (11 MFRs) | 🟡 (2 of 11 read) | https://www.archives.gov/declassification/iscap/pdf/2026-201 |
| MFR — Condoleezza Rice (7 February 2004) | 🟢 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-5-release-508.pdf |
| MFR — Mike Scheuer #1 (11 December 2003, under oath) | 🟢 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-6-release-508.pdf |
| MFR — Sandy Berger (14 January 2004) | ⚫ Stress-Test Track target; access blocked 19 September 2026 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-1-release-508.pdf |
| MFR — Richard A. Clarke #1 (18 December 2003) | ⚫ Stress-Test Track target; access blocked 19 September 2026 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-2-release-508.pdf |
| MFR — Richard A. Clarke #2 (12 January 2004) | ⚫ Stress-Test Track target; access blocked 19 September 2026 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-3-release-508.pdf |
| MFR — Richard A. Clarke #3 (3 February 2004) | ⚫ Stress-Test Track target; access blocked 19 September 2026 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-4-release-508.pdf |
| MFR — Michael Scheuer #2 (6 January 2004) | ⚫ Stress-Test Track target; access blocked 19 September 2026 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-7-release-508.pdf |
| MFR — Michael Scheuer #3 (11 March 2004) | ⚫ Stress-Test Track target; access blocked 19 September 2026 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-8-release-508.pdf |
| MFR — George Tenet #1 (23 December 2003) | ⚫ Stress-Test Track target; access blocked 19 September 2026 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-9-release-508.pdf |
| MFR — George Tenet #2 (22 January 2004) | ⚫ Stress-Test Track target; access blocked 19 September 2026 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-10-release-508.pdf |
| MFR — George Tenet #3 (28 January 2004) | ⚫ Stress-Test Track target; access blocked 19 September 2026 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-11-release-508.pdf |
| Bush/Cheney interview (redacted, released 2022 — not part of the 2026 tranche) | 🔴 not read | https://www.archives.gov/files/declassification/iscap/pdf/2012-163-doc-1-release-material.pdf |

## CIA — 71 declassified PDBs

| Source | Status | URL |
|---|---|---|
| Index page for the 71 PDBs (11 September 2026) | 🟡 full index read | https://www.cia.gov/stories/story/cia-releases-presidents-daily-briefs-in-commemoration-of-the-25th-anniversary-of-9-11/seventy-one-declassified-presidents-daily-brief-products/ |
| Individual PDB "Bin Ladin Determined To Strike in US" (6 August 2001) | ⚫ PDF without text layer | https://www.cia.gov/static/08-06-2001-Bin-Ladin-Determined-To-Strike-in-US.pdf |
| The other 70 individual PDBs | ⚫ not tested / presumably the same OCR problem | see index above |
| Complete collection (101 pp., 36.6 MB) | ⚫ not accessed | https://www.cia.gov/static/71-PDB-9_11-Related-Collection.pdf |

## MFRs outside the ISCAP 2026-201 release — needed to close Phase 2A claims

None located. All are needed for priorities 1, 2 and 6 in [`docs/03` §4](docs/03-phase2a-mfr-verification.md); the search should begin with NARA's general Commission MFR holdings, not with the 2026 release.

| Source | Status | Claim it would test |
|---|---|---|
| MFR — Janet Reno | 🔴 not located | A3 (30% vs 0%) |
| MFR — Louis Freeh | 🔴 not located | A3 |
| MFR — Mary Jo White | 🔴 not located | A3 — the alleged recipient of the "0%" |
| MFR — Patrick Fitzgerald | 🔴 not located | A3 — the alleged source of the account given to Scheuer |
| Situation Room logs and Presidential Diary, 11 September 2001 | 🔴 not located | A12 (timing of Rice's call to the President) |
| Scheuer memorandum of 28 June 1999 | 🔴 not located | A1 (absence of an NIE / analytic product) |
| Internal memorandum on the 25 March 1999 PDB | 🔴 not located | A2 — the real test of the withholding claim |
| Scheuer memo of 3 May 1996 and Spot Report of 24 June 1997 | 🔴 not located | A4 (Saudi non-cooperation) |

## Repositories listed in the original scope — not accessed in this phase

- National Archives — 9/11 Commission Records, FAA Finding Aid, NORAD/NEADS materials
- Joint Congressional Inquiry (2002) and Part Four (the "28 pages") — ⚫ Phase 2B target; access blocked 19 September 2026
  https://www.intelligence.senate.gov/2016/07/15/publications-declassified-version-part-four-joint-inquiry-intelligence-community-activities-and/
- FBI Vault — material released under Executive Order 14040
  https://vault.fbi.gov/9-11-attacks-investigation-and-related-materials/9-11-material-released-in-response-to-executive-order-14040
- 9/11 Review Commission Report (2015)
  https://www.fbi.gov/file-repository/reports-and-publications/final-9-11-review-commission-report-unclassified.pdf/view
- United States v. Zacarias Moussaoui — trial exhibits
  https://www.vaed.uscourts.gov/101cr00455-trial-exhibits
- In re Terrorist Attacks on September 11, 2001 — docket
  https://www.courtlistener.com/docket/4328332/in-re-terrorist-attacks-on-september-11-2001/
- SSCI Report on the CIA Detention and Interrogation Program (CRPT-113srpt288)
  https://www.govinfo.gov/app/details/CRPT-113srpt288/CRPT-113srpt288
- FEMA 403 (World Trade Center Building Performance Study), including Appendix C
