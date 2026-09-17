# Próximas Fases

Roteiro de continuação da auditoria, na ordem de execução planejada ao final da Fase 1 (ver [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md), seção 9).

**Ordem de execução:** 2A → 2B → 3 → 4. A sequência não é arbitrária: 2A e 2B usam material já desclassificado e de volume tratável, e incidem sobre as hipóteses onde a Fase 1 deixou lacunas explícitas (H5 no nó al-Mihdhar/al-Hazmi; H2/H3 na rede de apoio). A Fase 3 é a mais cara em volume de leitura e só rende depois que as correções da seção 2 de `docs/02` estiverem internalizadas. A Fase 4 depende de material com timestamp que pode exigir pedidos de acesso com prazo longo — vale iniciar os pedidos cedo, mesmo executando a fase por último.

Antes de iniciar qualquer fase, ler [`README.md`](README.md) (hipóteses e escala de confiança), [`docs/02-adversarial-audit-phase1.md`](docs/02-adversarial-audit-phase1.md) (estado atual) e [`SOURCES.md`](SOURCES.md) (o que já foi lido e com que profundidade).

## Fase 2A — MFRs restantes da liberação de 2026

Ler integralmente os 9 MFRs ainda não lidos: Tenet (×3), Clarke (×3), Berger, Scheuer (×2).

**Objetivo específico:** testar o depoimento de Scheuer contra o de Tenet e o de Clarke em dois pontos de fricção já identificados:
- A discrepância 30%/0% na operação de captura de UBL de maio de 1998 (ledger de contradições, item 5).
- O nó al-Mihdhar/al-Hazmi — quem sabia o quê e quando sobre a entrada dos dois nos EUA. Este é o ponto onde a hipótese H5 tem seu melhor caso teórico e que **não foi tocado** na Fase 1.

## Fase 2B — Joint Congressional Inquiry

Ler o relatório integral da Joint Inquiry de 2002 e a Parte Quatro ("28 páginas"), desclassificada em 2016. Comparar com o Capítulo 5 do relatório da Comissão do 11/9.

**Objetivo específico:** avançar H2/H3 — a única forma de sair do "genuinamente não resolvido" nessas duas hipóteses é com material que trate diretamente da rede de apoio a al-Hazmi e al-Mihdhar (Omar al-Bayoumi, Fahad al-Thumairy, Osama Bassnan), que a Fase 1 não tocou.

## Fase 3 — Auditoria técnica profunda (engenharia)

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

Cada nova fase deve seguir o mesmo padrão desta: registrar título completo, autor, data, URL, versão, extensão efetivamente lida, redações e limitações de acesso — antes de qualquer conclusão. Nenhum documento é citado como "lido" se apenas seu resumo, FAQ ou press release foi consultado.
