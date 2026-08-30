---
type: concept
slug: flow-wet-etch-surface-prep
canonical_name: Wet etch / chemical surface prep (process step)
seq: 24
phase: feol
related_concepts:
- etch-tools
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 7
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: etch-tools
  name: Etch Tools (ALE, plasma etch)
  path: /manufacturing/equipment-processes/etch-tools/
  macro: manufacturing
---
> Step 24 of 56 in the semiconductor flow (FEOL). Prev: [Plasma / dry etch (process step)](/semiconductor-process-flow/frontend/flow-plasma-dry-etch/) · Next: [Ion implantation (doping) (process step)](/semiconductor-process-flow/frontend/flow-ion-implantation/)

## What this step does
Wet processing uses liquid chemistry, not plasma, to remove material and to scrub the wafer surface clean between every patterning loop. It is the highest-frequency step in the whole flow: a leading-edge wafer is cleaned hundreds of times across its journey, so wet tools and the chemicals they pour are touched far more often than any single deposition or litho step. Two jobs sit here:
- Wet etch: dissolving a film selectively. Hydrofluoric acid (HF) and buffered oxide etch strip silicon dioxide; hot phosphoric acid removes silicon nitride; SPM (sulfuric-peroxide) strips photoresist.
- Surface prep / clean: removing particles, organic residue, native oxide and metal ions after etch, implant, CMP and resist strip. The workhorse recipe is the RCA clean (SC1 ammonia-peroxide for particles/organics, SC2 hydrochloric-peroxide for metals), plus dilute HF for native-oxide removal.

## Where it sits and why it matters
Every dry-etch, implant and polish step leaves residue and damage; wet clean is what makes the next litho or deposition step printable and defect-free. As nodes shrank, the industry shifted from batch wet benches (up to 50 wafers in a tank) to single-wafer tools, because below roughly the 22nm generation only one-wafer-at-a-time processing gives the particle control and uniformity that yield demands. The economics matter to investors twice: once on the capital tool, and again, recurring, on the litres of ultra-pure chemistry consumed for the life of the fab. This is the cleanest "razor-and-blades" layer in front-end equipment.

## Equipment market
Single-wafer wet cleaning / wet-process equipment was roughly USD 2.1B in 2024, growing about 6.2% CAGR toward ~USD 3.5B by 2033 [1]. The broader "wafer cleaning equipment" definition (single-wafer plus batch plus scrubbers) is larger and analysts project it past USD 15B by 2033 on a high-single-digit CAGR [2]. Treat the report-mill totals as directional; the segment is genuinely growing because clean-step count rises with every node and 3D structure.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| SCREEN (Semiconductor Solutions / Holdings) | Japan | ~45% single-wafer cleaning; #1 also in batch + spin scrubbers | 15,000+ cumulative cleaning units shipped; the category franchise [3][4] |
| Tokyo Electron (TEL) | Japan | #2 | Strong in single-wafer clean + coater/developer adjacency [1] |
| Lam Research | USA | top-3 | Wet + dry portfolio; less dominant in pure clean than in etch/deposition [1] |
| SEMES (Samsung affiliate) | South Korea | meaningful | Captive-plus-merchant supplier; Korea logic/memory base [1] |
| ACM Research | USA / China | rising | SAPS/TEBO megasonic clean; fast China share gains [1] |

Concentration note: this is a concentrated, Japan-anchored oligopoly. SCREEN plus TEL hold the bulk of the single-wafer clean market, with Lam, SEMES and a fast-growing ACM Research filling out the rest. NAURA, Kingsemi and other China-domestic tools are gaining inside China on localisation policy.

## Materials & consumables
This step is the biggest single consumer of wet process chemicals in the fab. The electronic wet chemicals market was about USD 4.1B in 2024 [5], of which semiconductor-grade hydrofluoric acid alone was roughly USD 1.2B in 2024 [6]. Inputs consumed per step: HF and buffered oxide etch, hot phosphoric acid, sulfuric acid + hydrogen peroxide (SPM), ammonia and hydrochloric acid (RCA), isopropyl alcohol for drying, plus the ultra-pure water that dilutes all of it.

