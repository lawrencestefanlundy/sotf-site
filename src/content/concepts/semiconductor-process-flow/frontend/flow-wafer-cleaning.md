---
type: concept
slug: flow-wafer-cleaning
canonical_name: Wafer cleaning & surface prep (process step)
seq: 20
phase: feol
related_concepts:
- semiconductor-materials-equipment
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
recent_mentions:
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
neighbors:
- slug: semiconductor-materials-equipment
  name: Semiconductor Materials & Equipment
  path: /manufacturing/equipment-processes/semiconductor-materials-equipment/
  macro: manufacturing
---
> Step 20 of 56 in the semiconductor flow (FEOL). Prev: [Wafer foundry / fabrication services (process step)](/semiconductor-process-flow/frontend/flow-foundry-fabrication-services/) · Next: [Thermal oxidation & gate dielectric (process step)](/semiconductor-process-flow/frontend/flow-thermal-oxidation-gate-dielectric/)

## What this step does
Wafer cleaning strips particles, organic residue, native oxide and trace metal ions off the wafer surface before each sensitive step, so contamination does not get baked into the device. It is not one step but a recurring one: a leading-edge wafer is cleaned hundreds of times across its trip through the fab, between almost every deposition, etch, litho and implant. The unit sub-processes inside it:
- Wet bench / immersion cleaning: the classic RCA chemistries, SC-1 (ammonia + hydrogen peroxide, removes particles/organics) and SC-2 (hydrochloric acid + hydrogen peroxide, removes metals), plus a sulfuric-peroxide "piranha" strip.
- Single-wafer spray / spin cleaning: one wafer at a time with dilute chemistries and tighter process control (lower chemical use, less pattern damage) - the format winning share at advanced nodes.
- Megasonic / cryogenic / CO2 particle removal: acoustic energy or solid-CO2 aerosol to lift sub-20nm particles off fragile high-aspect-ratio structures.
- HF native-oxide strip and surface passivation immediately before gate-oxide growth or epi.
- Post-CMP cleaning and drying (IPA / Marangoni dry) to avoid watermarks and pattern collapse.

## Where it sits and why it matters
Cleaning sits everywhere in FEOL: it is the connective tissue between the named process steps rather than a one-time station. Because a single missed particle becomes a killer defect, cleaning is a direct yield lever, and it gets harder every node as features shrink and aspect ratios climb (a 3nm fin will collapse under the surface tension of the wrong dry step). The strategic point for an investor is that cleaning is the highest-frequency consumable event in the fab, which makes the chemicals attached to it one of the stickiest recurring-revenue pools in the entire flow.

## Equipment market
The wafer-cleaning equipment market is roughly US$9-9.3B in 2024, with multi-report consensus around an ~8-9% CAGR toward ~US$18B by 2032 [1][2]. Treat the absolute figure as directional (the report-mill TAMs cluster but are not Yole-grade); the structure is firmer than the decimal. Single-wafer cleaning is the share-gaining format; batch still holds a majority of installed base [1].

| Vendor | HQ | est. share | notable |
|---|---|---|---|
| SCREEN Holdings | JP | leader; ~42% of single-wafer cleaning, ~20-24% of all cleaning | SU-series single-wafer + batch; CO2 cryogenic and low-damage megasonic for advanced nodes [4] |
| Tokyo Electron (TEL) | JP | ~26-30% of overall cleaning | broad wet/single-wafer line; co-leader by total revenue [3][4] |
| Lam Research | US | top-3 | single-wafer wet + the dry-clean adjacency [1][3] |
| SEMES (Samsung) | KR | rising | cost-competitive batch + single-wafer; captive Samsung pull [3] |
| ACM Research | US/CN | ~25-30% of the China wet-clean market | SAPS/TEBO megasonic single-wafer; China local-substitution champion [5] |
| Applied Materials / KLA | US | minority | AMAT wet adjacencies; KLA in clean-linked inspection [1][3] |

Concentration note: the top five (SCREEN, TEL, AMAT, ACM, Lam) held ~65% of 2024 revenue and the broader top group ~90%, so this is a concentrated oligopoly with one clear leader in single-wafer (SCREEN) and a fast-growing China-substitution entrant (ACM) [1][5].

