---
type: concept
slug: flow-crystal-growth-ingot
canonical_name: Crystal growth & ingot (Czochralski/Float-Zone) (process step)
seq: 16
phase: wafer
related_concepts:
- materials-process
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
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors:
- slug: materials-process
  name: Materials & Process
  path: /materials/advanced-materials/materials-process/
  macro: materials
---
> Step 16 of 56 in the semiconductor flow (Wafer). Prev: [Polysilicon (electronic-grade silicon) (process step)](/semiconductor-process-flow/wafer-materials/flow-polysilicon-egs/) · Next: [Wafer slicing, lapping & polishing (process step)](/semiconductor-process-flow/wafer-materials/flow-wafer-slicing-polishing/)

## What this step does
This step turns purified polysilicon feedstock (the 9N+ chunks from the prior step) into a single, defect-free silicon crystal: a cylindrical ingot that is one continuous crystal lattice. Almost all device-grade silicon, and effectively all 300mm wafers, is grown by the Czochralski (CZ) method; Float-Zone (FZ) is a smaller, premium route for high-resistivity power and detector wafers. Sub-processes inside the step:
- Melt the polysilicon in a quartz crucible (CZ) or melt a moving zone of a polysilicon rod with an RF coil, crucible-free (FZ).
- Dip a seed crystal, then pull and rotate it slowly so the melt solidifies onto the seed in a single orientation.
- Control diameter, dopant level (resistivity) and oxygen/defect content; crop and grind the boule to the target diameter.

## Where it sits and why it matters
Crystal growth sets the substrate quality that every downstream transistor inherits: orientation, resistivity, oxygen content, and crystal-defect density. It is the gate between commodity polysilicon and a value-added wafer. Crucially, the conversion of polysilicon to finished wafer costs roughly $22 to $26 per square metre, split about evenly between crystal growth and the later wafering/polishing steps [1]. So crystal growth is on the order of half the value added between feedstock and bare wafer, even though the bare-wafer market itself (~$12-13bn of shipments) is small relative to the $600bn+ chip industry it feeds.

## Equipment market
The honest read: published "crystal furnace" TAMs are unreliable because they fold in solar PV pullers, which dwarf the semiconductor pool. The widely cited "monocrystalline silicon furnace" market of ~$3.4bn in 2024 (12.9% CAGR to ~$7.0bn by 2030) is overwhelmingly solar [2]; the semiconductor-grade CZ/FZ puller pool is a fraction of that, plausibly low-hundreds of millions of dollars a year of new-tool revenue (rough estimate, no clean third-party number isolates it). PVA TePla's whole Semiconductor Systems segment, of which crystal-growing systems are one product line, was EUR 187.6m in 2024 [3], which frames the order of magnitude.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Zhejiang Jingsheng (JSG) | China | Largest by units (solar-led) | Dominant CZ furnace maker; volume sits in solar [2] |
| PVA TePla | Germany | Leader in semiconductor & SiC/specialty crystal pullers | EU-listed; semi segment EUR 187.6m 2024 [3] |
| Ferrotec | Japan/China | Mid | CZ pullers plus broad materials/components |
| Linton Crystal Technologies | USA | Niche | CZ growing equipment, machined-Si and specialty ingots [4] |
| NAURA | China | Growing | Furnaces incl. SiC single-crystal growth [2] |

Concentration note: for semiconductor-grade silicon, value is concentrated in a handful of Western/Japanese specialists (PVA TePla, Ferrotec, Linton, Cyberstar, Mitsubishi); for solar and SiC, Chinese vendors (JSG, NAURA) dominate by volume. The two markets share furnace concepts but are commercially separate.

## Materials & consumables
Each CZ pull consumes the polysilicon charge plus a hot zone of consumables that wear out and recur:
- Fused-quartz crucibles (the melt vessel) - single-use or few-use, 14 to 36 inch diameters. Lead supplier Momentive Technologies (US); also Ferrotec and several Asian makers [5].
- Graphite hot-zone parts: heaters, susceptors, heat shields, insulation. Lead suppliers SGL Carbon (Germany), Toyo Tanso, Tokai Carbon [6].
Recurring-revenue note: consumables are the steadier annuity in this step. Tool sales are cyclical and capex-gated, but every wafer maker burns crucibles and graphite continuously, so the consumables layer (Momentive, SGL) has more durable, less cyclical revenue than the puller OEMs.

