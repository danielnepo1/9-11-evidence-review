# 05 — Official Account Stress-Test Track: Execution Plan

> **Planning document. No source was read in producing it and no claim status changed.** Everything below is *targeting*: where fractures are most likely to be found, and what would settle them. A targeting hypothesis is a place to look, never a finding.

Governed by [`04-methodology-symmetric-skepticism.md`](04-methodology-symmetric-skepticism.md). Session date: **19 September 2026**.

---

## 0. Reading rule for this document

Every item marked **T-<n>** is a **targeting hypothesis**: an unverified expectation about where a contradiction or anomaly may exist, derived from the structure of the record rather than from reading it. Targeting hypotheses:

- may **not** be cited anywhere as evidence, in either direction;
- may **not** be entered in the anomaly register until a primary source has been read;
- are expected to fail often. A targeting hypothesis that dies on contact with the document is a successful use of this plan, and the death is recorded (`apparent anomaly with adequate explanation`).

The purpose of pre-registering targets is to stop post-hoc target selection — deciding after reading which discrepancy "counts". What each target would have to produce is written down **before** the reading.

---

## 1. Access re-check — material change since the last session

Connectivity re-tested at the start of this session. **The egress blockade recorded on 19 September 2026 in [`03` §3](03-phase2a-mfr-verification.md) and in [`../SOURCES.md`](../SOURCES.md) is largely lifted.**

| Domain | Previous (19 Sep 2026) | Now | Note |
|---|---|---|---|
| `www.archives.gov` | ⚫ 403 CONNECT | ✅ 200 | MFR PDFs return `206 application/pdf` on ranged request — retrievable |
| `www.cia.gov` | ⚫ 403 | ✅ 200 | 6 Aug 2001 PDB returns `206 application/pdf` |
| `www.intelligence.senate.gov` | ⚫ 403 | ✅ 200 | Part Four target |
| `www.nist.gov` | ⚫ 403 | ✅ 200 | NCSTAR target |
| `oig.justice.gov` | not tested | ✅ 200 | DOJ IG reports — ST-2 target |
| `vault.fbi.gov` | ⚫ 403 | ⛔ 403 | Still refused. Likely a site-side filter rather than the egress policy; retest, then route around via alternate provenance |

**Consequence:** ST-1, ST-2, ST-4, ST-7 and Phase 2B are executable now. ST-5's FBI-Vault component is not, and must either wait or be sourced from a repository with declared provenance. This changes nothing about any finding; it changes what the next session can do.

**Caveat before relying on it:** a `200` on a landing page and a `206` on a PDF prove retrievability, not readability. The 6 Aug 2001 PDB was already known to be a scan without a text layer (`02` DOC-6). Retrieval unblocks the OCR problem; it does not solve it. First action of the reading session is to confirm text extraction per document, and to record OCR quality in the document card.

---

## 2. Instruments added by this plan

Reconciling `04` with the forensic audit protocol, three instruments are added:

### 2.1 Escalation ladder (levels may not be skipped)

| Level | Name | What permits entry |
|---|---|---|
| 1 | Discrepancy | Records or claims do not align |
| 2 | Unresolved anomaly | Ordinary reconciliation has been *tested* and remains inadequate |
| 3 | Structured pattern | Multiple **substantially independent** anomalies point the same way |
| 4 | Evidence of concealment | Affirmative acts or records support deliberate withholding or deception |
| 5 | Evidence of foreknowledge or participation | Evidence connects a named actor to specific operational knowledge or material conduct |

Every register entry records its level **and the specific item that permitted the escalation**. A large collection of dependent, low-quality discrepancies does not become a level 3. Level 3 requires independence to be *demonstrated*, not assumed.

### 2.2 Research priority (P0–P3)

Priority measures **research value** — centrality × source quality × discriminating power. It does not measure probability of conspiracy.