## Materials & consumables
This is where the recurring money is. Cleaning consumes ultra-high-purity wet chemicals on every pass: hydrogen peroxide, sulfuric acid, hydrochloric acid, ammonium hydroxide, hydrofluoric acid (and ultra-high-purity HF specifically), plus dilute IPA for drying [6][7]. The semiconductor wet-chemicals pool is roughly US$3.4-4.3B in 2024 depending on definition, growing ~6-8% CAGR; the broader "electronic wet chemicals" definition runs ~US$4.3B in 2024 toward ~US$8.4B by 2034 [6][7]. Vendors: BASF, Fujifilm (which bought Entegris' electronic-chemicals division for ~US$700M in 2023), Entegris (filtration, fluid handling, drop-in purity), Cabot Microelectronics / CMC Materials (CMP slurries + post-CMP clean, now part of Entegris), Merck/Versum, Mitsubishi Chemical, Stella Chemifa (HF), SK Materials, Solvay, Tokyo Ohka Kogyo, Air Liquide and Linde [6][7]. The recurring-revenue note: a chemistry is qualified into a specific clean recipe and switched only with painful requalification, so once a fab is on your peroxide or HF grade, the spend repeats every wafer for the tool's life. Purity grade (G5 and tighter) is the differentiator, not the molecule.

## Volumes, revenue, profitability
Cleaning is the single most-repeated operation in the fab: a leading-edge wafer can see 100-200+ clean steps across its full process, so per-wafer chemical volume far outstrips most other consumables. With industry wafer starts in the high tens of millions of wafers per year, that is an enormous, non-cyclical consumable annuity layered on a cyclical tool sale. The revenue pool splits into ~US$9B of tools plus ~US$3.5-4.5B of attached wet chemicals (a slice of the broader electronic-chemicals spend). Margins: the equipment leaders earn the fattest cut - SCREEN's SPE segment and TEL run healthy double-digit operating margins, and ACM has grown to ~US$780M revenue riding China installs [5]. Wet chemicals are lower gross (commodity-ish acids/peroxides, roughly 20-35%) but extraordinarily durable; the purity, logistics and on-site bulk-delivery layer (Entegris, Air Liquide, Linde) is where chemical-side value concentrates rather than in the molecule itself. The margin sits with whoever owns the qualified recipe: the tool vendor at install, the chemical/purity major across the tool's life.

## Competitive landscape & value capture
Value capture is split between a concentrated tool oligopoly and a stickier chemicals annuity. On tools, SCREEN's single-wafer dominance is a genuine moat - the cleaning recipe is co-developed with the fab over years and the tool must hit sub-20nm particle and zero-damage targets, so mid-node switching is near-impossible. The most contestable seam is China local-substitution, where ACM Research is funded to take the domestic wet-clean market (already ~25-30%, targeting 60%) [5]. On chemicals, value accrues to purity and supply reliability (a fab cannot run on contaminated peroxide), which favours scaled majors with on-site bulk delivery over a chemistry-only entrant.

## Market drivers, constraints & trends
Net read: steady-to-accelerating on the served market, because cleaning is a per-wafer event whose frequency rises every node, layered on a cyclical tool sale that is now in an AI-led up-leg.

- **Drivers**
 - Node architecture multiplies the step count: GAA in high-volume manufacturing 2025-2027 lifts cleaning-cycle intensity ~15-20% per node generation (sacrificial-nanosheet release, residue strip without collapsing fragile geometry), directly expanding addressable spend per wafer start [8][9]. Single-wafer cleaning, the share-gainer, is already ~55-60% of equipment value [8].
 - AI/HBM and advanced packaging add a new clean-heavy domain: hybrid bonding needs near-atomically clean, particle-free surfaces at sub-micron pitch, and cleaning demand scales with HBM stack count and I/O density (Applied + BESI pushing die-to-wafer hybrid bonding to HVM) [10].
 - The tool up-cycle is real: SEMI puts WFE +11% in 2025 and +9% in 2026, led by DRAM/HBM and AI logic; NAND tool spend +45% in 2025 [11].
- **Constraints**
 - Cyclicality + China concentration: China was ~36% of WFE in 2024, falling toward ~31% as mature-node build moderates; a China air-pocket would hit the equipment line first [11], and ACM's growth is levered to exactly that pool.
 - Chemical chokepoints: >75% of ultra-high-purity HF output sits in three countries; Section 301 tariffs on Chinese high-purity peroxide doubled to 50% on 1 Jan 2025, and lead times have stretched 6+ months, lifting working capital 15-20% [12].
 - PFAS exposure: fluorinated cleaning chemistries fall inside the EU REACH CF2/CF3 restriction; ECHA committee opinions and a Commission decision could force reformulation/substitution with only time-limited semiconductor exemptions [13].
- **Trends & inflections to watch**
 - Dry/cryogenic shift: supercritical-CO2 and cryogenic-aerosol cleaning (zero surface tension, no pattern collapse below ~45nm) move share off pure wet at the most fragile structures. Tripwire: a foundry naming SCCO2/cryo as the qualified clean for a sub-2nm or high-stack 3D-NAND node [14][9].
 - GAA-to-HVM dating: tripwire = TSMC/Samsung/Intel confirming GAA volume ramp in 2025-2026 earnings, which converts the per-node intensity uplift into booked cleaning-tool orders [9].
 - Hybrid-bonding HVM: tripwire = a memory or foundry HBM4/3D-logic line going to volume on hybrid bonding, pulling post-bond clean + activation tools [10].

## Connections
- [Semiconductor Materials & Equipment](/manufacturing/equipment-processes/semiconductor-materials-equipment/) - the parent cluster page for the equipment + materials value chain this step sits in.
- **Deposition Materials Process Market** - thesis on where process-consumable revenue and margin accrue across FEOL.
- [Wafer foundry / fabrication services (process step)](/semiconductor-process-flow/frontend/flow-foundry-fabrication-services/) - prior step; the fab that runs these clean operations between every named step.
- [Thermal oxidation & gate dielectric (process step)](/semiconductor-process-flow/frontend/flow-thermal-oxidation-gate-dielectric/) - next step; the HF strip and surface passivation here are the immediate prep for gate-oxide growth.

## Sources
1. Mordor Intelligence / MarketsandMarkets / Valuates, wafer-cleaning equipment market (~US$9B 2024, ~8-9% CAGR; top-5 ~65% of 2024 revenue; single-wafer share-gaining). https://www.mordorintelligence.com/industry-reports/wafer-cleaning-equipment-market; https://www.marketsandmarkets.com/Market-Reports/microelectronics-cleaning-equipment-market-772.html; https://reports.valuates.com/market-reports/QYRE-Auto-8E1515/global-wafer-cleaning-equipment
2. Credence Research / SkyQuest / SNS Insider, semiconductor wafer-cleaning equipment (~US$9.28B 2024 to ~US$18B 2032, ~8.7% CAGR). https://www.credenceresearch.com/report/semiconductor-wafer-cleaning-equipment-market; https://www.skyquestt.com/report/semiconductor-wafer-cleaning-equipment-market; https://www.snsinsider.com/reports/wafer-cleaning-equipment-market-4371
3. Intel Market Research / Persistence, competitive set (SCREEN, TEL, Lam, KLA, SEMES, ACM; ~90% of revenue in top group; TEL ~26-30% overall). https://www.intelmarketresearch.com/semiconductor-cleaning-device-market-10304; https://www.persistencemarketresearch.com/market-research/semiconductor-wafer-cleaning-systems-market.asp
4. Persistence / Credence, SCREEN single-wafer leadership (~42% single-wafer per Gartner, ~20-24% overall; CO2 cryogenic / megasonic). https://www.persistencemarketresearch.com/market-research/semiconductor-wafer-cleaning-systems-market.asp; https://www.credenceresearch.com/report/semiconductor-wafer-cleaning-equipment-market
5. Kerrisdale Capital / TradingView, ACM Research (~25-30% China wet-clean, targeting 60%; ~US$782M revenue; SAPS/TEBO megasonic). https://www.kerrisdalecap.com/wp-content/uploads/2025/11/ACMR-Update-Kerrisdale.pdf; https://kr.tradingview.com/chart/ACMR/nqbmab9W-ACM-Research-ACMR-Expanding-Share-in-China-s-35B-Semi-Market
6. Custom Market Insights / GlobeNewswire / Mordor, semiconductor wet chemicals (~US$3.4-4.3B 2024, ~6-8% CAGR; BASF, Fujifilm, Entegris, Cabot/CMC, Merck/Versum, Mitsubishi, Shin-Etsu; Fujifilm-Entegris ~US$700M deal 2023). https://www.custommarketinsights.com/report/semiconductor-wet-chemical-market/; https://www.globenewswire.com/news-release/2024/10/10/2961329/0/en/Wet-Chemicals-for-Electronics-and-Semiconductor-Applications-Market-to-Cross-5-39-Billion-by-2032-Driven-by-Increasing-Demand-and-Industry-Expansion.html; https://www.mordorintelligence.com/industry-reports/wet-chemicals-market-for-electronics-and-semiconductor-applications
7. The Brainy Insights / OpenPR / Verified Market Reports, electronic wet chemicals (~US$4.3B 2024 to ~US$8.4B 2034, ~6.85% CAGR; G5+ purity; Mitsubishi Chemical, Stella Chemifa, SK Materials, Solvay; UHP HF). https://thebrainyinsights.com/report/electronic-wet-chemicals-market-14116; https://www.openpr.com/news/2944116/electronic-wet-chemicals-for-semiconductor-market-hits-new-high; https://www.verifiedmarketreports.com/product/g5-grade-wet-electronic-chemicals-market/
8. Future Market Insights / OpenPR, wafer-cleaning equipment growth + single-wafer share (single-wafer ~55-60% of value; ~7.5% CAGR 2026-31; ~US$6.4B 2025). https://www.futuremarketinsights.com/reports/wafer-cleaning-equipment-market; https://www.openpr.com/news/4464953/single-wafer-cleaning-equipment-market-size-share-growth
9. Future Market Insights / Semiconductor Engineering, GAA-driven cleaning intensity (+15-20% cleaning cycles per node; GAA HVM 2025-2027; SCCO2/cryo for sub-45nm 3D structures). https://www.futuremarketinsights.com/reports/wafer-cleaning-equipment-market; https://semiengineering.com/wafer-cleaning-becomes-key-challenge-in-manufacturing-3d-structures/
10. EE Times / Semiconductor Engineering, hybrid bonding cleaning demand (near-atomic clean surfaces, scales with HBM stacks + I/O density; Applied + BESI die-to-wafer hybrid bonding to HVM). https://www.eetimes.com/applied-materials-besi-push-die-to-wafer-hybrid-bonding-toward-high-volume-manufacturing/; https://semiengineering.com/making-hybrid-bonding-better/
11. SEMI / Gartner, WFE forecast + China share (WFE +11% 2025 to ~US$116B, +9% 2026; NAND tools +45% 2025; China ~36% 2024 to ~31% 2026). https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports; https://www.gartner.com/en/documents/7023598
12. Intel Market Research / 24chemicalresearch, wet-chemical supply constraints (>75% UHP HF in three countries; Section 301 50% tariff on Chinese high-purity peroxide from 1 Jan 2025; 6+ month lead times, +15-20% working capital). https://www.intelmarketresearch.com/high-purity-semiconductor-wet-chemicals-market-8055; https://www.24chemicalresearch.com/reports/295800/high-purity-semiconductor-wet-chemicals-market
13. ECHA / White & Case, EU PFAS restriction reaching cleaning chemistries (CF2/CF3 scope; committee opinions + Commission decision; time-limited semiconductor exemptions). https://www.echa.europa.eu/-/echa-publishes-updated-pfas-restriction-proposal; https://www.whitecase.com/insight-alert/europes-pfas-restriction-proposal-moving-forward
14. Tai Kong Kiso / ResearchGate, supercritical-CO2 + cryogenic-aerosol dry cleaning (zero surface tension, no pattern collapse, 3D NAND/FinFET/GAA). https://www.taikkiso.com.tw/en/news/semiconductor-wafer-clean-ssco2/; https://www.researchgate.net/publication/279429097_Cryogenic_Aerosols_and_Supercritical_Fluid_Cleaning
