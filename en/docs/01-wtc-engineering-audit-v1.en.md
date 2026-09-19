> ## 🌐 English companion translation
>
> | | |
> |---|---|
> | **Source (authoritative)** | [`../../docs/01-wtc-engineering-audit-v1.md`](../../docs/01-wtc-engineering-audit-v1.md) (Portuguese) |
> | **Source SHA-256 at translation** | `bcb012dff03a31028fa06f84e186a5014a65b904dc8c0a81d671da52c1f93ce0` |
> | **Translated** | 19 September 2026 |
> | **Status** | Faithful complete translation |
> | **Banner note** | The source carries a one-line English navigation banner pointing here. It is navigation, not content, and is not reproduced in the body below. The hash above is of the source **including** that banner |
>
> The Portuguese original is the authoritative record of Phase A. This is a reader's translation of it. Any disagreement between them is a **translation defect, to be corrected here and never in the original**. See [`../TRANSLATION-POLICY.md`](../TRANSLATION-POLICY.md).
>
> This document is superseded on many points. It is preserved, and translated, as the historical record of the audit's first pass.

---

# Technical Audit — Collapse of the Twin Towers and WTC 7 (v1)

> **Status:** superseded on several points by the revision in [`02-adversarial-audit-phase1.en.md`](02-adversarial-audit-phase1.en.md), section 2 ("What was wrong, overstated or premature"). Kept here in full as the historical record of the audit's first pass — not as a final conclusion.

**Sources accessed for this version:** NIST index pages, two NIST technical FAQ pages (derived from the NCSTAR reports, not the primary reports themselves), the archive of the 9/11 Commission Report (irrelevant to engineering — it deals with emergency response), and summaries/abstracts of the Bažant & Verdure literature and of the Hulsey/UAF report. **No NCSTAR PDF was read in full for this version.**

---

## 1. Executive summary

The three links provided were accessed. Two are NIST index pages (not the reports themselves) and one is the archive of the 9/11 Commission Report, which contains no structural analysis: it is a document about intelligence failures and emergency response, and explicitly does not investigate the collapse mechanism. This was supplemented with the two NIST technical FAQ pages and with the peer-reviewed literature on progressive collapse.

Main conclusion: the collapse of the Twin Towers is physically explicable by impact + fire + loss of thermal protection, with no need for additional external energy. The decisive argument is energetic and is robust by a wide margin: the gravitational potential energy stored in the tower exceeds the available structural dissipation energy by almost an order of magnitude per floor. There is no energy deficit to explain.

The weakest point of the official version is not the collapse itself but **initiation**: it depends critically on the premise that the thermal protection (SFRM) was dislodged on a large scale by the impact, a premise validated by simulation and by indirect evidence (inward bowing of the perimeter columns), not by direct measurement. WTC 7 is the case with the least empirical grounding: no identified steel sample was analysed, and NIST withheld the model's input files, which prevents independent replication.

## 2. Documents analysed

| Document | Access | Relevant content | Limitation |
|---|---|---|---|
| 9-11commission.gov/report | OK | Ch. 9 (emergency response), ch. 1 (flights) | Its mandate is the account of the circumstances of the attacks, preparedness and immediate response. Zero structural engineering. Not a source for this audit |
| nist.gov/el/final-reports-nist-world-trade-center-disaster-investigation | OK | Index of the 43 NCSTAR 1 reports (towers, 2005) + NCSTAR 1A/1-9/1-9A (WTC 7, 2008) | Index page; PDFs not read in full |
| nist.gov/world-trade-center-investigation | OK | Scope, scale (43 reports, ~10,000 pages on the towers; 3 reports, ~1,000 pages on WTC 7) | Institutional |
| NIST Towers FAQ (derived) | OK | Mechanism, connection calculations, energy, timings | FAQ format, not a primary source |
| NIST WTC 7 FAQ (derived) | OK | Column 79, thermal expansion, free-fall analysis | Idem |
| Bažant & Verdure (J. Eng. Mech. 2007); Bažant & Le (2008) | Summaries/abstracts | Energy criterion for progressive collapse | Full text not read |
| Hulsey/UAF (2020) | Summaries | Principal published dissent on WTC 7 | Full report not read |

## 3. The official mechanism, summarised

**Towers (NCSTAR 1):** the impact severed load-bearing columns, dislodged the thermal protection from floor trusses and columns, and dispersed jet fuel across multiple floors; the ensuing fires, with temperatures up to ~1,000 °C, weakened unprotected floors and columns until the floors sagged and pulled the perimeter columns inward, causing inward bowing and failure of the south face of WTC 1 and the east face of WTC 2. NIST explicitly rejects the "pancake theory": the failure of the bowed perimeter columns initiated the collapse, and that bowing required the floors to remain connected to the columns.

