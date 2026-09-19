# Atomic Claim Registry

> Living instrument. Governed by [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) §2 and §5.
> Last change event: **19 September 2026** (opening of the registry; ingestion of DOC-7, MFR George Tenet #2).

---

## 1. Required fields

Every atomic proposition carries these fields. Where a field is not yet determined it reads `unknown` or `not determined` — never blank, and never an assumption.

| Field | Meaning |
|---|---|
| **ID** | Stable. `A<n>.<k>` for propositions inside a Phase A container; `T-<nn>` for propositions first recorded from DOC-7; `C-<nn>` for critical/alternative claims |
| **Proposition** | One testable statement. If it contains "and", check whether it is two propositions |
| **Claimant / issuer** | Named person or institution |
| **First known date** | Earliest date at which the claim is recorded as made |
| **Later versions** | Cross-reference to [`version-history.md`](version-history.md) |
| **Supporting evidence** | What, read to what extent, image-verified or not |
| **Contrary evidence** | Same standard |
| **Contextualizing only** | Evidence that bears on plausibility but does not establish the proposition. Kept separate on purpose |
| **Provenance root** | Earliest recoverable source — see [`provenance.md`](provenance.md) |
| **Source dependencies** | Which other claims/documents share that root |
| **Access limitations** | Redaction, non-location, inaccessibility |
| **Competing explanations** | EC1–EC5, per `04` §5 |
| **Status** | Closed vocabulary, §2 below |
| **Confidence** | Qualitative and conservative. No numbers |
| **Closure condition** | What would have to exist and be read before this row may be closed |

---

## 2. Status vocabulary (closed — unchanged from [`../docs/03`](../docs/03-phase2a-mfr-verification.md) §5)

`declaração não corroborada` · `documento citado, não localizado` · `documento localizado, não lido` · `parcialmente corroborada` · `corroborada` · `contradita` · `inconclusiva`

The vocabulary is retained in Portuguese deliberately: it is the same closed vocabulary already applied to the sixteen Phase A rows, and translating the tokens would silently break comparability with [`../docs/03`](../docs/03-phase2a-mfr-verification.md) §5. Glossary:

| Token | English gloss |
|---|---|
| `declaração não corroborada` | uncorroborated statement |
| `documento citado, não localizado` | document cited, not located |
| `documento localizado, não lido` | document located, not read |
| `parcialmente corroborada` | partially corroborated |
| `corroborada` | corroborated (requires a source independent of the claimant, read in full) |
| `contradita` | contradicted (requires the contradicting source read in full) |
| `inconclusiva` | inconclusive |

Application rules from `03` §5 remain in force, with one addition under [`04` §0.2](../docs/04-controlling-methodology.md):

> **Addition (MD-002).** `corroborada` on the strength of a document's self-description establishes *officially asserted*, not *independently corroborated*. Such rows carry `independence: none (self-description)`.

---

## 3. Phase A containers, decomposed

The sixteen rows A1–A16 in [`../docs/03` §5](../docs/03-phase2a-mfr-verification.md) are **preserved verbatim there and are not edited**. They are carried here as containers with no status of their own (MD-007).

Sources: DOC-1 (*Report on Review of PDB Articles*, 09 Feb 2004), DOC-2 (MFR Rice, 07 Feb 2004), DOC-3 (MFR Scheuer #1, 11 Dec 2003) — all read in Phase A, **none image-verified** (see [`cards/README.md`](cards/README.md) §3). DOC-7 (MFR Tenet #2, 22 Jan 2004) read and partially image-verified in this session.

### A1 — container (Scheuer, sworn): absence of strategic analytic product / NIE until mid-1999

| ID | Proposition | Status | Moved this session | Closure condition |
|---|---|---|---|---|
| A1.1 | No NIE on UBL/al-Qa'ida attack methods was produced before mid-1999 | `documento citado, não localizado` | no | NIE production record, or its documented absence, from CIA/NIC |
| A1.2 | No consolidated strategic analytic product on UBL existed before mid-1999 | `inconclusiva` | **yes** — was `documento citado, não localizado` | Scheuer memo 28 Jun 1999; CIA analytic production record 1996–1999 |
| A1.3 | Scheuer repeatedly requested such a product | `documento citado, não localizado` | no | Scheuer memo 28 Jun 1999 located and read |

**A1.2 change note.** DOC-7 p.1 records Tenet stating that after the 1998 East African embassy bombings "CIA had a strategic framework to address the elements of the al Qaeda threat, but in 1999, a new strategic plan was required ('The Plan')", and p.16 that "contrary to the Joint Inquiry's conclusions, Tenet insisted that there was a plan for ramping up war-like activities." A *plan* and an *analytic product/NIE* are different objects (EC1 strongly live), so this is not a contradiction; it is an unresolved tension between two sworn witnesses about what existed before mid-1999. See [`discrepancies.md`](discrepancies.md) DISC-001.

### A2 — container (Scheuer, sworn): WMD text barred from the 25 Mar 1999 PDB

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A2.1 | A text on WMD was prepared for the 25 Mar 1999 PDB | `documento citado, não localizado` | no | The internal memorandum; testimony of the PDB author named in DOC-3 |
| A2.2 | It was removed before publication | `documento citado, não localizado` | no | Same. **The published PDB cannot test this** — `03` §4 priority 3 |
| A2.3 | Removal was directed by or on behalf of the DCI | `declaração não corroborada` | no | Contemporaneous direction record; Tenet MFRs #1 and #3 |
| A2.4 | The purpose was to conceal a ~2-year delay in passing information to the FBI | `declaração não corroborada` | no | Same, plus the FBI transmission record |

DOC-7 contains nothing on A2. Tenet MFRs #1 (23 Dec 2003) and #3 (28 Jan 2004) remain unread.

### A3 — container (Scheuer, sworn): 30% vs 0%

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A3.1 | An estimated probability of success at or below ~30% existed for the May 1998 capture operation | `parcialmente corroborada` | **yes** — was `declaração não corroborada` | The estimate's originating document; or the redacted attribution at DOC-7 p.3 released |
| A3.2 | That figure was communicated to Berger, Reno, Freeh and Clarke | `inconclusiva` | **yes** — was `declaração não corroborada` | MFRs of Berger, Reno, Freeh; contemporaneous briefing records |
| A3.3 | A figure of 0% was communicated to Mary Jo White | `declaração não corroborada` | no | MFR of Mary Jo White; MFR of Patrick Fitzgerald |
| A3.4 | The discrepancy between the two figures was deliberate | `declaração não corroborada` | no | All of the above plus a stated rationale |

**A3.1 change note (image-verified).** DOC-7, printed p.3, PDF p.3, checked against page image, source layer `native text` corroborated by image:

> "Tenet recalled talking about this issue for a long time—he 'probed on the operations side,' and noted that the operation's prospect of success as described to him was less than 30% (the figure agreed upon [REDACTED 25X1]."

Assertion type: `recollection` (of a 1998 briefing, given in 2004). This is a second sworn witness, independent of Scheuer, placing a sub-30% figure in the same decision. It **materially qualifies** Scheuer's "30%": Tenet says *less than* 30%, and describes it as the figure given **to him**, not as a figure briefed outward. The attribution of who agreed the figure is redacted — the row cannot close while that redaction stands.

**A3.2 change note.** DOC-7 p.4 (image-verified) records the opposite direction of flow: Tenet "called Berger to inform him of his operational decision—not to debate the issue, (that is, he did not offer Berger a choice)", and "did not tell the Principals' Committee why he cancelled the operation". Tenet says nothing about communicating any percentage to Berger, Reno, Freeh or Clarke. This is neither corroboration nor contradiction — it is a differently-scoped account of the same interaction (EC1), recorded at DISC-002.

### A4 — container (Scheuer, sworn): Saudi non-cooperation

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A4.1 | Obtaining direct access to individuals in Saudi custody or reach was a persistent problem for CIA | `parcialmente corroborada` | **yes** — was `documento citado, não localizado` | A contemporaneous 1996–2001 record of a refused access request |
| A4.2 | The Saudis never provided useful information on UBL (absolute form) | `contradita` | **yes** — was `documento citado, não localizado` | — contradicted; see note |
| A4.3 | Saudi Arabia gave sanctuary to al-Qa'ida financier Madani al-Tayyib | `documento citado, não localizado` | no | An independent contemporaneous record. **Possible circularity — see [`provenance.md`](provenance.md) PR-004** |
| A4.4 | The non-cooperation was systematic and deliberate rather than episodic | `declaração não corroborada` | no | A pattern established from contemporaneous records, not recollection |
| A4.5 | Saudi cooperation on UBL was materially incomplete | `parcialmente corroborada` | **new row** | Contemporaneous record of what was requested and what was supplied |

**A4.1 / A4.5 change note (image-verified).** DOC-7 printed p.5, checked against page image:

> "Tenet had no recollection on the issue of U.S. access to the al Qaeda treasurer Madani al-Tayyiib (to whom the Saudis had given sanctuary), but noted that getting direct access to people used to be a constant problem with the Saudis (though no longer)."

and

> "Overall, Tenet saw the Saudis as very concerned about UBL, but he was not always convinced that they gave the U.S. everything they knew about him."

**A4.2 change note.** The same page contradicts the absolute form: Tenet states that in 1998 "Crown Prince Abdullah was certainly sincere about helping the U.S.; he distinguished the Crown Prince as someone who was always helpful". `contradita` here means **the proposition as literally stated** is negated by a sworn witness's direct testimony read in full and image-verified. It does **not** mean the underlying question of Saudi cooperation is resolved — that is A4.5, which is not closed. Both witnesses are interested; neither offers a contemporaneous document.

**A4.3 warning.** The words "(to whom the Saudis had given sanctuary)" appear in DOC-7 as an unattributed parenthetical inside a sentence reporting Tenet's **non**-recollection. Its author is the Commission staff drafter, not necessarily the witness, and its own source is not given. It may derive from Scheuer's testimony to the same Commission — in which case it is not independent corroboration of Scheuer but a restatement of him. Recorded as an unattributed institutional assertion with `independence: unknown`. **It does not move A4.3.**

**Redaction finding.** Roughly 60% of DOC-7 printed p.4 — the page whose running head is "The Saudis" — is a single redaction block marked 25X1, invisible in the extracted text layer and visible only on the page image. Any conclusion about what this document does or does not say on Saudi matters must be read against that void. See [`cards/DOC-7-mfr-tenet-2.md`](cards/DOC-7-mfr-tenet-2.md) §5.

### A5 — container (Scheuer, sworn): Saudi offer as a reason for the May 1998 cancellation

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A5.1 | A Saudi initiative to resolve the UBL problem existed in 1998 | `parcialmente corroborada` | **yes** — was `declaração não corroborada` | Contemporaneous record of the initiative and its terms |
| A5.2 | That initiative was among the reasons the May 1998 capture operation was cancelled | `contradita` | **yes** — was `declaração não corroborada` | — contradicted by the decision-maker; see note and DISC-003 |

**Change note (image-verified).** DOC-7 printed p.4:

> "Tenet remarked that his contemporaneous trip to Saudi Arabia (May 1998) was entirely unrelated to the cancellation of the capture operation."

and, same page:

> "In the summer of 1998, Tenet did not think the USG was putting much faith in the Saudi initiative to persuade the Taliban to give up UBL—at least no more faith than in any other opportunities that presented themselves."

The second passage establishes A5.1 partially: a Saudi initiative existed and was known to the DCI — though its object as Tenet describes it (persuading the **Taliban** to give up UBL) is not identical to the object Scheuer describes (the Saudis resolving the UBL case **themselves**). That scope difference is itself recorded at DISC-003.

A5.2 is contradicted by the decision-maker's own sworn account of his own decision, image-verified. **This does not establish that the decision was sound, nor that no Saudi consideration existed anywhere in the process** — Tenet is an interested witness with a direct stake in this decision, EC3 is live, and no contemporaneous memorandum of the decision has been located (see T-03).

### A6 — container (Scheuer, sworn): the 10 Sep 1998 report and aircraft-as-weapon

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A6.1 | A PDB article of 10 Sep 1998 reported a plot involving an explosives-laden aircraft | `parcialmente corroborada` | no | The PDB article itself (indexed in DOC-1; not read) |
| A6.2 | Scheuer did not recall that report | `declaração não corroborada` | no | Not independently testable; retains recollection status permanently |
| A6.3 | Aircraft-as-weapon was known within the UBL target set before 1999 (Murad case) | `documento citado, não localizado` | no | The Murad case file / Bojinka record |

### A7 — container (Scheuer, sworn): Pakistani service and UBL

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A7.1 | Scheuer characterized an instrumental ISI–UBL training relationship as "too conspiratorial" | `corroborada` (as a statement in DOC-3) | no | — established only as *appearing in the document* |
| A7.2 | No instrumental relationship existed between the Pakistani service and UBL for training | `inconclusiva` | **yes** — was carried at container level as `declaração não corroborada` | Contemporaneous reporting on ISI–UBL contacts |

**Change note.** DOC-7 p.12: "Tenet commented that the Pakistanis could have delivered ½ of UBL's lieutenants if they had wanted to, but were cooperating with UBL." Two sworn witnesses give incompatible impressions — but of different objects: Scheuer addresses an instrumental *training* relationship; Tenet addresses *cooperation* with UBL generally. EC1 is strongly live. DISC-004. Not image-verified (text layer only) — flagged.

### A8 — container (Rice, not under oath): the May 2002 statement

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A8.1 | Rice stated publicly in May 2002 that the use of planes as missiles could not have been predicted | `documento citado, não localizado` | no | The May 2002 press-conference transcript — public, trivially locatable, **still unread** |
| A8.2 | Rice told the Commission she misspoke and meant herself | `parcialmente corroborada` | no | DOC-2 re-carded under the image standard |
| A8.3 | Rice learned only after 9/11 of earlier reporting on aircraft as weapons | `declaração não corroborada` | no | Briefing records of what was shown to her and when |

### A9 — container (Rice): "all of the reporting pointed abroad"

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A9.1 | No PDB-channel reporting in the relevant window described attacks inside the United States | `contradita` (absolute form) | no | — DOC-1 records 24 core-group articles on attacks in the US and/or aircraft |
| A9.2 | The reporting stream in summer 2001 predominantly indicated attacks abroad | `inconclusiva` | no | Month-by-month distribution of the 353-article corpus, with denominators |
| A9.3 | Rice's statement was scoped to summer 2001 rather than 1998–2001 | `inconclusiva` | no | The full text of her statement in context |

**Contextualizing only (does not move any row).** DOC-7 p.19 records Tenet, in 2004, on the Millennium period: the Ressam arrest, "the plot against LAX and the Seattle target—two domestic targets. Retrospectively, these were important examples of the potential for domestic attack"; and "Looking back now, Tenet recognizes that at this time the country was absolutely unprotected. Although the U.S. was under attack, border, visas, and watchlists were not thought about". This concerns 1999–2000, not summer 2001, and is retrospective judgment recorded in 2004. It is filed as context, not as evidence on A9.

### A10 — container (Rice): the 6 Aug 2001 PDB

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A10.1 | The 6 Aug 2001 PDB contained no current threat information | `inconclusiva` | no | **BLOCKED** — the PDB text (OCR required) **and** DOC-1 re-carded under the image standard |
| A10.2 | The reported UAE-embassy contact appeared to be a hoax | `inconclusiva` | no | Same |

### A11–A14 — containers (Rice)

| ID | Proposition | Status | Moved | Closure condition |
|---|---|---|---|---|
| A11.1 | Rice never saw Predator video of UBL | `inconclusiva` | no | Viewing records; the Gellman reporting's own underlying source |
| A11.2 | A Predator showing occurred on 10 Jan 2001 | `inconclusiva` | no | Same |
| A12.1 | Rice placed a call to the President from the Situation Room on 11 Sep 2001 | `documento citado, não localizado` | no | Situation Room log; Presidential Diary |
| A12.2 | That call preceded her move to the PEOC | `documento citado, não localizado` | no | Same |
| A12.3 | The log and Diary record 09:40 | `documento citado, não localizado` | no | Same. Cited by Commission staff **inside** DOC-2 — staff note, not the log |
| A13.1 | Prince Bandar's call at 12:25 on 11 Sep 2001 was condolences, not substantive | `declaração não corroborada` | no | Call record or a second participant's account |
| A13.2 | No Saudi evacuation was mentioned in that call | `declaração não corroborada` | no | Same |
| A14.1 | Private Saudi funds reached NGOs linked to terrorism | `parcialmente corroborada` | **yes** — was `declaração não corroborada` | Contemporaneous financial-intelligence records |
| A14.2 | Rice had no clarity about Saudi **government** money | `declaração não corroborada` | no | Not independently testable as to her state of mind |

**A14.1 change note (image-verified).** DOC-7 printed p.5: "Tenet noted that we now know about Saudi funding of suspect charitable organizations that were in fact supporting al Qaeda, but was not sure about the extent of what the U.S. knew about this at the time." And: "Saudi societal elite must have known that donations to charities were going to UBL, but Tenet cannot prove it." A second, independent, sworn witness — but both statements are 2003–2004 judgment, not contemporaneous record, and Tenet expressly disclaims proof. Note that Tenet draws the same individual/state distinction the Phase 2B protocol requires ([`../docs/03` §6.1](../docs/03-phase2a-mfr-verification.md)): "while many Saudi individuals are prominent fundraisers, does this mean that the Saudis in general are financing terrorism?"

### A15–A16 — containers (PDB Review Team, institutional)

| ID | Proposition | Status | Independence | Closure condition |
|---|---|---|---|---|
| A15.1 | The reviewed corpus comprised 353 PDB articles (1998 – 20 Sep 2001) on the defined topics | `corroborada` | **none (self-description)** | An external index of the corpus |
| A15.2 | A "core group" of 24 articles was identified | `corroborada` | **none (self-description)** | Same |
| A15.3 | The Review Team comprised 4 people, including Chair and Vice-Chair | `corroborada` | **none (self-description)** | Commission–White House correspondence; the memo's distribution list |
| A15.4 | A subcommittee of 2 had access to the remainder | `corroborada` | **none (self-description)** | Same |
| A16.1 | The 6 Aug 2001 PDB carried a bolded caveat that CIA could not corroborate the most sensational reporting | `documento localizado, não lido` | — | **BLOCKED** — the PDB text; DOC-1 re-carded |

> **MD-002 applied.** A15.1–A15.4 are established as *officially asserted by the document that describes itself*. None is independently corroborated. The `corroborada` status recorded in Phase A is retained, and the independence column now states the limit explicitly. Determinations 5a–5d in [`../docs/03` §4](../docs/03-phase2a-mfr-verification.md) remain open.

---

## 4. Competing-explanation fields (EC1–EC5)

Every discrepancy carries a full EC analysis — predicted evidence, weakening evidence, discriminating evidence, what is currently available, what is inaccessible, and whether the same evidence fits more than one class. Those analyses live in [`discrepancies.md`](discrepancies.md) §3 to avoid duplicating them per claim row. The mapping is:

| Claim rows | Discrepancy |
|---|---|
| A1.2 | [DISC-001](discrepancies.md#disc-001) |
| A3.1, A3.2, T-01, T-02, T-04 | [DISC-002](discrepancies.md#disc-002) |
| A4.1, A4.2, A5.1, A5.2, T-05 | [DISC-003](discrepancies.md#disc-003) |
| A7.2 | [DISC-004](discrepancies.md#disc-004) |
| T-06, T-07, T-09 | [DISC-005](discrepancies.md#disc-005) |
| DOC-7 document integrity | [DISC-006](discrepancies.md#disc-006) |

---

## 5. T-series — propositions first recorded from DOC-7 (MFR George Tenet #2, 22 Jan 2004)

Witness under oath (oath administered by Commissioner Roemer, recorded on printed p.1). Event date 22 Jan 2004; document date 22 Jan 2004 **plus later annotation** (see DISC-006); declassification date 8 Sep 2026. Distance event → facts described: 3 to 8 years. **None of these propositions is a contemporaneous record of 1996–2001.**

| ID | Proposition | Assertion type | Status | Image-verified | Closure condition |
|---|---|---|---|---|---|
| T-01 | The May 1998 capture operation was cancelled by the DCI on the strong and unanimous recommendation of DDO Jack Downing, C/CTC Geoff O'Connell and C/NE [REDACTED], citing operational impediments and collateral-damage risk | recollection | `declaração não corroborada` | **yes** (p.3) | The officers' recommendation as a contemporaneous record; MFRs of Downing/O'Connell |
| T-02 | The operation's prospect of success as described to the DCI was "less than 30%" | recollection | `declaração não corroborada` | **yes** (p.3) | The originating estimate document; release of the redacted attribution |
| T-03 | The DCI did not recall whether any memorandum memorialized his decision or the three officers' recommendation | access/process statement | `declaração não corroborada` | **yes** (p.4) | A records search establishing that such a memorandum exists or does not |
| T-04 | The DCI informed Berger of the cancellation without offering a choice; Berger did not push back; the DCI did not tell the Principals' Committee why he cancelled | recollection | `declaração não corroborada` | **yes** (p.4) | MFR Berger (unread); NSC records of the notification |
| T-05 | The DCI's May 1998 trip to Saudi Arabia was entirely unrelated to the cancellation | recollection | `declaração não corroborada` | **yes** (p.4) | Trip records; the redacted block on the same page |
| T-06 | On three occasions after August 1998 TLAM gyros were spun for a strike on UBL (Nov–late Dec 1998; Feb–Mar 1999, UAE hunting camp; May 1999, Kandahar); in none did the DCI have high confidence in the intelligence while no one acted | recollection, **read from a briefing paper** | `declaração não corroborada` | no (text layer, pp. 8–9) | The strike packages; the CIA staff paper at T-07 |
| T-07 | The DCI's account of those three occasions was read aloud from a CIA staff paper prepared to brief him for this interview, which CIA undertook to provide to the Commission | access/process statement | `documento citado, não localizado` | no (text layer, p.8) | **The staff paper itself.** See [`provenance.md`](provenance.md) PR-006 — this makes T-06 a 2004 CIA reconstruction, not the witness's memory |
| T-08 | CIA's draft February 1999 MON sought authority to kill UBL; President Clinton replaced the language by hand; Commissioner Ben-Veniste recorded a differing reading of the accompanying NSC note | direct quotation of a contemporaneous instrument, read aloud | `documento citado, não localizado` | no (text layer, p.11) | The February 1999 MON; CIA's transmittal letter and internal papers (item 9 of the document's own follow-up list) |
| T-09 | Richard Clarke warned the UAE about the possible strike near the hunting camp; Rousseau's impression was that the call preceded the strike decision; the DCI had no recollection of clearing it | third-party report | `documento citado, não localizado` | no (text layer, p.9) | The diplomatic cable traffic and the State reporting cable named on p.9 |
| T-10 | The DCI assessed covert action's probability of success against UBL at about 10%, and CIA's odds in Afghanistan at 10–20% | analytical judgment | `declaração não corroborada` | no (text layer, p.12) | Contemporaneous assessments, if any exist |
| T-11 | A June 1999 memo from Berger to President Clinton (per Zelikow, likely drafted by Clarke) stated that covert action was not fruitful, that more attacks were a certainty, and that they could occur in the US and involve WMD; the DCI agreed it fairly stated the period | third-party report of a contemporaneous document | `documento citado, não localizado` | no (text layer, p.17) | **The June 1999 memo.** A contemporaneous 1999 record — high priority under [`../docs/05` §4](../docs/05-phase-c-competing-narratives.md) |
| T-12 | The DCI described an "iron-clad wall" between intelligence and law enforcement; the FBI had no CT headquarters, lacked reports officers, could not link cases or do analysis, and did not disseminate intelligence; FBI 302s were hard for CIA to access | analytical judgment | `declaração não corroborada` | no (text layer, p.20) | DOJ IG reports; FBI dissemination records. Bears on [`../docs/03` §4](../docs/03-phase2a-mfr-verification.md) priority 6 |
| T-13 | During and after the Millennium period "the country was absolutely unprotected" and "border, visas, and watchlists were not thought about" | recollection / analytical judgment | `declaração não corroborada` | **yes** (p.19) | Watchlisting and border records for the period |

### 5.1 Negative finding — recorded as a finding, not as an absence of interest

**T-N1.** DOC-7 contains **no occurrence** of `Mihdhar`, `Hazmi`, `Malaysia`, `Kuala Lumpur`, `Moussaoui` or `Phoenix`, and exactly one occurrence of `watchlist` (printed p.19, in the general Millennium-lessons passage quoted at T-13). Verified by exhaustive string search of the full extracted text of all 24 pages.

Consequence: **Priority 1 of [`../docs/03` §4](../docs/03-phase2a-mfr-verification.md) — the al-Mihdhar / al-Hazmi node, where H5 has its best theoretical case — is not advanced by this document.** It remains untouched.

This is a statement about the reviewed corpus, not about the world: "not found in DOC-7" is not "was not discussed", and is certainly not "did not exist". The redaction blocks in DOC-7 are extensive; the single largest, on printed p.4, is unread by anyone outside the declassifying authority.

---

## 6. C-series — critical and alternative claims

**Empty by design.** Opening this series is gated on the source-inclusion procedure in [`source-policy.md`](source-policy.md) §2–§3, per [`../docs/05` §4](../docs/05-phase-c-competing-narratives.md). Populating it from memory or unconstrained search would import precisely the provenance failures this registry exists to detect.

---

## 7. Blocking gates currently in force

| Gate | Blocks | Cleared by |
|---|---|---|
| Re-carding of DOC-1, DOC-2, DOC-3 under the image-verification standard | A8.2, A9.1, A10.1, A10.2, A15.1–A15.4, A16.1 and every conclusion depending on them | Re-reading the three documents against page images; [`cards/README.md`](cards/README.md) §3 |
| OCR of the 6 Aug 2001 PDB | A10.1, A10.2, A16.1 | Access to the file plus OCR |
| MFRs of Tenet #1 and #3, Clarke ×3, Berger, Scheuer #2 and #3 | A1.x, A2.x, A3.2, A3.3, T-01, T-04 | Reading the remaining eight MFRs |
| Source policy applied to a candidate set | The entire C-series | [`source-policy.md`](source-policy.md) |
| B1 quarantine | Any reuse of B1 distributions | Permanent — B1 is invalidated, not pending |
