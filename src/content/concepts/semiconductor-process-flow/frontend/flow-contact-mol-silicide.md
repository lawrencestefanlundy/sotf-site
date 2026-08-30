---
type: concept
slug: flow-contact-mol-silicide
canonical_name: Contact & middle-of-line (silicide, contact fill) (process step)
seq: 32
phase: beol
related_concepts:
- ru-w-co-metallisation
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
- slug: ru-w-co-metallisation
  name: Ru / W / Co Metallisation
  path: /manufacturing/equipment-processes/ru-w-co-metallisation/
  macro: manufacturing
---
> Step 32 of 56 in the semiconductor flow (BEOL). Prev: [Transistor module (FinFET / GAA nanosheet) (process step)](/semiconductor-process-flow/frontend/flow-transistor-module-finfet-gaa/) · Next: [Low-k dielectric (IMD) deposition (process step)](/semiconductor-process-flow/frontend/flow-low-k-imd-deposition/)

## What this step does
The middle-of-line (MOL) connects the just-built transistors (source, drain, gate) up to the first metal wiring layer. It is the most resistance-sensitive, highest-aspect-ratio metal fill in the whole flow, because the contacts are the narrowest plugs on the chip. The sub-processes inside it:
- **Silicide / salicide formation** - deposit a thin metal (Ti, Co, or Ni) onto exposed silicon, anneal so it reacts to a low-resistance silicide (TiSi2, CoSi2, NiSi), then wet-strip the unreacted metal off the oxide. This drops contact resistance to the silicon.
- **Liner / barrier deposition** - a thin TiN (or barrierless scheme) to stop the fill metal diffusing.
- **Contact / plug fill** - fill the contact holes and local interconnect trenches with metal: historically tungsten (W), now transitioning to molybdenum (Mo) and ruthenium (Ru) at leading nodes.
- **CMP** - planarise back to the dielectric before the first IMD layer.

## Where it sits and why it matters
MOL is the resistance bottleneck of a modern transistor. As contacts shrank, the TiN barrier and W nucleation layer started eating most of the available cross-section, so the plug stopped scaling. The industry's answer is barrierless metals: Mo and Ru both wet silicon and oxide well enough to skip (or thin) the barrier, so more of the hole carries current. Lam cites ~30% lower resistivity for Mo thin films versus W [3], and Applied's Ru/Co interconnect scheme claims up to ~25% lower line resistance at 2nm [2]. This is the single biggest live materials transition in the flow, which is exactly why it carries an outsized equipment-and-materials refresh dollar.

## Equipment market
This step is bought as deposition tools (silicide metal PVD/CVD, liner ALD, contact-fill CVD/ALD) plus the anneal (RTP / millisecond / laser) that drives silicidation. There is no clean "MOL tool" SKU; the relevant pools:
- **Metal CVD/ALD deposition** sits inside a CVD+PVD equipment market of ~$13.6B (2025), ~5.9% CAGR to ~$21.6B by 2033 [4]; the ALD slice alone is ~$8.5-12.9B (2025), ~11% CAGR [5][8].
- **RTP / anneal** (silicidation, dopant activation) is a ~$2-3.9B market, ~22% of which is the furnace sub-segment [9].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Applied Materials | US | ~30% of deposition; ~22%+ RTP-furnace, RTP leader | Endura PVD/Ru-Co Barrier Seed IMS; Producer GT millisecond anneal; broadest MOL footprint [2][6][9] |
| Lam Research | US | #2 deposition, leader in W/Mo fill | ALTUS / ALTUS Halo CVD+ALD; first HVM Mo ALD tool (Feb 2025) [1][3] |
| Tokyo Electron (TEL) | JP | top-3 deposition | CVD/ALD and coater/anneal; with AMAT+TEL >50% of deposition [7] |
| ASM International | NL | ALD share leader | ALD for liners/barriers; Ru/high-k ALD adjacency [5] |
| Kokusai Electric | JP | RTP / furnace co-leader | batch and RTP; ~part of the ~77% RTP top-3 [9] |

Concentration note: AMAT + TEL alone hold over half of deposition [7], and AMAT + Mattson + Kokusai hold ~77% of RTP [9]. This is a 3-4 firm oligopoly; the W-to-Mo fill transition is a two-horse race (Lam ALTUS Halo vs Applied) where the incumbent fill leader is defending and the challenger is using the materials switch to take share.

