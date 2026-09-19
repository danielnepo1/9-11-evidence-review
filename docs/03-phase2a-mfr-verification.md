# Fase 2A — Correção de Enquadramento e Instrumento de Verificação dos MFRs

> Corrige formalmente o enquadramento de [`02-adversarial-audit-phase1.md`](02-adversarial-audit-phase1.md) e estabelece o instrumento de verificação alegação-a-alegação da liberação ISCAP 2026-201. **Execução da leitura dos nove MFRs restantes: concluída na sessão 2 (19/09/2026), após reabertura de acesso** — ver seção 3.1. Os resultados estão incorporados nas seções 4 e 5.

Data desta sessão: **19 de setembro de 2026** (sessão 1: correção de enquadramento e instrumento; sessão 2, mesmo dia: leitura dos nove MFRs e do PDB de 06/08/2001). Escopo: H1–H5. H6 e H7 não são reavaliadas aqui.

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

## 2. O que a sessão 1 entregou e o que não entregou

Tabela histórica da sessão 1 (correção de enquadramento), mantida sem edição por rastreabilidade. Para o que a sessão 2 acrescentou, ver seção 3.1 e o restante do documento.

| Item pedido | Estado (sessão 1) |
|---|---|
| Correção formal do enquadramento (regras 1 a 5) | **Executado** — seção 1, aplicado retroativamente em `02` com marcações `[corrigido]` |
| Fase 2A — leitura integral dos nove MFRs restantes | **Não executado nesta sessão.** Bloqueio de acesso de rede, seção 3. **Executado na sessão 2** — ver §3.1 |
| Fase 2A — tabela de verificação alegação-a-alegação | **Instrumento construído e populado** com as alegações dos documentos efetivamente lidos na Fase 1 (seção 5). As alegações de Clarke, Berger e Tenet não podem ser tabuladas: seus MFRs não foram lidos **nesta sessão — lidos e tabulados na sessão 2 (§5.1, linhas A3a–A3c, A4, A17–A20)** |
| Fase 2B — leitura integral da Part Four | **Não executado.** Mesmo bloqueio. Protocolo de classificação pré-registrado na seção 6. Acesso confirmado na sessão 2 (§3.1); leitura ainda não executada — ver §8 |
| Identificação nominal dos membros da Review Team | **Não determinado por fonte primária.** Pistas de fonte secundária registradas na seção 4, prioridade 5, explicitamente não promovidas a fato. Inalterado na sessão 2 |

---

## 3. Teto de acesso da sessão 1 — registrado com a evidência (superado na sessão 2, ver §3.1)

Nesta sessão (1), todos os repositórios primários do escopo das Fases 2A e 2B estavam inacessíveis a partir deste ambiente. O egresso de rede era intermediado por um proxy que negou a conexão (`CONNECT tunnel failed, response 403` / `connect_rejected — organization policy`) para **todos** os domínios testados:

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

**Consequência para a auditoria (sessão 1):** a Fase 2A permanece aberta. O que foi produzido aqui é o instrumento de verificação e a correção de enquadramento — ambos pré-condição da leitura, não substituto dela.

### 3.1 Acesso reaberto — sessão 2 (19/09/2026)

Novo teste de conectividade, na mesma data, com `curl` direto (fora da ferramenta de fetch do agente): **HTTP 200** em `archives.gov`, `cia.gov`, `nist.gov`, `intelligence.senate.gov`, `govinfo.gov`, `9-11commission.gov` e `govinfo.library.unt.edu`. `vault.fbi.gov` e `www.fbi.gov` continuaram em 403 — o bloqueio deixou de ser geral e passou a ser seletivo a esses dois hosts.

