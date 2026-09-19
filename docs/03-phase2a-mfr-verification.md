# Fase 2A — Correção de Enquadramento e Instrumento de Verificação dos MFRs

> Corrige formalmente o enquadramento de [`02-adversarial-audit-phase1.md`](02-adversarial-audit-phase1.md) e estabelece o instrumento de verificação alegação-a-alegação da liberação ISCAP 2026-201. **Execução da leitura dos nove MFRs restantes: não realizada nesta sessão por bloqueio de acesso de rede** — registrado na seção 3 com a evidência do teste.

Data desta sessão: **19 de setembro de 2026**. Escopo: H1–H5. H6 e H7 não são reavaliadas aqui.

---

## 1. Correções formais de enquadramento

Regra geral que passa a valer sobre todo o corpo da auditoria, retroativamente:

> **Restrição de acesso, alerta genérico e testemunho interessado não são — isolados nem somados — prova de encobrimento ou de conhecimento prévio.**

Cada um desses três tem um valor probatório próprio e limitado: restrição de acesso é fato sobre o *processo* de uma investigação; alerta genérico é evidência de que uma *categoria* de ameaça era conhecida; testemunho interessado é alegação que ganha peso com juramento e o perde com interesse. Nenhum se converte em prova de ato deliberado sem corroboração independente.

### 1.1 Regra das três datas

Toda citação documental nesta auditoria passa a distinguir obrigatoriamente:

| Data | O que é | Erro que evita |
|---|---|---|
| **Data do evento** | Quando ocorreu o fato relatado (reunião, decisão, relato de fonte) | Confundir o relato com o fato |
| **Data do documento** | Quando o registro foi produzido | Tratar memória reconstruída anos depois como registro contemporâneo |
| **Data da desclassificação** | Quando o registro se tornou público | **Tratar "documento novo" como "fato novo de 2001"** |

Aplicada aos três documentos lidos na Fase 1:

| Doc | Evento | Documento | Desclassificação | Distância evento → documento |
|---|---|---|---|---|
| DOC-1 — *Report on Review of PDB Articles* | PDBs de 1998 a 20/09/2001 (corpus revisado) | 09/02/2004 | 08/09/2026 | 2,5 a 6 anos |
| DOC-2 — MFR Condoleezza Rice | 07/02/2004 (a reunião); fatos relatados de 2000–2001 | 07/02/2004 (nota de trabalho) | 08/09/2026 | ~0 para a reunião; 2,5–4 anos para os fatos |
| DOC-3 — MFR Mike Scheuer | 11/12/2003 (o depoimento); fatos relatados de 1996–1999 | 11/12/2003 | 08/09/2026 | ~0 para o depoimento; 4–7 anos para os fatos |

**Consequência direta.** Nenhum dos três documentos é registro contemporâneo dos fatos de 1998–2001 que descreve. DOC-2 e DOC-3 são memória declarada com 2,5 a 7 anos de distância do fato; DOC-1 é uma síntese produzida em 2004 sobre documentos de 1998–2001. A desclassificação de 2026 tornou públicos **registros de 2003–2004**, não documentos operacionais de 2001. Onde o valor probatório depende de contemporaneidade — e nas prioridades 2, 3 e 6 abaixo depende —, o que importa é o documento contemporâneo *citado* dentro do depoimento, não o depoimento.

### 1.2 H1 — formulação substituída

| | |
|---|---|
| **Antes (Fase 1)** | "H1 reforçada, e mais cedo do que se supunha. […] Mais provável que não." |
| **Agora** | **"Existem indícios documentados de falhas burocráticas e possível autoproteção institucional; a alegação específica de supressão deliberada ainda não está corroborada."** |

Razão da troca: os dois pilares da formulação anterior não sustentam o peso que carregavam. O episódio do PDB de 25/03/1999 é alegação sob juramento de testemunha com interesse declarado, cujo memorando de apoio não foi localizado nem lido. A retratação de Rice é retratação de uma **frase pública**, não evidência de supressão de informação. E a estrutura de acesso aos PDBs é fato sobre o processo da Comissão em 2004 — posterior ao ataque, interno a uma investigação, e sem relação lógica com supressão em 1999–2001.

### 1.3 H5 — formulação substituída

