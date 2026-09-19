# Next Phases

> **Environment update (19/09/2026, session 2).** The network block recorded below (session 1, same date) was retested and **did not hold** for most domains: `archives.gov`, `cia.gov`, `nist.gov`, `intelligence.senate.gov`, `govinfo.gov`, `9-11commission.gov`, and `govinfo.library.unt.edu` respond HTTP 200. `vault.fbi.gov` and `www.fbi.gov` remain blocked (403) — the block stopped being general and is now selective to those two hosts. With access restored, Phase 2A was executed in this session: the nine pending MFRs and the 06/08/2001 PDB (via OCR) were read in full — see [`docs/03-phase2a-mfr-verification.md`](docs/03-phase2a-mfr-verification.md), sections 3.1, 4, 5, and 7, and [`SOURCES.md`](SOURCES.md). **Before starting any new phase, always re-verify read access to the target domains** — the block has already shown itself to be unstable between sessions on the same day — and never produce conclusions from search results or prior knowledge, per the execution rule at the end of this file.
>
> **Original failure record (session 1, kept for traceability).** In an attempt to execute this on 19/09/2026, all the domains above (except the two FBI ones) were blocked by the environment's network egress policy (403 on CONNECT).

Roadmap for continuing the audit, in the execution order planned at the end of Phase 1 (see [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md), section 9).

**Execution order:** 2A → 2B → 3 → 4. The sequence is not arbitrary: 2A and 2B use material that is already declassified and of a manageable volume, and bear on the hypotheses where Phase 1 left explicit gaps (H5 at the al-Mihdhar/al-Hazmi node; H2/H3 in the support network). Phase 3 is the most expensive in reading volume and only pays off once the corrections in section 2 of `docs/02` have been internalized. Phase 4 depends on time-stamped material that may require long-lead access requests — it is worth starting those requests early, even while running this phase last.

Before starting any phase, read [`README.md`](README.md) (hypotheses and confidence scale), [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md) (current state), and [`SOURCES.md`](SOURCES.md) (what has already been read, and to what depth).

## Phase 2A — Remaining MFRs from the 2026 release

**Status: reading of the nine MFRs completed on 19/09/2026 (session 2).** Results incorporated into [`docs/03-phase2a-mfr-verification.md`](docs/03-phase2a-mfr-verification.md) (sections 4, 5, 7). Remaining pending items for this phase: a targeted rereading of DOC-1 for priority 5 (5a/5b), and locating — outside the 2026-201 release — the MFRs of Reno, Freeh, White, and Fitzgerald in NARA's general holdings. Neither of these two items has been started.

~~Read the 9 still-unread MFRs in full, in this order: Tenet (×3) → Clarke (×3) → Berger → Scheuer (×2).~~ — done.

**Six pre-registered priorities** (questions, discriminating tests, and criteria for a positive/negative/inconclusive answer in [`docs/03` §4](docs/03-phase2a-mfr-verification.md)):

1. The al-Mihdhar/al-Hazmi node — where H5 is decided. It stopped being untouched in session 2 (19/09/2026): testimony from Clarke/Tenet/Black has been read and tabulated, but no contemporaneous document has been located yet — see [`docs/03` Priority 1](docs/03-phase2a-mfr-verification.md).
2. The 30% vs. 0% discrepancy in the May 1998 UBL capture operation.
3. The allegedly withheld 25/03/1999 PDB — watch for the trap: the published PDB does not test the claim, the internal memorandum does.
4. The 06/08/2001 PDB — requires OCR, the PDF has no text layer.
5. The Commission's PDB access structure — four separate determinations (5a–5d), including the named identification of the 4 Review Team members and the 2 subcommittee members.
6. CIA–FBI interaction and the gap between foreign intelligence and domestic investigation — a legal barrier, institutional practice, or a case-by-case decision are three different things.

**Required output:** every relevant claim enters the table in [`docs/03` §5](docs/03-phase2a-mfr-verification.md) with the fixed columns (claim · made by · under oath · contemporaneous document cited · located · read · independent corroboration · status) and a status from the closed vocabulary.

## Phase 2B — Joint Congressional Inquiry