Os nove PDFs-alvo (os MFRs de Tenet ×3, Clarke ×3, Berger, Scheuer #2 e #3) foram baixados, verificados como documentos íntegros (tamanho entre 276 KB e 3,1 MB, não páginas de erro) e lidos integralmente — texto extraído com `pdftotext`, entre 11.612 e 82.089 caracteres por documento, todos com múltiplas páginas de conteúdo substantivo. O PDB de 06/08/2001, cujo PDF não tem camada de texto nativa (confirmado: `pdftotext` extraía 2 caracteres), foi lido via OCR (`pdftoppm` a 300 DPI + `tesseract`), com resultado legível e coerente com o texto já conhecido publicamente deste documento.

Os resultados dessa leitura estão incorporados nas seções 4 (prioridades) e 5 (tabela de verificação) abaixo, com marcação `[sessão 2]` em cada linha nova ou alterada. Nenhuma linha da tabela foi alterada com base em busca ou em conhecimento prévio — todas as alterações citam o MFR específico lido nesta sessão.

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

**Resultado [sessão 2].** O MFR de Tenet #3 (28/01/2004) trata diretamente do episódio Kuala Lumpur/al-Mihdhar ("The Kuala Lumpur (KL) Story"), e o MFR de Clarke #2 (12/01/2004) trata diretamente da ausência de repasse a Clarke. Nenhum dos dois é o documento contemporâneo exigido pelo teste — ambos são memória declarada em 2004 sobre fatos de 2000–2001 — mas ambos foram lidos integralmente e mudam o estado da prioridade de "inteiramente não tocado" para "tocado, ainda inconclusivo":

- Tenet contesta a caracterização da Joint Inquiry de que CIA e FBI não se comunicavam sobre o caso KL, afirmando que "FBI was, in fact, far more aware of the Kuala Lumpur meeting than has previously been made public" e que a CIA pediu à NSA para colocar al-Mihdhar em lista de vigilância ("CIA asked NSA to put Midhar on a watchlist"). Não há data específica para esse pedido nem explicação de por que a inclusão formal na watchlist só ocorreu em agosto de 2001.
- Clarke declara sob juramento que não sabia da presença de al-Mihdhar e al-Hazmi nos EUA, que Dale Watson (FBI) nunca lhe mencionou a busca pelos dois, e que, ao perguntar depois do 11/9 a Tenet e ao C/CTC Cofer Black por que não soube, "[eles] said that one analyst in CTC who should have put the two on the watchlist did not" — ou seja, a explicação dada pela própria liderança da CIA a Clarke, relatada por ele, é falha individual de um analista, não decisão deliberada de reter.
- Nenhum documento contemporâneo (cabo, memorando interno de 2000–2001) foi localizado ou citado por nome de autor nesta sessão. O padrão observado — três depoentes (Clarke, Tenet, Black via Clarke) convergindo em 2003–2004 numa explicação de falha individual/processual — é consistente com a **resposta negativa** do teste pré-registrado, mas não a satisfaz formalmente, porque o teste exige "registro contemporâneo", e o que existe é testemunho declarado quase quatro anos depois.
- **Status da prioridade: permanece inconclusiva quanto ao teste formal; avança de "não tocada" para "tocada, com convergência testemunhal — não documental — para explicação de falha de processo".** H5 continua sem evidência positiva encontrada.

### Prioridade 2 — A discrepância 30% vs 0% (operação de captura, maio de 1998)

- **Alvos:** MFRs de Tenet e Berger; MFRs de Reno, Freeh, White e Fitzgerald (**não** integram a liberação de 2026 — localização pendente no acervo geral de MFRs do NARA).
- **Pergunta:** os dois números existem em registro contemporâneo, ou apenas na memória de Scheuer em dezembro de 2003? Quem comunicou qual estimativa a quem, e em que data?
- **Teste discriminante:** se Tenet ou Berger descrevem a mesma reunião com estimativa diferente de 30%, a alegação passa a `contradita` ou `parcialmente corroborada` conforme o detalhe; se nenhum dos dois menciona números, permanece `declaração não corroborada`.

**Resultado [sessão 2].** O teste discriminante foi aplicado e divide a alegação A3 em duas partes com destinos opostos — ver detalhamento em A3a/A3b na tabela §5:

- **A existência de uma estimativa interna de sucesso abaixo de 30% é agora corroborada por fonte independente do depoente.** O MFR de Tenet #2 (22/01/2004) declara, sobre a mesma operação de maio de 1998: "the chance of success... described to him was less than 30% (the figure agreed upon [pela cadeia de aprovação da CIA])". Isso bate com o que o próprio Scheuer #2 (06/01/2004, lido nesta sessão) registra como o número de aprovação interna da Agência: "It was agreed that the plan had a 20-30% chance of complete success", com o chefe de estação em Islamabad estimando 50-60%. Tenet e Scheuer são declarantes distintos, cada um lido integralmente, descrevendo o mesmo número para a mesma operação — o padrão de `corroborada` do instrumento (§5, regras de aplicação) é satisfeito **para a existência do número**, não para a quem ele foi comunicado.
- **A alegação de que 30% foi comunicado especificamente a Berger, Reno, Freeh e Clarke não encontra apoio em nenhum dos nove MFRs, e Berger nega diretamente ter recebido qualquer estimativa.** O MFR de Berger (14/01/2004) é textual: "Berger does not remember ever being given estimates or the plan's chances for success" e "the operation was never presented to the White House for a decision." O relato de Tenet #2 sobre ter ligado para Berger confirma que a ligação existiu, mas foi para informar a decisão de cancelamento já tomada — "he did not ask for Berger's opinion... rather called Berger to inform him of his operational decision" — sem menção a percentuais. Os MFRs de Clarke (×3) descrevem o processo de cancelamento em detalhe (Berger perguntou a Tenet se aprovava o plano; Tenet disse que não) mas também não mencionam nenhum número comunicado a Clarke. Por não haver contradição frontal de um número específico — porque nenhuma das três fontes independentes confirma que um número foi dado a essas pessoas —, o status correto pelo vocabulário fechado é `declaração não corroborada`, e não `contradita`; a negação direta de Berger quanto a **ter recebido qualquer estimativa** é o achado mais forte contra essa parte da alegação.
- **A alegação do "0% informado a Mary Jo White" permanece integralmente não corroborada, e o próprio MFR de Scheuer #2 revela que a fonte de Scheuer para esse dado era, já em 2003, de segunda mão.** O texto: "it was relayed back to Scheuer by his contacts in New York that C/CTC Geoff O'Connell had briefed the operation to the Attorney's office of the Southern District of New York as having 0% chance of success." Não é Scheuer testemunhando algo que presenciou; é algo que lhe foi "relayed back" por "contatos em Nova York", sobre um briefing ao "gabinete do procurador" do SDNY em geral — não nomeadamente a Mary Jo White. Isso não é uma contradição do que constava em `02`/DOC-3 (a Fase 1 já registrava a alegação como vinda de Scheuer), mas é uma precisão importante: a cadeia de custódia da informação, na fonte primária, é depoente → boato de terceiros não identificados → característica atribuída a O'Connell. Mantém-se `declaração não corroborada`.

### Prioridade 3 — O PDB de 25/03/1999 supostamente retido

- **Alvos:** o memorando citado por Scheuer; o autor do texto barrado, nomeado no MFR; MFRs de Tenet.
- **Armadilha metodológica a evitar:** o PDB publicado de 25/03/1999 — se estiver entre os 71 liberados — **não** pode confirmar nem refutar a alegação, porque a alegação é sobre um texto que teria sido *removido antes da publicação*. Um item ausente de um PDB é compatível tanto com "foi barrado" quanto com "nunca foi escrito". O teste real é o memorando interno e o depoimento do autor nomeado.
- **Status atual:** `documento citado, não localizado`.

**Resultado [sessão 2].** Os três MFRs de Tenet — os únicos, entre os nove, cujo depoente poderia falar com autoridade sobre uma decisão do DCI de barrar texto de um PDB — foram lidos integralmente e **não contêm nenhuma menção** a um PDB de 25/03/1999, a texto sobre WMD removido, ou a uma decisão de ocultar atraso no repasse ao FBI. Isto é uma busca negativa, não uma refutação: os interrogadores da Comissão simplesmente não trouxeram o assunto a Tenet nestas três sessões (23/12/2003, 22/01/2004, 28/01/2004), e o memorando interno citado por Scheuer continua não localizado. **Status inalterado: `documento citado, não localizado`.**

### Prioridade 4 — O PDB de 06/08/2001

- **Alvo:** o PDF do PDB na página da CIA. Obstáculo técnico já documentado: digitalização sem camada de texto. Exige OCR — portanto, exige acesso ao arquivo.
- **Pergunta:** o texto integral sustenta a caracterização de Rice ("nenhuma informação corrente"; contato com a embaixada dos EAU como trote) ou a descrição da Comissão em DOC-1 (70 investigações de campo do FBI; CIA e FBI investigando o contato)?
- **Observação:** as duas coisas podem ser verdadeiras ao mesmo tempo. "Informação histórica, não corrente" e "há 70 investigações abertas" não se contradizem necessariamente. O teste é o texto.

**Resultado [sessão 2] — prioridade resolvida.** O obstáculo técnico foi superado: o PDF de 06/08/2001 não tem camada de texto nativa, mas OCR (`pdftoppm` 300 DPI + `tesseract`) produziu texto corrido, legível e internamente coerente nas suas duas páginas. O texto integral **sustenta a descrição de DOC-1 e contradiz a caracterização de Rice**:

> "The FBI is conducting approximately 70 full field investigations throughout the US that it considers Bin Ladin-related. CIA and the FBI are investigating a call to our Embassy in the UAE in May saying that a group of Bin Ladin supporters was in the US planning attacks with explosives."

O documento não chama o contato da embaixada dos EAU de trote — trata-o como objeto de investigação ativa conjunta CIA-FBI. A ressalva de não-corroboração que o PDB efetivamente contém é sobre um item diferente e mais antigo (um relato de 1998 sobre sequestro de avião para libertar o "Blind Shaykh"): "We have not been able to corroborate some of the more sensational threat reporting, such as that from a [redigido] service in 1998 saying that Bin Ladin wanted to hijack a US aircraft...". Não há, em nenhuma frase do documento, a afirmação de que a informação era puramente histórica e sem relevância corrente — pelo contrário, o PDB abre afirmando que Bin Ladin "since 1997 has wanted to conduct terrorist attacks in the US" e fecha com as duas investigações ativas citadas acima.

- **A10 muda de `inconclusiva` para `contradita`** (fonte contraditória — o próprio PDB — lida integralmente, conforme exige a regra de aplicação do instrumento).
- **A16 muda de `documento localizado, não lido` para `corroborada`**: a caracterização da PDB Review Team (DOC-1) de que o documento trazia ressalva de não-corroboração dos relatos mais sensacionais é confirmada pelo texto agora lido — embora não seja possível confirmar nesta sessão se a ressalva estava, no original, em negrito (a formatação de ênfase não sobrevive de forma confiável ao OCR).

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

**Resultado [sessão 2] — prioridade parcialmente resolvida: (i) e (ii) coexistem, com corroboração cruzada entre dois depoentes independentes.**

- **(i) Barreira jurídica formal, identificada e nomeada.** Clarke #1 (18/12/2003) descreve a Regra Federal 6E (regra do grande júri) como o obstáculo formal citado pelo FBI para não compartilhar informação com a Casa Branca: "the FBI said the White House couldn't see it because of Federal Rule 6E, the grand jury rule." Reno propôs contornar isso mostrando material ao NSC antes do grande júri, mas o acordo formal NSC-DOJ "went into perpetual negotiations and was never finished."
- **(ii) Prática institucional além da barreira formal, corroborada por dois depoentes independentes que descrevem as mesmas deficiências concretas.** Clarke #1 e Tenet #2 (22/01/2004) — lidos integralmente, depoentes distintos, sem que um cite o outro nesse ponto — convergem na mesma lista de deficiências institucionais do FBI, não decorrentes da Regra 6E: ausência de um quartel-general de contraterrorismo dedicado (Tenet: "the Bureau had no CT headquarters"), ausência de oficiais de relatório para produzir análise a partir dos 302s (Clarke: "FBI has no reports-officer mechanism for analytical comment"; Tenet, quase nas mesmas palavras: "the FBI lacked reports officers, the ability to link cases, spot trends and do analyses, and did not disseminate intelligence"), e dificuldade de acesso aos próprios 302s do FBI mesmo pela CIA (Tenet: "It was hard to access FBI's 302s"). A convergência entre dois depoentes que não estavam coordenando essa parte específica do testemunho satisfaz a regra de `corroborada` do instrumento (§5) para a proposição estreita: **as limitações iam além da barreira jurídica formal e incluíam déficits de capacidade analítica e de disseminação, próprios da instituição.**
- **(iii) Decisão caso a caso de reter informação específica** não foi corroborada nem refutada por nenhum dos nove MFRs como explicação geral — mas apareceu como explicação pontual no caso concreto de al-Mihdhar/al-Hazmi (ver Prioridade 1, resultado): ali a explicação dada foi falha individual de um analista, não barreira jurídica nem decisão deliberada.
- **Conclusão da prioridade:** a lacuna CIA-FBI não tem causa única. (i) e (ii) operavam simultaneamente e são distinguíveis na fonte primária — a barreira formal (Regra 6E) explica por que a Casa Branca não recebia material de grande júri por escrito; os déficits institucionais do FBI (sem oficiais de relatório, sem HQ de CT, sem disseminação) explicam por que mesmo informação fora do escopo da Regra 6E não circulava bem. Nenhuma das duas, isoladamente ou somadas, equivale a "decisão caso a caso de reter" no sentido do item (iii) — que continua sem corroboração como padrão geral.

---

## 5. Instrumento de verificação alegação-a-alegação

Vocabulário de status fechado. Nenhum outro termo é admitido nesta coluna:

`declaração não corroborada` · `documento citado, não localizado` · `documento localizado, não lido` · `parcialmente corroborada` · `corroborada` · `contradita` · `inconclusiva`

Regras de aplicação:

- `corroborada` exige **fonte independente do depoente**, lida integralmente. Um depoente corroborando a si mesmo em outro depoimento não corrobora nada.
- `documento citado, não localizado` é o status padrão de toda alegação que se apoia em memorando, cabo ou relatório que a auditoria não localizou — mesmo sob juramento, mesmo com data e destinatário.
- `contradita` exige que a fonte contraditória tenha sido lida integralmente. Tensão entre duas descrições não lidas em paralelo é `inconclusiva`, não `contradita`.

### 5.1 Alegações dos documentos efetivamente lidos

Linhas A1–A16 derivam de DOC-1, DOC-2 e DOC-3, lidos integralmente em 17/09/2026 (sessão 1), com A3, A4, A10 e A16 revisadas em 19/09/2026 (sessão 2) à luz dos nove MFRs e do PDB agora lidos. Linhas A17 em diante derivam exclusivamente dos nove MFRs e do PDB lidos na sessão 2; cada uma cita o documento específico.

| # | Alegação | Quem a fez | Sob juramento? | Documento contemporâneo citado | Localizado? | Lido? | Corroboração independente | Status |
|---|---|---|---|---|---|---|---|---|
| A1 | Não houve produto analítico estratégico nem NIE sobre métodos de ataque de UBL até meados de 1999; pediu repetidamente | Scheuer | **Sim** | Memorando próprio de 28/06/1999 | Não | Não | Nenhuma — os MFRs de Tenet (×3) e Clarke (×3), agora lidos integralmente, não abordam este ponto especificamente | `documento citado, não localizado` |
| A2 | Texto sobre WMD barrado do PDB de 25/03/1999 por direção do DCI, para ocultar atraso de 2 anos no repasse do FBI | Scheuer | **Sim** | Memorando interno + autor do PDB nomeado no MFR | Não | Não | Nenhuma — busca negativa confirmada nos três MFRs de Tenet, lidos integralmente (Prioridade 3, sessão 2) | `documento citado, não localizado` |
| A3a `[sessão 2]` | Existia estimativa interna da CIA de sucesso abaixo de 30% para a operação de captura de maio/1998 | Scheuer | **Sim** | Nenhum documento citado; número de aprovação interna relatado de memória | Não aplicável | — | **Corroborada por Tenet #2** ("less than 30%... the figure agreed upon"), que é fonte independente do depoente, lida integralmente | `corroborada` |
| A3b `[sessão 2]` | Essa estimativa (ou qualquer estimativa) foi comunicada especificamente a Berger, Reno, Freeh e Clarke | Scheuer | **Sim** | Nenhum | Não aplicável | — | Berger nega diretamente ter recebido qualquer estimativa e afirma que a operação nunca foi apresentada à Casa Branca para decisão; Tenet #2 confirma a ligação a Berger mas apenas para informar o cancelamento, sem número; Clarke (×3) não menciona número | `declaração não corroborada` — componente com negação direta de um dos quatro destinatários alegados |
| A3c `[sessão 2]` | 0% de chance de sucesso foi informado por O'Connell ao gabinete do procurador do SDNY (Mary Jo White) | Scheuer | **Sim** | Nenhum | Não aplicável | — | Nenhuma; o próprio MFR de Scheuer #2 revela que a informação lhe foi "relayed back" por "contatos em Nova York" — de segunda mão já na fonte primária | `declaração não corroborada` |
| A4 `[sessão 2: revisada]` | Sauditas sistematicamente não cooperativos; nunca forneceram informação útil; abrigo a Madani al-Tayyib sem acesso da CIA | Scheuer | **Sim** | Memo próprio de 03/05/1996; Spot Report de 24/06/1997 (não localizados) | Não | Não | **Parcialmente corroborada por Clarke #3**, fonte independente lida integralmente: confirma que a CIA soube pela imprensa que os sauditas abrigavam al-Tayyib e que "the USG never got to question al-Tayyib" após pedido formal de acesso | `parcialmente corroborada` (quanto ao caso concreto de al-Tayyib; a generalização "nunca forneceram informação útil" permanece não corroborada) |
| A5 | Uma das razões do cancelamento da operação de maio/1998 foi oferta saudita de resolver o caso UBL por conta própria | Scheuer | **Sim** | Nenhum; declarado como crença do depoente | Não aplicável | Não | Tenet #2 e Clarke #1 (ambos lidos integralmente) atribuem o cancelamento à recomendação unânime de DDO/C-CTC/C-NE por razões operacionais (risco de dano colateral, ativos não confiáveis) — nenhum dos dois menciona a oferta saudita como causa. Tensão não resolvida, não contradição frontal (nenhuma fonte nega que a oferta saudita tenha sido *um* fator concorrente) | `inconclusiva` |
| A6 | Não recordava o relato de 10/09/1998 sobre avião carregado de explosivos, mas aeronave-como-arma era conhecida no alvo UBL (caso Murad) | Scheuer | **Sim** | O próprio artigo de PDB de 10/09/1998 | Sim — indexado em DOC-1 | Não (PDB original não lido) | DOC-1 corrobora a **existência** do relato; Scheuer #2 (sessão 2) acrescenta detalhe de primeira mão sobre o caso Murad ("the airplane guy") como precedente conhecido desde 1996, mas é o mesmo depoente, não corroboração independente | `parcialmente corroborada` |
| A7 | Relação instrumental entre serviço paquistanês e UBL para treinamento é "too conspiratorial" | Scheuer | **Sim** | Nenhum | Não aplicável | Não | Nenhuma | `declaração não corroborada` |
| A8 | Expressou-se mal em maio/2002; deveria ter dito que *ela* não poderia ter imaginado aviões como mísseis; soube depois de relatos anteriores | Rice | **Não** (reunião, sem juramento registrado) | Transcrição da coletiva de maio/2002 | Não nesta sessão (documento público, localização trivial) | Não | O próprio MFR registra a retratação; a declaração original não foi lida no primário | `parcialmente corroborada` |
| A9 | Não havia fluxo de relatos sobre ataques dentro dos EUA; todos apontavam para fora | Rice | **Não** | Nenhum citado pela depoente | — | — | Tensão com DOC-1 (24 artigos do core group sobre ataques nos EUA e/ou aeronaves); o PDB de 06/08/2001, agora lido (A10), reforça a tensão ao registrar 70 investigações domésticas ativas do FBI em agosto de 2001 | `inconclusiva` — tensão documental não resolvida |
| A10 `[sessão 2: resolvida]` | O PDB de 06/08/2001 não continha informação corrente; o contato com a embaixada dos EAU aparentava ser um trote | Rice | **Não** | O PDB de 06/08/2001 | Sim (página da CIA) | **Sim — lido integralmente via OCR** | O texto lido não descreve o contato da embaixada dos EAU como trote; registra-o como objeto de investigação ativa CIA-FBI ("CIA and the FBI are investigating a call to our Embassy in the UAE..."), e a ressalva de não-corroboração do documento é sobre um item distinto (relato de sequestro de 1998) | `contradita` |
| A11 | Nunca viu vídeo do Predator | Rice | **Não** | Reportagem de Barton Gellman, que afirma exibição em 10/01/2001 | Não nesta sessão | Não | Reportagem jornalística é fonte secundária; não decide contra nota de trabalho não juramentada. Clarke #3 (sessão 2) declara que Tenet mostrou o vídeo do Predator "a todo mundo na cidade" em maio de 2001 e que era "inteiramente plausível" que Bush o tivesse visto, mas Clarke não afirma ter visto Rice assistir | `inconclusiva` |
| A12 | Ligou ao Presidente da Situation Room antes de ir ao PEOC, em 11/09 | Rice | **Não** | Log da Situation Room e Diário Presidencial (registram 09h40), citados pela equipe da Comissão no próprio MFR | Não | Não | A nota da equipe da Comissão é contemporânea ao MFR e independente da depoente, mas os logs em si não foram lidos | `documento citado, não localizado` |
| A13 | A ligação do Príncipe Bandar às 12h25 de 11/09 foi de condolências, não substantiva; não recorda menção a evacuação de sauditas | Rice | **Não** | Nenhum | — | — | Nenhuma | `declaração não corroborada` |
| A14 | Dinheiro de cidadãos privados sauditas ia para ONGs ligadas a terrorismo; quanto a dinheiro do **governo** saudita, não tinha clareza | Rice | **Não** | Nenhum | — | — | Nenhuma. Berger (sessão 2) declara nunca ter visto evidência de dinheiro do governo saudita para UBL/al-Qa'ida, "as opposed to money from individual Saudis" — mesma distinção de Rice, mas é depoente diferente descrevendo sua própria ausência de evidência, não confirmação da alegação de Rice sobre o que ela sabia | `declaração não corroborada` |
| A15 | Havia 353 artigos de PDB (1998–20/09/2001) sobre al-Qa'ida/UBL/Afeganistão/terrorismo com Paquistão, Arábia Saudita ou Sudão; core group de 24; Review Team de 4 pessoas; subcomissão de 2 com acesso ao restante | PDB Review Team (documento institucional) | Não aplicável | O próprio memorando de 09/02/2004 | Sim | **Sim — lido integralmente** | Autodescrição de documento primário lido | `corroborada` (quanto à estrutura de acesso; ver 5c/5d para o que **não** cobre) |
| A16 `[sessão 2: resolvida]` | O PDB de 06/08/2001 trazia, em negrito no original, ressalva de que a CIA não conseguira corroborar os relatos mais sensacionais | PDB Review Team | Não aplicável | O PDB de 06/08/2001 | Sim | **Sim — lido integralmente via OCR** | O texto lido contém a ressalva quase literalmente: "We have not been able to corroborate some of the more sensational threat reporting..." Não é possível confirmar a formatação em negrito do original a partir do OCR | `corroborada` (quanto ao conteúdo da ressalva; formatação não verificável) |
| A17 `[sessão 2, nova]` | O motivo de Clarke não saber da presença de al-Mihdhar/al-Hazmi nos EUA foi falha de um único analista do CTC em colocá-los na watchlist — não decisão deliberada | Clarke, relatando resposta de Tenet e Cofer Black | **Sim** (depoimento de Clarke; a resposta de Tenet/Black a ele não é, ela mesma, sob juramento nesta cena) | Nenhum documento citado | Não aplicável | — | Nenhuma fonte documental contemporânea; é testemunho de 2004 sobre explicação dada em conversa não datada com precisão | `declaração não corroborada` — ver Prioridade 1 para o enquadramento completo |
| A18 `[sessão 2, nova]` | A lacuna de compartilhamento CIA-FBI combinava barreira jurídica formal (Regra Federal 6E) com déficits institucionais do FBI (sem HQ de CT, sem oficiais de relatório, sem disseminação) | Clarke e Tenet, independentemente | **Sim** (ambos) | Nenhum documento formal citado para os déficits institucionais; a Regra 6E é norma pública, não documento do caso | Não aplicável | — | **Corroborada** — dois depoentes independentes (Clarke #1, Tenet #2), lidos integralmente, descrevem as mesmas deficiências concretas do FBI sem que um cite o outro nesse ponto específico | `corroborada` — ver Prioridade 6 |
| A19 `[sessão 2, nova]` | A operação de captura de maio/1998 nunca foi apresentada à Casa Branca para decisão, e Berger nunca recebeu estimativa de sucesso | Berger | **Sim** | Nenhum | Não aplicável | — | Consistente com o relato de Tenet #2 de que ligou a Berger apenas para informar o cancelamento já decidido pela CIA, sem pedir opinião | `parcialmente corroborada` |
| A20 `[sessão 2, nova]` | O cancelamento da operação de maio/1998 seguiu recomendação unânime de três oficiais operacionais da CIA (DDO Downing, C/CTC O'Connell, C/NE) por razões operacionais, sem decisão política externa | Tenet | **Sim** | Nenhum documento citado; Tenet declara não recordar se houve memorando registrando a decisão | Não aplicável | — | **Corroborada por Clarke #1**, fonte independente lida integralmente, que descreve o mesmo processo (CSG pediu fotos melhores do composto de Tarnak; autoridades da CIA "acima" da cadeia "laughed at it" e recusaram aprovar; Berger perguntou a Tenet se aprovava, Tenet disse que não) | `corroborada` |

### 5.2 Situação de leitura após a sessão 2 — nenhum MFR da liberação 2026-201 permanece não lido

Os nove MFRs listados na versão anterior desta seção (Tenet ×3, Clarke ×3, Berger, Scheuer #2 e #3) foram lidos integralmente em 19/09/2026 (sessão 2) — ver §3.1 e SOURCES.md. Todas as alegações desses MFRs relevantes às seis prioridades pré-registradas estão incorporadas na tabela 5.1 (linhas A3a–A3c, A4 revisada, A17–A20). Isto fecha a liberação ISCAP 2026-201 como fonte para a Fase 2A.

**O que permanece fora do alcance desta liberação, sem mudança nesta sessão:**

| Item | Estado |
|---|---|
| MFRs de Janet Reno, Louis Freeh, Mary Jo White, Patrick Fitzgerald | Não localizados — não integram a liberação 2026-201; localização pendente no acervo geral de MFRs da Comissão no NARA (fora do escopo desta sessão) |
| Memorando de Scheuer de 28/06/1999 (A1) | Não localizado |
| Memorando interno sobre o PDB de 25/03/1999 (A2) | Não localizado |
| Memo de Scheuer de 03/05/1996 e Spot Report de 24/06/1997 (A4) | Não localizados |
| Consistência interna de Scheuer entre seus três MFRs (#1, #2, #3) | Não testada sistematicamente nesta sessão — os três foram lidos, mas uma checagem linha a linha de consistência entre eles fica para sessão futura |

---

## 6. Fase 2B — Joint Inquiry, Part Four: protocolo pré-registrado

**Não executada.** Na sessão 1, `intelligence.senate.gov` estava bloqueado (seção 3). **Na sessão 2 (19/09/2026), o acesso a esse domínio foi testado e confirmado (HTTP 200)** — ver §3.1 — mas a leitura da Part Four não foi realizada nesta sessão; ficou fora do escopo executado, que se concentrou nos nove MFRs e no PDB (Fase 2A). O protocolo abaixo permanece pré-registrado para a sessão que executar a leitura.

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

Esta seção tem duas camadas. A sessão 1 (correção de enquadramento) não leu documento novo — o que mudou ali decorreu só da correção de enquadramento. A sessão 2 leu nove MFRs e um PDB; o que muda abaixo por causa dela é assinalado `[sessão 2]` e decorre de evidência nova, citada por documento. H6 e H7 não são reavaliadas.

| Hipótese | Estado após sessão 2 | Mudou por quê |
|---|---|---|
| **H0** | Fortemente sustentado | Inalterado |
| **H1** | **Existem indícios documentados de falhas burocráticas e possível autoproteção institucional; a alegação específica de supressão deliberada ainda não está corroborada** | Enquadramento inalterado desde a sessão 1. `[sessão 2]` A10 mudou de `inconclusiva` para `contradita` — a caracterização pública de Rice sobre o PDB de 06/08/2001 não se sustenta contra o texto agora lido — mas isso pesa sobre a precisão de uma declaração pública específica, não estabelece por si só supressão deliberada de informação em 2001. Não move H1. |
| **H2** | Genuinamente não resolvido | Inalterado. Fase 2B não executada |
| **H3** | Não testável com o que foi lido | Inalterado |
| **H4** | Fortemente sustentado | Inalterado — é a hipótese com melhor lastro documental direto, e a correção de H1 não a afeta |
| **H5** | **Nenhuma evidência positiva foi encontrada; o nó central al-Mihdhar/al-Hazmi deixou de estar "inteiramente não tocado" e passou a "tocado, com explicação convergente de falha de processo, não documental"** | `[sessão 2]` Prioridade 1: Clarke, Tenet e Black (via Clarke) convergem em atribuir a falha de repasse a um analista individual do CTC que não colocou os dois na watchlist — não a uma decisão deliberada de reter. É testemunho de 2003–2004, não documento contemporâneo; não satisfaz o teste pré-registrado de "resposta negativa" formalmente, mas é o padrão mais consistente com ela. H5 permanece sem evidência positiva. |

**Achado novo que não muda nenhuma hipótese, mas é relevante para o padrão geral `[sessão 2]`.** A Prioridade 6 mostrou que a lacuna de compartilhamento CIA-FBI teve pelo menos duas causas distintas e corroboradas — uma barreira jurídica formal (Regra 6E) e déficits institucionais do FBI independentes dela (sem quartel-general de CT, sem oficiais de relatório, sem disseminação) — nenhuma das quais equivale a decisão caso a caso de reter informação especificamente relacionada ao 11/9. Isso reforça, com evidência agora lida, a distinção de categoria que a seção 1 já exigia: falha de processo, autoproteção institucional e conhecimento prévio operacional continuam sendo três proposições diferentes, e a sessão 2 corrobora a primeira sem tocar as outras duas.

**Registro explícito.** A distância entre H4 e H1 aumentou com a correção da sessão 1, e a distância entre H1 e H5 aumentou mais ainda. O erro epistêmico a evitar continua sendo o mesmo, agora testado contra evidência lida, não apenas contra enquadramento: evidência de falha de processo não é evidência de autoproteção; indício de autoproteção não é evidência de supressão deliberada; e nenhum dos três é evidência de conhecimento prévio operacional.

---

## 8. Condição de retomada

**Passos 1 e 3 da versão anterior desta seção foram executados na sessão 2 (19/09/2026)** — os nove MFRs e o PDB de 06/08/2001, com os resultados incorporados nas seções 4, 5 e 7. O que segue é o que resta, com acesso já testado e confirmado nesta mesma sessão para a maioria dos domínios (§3.1):

1. **Releitura dirigida de DOC-1 para 5a e 5b** (assinaturas, endereçamento, lista de distribuição da PDB Review Team) — não executada. Acesso a `archives.gov` confirmado.
2. **Fase 2B — Joint Inquiry, Part Four**, com o instrumento da seção 6 — não executada. Acesso a `intelligence.senate.gov` confirmado nesta sessão (HTTP 200), ao contrário do registrado na sessão 1; a fase é executável a partir daqui.
3. **Localização dos MFRs de Reno, Freeh, White e Fitzgerald** no acervo geral de MFRs da Comissão no NARA (não a liberação 2026-201) — necessária para fechar A1, A3b/A3c e A4 além do que a liberação 2026-201 permite. Não iniciada.
4. **Fase 3 (NIST/NCSTAR)** — fora do escopo desta sessão, mas acesso a `nist.gov` confirmado (HTTP 200); ver [`NEXT-STEPS.md`](../NEXT-STEPS.md).
5. **Fase 4 (cronologia FAA/NORAD)** — fora do escopo desta sessão; fontes ainda não testadas quanto a acesso.

**Nota sobre `vault.fbi.gov`/`www.fbi.gov`:** esses dois hosts continuam bloqueados (403) mesmo com o acesso geral restaurado (§3.1). O material do FBI liberado sob a Executive Order 14040 permanece inacessível a partir deste ambiente; isso afeta especificamente a Prioridade 1 (registro do FBI sobre o caso KL/watchlist) e a Fase 4.

Cada leitura fecha linhas da tabela 5.1 ou acrescenta linhas novas. Nenhuma linha muda de status sem que o documento que a move tenha sido lido integralmente e registrado em [`../SOURCES.md`](../SOURCES.md) com data de acesso, extensão lida e limitações.
