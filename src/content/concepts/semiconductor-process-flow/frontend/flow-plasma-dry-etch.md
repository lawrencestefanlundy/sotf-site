---
type: concept
slug: flow-plasma-dry-etch
canonical_name: Plasma / dry etch (process step)
seq: 23
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
- slug: etch-tools
  name: Etch Tools (ALE, plasma etch)
  path: /manufacturing/equipment-processes/etch-tools/
  macro: manufacturing
---
> Step 23 of 56 in the semiconductor flow (FEOL). Prev: [Photolithography (coat / expose / develop) (process step)](/semiconductor-process-flow/frontend/flow-photolithography/) · Next: [Wet etch / chemical surface prep (process step)](/semiconductor-process-flow/frontend/flow-wet-etch-surface-prep/)

## What this step does
After the resist pattern is printed (Step 22), plasma etch physically and chemically removes the exposed material so the pattern is transferred permanently into the film underneath. A reactive plasma (fluorine, chlorine, oxygen or bromine chemistries) is struck above the wafer; ions are accelerated straight down to give directional ("anisotropic") removal that holds the printed dimension. This is where the wafer's flat 2D pattern becomes a real 3D structure. Sub-processes inside the step:
- Conductor etch (polysilicon, metal gate, tungsten, the channel in gate-all-around).
- Dielectric etch (oxide/nitride contacts, vias, high-aspect-ratio holes for 3D NAND and DRAM capacitors).
- High-aspect-ratio (HAR) etch: very deep, narrow holes/trenches where Lam dominates.
- Atomic layer etch (ALE): self-limiting, one-monolayer-at-a-time removal for the most advanced nodes.
- Deep reactive-ion etch (DRIE / Bosch process) for MEMS, power, and through-silicon vias.

## Where it sits and why it matters
Etch is the twin of lithography. Litho decides where the pattern goes; etch decides whether the pattern survives at the right shape, depth and profile. A leading-edge logic or memory wafer cycles through litho-etch dozens of times. As scaling shifted from shrinking flat features to building tall 3D structures (3D NAND now 200+ layers, gate-all-around transistors, DRAM high-aspect-ratio capacitors), etch difficulty and tool intensity rose faster than litho. Etch and deposition together are the two segments where wafer-fab-equipment (WFE) spend is growing structurally, and they are the heart of the **Deposition Materials Process Market** thesis.

## Equipment market
Etch is one of the largest WFE segments. Sizing varies by definition: narrow "plasma etch equipment" reports cluster around $12-15B (2024), while broad "semiconductor etch equipment" (all dry plus the small wet-etch tail) is put nearer $20-25B. The ~$25B figure is the high end and likely over-counts; a defensible 2024 number is roughly $14-20B, growing ~7-9% CAGR. Treat all report-mill TAMs here with caution. The cleaner anchor is Lam Research's own FY2024 revenue of $14.9B with etch ~55% of it [3][5].

| Vendor | HQ | Est. etch share | Notable |
|---|---|---|---|
| Lam Research | US (Fremont, CA) | ~50-55% | Clear #1; dominates HAR and 3D-NAND etch (90%+), strong in ALE/selective etch [3][5][6] |
| Tokyo Electron (TEL) | Japan | ~20-25% | #2; strong conductor and dielectric etch, gaining at GAA [2] |
| Applied Materials | US (Santa Clara) | ~15-20% | #3; bought Plasma-Therm (2024) for specialty etch; Sculpta/ALE push [1][6] |
| Hitachi High-Tech | Japan | ~5% | Specialty conductor/microwave etch, niche logic strength [2] |
| KLA (SPTS) / Oxford Instruments / Plasma-Therm | UK / UK / US | low single digits | Compound-semi, MEMS, power, R&D, deep-silicon (DRIE) [7] |

Concentration note: this is a near-oligopoly. The top three take roughly 85-90% of revenue, and Lam alone takes about half. The remainder is specialty/compound-semiconductor and research tools, not mainstream leading-edge silicon.