## Materials & consumables
Recurring per-wafer spend is the real annuity here, far stickier than the one-time tool:
- **Precursors** - W (WF6), Mo (MoO2Cl2 and non-fluorinated halides), Ru (organometallic CVD precursors), Ti/Co/Ni silicide metals, TiN barrier precursors. Ru and Mo ALD-grade materials are growing ~12-14% annually [10].
- **Ru / Mo CVD-precursor** demand is ~70-80% driven by leading-edge foundry + DRAM at 7nm and below [10]; the broader ALD/high-k metal-precursor market grows ~9-14% CAGR [10].
- **The metal itself** - Ru is a thin, illiquid precious-metal market; the price moved from ~$450/oz (2024) to ~$603/oz (end-2025) on chip demand [11], so a supply squeeze is a real cost risk, not a rounding error.
- **CMP slurries / pads** for W/Mo/Ru polish, and wet-strip chemistries for the salicide step.
Vendors: Entegris (Mo MoO2Cl2, ProE-Vap delivery) [12], Merck/Versum, Air Liquide Advanced Materials, Linde, TANAKA Precious Metals (Ru), SK Materials, Mitsubishi Gas Chemical, Dow [10]. This is the recurring-revenue layer that compounds with every wafer start.

## Volumes, revenue, profitability
Every logic and advanced-memory wafer goes through MOL, so volume tracks total leading-edge wafer starts (tens of millions of 300mm-equivalent wafers/yr). Within ~$104B of wafer-fab equipment (2025) [7], the metal-deposition-plus-anneal slice attributable to MOL is a high-single-digit-to-low-double-digit billion pool, with the recurring precursor/consumable pull layered on top and growing double digits. Margins: the equipment oligopoly (AMAT, Lam, TEL, ASM) runs ~45-48% gross and ~28-32% operating; precursor/materials specialists (Entegris, Merck EMD) run ~40-45% gross. The margin is earned by the tool vendors (process IP + installed-base lock-in) and the precursor houses (qualified-material switching cost), not by the foundry, which is a price-taker on these inputs.

## Market drivers, constraints & trends
Net read is accelerating: this step sits on the live materials transition AND the AI-capex wave, so its served pool grows faster than the WFE average through the GAA/backside-power ramp.
- **Drivers** — SEMI puts foundry-and-logic equipment spend at ~$75.2B by 2027 with WFE up ~9% in 2026 and ~7.3% in 2027 to a record ~$156B total, driven by AI accelerators and HBM [13][14]; TSMC's N2 GAA entered HVM in Dec 2025 and every new GAA wafer adds MOL contact-fill and silicide steps [15]. RuCo liner cuts barrier thickness 33% to ~20 angstroms and has been adopted by all leading logic makers at the 2nm node, so the Ru pull is already a placed order, not a forecast [16].
- **Constraints** — WFE is cyclical and concentration-heavy: ~75% of 2026-27 leading-edge spend is three regions (Taiwan, Korea, China), so a single foundry capex pause swings the pool [13]. Ru is a thin, illiquid precious-metal feed (a real cost-and-supply chokepoint) [11], and the W-to-Mo/Mo-fill recipe is gated by CMP, purity and EM-reliability qualification that can slip nodes [15].
- **Trends & inflections to watch** — backside power delivery (TSMC A16, H2 2026) and subtractive-Ru/airgap schemes move more current through MOL-grade metal; tripwire: A16 reaching HVM on schedule in 2H26 confirms the backside-MOL metal pull [15]. CFET (imec A7 and below) optionally puts an M0 power rail in the MOL, expanding the step's metal content; tripwire: a foundry committing CFET with an MOL power rail at IEDM-class disclosure [17]. Mo displacing W in contacts/backside: tripwire: a second foundry qualifying Mo fill in HVM after Lam's first HVM Mo ALD tool (Feb 2025) [1][18].

## Connections
- [Ru / W / Co Metallisation](/manufacturing/equipment-processes/ru-w-co-metallisation/)
- [Transistor module (FinFET / GAA nanosheet) (process step)](/semiconductor-process-flow/frontend/flow-transistor-module-finfet-gaa/) · [Low-k dielectric (IMD) deposition (process step)](/semiconductor-process-flow/frontend/flow-low-k-imd-deposition/) · [Atomic layer deposition (ALD) (process step)](/semiconductor-process-flow/frontend/flow-ald-atomic-layer-deposition/) · [CVD / PECVD deposition (process step)](/semiconductor-process-flow/frontend/flow-cvd-pecvd/) · [PVD / sputtering (process step)](/semiconductor-process-flow/frontend/flow-pvd-sputtering/) · [Annealing / rapid thermal processing (process step)](/semiconductor-process-flow/frontend/flow-annealing-rtp/) · [Chemical-mechanical planarisation (CMP) (process step)](/semiconductor-process-flow/frontend/flow-cmp-planarisation/)

