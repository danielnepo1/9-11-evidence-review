# Próximas Fases

> **Atualização de ambiente (19/09/2026, sessão 2).** O bloqueio de rede registrado abaixo (sessão 1, mesma data) foi retestado e **não se confirmou** para a maioria dos domínios: `archives.gov`, `cia.gov`, `nist.gov`, `intelligence.senate.gov`, `govinfo.gov`, `9-11commission.gov` e `govinfo.library.unt.edu` respondem HTTP 200. `vault.fbi.gov` e `www.fbi.gov` continuam bloqueados (403) — o bloqueio deixou de ser geral e é agora seletivo a esses dois hosts. Com o acesso restaurado, a Fase 2A foi executada nesta sessão: os nove MFRs pendentes e o PDB de 06/08/2001 (via OCR) foram lidos integralmente — ver [`docs/03-phase2a-mfr-verification.md`](docs/03-phase2a-mfr-verification.md), seções 3.1, 4, 5 e 7, e [`SOURCES.md`](SOURCES.md). **Antes de iniciar qualquer fase nova, sempre reverificar o acesso de leitura aos domínios-alvo** — o bloqueio já se mostrou instável entre sessões no mesmo dia — e nunca produzir conclusões a partir de busca ou de conhecimento prévio, conforme a regra de execução no final deste arquivo.
>
> **Registro original da falha (sessão 1, mantido por rastreabilidade).** Numa tentativa de execução em 19/09/2026, todos os domínios acima (exceto os dois do FBI) estavam bloqueados por política de egresso de rede do ambiente (403 no CONNECT).

Roteiro de continuação da auditoria, na ordem de execução planejada ao final da Fase 1 (ver [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md), seção 9).

**Ordem de execução:** 2A → 2B → 3 → 4. A sequência não é arbitrária: 2A e 2B usam material já desclassificado e de volume tratável, e incidem sobre as hipóteses onde a Fase 1 deixou lacunas explícitas (H5 no nó al-Mihdhar/al-Hazmi; H2/H3 na rede de apoio). A Fase 3 é a mais cara em volume de leitura e só rende depois que as correções da seção 2 de `docs/02` estiverem internalizadas. A Fase 4 depende de material com timestamp que pode exigir pedidos de acesso com prazo longo — vale iniciar os pedidos cedo, mesmo executando a fase por último.

Antes de iniciar qualquer fase, ler [`README.md`](README.md) (hipóteses e escala de confiança), [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md) (estado atual) e [`SOURCES.md`](SOURCES.md) (o que já foi lido e com que profundidade).

## Fase 2A — MFRs restantes da liberação de 2026

**Status: leitura dos nove MFRs concluída em 19/09/2026 (sessão 2).** Resultados incorporados em [`docs/03-phase2a-mfr-verification.md`](docs/03-phase2a-mfr-verification.md) (seções 4, 5, 7). Pendências remanescentes da fase: releitura dirigida de DOC-1 para a prioridade 5 (5a/5b), e localização — fora da liberação 2026-201 — dos MFRs de Reno, Freeh, White e Fitzgerald no acervo geral do NARA. Nenhuma dessas duas pendências foi iniciada.

~~Ler integralmente os 9 MFRs ainda não lidos, nesta ordem: Tenet (×3) → Clarke (×3) → Berger → Scheuer (×2).~~ — concluído.

**Seis prioridades pré-registradas** (perguntas, testes discriminantes e critérios de resposta positiva/negativa/inconclusiva em [`docs/03` §4](docs/03-phase2a-mfr-verification.md)):

1. O nó al-Mihdhar/al-Hazmi — onde H5 se decide. Deixou de estar intocado na sessão 2 (19/09/2026): testemunho de Clarke/Tenet/Black lido e tabulado, mas nenhum documento contemporâneo localizado ainda — ver [`docs/03` Prioridade 1](docs/03-phase2a-mfr-verification.md).
2. A discrepância 30% vs 0% na operação de captura de UBL de maio de 1998.
3. O PDB de 25/03/1999 supostamente retido — atenção à armadilha: o PDB publicado não testa a alegação, o memorando interno testa.
4. O PDB de 06/08/2001 — exige OCR, o PDF não tem camada de texto.
5. A estrutura de acesso da Comissão aos PDBs — quatro determinações separadas (5a a 5d), incluindo a identificação nominal dos 4 da Review Team e dos 2 da subcomissão.
6. Interação CIA–FBI e a lacuna entre inteligência externa e investigação doméstica — barreira jurídica, prática institucional ou decisão caso a caso são três coisas diferentes.

**Produto obrigatório:** cada alegação relevante entra na tabela de [`docs/03` §5](docs/03-phase2a-mfr-verification.md) com as colunas fixas (alegação · quem · sob juramento · documento contemporâneo citado · localizado · lido · corroboração independente · status) e status do vocabulário fechado.

## Fase 2B — Joint Congressional Inquiry

