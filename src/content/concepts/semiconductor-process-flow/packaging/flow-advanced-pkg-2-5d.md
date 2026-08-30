---
type: concept
slug: flow-advanced-pkg-2-5d
canonical_name: 'Advanced packaging: 2.5D (CoWoS / EMIB / interposer) (process step)'
seq: 50
phase: assembly
related_concepts:
- cowos
- advanced-packaging
- glass-interposers
- heterogeneous-integration
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
- slug: cowos
  name: CoWoS (TSMC)
  path: /manufacturing/packaging/cowos/
  macro: manufacturing
- slug: advanced-packaging
  name: Advanced Packaging
  path: /manufacturing/packaging/advanced-packaging/
  macro: manufacturing
- slug: glass-interposers
  name: Glass Interposers
  path: /manufacturing/packaging/glass-interposers/
  macro: manufacturing
- slug: heterogeneous-integration
  name: Heterogeneous Integration
  path: /manufacturing/packaging/heterogeneous-integration/
  macro: manufacturing
---
> Step 50 of 56 in the semiconductor flow (Assembly). Prev: [Solder ball attach / BGA (process step)](/semiconductor-process-flow/packaging/flow-solder-ball-bga/) · Next: [Advanced packaging: fan-out (InFO / FOWLP / FOPLP) (process step)](/semiconductor-process-flow/packaging/flow-advanced-pkg-fanout/)

## What this step does
2.5D packaging puts two or more bare dies side-by-side on a shared high-density routing layer so they behave like one chip. The classic case is an AI GPU or ASIC sitting next to stacks of HBM memory, wired together at a pitch no organic board can reach. This is the single tightest physical bottleneck in the AI supply chain right now: you cannot ship an NVIDIA Blackwell or AMD MI-series part without it [1][9]. The sub-processes inside the step:
- Fabricate the interconnect layer: a silicon interposer with through-silicon vias and fine redistribution layers (TSMC CoWoS-S/L), or an embedded silicon bridge dropped into the substrate (Intel EMIB), or an emerging glass interposer [6][9].
- Chip-on-wafer attach: place logic die plus HBM stacks onto the interposer/wafer, usually by thermo-compression bonding (TCB), increasingly by copper hybrid bonding [3].
- Wafer-on-substrate: mount the bonded assembly on a high-end ABF organic substrate, then underfill, mold, and ball-out [9].

## Where it sits and why it matters
This is back-end (assembly), after wafer fab and [Flip-chip bumping (C4 / Cu pillar / microbump) (process step)](/semiconductor-process-flow/packaging/flow-flip-chip-bumping/), feeding [Molding / encapsulation (process step)](/semiconductor-process-flow/packaging/flow-molding-encapsulation/) and final test. It matters because Moore's-law die shrink has stalled while AI demands ever more compute and memory bandwidth per package. 2.5D is how the industry buys performance now: stitch known-good chiplets onto an interposer instead of building one giant reticle-limited die. Value has migrated decisively from the transistor to the package, which is why the foundry that owns 2.5D (TSMC) captures the scarcity rent.

## Equipment market
Advanced-packaging back-end equipment is a small but fast-compounding pool. The two bonding categories that gate 2.5D: thermo-compression bonders were ~$750M in 2025, forecast to ~$936M by 2030 (~11.6% CAGR); copper hybrid bonders ~$152M in 2025 to ~$397M by 2030 (~21.1% CAGR) [3]. Yole frames advanced packaging as the engine pulling total back-end equipment up by ~$1.3B to 2030 [3]. These are rough vendor-reported splits, not audited.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| BESI (Besi) | Netherlands | ~67% of hybrid-bonding tools [3] | Die-based hybrid bonding leader; Applied Materials took a ~9% stake (Apr 2025) [3] |
| EV Group (EVG) | Austria | ~82% of wafer-to-wafer hybrid bonding [3] | EU player; W2W bonding + lithography for interposers |
| ASMPT | Hong Kong / Singapore | strong in TCB (logic) + rising hybrid [3] | Broad bonder + placement line |
| Hanmi Semiconductor | South Korea | TCB leader (esp. HBM) [3] | Dominant TCB bonder for memory stacking |
| Applied Materials | USA | interposer process tools | Deposition/etch/CMP for TSVs + RDL; BESI partner [3] |
| SUSS MicroTec | Germany | lithography / coaters | EU player; panel-level + RDL litho |

Concentration note: bonding is a near-duopoly per modality (BESI in die-level hybrid, EVG in wafer-to-wafer, Hanmi/ASMPT in TCB). High moat from process co-development with TSMC/Intel; new entrants struggle to qualify.

## Materials & consumables
The step consumes the priciest bill-of-materials in all of packaging. The ABF (Ajinomoto Build-up Film) organic substrate alone is 50-70% of package cost, and its ASP rose from ~$65 (2024) to ~$82 (2025), ~26% in a year [9]. This is the recurring-revenue layer: every package burns substrate, interposer wafers, underfill, micro-bumps, and dielectric.

