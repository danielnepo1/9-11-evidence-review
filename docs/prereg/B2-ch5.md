# Pre-registration — B2, Chapter 5: detainee/interrogation-derived support census

> **Written before any of the 84 chapter-5 retrospective-only notes was classified.** The 84-note set itself was fixed by [`09-b7-retrospective-support-census.md`](../09-b7-retrospective-support-census.md) (validated at 5.0% disagreement) before this document existed, so the denominator was not chosen after seeing which notes would classify favourably. Full, untruncated note text was re-extracted from the validated segmentation (`tools/endnotes.py`) because `corpus/analysis/endnotes.jsonl` truncates at 1,200 characters and two of the 84 notes exceed that.

Pre-registered: **21 September 2026.** Governed by `04` §2.2 (three dates), `05` §3.2 (source genealogy), `decisions.md` D-002 (two non-summed columns).

---

## 1. Scope

Denominator: **the 84 chapter-5 notes** classified `retrospective-only` (earliest cited document date ≥ 2002) by the validated B7 run (seed 20260922, 5.0% disagreement). This is a closed, pre-fixed list — [`../../corpus/analysis/b2_ch5_notes.json`](../../corpus/analysis/b2_ch5_notes.json), written before classification and hashed below.

**What this census is not.** It is not a census of chapter 5, and not of the report. Chapter 5 has 132 notes; 42 are contemporaneous-capable and 3 no-date, both left aside. It measures the retrospective slice only, because that is the slice B7 flagged as resting on post-event evidence, and B2's job is to say what kind of post-event evidence.

## 2. The two columns — fixed, never summed (D-002)

| Column | Definition |
|---|---|
| **B2-ref** | The note mentions or cites interrogation- or detention-derived reporting |
| **B2-rely** | An atomic proposition in the note's own text **rests on** such reporting as its cited source (not merely mentions the subject) |

## 3. Source subtype — fixed vocabulary, one subtype per B2-rely=yes note (the dominant one if mixed, with the mix recorded)

| Subtype | Definition | Example already on file |
|---|---|---|
| **CIA-DETENTION** | "Intelligence report, interrogation of [name]" — the CIA detention-and-interrogation programme | `CR-2004` note 42 (Khallad), already carded |
| **COOPERATING-WITNESS** | A convicted or cooperating defendant's statements to US law enforcement (FBI 302s, trial testimony) — NOT the CIA programme | `PDB-20010806` P5 (Ressam), already carded — different document, same subtype |
| **FOREIGN-LIAISON** | A foreign government's custodial interrogation or briefing of a detained person, relayed to the US | Not yet seen |
| **LATER-ANALYTIC** | A later CIA/FBI analytic product (e.g. "The Plot and the Plotters") that itself synthesises detainee reporting, cited without naming the underlying interrogation | Distinguished from CIA-DETENTION because the citation does not point at an interrogation report directly — recorded separately so the two are never conflated into one count |
| **OTHER-RETROSPECTIVE** | Retrospective but not detainee-derived at all: a 2003–04 Commission interview of a US official, a later court filing, a later press account | The majority class is expected here |

**Mixed notes** (citing more than one subtype) are tagged with all subtypes present; the summary counts each subtype's presence, so subtype counts may sum to more than the number of B2-rely=yes notes. This is disclosed, not hidden.

## 4. Verification standard

- **Every B2-rely=yes classification is hand-read in full** (not the 1,200-character truncation) before being recorded.
- **Text-layer reliability is stratified, not assumed uniform** (`decisions.md` D-003): `CR-2004`'s PDF producer is `Acrobat Distiller 6.0.1 for Macintosh` from `Preps 4.2.1` — a prepress workflow that produces **born-digital text**, not agency OCR. `corpus/pages.db` scores 571/585 of its pages `good` by the text-layer route with only 1 page OCR'd (not in chapter 5's note pages, 506–518). On this basis, full-text reading from the extracted layer is treated as equivalent to image verification for this document, **except** that a fixed random sample of positives is image-checked as a calibration spot-check, at the rate below.
- **Spot-check rate:** at least 5 of the B2-rely=yes notes, or 20% of them (whichever is larger), rendered and checked against the page image. Any mismatch found voids the exemption in the bullet above for the rest of the set and forces full image verification.
- Every positive (B2-rely=yes) carries the exact note number, PDF page(s), and the quoted citation fragment that supports the classification.

## 5. Conclusion ceiling — fixed before classification

> A note classified B2-rely=yes under subtype CIA-DETENTION or FOREIGN-LIAISON shows that **this specific proposition** in chapter 5 is sourced to a detainee's statement under interrogation. It does not show the proposition is false, coerced, or unreliable — interrogation-derived intelligence can be accurate — and it is not evidence for any alternative hypothesis. It is a fact about **evidentiary provenance**, to be weighed by the reader against the known limitations of that provenance (documented separately in the SSCI report, not re-litigated here). The count is a **denominator inside a denominator**: chapter 5 retrospective-only notes (84) are already a subset of chapter 5 notes (132), themselves a subset of the report; nothing here characterises the report as a whole.

## 6. Expectation, stated in advance

Given chapter 5's subject (al Qaeda's internal planning, recruitment and operative selection — matters to which only participants had access), **CIA-DETENTION is expected to be the largest single subtype**, plausibly a majority of B2-rely=yes notes. **If OTHER-RETROSPECTIVE is instead the largest subtype, that is reported with equal prominence** — it would mean the chapter's post-event reliance is broader than detainee reporting specifically, which changes what follow-up (e.g. an SSCI cross-reference) is worth doing next.