| Priority | Criterion |
|---|---|
| **P0** | Documented fracture on a central claim, capable of separating major hypotheses |
| **P1** | Material unresolved tension whose discriminating evidence is obtainable |
| **P2** | Real anomaly with several viable ordinary explanations |
| **P3** | Low-centrality curiosity, or weakly sourced allegation |

### 2.3 Contradiction ledger

Contradictions get their own record, separate from anomalies, because they require a relationship classification the anomaly register does not carry: `direct contradiction` / `material tension` / `scope mismatch` / `revision` / `unresolved`. See [`contradiction-ledger.md`](contradiction-ledger.md).

**Gate before declaring any contradiction:** same proposition, same time interval, same meaning, same organizational level, compatible uncertainty, same clock reference — and a test of whether one statement is simply narrower than the other. Most apparent 9/11 contradictions are scope mismatches. Finding that is a result.

---

## 3. Cross-cutting attack patterns

These apply in every workstream and are where the highest-quality findings usually come from.

### 3.1 Quantifier drift audit

The most productive single technique on this record. For every central claim, recover the **earliest** wording and track each mutation:

| Drift pattern | What to check |
|---|---|
| "no *current* intelligence" → "no intelligence" | Was the qualifier in the original? Who dropped it, and when? |
| "not corroborated" → "false" | A non-corroboration caveat is a statement about verification status, not about truth |
| "not shared *with this official*" → "not shared" | Recipient scope is the whole claim |
| "no *identified* steel sample" → "no steel recovered" | Identification scope vs. recovery scope |
| "no evidence found" → "evidence of absence" | Requires the negative-evidence test (§3.4) |
| "*I* could not have imagined" → "no one imagined" | Person scope |

Drift is checked in **both** directions: critics' summaries of official documents are audited for the same mutations as officials' summaries of their own documents.

### 3.2 Source genealogy mapping

Before treating two accounts as mutual corroboration, establish whether they are genealogically independent. On this record the common ancestors are: a single MFR, a shared briefing, the same institutional talking points, the same attorney, the same press account, or the Commission's own reconstruction fed back to later witnesses.

**Rule:** two retrospective accounts sharing an ancestor are one account. Mark every corroboration claim `independent` / `possibly dependent` / `shared source` / `unknown`.

### 3.3 Three-track timeline

Never merge these: **event time · observation time · communication time · record creation time · later recollection time · release time.** Record clock source, precision, synchronization evidence, and whether a timestamp was machine-generated or reconstructed. Never combine "approximately", rounded media times and synchronized system logs without stating uncertainty bounds — this is the single most common source of false contradictions in the FAA/NORAD material.

### 3.4 Negative-evidence discipline

An absence is probative only if all five hold: the item would probably exist if the hypothesis were true; the search was capable of finding it; the material was preserved; the search scope is documented; and non-recording is not equally plausible. Absent any one, the absence is a **limitation**. This constrains official claims ("no evidence of X was found") and alternative claims ("no test for X was ever run") identically.

---

## 4. Workstream targets

Priorities below are **research priorities**, assigned before reading.

### ST-1 — Intelligence warnings and PDB characterization

Executable now (`archives.gov`, `cia.gov` reachable).

