---
type: concept
slug: flow-pvd-sputtering
canonical_name: PVD / sputtering (process step)
seq: 29
phase: feol
related_concepts:
- pvd-sputtering
- diffusion-barriers
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
- slug: pvd-sputtering
  name: PVD / Sputtering
  path: /manufacturing/equipment-processes/pvd-sputtering/
  macro: manufacturing
- slug: diffusion-barriers
  name: Diffusion Barriers (TiN, TaN)
  path: /materials/coatings-interfaces/diffusion-barriers/
  macro: materials
---
> Step 29 of 56 in the semiconductor flow (FEOL). Prev: [Atomic layer deposition (ALD) (process step)](/semiconductor-process-flow/frontend/flow-ald-atomic-layer-deposition/) · Next: [Chemical-mechanical planarisation (CMP) (process step)](/semiconductor-process-flow/frontend/flow-cmp-planarisation/)

## What this step does
Physical vapour deposition (PVD), almost always done by sputtering, fires energetic argon ions at a solid metal "target" in vacuum, knocking atoms loose so they condense as a thin metal film on the wafer. Unlike ALD or CVD it is a physical, line-of-sight process, so it deposits metals fast and cheaply but conforms poorly to deep features. It is the workhorse for the metal layers that ALD/CVD cannot do economically. Sub-processes inside this step:
- Barrier and liner deposition (Ti/TiN, Ta/TaN) to stop copper diffusing into silicon.
- Copper seed layer, the conductive starter film that electroplating later thickens into the wires.
- Aluminium pads, tungsten/cobalt/ruthenium liners, and back-side or hardmask metal.
- Target conditioning, pre-clean (sputter etch), and degas chambers on the same cluster tool.

## Where it sits and why it matters
PVD is the first metal contact in the interconnect stack: after the via is etched (step before) and before CMP planarises (next). Get the barrier/seed wrong and the copper either voids during plating or poisons the transistor. It is one of the highest value-capture steps in FEOL/BEOL because a single vendor effectively owns the front-end metallisation niche, and because every wafer consumes physical metal targets, giving the step a rare razor-and-blades consumable tail on top of the tool sale.

## Equipment market
The semiconductor-specific PVD equipment market was roughly **$4.2bn in 2024**, forecast to ~$8.5bn by 2033 at ~8.6% CAGR (Verified Market Reports; treat the long-dated forecast as indicative). This is the slice that matters; broad "PVD market" figures of $23-26bn include tool coatings, optics and decorative coatings and should be ignored for chip work.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Applied Materials | US | ~70-85% of front-end metallisation PVD (rough) | Endura platform is the industry gold standard; >4,500 systems shipped; "undisputed leadership" |
| ULVAC | Japan | ~10-15% overall | Strong in Japan/memory and high-throughput tools; perennial #2 |
| Evatec | Switzerland (EU) | low single digits | Advanced packaging, power, MEMS, photonics; CLUSTERLINE family |
| Canon Anelva | Japan | niche | MRAM/magnetic and specialty PVD |
| Singulus | Germany (EU) | niche | PV, sensors, advanced packaging; not leading-edge logic |

Concentration note: this is one of the most concentrated steps in the whole flow. In leading-edge front-end metallisation AMAT is close to a sole supplier; analyst reads put it ~85% there, hence the prompt's framing. Across the broader semiconductor PVD tool market AMAT + ULVAC together hold the clear majority. The ~85% figure is a niche estimate, not a single audited number.

## Materials and consumables
Each tool consumes high-purity (5N-6N+) sputter targets that erode and are replaced every few weeks, plus argon and replacement shields. Target market: **~$1.45bn in 2025**, up 7.3% YoY from ~$1.35bn in 2024, on ~0.77M kg of metal shipped (TECHCET Critical Materials Report, via Semiconductor Digest). Copper, tantalum, titanium, tungsten, cobalt and ruthenium are the workhorse metals; Cu/Al/Ti demand is rising fastest as nodes shrink.

