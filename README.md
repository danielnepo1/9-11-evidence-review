# 9/11 Evidence Review

> Adversarial, document-based audit of the official 9/11 narrative — WTC structural engineering and pre-9/11 intelligence timeline, primary sources cited.

A systematic review of primary sources (NIST, the 9/11 Commission, CIA, NARA) across two tracks: (1) the physical plausibility of the Twin Towers and WTC 7 collapses, and (2) pre-9/11 intelligence failures. Method: steelman the official account → challenge it with primary evidence → judge without a fixed prior conclusion. Every claim is tagged with a confidence level, and every source is logged with access date, extent read, and known limitations.

---

---

## ⚠️ Controlling framework (added 19 September 2026)

**The methodology of this project changed on 19 September 2026.** A permanent framework for provenance, source independence, competing-hypothesis testing and symmetric treatment of official and alternative narratives was adopted and now governs everything below.

**Read these first. Where they conflict with anything else in this repository, they prevail.**

| Document | What it is |
|---|---|
| [`docs/04-controlling-methodology.md`](docs/04-controlling-methodology.md) | **Controlling methodology.** The baseline axiom, the three workstreams, explanation classes EC1–EC5, closure gates, document-card language, preservation and language rules, and the register of methodological decisions MD-001 … MD-010 |
| [`docs/05-phase-c-competing-narratives.md`](docs/05-phase-c-competing-narratives.md) | **Phase C — Competing Narratives and Independent Evidence.** Runs across Phases 2A–4, not after them |
| [`registry/`](registry/) | The living instruments: atomic claim registry, provenance graph, version-history ledger, discrepancy ledger, source policy, B1/B2 instruments, document cards |
| [`corpus/manifest.md`](corpus/manifest.md) | Retrieved artifacts, hashes, extraction tooling |

Two rules from that framework that change how everything already in this README should be read:

1. **Reading official documents establishes the baseline. It cannot independently validate the baseline.** A claim appearing in an official document is thereby established as *officially asserted*, not as true. Corroboration requires a source whose provenance root is independent — and repeated publications sharing one root are not independent.
2. **Equal procedural treatment; evidentiary weight proportional to provenance, independence, contemporaneity, auditability and corroboration.** Alternative and critical claims are held to exactly this standard — no lower, and no higher.

**Language.** All artifacts added from 19 September 2026 onward are written in English. The Portuguese documents (`01`–`03`, this README, `SOURCES.md`, `NEXT-STEPS.md`) are **preserved verbatim as the Phase A historical record** and are not translated or rewritten: see [`docs/04` MD-003](docs/04-controlling-methodology.md).

**Status of the hypotheses.** H0–H7 are **unchanged** by the adoption of this framework. Building the instrument is not evidence (MD-009).

## Sobre este projeto

Este repositório documenta uma auditoria em andamento, feita em duas passagens, sobre a narrativa oficial dos ataques de 11 de setembro de 2001. O objetivo não é confirmar nem refutar a versão oficial, mas submetê-la — e às hipóteses alternativas — ao mesmo padrão probatório, com rastreabilidade total de fontes.

**Padrão de honestidade adotado:** nenhuma conclusão é apresentada sem indicar se o documento subjacente foi lido integralmente, parcialmente, ou apenas conhecido por resumo/FAQ/press release. Quando isso não foi possível dentro de uma sessão, o repositório registra isso explicitamente em vez de preencher a lacuna com conhecimento prévio não verificado.

## Estrutura

```
9-11-evidence-review/
├── README.md                              ← este arquivo
├── docs/
│   ├── 01-wtc-engineering-audit-v1.md     ← primeira auditoria (engenharia estrutural do WTC)
│   ├── 02-adversarial-audit-phase1.md     ← segunda auditoria (adversarial, multi-hipótese, Fase 1)
│   ├── 03-phase2a-mfr-verification.md     ← correção de enquadramento + instrumento de verificação (Fase 2A)
│   ├── 04-controlling-methodology.md      ← CONTROLLING framework (EN, 19/09/2026) — prevalece sobre tudo
│   └── 05-phase-c-competing-narratives.md ← Phase C: Competing Narratives and Independent Evidence (EN)
├── registry/                              ← living instruments (EN)
│   ├── claims.md                          ← atomic claim registry (A<n>.<k>, T-nn, C-nn)
│   ├── provenance.md                      ← provenance / source-independence graph
│   ├── version-history.md                 ← version ledger + repository change events
│   ├── discrepancies.md                   ← discrepancy ledger + controlled taxonomy
│   ├── source-policy.md                   ← inclusion / provenance / preservation / dedup rules
│   ├── instruments-b1-b2.md               ← B1 quarantine; B2-ref / B2-rely
│   └── cards/                             ← document cards (DOC-n)
├── corpus/
│   ├── manifest.md                        ← retrieved artifacts, hashes, extraction tooling
│   └── text/                              ← preserved extracted text
├── SOURCES.md                             ← bibliografia consolidada de ambas as auditorias
└── NEXT-STEPS.md                          ← roteiro das próximas fases (2A, 2B, 3, 4)
```

