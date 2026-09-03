---
type: concept
slug: flow-thermal-oxidation-gate-dielectric
canonical_name: Thermal oxidation & gate dielectric (process step)
seq: 21
phase: feol
related_concepts:
- high-k-dielectrics
- hafnium-oxide
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 9
sources_7d: 1
sources_30d: 2
recent_mentions:
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors:
- slug: high-k-dielectrics
  name: High-K Dielectrics (HfO2, ZrO2)
  path: /materials/functional-layers/high-k-dielectrics/
  macro: materials
- slug: hafnium-oxide
  name: Hafnium Oxide
  path: /materials/functional-layers/hafnium-oxide/
  macro: materials
---
> Step 21 of 56 in the semiconductor flow (FEOL). Prev: [Wafer cleaning & surface prep (process step)](/semiconductor-process-flow/frontend/flow-wafer-cleaning/) · Next: [Photolithography (coat / expose / develop) (process step)](/semiconductor-process-flow/frontend/flow-photolithography/)

## What this step does
This step grows or deposits the thin insulating layer that sits under the transistor gate and separates it from the channel. Two distinct technology families do the work: classic thermal oxidation (grow SiO2 by reacting silicon with oxygen or steam at 800-1100C) for mature nodes, and high-k deposition (lay down hafnium-based oxide a few atomic layers at a time) for leading-edge logic. The same furnace and rapid-thermal hardware also does dopant-activation anneals, silicidation, and densification, so this step is best read as the broad "thermal processing + gate dielectric" budget, not oxide alone.
- Dry/wet thermal oxidation of SiO2 in vertical batch furnaces.
- Rapid thermal oxidation and rapid thermal anneal (RTP/RTA), single-wafer, seconds-scale.
- Atomic layer deposition (ALD) of high-k HfO2 / HfSiO / ZrO2 plus interfacial layer.
- Nitridation, densification and post-deposition anneal of the dielectric stack.

## Where it sits and why it matters
The gate dielectric is the single most performance-critical film in a logic transistor: its thickness and leakage set drive current, power, and how far the node can scale. The industry switched from SiO2 to hafnium high-k at the 45nm node (Intel, 2007) because SiO2 thinned to a couple of atoms leaks too much. Every advanced-logic and DRAM transistor since runs on a high-k stack, and the gate-all-around (GAA) transition at 2nm wraps that dielectric fully around the channel, raising ALD intensity per wafer. So value is migrating from grow-it-in-a-furnace toward deposit-it-atom-by-atom, and from cheap oxygen/steam toward expensive engineered precursors.

## Equipment market
Thermal processing equipment (furnaces, RTP, and the batch-ALD that shares the furnace platform) is a roughly USD 3-4B/year tool segment, growing high-single-digits. The narrow RTP slice was ~USD 1.77B in 2025, projected to USD 3.90B by 2035 (~8.3% CAGR) on the higher estimate, or ~USD 0.7B at the conservative end [1]; the RTP furnace sub-segment is put at USD 741.5M in 2025, ~5.2% CAGR [1]. Single-wafer ALD (the high-k workhorse) is a much larger and faster pool at ~USD 3.1-3.7B in 2025 growing 10-14% [4].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Tokyo Electron (TEL) | Japan | Leader in vertical furnaces/oxidation | Highly automated batch furnace + RTP; broad WFE breadth |
| Kokusai Electric | Japan | ~70% of batch ALD; co-leader in furnaces | Spun out of Hitachi (KKR 2017), IPO'd Tokyo 2024 [3] |
| ASM International | Netherlands | 50-60% of single-wafer ALD at 5-2nm | Dominates high-k metal gate ALD; €839M Q1'25 rev, +26% [4] |
| Applied Materials | US | Strong in RTP/RTA + epi/anneal | Vantage RTP family; scale buyer relationships |
| NAURA / Koyo Thermo / Tempress / Centrotherm | CN / JP / NL / DE | Tail, plus China onshoring | China is ~37% of furnace demand [2] |

Concentration note: top 3 hold >73% of vertical furnaces [2]; ALD is even tighter, effectively a Kokusai (batch) / ASM (single-wafer) duopoly. This is one of the most concentrated value-capture layers in the whole flow.

