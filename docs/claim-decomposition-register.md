# Claim Decomposition Register

> Working register of atomic propositions extracted from official and alternative claims. Field definitions, status vocabulary and application rules are in [`04-methodology-symmetric-skepticism.md`](04-methodology-symmetric-skepticism.md) §4, which governs this file.

**Created: 19 September 2026.** Empty of substantive entries at creation. Populated only by phases that read primary sources.

---

## 1. Scope

This register holds **atomic propositions** — statements that can be true or false independently of the others in their set. A statement that can be half-true has not yet been decomposed.

It covers both directions:

- **Official-account propositions**, decomposed under the Official Account Stress-Test Track (see [`../NEXT-STEPS.md`](../NEXT-STEPS.md)). H0 is never scored as a unit; it exists here as its constituent propositions.
- **Alternative-account propositions** (H1–H7), decomposed with the same twelve fields and judged by the same status vocabulary.

---

## 2. Status vocabulary (closed)

`unsupported statement` · `document cited, not located` · `document located, not read` · `partially corroborated` · `corroborated` · `contradicted` · `inconclusive`

- `corroborated` requires a source independent of the claimant, read in full.
- `contradicted` requires the contradicting source to have been read in full.
- Tension between two sources not read in parallel is `inconclusive`, never `contradicted`.
- These rules apply identically to official and alternative propositions.

---

## 3. Entry template

Copy verbatim for each new entry.

```
### C-<nnn> — <short label>

| Field | Value |
|---|---|
| C1 Exact claim | |
| C2 Institution / witness | |
| C3 Source · event date · document date · declassification date | |
| C4 Source character | contemporaneous / retrospective / sworn / technical / secondary |
| C5 Revisions, retractions, conflicting accounts | |
| C6 Required assumptions | |
| C7 Supporting evidence (with read status) | |
| C8 Contradicting or weakening evidence (with read status) | |
| C9 Plausible non-conspiratorial explanations | |
| C10 Plausible alternative explanations (mapped to H1–H7) | |
| C11 Single most discriminating missing document / test / data point | |
| C12 Status | |
| Side | official / alternative |
| Workstream | ST-1 … ST-7 |
| Linked anomalies | A-<id>, … |
| Opened | |
| Last reviewed | |
```

---

## 4. Index

No entries yet.

| ID | Short label | Side | Workstream | Source character | Status | Opened |
|---|---|---|---|---|---|---|
| — | *(empty at creation)* | — | — | — | — | — |

---

## 5. Entries

*(none)*

---

## 6. Migration of the Phase 2A claim table

[`03-phase2a-mfr-verification.md`](03-phase2a-mfr-verification.md) §5.1 holds sixteen claims (A1–A16) already classified under the earlier eight-column instrument. Those rows are **retained unchanged in `03`** and are migrated into this register field by field when Phase 2A executes.

Migration rules:

1. **No status changes on migration.** A row's status may change only when a document that moves it has been read in full. Migration is a change of form, not of finding.
2. The eight existing columns map onto C1, C2, C4 (sworn), C3/C7 (cited contemporaneous document), C7 (located/read), C7 (independent corroboration) and C12.
3. The four new fields — C6 (assumptions), C9 (non-conspiratorial explanations), C10 (alternative explanations), C11 (most discriminating missing item) — are filled at migration time from the material already read. Where the material read does not support filling a field, it reads `not determined`.
4. Identifier continuity is preserved: A1 → `C-001`, A2 → `C-002`, … A16 → `C-016`, with the old identifier recorded in the short label. Note that `A-<nnn>` identifiers in the **anomaly** register are a separate series and do not correspond to the old `A1`–`A16` claim labels.