### Ordem de leitura

A numeração dos documentos é cronológica **e** hierárquica: cada documento posterior corrige o anterior, e onde houver conflito **prevalece sempre o de número maior**.

| Ordem | Arquivo | Papel | Como ler |
|---|---|---|---|
| 1 | [`README.md`](README.md) | Método, hipóteses H0–H7, escala de confiança | Ponto de entrada — define o vocabulário usado nos demais |
| 2 | [`docs/01-wtc-engineering-audit-v1.md`](docs/01-wtc-engineering-audit-v1.md) | Primeiro passe, engenharia | **Registro histórico.** Não citar isoladamente: vários pontos foram retratados |
| 3 | [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md) | Fase 1 documental | Seção 2 lista o que foi retratado de `01`; seções 3–6 são o achado substantivo. **Ler já com as correções de `03` §1** |
| 4 | [`docs/03-phase2a-mfr-verification.md`](docs/03-phase2a-mfr-verification.md) | **Enquadramento vigente + instrumento de verificação** | §1 corrige cinco formulações de `02`; §5 é a tabela de status alegação-a-alegação; §7 é o estado corrente de H1–H5 |
| 5 | [`SOURCES.md`](SOURCES.md) | Bibliografia consolidada com status de leitura | Consultar antes de atribuir peso a qualquer afirmação |
| 6 | [`NEXT-STEPS.md`](NEXT-STEPS.md) | Roteiro de execução (Fases 2A, 2B, 3, 4) | Ponto de partida de qualquer sessão nova |

**Referência vs. próximo passo:** os itens 1–5 são material de **referência** (o que já está estabelecido e com que lastro); o item 6 é a fila de **execução**. Uma sessão nova começa lendo 1, 4 e 6 — o `01` só é necessário quando o trabalho tocar engenharia estrutural, e nesse caso sempre junto da seção 2 do `02`; o `02` sempre lido com a errata de `03` §1 em mãos.

**Regra de precedência sobre enquadramento:** onde `02` e `03` divergirem na classificação de uma hipótese ou de uma alegação, **prevalece `03`**.

## Metodologia

A auditoria segue três passagens declaradas explicitamente:

1. **Steelman oficial** — construir a melhor versão possível da explicação oficial (NIST, Comissão do 11/9).
2. **Red team** — construir a crítica mais forte possível usando documentos primários, contradições internas e dados liberados posteriormente.
3. **Juiz** — comparar as duas sem partir de uma conclusão desejada.

### Hipóteses mantidas separadas

Para a dimensão de inteligência/resposta institucional, oito hipóteses são tratadas como categorias distintas, cada uma exigindo evidência própria (evidência de uma nunca é tratada automaticamente como evidência de outra):

| # | Hipótese |
|---|---|
| H0 | Ataque planejado pela al-Qaeda; falhas institucionais e explicação estrutural essencialmente corretas |
| H1 | H0 + autoproteção/declarações enganosas/encobrimento posterior de incompetência, sem conhecimento prévio operacional |
| H2 | H0 + apoio logístico consciente por indivíduos ligados a governo estrangeiro, sem prova de autorização superior |
| H3 | Apoio ou proteção institucional estrangeira mais ampla |
| H4 | Autoridades americanas tinham alertas suficientes, mas falharam por negligência/fragmentação/prioridades políticas |
| H5 | Segmentos de autoridades tinham conhecimento operacional específico e deliberadamente não impediram o ataque |
| H6 | O mecanismo de um ou mais colapsos foi significativamente diferente do apresentado pelo NIST |
| H7 | Intervenção deliberada adicional nos edifícios |

### Regra de enquadramento probatório

> Restrição de acesso, alerta genérico e testemunho interessado não são — isolados nem somados — prova de encobrimento ou de conhecimento prévio.

Três corolários de uso obrigatório:

