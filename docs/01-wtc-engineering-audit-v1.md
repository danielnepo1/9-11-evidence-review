# Auditoria Técnica — Colapso das Torres Gêmeas e do WTC 7 (v1)

> **Status:** superada em vários pontos pela revisão em [`02-adversarial-audit-phase1.md`](02-adversarial-audit-phase1.md), seção 2 ("O que estava errado, exagerado ou prematuro"). Mantida aqui na íntegra como registro histórico do primeiro passe da auditoria — não como conclusão final.

**Fontes acessadas nesta versão:** páginas-índice do NIST, duas páginas de FAQ técnica do NIST (derivadas dos relatórios NCSTAR, não os relatórios primários em si), o arquivo do Relatório da Comissão do 11/9 (irrelevante para engenharia — trata de resposta emergencial), e resumos/abstracts da literatura de Bažant & Verdure e do relatório Hulsey/UAF. **Nenhum PDF do NCSTAR foi lido integralmente nesta versão.**

---

## 1. Sumário executivo

Os três links fornecidos foram acessados. Dois são páginas-índice do NIST (não os relatórios em si) e um é o arquivo do Relatório da Comissão do 11/9, que não contém análise estrutural: é um documento sobre falhas de inteligência e resposta emergencial, e explicitamente não investiga o mecanismo de colapso. Complementou-se com as duas páginas de FAQ técnicas do NIST e com a literatura revisada por pares sobre colapso progressivo.

Conclusão principal: o colapso das Torres Gêmeas é fisicamente explicável por impacto + incêndio + perda de proteção térmica, sem necessidade de energia externa adicional. O argumento decisivo é energético e é robusto por larga margem: a energia potencial gravitacional armazenada na torre excede a energia de dissipação estrutural disponível em quase uma ordem de grandeza por andar. Não há déficit energético a explicar.

O ponto mais frágil da versão oficial não é o colapso em si, mas a **iniciação**: ela depende criticamente da premissa de que a proteção térmica (SFRM) foi desalojada em larga escala pelo impacto, premissa validada por simulação e por evidência indireta (arqueamento das colunas perimetrais), não por medição direta. O WTC 7 é o caso com menor lastro empírico: nenhuma amostra de aço identificada foi analisada, e o NIST reteve arquivos de entrada do modelo, o que impede replicação independente.

## 2. Documentos analisados

| Documento | Acesso | Conteúdo relevante | Limitação |
|---|---|---|---|
| 9-11commission.gov/report | OK | Cap. 9 (resposta emergencial), cap. 1 (voos) | Mandato é o relato das circunstâncias dos ataques, preparação e resposta imediata. Zero engenharia estrutural. Não é fonte para esta auditoria |
| nist.gov/el/final-reports-nist-world-trade-center-disaster-investigation | OK | Índice dos 43 relatórios NCSTAR 1 (torres, 2005) + NCSTAR 1A/1-9/1-9A (WTC 7, 2008) | Página-índice; PDFs não lidos integralmente |
| nist.gov/world-trade-center-investigation | OK | Escopo, escala (43 relatórios, ~10.000 páginas sobre as torres; 3 relatórios, ~1.000 páginas sobre o WTC 7) | Institucional |
| NIST FAQ Torres (derivado) | OK | Mecanismo, cálculos de conexão, energia, tempos | Formato FAQ, não fonte primária |
| NIST FAQ WTC 7 (derivado) | OK | Coluna 79, expansão térmica, análise de queda livre | Idem |
| Bažant & Verdure (J. Eng. Mech. 2007); Bažant & Le (2008) | Resumos/abstracts | Critério energético de colapso progressivo | Texto integral não lido |
| Hulsey/UAF (2020) | Resumos | Principal dissidência publicada sobre WTC 7 | Relatório integral não lido |

## 3. Mecanismo oficial resumido

**Torres (NCSTAR 1):** o impacto seccionou colunas de sustentação, desalojou a proteção térmica das treliças de piso e colunas, e dispersou querosene por múltiplos andares; os incêndios subsequentes, com temperaturas de até ~1.000 °C, enfraqueceram pisos e colunas desprotegidos até que os pisos cederam e puxaram as colunas perimetrais para dentro, causando arqueamento interno e falha da face sul do WTC 1 e da face leste do WTC 2. O NIST rejeita explicitamente a "teoria da panqueca": a falha das colunas perimetrais arqueadas iniciou o colapso, e esse arqueamento exigia que os pisos permanecessem conectados às colunas.

**Progressão:** não modelada em detalhe pelo NIST. O relatório afirma que, uma vez iniciado, a propagação do colapso era explicável sem a mesma complexidade de modelagem.

**WTC 7 (NCSTAR 1A):** expansão térmica de vigas nos andares inferiores do lado leste; a viga do 13º andar perdeu a conexão com a Coluna 79; cascata de falhas de piso do 13º ao 5º andar deixou a Coluna 79 sem travamento lateral por nove pavimentos; flambagem da Coluna 79, propagação até o penthouse leste, falha das colunas do núcleo de leste para oeste e, por fim, colapso da fachada. Mecanismo dominado por expansão térmica, não por perda de resistência: as colunas atingiram no máximo ~300 °C e apenas as vigas de piso do lado leste ultrapassaram 600 °C.

