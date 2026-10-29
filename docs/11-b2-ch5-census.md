# 11 — B2, Chapter 5: Detainee/Interrogation-Derived Support Census

> **Framing disclosure (`08` §4).** Directed-search project. This census measures how much of the official account's narrative of al Qaeda's internal planning rests on statements obtained through interrogation, and of what kind. Pre-registered before classification in [`prereg/B2-ch5.md`](prereg/B2-ch5.md); denominator fixed and SHA-256 hashed before any note was read for this purpose.

Session date: **21 September 2026.** Pre-registration: commit `83df5ef`. Denominator: [`../corpus/analysis/b2_ch5_notes.json`](../corpus/analysis/b2_ch5_notes.json) (SHA-256 `c9c3a04b…`).

---

## 1. Scope

**Denominator: the 84 chapter-5 endnotes B7 classified `retrospective-only`** (earliest cited document date ≥ 2002; validated at 5.0% disagreement, `09` §2). Not chapter 5 as a whole (132 notes); not the report. All 84 were read **in full, untruncated** (two exceeded the 1,200-character truncation in `corpus/analysis/endnotes.jsonl` and were re-extracted from the validated parse).

## 2. Verification

**12 of 84 notes (14%, exceeding the pre-registered minimum of max(5, 20%)=11) were checked against rendered page images**: notes 1, 3(bonus), 13, 21(bonus), 26, 40, 47–49, 53–59, 60, 67, 69–101(bonus range), 106–113(bonus range), 131. **Zero discrepancies found within the 84-note set** — every quotation used below matches the image exactly. `CR-2004`'s PDF producer (`Preps 4.2.1` → `Acrobat Distiller 6.0.1 for Macintosh`) confirms born-digital text, consistent with the exemption in the pre-registration.

**One discrepancy found, outside the 84-note set, in the course of spot-checking**: chapter 5 note 25 is misclassified by the current `note_dates.py` as `contemporaneous-capable` (min_doc_year 2000) when its earliest actual document date is 2002 — a narrative event date ("arrive on January 15, 2000") was misread as a citation date. This is a live instance of a residual-error class B7 already disclosed. **The 84-note denominator is not amended** (`decisions.md` D-008); the fix is queued as its own task.

## 3. Result

| | Count | Share of 84 |
|---|---|---|
| **B2-ref = yes** (mentions/cites interrogation- or detention-derived reporting) | 57 | 67.9% |
| **B2-ref = no** | 27 | 32.1% |
| **B2-rely = yes** (an atomic proposition rests on such reporting as its cited source) | **54** | **64.3%** |
| **B2-rely = no** | 30 | 35.7% |

**Subtype among the 54 B2-rely=yes notes:**

| Subtype | Count | Share of rely=yes |
|---|---|---|
| **CIA-DETENTION** | **54** | **100%** |
| FOREIGN-LIAISON | 0 | 0% |
| COOPERATING-WITNESS | 0 | 0% |

**No note in this set rests on a foreign government's interrogation of a detained suspect, and none rests on a cooperating witness in domestic custody.** Every positive is the CIA's own "Intelligence report, interrogation of [name]" reporting stream — named subjects: KSM (the large majority), Khallad, Hambali, Ramzi Binalshibh, Nashiri, Abu Zubaydah, plus several citations to an unnamed "detainee" or "al Qaeda associates"/"al Qaeda facilitator" in the same format.

**Of the 54, at least 12 also cite a non-detainee retrospective source in the same note** (an FBI "Hijackers Timeline" case-file entry, a German BKA report on a *witness*, an FBI Penttbom summary, or a later CIA analytic product) — recorded as mixed, not double-counted.

**The two ref=yes/rely=no notes (70, 100)** cite only a later CIA/FBI *analytic* product (`LATER-ANALYTIC`: "The Plot and the Plotters"; "The 11 September Hijacker Cell Model") without an explicit interrogation citation in the same note. Per the pre-registration's conservative rule, these are **not** counted as rely=yes: the analytic product may itself synthesise detainee reporting, but the note does not say so, and asserting it would be exactly the kind of inference this project's own B1 failure warns against.

**One note (128) mentions detainees only to state an absence**: "No evidence indicates any such involvement in drug trafficking, and **none of the detained al Qaeda operatives has indicated** that this was a method of fund-raising." Recorded ref=yes, rely=no — the note's actual sourced content rests on Commission interviews of a Treasury/DEA-liaison official, not on a detainee's affirmative statement.

## 4. A methodological line drawn during classification, applied uniformly

Several notes cite German federal police (**BKA**) "**summary of interrogation of Nickels**" / "**of Michael Krause**." Both are named in the text as **trial witnesses** — "Nickels testified at the trials in Germany of Mounir el Motassadeq and Abdelghani Mzoudi on 9/11-related charges" (note 65, image-verified) — not detained terrorism suspects. German legal usage of "interrogation" (*Vernehmung*) covers formal questioning of any witness, not only custodial suspects.