**Progression:** not modelled in detail by NIST. The report states that, once initiated, the propagation of the collapse was explicable without the same modelling complexity.

**WTC 7 (NCSTAR 1A):** thermal expansion of beams on the lower floors of the east side; the 13th-floor beam lost its connection to Column 79; a cascade of floor failures from the 13th to the 5th floor left Column 79 without lateral bracing across nine storeys; buckling of Column 79, propagation to the east penthouse, failure of the core columns from east to west and, finally, collapse of the façade. A mechanism dominated by thermal expansion, not by loss of strength: the columns reached at most ~300 °C and only the east-side floor beams exceeded 600 °C.

## 4. Physical analysis

### 4.1 Impact energy vs. structural energy

767-200ER, mass at impact ≈ 1.3×10⁵ kg; v ≈ 198 m/s (WTC 1) and 242 m/s (WTC 2).

- E_k(WTC 1) = ½ · 1.3×10⁵ · 198² ≈ **2.5 GJ**
- E_k(WTC 2) = ½ · 1.3×10⁵ · 242² ≈ **3.8 GJ**

Potential energy of the tower: m ≈ 5×10⁸ kg, centre of mass ≈ 190 m:
E_p = 5×10⁸ · 9.81 · 190 ≈ **9×10¹¹ J ≈ 900 GJ**

Ratio E_k/E_p ≈ **0.3 %**. The impact alone is energetically irrelevant to bringing the tower down, consistent with what was observed: both stood for 56 and 102 minutes.

> **Revision note (see doc 02):** using the *total* potential energy of the tower as if that resolved the *progression* of the collapse was an error identified in the following revision. The calculation above is valid only to show that the impact alone does not bring the tower down — it establishes nothing about the later stages.

### 4.2 Thermal energy

Jet fuel: ~38,000 L per aircraft ≈ 3×10⁴ kg; LHV ≈ 43 MJ/kg → **~1,300 GJ** of chemical potential, much of it consumed in seconds in the fireballs.

Office fire load: ~4,000 m²/floor × 20 kg/m² (wood equivalent) × 16 MJ/kg ≈ **1,280 GJ per floor**. Six floors ≈ **7,700 GJ**.

Office fuel exceeds the jet fuel by almost an order of magnitude. The jet fuel was the **simultaneous multi-floor igniter**, not the principal energy source.

### 4.3 Steel: temperature and heating kinetics

Steel does not need to melt in order to fail. At 1,000 °C bare steel softens and its strength falls to about 10% of its room-temperature value. At ~600 °C the yield stress has already fallen to ~50%.

Lumped-capacitance heating:

```
dT/dt = h·(A/V)·(T_g − T_s) / (ρ·c)
```

With h_effective ≈ 100 W/m²K, A/V ≈ 100 m⁻¹ (light truss sections), ρc ≈ 4.7×10⁶ J/m³K:

```
dT/dt ≈ 100 · 100 · 600 / 4.7×10⁶ ≈ 1.3 K/s
```

Light **unprotected** steel reaches 600–700 °C in **8 to 15 minutes**. Heavy core columns (A/V ≈ 20 m⁻¹) take ~4× longer, still within the 56–102 minutes available.

> **Revision note (see doc 02):** this is a simplified lumped-capacitance calculation. It demonstrates *class* plausibility (that unprotected steel can reach those temperatures in that interval), not the actual temperatures of any specific structural element at any instant.

### 4.4 Initiation of progressive collapse

Upper block of WTC 1 (12 floors, ~3.5×10⁶ kg/floor → 4.2×10⁷ kg), falling h = 3.7 m:

```
E_available = 4.2×10⁷ · 9.81 · 3.7 ≈ 1.5×10⁹ J
```

Energy dissipated by inelastic buckling of the columns of one intact storey: Bažant and Zhou obtained a ratio K/W_c ≥ 8.4.

NIST's check via connection capacity: total vertical capacity of the connections of a typical floor ≈ 29,000,000 lb against a load of 2,500,000 lb, or 11 additional floors under static loading; with a dynamic amplification factor of 2, at most 6 floors. There were 12 floors above the initiation point in WTC 1 and 29 in WTC 2.

> **Revision note (see doc 02):** the capacity of floor connections, on its own, answers only whether *one* floor could have arrested the fall — it is not proof of global progression. Presenting it as "convergent independent verification" of Bažant's criterion was rhetorical inflation, corrected in the following revision.

### 4.5 Fall time

Free fall over 417 m: t = √(2h/g) = **9.2 s**.