1. **Documento novo ≠ fato novo.** Toda citação distingue **data do evento**, **data do documento** e **data da desclassificação**. Um registro de 2004 desclassificado em 2026 é memória de 2004, não registro contemporâneo de 2001.
2. **Cada degrau exige evidência própria.** Falha de processo → autoproteção institucional → supressão deliberada → conhecimento prévio operacional são quatro proposições distintas; evidência de uma nunca é promovida a evidência da seguinte.
3. **Leitura é leitura.** Resumo, FAQ, press release, trecho de busca e reportagem de terceiros não sustentam status `corroborada` nem `contradita`.

### Classificações de confiança usadas

`comprovado` · `fortemente sustentado` · `mais provável que não` · `plausível` · `genuinamente não resolvido` · `improvável` · `contradito` · `não testável com o registro público`

Evita-se deliberadamente a frase genérica "sem evidência" em favor de formulações mais precisas: evidência insuficiente, evidência indireta, evidência contestada, documento indisponível, ausência de teste, resultado não replicável.

Para alegações individuais de depoentes, a escala é outra e é fechada (ver [`docs/03`](docs/03-phase2a-mfr-verification.md) §5):

`declaração não corroborada` · `documento citado, não localizado` · `documento localizado, não lido` · `parcialmente corroborada` · `corroborada` · `contradita` · `inconclusiva`

## Status atual

- ✅ **Fase 1 — Auditoria técnica v1** (`docs/01`): análise energética e cinética do colapso das Torres e do WTC 7 a partir das FAQs técnicas do NIST e de literatura revisada por pares (Bažant & Verdure, Bažant & Le). Identificadas limitações metodológicas próprias na revisão seguinte.
- ✅ **Fase 2, primeira tranche — Auditoria adversarial documental** (`docs/02`): correção explícita das limitações da Fase 1; leitura integral de três documentos primários desclassificados em setembro de 2026 (PDB Review Team memo, MFRs de Condoleezza Rice e Michael Scheuer); primeira matriz H0–H7; primeiro ledger de contradições.
- ✅ **Correção de enquadramento + instrumento da Fase 2A** (`docs/03`): cinco formulações de `02` corrigidas (H1, H5, Rice "all reporting pointed abroad", estrutura de acesso da Comissão, regra das três datas); tabela de verificação alegação-a-alegação com 16 linhas classificadas; prioridades da Fase 2A pré-registradas.
- 🔄 **Fase 2A — em execução.** Acesso de rede restaurado em 19/09/2026 (`archives.gov` responde HTTP 200; o registro da falha anterior é preservado em [`docs/03` §3](docs/03-phase2a-mfr-verification.md)). **DOC-7 — MFR George Tenet #2 (22/01/2004) — lido integralmente (24/24 pp.) e fichado**, com verificação por imagem das pp. 3, 4, 5 e 19: [`registry/cards/DOC-7-mfr-tenet-2.md`](registry/cards/DOC-7-mfr-tenet-2.md). Restam oito MFRs.
- ✅ **Framework metodológico v2 + Fase C** (`docs/04`, `docs/05`, `registry/`, `corpus/`): ver o bloco no topo deste arquivo.
- ⛔ **Fase 2B — Part Four da Joint Inquiry: não executada.** Mesmo bloqueio (`intelligence.senate.gov`). Protocolo de classificação pré-registrado em [`docs/03` §6](docs/03-phase2a-mfr-verification.md).
- ⏳ **Próximas fases**: ver [`NEXT-STEPS.md`](NEXT-STEPS.md).

## Limitações reconhecidas (leia antes de citar este material)

- Nenhuma fonte de mais de algumas dezenas de páginas foi lida integralmente até o momento — isso inclui o relatório completo da Comissão do 11/9, os volumes NCSTAR do NIST, o relatório Hulsey/UAF e os exhibits do caso Moussaoui.
- Vários dos 71 PDBs liberados pela CIA em setembro de 2026 são digitalizações sem camada de texto pesquisável e não puderam ser lidos nesta fase.
- Conclusões sobre H2, H3, H6 e H7 permanecem em grande parte não testadas pelos documentos lidos até agora.
- **H5 não está testada.** O nó al-Mihdhar/al-Hazmi, onde a hipótese tem seu melhor caso teórico, não foi tocado por nenhuma fase até aqui.
- **H1 não sustenta "encobrimento".** O que há são indícios de falhas burocráticas e de possível autoproteção institucional; supressão deliberada não está corroborada.

## Licença de uso do conteúdo

Este material é uma análise original produzida para fins de pesquisa pessoal. Citações de fontes governamentais e acadêmicas seguem os links diretos listados em [`SOURCES.md`](SOURCES.md); nenhum trecho extenso de terceiros é reproduzido — apenas paráfrase com atribuição.
