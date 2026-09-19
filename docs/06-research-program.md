# 06 — Research Program: From Reading Documents to Auditing the Record

> **Strategy document and capability verification.** No substantive claim is drawn here and no status changes. It proposes a change in *method of attack*, verifies that the method is executable in this environment, and ranks the lines of inquiry by expected yield.

Governed by [`04-methodology-symmetric-skepticism.md`](04-methodology-symmetric-skepticism.md). Targeting from [`05-stress-test-execution-plan.md`](05-stress-test-execution-plan.md) is retained in full and is absorbed into Phase C below.

Session date: **19 September 2026**.

---

## 1. Audit of our own strategy

Before proposing more work, the honest finding about the work so far.

**The project has been reading artisanally.** Three documents read in full across three sessions. The relevant record — Commission report and its staff monographs, the Joint Inquiry, the NCSTAR volumes, the DOJ IG reports, the SSCI report, the ISCAP releases, the PDB tranche, the Moussaoui exhibits, the EO 14040 releases — is on the order of **10⁵ pages**. At the current rate the audit finishes some time after everyone involved is dead.

Worse, artisanal reading has a systematic bias that the methodology in `04` cannot correct: **you find anomalies where you look, and you look where others have already pointed.** Every target in `05` is, to some degree, a place the existing literature has already lit up. A project that only re-examines famous controversies will produce a better-argued version of the existing debate and nothing new.

**The correction is instrumental, not moral.** Stop hunting anomalies one at a time. Build something that can interrogate the whole corpus at once, and ask it structural questions that nobody has asked because asking them by hand is impossible.

The structural question with the highest yield is not "where is the record contradictory?" It is:

> **Which claims in the official account are load-bearing, and how deep is the evidence under each one?**

That is answerable, systematically and reproducibly, because the 9/11 Commission Report cites its sources in roughly 1,700 endnotes. The citation structure is machine-readable. Nobody in this project has parsed it.

---

## 2. Capability verification (executed this session)

A plan that assumes unavailable tooling is worthless, so the pipeline was tested before being proposed.

| Capability | Result |
|---|---|
| Network to primary repositories | `archives.gov`, `cia.gov`, `intelligence.senate.gov`, `nist.gov`, `oig.justice.gov`, `govinfo.gov`, `archive.org`, `vaed.uscourts.gov` all reachable. `vault.fbi.gov` 403; `courtlistener.com` 403 |
| Large primary documents retrievable | 9/11 Commission Report (govinfo + UNT mirror), SSCI CRPT-113srpt288, DOJ IG report: all return `206 application/pdf` on ranged request |
| PDF text extraction | `pdftotext`, `pdfimages` (poppler 24.02), `pypdf` 6.19, `pdfplumber` — installed and working in `/tmp/v911` venv |
| **OCR** | **`tesseract` 5.3.4 installed and working** |

### 2.1 The OCR blocker is solved

The 6 August 2001 PDB has been recorded as unreadable since `02` (DOC-6) — "PDF without a text layer" — and that single obstacle has blocked claims A10 and A16 and targets T-1.1 and T-1.2 across three sessions.

Capability test, run this session:

| Item | Value |
|---|---|
| File | `https://www.cia.gov/static/08-06-2001-Bin-Ladin-Determined-To-Strike-in-US.pdf` |
| SHA-256 | `dc7e2d7a281726b2262ee7ff3b2c4144cf80a1e5167f330147243a5dd39070af` |
| Size | 763,998 bytes |
| Embedded text layer | **2 characters total** — confirms the original diagnosis |
| Page 1 rasterised + OCR | **2,419 characters, clean, headings and body recovered** |

**This was a pipeline test, not a reading.** No claim, status or register entry derives from it. The document will be read properly under a document card, with decisive passages checked against the page image, in Phase C2. What the test establishes is that the obstacle was tooling, not the record — and that the same pipeline unlocks the other 70 PDBs, which were never even tested.

---

## 3. Program structure

Five phases. A and B are instrument-building and machine-assisted structural audit; C is the human-judgment deep dives (absorbing all of `05`); D is the adversarial infrastructure that keeps us honest; E is synthesis.

A and B are new. They are also, in my assessment, where this project's only chance of an original contribution lies.

---

## Phase A — Instrumentation

Goal: a hash-verified, OCR'd, full-text-searchable local corpus with a provenance record for every page, reproducible by anyone from scripts in this repository.