- Owning idea: **Deposition Materials Process Market** (materials/process tool layer).

## Sources
1. Lam Research, ALTUS product family / ALTUS Halo Mo ALD - https://www.lamresearch.com/product/altus-product-family/ and https://www.prnewswire.com/news-releases/lam-research-ushers-in-new-era-of-semiconductor-metallization-with-altus-halo-for-molybdenum-atomic-layer-deposition-302379972.html
2. SemiEngineering, "Ruthenium Interconnects On Tap" / Applied Ru-Co Endura - https://semiengineering.com/ruthenium-interconnects-on-tap/
3. BALD Engineering, "Molybdenum: The New Frontier in Semiconductor Metallization (Lam)" - https://www.blog.baldengineering.com/2023/11/molybdenum-new-frontier-in.html
4. Global Growth Insights, Semiconductor CVD and PVD Equipment Market ($13.6B 2025, 5.9% CAGR) - https://www.globalgrowthinsights.com/market-reports/semiconductor-cvd-and-pvd-equipment-market-110733
5. Fortune Business Insights, ALD Equipment Market ($8.5B 2025) - https://www.fortunebusinessinsights.com/atomic-layer-deposition-equipment-market-115241
6. PatentPC / AInvest, AMAT ~30% deposition share - https://patentpc.com/blog/top-chip-making-equipment-companies-asml-applied-materials-and-lam-research-market-data
7. Global Growth Insights WFE Market ($103.8B 2025); deposition concentration - https://www.globalgrowthinsights.com/market-reports/wafer-fab-equipment-wfe-market-115191
8. Market Research Future, ALD Equipment Market (~$12.85B 2025, ~11% CAGR) - https://www.marketresearchfuture.com/reports/atomic-layer-deposition-equipment-market-24147
9. SNS Insider / Industry Research, RTP Equipment Market ($3.9B 2035; AMAT+Mattson+Kokusai ~77%) - https://www.globenewswire.com/news-release/2026/03/13/3255288/0/en/Rapid-Thermal-Processing-RTP-Equipment-Market-Size-to-Hit-USD-3-90-Billion-by-2035-SNS-Insider.html
10. IndexBox, Ruthenium / high-k & ALD-CVD metal precursors (9-14% CAGR; 70-80% leading edge) - https://www.indexbox.io/blog/ruthenium-cvd-precursors-market-forecast-points-higher-toward-2035-driven-by-advanced-semiconductor-node-scaling/
11. Web search aggregate, Ru price $450/oz (2024) to $603/oz (end-2025) - https://www.intelmarketresearch.com/semiconductor-metal-precursor-market-42000
12. Entegris, Molybdenum precursor (MoO2Cl2 / ProE-Vap) - https://www.entegris.com/en/home/resources/industry-insights/molybdenum.html
13. SEMI, "300mm fab equipment double-digit growth 2026/2027" + foundry/logic to $75.2B - https://www.prnewswire.com/news-releases/semi-projects-double-digit-growth-in-global-300mm-fab-equipment-spending-for-2026-and-2027-302730416.html
14. SEMI / EE Times, semiconductor equipment to record ~$156B in 2027 (WFE +9% 2026, +7.3% 2027) - https://www.eetimes.com/ai-drives-capex-chip-equipment-to-record-156b-in-2027/
15. SemiAnalysis, "Clash of the Foundries: GAA + Backside Power at 2nm" (N2 HVM Dec 2025; A16 GAA+backside H2 2026) - https://newsletter.semianalysis.com/p/clash-of-the-foundries
16. SemiEngineering, "Extending Copper Interconnects To 2nm" (RuCo liner -33% to ~20A, adopted by all leading logic at 2nm; subtractive Ru) - https://semiengineering.com/extending-copper-interconnects-to-2nm/
17. imec, "Scaling monolithic CFET across multiple logic technology nodes" (A7/A5/A3; optional M0 power rail in MOL) - https://www.imec-int.com/en/articles/performance-boosters-scale-monolithic-cfet-across-multiple-logic-technology-nodes
18. Entegris, "Molybdenum's role in ultra-fast computing" (Mo across contacts, vias, backside power, selective prefill) - https://blog.entegris.com/molybdenums-role-in-ultra-fast-computing-the-metal-behind-the-speed