| ID | Targeting hypothesis | Priority | Discriminating evidence |
|---|---|---|---|
| **T-1.1** | The public characterization of the 6 Aug 2001 PDB, the PDB's own text, and the Commission's description of it in DOC-1 are three distinct texts. Suspect **quantifier drift on "current"**, and a scope difference between "historical vs current reporting" and "number of open FBI investigations" — two propositions that can both be true. Classification likely `scope mismatch`, not contradiction | **P0** | Full OCR text of the 6 Aug 2001 PDB, checked against the page image for the decisive sentences. Already located; unread for want of a text layer |
| **T-1.2** | The bolded non-corroboration caveat DOC-1 attributes to the PDB: verify it exists **in the PDB as delivered** and is not the Commission's gloss. If present, it materially weakens any reading of the PDB as an actionable warning; if added later, it weakens DOC-1's characterization | **P0** | Page image of the PDB. Pure document-vs-document test |
| **T-1.3** | The 353-article corpus has **no published topical denominator**. "The reporting pointed abroad" is untestable without it. The Commission published a 24-item core group — a numerator with no denominator | **P1** | The corpus index or article-title list in the ISCAP/NARA holdings. If it does not exist, the claim is permanently `not testable with the public record` — which is itself a reportable result |
| **T-1.4** | Source-reliability annotation. DOC-1 records that CIA rated some core-group reporting "highly questionable, unreliable". Test whether the reliability ratings were carried into the PDBs as briefed, or stripped | **P1** | The PDB texts themselves vs. the underlying reporting cited in DOC-1 |
| **T-1.5** | The 10 Sep 1998 PDB item on an aircraft loaded with explosives vs. the "could not have imagined" family of statements. Run §3.1 on person scope and on "aircraft as bomb" vs "aircraft as guided missile" — plausibly a genuine scope distinction rather than a contradiction | **P1** | The 10 Sep 1998 PDB article; the verbatim transcript of the May 2002 statement, from the primary record, not from quotation |
| **T-1.6** | Title provenance of "Bin Ladin Determined To Strike in US" — whether the title was on the document as delivered. Affects nothing about the content but is a clean test of whether public artifacts match delivered artifacts | **P3** | Page image |

**Pre-registered failure condition for ST-1:** if the PDB text supports Rice's characterization on "current" and the Commission's on "open investigations" simultaneously, the whole cluster resolves as `scope mismatch` and A9/A10 move to `apparent anomaly with adequate explanation`. That outcome is to be reported as prominently as the opposite.

### ST-2 — CIA–FBI information sharing (highest-yield workstream)

Executable now for the MFRs and DOJ IG material.

The al-Mihdhar / al-Hazmi node is where this project's central open question sits, and it is the one place where the record plausibly contains a **contemporaneous** document rather than retrospective memory. That is what makes it P0: everything else in the intelligence track is 2003–2004 recollection.

| ID | Targeting hypothesis | Priority | Discriminating evidence |
|---|---|---|---|
| **T-2.1** | **The cable-that-was-not-sent.** The reported pattern is a draft notification to the FBI prepared in January 2000, and a subsequent internal record indicating it had been sent. If a contemporaneous record states a transmission occurred that did not occur, that is a documentary contradiction with contemporaneous provenance — **the strongest single artifact available anywhere in this track** | **P0** | The cable traffic itself and the DOJ IG's reconstruction of it. **Conclusion ceiling: such a record supports "false internal record" and demands a cause; it does not by itself support intent, and a routine drafting/marking failure predicts the same artifact.** Level 1 on entry; level 4 requires much more |
| **T-2.2** | Named-individual decomposition. "CIA did not tell FBI" is not atomic. Decompose to: who knew of the visa; who knew of the US entry; who had watchlisting authority; who had a duty to act; what each person's channel was; what each did. Institutional claims collapse or survive at this resolution | **P0** | MFRs of Tenet ×3 and Clarke ×3 (retrievable now); DOJ IG report; PENTTBOM |
| **T-2.3** | **"The wall" — legal barrier, practice, or retrospective justification.** Three explanations, identical observable, entirely different implications for H1/H4/H5. Test the text of the 1995 procedures against the barrier as described in later testimony, and against the FISA Court's own characterization | **P1** | The 1995 procedures; OIPR practice records; the FISA Court opinion; contemporaneous legal guidance. **Note the ST-4 interlock:** the author of the 1995 memo later sat on the Commission. That is an independence question for ST-4, not evidence about the wall |
| **T-2.4** | Three institutional reconstructions of the same events exist — Joint Inquiry (2002), DOJ IG, 9/11 Commission (2004). Where they diverge on the same proposition, one is wrong, and the divergence is documented. Where they agree, apply §3.2: agreement may be genealogical | **P1** | The three texts, read against each other proposition by proposition |
| **T-2.5** | Scheuer's A1–A5 claims (`03` §5.1) are currently `document cited, not located`. Tenet's and Berger's MFRs are the second side of the same meetings | **P1** | Tenet ×3, Berger — retrievable now. This closes or hardens rows A1–A5 without any new theory |