## Materials & consumables
Etch is consumables-heavy, which makes it a recurring-revenue annuity layered on top of the tool sale.
- Etch gases: fluorocarbons (CF4, CHF3, C4F8), NF3, SF6, Cl2, HBr, plus carrier gases. Market ~$2.5B (2024), ~6% CAGR [4]. Suppliers: Linde, Air Liquide, Taiyo Nippon Sanso, SK Materials (SK Specialty), Kanto Denka, Resonac (Showa Denko), Central Glass, OCI [4].
- Chamber consumables: electrostatic chucks, focus rings, edge rings, electrodes, quartz/ceramic/yttria-coated parts that erode under plasma and are replaced on a cadence.
- Spares + service: the installed base of etch tools generates a large, sticky service revenue stream for Lam/TEL/AMAT (Lam's Customer Support Business Group is ~40% of sales) [5].
Recurring-revenue note: gases, rings and service recur every wafer/every campaign, so the materials-and-service pool around etch is structurally less cyclical than the tool pool and is where steady cash compounds.

## Volumes, revenue, profitability
Volume here is best read in chambers and wafer passes, not "units": a modern fab runs hundreds of etch chambers and a leading-edge wafer sees dozens of etch steps. The revenue pool splits into the tool pool (~$14-20B equipment) plus the materials/service annuity (~$2.5B gases plus multi-billion service/spares). Margins of the value-capturing layer (the tool makers): Lam Research FY2024 gross margin ~47%, rising to ~50% by late 2025; operating margin ~30-35% [3][8]. TEL and AMAT sit in similar ranges. Gas suppliers earn industrial-gas-style margins (mid-teens to ~30% gross), well below the toolmakers. The margin sits overwhelmingly with the three equipment oligopolists, and within etch, disproportionately with Lam.

## Market drivers, constraints & trends
Net read: the served etch market should grow faster than overall WFE through 2025-2030 (etch is share-gaining inside WFE, with consensus single-digit-to-low-teens CAGRs depending on definition), because the industry's hardest 3D scaling problems now sit in etch rather than litho [9][11].

- **Drivers** — 3D NAND past 300 layers heading to 400+ and a 1,000-layer roadmap multiplies high-aspect-ratio dielectric-etch passes per wafer; a single channel-etch cuts through hundreds of oxide/nitride layers [12][13]. Gate-all-around at sub-3nm and the move to 6F2/4F2 DRAM add etch steps and tighten control, lifting tool ASPs [9][10]. Backside power delivery introduces ~100:1 via etches needing millitorr-level pressure control, a new high-value etch category [11]. AI/HBM-led memory and leading-edge logic capex is the demand pull; 2025 WFE rose ~11-12% with etch among the weighted segments [14][15].
- **Constraints** — China was ~32% of top-vendor WFE in 2025 and a local-content rule (>=50% domestic WFE on new fabs) directly threatens etch, where NAURA and AMEC are strongest and most credible as import substitutes [15][16]. Export controls cap the China-advanced-node served market [16]. The segment is deeply cyclical and memory-capex-driven, so a NAND/DRAM pause hits etch hard. The top-three oligopoly leaves no greenfield entry room.
- **Trends & inflections to watch** — Cryogenic etch (Lam Cryo 3.0, ~2.5x faster, aimed at 400+ layer NAND) is the enabling shift; tripwire: a memory maker qualifying a 400+ layer node in volume on cryo etch before 2027 [12][13]. ALE spreading from a few critical steps to mainstream (already in ~42% of advanced logic fabs) is the second; tripwire: ALE attach rate crossing ~60% of advanced logic steps [10]. China substitution; tripwire: NAURA/AMEC winning a leading-edge (not trailing) etch tool-of-record before 2028 [16].

## Connections
- Cluster: [Etch Tools (ALE, plasma etch)](/manufacturing/equipment-processes/etch-tools/)
- Process neighbours: [Photolithography (coat / expose / develop) (process step)](/semiconductor-process-flow/frontend/flow-photolithography/) · [Wet etch / chemical surface prep (process step)](/semiconductor-process-flow/frontend/flow-wet-etch-surface-prep/)
- Thesis: **Deposition Materials Process Market**

## Sources
1. Mordor Intelligence / openPR, Plasma & semiconductor etch equipment market size and share (2024), https://www.mordorintelligence.com/industry-reports/plasma-etching-equipment-market and https://www.openpr.com/news/4502605/semiconductor-etch-equipment-market-size-propelled-by-8-7-cagr
2. Yole Group, "Semiconductor equipment: market share reshuffles amid memory demand decline", https://www.yolegroup.com/strategy-insights/semiconductor-equipment-market-share-reshuffles-amid-memory-demand-decline/
3. Statista, Lam Research revenue by segment 2024 (FY24 revenue $14.9B), https://www.statista.com/statistics/1374835/lam-research-revenue-by-segment/
4. Semiconductor etching gas market size and suppliers (Linde, SK Materials, Kanto Denka, etc.), https://www.intelmarketresearch.com/semiconductor-etching-gas-market-22495 and https://www.openpr.com/news/3084502/global-semiconductor-grade-etching-gas-market-analysis
5. Lam Research FY2024 financial results (8-K), https://www.sec.gov/Archives/edgar/data/0000707549/000070754924000099/lrcx_exhibitx991xq4x2024.htm
6. GMInsights, Atomic Layer Etching Equipment Market (ALE ~$1.1B 2024, Lam/AMAT/TEL shares), https://www.gminsights.com/industry-analysis/atomic-layer-etching-equipment-market
7. Oxford Instruments Plasma Technology, compound-semi / MEMS / DRIE etch, https://plasma.oxinst.com/home/production
8. Lam Research FY2025 results (gross margin ~48.7%, op margin ~33-35%), https://newsroom.lamresearch.com/2025-01-29-Lam-Research-Corporation-Reports-Financial-Results-for-the-Quarter-Ended-December-29,-2024
9. Knowledge Sourcing / Mordor, Semiconductor etch equipment market forecast 2025-2030 (~5-7.5% CAGR; GAA + 300+ layer NAND drivers), https://www.knowledge-sourcing.com/report/semiconductor-etch-equipment-market and https://www.mordorintelligence.com/industry-reports/semiconductor-etch-equipment-market
10. GMInsights, Atomic Layer Etching equipment market (~42% of advanced logic fabs using ALE; CD-control + line-edge-roughness gains), https://www.gminsights.com/industry-analysis/atomic-layer-etching-equipment-market
11. Lam Research Akara conductor etch (DirectDrive, GAA + 6F2/4F2 DRAM + 3D NAND) and backside-power ~100:1 vias, https://www.prnewswire.com/news-releases/lam-research-unveils-industrys-most-advanced-conductor-etch-technology-to-date-302380153.html
12. Lam Research Lam Cryo 3.0 cryogenic etch (~2.5x faster, optimised for 400+ layer 3D NAND, ~1,000 etch chambers installed), https://www.prnewswire.com/news-releases/lam-research-introduces-lam-cryo-3-0-cryogenic-etch-technology-to-accelerate-scaling-of-3d-nand-for-the-ai-era-302211557.html
13. Semiconductor Digest / SemiEngineering, etch breakthroughs and 3D NAND scaling toward 1,000 layers, https://www.semiconductor-digest.com/how-etch-breakthroughs-are-tackling-3d-nand-scaling-challenges-on-the-path-to-1000-layers/ and https://semiengineering.com/cryogenic-etch-a-key-enabler-of-3d-nand/
14. Semiconductor Wafer Fab Equipment market (2025 WFE ~$109B; etch among weighted growth segments), https://www.fortunebusinessinsights.com/semiconductor-wafer-fab-equipment-market-113030
15. Electronics Weekly, 2025 WFE vendor revenue up ~12%; growth weighted to H2 across litho/etch/deposition; China ~32% of top-five system sales, https://www.electronicsweekly.com/news/business/2025-wafer-fab-equipment-vendor-revenue-up-12-2026-04/
16. EE Times, China WFE self-sufficiency push (NAURA, AMEC) + >=50% domestic-WFE local-content rule on new fabs; export controls, https://www.eetimes.com/how-china-struggles-to-reach-wfe-self-sufficiency/