| ID | Task | Output |
|---|---|---|
| **A1** | **Harvest script.** Fetch every target from `SOURCES.md` plus the Phase C additions. Record URL, retrieval timestamp, HTTP status, byte size, SHA-256, content type. Never overwrite: a re-fetch that produces a different hash is itself an event and is logged | `corpus/manifest.jsonl`, `tools/harvest.py` |
| **A2** | **Extraction pipeline.** Per document: try embedded text; measure characters-per-page; below threshold, rasterise and OCR; store page images for every OCR'd page so decisive passages remain verifiable against the image | `corpus/text/`, `corpus/images/`, per-page quality score |
| **A3** | **Provenance database.** One row per page: document ID, page number, extraction method, OCR confidence, whether a human has verified it. Every later quotation resolves to a page row | `corpus/pages.db` (SQLite) |
| **A4** | **Reproducibility record.** Scripts committed, manifest committed, corpus itself not committed (size) but reconstructible by running the scripts. A third party must be able to reproduce every quotation we use | `REPRODUCIBILITY.md` |

**Discipline:** OCR text is never quoted as evidence without image verification of the decisive passage. The quality score decides what needs checking; it does not excuse skipping it. `04` §2.4 is unchanged — machine extraction is not a licence to treat unverified text as read.

**Estimated effort:** one working session for A1–A3 on the first ~20 documents; extensible thereafter.

---

## Phase B — Structural audits

This is the original work. Each item asks a question that cannot be asked by hand.

### B1 — Citation genealogy graph *(flagship)*

**The idea.** The 9/11 Commission Report supports its narrative with roughly 1,700 endnotes. Parse them. Build a graph: **narrative claim → endnote → cited source → (where the source is itself in the corpus) its own support**. Classify every cited source by type:

`contemporaneous document` · `MFR / Commission interview` · `detainee interrogation report` · `agency briefing to the Commission` · `public testimony` · `press account` · `the Commission's own analysis` · `unrecoverable / not publicly available`

**Then compute, for every claim:**

- **evidentiary depth** — how many links before the chain terminates;
- **terminal source type** — what kind of thing the chain bottoms out in;
- **source count and independence** — how many genuinely distinct sources, applying `05` §3.2 (accounts sharing an ancestor are one account);
- **recoverability** — can a reader obtain the cited source at all?

**The output nobody has produced:** a ranked list of the official account's load-bearing claims by how thin the evidence under them is, computed rather than argued.

**Why this is the best idea in the program:** it is systematic (no cherry-picking), reproducible (anyone can re-run it), symmetric (it measures evidentiary structure, not truth), and genuinely novel. And it inverts the usual failure mode: instead of us choosing which claims to attack, the citation structure tells us which claims *are* structurally weak, including ones nobody has ever discussed.

**Conclusion ceiling, fixed now:** a shallow or single-sourced citation chain establishes **"this claim rests on a thin evidentiary base."** It does not establish the claim is false, and it is not evidence for any alternative. A thin chain is an invitation to go find the underlying source, not a verdict. Under `04` S5, "we could not verify it" is a limitation.

### B2 — Detainee-derived claim census

**The idea.** A large part of the plot narrative — origins, financing, operative selection, target choice — traces to interrogation reports of a handful of detainees. The Commission had no access to the detainees or the interrogators and said so. The SSCI report (CRPT-113srpt288) documents the interrogation programme, including dates and techniques.

**The audit:** from the B1 graph, extract every claim whose terminal source is a detainee report. For each, record the report's date and cross-reference the SSCI record for what preceded it. Then compute:

1. what share of the plot narrative rests solely on detainee reporting;
2. of that, what share post-dates coercive technique on that detainee;
3. which claims have independent documentary corroboration in the corpus and which do not.

**This is high-value precisely because it is uncomfortable in both directions.** If the share is small and corroboration is broad, that substantially strengthens H0 and weakens a standard line of attack on it. If the share is large and uncorroborated, it shows a central narrative resting on evidence of a type that courts exclude — **and still establishes nothing about what actually happened.** Either result is publishable and neither is a verdict.

**Symmetric obligation:** run the identical census over the alternative literature. Critics routinely cite the same detainee reporting when it suits. That gets measured too.

### B3 — Version-diff engine

Official accounts that were revised are the cleanest evidence available, because both versions are public and the change is a fact rather than an interpretation. Automate it:

| Pair | What a diff exposes |
|---|---|
| NIST WTC 7 draft (Aug 2008) vs final (Nov 2008) | A quantitative revision to a collapse-phase claim, made after external comment |
| NORAD chronology (Sep 2001) vs Commission reconstruction (2004) | The largest documented revision of an official timeline |
| Commission staff statements vs the final report | What survived internal review and what did not |
| NCSTAR drafts vs finals generally | Scenario selection and assumption changes |
| Agency public statements over time on the same proposition | Quantifier drift (`05` §3.1) at scale |

