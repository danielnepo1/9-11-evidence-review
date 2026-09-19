# Registry — Living Instruments

These are **living instruments**, not chronological documents. Unlike `docs/NN-*.md`, which are dated and superseded in sequence, the files here are updated in place and record their own change events.

| File | Purpose | Governed by |
|---|---|---|
| [`claims.md`](claims.md) | Atomic claim registry — every material proposition, its evidence, provenance root, competing explanations and closure conditions | [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) §2, §5 |
| [`provenance.md`](provenance.md) | Provenance and source-independence graph — claim → publishing document → cited source → earliest recoverable source | `04` §3 |
| [`version-history.md`](version-history.md) | Chronological version ledger of official wording, and the change-event log for this repository's own reclassifications | `04` §4, §11 |
| [`discrepancies.md`](discrepancies.md) | Discrepancy ledger and the closed taxonomy | `04` §6 |
| [`source-policy.md`](source-policy.md) | Source inclusion, provenance, preservation and deduplication rules — **gate** on any corpus expansion | `04` §10 |
| [`witness-status.md`](witness-status.md) | Procedural status per witness document — what may and may not be called testimony under oath | `04` §7.4 |
| [`instruments-b1-b2.md`](instruments-b1-b2.md) | B1 quarantine record; B2-ref / B2-rely definitions and subtypes | `04` §8 |
| [`cards/`](cards/) | Document cards — one per document read, with the required fields for decisive quotations | `04` §7 |

## Change-event discipline

No row is silently overwritten. A status change requires a dated entry in [`version-history.md`](version-history.md) §3 naming: the row, the old value, the new value, the document that moved it, and whether that document was image-verified.

## ID namespaces

| Prefix | Meaning | Allocated |
|---|---|---|
| `DOC-n` | Document read or verified | DOC-1 … DOC-8 |
| `A<n>` | Phase A legacy claim container (from [`../docs/03`](../docs/03-phase2a-mfr-verification.md) §5) | A1 … A16 |
| `A<n>.<k>` | Atomic proposition inside a legacy container | see [`claims.md`](claims.md) |
| `T-<nn>` | Claim first recorded from DOC-7 (MFR Tenet #2) | T-01 … T-13, T-N1 |
| `U-<nn>` | Claim first recorded from DOC-8 (MFR Tenet #3) | U-01 … U-18, U-N1, U-N2 |
| `C-<nn>` | Critical / alternative claim | **none yet** — gated, see [`../docs/05-phase-c-competing-narratives.md`](../docs/05-phase-c-competing-narratives.md) §4 |
| `DISC-<nnn>` | Discrepancy ledger row | DISC-001 … DISC-011 |
| `PR-<nnn>` | Provenance chain | PR-001 … PR-013 |
| `EC1`–`EC5` | Explanation class (never `H1`–`H5` — see `04` MD-001) | fixed |

**Prefix allocation rule.** Claim prefixes are assigned **per source document**, one letter each, in reading order: `T` = DOC-7, `U` = DOC-8, then `V`, `W`, … for DOC-9 onward. `A` is reserved for the Phase A legacy containers and `C` for critical/alternative claims; neither is reallocated.
| `MD-<nnn>` | Methodological decision | MD-001 … MD-014 |
