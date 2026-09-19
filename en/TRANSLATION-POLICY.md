# Translation Policy and Companion Index

> Opened 19 September 2026 under [`../docs/04-controlling-methodology.md`](../docs/04-controlling-methodology.md) §11 (MD-003, as amended by MD-013).

---

## 1. What the `en/` directory is

Phase A of this audit was written in Portuguese. Those documents are the **historical record** of how the audit actually proceeded, including its errors and their corrections. Translating them in place, or replacing them, would destroy that record.

The `en/` directory therefore holds **faithful, complete English companion versions** of every Portuguese project document. Each companion:

- is a translation of the whole source document, not a summary, abridgement or rewrite;
- carries a header identifying its source file, the source's SHA-256 at translation time, and the translation date;
- links back to the preserved original;
- preserves the source's structure, section numbering, tables, classifications and hedging exactly.

## 2. Precedence rule (MD-013)

> **The Portuguese original is the authoritative record. The English companion is a reader's translation of it.**

Where a companion and its original disagree, the disagreement is a **translation defect**, to be corrected in the companion — never in the original. This is the opposite of the precedence rule that governs `docs/NN-*.md`, where a higher-numbered document supersedes a lower one; a translation supersedes nothing.

**All new GitHub-facing content is written in English.** New artifacts (`docs/04`, `docs/05`, `registry/`, `corpus/`, `en/`) are English-native and have no Portuguese counterpart.

## 3. Drift detection

The source SHA-256 recorded in each companion header is the hash at the moment of translation. If a source file's current hash differs from the hash recorded in its companion, the companion is **stale** and says so until re-translated. Verify with:

```
sha256sum README.md SOURCES.md NEXT-STEPS.md docs/0[123]-*.md
```

and compare against §4.

## 4. Companion index

| Source (Portuguese, authoritative) | Companion (English) | Source SHA-256 at translation | Status |
|---|---|---|---|
| [`../README.md`](../README.md) | [`README.en.md`](README.en.md) | `f3974518c00feb978acd984937631868356dcd2adb90874c2dbe610e7552a024` | complete |
| [`../SOURCES.md`](../SOURCES.md) | [`SOURCES.en.md`](SOURCES.en.md) | `304e8751b053397fe07d1683a13daa7f0d1b3ed025896831ab74e908eeac57e2` | complete |
| [`../NEXT-STEPS.md`](../NEXT-STEPS.md) | [`NEXT-STEPS.en.md`](NEXT-STEPS.en.md) | `51c25af31ec60d3dadffb23788043a376242207874341c45a14bf2cebcaf6145` | complete |
| [`../docs/01-wtc-engineering-audit-v1.md`](../docs/01-wtc-engineering-audit-v1.md) | [`docs/01-wtc-engineering-audit-v1.en.md`](docs/01-wtc-engineering-audit-v1.en.md) | `bcb012dff03a31028fa06f84e186a5014a65b904dc8c0a81d671da52c1f93ce0` | complete |
| [`../docs/02-adversarial-audit-phase1.md`](../docs/02-adversarial-audit-phase1.md) | [`docs/02-adversarial-audit-phase1.en.md`](docs/02-adversarial-audit-phase1.en.md) | `45b77e3d798d85b8fe86ed16f0372896c79e3745bac4776f51ce366ca2d58d88` | complete |
| [`../docs/03-phase2a-mfr-verification.md`](../docs/03-phase2a-mfr-verification.md) | [`docs/03-phase2a-mfr-verification.en.md`](docs/03-phase2a-mfr-verification.en.md) | `7a224700bb637d392038c4079136b95c911a48f0a26ce760fb40f9cd639cd81a` | complete |

**Navigation banner.** Each Portuguese source carries one added line at the top: an English pointer to its companion. That line is the **only** modification made to a Phase A document by the translation work, it is additive, it deletes nothing, and it is navigation rather than content — so it is not reproduced in the companion bodies. The hashes above are of the sources **including** the banner, so drift detection works against the current files.

## 5. Translation conventions

| Portuguese | English | Note |
|---|---|---|
| `comprovado` | proven | Confidence scale — the source's own term, translated, not reinterpreted |
| `fortemente sustentado` | strongly supported | |
| `mais provável que não` | more likely than not | |
| `plausível` | plausible | |
| `genuinamente não resolvido` | genuinely unresolved | |
| `improvável` | unlikely | |
| `contradito` | contradicted | |
| `não testável com o registro público` | not testable on the public record | |
| `declaração não corroborada` etc. | **left untranslated in the claim registry** | The closed status vocabulary is an identifier, not prose. Translating the tokens would break comparability with `docs/03` §5. Glossed in [`../registry/claims.md`](../registry/claims.md) §2 |
| `sob juramento` | see §6 | Not translated mechanically — see the evidentiary-wording rule |

Where the source hedges ("indícios", "tensão não resolvida", "não estabelecido"), the companion hedges identically. Where the source is wrong and later corrected, the companion reproduces both the error and the correction, in place.

## 6. Evidentiary wording in translation (MD-012)

`sob juramento` is **not** rendered as "under oath" by default. Every occurrence is resolved against the witness-status register in [`../registry/witness-status.md`](../registry/witness-status.md), and rendered with the label that register assigns to that document. Where procedural status is not established by the source or a directly linked procedural record, the companion uses **"Commission interview record"** or **"interview memorandum"**.

This is the one place where a companion does not mirror the source word-for-word, and it is deliberate: the Portuguese source's `sob juramento` is a claim about procedural status, and the governing methodology now requires that claim to be substantiated per document. Every such rendering carries a footnote pointing at the register.