| Vendor | HQ | Role |
|---|---|---|
| Stella Chemifa | Japan | Dominant in high-purity / ultra-high-purity HF [6] |
| BASF | Germany | Wet chemicals incl. nitric, ammonium hydroxide (e.g. TSMC supply deal) [5] |
| Kanto Chemical | Japan | Broad high-purity acids and cleans [5] |
| Fujifilm | Japan | Acquired Entegris electronic chemicals 2023; process chemicals [5] |
| Honeywell / Solvay / Mitsubishi Chemical / Avantor | US/EU/Japan | High-purity acids, peroxides, solvents [5][6] |

Recurring-revenue note: chemicals are bought continuously for the fab's whole life, with logistics, purity certification and on-site blending creating switching cost and stickiness. This is where the durable annuity sits, not in the one-time tool.

## Volumes, revenue, profitability
Volume driver is clean-step count: a leading-edge wafer sees on the order of 100+ wet clean operations, so wet tools log the most wafer-passes in the fab. Revenue pool: ~USD 2B/yr single-wafer wet equipment plus ~USD 4B/yr electronic wet chemicals, with the chemicals pool growing on consumables logic rather than capex cycles. Margins: front-end equipment leaders run gross margins in the ~40-50% band and operating margins in the high-teens to ~30% (SCREEN/TEL/Lam profile); electronic specialty chemicals are lower-gross (often ~20-35%) but stickier and less cyclical. The tool vendor earns the cyclical capex margin; the chemicals supplier earns the steadier annuity.

## Competitive landscape & value capture
Moat is process qualification: a cleaning recipe is co-developed with the fab and locked into the process of record, so incumbents (SCREEN, TEL) are extremely hard to displace once designed in. Value accrues to (a) the concentrated Japanese equipment oligopoly on the capital side and (b) the high-purity chemicals suppliers on the recurring side, with HF purity (Stella Chemifa) a genuine choke point. EU / seed-relevant: AP&S International (Germany) builds wet-process and single-wafer systems for specialty/compound-semi and R&D lines, a niche away from the leading-edge oligopoly; the broader European angle is in ultra-high-purity chemicals, fluid handling, filtration and metrology around the wet bench rather than the mainstream cleaning tool itself.

## Market drivers, constraints & trends
Net read: structurally accelerating. Clean is the one step whose count rises mechanically with device complexity, so it grows faster than the wafer-start base even in a flat capex year.

- **Drivers**
  - Step-count inflation is the core engine: complex logic, DRAM and 3D NAND now run 80+ clean steps per wafer, 3D NAND clean-etch-clean loops stretch past 900 process steps, and GAA plus rising layer counts push cleaning intensity up ~15-20% per node generation [7]. Roadmaps toward 1,000-layer 3D NAND by 2030 multiply this again [7].
  - GAA nanosheets need a brand-new selective wet/isotropic etch (SiGe-vs-Si removal to release channels), a net-new recipe family designed into single-wafer tools, with the etch-cleaning sub-segment forecast as the fastest grower at ~14.3% to 2032 [8][7].
  - AI / advanced packaging demand: hybrid bonding requires ISO Class 3 front-end-grade cleanliness where a single 1um particle kills a bond, pulling fab-class wet clean into packaging; hybrid-bonding revenue alone is projected from EUR 36M (2023) to EUR 476M (2026) [9], and ACM Research grew 40% to USD 782M on AI and advanced-packaging clean demand [10].

- **Constraints**
  - PFAS regulation: ECHA's final REACH consultation opened 26 March 2026 with a Commission decision expected 2027; semiconductor fluorinated surfactants and etch chemistries sit in scope with time-limited derogations, raising reformulation cost and supply risk on incumbent chemistries [11].
  - Cyclicality and capex concentration: the tool half rides the WFE cycle, and Asia-Pacific is ~72% of demand with China localisation (ACM, NAURA, Kingsemi) compressing merchant share for SCREEN/TEL inside China [10].
  - Water and chemical intensity: ultra-pure water and high-purity acid consumption per wafer scale with step count, exposing the step to water-scarcity and HF-purity choke-point risk [11].