| | |
|---|---|
| **Antes (Fase 1)** | "Improvável no que foi lido; não testado onde importa." |
| **Agora** | **"Nenhuma evidência positiva de H5 foi encontrada nesta tranche; ela permanece não testada no nó central al-Mihdhar/al-Hazmi."** |

Razão da troca: "improvável" é uma afirmação sobre probabilidade que exigiria ter examinado onde a hipótese tem seu melhor caso. Não foi examinado. A ausência de produto analítico consolidado descrita por Scheuer é evidência sobre o processo analítico da CIA no período que ele cobre — não é um teste de H5. Ausência de evidência positiva em documentos que não tratam do nó não é evidência de ausência.

### 1.4 Rice, "all of the reporting pointed abroad" — reclassificada

| | |
|---|---|
| **Antes (Fase 1)** | "Contradita na forma absoluta; defensável em leitura restrita ao verão de 2001." |
| **Agora** | **"Tensão documental não resolvida."** |

Fechar a questão em qualquer direção exige quatro itens, nenhum deles disponível nas fontes lidas:

1. **O PDB de 06/08/2001 integral** — o que existe no registro da auditoria é a descrição que a Comissão fez dele em DOC-1, não o texto. Um PDF sem camada de texto (registrado em `02`, DOC-6) não é leitura.
2. **A cronologia precisa do verão de 2001** — mês a mês, e não o agregado 1998–2001. A afirmação de Rice é plausivelmente sobre o *threat spike* de junho–agosto; o corpus de 353 artigos cobre três anos.
3. **A confiabilidade atribuída às fontes** — o próprio DOC-1 registra que vários relatos do core group vinham de fontes que a CIA classificava como "altamente questionáveis, não confiáveis", e que o PDB de 06/08/2001 trazia, em negrito no original, ressalva de não-corroboração. "Havia relatos" e "havia relatos que o serviço considerava confiáveis" são proposições diferentes.
4. **A distribuição real dos alertas entre doméstico e externo** — DOC-1 dá o recorte temático de 24 artigos, não a distribuição do corpus. Sem denominador, "o fluxo apontava para fora" não é testável.

### 1.5 Estrutura de acesso da Comissão — inferência retirada

| | |
|---|---|
| **Antes (Fase 1)** | "Nenhum comissário além de Kean e Hamilton, e nenhuma equipe temática, teve acesso direto ao corpus de PDBs […] a verificação independente por outros comissários era estruturalmente impossível." |
| **Agora** | **Comprovado** quanto à estrutura de acesso ao corpus de PDBs. **Não determinado** quanto ao acesso dos demais comissários a material derivado. **Não estabelecido** que a verificação independente fosse impossível. |

O memorando estabelece quantas pessoas viram os PDBs. Ele não estabelece o que as outras pessoas viram por outras vias. São quatro determinações distintas, todas pendentes — ver seção 4, prioridade 5.

---

## 2. O que esta sessão entregou e o que não entregou

| Item pedido | Estado |
|---|---|
| Correção formal do enquadramento (regras 1 a 5) | **Executado** — seção 1, aplicado retroativamente em `02` com marcações `[corrigido]` |
| Fase 2A — leitura integral dos nove MFRs restantes | **Não executado.** Bloqueio de acesso de rede, seção 3 |
| Fase 2A — tabela de verificação alegação-a-alegação | **Instrumento construído e populado** com as alegações dos documentos efetivamente lidos na Fase 1 (seção 5). As alegações de Clarke, Berger e Tenet não podem ser tabuladas: seus MFRs não foram lidos |
| Fase 2B — leitura integral da Part Four | **Não executado.** Mesmo bloqueio. Protocolo de classificação pré-registrado na seção 6 |
| Identificação nominal dos membros da Review Team | **Não determinado por fonte primária.** Pistas de fonte secundária registradas na seção 4, prioridade 5, explicitamente não promovidas a fato |

---

## 3. Teto de acesso desta sessão — registrado com a evidência

Todos os repositórios primários do escopo das Fases 2A e 2B estão inacessíveis a partir deste ambiente. O egresso de rede é intermediado por um proxy que negou a conexão (`CONNECT tunnel failed, response 403` / `connect_rejected — organization policy`) para **todos** os domínios testados:

| Domínio | Material do escopo | Resultado do teste (19/09/2026) |
|---|---|---|
| `www.archives.gov` | Os 9 MFRs restantes; índice ISCAP 2026-201; memo dos PDBs | ⚫ bloqueado (403 no CONNECT) |
| `transforming-classification.blogs.archives.gov` | Post do PIDB | ⚫ bloqueado |
| `www.intelligence.senate.gov` | Joint Inquiry, Part Four | ⚫ bloqueado |
| `www.govinfo.gov` | SSCI CRPT-113srpt288; 9/11 Commission Report | ⚫ bloqueado |
| `www.cia.gov` | Os 71 PDBs | ⚫ bloqueado |
| `vault.fbi.gov` | Material liberado sob EO 14040 | ⚫ bloqueado |
| `www.9-11commission.gov` / `govinfo.library.unt.edu` | Relatório e arquivo da Comissão | ⚫ bloqueado |
| `www.nist.gov` | NCSTAR (escopo da Fase 3) | ⚫ bloqueado |

O bloqueio não é seletivo por domínio: qualquer host externo testado foi recusado. O único canal externo disponível é **busca**, que retorna títulos e trechos de terceiros.

**Regra aplicada, sem exceção:** trecho de busca, resumo jornalístico ou página de terceiros **não** constitui leitura de documento primário e não pode ser fonte de nenhuma linha classificada como `corroborada` ou `contradita`. Onde uma pista de busca foi registrada nesta sessão, ela aparece marcada como pista não verificada e não altera o status de nenhuma alegação.

**Consequência para a auditoria:** a Fase 2A permanece aberta. O que foi produzido aqui é o instrumento de verificação e a correção de enquadramento — ambos pré-condição da leitura, não substituto dela.

---

## 4. Prioridades da Fase 2A — perguntas pré-registradas

Pré-registrar a pergunta antes de ler o documento é o que impede o ajuste a posteriori que a Fase 1 identificou como falha metodológica na auditoria `01`. Cada prioridade abaixo define **o que seria uma resposta positiva, uma negativa e uma inconclusiva** antes de qualquer leitura.

### Prioridade 1 — O nó al-Mihdhar/al-Hazmi

O ponto onde H5 tem seu melhor caso teórico e que continua **inteiramente não tocado**.

- **Alvos:** MFRs de Tenet (×3) e Clarke (×3); Scheuer #2 (06/01/2004) e #3 (11/03/2004); Joint Inquiry; relatórios do DOJ IG; PENTTBOM.
- **Pergunta:** quem soube, em que data, que al-Mihdhar tinha visto americano válido e que al-Hazmi havia entrado nos EUA; por que a informação não foi passada ao FBI ou incluída em watchlist entre janeiro de 2000 e agosto de 2001; e existe registro contemporâneo — não memória de 2003–2004 — de decisão de **reter** a informação.
- **Resposta positiva para H5:** documento contemporâneo mostrando decisão deliberada de não repassar, com autoria identificada e sem justificativa operacional declarada.
- **Resposta negativa:** registro contemporâneo de falha de processo (cabo não enviado, rascunho não aprovado, canal errado), ou justificativa operacional declarada na época.
- **Inconclusiva:** apenas memória declarada anos depois, sem documento contemporâneo localizado — que é o estado atual.

### Prioridade 2 — A discrepância 30% vs 0% (operação de captura, maio de 1998)

- **Alvos:** MFRs de Tenet e Berger; MFRs de Reno, Freeh, White e Fitzgerald (**não** integram a liberação de 2026 — localização pendente no acervo geral de MFRs do NARA).
- **Pergunta:** os dois números existem em registro contemporâneo, ou apenas na memória de Scheuer em dezembro de 2003? Quem comunicou qual estimativa a quem, e em que data?
- **Teste discriminante:** se Tenet ou Berger descrevem a mesma reunião com estimativa diferente de 30%, a alegação passa a `contradita` ou `parcialmente corroborada` conforme o detalhe; se nenhum dos dois menciona números, permanece `declaração não corroborada`.

### Prioridade 3 — O PDB de 25/03/1999 supostamente retido

- **Alvos:** o memorando citado por Scheuer; o autor do texto barrado, nomeado no MFR; MFRs de Tenet.
- **Armadilha metodológica a evitar:** o PDB publicado de 25/03/1999 — se estiver entre os 71 liberados — **não** pode confirmar nem refutar a alegação, porque a alegação é sobre um texto que teria sido *removido antes da publicação*. Um item ausente de um PDB é compatível tanto com "foi barrado" quanto com "nunca foi escrito". O teste real é o memorando interno e o depoimento do autor nomeado.
- **Status atual:** `documento citado, não localizado`.