## Materials & consumables
The recurring spend is the precursor chemistry, plus quartzware, hot-zone parts, and process gases (O2, steam, N2, NH3). The high-k & ALD/CVD metal precursors market was ~USD 0.6-0.67B in 2025, ~6.4-6.7% CAGR to ~USD 0.9-1.0B by 2030-2034 [5]. Hafnium precursors are the largest slice at ~42% of that pool [5]. Underneath sits the hafnium feedstock squeeze: global hafnium output is only ~70-80 t/yr and 99.9% HfCl4 hit ~USD 930/kg in 2025, up ~33% YoY [5] - a thin, concentrated raw-material chokepoint. Precursor supply is recurring (every wafer consumes it), so it behaves like a razor-and-blades annuity against the one-time tool sale.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Merck KGaA (EMD) | Germany | ~21% | 1,200+ qualified precursor formulations [5] |
| Air Liquide | France | ~16% | Ultra-high-purity Hf/Zr precursors, 6N+ [5] |
| Entegris | US | top-5 | +USD 150M Korea capacity expansion [5] |
| ADEKA | Japan | top-5 | Hf precursor JV with Siltronic [5] |
| SK Specialty / SK Materials | South Korea | top-5 | Top-5 combine for ~36% of ALD precursors [5] |

## Volumes, revenue, profitability
Thermal/oxidation/ALD tools sit inside the ~USD 110-120B/yr wafer-fab-equipment (WFE) market; the combined thermal-processing-plus-high-k-ALD tool revenue pool is on the order of USD 6-8B/yr, with consumable precursors adding ~USD 0.6-0.7B/yr of recurring spend on top. A leading-edge fab runs hundreds of oxidation/anneal/ALD passes across its tool fleet; GAA raises ALD cycles per wafer, so per-wafer dielectric value rises even as wafer counts hold. Margins favour the concentrated equipment incumbents: ASM and Kokusai run gross margins in the high-40s to ~50% and operating margins ~25-30% at cycle peak; precursor majors (Merck Electronics, Air Liquide, Entegris) run lower gross margins (~30-45%) but capture sticky, fab-qualified recurring revenue. The margin is earned by the duopoly toolmakers and the qualified-precursor oligopoly, not by the fabs.

## Competitive landscape & value capture
The moat is qualification: a high-k stack is co-developed with the fab over years, and once a Kokusai batch-ALD or ASM single-wafer tool plus a specific Merck/Air Liquide precursor is qualified into a node, switching means re-qualifying the transistor. That locks in both the tool vendor and the precursor supplier and is why these are duopoly/oligopoly structures rather than fragmented markets. Value accrues to (1) ASM and Kokusai on tools and (2) Merck, Air Liquide, Entegris, ADEKA on consumables, with a structural chokepoint at hafnium raw supply. European players are unusually strong here: ASM (NL) and Merck/Air Liquide (DE/FR) are global leaders, the rare flow step where Europe captures core value rather than a fragment.

## Market drivers, constraints & trends
Net read: accelerating. The served pool (single-wafer high-k ALD plus precursors) is in the fastest-growing slice of WFE, pulled by the GAA upgrade and AI logic capacity, with hafnium supply the live swing factor.

- **Drivers** — The FinFET-to-GAA switch raises high-k ALD intensity per wafer: ASM puts the GAA-1 step-up at ~+USD 400M of served market per 100k wafer-starts/month, with the 1.4nm GAA-2 generation adding a further ~USD 450-500M [6]. ASM now forecasts single-wafer ALD growing to USD 4.2-5.0B by 2027 (from USD 2.6B in 2022) at a 10-14% CAGR [6]. GAA plus backside power lifts equipment revenue per 100k wpm from ~USD 6B to ~USD 7B, structural demand independent of unit volume [7]. AI/HPC, HBM and advanced DRAM are steadily lifting high-k/hafnium consumption [8].
- **Constraints** — Hafnium feedstock is the chokepoint: it is only a zirconium by-product (~1t Hf per 50t Zr), global output ~70-75 t/yr, so capacity cannot ramp on demand [9]. China tightened hafnium export controls from H2 2025; overseas prices ran from ~USD 5,000/kg to ~USD 13,115/kg by April 2026 (+140% in ~5 months) [8]. Mature-node furnace/oxidation demand faces China-driven overcapacity (utilisation ~70% in 2024) [10], so the legacy-node half of the pool is the soft spot.
- **Trends & inflections to watch** — Ferroelectric HfO2 (FeFET/eFeRAM) is a potential new demand category for the same ALD base; tripwire: a foundry/IDM announcing HVM (not R&D) eFeRAM, with credible forecasts only 2028-2030 [8]. CFET stacking compounds high-k ALD cycles; tripwire: backside-power insertion at SF2Z/14A in 2027-2028 confirming the next intensity step [7]. Hafnium-free or low-temperature dielectric chemistries; tripwire: a qualified non-Hf high-k entering a leading-edge node, which would relieve the feedstock squeeze [9].