| Consumable vendor | HQ | Notable |
|---|---|---|
| JX Advanced Metals (ex-JX Nippon) | Japan | Market leader; vertically integrated mine-to-target; IPO'd 2025; Isohara plant +35% capacity |
| Solstice Advanced Materials (ex-Honeywell EM) | US | Spun from Honeywell; top-tier high-purity targets |
| Materion | US | High-purity and custom targets (acquired Heraeus target lines) |
| Plansee / Global Tungsten | Austria (EU) | Refractory metal (W, Mo, Ta) targets |
| KFMI | China | Fast-closing challenger on cost |

Recurring-revenue note: targets are a consumable that re-orders for the life of the fab, so the materials pool grows with wafer starts not just capex cycles, smoothing the cyclicality that hits tool vendors.

## Volumes, revenue, profitability
Revenue pool per year: ~$4bn tools + ~$1.5bn targets ≈ **$5.5-6bn**, plus AMAT's service/spares attach. ~0.77M kg of target metal flows through fabs annually. Margins: AMAT runs ~48% gross and ~29% non-GAAP operating company-wide (FY2025, SEC 8-K); PVD tools sit at or above the corporate average given near-monopoly pricing. Target makers earn far thinner margins (commodity-metal pass-through plus a purity/qualification premium), typically high-teens to ~30% gross depending on metal. So the tool vendor (AMAT) captures the fat margin; the materials layer earns a steadier but slimmer cut.

## Competitive landscape and value capture
The moat is qualification lock-in: a barrier/seed recipe is co-developed with the fab over years, and re-qualifying a competing tool risks yield, so incumbents almost never get displaced at leading-edge logic. Value accrues overwhelmingly to AMAT (tool + service), then to the handful of qualified target suppliers (JX, Solstice, Materion, Plansee). EU exposure is real but second-tier: Evatec (Switzerland) and Singulus (Germany) on the tool side in packaging/power/MEMS, Plansee (Austria) on refractory targets. New-entrant tool risk at leading edge is near zero; the live frontier is alternative barrier metals (Ru, Mo) and ALD-vs-PVD substitution at the thinnest liners.

## Market drivers, constraints & trends
Net read: the served pool grows through the late 2020s, faster than the ~8.6% headline if metals-mix and packaging shifts hit, but the materials slice is hostage to one platinum-group metal price.

- **Drivers** — WFE spend is forecast at ~$115.7bn in 2025 (+11%), rising to ~$135bn by 2027 on AI logic and HBM build-out, with sub-2nm equipment spend more than doubling from ~$19bn (2024) to ~$43bn (2028); PVD metallisation rides every advanced wafer [9][10]. Hybrid bonding tooling, where PVD deposits SiCN dielectric and nanotwinned-copper bond pads, is growing ~21% CAGR 2025-2032 (from ~$165m to ~$634m) as 3D stacking displaces solder bumps [11]. Each new metal layer (backside power adds a whole second interconnect stack) is more PVD passes per wafer [12].
- **Constraints** — Ruthenium, the frontier barrier/liner metal, ran a seventh straight supply deficit and rose ~238% in 2025; it is a platinum by-product, so supply cannot flex to chip demand, squeezing the target-makers' thin margin [13]. China's Oct 2025 MOFCOM controls explicitly name sputtering-target materials, with extraterritorial 0.1%-value reach from 1 Dec 2025, a direct chokepoint on the consumables tail [14]. Tool revenue stays cyclical on the WFE capex cycle even as the target re-order stream smooths it [9].
- **Trends & inflections to watch** — Copper-to-ruthenium/molybdenum substitution at 2nm could eliminate the Ta/TaN barrier PVD does today; tripwire: a foundry confirming a barrierless Ru or Mo liner in volume at 2nm/A16 [15][16]. ALD encroaching on the thinnest liners shifts spend off PVD; tripwire: an Endura-class liner replaced by ALD in a 2nm PDK. Backside power going to volume re-rates passes-per-wafer up; tripwire: Intel 18A PowerVia shipping in Panther Lake (2026) and TSMC A16 BSPDN at Q3 2026 both ramping [12].