## Volumes, revenue, profitability
Global silicon wafer shipments were ~12,178 MSI (million square inches) in 2024, recovering toward ~13,328 MSI in 2025 [7] - these are the wafers that crystal growth feeds. The bare-wafer market is ~$12-13bn of revenue, and crystal growth is roughly half the polysilicon-to-wafer conversion cost [1]. Margins by layer: the value-capturing layer here is mostly the wafer makers themselves (they grow in-house), not the tool vendors. As a proxy for the equipment layer, PVA TePla ran a 21.4% group EBITDA margin in 2024 (EUR 40.2m EBITDA) [3] - healthy for capital equipment but well below front-end litho/etch OEMs. Wafer makers (Shin-Etsu, SUMCO) earn the substrate margin; their economics swing hard with the silicon cycle.

## Competitive landscape & value capture
The defining structural fact: crystal growth is mostly captive. The big wafer makers - Shin-Etsu (~32-33% of 300mm) and SUMCO (~26-27%) [7], plus GlobalWafers, Siltronic, SK Siltron - run their own crystal pullers as a core trade secret. They buy some furnaces but also build and tune their own hot zones, so the merchant puller-OEM revenue pool is thinner than the wafer market implies. Value accrues to (a) the wafer makers, who hold the process know-how and the consolidated, oligopolistic market, and (b) the consumables suppliers who feed every pull. FZ is a defensible premium niche: FZ wafers cost ~30% more than CZ and serve high-voltage power devices (IGBTs, EV inverters), growing ~8% a year [8]. EU/specialty angle: PVA TePla (DE, listed) is the clear European pure-play and the go-to for SiC and specialty-crystal pullers, which matters for the power-electronics and compound-semi build-out.

## Market drivers, constraints & trends
Net read: the served market is cyclical with a structurally higher floor. AI has pulled 300mm wafers from glut to tightness, but the value still accrues to captive wafer makers, and a 2027 correction is the consensus base case.

- **Drivers**
 - AI/datacentre demand has flipped the cycle: Q1 2026 silicon wafer shipments hit 3,275 MSI, up 13.1% year-on-year, led by 300mm for AI logic and HBM [9][10]. SemiAnalysis frames the industry as now in a genuine "silicon shortage" phase, with hyperscaler capex gated by fab/wafer supply, not appetite [11].
 - Node transitions lift wafer spec and price: Shin-Etsu and SUMCO put in JPY 150bn (~$1bn) in 2025 for 200,000 wpm of ultra-flat 2nm/3nm-grade 300mm capacity, and SUMCO is killing 200mm at Miyazaki by late 2026 to shift to AI-grade 300mm [12].
 - Reshoring/sovereignty adds greenfield demand: GlobalWafers opened Sherman, Texas (now a $7.5bn programme) and started Italy's first 300mm plant in Oct 2025 on multi-year STMicro/Infineon deals [12].

- **Constraints**
 - Hard cyclicality: SEMI's base case is +5.1%/+5.4% in 2025/26, a -6.2% correction in 2027, recovery in 2028 [13] — the served market is not a smooth compounder.
 - ASP erosion: all five incumbents have secured greenfield capacity and, under depreciation pressure, will run it hard; Chinese suppliers pivoting from 200mm to 300mm add structural price pressure [13].
 - Captive value capture: the big-5 hold ~85% of 300mm capacity and grow crystals in-house as a trade secret, so the merchant puller-OEM pool stays thin even as wafer demand climbs [12].

- **Trends & inflections to watch**
 - Silicon-shortage re-rating: substrate scarcity could re-price the wafer layer above its historic cyclical band. Tripwire: SEMI quarterly shipments holding double-digit YoY growth into the back-half of 2026 [9][10], rather than rolling over toward the forecast 2027 dip [13].
 - SiC to larger diameters: the 150mm to 200mm shift is underway and Wolfspeed demoed a single-crystal 300mm SiC wafer [14], lifting demand for specialty pullers (PVA TePla). Tripwire: first volume 200mm SiC supply contract or a foundry committing to 300mm SiC.
 - China 300mm entry: Chinese wafer capacity moving into 300mm is the clearest downside catalyst. Tripwire: a Chinese maker qualifying 300mm at a non-Chinese logic/memory fab [13].

