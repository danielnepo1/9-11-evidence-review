# 12 — EIT-Timing Cross-Reference for the 54 CIA-DETENTION Notes

> **Framing disclosure (`08` §4).** Directed-search project. This cross-reference measures a provenance-timing fact — whether each chapter-5 endnote's cited interrogation date falls before, during, or after the SSCI-documented use of coercive technique against the named detainee — for the 54 notes `11` found resting on CIA detention-program reporting. Pre-registered before any SSCI-2014 date was read, in [`prereg/B2-ch5-EIT-timing.md`](prereg/B2-ch5-EIT-timing.md); denominator is the closed 54-note list already fixed in [`11-b2-ch5-census.md`](11-b2-ch5-census.md).

Session date: **21 September 2026.** Pre-registration: commit `43ce377`. Source: `SSCI-2014` (`corpus/manifest.jsonl`; SHA-256 `4989f2fb14509322…`), ABBYY-OCR'd, D-003 applies.

---

## 1. Scope

**Denominator: the 54 notes `11` classified `CIA-DETENTION` (B2-rely=yes)** — not the 84-note B7 set, not chapter 5 as a whole. Every citation date in every one of the 54 notes was extracted (160 individual date-citations across the 54 notes; several notes cite more than one date, sometimes for more than one detainee) and classified against the six detainees' SSCI-documented timelines.

## 2. The six detainee timelines, sourced and image-verified

Every capture/rendition date and every EIT-application boundary below is a direct quotation from `SSCI-2014`, checked against the rendered page image (D-003 — the PDF producer is `ABBYY FineReader 10`).

| Detainee | Capture / custody transfer | EIT window (start → documented end) | Source (PDF p. / printed p.) |
|---|---|---|---|
| **KSM** | March 1, 2003 | March 1, 2003 → ≈ March 25–26, 2003 (derived: "24 days after" cessation relative to April 19, 2003; "more than three months after cessation" relative to June 27, 2003) | p. 283 / printed p. 254, image-verified |
| **Abu Zubaydah** | March 28, 2002 | DOJ approval Aug. 1, 2002; applied Aug. 4–20, 2002; ceased Aug. 30, 2002 ("when Abu Zubaydah received clothing") | p. 260 / printed p. 231 (main text) and footnote 1316, p. 231, independently identical wording; both image-verified |
| **Khallad / Tawfiq bin Attash** | Arrested by Pakistan Apr. 29, 2003; rendered "On May [redacted], 2003" | Two documented windows: **May 16–18, 2003** and **July 18–29, 2003** | p. 428 / printed p. 399, image-verified |
| **Hambali** | "In August 2003, Hambali was captured and transferred to CIA custody" (exact day redacted) | EITs approved "approximately a month after his transfer" (≥ mid-Sept. 2003); documented in EIT-context questioning through **Nov. 30, 2003** (cables 1142, 1144); **no cessation date stated by SSCI** | p. 137 / printed p. 108, image-verified; corroborated (not image-verified, not relied on) at pp. 279, 285, 422, 511, 631 |
| **Nashiri** | Captured "in the United Arab Emirates in mid-October 2002"; rendered to DETENTION SITE COBALT ≈ Nov. 2002 | Four documented periods: Dec. 5–8, 2002; Dec. 27, 2002–Jan. 1, 2003; Jan. 9–10, 2003; **Jan. 15–27, 2003** (final documented use) | pp. 95–96 / printed pp. 66–67, image-verified. Independently cross-checked: an October 2004 passage states an assessment occurred "21 months after the final documented use" of EITs against him — Oct. 2004 − 21 months = Jan. 2003, consistent |
| **Ramzi bin al-Shibh** | Captured Sept. 11, 2002 (Pakistani raid); "immediately subjected to the CIA's enhanced interrogation techniques" upon CIA custody | Continued EIT use documented through a Feb. 13, 2003 cable and "approximately three additional weeks" thereafter, with cables dated Feb. 20 and **Feb. 24, 2003** as the latest documented instances; estimated actual cessation ≈ early March 2003 | p. 108 / printed p. 79, image-verified |

**Six of six named detainees were subjected to EITs per SSCI's own accounting** — none of the 54 notes' named subjects falls under `NEVER-SUBJECTED`. The 6 notes citing an unnamed "detainee" or a joint "KSM and Binalshibh" citation cannot be matched to an individual timeline and classify `INCONCLUSIVE` by construction, per `prereg/B2-ch5-EIT-timing.md` §3.

## 3. A vocabulary gap found during classification (`decisions.md` D-009)