**Method:** align by section, diff at sentence level, filter to changes that alter a quantity, a hedge, an actor or a time. Rank by materiality. Every survivor gets a `revision` entry in the contradiction ledger with the prompting event recorded where it can be established.

### B4 — Quantifier-drift scanner

Corpus-wide, automated. Find every proposition that appears in more than one document and detect the mutations catalogued in `05` §3.1 — dropped qualifiers, widened scope, hardened certainty, changed actor, changed time range. Run **in both directions**: official summaries of official documents, and critics' summaries of the same documents. The symmetric result is the interesting one.

### B5 — Missing-record census (negative space)

Instead of asking "what does the record contain?", ask **"what records should exist?"**

Method: from stated procedures, retention schedules and statutory duties, enumerate the records that a given event *ought* to have generated — a cable log, a watchlist entry, a notification receipt, a scramble order, a disposition record, a custody form. For each, determine: does it exist, was it requested, was it released, is it withheld, was it destroyed, or was it never created?

Then apply `05` §3.4 to every absence, strictly. This converts scattered "why is there no record of X?" anecdotes into a **census with a denominator** — which is the only form in which an absence argument can be honest, in either direction.

### B6 — Timeline database with uncertainty intervals

Every timed event as a row: event time, zone, precision, clock source, whether machine-generated or reconstructed, observation time, record-creation time, later-recollection time. Then let the machine find what humans miss and, more importantly, **stop the false positives**: an ordering is only impossible once the uncertainty intervals fail to overlap. Most published FAA/NORAD "impossibilities" are, on my expectation, interval-overlap failures in the analysis rather than in the record. Proving that would be a real contribution and would weaken a lot of alternative-account argumentation.

---

## Phase C — Targeted deep dives

All of `05`'s ST-1…ST-7 targeting is retained and runs here, now informed by B1's ranking rather than by prior fame. Plus five lines `05` does not cover:

| ID | New line | Why it is worth opening |
|---|---|---|
| **C-N1** | **Able Danger** | A documented conflict between an officer's sworn account and an institutional denial, with a DoD IG review and congressional record. Clean test case for the institutional-process audit, and it has a definite answer |
| **C-N2** | **Moussaoui trial exhibits** | Adversarial-tested evidence — admitted in a criminal proceeding with defence challenge. Includes FAA/NORAD materials and flight data. **Evidence that has survived cross-examination is a different epistemic category from everything else in this corpus**, and the project has ignored it entirely. Reachable now |
| **C-N3** | **Foreign-service archives** | German (Hamburg cell — BKA/BfV, Bundestag inquiry), Spanish (Garzón investigations), Italian (Milan wiretaps), Philippine (Bojinka). Parts of the US account rest on foreign reporting. **These are the only genuinely institutionally independent sources in the whole record** — they do not share the US interagency ancestor that makes so much US corroboration circular (`05` §3.2). Language handling per the project rule: quote verbatim, translate in a labelled working translation, never silently |
| **C-N4** | **Financial/SEC trading claims** | The pre-attack trading allegation has a specific published resolution with a traceable chain. Test the chain rather than the allegation. A symmetric target: it is an alternative-account staple |
| **C-N5** | **Replication attempt (ST-7)** | For the structural track, stop arguing about models and build a reduced-order sensitivity model from published parameters. Not to "solve" the collapse — to answer one question: **are the published conclusions sensitive to the assumptions that were withheld?** If yes, the §7d withholding becomes materially important; if no, it stops being important and a lot of argument dies. Applies identically to NIST and to Hulsey/UAF |

---

## Phase D — Adversarial infrastructure

Instruments that attack *us*.

| ID | Mechanism |
|---|---|
| **D1** | **Standing H0 steelman.** Every phase closes with an explicit attempt to argue the official account's side of each finding, written as advocacy, before the finding is recorded. A finding that survives its own steelman is worth something; one that does not gets downgraded in the same session |
| **D2** | **Pre-registration is mandatory.** Every question, and what would count as positive, negative and inconclusive, is written down **before** the document is opened. Already project practice (`03` §4); now enforced by the targeting audit in `anomaly-register.md` §6 |
| **D3** | **Register balance monitoring.** Entry counts by side, reported every phase. A one-sided register triggers an investigation of our reading, not a conclusion about the world |
| **D4** | **Long-lead access requests.** MDR to NARA for the Commission materials still classified; FOIA to DOJ/FBI/DoD IG for the underlying reports. These take months to years, so **file early even though they resolve late.** Track in a request register with dates |
| **D5** | **Kill criteria.** Each targeting hypothesis carries the observation that would retire it. A T-item that survives three sessions without a discriminating test gets closed as `low` discriminating power rather than lingering as permanent innuendo |

