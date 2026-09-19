# Version-History Ledger

> Living instrument. Governed by [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) §4 and §11.
> Opened 19 September 2026.

Two things are tracked here and must not be confused:

- **§2 — Version ledgers for external claims.** How an official or critical claim's wording changed across bodies, publications, hearings, drafts, testimony, declassifications and time.
- **§3 — Change events in this repository.** Every status change this project makes to its own rows, with what moved it.

---

## 1. Fields for an external version ledger

| Field | Meaning |
|---|---|
| Version | Sequential, per claim |
| Date | Of the statement, not of its release |
| Body / person | Never merged into "the government" |
| Wording | Verbatim where available |
| Certainty expressed | Hedged / asserted / declined to state |
| Source attributed | What the statement cites |
| Change from previous | Addition, removal, narrowing, expansion, change of attributed source |
| New evidence offered for the change | Named, or `none disclosed` |
| Formally corrected? | Yes / no / partially |
| Substantive or scope? | Whether an apparent contradiction is a real conflict or a difference of scope |

> **Watch condition.** Flag every instance of **uncertainty later converted into certainty without new disclosed evidence.** It is the single most common way a synthesized narrative hardens.

---

## 2. Version ledgers

### VL-001 — The probability of success of the May 1998 capture operation

| V | Date | Who | Wording | Certainty | Source attributed | Change | New evidence | Scope or substance |
|---|---|---|---|---|---|---|---|---|
| 1 | 11 Dec 2003 | Scheuer (sworn), DOC-3 | 30% conveyed to Berger, Reno, Freeh, Clarke; 0% to Mary Jo White | Asserted | Report of a call from Fitzgerald and others | — | — | — |
| 2 | 22 Jan 2004 | Tenet (sworn), DOC-7 p.3 | "the operation's prospect of success as described to him was less than 30% (the figure agreed upon [REDACTED])" | Asserted, but hedged as what was *described to him* | Redacted | Number narrowed from "30%" to "less than 30%"; direction of flow changed from outward-briefing to inward-description | None disclosed | **Scope**, primarily — see [DISC-002](discrepancies.md#disc-002) |

**Open:** whether any 2004 Commission publication restated either figure, and with what hedging. The 9/11 Commission Report has not been read in this project.

### VL-002 — Why the May 1998 capture operation was cancelled

| V | Date | Who | Wording | Certainty | Source attributed | Change | New evidence |
|---|---|---|---|---|---|---|---|
| 1 | 11 Dec 2003 | Scheuer (sworn), DOC-3 | Among the reasons was a Saudi offer to resolve the UBL case themselves | Stated as the witness's **belief** | None | — | — |
| 2 | 22 Jan 2004 | Tenet (sworn), DOC-7 p.3–4 | Cancelled on "the strong and unanimous recommendation" of DDO Downing, C/CTC O'Connell and C/NE [REDACTED], for "operational impediments and the risk of collateral damage"; the May 1998 Saudi trip was "entirely unrelated" | Asserted | The three officers' recommendation — **which he does not recall being memorialized** | Reason changed entirely; a diplomatic factor replaced by an operational one | None disclosed |

**Watch flag raised.** Version 2 states an operational rationale with high certainty while the same passage concedes that no memorandum of it is recalled to exist. That is an assertion whose supporting record the asserter cannot confirm — the profile of a claim that hardens on repetition. Recorded now so that any later, firmer restatement can be measured against it.

### VL-003 — Rice, "all of the reporting pointed abroad"

| V | Date | Who | Wording | Certainty | Change |
|---|---|---|---|---|---|
| 1 | May 2002 | Rice, public press conference | No one could have predicted the use of planes as missiles | Asserted, absolute | — |
| 2 | 7 Feb 2004 | Rice, DOC-2 (not under oath) | She misspoke; should have said *she* could not have imagined it; there was no stream of reporting on attacks inside the US — all pointed abroad | Retraction of V1's scope; new absolute on the reporting stream | Narrowing on one proposition, **new absolute introduced on another** |
| 3 | 9 Feb 2004 | PDB Review Team, DOC-1 | 24 core-group articles concerning attacks in the US and/or aircraft, within a 353-article corpus | Institutional, quantified | In tension with V2's second absolute |

**Note.** The V1 transcript has still not been read in this project (A8.1). A version ledger built on a paraphrase of V1 is provisional.

### VL-004 — This project's own framing of H1 and H5

Recorded because the project's own wording is subject to the same discipline as its sources.

| V | Date | Document | H1 | H5 |
|---|---|---|---|---|
| 1 | 17 Sep 2026 | [`../docs/02`](../docs/02-adversarial-audit-phase1.md) | "H1 reforçada… mais provável que não" | "Improvável no que foi lido; não testado onde importa" |
| 2 | 19 Sep 2026 | [`../docs/03` §1.2, §1.3](../docs/03-phase2a-mfr-verification.md) | Documented bureaucratic failure and possible institutional self-protection; deliberate suppression **not** corroborated | No positive evidence in this tranche; **untested** at the al-Mihdhar/al-Hazmi node |
| 3 | 19 Sep 2026 | this commit | **unchanged** | **unchanged** |

**V3 note.** Reading DOC-7 did not change H0–H7. Per MD-009, this commit makes no substantive conclusions. DOC-7 contains no material on the al-Mihdhar/al-Hazmi node at all (T-N1), so H5 could not have been tested by it even in principle.

---

## 3. Change events in this repository

Every row change carries: date, row, old value, new value, the document that moved it, and whether that document was image-verified.

| Date | Row | Old | New | Moved by | Image-verified |
|---|---|---|---|---|---|
| 19 Sep 2026 | A1.2 | `documento citado, não localizado` | `inconclusiva` | DOC-7 pp. 1, 16 | no (text layer) |
| 19 Sep 2026 | A3.1 | `declaração não corroborada` | `parcialmente corroborada` | DOC-7 p.3 | **yes** |
| 19 Sep 2026 | A3.2 | `declaração não corroborada` | `inconclusiva` | DOC-7 p.4 | **yes** |
| 19 Sep 2026 | A4.1 | `documento citado, não localizado` | `parcialmente corroborada` | DOC-7 p.5 | **yes** |
| 19 Sep 2026 | A4.2 | `documento citado, não localizado` | `contradita` (absolute form only) | DOC-7 p.5 | **yes** |
| 19 Sep 2026 | A4.5 | — (new row) | `parcialmente corroborada` | DOC-7 p.5 | **yes** |
| 19 Sep 2026 | A5.1 | `declaração não corroborada` | `parcialmente corroborada` | DOC-7 p.4 | **yes** |
| 19 Sep 2026 | A5.2 | `declaração não corroborada` | `contradita` | DOC-7 p.4 | **yes** |
| 19 Sep 2026 | A7.2 | `declaração não corroborada` (container) | `inconclusiva` | DOC-7 p.12 | no (text layer) — **flagged for verification** |
| 19 Sep 2026 | A14.1 | `declaração não corroborada` | `parcialmente corroborada` | DOC-7 p.5 | **yes** |
| 19 Sep 2026 | A15.1–A15.4 | `corroborada` | `corroborada` + `independence: none (self-description)` | MD-002, no new document | n/a |
| 19 Sep 2026 | T-01 … T-13, T-N1 | — (new rows) | see [`claims.md`](claims.md) §5 | DOC-7 | partial |
| 19 Sep 2026 | H0–H7 | — | **unchanged** | — | — |

### 3.1 Access-state change events

| Date | Event | Evidence |
|---|---|---|
| 19 Sep 2026, earlier session | All primary repositories blocked by network egress policy (403 on CONNECT) | [`../docs/03` §3](../docs/03-phase2a-mfr-verification.md) |
| 19 Sep 2026, this session | **Access restored.** `www.archives.gov` and `www.intelligence.senate.gov` both returned HTTP 200 | Recorded in [`../SOURCES.md`](../SOURCES.md) and [`cards/DOC-7-mfr-tenet-2.md`](cards/DOC-7-mfr-tenet-2.md) §1 |

The earlier failure record is **preserved, not overwritten**. It is an accurate record of that session's ceiling.

### 3.2 Corrections to earlier repository statements

| Date | Statement corrected | Correction |
|---|---|---|
| 19 Sep 2026 | [`../docs/03` §8](../docs/03-phase2a-mfr-verification.md): "Phase 2A resumes when there is read access to `archives.gov`" | The condition is met. Phase 2A is now open and in progress, beginning with DOC-7 |
| 19 Sep 2026 | [`../docs/02` §1.1](../docs/02-adversarial-audit-phase1.md) records DOC-1's OCR as poor with sense "reconstructed by context" | Under [`../docs/04` §7.2](../docs/04-controlling-methodology.md) this is no longer sufficient for a decisive quotation. DOC-1 must be re-carded. Its Phase A text is **not** altered |