## Connections
[Materials & Process](/materials/advanced-materials/materials-process/) · thesis: **Specialty Silicon Non Leading Edge**

## Sources
1. Cost to convert polysilicon to wafer ~$22-26/m2, split ~50/50 between crystal growth and wafering - cited via wafer-cost discussion: https://www.zmsh-semitech.com/the-300mm-silicon-wafer-manufacturing-process-crystal-growth-slicing-and-polishing/ (rough/old industry figure)
2. Monocrystalline silicon furnace market ~$3.36bn 2024, 12.9% CAGR to ~$6.97bn 2030 (solar-heavy); vendor list incl. JSG, NAURA, PVA TePla, Ferrotec, Linton: https://www.marketresearchreports.com/lpi/global-czochralski-monocrystalline-silicon-furnace-market-growth-2024-2030 (report-mill, treat as directional)
3. PVA TePla FY2024: Semiconductor Systems segment EUR 187.6m; group EBITDA EUR 40.2m, 21.4% margin: https://www.pvatepla-cgs.com/en/news/news-detail/news/pva-tepla-with-slight-sales-growth-and-robust-earnings-increase-in-2024/
4. Linton Crystal Technologies, CZ growing equipment: https://www.lintoncrystal.com/products/cz-growing-equipment
5. Momentive Technologies quartz crucibles for silicon crystal growth (14-36 inch): https://www.momentivetech.com/products/crucibles
6. SGL Carbon specialty graphites for semiconductor crystal growth (heaters, susceptors, heat shields): https://www.sglcarbon.com/en/markets-solutions/applications/semiconductor-crystal-growth/
7. Silicon wafer shipments ~12,178 MSI 2024, ~13,328 MSI 2025; Shin-Etsu ~32-33%, SUMCO ~26-27% of 300mm: https://marklapedus.substack.com/p/silicon-wafer-market-upturn-higher
8. Float-Zone silicon wafers ~30% costlier than CZ, ~7.9-8.5% CAGR, power-device driven: https://www.indexbox.io/blog/float-zone-silicon-wafers-market-forecast-points-higher-toward-2035-driven-by-power-semiconductor-demand/
9. SEMI: Q1 2026 silicon wafer shipments 3,275 MSI, up 13.1% YoY on AI datacentre demand: https://ninescrolls.com/news/semi-q1-2026-silicon-wafer-shipments-hit-3-275-msi-up-13-1-year-on-year-on-ai
10. AI and 300mm demand drive 2025 silicon wafer growth (5.4% to ~13,076 MSI, 300mm +7%): https://www.semiconductor-digest.com/ai-and-300mm-demand-drive-2025-silicon-wafer-growth/
11. SemiAnalysis "The Great AI Silicon Shortage" — hyperscaler capex gated by silicon supply: https://newsletter.semianalysis.com/p/the-great-ai-silicon-shortage
12. Wafer-maker capacity moves: Shin-Etsu/SUMCO JPY 150bn for 2nm/3nm ultra-flat 300mm; SUMCO exits Miyazaki 200mm by late 2026; GlobalWafers Sherman ($7.5bn) + Italy 300mm; big-5 ~85% of 300mm: https://www.mordorintelligence.com/industry-reports/semiconductor-silicon-wafer-market
13. SEMI 2025 silicon wafer market — cyclical limits vs structural change; +5.1%/+5.4%/-6.2%/+9.8% 2025-28; ASP erosion, China 300mm pivot: https://www.semi.org/en/blogs/2025-silicon-wafer-market-at-the-threshold-between-cyclical-limits-and-structural-change
14. Wolfspeed FY2026 8-K — 150mm to 200mm SiC transition; single-crystal 300mm SiC wafer demonstrated: https://www.sec.gov/Archives/edgar/data/0000895419/000089541926000012/ex991q2-26.htm
