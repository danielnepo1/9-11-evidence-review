# 9/11 Evidence Review

> Adversarial, document-based audit of the official 9/11 narrative — WTC structural engineering and pre-9/11 intelligence timeline, primary sources cited.

A systematic review of primary sources (NIST, the 9/11 Commission, CIA, NARA) across two tracks: (1) the physical plausibility of the Twin Towers and WTC 7 collapses, and (2) pre-9/11 intelligence failures. Method: steelman the official account → challenge it with primary evidence → judge without a fixed prior conclusion. Every claim is tagged with a confidence level, and every source is logged with access date, extent read, and known limitations.

---

## Sobre este projeto

Este repositório documenta uma auditoria em andamento, feita em duas passagens, sobre a narrativa oficial dos ataques de 11 de setembro de 2001. O objetivo não é confirmar nem refutar a versão oficial, mas submetê-la — e às hipóteses alternativas — ao mesmo padrão probatório, com rastreabilidade total de fontes.

**Padrão de honestidade adotado:** nenhuma conclusão é apresentada sem indicar se o documento subjacente foi lido integralmente, parcialmente, ou apenas conhecido por resumo/FAQ/press release. Quando isso não foi possível dentro de uma sessão, o repositório registra isso explicitamente em vez de preencher a lacuna com conhecimento prévio não verificado.

## Estrutura

```
9-11-evidence-review/
├── README.md                              ← este arquivo
├── docs/
│   ├── 01-wtc-engineering-audit-v1.md     ← primeira auditoria (engenharia estrutural do WTC)
│   └── 02-adversarial-audit-phase1.md     ← segunda auditoria (adversarial, multi-hipótese, Fase 1)
├── SOURCES.md                             ← bibliografia consolidada de ambas as auditorias
└── NEXT-STEPS.md                          ← roteiro das próximas fases (2A, 2B, 3, 4)
```

### Ordem de leitura

A numeração dos documentos é cronológica **e** hierárquica: cada documento posterior corrige o anterior, e onde houver conflito **prevalece sempre o de número maior**.

| Ordem | Arquivo | Papel | Como ler |
|---|---|---|---|
| 1 | [`README.md`](README.md) | Método, hipóteses H0–H7, escala de confiança | Ponto de entrada — define o vocabulário usado nos demais |
| 2 | [`docs/01-wtc-engineering-audit-v1.md`](docs/01-wtc-engineering-audit-v1.md) | Primeiro passe, engenharia | **Registro histórico.** Não citar isoladamente: vários pontos foram retratados |
| 3 | [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md) | Estado atual da auditoria | Seção 2 lista o que foi retratado de `01`; seções 3–6 são o achado substantivo |
| 4 | [`SOURCES.md`](SOURCES.md) | Bibliografia consolidada com status de leitura | Consultar antes de atribuir peso a qualquer afirmação |
| 5 | [`NEXT-STEPS.md`](NEXT-STEPS.md) | Roteiro de execução (Fases 2A, 2B, 3, 4) | Ponto de partida de qualquer sessão nova |

**Referência vs. próximo passo:** os itens 1–4 são material de **referência** (o que já está estabelecido e com que lastro); o item 5 é a fila de **execução**. Uma sessão nova começa lendo 1, 3 e 5 — o `01` só é necessário quando o trabalho tocar engenharia estrutural, e nesse caso sempre junto da seção 2 do `02`.

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

### Classificações de confiança usadas

`comprovado` · `fortemente sustentado` · `mais provável que não` · `plausível` · `genuinamente não resolvido` · `improvável` · `contradito` · `não testável com o registro público`

Evita-se deliberadamente a frase genérica "sem evidência" em favor de formulações mais precisas: evidência insuficiente, evidência indireta, evidência contestada, documento indisponível, ausência de teste, resultado não replicável.

## Status atual

- ✅ **Fase 1 — Auditoria técnica v1** (`docs/01`): análise energética e cinética do colapso das Torres e do WTC 7 a partir das FAQs técnicas do NIST e de literatura revisada por pares (Bažant & Verdure, Bažant & Le). Identificadas limitações metodológicas próprias na revisão seguinte.
- ✅ **Fase 2, primeira tranche — Auditoria adversarial documental** (`docs/02`): correção explícita das limitações da Fase 1; leitura integral de três documentos primários desclassificados em setembro de 2026 (PDB Review Team memo, MFRs de Condoleezza Rice e Michael Scheuer); primeira matriz H0–H7; primeiro ledger de contradições.
- ⏳ **Próximas fases**: ver [`NEXT-STEPS.md`](NEXT-STEPS.md).

## Limitações reconhecidas (leia antes de citar este material)

- Nenhuma fonte de mais de algumas dezenas de páginas foi lida integralmente até o momento — isso inclui o relatório completo da Comissão do 11/9, os volumes NCSTAR do NIST, o relatório Hulsey/UAF e os exhibits do caso Moussaoui.
- Vários dos 71 PDBs liberados pela CIA em setembro de 2026 são digitalizações sem camada de texto pesquisável e não puderam ser lidos nesta fase.
- Conclusões sobre H2, H3, H6 e H7 permanecem em grande parte não testadas pelos documentos lidos até agora.

## Licença de uso do conteúdo

Este material é uma análise original produzida para fins de pesquisa pessoal. Citações de fontes governamentais e acadêmicas seguem os links diretos listados em [`SOURCES.md`](SOURCES.md); nenhum trecho extenso de terceiros é reproduzido — apenas paráfrase com atribuição.