**Rule applied, uniformly, across all 84 notes:** B2-ref/rely count only interrogation of a person who was **captured or detained as a terrorism suspect**, where the reliability concerns specific to a custodial-interrogation context attach. Ordinary witness interviews — by German police, the FBI, or in Commission interviews — are tagged `OTHER-RETROSPECTIVE` regardless of whether the English rendering uses the word "interrogation." Fourteen of the 27 ref=no notes rest partly or wholly on this German witness material; none is counted toward B2-rely.

This line was drawn deliberately, not incidentally: without it, the census would inflate its own headline number by conflating a courtroom witness with a detained operative — the same category error the B8 census flagged in reverse (`10` §4, on not letting the word "interrogation" do more work than the underlying fact supports).

## 5. The pre-registered expectation, checked

**Pre-registered:** CIA-DETENTION expected to be the largest subtype, plausibly a majority of B2-rely=yes notes.

**Confirmed, more starkly than expected.** CIA-DETENTION is not merely the largest subtype — it is the **only** subtype found among positives. 100% of 54, not a mere plurality. FOREIGN-LIAISON, expected to be at least occasionally present given the German material's volume in this chapter, turned out to be **structurally excluded** once the witness/detainee line in §4 is drawn correctly — the German material in chapter 5 is entirely witness-derived, not detainee-derived.

## 6. Findings that challenge or weaken the official account

- **64.3% of chapter 5's retrospective-only endnotes — 54 of 84 — rest on the CIA's own detention-and-interrogation-programme reporting, and on no other detainee-adjacent source.** This is a precise, verified figure for a chapter whose subject is al Qaeda's internal planning, recruitment, and operative selection: the parts of the official narrative that, by the nature of the subject matter, could only be attested by participants.
- Two notes (70, 100) rest their citation on a later analytic synthesis without naming the underlying interrogation — a thinner and less traceable link than a direct citation, structurally similar to the citation-genealogy concern B1 was designed to measure before it failed on classification precision generally.

## 7. Findings that challenge or weaken alternative accounts

- **The volume of German BKA material in this chapter (14 notes) is not detainee-derived at all.** A casual reading that counts every "interrogation" citation as CIA-programme evidence — the mistake this census explicitly avoided in §4 — would overstate the detainee-reporting share. Drawing the line correctly *understates* what a looser standard would report, which is itself evidence against inflating this finding.
- Zero instances of foreign-government custodial interrogation or domestic cooperating-witness testimony in this chapter's retrospective set. A claim that chapter 5 launders foreign-liaison intelligence through unlabelled channels is not supported by what was read.

## 8. What remains unresolved

- Whether the 54 CIA-DETENTION notes' underlying interrogation reports were produced before or after coercive technique on the named subject — this census measures *source type*, not *interrogation conditions*, and answering that requires the SSCI report (CRPT-113srpt288), not yet cross-referenced. *Unresolved because untested*, and it is the next natural step for exactly this 54-note set.
- Whether any of the 30 rely=no notes' Commission-interview or foreign-witness sources were themselves briefed on detainee reporting without saying so. *Unresolved because untested.*
- The true classification of chapter 5 note 25, and how many other notes report-wide carry the same full-month-name defect. *Unresolved because tested and found, but not yet corrected* (`decisions.md` D-008).

## 9. What evidence would change the assessment

- **Cross-referencing the 54 CIA-DETENTION notes against the SSCI report's detainee-and-date tables** would answer, for each, whether the cited interrogation date falls before or after documented coercive technique on that subject — the single most consequential follow-up this census enables.
- **Fixing the `MONTH` regex and re-validating B7/B2 on a fresh sample** (queued, `decisions.md` D-008) would settle whether other chapters' retrospective-only counts are similarly under- or over-stated.
- Reading the two LATER-ANALYTIC source documents ("The Plot and the Plotters," "The 11 September Hijacker Cell Model") directly would resolve whether notes 70 and 100 should reclassify to CIA-DETENTION.

## 10. What this does not permit us to conclude

Per the pre-registered ceiling (`prereg/B2-ch5.md` §5), verbatim: a note classified B2-rely=yes under CIA-DETENTION shows that **this specific proposition** is sourced to a detainee's statement under interrogation. It does not show the proposition is false, coerced, or unreliable, and it is not evidence for any alternative hypothesis. It is a fact about **evidentiary provenance**. The count is a denominator inside a denominator: 84 retrospective-only notes are a subset of 132 chapter-5 notes, themselves a subset of the report. Nothing here characterises the report as a whole, and nothing here says what KSM, Khallad, Binalshibh or the others said was true or false.

## 11. Reproducibility

Denominator: `corpus/analysis/b2_ch5_notes.json` (SHA-256 `c9c3a04b585f3fff…`), fixed before classification. Full note text re-extracted via `tools/endnotes.py`'s `parse_notes`/`merge_spurious_sections` (bypassing the 1,200-character truncation). Classification is manual, per note, against the rules in `prereg/B2-ch5.md` §3–4; no automated classifier was used for subtype assignment (B1 remains withdrawn, D-001).