### ST-3 — FAA / NORAD / NEADS chronology

| ID | Targeting hypothesis | Priority | Discriminating evidence |
|---|---|---|---|
| **T-3.1** | The **2001 official chronology vs the 2004 tape-based reconstruction** is the cleanest documented revision of an official account in the entire record: an institution's own later work contradicting its earlier public account. Treat as `revision`, and ask the level-4 question explicitly — was the earlier account an error, a reconstruction under pressure, or a misstatement? | **P0** | The 18 Sep 2001 NORAD statement vs the NEADS audio and the Commission's reconstruction; the DoD IG and DOT IG reviews commissioned after the Commission referred the matter |
| **T-3.2** | **"Phantom Flight 11."** Before treating it as an anomaly, test whether it *explains* the earlier chronology innocently — a tracked aircraft that did not exist would produce exactly the notification-time confusion observed. This is a candidate for `apparent anomaly with adequate explanation`, and a good discipline test | **P1** | NEADS audio with timestamps; the position logs |
| **T-3.3** | Shootdown-authorization timing vs PEOC arrival time. Two accounts differ materially; one is a sworn public account, the other a Commission reconstruction footnoted to other sources. Apply §3.3 before calling it a contradiction — clock source and "approximately" wreck most analyses here | **P1** | The Commission's underlying source for its timing; the Secret Service and White House logs; the primary transcript of the conflicting testimony |
| **T-3.4** | Destroyed New York controller recording — a procedural-deviation and chain-of-custody item with a documented IG trail | **P1** | The DOT IG report on the destruction; the retention rules in force. **Ceiling: destruction of a recording of accounts *given after the event* forecloses testimony, not primary event data. Do not inflate.** |

**Discipline note for ST-3:** this workstream generates more false contradictions than any other, because the sources mix machine timestamps, rounded media times and recollection. Every entry carries uncertainty bounds or it does not get entered.

### ST-4 — Commission process, access, testimony, documentation

| ID | Targeting hypothesis | Priority | Discriminating evidence |
|---|---|---|---|
| **T-4.1** | Determinations 5a–5d (`03` §4 priority 5) — who saw the PDB corpus, who saw derived material, whether a formal sharing mechanism existed. Currently the project's largest open factual question about process | **P1** | DOC-1 re-read for signatures, addressee and distribution list; Commission–White House correspondence; internal rules and minutes; Kean/Hamilton archive |
| **T-4.2** | **The Commission's own referral of NORAD/FAA to the Inspectors General.** An official body stating on the record that it was given inaccurate information by another official body is an institutional admission with a paper trail. High yield precisely because it is *internal* to the official account | **P0** | The referral records; the resulting IG reports; the Commission's own statements on the matter |
| **T-4.3** | Independence audit: declared and undeclared conflicts between staff/commissioners and Executive Branch witnesses — including the Zelikow/Rice 1995 co-authorship already noted incidentally in `02`, and the 1995-memo authorship noted at T-2.3 | **P1** | Commission conflict-of-interest declarations; recusal records; staffing records. **Ceiling: a conflict is a reason to scrutinize a product, not a finding about that product's content.** Any conclusion must come from the product itself |
| **T-4.4** | Document-request fulfilment: where the Commission asked for material and did not receive it, and what it recorded about that. Includes material destroyed *after* a request was outstanding | **P2** | Commission document requests and responses; custodian records. This is where a level-4 escalation would have to come from, if anywhere in ST-4 |

### ST-5 — Foreign support and financing

Partially blocked (`vault.fbi.gov` 403); Part Four and the 2015 Review Commission report are reachable.