| Material | Vendors | Note |
|---|---|---|
| ABF dielectric resin | Ajinomoto (~95% share) [9] | Single-source choke point for the whole stack |
| ABF substrates | Unimicron (largest), Ibiden, Nan Ya PCB, Shinko | Capacity-constrained; Taiwan/Japan concentrated [9] |
| Silicon interposer wafers | TSMC (captive), UMC, GlobalFoundries | Made in-fab; the interposer IS a wafer-fab product |
| Underfill / micro-bumps / TSV fill | Henkel, Namics, plating chem suppliers | Per-unit consumables, sticky recurring revenue |
| Glass interposer/substrate | Absolics (SKC), SCHOTT, Corning, AGC, Samsung/SEMCO | Emerging; mass production ~2027 [10] |

## Volumes, revenue, profitability
CoWoS is sold out through 2026 [1]. TSMC monthly CoWoS capacity: ~35-40k wafers/month end-2024 → ~70-75k end-2025 → ~125-150k by end-2026, a near-4x build [1][8]. NVIDIA alone has locked 60-70% of total CoWoS capacity for 2025-26 [1][7]. TSMC's quarterly packaging revenue was already ~$3.2B in Q3 2024 [8]. Advanced packaging was ~8% of TSMC revenue in 2024 and crossed >10% in 2025, at a gross margin TSMC says runs above its corporate average (i.e. north of ~55%) [8]. The high-end 2.5D/3D segment is the fastest part of a ~$46B (2024) to ~$80B (2030) advanced-packaging market growing ~9.6% CAGR overall, with the high-performance 2.5D/3D slice forecast to ~$28B by 2029-2030 at ~23-37% CAGR depending on base year [2]. Who earns the margin: the integrating foundry (TSMC) takes the scarcity rent; OSATs (ASE, Amkor, JCET) and the substrate makers earn thinner, capacity-gated margins. Intel's EMIB packaging is pitched at ~40% gross margin, below TSMC's blended take [Intel Foundry].

## Market drivers, constraints & trends
Net read: the served equipment + materials pool keeps accelerating through 2027 because the bottleneck is architectural, not cyclical, but the served market is concentrated on three buyers and a handful of chokepoints.

- **Drivers**
  - AI accelerator wafer demand is forecast to rise ~11x from 2022 to 2026, and CoWoS capacity to compound at a >80% CAGR 2022-2027, dragging the whole back-end tool + consumable pool with it [11][12].
  - The shortage is structural, not a cycle: shortages are now architectural (allocation, not wafer starts, is the binding constraint), so the demand floor holds even if a capex pause hits front-end fabs [14].
  - Capacity is being doubled twice over: TSMC ~120-140k wafers/month in 2026 toward ~160-170k by end-2027, plus ~50-60k of new OSAT capacity, lifting industry capacity toward ~200k/month, every wafer of which burns interposer, substrate, and bonder time [13].

- **Constraints**
  - Demand concentration: NVIDIA, Broadcom and AMD together hold ~85%+ of CoWoS capacity (NVIDIA alone ~60%, ~595k wafers booked), so a single hyperscaler order cut would whipsaw the served market [14].
  - Materials chokepoints stay binding: ABF resin (Ajinomoto ~95%) raised film prices ~30% with the supply-demand gap extending to end-2027 [15]; substrate makers (Unimicron, Kinsus, Nan Ya) are sold out [16].
  - Asymmetric overbuild risk: the substrate market has split into scarce AI-grade vs over-supplied commodity PC-grade; if every announced expansion ships, 2026-27 overcapacity hits the commodity tier first [15].

- **Trends & inflections to watch**
  - Panel-level / CoPoS (Chip-on-Panel-on-Substrate) is the next reticle break. Tripwire: TSMC starting CoPoS production in 2027 alongside Rubin Ultra (~9.5x reticle) confirms the panel transition is real [12][13].
  - Glass-core substrates moving from sample to volume. Tripwire: glass-core revenue clearing ~$460M-scale by 2030 with adoption visibly starting 2027-28 would re-rate the materials pool toward EU/Korea entrants (Absolics, SCHOTT) [10][12].
  - 2.5D bleeding into 3D via hybrid bonding sub-10um. Tripwire: TSMC SoIC face-to-face hybrid bonding at ~6um in production and CoWoS holding 24 HBM stacks targeted for 2029 would shift tool spend from TCB toward hybrid bonders (BESI/EVG) faster than the base case [11][17].

## Connections
[CoWoS (TSMC)](/manufacturing/packaging/cowos/) · [Advanced Packaging](/manufacturing/packaging/advanced-packaging/) · [Glass Interposers](/manufacturing/packaging/glass-interposers/) · [Heterogeneous Integration](/manufacturing/packaging/heterogeneous-integration/) · theses: **Advanced Packaging Market** · **Chiplets Architecture Share** · **Photonic Packaging Cpo**