**Status: aberta, não executada. Acesso a `intelligence.senate.gov` confirmado em 19/09/2026 (sessão 2)** — a fase é executável a partir daqui, ao contrário do que a sessão 1 havia registrado. Protocolo de classificação pré-registrado em [`docs/03` §6](docs/03-phase2a-mfr-verification.md).

Ler o relatório integral da Joint Inquiry de 2002 e a Parte Quatro ("28 páginas"), desclassificada em 2016. Comparar com o Capítulo 5 do relatório da Comissão do 11/9.

**Objetivo específico:** avançar H2/H3 — a única forma de sair do "genuinamente não resolvido" nessas duas hipóteses é com material que trate diretamente da rede de apoio a al-Hazmi e al-Mihdhar (Omar al-Bayoumi, Fahad al-Thumairy, Osama Bassnan), que a Fase 1 não tocou.

**Regra de tratamento, não negociável:** as "28 páginas" **não** são prova de participação estatal saudita. Cada item recebe exatamente uma classificação — `pista`, `declaração`, `documento`, `fato corroborado`, `alegação judicial` ou `conclusão investigativa` — mais o registro de se a Joint Inquiry o declarou resolvido, não resolvido ou não perseguido. Indivíduo com vínculo governamental não é governo; contato não é apoio; apoio não é apoio consciente ao ataque.

## Fase 3 — Auditoria técnica profunda (engenharia)

**Acesso a `nist.gov` confirmado em 19/09/2026 (sessão 2).** Fase não iniciada nesta sessão — ordem de execução é 2A → 2B → 3 → 4 (ver acima), e 2B segue aberta.

Sequência de leitura definida em [`docs/02`](docs/02-adversarial-audit-phase1.md), seção 7:

1. FEMA 403, Appendix C — corrosão/eutética sulfídica, com atenção à datação da amostra (antes ou depois do colapso).
2. NCSTAR 1-9, capítulos 8 e 12 — propriedades de conexão, shear studs, dimensões de assento, transferência ANSYS→LS-DYNA, condições de contorno.
3. NCSTAR 1-9A — modelos que **não** produziram colapso e o critério de seleção do caso final. Prioridade alta: é o ponto de maior rendimento probatório e o mais afetado pelos arquivos retidos sob Seção 7d do NCST Act.
4. NCSTAR 1-6C e 1-6D — conexões, restrição térmica, análise global das torres.
5. Relatório Hulsey/UAF integral + críticas técnicas formais publicadas contra ele.
6. Modelagem conceitual própria, estágio a estágio: massa participante, fração ejetada, razão de compactação, altura de queda disponível, sensibilidade das conclusões às premissas.

## Fase 4 — Cronologia FAA/NORAD

Reconstrução minuto a minuto usando registros com timestamp: gravações FAA, gravações NEADS/NORAD, radar, logs, telefonemas, ordens de scramble, comparando versões oficiais de 2001, 2003 e 2004.

**Pontos de investigação específica:**
- Por que a cronologia inicial do NORAD diferia da reconstrução posterior.
- O "phantom Flight 11".
- Horários de notificação dos voos 11, 175, 77 e 93.
- Destruição da gravação com relatos de controladores de Nova York.

**Regra de tratamento:** não transformar falsidade ou encobrimento pós-evento automaticamente em prova de participação prévia — testar como hipóteses separadas (H1 vs. H5).

## Itens de fundo, sem fase fixa ainda

- Interrogatórios de KSM, bin al-Shibh, Abu Zubaydah: para cada afirmação usada na narrativa de planejamento, verificar se foi produzida antes ou depois de técnica coercitiva, se há corroboração documental independente, e comparar com o relatório do Senado (SSCI CRPT-113srpt288).
- Evidência sísmica, financeira (negociações suspeitas, SEC/FBI) e Pentágono/Voo 93 — nenhuma tocada ainda.
- Auditoria de independência da própria Comissão: o MFR de Rice já expôs, incidentalmente, que Philip Zelikow (Diretor Executivo) coautorou um livro acadêmico com a depoente em 1995. Vale uma checagem sistemática de conflitos de interesse declarados/não declarados entre staff da Comissão e os depoentes do Executivo.

## Regra de execução

Cada nova fase deve seguir o mesmo padrão desta: registrar título completo, autor, data do evento, data do documento, data da desclassificação, URL, versão, extensão efetivamente lida, redações e limitações de acesso — antes de qualquer conclusão. Nenhum documento é citado como "lido" se apenas seu resumo, FAQ, press release ou um trecho de busca foi consultado.

E a regra de enquadramento, que vale em todas as fases: restrição de acesso, alerta genérico e testemunho interessado não são prova de encobrimento nem de conhecimento prévio. Falha de processo, autoproteção institucional, supressão deliberada e conhecimento prévio operacional são quatro proposições distintas, cada uma com ônus probatório próprio.