| ID | Targeting hypothesis | Priority | Discriminating evidence |
|---|---|---|---|
| **T-5.1** | Part Four item-by-item classification under the `03` §6.2 instrument. The pre-registered expectation is that most items are `lead` or `statement` and few are `corroborated fact`. **Count them and report the ratio** — that ratio is the finding, and it constrains both H2/H3 and the popular reading of the "28 pages" | **P0** | Part Four itself, reachable now |
| **T-5.2** | Where an FBI working document and a later official characterization diverge on whether connections existed, that divergence is a documentary contradiction worth locating. **But note the trap:** an investigative working document records what an agent suspected, not what the Bureau established. A "many connections" line in a lead document contradicts a "no connections established" statement only if both address the same proposition at the same evidentiary level — usually they do not | **P1** | The underlying 302s and lead documents; the EO 14040 tranche. Blocked at `vault.fbi.gov`; find declared-provenance alternates |
| **T-5.3** | **Symmetric target.** The pleadings in *In re Terrorist Attacks* are interested-party allegations. Test the cited exhibits against the allegations that rest on them. Where a widely repeated claim traces back only to a pleading, record it as such | **P1** | The docket exhibits themselves. This is the alternative-account stress test for ST-5 and is not optional |

### ST-6 — Evidence preservation and chain of custody

| ID | Targeting hypothesis | Priority | Discriminating evidence |
|---|---|---|---|
| **T-6.1** | Steel retention: how much was kept, by what selection criterion, under whose authority, and what analysis the disposal forecloses. Apply §3.4 rigorously — "no identified sample showing X" and "no steel showing X existed" are different claims (§3.1) | **P1** | Disposition records; the SEAoNY/FEMA collection protocol; FEMA 403 App. C sample provenance **and dating relative to collapse** — the dating is the whole test |
| **T-6.2** | NIST model inputs withheld under NCST Act §7d. A replication limitation, documented and uncontested | **P0** for research value | The §7d determination and its stated basis. **Ceiling: this supports "not independently replicable". It is not evidence the model is wrong, and under `04` S5 it is a limitation, not a result for H6 or H7** |
| **T-6.3** | Recorders: what was searched for, by whom, with what capability, and what was recorded about the search. A textbook §3.4 case in both directions | **P2** | NTSB/FBI search records |

### ST-7 — Structural and forensic claims

| ID | Targeting hypothesis | Priority | Discriminating evidence |
|---|---|---|---|
| **T-7.1** | **NIST's WTC 7 draft-to-final revision on collapse-phase acceleration.** An official technical body revising a quantitative claim between draft and final, in response to external comment, is a documented `revision` with both texts public. This is the highest-value single item in ST-7 because both versions are obtainable and the change is quantitative, not rhetorical | **P0** | The August 2008 draft and the November 2008 final, compared directly. **Ceiling: a revision shows the draft was wrong and the process responsive. Free-fall over an interval is a kinematic description; it is not a mechanism, and it does not by itself select H6 or H7** |
| **T-7.2** | NCSTAR 1-9A: the model runs that did **not** produce collapse, and the criterion by which the final case was selected. Ask the protocol's question directly — did the model *predict* the observation, or was it *selected for matching* it? | **P0** | NCSTAR 1-9A's own scenario-selection text; the excluded runs; sensitivity analysis if published |
| **T-7.3** | Separate the four questions for every proposed mechanism: possibility, case applicability, sufficiency, discrimination. Most of this literature — official and dissenting — conflates possibility with case applicability | **P1** | NCSTAR 1-9 ch. 8 and 12; 1-6C/1-6D |
| **T-7.4** | **Symmetric target — Hulsey/UAF.** Decompose with the same twelve fields: boundary conditions, connection modelling, which failure modes were included and excluded, peer-review status, and whether its inputs are available for replication. If NIST is faulted for withheld inputs, the same standard applies here | **P0** | The full report plus the published formal technical criticism of it |
| **T-7.5** | **Symmetric target — Bažant's energy argument.** A total-energy sufficiency argument does not establish a stage-by-stage mechanism. Test whether the project's own `01` reasoning, and the literature it relied on, made that substitution | **P1** | The papers in full, not the abstracts (`SOURCES.md` currently records abstract-only) |
| **T-7.6** | Each proposed deliberate-intervention mechanism (explosive, incendiary, mechanical) analysed **separately**, with its expected physical, acoustic, seismic, chemical, logistical, photographic and testimonial signatures stated in advance, then asked: was it tested, does a reliable negative exist, and could ordinary processes produce the same signature? | **P1** | Seismic records; dust and residue studies with stated chain of custody; photographic record. Bundling mechanisms is the standard failure here and is prohibited |

