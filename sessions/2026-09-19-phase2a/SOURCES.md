# Consolidated Bibliography

All sources accessed throughout the audit's phases, consolidated by provenance. Access date: **September 17, 2026**, unless otherwise noted.

Reading-status legend: 🟢 read in full · 🟡 read partially / index or FAQ only · 🔴 verified only by summary/abstract · ⚫ access failed

> **Access-failure record — September 19, 2026 (session 1).** In an attempt to execute Phases 2A and 2B, **all** primary-source domains in this file were blocked by the environment's network egress policy (403 on CONNECT, both via the HTTP client and via the fetch tool): `archives.gov` and subdomains, `intelligence.senate.gov`, `cia.gov`, `govinfo.gov`, `vault.fbi.gov`, `9-11commission.gov`, `govinfo.library.unt.edu`, `nist.gov`. The block was not selective — no external host tested responded. The only available channel was search, which returns third-party excerpts and **does not** count as reading under this project's standard. No source had its status changed in this session. Details in [`docs/03` §3](docs/03-phase2a-mfr-verification.md).

> **Access reopened — September 19, 2026 (session 2).** A new connectivity test (`curl` directly, without the fetch tool) showed HTTP 200 on `archives.gov`, `cia.gov`, `nist.gov`, `intelligence.senate.gov`, `govinfo.gov`, `9-11commission.gov`, and `govinfo.library.unt.edu`. The 9 MFRs from the ISCAP 2026-201 release pending since session 1, plus the 06/08/2001 PDB, were downloaded and verified as intact PDFs (not block pages). The 9 MFRs were read in full in this session (text extracted with `pdftotext`, 11 to 82 thousand characters each) and the 06/08/2001 PDB — previously unreadable due to the absence of a text layer — was read via OCR (`tesseract`, 300 DPI). Results tabulated in [`docs/03` §5](docs/03-phase2a-mfr-verification.md#5-claim-by-claim-verification-instrument).

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
| PRNewswire — final-report release (25/03/2020) | 🟡 | https://www.prnewswire.com/news-releases/university-report-on-911-building-collapse-contradicts-official-conclusions-301029854.html |
| Full Hulsey/UAF report | 🔴 not accessed | via ine.uaf.edu/wtc7 |

## NARA / ISCAP — September 2026 declassification

| Source | Status | URL |
|---|---|---|
| PIDB, "Long-Sought 9/11 Records Now Declassified" (11/09/2026) | 🟢 | https://transforming-classification.blogs.archives.gov/2026/09/11/long-sought-9-11-records-now-declassified-and-available-to-the-public/ |
| *Report on Review of PDB Articles* (09/02/2004, declass. 08/09/2026) | 🟢 | https://www.archives.gov/files/declassification/iscap/pdf/2022-008-document-release-508.pdf |
| ISCAP 2026-201 index (11 MFRs) | 🟢 (11 of 11 read on 19/09/2026, session 2) | https://www.archives.gov/declassification/iscap/pdf/2026-201 |
| MFR — Condoleezza Rice (07/02/2004) | 🟢 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-5-release-508.pdf |
| MFR — Mike Scheuer #1 (11/12/2003, under oath) | 🟢 | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-6-release-508.pdf |
| MFR — Sandy Berger (14/01/2004) | 🟢 read in full on 19/09/2026 (session 2) | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-1-release-508.pdf |
| MFR — Richard A. Clarke #1 (18/12/2003) | 🟢 read in full on 19/09/2026 (session 2) | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-2-release-508.pdf |
| MFR — Richard A. Clarke #2 (12/01/2004) | 🟢 read in full on 19/09/2026 (session 2) | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-3-release-508.pdf |
| MFR — Richard A. Clarke #3 (03/02/2004) | 🟢 read in full on 19/09/2026 (session 2) | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-4-release-508.pdf |
| MFR — Michael Scheuer #2 (06/01/2004) | 🟢 read in full on 19/09/2026 (session 2) | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-7-release-508.pdf |
| MFR — Michael Scheuer #3 (11/03/2004) | 🟢 read in full on 19/09/2026 (session 2) | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-8-release-508.pdf |
| MFR — George Tenet #1 (23/12/2003) | 🟢 read in full on 19/09/2026 (session 2) | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-9-release-508.pdf |
| MFR — George Tenet #2 (22/01/2004) | 🟢 read in full on 19/09/2026 (session 2) | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-10-release-508.pdf |
| MFR — George Tenet #3 (28/01/2004) | 🟢 read in full on 19/09/2026 (session 2) | https://www.archives.gov/files/declassification/iscap/pdf/2026-201-document-11-release-508.pdf |
| Bush/Cheney interview (redacted, released 2022 — not part of the 2026 release) | 🔴 not read | https://www.archives.gov/files/declassification/iscap/pdf/2012-163-doc-1-release-material.pdf |

## CIA — 71 declassified PDBs

| Source | Status | URL |
|---|---|---|
| Index page for the 71 PDBs (11/09/2026) | 🟡 full index read | https://www.cia.gov/stories/story/cia-releases-presidents-daily-briefs-in-commemoration-of-the-25th-anniversary-of-9-11/seventy-one-declassified-presidents-daily-brief-products/ |
| Individual PDB "Bin Ladin Determined To Strike in US" (06/08/2001) | 🟢 read in full on 19/09/2026 (session 2), via OCR — PDF has no native text layer; extracted with `pdftoppm` (300 DPI) + `tesseract` | https://www.cia.gov/static/08-06-2001-Bin-Ladin-Determined-To-Strike-in-US.pdf |
| Remaining 70 individual PDBs | ⚫ not tested / presumably the same OCR issue | see index above |
| Full collection (101 pp., 36.6 MB) | ⚫ not accessed | https://www.cia.gov/static/71-PDB-9_11-Related-Collection.pdf |

## MFRs outside the ISCAP 2026-201 release — needed to close Phase 2A claims

None located. All needed for priorities 1, 2, and 6 of [`docs/03` §4](docs/03-phase2a-mfr-verification.md); the search should start with the Commission's general MFR holdings at NARA, not the 2026 release.

| Source | Status | Claim it would test |
|---|---|---|
| MFR — Janet Reno | 🔴 not located | A3 (30% vs. 0%) |
| MFR — Louis Freeh | 🔴 not located | A3 |
| MFR — Mary Jo White | 🔴 not located | A3 — the alleged recipient of the "0%" |
| MFR — Patrick Fitzgerald | 🔴 not located | A3 — the alleged source of the report to Scheuer |
| Situation Room logs and President's Daily Diary for 11/09/2001 | 🔴 not located | A12 (timing of Rice's call to the President) |
| Scheuer's memorandum of 28/06/1999 | 🔴 not located | A1 (absence of an NIE/analytic product) |
| Internal memorandum on the 25/03/1999 PDB | 🔴 not located | A2 — the real test of the withholding claim |
| Scheuer's memo of 03/05/1996 and Spot Report of 24/06/1997 | 🔴 not located | A4 (Saudi non-cooperation) |

## Repositories listed in the original scope — not accessed in this phase

- National Archives — 9/11 Commission Records, FAA Finding Aid, NORAD/NEADS materials
- Joint Congressional Inquiry (2002) and Part Four ("28 pages") — ⚫ Phase 2B target; access blocked on 19/09/2026
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