### Prioridade 4 — O PDB de 06/08/2001

- **Alvo:** o PDF do PDB na página da CIA. Obstáculo técnico já documentado: digitalização sem camada de texto. Exige OCR — portanto, exige acesso ao arquivo.
- **Pergunta:** o texto integral sustenta a caracterização de Rice ("nenhuma informação corrente"; contato com a embaixada dos EAU como trote) ou a descrição da Comissão em DOC-1 (70 investigações de campo do FBI; CIA e FBI investigando o contato)?
- **Observação:** as duas coisas podem ser verdadeiras ao mesmo tempo. "Informação histórica, não corrente" e "há 70 investigações abertas" não se contradizem necessariamente. O teste é o texto.

### Prioridade 5 — A estrutura de acesso da Comissão aos PDBs

Quatro determinações distintas, todas pendentes:

| # | Determinação | Estado | Onde se resolve |
|---|---|---|---|
| 5a | Quem eram exatamente os **quatro** membros da Review Team | Não determinado. DOC-1 registra que incluía Presidente e Vice-Presidente; **não nomeia** os quatro | DOC-1 relido com atenção a assinaturas e lista de distribuição; correspondência Comissão–Casa Branca |
| 5b | Quem eram os **dois** da subcomissão com acesso ao corpus completo | Não determinado | Idem |
| 5c | Quais comissários e equipes temáticas tiveram acesso a **NID/SEIB, MFRs, briefings e documentos derivados** | Não determinado — e é isto que decide se a verificação independente era ou não possível | Atas e regras internas da Comissão; MFRs de equipes temáticas; acervo Kean/Hamilton |
| 5d | Se havia **mecanismo formal de compartilhamento** dos achados da Review Team com o plenário | Não determinado | Regimento interno da Comissão; o próprio DOC-1, que é formalmente um *report* — a quem foi endereçado? |

**Pista de fonte secundária, não verificada e não promovida a fato:** reportagem de época indica que o acordo com a Casa Branca previa um grupo restrito que faria o briefing do plenário, e menciona Philip Zelikow (Diretor Executivo) e a comissária Jamie Gorelick como os dois com acesso ampliado. Isto **não** foi confirmado em documento primário nesta sessão e é registrado apenas como direção de busca. Se confirmado, teria consequência direta: o acesso ampliado incluiria um comissário fora da dupla Kean/Hamilton e o Diretor Executivo — o que tornaria a formulação original da Fase 1 incorreta no nome, não apenas no escopo. Registre-se também que Zelikow é a mesma pessoa cujo conflito de interesse aparente com Rice (coautoria de livro em 1995) a Fase 1 identificou; se ele for um dos dois, isso é relevante para a auditoria de independência, e não para H5.

### Prioridade 6 — Interação CIA–FBI e a lacuna inteligência externa / investigação doméstica

- **Alvos:** MFRs de Tenet e Clarke; Joint Inquiry; relatórios do DOJ IG.
- **Pergunta:** a lacuna era (i) barreira jurídica ("the wall"), (ii) prática institucional além do que a barreira exigia, ou (iii) decisão caso a caso de reter? As três produzem o mesmo resultado observável e têm implicações completamente diferentes para H1, H4 e H5.
- **Por que importa:** esta é a distinção que separa H4 de H5 no caso concreto. Tratá-las como uma só foi o erro de categoria que a Fase 1 cometeu com as quatro hipóteses de demolição e que não deve se repetir aqui.

---

## 5. Instrumento de verificação alegação-a-alegação

Vocabulário de status fechado. Nenhum outro termo é admitido nesta coluna:

`declaração não corroborada` · `documento citado, não localizado` · `documento localizado, não lido` · `parcialmente corroborada` · `corroborada` · `contradita` · `inconclusiva`

Regras de aplicação:

- `corroborada` exige **fonte independente do depoente**, lida integralmente. Um depoente corroborando a si mesmo em outro depoimento não corrobora nada.
- `documento citado, não localizado` é o status padrão de toda alegação que se apoia em memorando, cabo ou relatório que a auditoria não localizou — mesmo sob juramento, mesmo com data e destinatário.
- `contradita` exige que a fonte contraditória tenha sido lida integralmente. Tensão entre duas descrições não lidas em paralelo é `inconclusiva`, não `contradita`.