---

## 5. Symmetric obligation

Four alternative-account claim families are stress-tested with the same instruments, and this is a delivery requirement, not a gesture:

1. **Hulsey/UAF and technical dissent** (T-7.4) — modelling assumptions, excluded failure modes, replicability.
2. **"28 pages" as proof of state participation** (T-5.1) — the classification ratio tests it directly.
3. **Pleading-sourced claims** (T-5.3) — trace to exhibit or mark as allegation.
4. **Foreknowledge-from-warnings inference** — the step from "warnings existed" to "operational foreknowledge" is tested as its own proposition, with its own required evidence, in every workstream that touches it.

Register health check (`anomaly-register.md` §6) reports the official/alternative entry balance at the end of every phase. A register populated in one direction only is treated as evidence about the reading, not about the world.

---

## 6. Execution order for the next reading session

Access is open. The queue is:

1. **Document cards first.** For each of the nine unread MFRs and the 6 Aug 2001 PDB: retrieve, record the card fields from [`../SOURCES.md`](../SOURCES.md) §Document cards, test text extraction, record OCR quality. No claims yet. *Stop condition: if decisive OCR cannot be checked against the page image, the passage is not quotable.*
2. **ST-2 / T-2.5 and T-2.2** — Tenet ×3, then Berger, then Clarke ×3, then Scheuer #2/#3. This closes or hardens A1–A5 and builds the named-individual decomposition. Highest yield per page.
3. **ST-1 / T-1.1 and T-1.2** — the 6 Aug 2001 PDB with OCR, against DOC-1 and against the primary transcript of the public characterization.
4. **ST-2 / T-2.1** — DOJ IG material on the January 2000 notification chain, via `oig.justice.gov`.
5. **ST-4 / T-4.1** — DOC-1 re-read for signatures, addressee, distribution list.

Steps 2–5 populate [`claim-decomposition-register.md`](claim-decomposition-register.md), [`anomaly-register.md`](anomaly-register.md) and [`contradiction-ledger.md`](contradiction-ledger.md). The phase closes with the four mandatory sections of `04` §6 plus a reproducibility record.

**Before any of it:** update the access-failure record in `SOURCES.md` with today's re-check. The blockade note is now stale and would otherwise be read as current.

---

## 7. Conclusion ceilings fixed in advance

Written before reading, so they cannot be loosened afterward:

| If the reading shows | The strongest permitted conclusion is |
|---|---|
| A contemporaneous record stating a notification was sent that was not sent | "False internal record; cause undetermined." Not intent |
| Conflicting recollections between two witnesses | "Testimony conflict." Not that either lied |
| Model inputs withheld | "Replication limitation." Not that the model is wrong or fraudulent |
| Warnings existed and were specific | "Forewarning of a threat category." Not operational foreknowledge |
| Documented contact between a foreign-linked individual and a hijacker | "Contact." Not support, not knowing support, not state direction |
| An official chronology revised after tapes were reviewed | "Revision, and a duty to explain the earlier account." Not proof the earlier account was deliberate |
| An unexplained physical observation | "Warrants forensic testing." Not a specific mechanism |
| A test was never run | "Limitation." Never a result, in either direction |

---

## 8. What this plan does not assert

It asserts no fact about 9/11. Every T-item is an expectation about where to look, generated from the shape of the record — which documents exist, which were produced when, and which have been compared with which. Several are expected to resolve as ordinary. None of them may be quoted as a finding, and the anomaly register stays empty until primary sources have been read.