## 4. Análise física

### 4.1 Energia do impacto vs. energia da estrutura

767-200ER, massa no impacto ≈ 1,3×10⁵ kg; v ≈ 198 m/s (WTC 1) e 242 m/s (WTC 2).

- E_k(WTC 1) = ½ · 1,3×10⁵ · 198² ≈ **2,5 GJ**
- E_k(WTC 2) = ½ · 1,3×10⁵ · 242² ≈ **3,8 GJ**

Energia potencial da torre: m ≈ 5×10⁸ kg, centro de massa ≈ 190 m:
E_p = 5×10⁸ · 9,81 · 190 ≈ **9×10¹¹ J ≈ 900 GJ**

Razão E_k/E_p ≈ **0,3 %**. O impacto sozinho é energeticamente irrelevante para derrubar a torre, consistente com o observado: ambas ficaram de pé por 56 e 102 minutos.

> **Nota de revisão (ver doc 02):** usar a energia potencial *total* da torre como se isso resolvesse a *progressão* do colapso foi um erro identificado na revisão seguinte. O cálculo acima é válido apenas para mostrar que o impacto isolado não derruba a torre — não estabelece nada sobre os estágios posteriores.

### 4.2 Energia térmica

Querosene: ~38.000 L por aeronave ≈ 3×10⁴ kg; PCI ≈ 43 MJ/kg → **~1.300 GJ** de potencial químico, boa parte consumida em segundos nas bolas de fogo.

Carga de incêndio de escritório: ~4.000 m²/andar × 20 kg/m² (equivalente madeira) × 16 MJ/kg ≈ **1.280 GJ por andar**. Seis andares ≈ **7.700 GJ**.

O combustível de escritório supera o querosene em quase uma ordem de grandeza. O querosene foi o **ignitor simultâneo multi-andar**, não a fonte principal de energia.

### 4.3 Aço: temperatura e cinética de aquecimento

O aço não precisa fundir para falhar. A 1.000 °C o aço nu amolece e sua resistência cai a cerca de 10% do valor à temperatura ambiente. A ~600 °C a tensão de escoamento já cai a ~50%.

Aquecimento por capacitância concentrada:

```
dT/dt = h·(A/V)·(T_g − T_s) / (ρ·c)
```

Com h_efetivo ≈ 100 W/m²K, A/V ≈ 100 m⁻¹ (perfis leves de treliça), ρc ≈ 4,7×10⁶ J/m³K:

```
dT/dt ≈ 100 · 100 · 600 / 4,7×10⁶ ≈ 1,3 K/s
```

Aço **desprotegido** leve atinge 600–700 °C em **8 a 15 minutos**. Colunas pesadas do núcleo (A/V ≈ 20 m⁻¹) levam ~4× mais, ainda dentro dos 56–102 minutos disponíveis.

> **Nota de revisão (ver doc 02):** este é um cálculo de capacitância concentrada simplificado. Ele demonstra plausibilidade de *classe* (que aço desprotegido pode atingir essas temperaturas nesse intervalo de tempo), não as temperaturas reais de nenhum elemento específico da estrutura em nenhum instante.

### 4.4 Iniciação do colapso progressivo

Bloco superior do WTC 1 (12 andares, ~3,5×10⁶ kg/andar → 4,2×10⁷ kg), queda de h = 3,7 m:

```
E_disponível = 4,2×10⁷ · 9,81 · 3,7 ≈ 1,5×10⁹ J
```

Energia dissipada pela flambagem inelástica das colunas de um pavimento intacto: Bažant e Zhou obtiveram razão K/W_c ≥ 8,4.

Verificação pelo NIST via capacidade de conexão: capacidade vertical total das conexões de um piso típico ≈ 29.000.000 lb contra carga de 2.500.000 lb, ou 11 andares adicionais em carregamento estático; com fator de amplificação dinâmica 2, no máximo 6 andares. Havia 12 andares acima do ponto de iniciação no WTC 1 e 29 no WTC 2.

> **Nota de revisão (ver doc 02):** a capacidade de conexões de piso, isoladamente, responde apenas se *um* piso poderia deter a queda — não é prova da progressão global. Apresentar isso como "verificação independente convergente" com o critério de Bažant foi inflação retórica corrigida na revisão seguinte.

### 4.5 Tempo de queda

Queda livre de 417 m: t = √(2h/g) = **9,2 s**.

O NIST estimou ~11 s (WTC 1) e ~9 s (WTC 2) para os primeiros painéis externos atingirem o solo. Painéis perimetrais ejetados lateralmente caem fora da estrutura em queda quase livre e não medem a frente de esmagamento. Porções substanciais dos núcleos (≈60 pavimentos do WTC 1 e 40 do WTC 2) permaneceram de pé por 15 a 25 segundos após a iniciação — incompatível com queda livre global.