---

## Phase E — Synthesis

Hypothesis tournament, run only where the hypotheses' predictions genuinely diverge — H0 can coexist with H1 and H4, H1 does not imply H5, H6 does not imply H7, H2 does not imply H3. Forcing compatible hypotheses into a winner-take-all comparison is itself an error.

Final report carries the four mandatory sections of `04` §6, plus the B1 depth ranking, the B2 census, the B5 census with its denominator, and a reproducibility record.

---

## 4. Expected yield — my honest ranking

Stated in advance so it can be checked against what actually happens.

| Rank | Line | Probability of a defensible original finding | What it would actually show |
|---|---|---|---|
| 1 | **B1 citation genealogy** | High | Which official claims rest on thin or non-independent evidence. A structural result, not a verdict |
| 2 | **B2 detainee-derived census** | High | The evidentiary base of the plot narrative, quantified. Cuts both ways and is valuable either way |
| 3 | **B3 version diffs** | High | Documented revisions, including ones nobody has catalogued. Cheap and hard to dispute |
| 4 | **B5 missing-record census** | Medium-high | Absence arguments with a denominator, for the first time in this project |
| 5 | **C-N2 Moussaoui exhibits / C-N3 foreign archives** | Medium-high | The only adversarially-tested and the only institutionally-independent evidence in the corpus |
| 6 | **B6 timeline intervals** | Medium | Probably kills more alternative-account claims than official ones. That is a finding |
| 7 | **C1 al-Mihdhar node** | Medium | Heavily worked by others; our contribution is atomisation and naming individuals, not discovery |
| 8 | **C6 / ST-7 structural** | Low by reading, medium with C-N5 replication | Document reading alone will not settle this. Sensitivity analysis might make the withheld-inputs question decidable |

**What I expect the program to conclude, stated now so it cannot be retrofitted:** that parts of the official account — particularly the plot-history narrative — rest on a narrower and less independent evidentiary base than their confident presentation implies; that most famous "anomalies" resolve as scope mismatches, clock artefacts or ordinary bureaucratic failure; that some do not; and that **none of this, by itself, supports any alternative hypothesis**, because a weak official chain is an absence of proof, not proof of something else.

If the work instead produces positive evidence for H1–H7, it will be recorded with the same discipline. But an audit that begins by expecting to find that is not an audit.

---

## 5. Risks to this program

| Risk | Control |
|---|---|
| Machine methods produce quantified nonsense that looks authoritative | Every computed result carries its extraction method and error rate; nothing is quoted without image verification of the decisive passage |
| The graph's source classification encodes our own bias | Classification rules written and committed **before** parsing; a sample is hand-checked and the disagreement rate is published |
| Corpus-scale work becomes an end in itself | Phase A is time-boxed to what Phase B needs; instrument-building that is not feeding an audit question gets cut |
| OCR errors become "contradictions" | No contradiction is entered from OCR text alone, ever |
| We find a thin citation chain and inflate it | The B1 conclusion ceiling is fixed in §3 above, before any result exists |
| The program's scale becomes an excuse for never concluding | Each phase closes with the four mandatory sections, whatever state the corpus is in |

---

## 6. What to do now — the next session, concretely

1. **A1 + A2 on a 12-document seed corpus:** the nine unread ISCAP MFRs, the 6 Aug 2001 PDB, the full 9/11 Commission Report, the Joint Inquiry. Harvest with hashes, extract, OCR where needed, score quality. Commit the scripts and the manifest.
2. **Document cards** for all twelve, per the `SOURCES.md` schema. This is the evidence boundary and it comes before any claim.
3. **B1 parser, first pass:** extract the Commission Report's endnotes, classify cited source types, produce the first depth ranking. Even a rough first pass reorders every priority in `05`.
4. **C2 / T-1.1 and T-1.2:** the 6 Aug 2001 PDB read properly — OCR text against page images, then against DOC-1's characterisation and the primary transcript of the public characterisation. This closes A10/A16 in one direction or the other after three sessions of being stuck.
5. **File the D4 requests.** They will not resolve for months; that is the reason to file them in session four rather than session forty.

Phase closes with the four mandatory sections of `04` §6, the register health checks, and a reproducibility record.

---

## 7. Standing caution

This program is designed to find out what the record can and cannot support. It is not designed to find a particular thing, and the phrase "what we are looking for" has no referent in it. The most likely outcome of rigorous work here is a map of evidentiary quality — strong in places, thin in others — rather than a discovery. A map of that kind is worth building, and it is the only output this method can honestly produce.