### 5.1 Alegações dos documentos efetivamente lidos (Fase 1)

Todas as linhas abaixo derivam de DOC-1, DOC-2 e DOC-3, lidos integralmente em 17/09/2026. Nenhuma linha deriva de MFR não lido.

| # | Alegação | Quem a fez | Sob juramento? | Documento contemporâneo citado | Localizado? | Lido? | Corroboração independente | Status |
|---|---|---|---|---|---|---|---|---|
| A1 | Não houve produto analítico estratégico nem NIE sobre métodos de ataque de UBL até meados de 1999; pediu repetidamente | Scheuer | **Sim** | Memorando próprio de 28/06/1999 | Não | Não | Nenhuma (MFRs de Tenet e Clarke não lidos) | `documento citado, não localizado` |
| A2 | Texto sobre WMD barrado do PDB de 25/03/1999 por direção do DCI, para ocultar atraso de 2 anos no repasse do FBI | Scheuer | **Sim** | Memorando interno + autor do PDB nomeado no MFR | Não | Não | Nenhuma | `documento citado, não localizado` |
| A3 | Estimativa de 30% de sucesso informada a Berger, Reno, Freeh e Clarke; 0% informado a Mary Jo White | Scheuer | **Sim** | Nenhum documento; relato de ligação de Fitzgerald e outros | Não aplicável | Não | Nenhuma (MFRs de Tenet/Berger não lidos; MFRs de Reno, Freeh, White e Fitzgerald fora desta liberação) | `declaração não corroborada` |
| A4 | Sauditas sistematicamente não cooperativos; nunca forneceram informação útil; abrigo a Madani al-Tayyib | Scheuer | **Sim** | Memo próprio de 03/05/1996; Spot Report de 24/06/1997 | Não | Não | Nenhuma | `documento citado, não localizado` |
| A5 | Uma das razões do cancelamento da operação de maio/1998 foi oferta saudita de resolver o caso UBL por conta própria | Scheuer | **Sim** | Nenhum; declarado como crença do depoente | Não aplicável | Não | Nenhuma | `declaração não corroborada` |
| A6 | Não recordava o relato de 10/09/1998 sobre avião carregado de explosivos, mas aeronave-como-arma era conhecida no alvo UBL (caso Murad) | Scheuer | **Sim** | O próprio artigo de PDB de 10/09/1998 | Sim — indexado em DOC-1 | Não (PDB original não lido) | DOC-1 corrobora a **existência** do relato, não a recordação nem o caso Murad | `parcialmente corroborada` |
| A7 | Relação instrumental entre serviço paquistanês e UBL para treinamento é "too conspiratorial" | Scheuer | **Sim** | Nenhum | Não aplicável | Não | Nenhuma | `declaração não corroborada` |
| A8 | Expressou-se mal em maio/2002; deveria ter dito que *ela* não poderia ter imaginado aviões como mísseis; soube depois de relatos anteriores | Rice | **Não** (reunião, sem juramento registrado) | Transcrição da coletiva de maio/2002 | Não nesta sessão (documento público, localização trivial) | Não | O próprio MFR registra a retratação; a declaração original não foi lida no primário | `parcialmente corroborada` |
| A9 | Não havia fluxo de relatos sobre ataques dentro dos EUA; todos apontavam para fora | Rice | **Não** | Nenhum citado pela depoente | — | — | Tensão com DOC-1 (24 artigos do core group sobre ataques nos EUA e/ou aeronaves), mas sem os quatro itens da seção 1.4 | `inconclusiva` — tensão documental não resolvida |
| A10 | O PDB de 06/08/2001 não continha informação corrente; o contato com a embaixada dos EAU aparentava ser um trote | Rice | **Não** | O PDB de 06/08/2001 | Sim (página da CIA) | **Não** — PDF sem camada de texto | DOC-1 descreve o mesmo PDB de forma diferente (70 investigações do FBI; contato sob investigação por CIA e FBI), mas DOC-1 é síntese de 2004, não o texto | `inconclusiva` |
| A11 | Nunca viu vídeo do Predator | Rice | **Não** | Reportagem de Barton Gellman, que afirma exibição em 10/01/2001 | Não nesta sessão | Não | Reportagem jornalística é fonte secundária; não decide contra nota de trabalho não juramentada | `inconclusiva` |
| A12 | Ligou ao Presidente da Situation Room antes de ir ao PEOC, em 11/09 | Rice | **Não** | Log da Situation Room e Diário Presidencial (registram 09h40), citados pela equipe da Comissão no próprio MFR | Não | Não | A nota da equipe da Comissão é contemporânea ao MFR e independente da depoente, mas os logs em si não foram lidos | `documento citado, não localizado` |
| A13 | A ligação do Príncipe Bandar às 12h25 de 11/09 foi de condolências, não substantiva; não recorda menção a evacuação de sauditas | Rice | **Não** | Nenhum | — | — | Nenhuma | `declaração não corroborada` |
| A14 | Dinheiro de cidadãos privados sauditas ia para ONGs ligadas a terrorismo; quanto a dinheiro do **governo** saudita, não tinha clareza | Rice | **Não** | Nenhum | — | — | Nenhuma | `declaração não corroborada` |
| A15 | Havia 353 artigos de PDB (1998–20/09/2001) sobre al-Qa'ida/UBL/Afeganistão/terrorismo com Paquistão, Arábia Saudita ou Sudão; core group de 24; Review Team de 4 pessoas; subcomissão de 2 com acesso ao restante | PDB Review Team (documento institucional) | Não aplicável | O próprio memorando de 09/02/2004 | Sim | **Sim — lido integralmente** | Autodescrição de documento primário lido | `corroborada` (quanto à estrutura de acesso; ver 5c/5d para o que **não** cobre) |
| A16 | O PDB de 06/08/2001 trazia, em negrito no original, ressalva de que a CIA não conseguira corroborar os relatos mais sensacionais | PDB Review Team | Não aplicável | O PDB de 06/08/2001 | Sim | Não (sem camada de texto) | Nenhuma — é a caracterização da Comissão, não o texto | `documento localizado, não lido` |