### 4.6 WTC 7: os 2,25 segundos

Único ponto onde queda livre literal é **admitida pelo próprio NIST**: a face norte desceu 18 pavimentos em 5,4 s (40% mais do que os 3,9 s de queda livre), em três estágios: 0–1,75 s abaixo de g; 1,75–4,0 s em aceleração gravitacional; 4,0–5,4 s desacelerando.

A explicação do NIST é internamente coerente: as colunas exteriores já haviam flambado nos pavimentos inferiores, e o interior já havia colapsado antes. O penthouse leste cai visivelmente antes da fachada.

> **Nota de revisão (ver doc 02):** a queda do penthouse antes da fachada é evidência de falha interna anterior, mas não é automaticamente "o oposto" de toda demolição controlada — apenas exclui o padrão clássico fachada-primeiro.

### 4.7 Pulverização do concreto

Massa de concreto ≈ 1×10⁸ kg. Energia de cominuição até dezenas de µm: ordem de 1–3 kJ/kg → 1–3×10¹¹ J, ou 10–30% da energia gravitacional. Bažant e Le concluem que menos de 10% da energia gravitacional convertida em cinética é suficiente.

## 5. Inconsistências classificadas

**(A) Inconsistência comprovada:** o NIST não conseguiu verificar a alegação de projeto contra impacto de Boeing 707 — não localizou documentação dos critérios usados na análise original da Autoridade Portuária.

**(B) Possível inconsistência, faltam dados:**
1. Desalojamento da SFRM — premissa causal central, sustentada por simulação e inferência, sem medição direta.
2. Progressão do colapso não modelada em detalhe equivalente à iniciação.
3. Seleção do "caso mais severo" por melhor ajuste à evidência observada — ajuste a posteriori.
4. WTC 7 sem amostra de aço identificada.
5. Retenção de arquivos do modelo WTC 7 sob Seção 7d do NCST Act.
6. Modelagem das vigas do WTC 7 sem shear studs, contra figura de artigo de Salvarinas (1986).

**(C) Alegação não sustentada por evidências:**
1. "As torres caíram em queda livre" — falso para as torres; verdadeiro apenas para 2,25 s da fachada do WTC 7.
2. Termita/nanotermita — logisticamente implausível pela quantidade necessária; artigo de Harrit et al. sobre "chips vermelho-cinza" não replicado.
3. Metal fundido do 80º andar do WTC 2 = alumínio da aeronave (hipótese do NIST, não refutada, também não comprovada de forma independente).
4. "Picos sísmicos antes do colapso" — começaram ~10s após o início de cada colapso.
5. "Queda simétrica implica demolição" — para o WTC 7, penthouse cai antes da fachada.

**(D) Já explicado satisfatoriamente:** aço não fundiu; puffs de fumaça por compressão de ar; fumaça preta por combustão incompleta; pessoas nas aberturas em zonas de entrada de ar; sprinklers sem água por tubulação rompida; óleo diesel do WTC 7 insuficiente para o calor observado.

## 6. Conclusão desta versão

É fisicamente explicável sem déficit energético. Pontos mais fracos: premissa de desalojamento de SFRM sem verificação direta; WTC 7 como conclusão forense sem evidência física direta e com arquivos retidos; escolha do caso "mais severo" com circularidade metodológica.

**Dissidência relevante identificada:** estudo Hulsey/UAF (2020, financiado por AE911Truth) concluiu que o fogo não causou o colapso do WTC 7 e que a única forma de queda no modo observado seria falha quase simultânea de todas as colunas — não publicado em periódico de engenharia estrutural com revisão por pares independente até onde verificado nesta sessão.

## 7. Limitações desta versão

- PDFs do NCSTAR não lidos integralmente.
- Relatório Hulsey/UAF não lido integralmente.
- Todos os cálculos da seção 4 são estimativas de ordem de grandeza com incerteza de fator 2–3.
- Nenhum aspecto de Pentágono, Voo 93, inteligência, ou financeiro foi avaliado nesta versão.

## 8. Referências

- Comissão Nacional sobre os Ataques Terroristas: https://www.9-11commission.gov/report/
- NIST, índice dos relatórios finais: https://www.nist.gov/el/final-reports-nist-world-trade-center-disaster-investigation
- NIST, página da investigação: https://www.nist.gov/world-trade-center-investigation
- NIST, FAQ Torres: https://www.nist.gov/world-trade-center-investigation/study-faqs/wtc-towers-investigation
- NIST, FAQ WTC 7: https://www.nist.gov/world-trade-center-investigation/study-faqs/wtc-7-investigation
- Bažant, Z. P. & Verdure, M. (2007), *Journal of Engineering Mechanics* 133(3):308
- Bažant, Z. P. & Le, J.-L. (2008), *Journal of Engineering Mechanics* 134(10):892 e 917
- Hulsey, J. L. et al. (2020), University of Alaska Fairbanks: https://ine.uaf.edu/wtc7