The pre-registered four-way status (DURING-EIT / POST-EIT / NEVER-SUBJECTED / INCONCLUSIVE) did not anticipate a **gap between capture and first documented EIT use** — present for Hambali (captured August 2003; EITs approved "approximately a month after"). A citation dated in that gap is classified **PRE-EIT** (added and justified in `decisions.md` D-009, not folded into an existing category). Separately, SSCI states no cessation date for Hambali; citations after the latest documented EIT-context cable (Nov. 30, 2003) are labeled **INCONCLUSIVE (no stated cessation)** rather than POST-EIT, so as not to assert a cessation fact the source does not state. Both additions apply to Hambali citations only (8 of 160) and are reported as their own rows below, not merged into either favourable or unfavourable existing totals.

## 4. Verification

Nine decisive SSCI-2014 pages were image-verified (§2 table): every quotation used to fix a timeline boundary matches the rendered page exactly. No discrepancy was found. The 54 notes' own citation text (detainee name, cited date) was re-extracted from `CR-2004`'s validated endnote segmentation (`tools/endnotes.py`); `CR-2004` is born-digital (D-003 exemption, confirmed in `11` §2). The extraction was checked against `11`'s own reported totals (54 notes, exact note-ID list) as an internal consistency check — it reproduced the 54-note set exactly, confirming the two independent extraction passes agree on the denominator.

## 5. Result

**Date-citation level (160 citations across 54 notes — several notes cite more than one date):**

| Status | Count | Share |
|---|---|---|
| **POST-EIT** | 128 | 80.0% |
| **DURING-EIT** | 18 | 11.2% |
| PRE-EIT | 6 | 3.8% |
| INCONCLUSIVE (unnamed subject) | 5 | 3.1% |
| INCONCLUSIVE (Hambali, no stated cessation) | 2 | 1.3% |
| ANOMALY-PRE-CAPTURE | 1 | 0.6% |

**Note level (54 notes, one classification per note by its full set of cited dates):**

| Classification | Count | Share of 54 |
|---|---|---|
| **All cited dates POST-EIT** | 36 | 66.7% |
| **Mixed — cites both a DURING-EIT and a POST-EIT date** | 12 | 22.2% |
| **All cited dates DURING-EIT** | 4 | 7.4% |
| Hambali-specific edge case (no firm DURING/POST citation) | 2 | 3.7% |

The 4 pure-DURING-EIT notes are: note 30 (Nashiri, Jan. 27, 2003 — the last day of his last documented EIT period) and notes 65, 67, 68 (bin al-Shibh, Sept.–Oct. 2002, within weeks of his capture and immediate subjection to EITs).

The 12 mixed notes are 43, 53, 54, 56, 58, 60, 89, 91, 92, 93, 98, 106 — each cites at least one date inside a detainee's EIT window and at least one date after it, reflecting the report's practice of stacking multiple interrogation-report citations, spanning months or years, behind a single sentence.

## 6. The anomaly found in the course of this cross-reference

Chapter 5 note 20 cites "Intelligence reports, interrogations of Hambali, Jan. 14, 2003; Mar. 5, 2004" — but Hambali was not captured until August 2003, seven months after the first date. This is registered as **A-002** (anomaly register) and **X-004** (contradiction ledger), with the full mirror test. **Summary of the assessment reached there:** the note's second citation ("Mar. 5, 2004") and every other Hambali-attributed citation in the 84-note B7 set cluster at Sept. 2003 or later, making "Jan. 14, 2003" the sole outlier and a well-fitting date if read as "Jan. 14, 2004." The claim the note supports — pre-2001 organizational history — does not depend on which year is correct. Assessed as `apparent anomaly with adequate explanation` (single-digit transcription error), escalation level 1, not elevated, per the full test in `A-002`.

## 7. Findings that challenge or weaken the official account

- **80.0% of individual interrogation-date citations, and two-thirds of the 54 notes outright, cite a date after SSCI's own documented cessation of coercive technique against the named subject.** For KSM and Khallad specifically, this is close to total: of 91 KSM citations, 89 are POST-EIT (only 2, both Mar. 24, 2003, are DURING); of 33 Khallad citations, 29 are POST-EIT and 4 DURING. **The pre-registered expectation (`prereg` §6) — that a material share of KSM citations would classify DURING or near cessation, and later 2004 citations would classify POST — is confirmed, but more starkly than expected: post-cessation citations are not merely present but overwhelming**, and DURING-EIT citations for KSM are two dates out of ninety-one.
- **For bin al-Shibh, the reverse pattern holds**: 11 of 18 citations (61%) are DURING-EIT, reflecting his shorter, front-loaded EIT window immediately after a September 2002 capture. This is reported with equal prominence, per the pre-registration's own instruction (§6) that a result contrary to expectation "is reported with equal weight."
- **A verified, well-documented internal chronological error** (§6, A-002/X-004) exists in the Commission's own endnote apparatus — found only by the kind of cross-source, date-level scrutiny this project's methodology requires, and not previously flagged in any source consulted.