**Status: open, not executed. Access to `intelligence.senate.gov` confirmed on 19/09/2026 (session 2)** — the phase is executable from here, contrary to what session 1 recorded. Classification protocol pre-registered in [`docs/03` §6](docs/03-phase2a-mfr-verification.md).

Read the full 2002 Joint Inquiry report and Part Four (the "28 pages"), declassified in 2016. Compare with Chapter 5 of the 9/11 Commission Report.

**Specific objective:** advance H2/H3 — the only way out of "genuinely unresolved" for these two hypotheses is with material that directly addresses the support network for al-Hazmi and al-Mihdhar (Omar al-Bayoumi, Fahad al-Thumairy, Osama Bassnan), which Phase 1 did not touch.

**Non-negotiable treatment rule:** the "28 pages" are **not** proof of Saudi state participation. Each item receives exactly one classification — `lead`, `statement`, `document`, `corroborated fact`, `judicial allegation`, or `investigative conclusion` — plus a record of whether the Joint Inquiry declared it resolved, unresolved, or not pursued. An individual with a government tie is not the government; contact is not support; support is not conscious support for the attack.

## Phase 3 — Deep technical audit (engineering)

**Access to `nist.gov` confirmed on 19/09/2026 (session 2).** Phase not started in this session — the execution order is 2A → 2B → 3 → 4 (see above), and 2B is still open.

Reading sequence defined in [`docs/02`](docs/02-adversarial-audit-phase1.md), section 7:

1. FEMA 403, Appendix C — sulfidic corrosion/eutectic, with attention to sample dating (before or after the collapse).
2. NCSTAR 1-9, chapters 8 and 12 — connection properties, shear studs, seat dimensions, ANSYS→LS-DYNA data transfer, boundary conditions.
3. NCSTAR 1-9A — models that did **not** produce collapse and the criterion for selecting the final case. High priority: the point of highest potential evidentiary yield, and the most affected by files withheld under Section 7d of the NCST Act.
4. NCSTAR 1-6C and 1-6D — connections, thermal restraint, global tower analysis.
5. The full Hulsey/UAF report + published formal technical critiques of it.
6. Own stage-by-stage conceptual modeling: participating mass, ejected fraction, compaction ratio, available fall height, sensitivity of conclusions to assumptions.

## Phase 4 — FAA/NORAD Chronology

Minute-by-minute reconstruction using time-stamped records: FAA recordings, NEADS/NORAD recordings, radar, logs, phone calls, scramble orders, comparing the official 2001, 2003, and 2004 versions.

**Specific points of investigation:**
- Why NORAD's initial chronology differed from the later reconstruction.
- The "phantom Flight 11."
- Notification times for Flights 11, 175, 77, and 93.
- Destruction of the recording of New York controllers' accounts.

**Treatment rule:** do not automatically turn post-event falsehood or cover-up into proof of prior participation — test these as separate hypotheses (H1 vs. H5).

## Background items, not yet assigned to a phase

- Interrogations of KSM, bin al-Shibh, Abu Zubaydah: for each statement used in the planning narrative, verify whether it was produced before or after a coercive technique, whether there is independent documentary corroboration, and compare with the Senate report (SSCI CRPT-113srpt288).
- Seismic and financial evidence (suspicious trading, SEC/FBI) and the Pentagon/Flight 93 — none touched yet.
- Audit of the Commission's own independence: Rice's MFR already incidentally revealed that Philip Zelikow (Executive Director) co-authored an academic book with the witness in 1995. A systematic check of declared/undeclared conflicts of interest between Commission staff and Executive Branch witnesses is warranted.

## Execution rule

Every new phase must follow this same pattern: record the full title, author, event date, document date, declassification date, URL, version, extent actually read, redactions, and access limitations — before any conclusion. No document is cited as "read" if only its summary, FAQ, press release, or a search snippet was consulted.

And the framing rule that applies across every phase: access restriction, generic warning, and interested testimony are not proof of cover-up or of prior knowledge. Process failure, institutional self-protection, deliberate suppression, and prior operational knowledge are four distinct propositions, each with its own burden of proof. See also the impartiality rule in [`README.md`](README.md): no hypothesis, official or alternative, receives a presumption of truth or falsity, and an evidentiary gap is never itself treated as proof of any hypothesis.