## Connections
- [PVD / Sputtering](/manufacturing/equipment-processes/pvd-sputtering/) - the technology cluster page (physics, target types, chamber design)
- [Diffusion Barriers (TiN, TaN)](/materials/coatings-interfaces/diffusion-barriers/) - the barrier/liner films this step deposits
- **Deposition Materials Process Market** - thesis on where deposition value pools across the flow

## Sources
1. Verified Market Reports, Semiconductor PVD Equipment Market ($4.2bn 2024 -> $8.5bn 2033, 8.6% CAGR) - https://www.verifiedmarketreports.com/product/semiconductor-pvd-equipment-market/
2. Semiconductor Digest / TECHCET, sputtering target market ($1.45bn 2025, 0.77M kg, +7.3% YoY) - https://www.semiconductor-digest.com/pvd-driven-growth-pushes-sputtering-target-market-forward/
3. Applied Materials, Endura PVD platform and PVD leadership - https://www.appliedmaterials.com/us/en/semiconductor/products/processes/pvd.html
4. Applied Materials FY2025 Q4 8-K, gross ~48% / non-GAAP operating ~28.6% - https://ir.appliedmaterials.com/static-files/4d5a62a2-1796-4d11-ae7c-848c1ed7ea27
5. Spherical Insights, top sputtering target companies (JX, Materion, Honeywell/Solstice, Plansee) - https://www.sphericalinsights.com/blogs/top-20-companies-in-global-sputtering-targets-market-worldwide-2025-market-research-report-2026-2035
6. Evatec AG company overview (Switzerland PVD vendor) - https://evatecnet.com/about-us/company-overview/
7. Singulus Technologies PVD sputtering (Germany) - https://www.singulus.com/pvd-sputtering/
8. Mordor Intelligence / market data, AMAT + ULVAC PVD tool concentration - https://www.mordorintelligence.com/industry-reports/physical-vapor-deposition-pvd-equipment-market
9. SEMI, WFE sales ~$115.7bn 2025 (+11%) rising to ~$135.2bn by 2027 - https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports
10. EE Times, advanced-process capex ~$19bn (2024) to ~$43bn (2028) at 2nm and below - https://www.eetimes.com/ai-drives-capex-chip-equipment-to-record-156b-in-2027/
11. MarketsandMarkets, hybrid bonding market $164.7m (2025) -> $633.9m (2032), 21.2% CAGR - https://www.marketsandmarkets.com/Market-Reports/hybrid-bonding-market-2641237.html
12. Semiconductor Engineering, backside power delivery fab-tool and process implications (Intel 18A PowerVia, TSMC A16) - https://semiengineering.com/backside-power-delivery-creates-fab-tool-thermal-dissipation-barriers/
13. SFA (Oxford) / Strategic Metals Invest, ruthenium ~238% rise in 2025, 7th straight supply deficit, platinum by-product - https://strategicmetalsinvest.com/ruthenium-prices/
14. White & Case, China MOFCOM Oct 2025 export controls naming sputtering-target materials, extraterritorial 0.1% threshold from 1 Dec 2025 - https://www.whitecase.com/insight-alert/china-imposes-extraterritorial-jurisdiction-and-50-rule-export-controls-rare-earth
15. Semiconductor Engineering, copper-to-ruthenium/molybdenum substitution and barrierless liners at 2nm - https://semiengineering.com/the-end-of-copper-interconnects/
16. SputterTargets.net, Co/Ru barrier-layer PVD target selection for 3nm/2nm nodes - https://www.sputtertargets.net/blog/key-pvd-target-guide-for-3nm-2nm-nodes-selecting-cobalt-ruthenium-barrier-layers.html