NIST estimated ~11 s (WTC 1) and ~9 s (WTC 2) for the first external panels to reach the ground. Perimeter panels ejected laterally fall outside the structure in near free fall and do not measure the crush front. Substantial portions of the cores (≈60 storeys of WTC 1 and 40 of WTC 2) remained standing for 15 to 25 seconds after initiation — incompatible with global free fall.

### 4.6 WTC 7: the 2.25 seconds

The single point where literal free fall is **admitted by NIST itself**: the north face descended 18 storeys in 5.4 s (40% more than the 3.9 s of free fall), in three stages: 0–1.75 s below g; 1.75–4.0 s at gravitational acceleration; 4.0–5.4 s decelerating.

NIST's explanation is internally coherent: the exterior columns had already buckled on the lower storeys, and the interior had already collapsed beforehand. The east penthouse visibly falls before the façade.

> **Revision note (see doc 02):** the penthouse falling before the façade is evidence of prior internal failure, but it is not automatically "the opposite" of every controlled demolition — it only excludes the classic façade-first pattern.

### 4.7 Pulverisation of the concrete

Concrete mass ≈ 1×10⁸ kg. Comminution energy down to tens of µm: of the order of 1–3 kJ/kg → 1–3×10¹¹ J, or 10–30% of the gravitational energy. Bažant and Le conclude that less than 10% of the gravitational energy converted into kinetic energy is sufficient.

## 5. Classified inconsistencies

**(A) Proven inconsistency:** NIST was unable to verify the claim of design against a Boeing 707 impact — it did not locate documentation of the criteria used in the Port Authority's original analysis.

**(B) Possible inconsistency, data missing:**
1. SFRM dislodgement — the central causal premise, sustained by simulation and inference, without direct measurement.
2. Collapse progression not modelled in detail equivalent to initiation.
3. Selection of the "most severe case" by best fit to the observed evidence — post-hoc fitting.
4. WTC 7 with no identified steel sample.
5. Withholding of the WTC 7 model files under Section 7d of the NCST Act.
6. Modelling of the WTC 7 beams without shear studs, against a figure in a Salvarinas paper (1986).

**(C) Claim not sustained by evidence:**
1. "The towers fell at free fall" — false for the towers; true only for 2.25 s of the WTC 7 façade.
2. Thermite/nanothermite — logistically implausible given the quantity required; the Harrit et al. paper on "red-grey chips" not replicated.
3. Molten metal on the 80th floor of WTC 2 = aircraft aluminium (NIST's hypothesis, not refuted, and also not independently proven).
4. "Seismic spikes before the collapse" — they began ~10 s after the start of each collapse.
5. "Symmetric fall implies demolition" — for WTC 7, the penthouse falls before the façade.

**(D) Already satisfactorily explained:** the steel did not melt; smoke puffs from air compression; black smoke from incomplete combustion; people in the openings in air-intake zones; sprinklers without water because of ruptured piping; WTC 7's diesel fuel insufficient for the observed heat.

## 6. Conclusion of this version

It is physically explicable with no energy deficit. Weakest points: the SFRM-dislodgement premise without direct verification; WTC 7 as a forensic conclusion with no direct physical evidence and with files withheld; the choice of the "most severe" case with methodological circularity.

**Relevant dissent identified:** the Hulsey/UAF study (2020, funded by AE911Truth) concluded that fire did not cause the collapse of WTC 7 and that the only way it could have fallen in the observed manner would be near-simultaneous failure of all columns — not published in a structural-engineering journal with independent peer review as far as verified in this session.

## 7. Limitations of this version

- NCSTAR PDFs not read in full.
- Hulsey/UAF report not read in full.
- All section 4 calculations are order-of-magnitude estimates with a factor 2–3 uncertainty.
- No aspect of the Pentagon, Flight 93, intelligence or finance was assessed in this version.

## 8. References

- National Commission on Terrorist Attacks: https://www.9-11commission.gov/report/
- NIST, index of final reports: https://www.nist.gov/el/final-reports-nist-world-trade-center-disaster-investigation
- NIST, investigation page: https://www.nist.gov/world-trade-center-investigation
- NIST, Towers FAQ: https://www.nist.gov/world-trade-center-investigation/study-faqs/wtc-towers-investigation
- NIST, WTC 7 FAQ: https://www.nist.gov/world-trade-center-investigation/study-faqs/wtc-7-investigation
- Bažant, Z. P. & Verdure, M. (2007), *Journal of Engineering Mechanics* 133(3):308
- Bažant, Z. P. & Le, J.-L. (2008), *Journal of Engineering Mechanics* 134(10):892 and 917
- Hulsey, J. L. et al. (2020), University of Alaska Fairbanks: https://ine.uaf.edu/wtc7