## Sources
1. ad-hoc-news / TrendForce, TSMC CoWoS ramps toward 140,000 wafers/month, sold out through 2026 — https://www.ad-hoc-news.de/boerse/news/ueberblick/capacity-push-for-ai-tsmc-s-cowos-packaging-ramps-toward-140-000-wafers/69548342
2. Yole Group, Advanced packaging market set to reach $79.4B by 2030 (~9.6% CAGR; high-end 2.5D/3D to ~$28B) — https://www.yolegroup.com/press-release/advanced-packaging-market-set-to-reach-79-4-billion-by-2030/
3. Yole Group, TCB and hybrid bonding to lead $1.3B back-end equipment expansion by 2030 (BESI ~67%, EVG ~82% W2W) — https://www.yolegroup.com/press-release/advanced-packaging-fuels-transformation-in-back-end-equipment-tcb-and-hybrid-bonding-to-lead-1-3-billion-market-expansion-by-2030/
6. TSMC 3DFabric / CoWoS technology page — https://3dfabric.tsmc.com/english/dedicatedFoundry/technology/cowos.htm
7. TrendForce, NVIDIA securing ~70% of 2025 CoWoS-L capacity — https://www.trendforce.com/news/2025/02/24/news-tsmc-reportedly-sees-cowos-order-surge-with-nvidia-securing-70-of-2025-cowos-l-capacity/
8. TrendForce / TSMC filings, advanced packaging ~8% (2024) to >10% (2025) revenue; Q3'24 packaging ~$3.2B — https://www.trendforce.com/news/2024/12/13/news-tsmc-ramps-up-cowos-capacity-across-taiwan-projected-to-nearly-triple-by-2026/
9. Substrates & interposers (ABF $65→$82 ASP; substrate 50-70% of cost; Ajinomoto ~95% resin; Unimicron largest) — https://semiconductorx.com/packaging-substrates-interposers.html
10. TrendForce, glass substrate development; Samsung/SEMCO mass production ~2027; Absolics — https://insights.trendforce.com/p/glass-substrate-development
- Intel: Intel Foundry advanced packaging (EMIB ~40% gross margin; billion-dollar deals; Amkor EMIB partnership) — https://community.intel.com/t5/Blogs/Intel-Foundry/Systems-Foundry-for-the-AI-Era/Intel-Foundry-s-Advanced-Packaging-Enables-Next-Gen-Technologies/post/1719719
- EU: Europe opens advanced-packaging pilot line (Fraunhofer IZM APECS; EVG, SUSS MicroTec) — https://marklapedus.substack.com/p/europe-opens-advanced-packaging-pilot
11. TrendForce, TSMC sees AI wafer demand rising 11x 2022-2026; CoWoS targeting 24 HBM stacks in 2029 — https://www.trendforce.com/news/2026/05/14/news-tsmc-sees-ai-wafer-demand-rising-11x-from-2022-2026-targets-cowos-with-24-hbm-stacks-in-2029/
12. wccftech / TSMC roadmap, CoPoS to replace CoWoS in 2027 with Rubin Ultra (~9.5x reticle); glass core cuts cost ~30%; 9.5x reticle 2027 / 14x 2028 — https://wccftech.com/tsmc-accelerates-copos-packaging-replace-cowos-as-glass-core-substrates-cut-costs-boost-wafer-utilizatio/
13. TrendForce, CoWoS supply-demand gap narrowing 20% to 10% by end-2026; ~120-140k TSMC + ~50-60k OSAT toward ~200k/month; >80% CAGR 2022-2027 — https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/
14. Astute Group / DigiTimes, NVIDIA ~60% of CoWoS (~595k wafers), top-3 ~85%+; shortages architectural not cyclical, allocation is the binding constraint — https://www.astutegroup.com/news/industrial/advanced-packaging-demand-soars-nvidia-secures-60-of-cowos-capacity/
15. AtlasPCB / wccftech, Ajinomoto raises ABF film prices ~30%, supply-demand gap extends to end-2027; AI-grade scarce vs commodity PC over-supply — https://www.atlaspcb.com/news/news-ajinomoto-abf-substrate-price-increase-2026/
16. DigiTimes, ABF substrate sold out for Unimicron, Kinsus, Nan Ya PCB on AI chip demand — https://www.digitimes.com/news/a20260420PD216/revenue-pcb-abf-substrate-unimicron-ai-chip.html
17. SemiAnalysis / nomadsemi (TSMC 2025 symposium), SoIC ~6um face-to-face hybrid bonding in production; hybrid bonding sub-10um in production, ~1um in research — https://www.nomadsemi.com/p/tsmc-2025-technology-symposium