## Connections
- [High-K Dielectrics (HfO2, ZrO2)](/materials/functional-layers/high-k-dielectrics/) - the material class this step deposits
- [Hafnium Oxide](/materials/functional-layers/hafnium-oxide/) - the dominant high-k chemistry and its supply chokepoint
- **Deposition Materials Process Market** - the thesis covering deposition tools + precursor materials value capture
- Adjacent steps: [Wafer cleaning & surface prep (process step)](/semiconductor-process-flow/frontend/flow-wafer-cleaning/) (prev), [Photolithography (coat / expose / develop) (process step)](/semiconductor-process-flow/frontend/flow-photolithography/) (next), [Epitaxial deposition (epi) (process step)](/semiconductor-process-flow/frontend/flow-epitaxy/)

## Sources
1. SNS Insider / Business Research Insights, RTP equipment market 2025-2035. https://www.globenewswire.com/news-release/2026/03/13/3255288/0/en/Rapid-Thermal-Processing-RTP-Equipment-Market-Size-to-Hit-USD-3-90-Billion-by-2035-SNS-Insider.html and https://www.businessresearchinsights.com/market-reports/rapid-thermal-processing-equipment-market-105663
2. ResearchAndMarkets / Valuates, vertical furnace equipment vendors + concentration. https://www.researchandmarkets.com/articles/key-companies-in-semiconductor-vertical-furnace-equipment-market
3. Investing.com Kokusai Electric Q2 FY25 earnings; BALD Engineering on Kokusai batch-ALD share. https://www.investing.com/news/transcripts/earnings-call-transcript-kokusai-electric-beats-q2-2025-forecasts-stock-drops-93CH-4348555 and https://www.blog.baldengineering.com/search/label/Kokusai
4. BALD Engineering / Bits&Chips on ASM ALD share, single-wafer ALD size, Q1'25 revenue. https://www.blog.baldengineering.com/2025/05/asm-international-strengthens-ald.html and https://bits-chips.com/article/asm-projects-doubling-revenues-by-2030/
5. Mordor Intelligence / GM Insights / Market Growth Reports, high-k & CVD/ALD metal precursors market size, hafnium share, supplier shares, Hf feedstock pricing. https://www.mordorintelligence.com/industry-reports/high-k-and-cvd-ald-metal-precursors-market and https://www.gminsights.com/industry-analysis/atomic-layer-deposition-precursors-market and https://www.marketgrowthreports.com/market-reports/high-k-and-cvd-ald-metal-precursor-market-118564
6. ASM International Investor Day / Q1 2026 + BALD Engineering, single-wafer ALD to USD 4.2-5.0B by 2027, GAA served-market step-up (+USD 400M GAA-1, +450-500M at 1.4nm). https://www.nasdaq.com/press-release/asm-hosts-investor-day-increases-2025-revenue-targets-and-provides-guidance-for-2027 and https://www.blog.baldengineering.com/2025/05/asm-international-strengthens-ald.html
7. SemiAnalysis "Clash of the Foundries" + Future Bridge, GAA + backside power equipment revenue ~USD 6B to ~7B per 100k wpm, KLA film/inspection layer step-up, backside-power insertion 2027-2028. https://newsletter.semianalysis.com/p/clash-of-the-foundries and https://future-bridge.us/gate-all-around-gaa-what-it-means-for-future-fab-design/
8. Metal.com + Electronics For U / Semiconductor Engineering, overseas hafnium to ~USD 13,115/kg by April 2026 (+140% in ~5 months from Nov 2025), AI/HPC/HBM/DRAM demand, China export controls H2 2025, ferroelectric HfO2 / eFeRAM commercialisation 2028-2030. https://news.metal.com/newscontent/103938701-From-Stability-to-Surge-The-Overseas-Hafnium-Market-Caught-Between-AI-Demand-and-Supply-Controls and https://semiengineering.com/a-new-memory-contender/
9. Strategic Metals Invest + Legal Era, hafnium as zirconium by-product (~1t per 50t Zr), global output ~70-75 t/yr, China exports down ~90% Jan-Sep 2025. https://strategicmetalsinvest.com/hafnium-price-forecast-2026/ and https://www.legaleraonline.com/amp/europe_n_uk/chinas-export-curbs-result-in-hafnium-prices-skyrocketing-970210
10. EE Times, mature-node foundry overcapacity from China onshoring, utilisation ~70% in 2024. https://www.eetimes.com/mature-node-foundries-face-overcapacity-from-china/