- **Trends & inflections to watch**
  - Supercritical-CO2 drying is becoming standard to beat capillary pattern collapse on high-aspect-ratio 3D structures; this is a tailwind, not a substitution threat, since the wet-tool vendors sell the sCO2 dry module. Tripwire: a leading-edge fab specifying sCO2 dry as the default finish on a sub-2nm GAA or 1000-layer NAND line [12].
  - Selective-etch recipe wins decide vendor share for the GAA decade. Tripwire: a named single-wafer tool (e.g. SCREEN SU-3200-class) qualified into a foundry's 2nm GAA process of record for SiGe channel release [8].
  - Green / PFAS-free clean chemistry as a forcing-function wedge. Tripwire: a top-5 fab qualifying a PFAS-free surfactant or low-water clean into a production node before the 2027 EU decision [11].

## Connections
[Etch Tools (ALE, plasma etch)](/manufacturing/equipment-processes/etch-tools/) · [Plasma / dry etch (process step)](/semiconductor-process-flow/frontend/flow-plasma-dry-etch/) · [Ion implantation (doping) (process step)](/semiconductor-process-flow/frontend/flow-ion-implantation/)

- Owning idea: **Deposition Materials Process Market** (materials/process tool layer).

## Sources
1. Single Wafer Wet Cleaning Equipment Market (USD 2.1B 2024, 6.2% CAGR to USD 3.5B 2033; vendors list incl. SCREEN, TEL, Lam, SEMES, ACM). https://www.verifiedmarketreports.com/product/single-wafer-wet-cleaning-equipment-market/
2. Wafer Cleaning Equipment Market (broad definition, projected >USD 15B by 2033). https://www.snsinsider.com/reports/wafer-cleaning-equipment-market-4371
3. SCREEN ~45% single-wafer cleaning share estimate (2024). https://matrixbcg.com/products/screen-swot-analysis
4. SCREEN: cumulative cleaning equipment shipments surpass 15,000 units; top global share in single-wafer, batch, spin scrubbers. https://www.screen.co.jp/spe/en/information/spe250701
5. Electronic Wet Chemicals Market (~USD 4.1B 2024; players incl. BASF, Kanto, Fujifilm, Avantor, Mitsubishi, Honeywell, Solvay; BASF-TSMC supply deal). https://www.emergenresearch.com/industry-report/electronic-wet-chemicals-market
6. Semiconductor / Electronic Grade Hydrofluoric Acid Market (~USD 1.2B 2024; Stella Chemifa, Honeywell, Solvay, Morita). https://www.verifiedmarketreports.com/product/semiconductor-grade-hydrofluoric-acid-market/
7. Wafer cleaning as a key challenge in 3D structures (80+ clean steps/wafer; 3D NAND >900 process steps; GAA pushing cleaning intensity +15-20% per node; 1,000-layer 3D NAND by 2030; etch-cleaning fastest-growing sub-segment ~14.3% CAGR 2025-2032). https://semiengineering.com/wafer-cleaning-becomes-key-challenge-in-manufacturing-3d-structures/
8. SiGe-vs-Si selective wet/isotropic etch for GAA nanosheet channel release; single-wafer tool implementation (ACT SG-101 on SCREEN SU-3200). https://www.mdpi.com/2079-4991/15/19/1469
9. Hybrid bonding requires ISO Class 3 front-end cleanliness, 1um particle kills bond; hybrid-bonding revenue EUR 36M (2023) to EUR 476M (2026). https://semiengineering.com/making-hybrid-bonding-better/
10. ACM Research grew 40% to USD 782M on AI + advanced-packaging clean demand; Asia-Pacific ~72% of 2025 revenue; China localisation (SAPS/TEBO, Ultra C Tahoe). https://www.mordorintelligence.com/industry-reports/wafer-cleaning-equipment-market
11. EU PFAS REACH restriction: ECHA final consultation opened 26 Mar 2026, Commission decision expected 2027; etchants/surfactants in scope with semiconductor derogations. https://www.kirkland.com/publications/kirkland-alert/2025/10/pfas-update-scrapping-prior-broader-proposal-eu-publishes-updated-narrower-proposal-to-restrict-the
12. Supercritical-CO2 drying to prevent capillary pattern collapse on high-aspect-ratio 3D / NAND structures (leaning-free at 2x NAND trench AR). https://eureka.patsnap.com/article/pattern-collapse-mitigation-supercritical-co2-drying-techniques