### 5.2 Alegações não tabuláveis nesta sessão

| Depoente | MFRs não lidos | Efeito |
|---|---|---|
| George Tenet | 3 (23/12/2003; 22/01/2004; 28/01/2004) | Prioridades 1, 2, 3 e 6 permanecem sem o depoimento mais central |
| Richard A. Clarke | 3 (18/12/2003; 12/01/2004; 03/02/2004) | Prioridades 1, 2 e 6 sem contraprova |
| Sandy Berger | 1 (14/01/2004) | Prioridade 2 sem o segundo lado da reunião de maio/1998 |
| Michael Scheuer | 2 (06/01/2004; 11/03/2004) | Consistência interna do próprio Scheuer não testada |

**Nenhuma alegação atribuída a Clarke, Berger ou Tenet aparece na tabela 5.1.** Não há como tabular o que não foi lido, e preencher essas linhas por conhecimento prévio seria exatamente a falha que o padrão do projeto proíbe.

---

## 6. Fase 2B — Joint Inquiry, Part Four: protocolo pré-registrado

**Não executada.** `intelligence.senate.gov` bloqueado (seção 3). O protocolo abaixo fica pré-registrado para a sessão com acesso.

### 6.1 Regra de tratamento

> As "28 páginas" **não** são prova de participação estatal saudita, e não serão tratadas como tal em nenhuma circunstância.

O documento é, por construção, um capítulo sobre **informação não perseguida até o fim** — um inventário do que a Joint Inquiry encontrou e não resolveu. Um item não perseguido é uma pista pendente, não uma conclusão suprimida. Três distinções que o protocolo mantém separadas em todas as linhas:

1. **Indivíduo com vínculo governamental ≠ governo.** Emprego, estipêndio ou credencial consular estabelecem vínculo, não autorização.
2. **Contato ≠ apoio ≠ apoio consciente ao ataque.** Cada degrau exige evidência própria.
3. **Pista investigativa ≠ conclusão investigativa.** A Part Four registra majoritariamente o primeiro tipo; dizer qual é qual é o produto da leitura.

### 6.2 Instrumento de classificação

Cada item da Part Four recebe exatamente uma categoria:

| Categoria | Definição operacional | Peso probatório |
|---|---|---|
| **pista** | Linha de investigação registrada, sem resolução declarada | Direciona busca futura. Zero como prova |
| **declaração** | Afirmação de pessoa identificada ou não, sem corroboração documental no texto | Depende de identificação, interesse e corroboração |
| **documento** | Registro citado com data e origem | Peso conforme contemporaneidade e proveniência |
| **fato corroborado** | Afirmação que o texto declara verificada por duas ou mais fontes independentes | Mais alto disponível no documento |
| **alegação judicial** | Alegação de peça processual (*In re Terrorist Attacks* e correlatos) | Alegação de parte interessada. **Nunca** tratada como achado investigativo |
| **conclusão investigativa** | Juízo explícito da própria Joint Inquiry | Peso do órgão, limitado pelo que o órgão declara ter verificado |

Cada linha registra ainda: se a Joint Inquiry declarou o item **resolvido, não resolvido ou não perseguido**; e se há indicação de que o FBI ou a CIA deram seguimento.

### 6.3 Pergunta pré-registrada

Ao final da leitura, três perguntas, respondidas apenas com o que o texto sustenta:

1. Quantos itens são `fato corroborado` ou `conclusão investigativa`, contra quantos são `pista` ou `declaração`?
2. Algum item estabelece **autorização ou conhecimento por autoridade do governo saudita**, em oposição a conduta de indivíduos com vínculo governamental?
3. O que a Part Four diz sobre al-Bayoumi, al-Thumairy e Bassnan é apoio consciente ao ataque, contato documentado, ou pista não perseguida — item a item?

**Nenhuma dessas perguntas é respondida nesta sessão.** H2 e H3 permanecem onde a Fase 1 as deixou: genuinamente não resolvidas.

---

## 7. Estado das hipóteses após esta sessão — H1 a H5

Esta sessão **não leu documento novo algum**. O que muda abaixo decorre exclusivamente da correção de enquadramento, não de evidência nova. H6 e H7 não são reavaliadas.

| Hipótese | Estado após correção | Mudou por quê |
|---|---|---|
| **H0** | Fortemente sustentado | Inalterado |
| **H1** | **Existem indícios documentados de falhas burocráticas e possível autoproteção institucional; a alegação específica de supressão deliberada ainda não está corroborada** | Correção de enquadramento (1.2). Os dois pilares anteriores não sustentavam "mais provável que não" |
| **H2** | Genuinamente não resolvido | Inalterado. Fase 2B não executada |
| **H3** | Não testável com o que foi lido | Inalterado |
| **H4** | Fortemente sustentado | Inalterado — é a hipótese com melhor lastro documental direto, e a correção de H1 não a afeta |
| **H5** | **Nenhuma evidência positiva foi encontrada nesta tranche; permanece não testada no nó central al-Mihdhar/al-Hazmi** | Correção de enquadramento (1.3). "Improvável" era uma afirmação de probabilidade sem o exame que a justificaria |

**Registro explícito.** A distância entre H4 e H1 aumentou com esta correção, e a distância entre H1 e H5 aumentou mais ainda. O erro epistêmico a evitar continua sendo o mesmo, agora em versão mais estrita: evidência de falha de processo não é evidência de autoproteção; indício de autoproteção não é evidência de supressão deliberada; e nenhum dos três é evidência de conhecimento prévio operacional.

---

## 8. Condição de retomada

A Fase 2A retoma quando houver acesso de leitura a `archives.gov`. A Fase 2B, quando houver acesso a `intelligence.senate.gov` ou a outra cópia de proveniência declarada da Part Four. Ordem de execução ao retomar, e o que cada passo alimenta:

1. Os nove MFRs, na ordem Tenet ×3 → Clarke ×3 → Berger → Scheuer #2 e #3 — prioridades 1, 2, 3 e 6, e as linhas A1 a A7 da tabela 5.1.
2. Releitura dirigida de DOC-1 para 5a e 5b (assinaturas, endereçamento, lista de distribuição).
3. O PDB de 06/08/2001 com OCR — prioridade 4, linhas A10 e A16.
4. Part Four com o instrumento da seção 6.

Cada leitura fecha linhas da tabela 5.1 ou acrescenta linhas novas. Nenhuma linha muda de status sem que o documento que a move tenha sido lido integralmente e registrado em [`../SOURCES.md`](../SOURCES.md) com data de acesso, extensão lida e limitações.