## 8. Findings that challenge or weaken alternative accounts

- **All six named detainees were, per SSCI's own account, subjected to EITs at some point** — there is no case in this 54-note set of a detainee's reporting being used who SSCI documents as never coerced. A claim that this chapter's sourcing quietly relies on uncoerced testimony to launder a coerced narrative is not supported: coercion, per SSCI, was in fact used against every one of the six.
- **The dominant pattern — post-cessation citation — is not itself evidence that the underlying statements are false or fabricated.** SSCI documents that some post-EIT statements (e.g., Hambali's November 2003 admissions, later recanted) were themselves products of psychological pressure from the custodial relationship, not evidence-free assertions; but SSCI also documents extensive post-cessation cooperation assessed as credible. A blanket claim that "post-EIT" implies "unreliable" would overreach the source in the opposite direction from underclaiming, and this census does not make it.
- **Nashiri's single pure-DURING-EIT citation (note 30, Jan. 27, 2003) falls on the exact last day of his last documented EIT period** — a boundary case, not a citation deep inside a coercive episode. Treating it as equivalent in strength to, e.g., bin al-Shibh's within-days-of-capture citations would overstate the DURING-EIT finding's uniformity.

## 9. What remains unresolved

- **Whether the 128 POST-EIT citations reflect information genuinely re-derived after cessation, or reporting whose content originated during the EIT period and was merely re-elicited or re-confirmed later** — this cross-reference measures the date stamped on the cited report, not the provenance of the information within it. SSCI itself documents this exact concern for some subjects (e.g., Hambali's cable describing "gradual ramp-up... and the use of the enhanced measures" preceding a disclosure): the report's date and the information's origin are not always the same fact, and this census cannot separate them from the citations alone.
- **Hambali's true EIT-cessation date** — SSCI states none; the 9 Hambali citations in this set (6 PRE-EIT, 2 INCONCLUSIVE-no-cessation, 1 the ANOMALY-PRE-CAPTURE date already registered as A-002) cannot be fully resolved without it.
- **The raw cable underlying note 20's "Jan. 14, 2003" citation** — not sought in this project; would settle A-002/X-004 definitively.
- **Whether other chapters' CIA-DETENTION notes show the same POST-EIT concentration** — untested; this cross-reference covers only chapter 5.

## 10. What evidence would change the assessment

- **The unredacted SSCI report (or its Volume III detainee reviews)** would supply exact capture days (several are redacted to the month here) and, for Hambali, a stated cessation date — narrowing or eliminating the PRE-EIT/INCONCLUSIVE categories.
- **The raw CIA reporting cables underlying each of the 160 citations** would show whether a POST-EIT report's content was newly elicited or re-confirmed from an earlier, DURING-EIT-period statement — the single most consequential gap identified in §9.
- **Locating the specific cable behind note 20** would resolve A-002/X-004 from "well-supported ordinary explanation" to a settled fact.

## 11. What this does not permit us to conclude

Per the pre-registered ceiling (`prereg/B2-ch5-EIT-timing.md` §5), verbatim: **a `DURING-EIT` classification shows that the cited interrogation report's date falls within the window SSCI documents that detainee as having been subjected to coercive technique. It does not show that the specific statement cited in the Commission Report's note is false, unreliable, or was itself obtained coercively.** A `POST-EIT` classification shows the opposite timing fact and carries the same non-inference — **it does not certify the statement's truth either**, and it does not mean the statement is more reliable merely because the technique's formal application window had closed; the subject remained in the same custodial program. No classification here resolves whether any specific claim used in `CR-2004` chapter 5 is true. The count is a fact about the report's own evidentiary architecture — when, relative to documented coercion, the cited reporting was dated — not a verdict on the report's contents.

## 12. Reproducibility

Denominator: the 54-note list from `11-b2-ch5-census.md` §3 (re-derived independently from `CR-2004`'s validated endnote segmentation and confirmed to match exactly). Detainee timelines: `SSCI-2014` (`corpus/manifest.jsonl`, SHA-256 `4989f2fb14509322…`), quotations image-verified against pages listed in §2. Classification script and intermediate data are session-local (not committed, consistent with existing practice for `note_dates.py`-class intermediate dumps); the per-note classification table is reproducible from the quoted windows in §2 applied to the citation dates listed in `11`'s underlying note text.
