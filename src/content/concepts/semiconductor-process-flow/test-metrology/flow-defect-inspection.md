---
type: concept
slug: flow-defect-inspection
canonical_name: Defect inspection & review (process step)
seq: 38
phase: control
related_concepts:
- semiconductor-metrology-inspection
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
- slug: semiconductor-metrology-inspection
  name: Semiconductor Metrology & Inspection
  path: /manufacturing/equipment-processes/semiconductor-metrology-inspection/
  macro: manufacturing
---
> Step 38 of 56 in the semiconductor flow (Control). Prev: [Metrology (CD, overlay, film, OCD) (process step)](/semiconductor-process-flow/test-metrology/flow-metrology-cd-overlay/) · Next: [Parametric / in-line E-test (process step)](/semiconductor-process-flow/test-metrology/flow-parametric-e-test/)

## What this step does
Defect inspection finds physical anomalies on the wafer (particles, scratches, pattern bridges, opens, residue) by scanning the surface and comparing it to a defect-free reference. It answers "is something there that shouldn't be?", which is a different job from metrology's "is the right thing the right size?". A flagged defect is then sent to defect review, where a high-resolution image classifies it so engineers can trace the root cause back to a tool or step. Sub-processes inside this step:
- **Optical inspection** — broadband/laser brightfield and darkfield scanning of patterned and unpatterned (bare) wafers at high throughput to catch yield-killing defects fast.
- **E-beam inspection** — slower, far higher resolution scanning that resolves defects optics physically cannot, including buried/voltage-contrast (electrical) defects in 3D structures.
- **Defect review** — a review SEM revisits each flagged coordinate to image and classify it (often AI-assisted).
- **Defect classification + sampling** — software bins defects, builds wafermaps, and decides which to review; the data feeds yield management.

## Where it sits and why it matters
Inspection runs repeatedly through the flow, after litho, etch, deposition and CMP, both inline in production and heavily in process R&D and ramp, where finding a new defect mode first decides who hits yield first. It is the eyes of the fab: a single uncaught systematic defect can scrap thousands of wafers. Value here is overwhelmingly equipment-led (the tools cost millions each and there is little consumable), which makes it one of the highest-margin, most concentrated niches in all of semiconductor equipment.

## Equipment market
Wafer inspection equipment was roughly $6.9B in 2025 (some syndicated reads put the broader "defect inspection" line at $7.4-7.8B in 2024), growing ~8-9% CAGR, faster than the equipment average because shrinking nodes and 3D/GAA stacks need ever more sensitive inspection [1][3][7]. This is the most KLA-dominated step in the whole flow:

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| KLA | US | ~56% of wafer inspection; >85% of optical | BBP broadband-plasma optical patterned inspectors (~3,000 installed); eSL10 e-beam; review SEMs (eDR) [2][3][4] |
| Applied Materials | US | ~10-19% | Optical + e-beam (SEMVision review, e-beam inspection); lost e-beam share to KLA optical 2022-25 [1][6] |
| Hitachi High-Tech | Japan | mid-single digit | Review SEMs and e-beam inspection; strong Asia service [6][7] |
| Onto Innovation | US | low-single digit | Macro/edge + some defect inspection; mainly metrology [6] |
| ASML / JEOL / Thermo Fisher | NL / Japan / US | small, e-beam-tilted | Multibeam e-beam and SEM platforms; top-5 e-beam club ~41% combined [3][6] |

Concentration note: KLA + AMAT hold >60% of all defect inspection and KLA alone is past 85% in optical, one of the most monopolistic positions in WFE outside EUV litho. E-beam is the contested frontier, growing fastest (~9% CAGR) on multibeam throughput and voltage-contrast needs, and is the one segment where the field is genuinely plural [1][3].

## Materials & consumables
Almost none, which is the point. Inspection tools consume electron-source filaments/cathodes (e-beam columns), calibration/reference wafers, optics and vacuum spares, plus the maintenance and service contract. There is no slurry-style razor-and-blades stream as in CMP. The recurring revenue is service + software: maintenance, applications support and yield-management software (e.g. KLA's Klarity), which is high-margin and sticky but tied to the installed tool base rather than per-wafer consumption.

## Volumes, revenue, profitability
Inspection is sampling-based, not every-wafer, so the volume driver is the number of installed tools and inspection points per flow, not wafer-passes. A leading-edge fab runs dozens of inspection steps and buys tools at $2-10M+ each (e-beam at the top). Revenue pool: ~$6.9-7.8B equipment annually, with KLA's inspection-systems line alone ~$4.3B (51% of KLA's ~$9.8B FY24) [2][5]. Profitability is the headline: KLA runs ~60%+ corporate gross margin and ~40% operating margin, the richest in large-cap WFE, precisely because process control is concentrated, software-attached and mission-critical [2]. The margin is earned by the toolmaker, overwhelmingly KLA.

## Competitive landscape & value capture
The moat is the deepest in equipment: decades of defect-detection physics, the installed base of BBP optical inspectors with thousands of patents, qualification lock-in at every leading-edge fab, and a yield-data flywheel (more installed tools means more defect signatures means better algorithms). Value accrues to the toolmaker, and within that almost entirely to KLA in optical, with the e-beam segment the only place a challenger can win. EU exposure is thin: ASML touches e-beam/multibeam via past acquisitions (HMI) and Carl Zeiss SMT (Germany) supplies the optics/e-beam columns behind several platforms, but there is no EU-headquartered defect-inspection tool champion. Seed-relevant angle is narrow and software/AI-shaped: defect classification, deep-learning review automation, and computational/optical-inspection startups that could be acquired into a platform, rather than a credible new hardware entrant against KLA.

## Market drivers, constraints & trends
Net read: a structurally accelerating served market, growing meaningfully faster than WFE through 2030 on AI-die complexity and advanced packaging, with China the one drag on an otherwise compounding base.

- **Drivers**
  - **AI-die inspection intensity is rising per wafer**: larger AI/HBM dies mean a single flaw scraps proportionally more silicon, so leading-edge logic and DRAM buy more inspection passes per layer. KLA frames a ~15% process-control revenue CAGR off exactly this plus packaging [8]. JPMorgan models a path to ~20% annual process-control growth to 2030 on GAA + backside power delivery [9].
  - **Advanced packaging is the fastest new pool**: KLA's packaging process-control revenue is on track for ~$1B in CY2026, up from ~$635M (2025) and ~$300M the year before, growing in the high-50s percent; share went from <1% three years ago to >6% now [9]. 2.5D/3D, hybrid bonding and heterogeneous integration each add alignment and bond-void inspection that did not exist at this scale before [10].
  - **Node transitions force new sensitivity**: GAA, 3D stacks and High-NA EUV each create defect modes prior tools cannot resolve, with KLA's Gen-4 optical and e-beam aimed at GAA structures [9].

- **Constraints**
  - **China is the live drag**: China fell to ~30% of KLA revenue in Q4 FY25 from ~44% a year earlier, a ~$500M incremental export-control hit, with a further ~20% China decline guided and a 50% domestic-equipment mandate threatening the trailing-edge pool [11].
  - **E-beam throughput ceiling**: single-column e-beam can take hours to days per 300mm wafer, capping how much of the rising defect load can actually be inspected and limiting how fast the highest-margin segment converts demand to revenue [12].
  - **Cyclicality + concentration**: a sampling-driven, equipment-led pool tied to fab capex still rides the WFE cycle, and KLA's >85% optical share leaves the served market's growth hostage to one vendor's roadmap [7].

- **Trends & inflections to watch**
  - **Multibeam e-beam scaling**: multi-column platforms lifted throughput ~28% with ~53% of logic makers expanding deployment in 2024; tripwire = a >100-beam production-qualified inspection tool shipping at a leading-edge logic/DRAM fab [1][12].
  - **High-NA stochastic-defect inspection**: ppt-level stochastic defects make High-NA layers uninspectable by today's optics; tripwire = a named foundry qualifying a dedicated High-NA stochastic-defect inspection flow (the planned 2026-27 High-NA era) [12].
  - **Packaging re-rate**: tripwire = KLA's packaging process-control line printing >$1B in CY2026, confirming the new pool compounds rather than spikes [9][10].

## Connections
- [Semiconductor Metrology & Inspection](/manufacturing/equipment-processes/semiconductor-metrology-inspection/) — the metrology + inspection equipment cluster page
- **Semiconductor Metrology Wedge** — thesis on where value accrues across the metrology/inspection layer

## Sources
1. Seeking Alpha, Applied Materials e-beam inspection lost share to KLA's optical (segment dynamics, AMAT vs KLA) — https://seekingalpha.com/article/4565533-applied-materials-ballyhooed-e-beam-inspection-sector-lost-share-to-klas-optical
2. KLA FY2024 results / 10-K (total revenue ~$9.8B, process control 89%, inspection systems 51% of net sales; corporate margins) — https://ir.kla.com/news-events/press-releases/detail/478/kla-corporation-reports-fiscal-2024-fourth-quarter-results
3. GlobalGrowthInsights, Semiconductor Wafer Defect Inspection System Market (~$7.82B 2024; vendor shares; optical vs e-beam) — https://www.globalgrowthinsights.com/market-reports/semiconductor-wafer-defect-inspection-system-market-115186
4. KLA, BBP broadband-plasma patterned wafer inspection 40th anniversary (~3,000 BBP installed, ~1,000 patents) — https://www.kla.com/esl10-ebeam-inspection
5. Statista, KLA revenue by product 2024 (wafer inspection ~$4.33B) — https://www.statista.com/statistics/1358062/kla-revenue-by-product/
6. GMInsights, Semiconductor Metrology & Inspection Market (KLA/AMAT/Onto/Thermo Fisher/Hitachi ~58% combined; AMAT ~9.8%) — https://www.gminsights.com/industry-analysis/semiconductor-metrology-and-inspection-market
7. Maximize Market Research, KLA wafer inspection (market ~$6.92B 2025 → ~$12.03B 2032, 8.22% CAGR; KLA >56% process control, >85% optical) — https://www.maximizemarketresearch.com/news/kla-corporation-semiconductor-wafer-inspection/
8. The Index Times, KLA process control + AI-die inspection intensity (~15% process-control revenue CAGR; larger AI dies, inspection per wafer rising) — https://www.theindextimes.com/post/klac-kla-s-58-process-control-stranglehold-tightens-as-ai
9. TIKR / JPMorgan KLAC note (packaging process control ~$1B CY2026 vs ~$635M 2025 / ~$300M prior, high-50s% growth, share <1%→>6%; ~20% process-control CAGR to 2030 on GAA + backside power; Gen-4 for GAA) — https://www.tikr.com/blog/kla-corporation-jumped-5-after-jpmorgan-conference-heres-what-klac-stock-could-return
10. KLA, the packaging pivot driving AI chip performance (2.5D/3D, hybrid bonding, heterogeneous integration inspection requirements) — https://www.kla.com/advance/innovation/the-packaging-pivot-driving-ai-chip-performance
11. TrendForce, KLA China demand + export curbs (China ~30% of revenue Q4 FY25 from ~44%; ~$500M incremental hit; ~20% China decline guided) + Fintool, China 50% domestic-equipment mandate — https://www.trendforce.com/news/2025/08/01/news-chip-equipment-giants-tel-kla-flag-weak-china-demand-in-2025-amid-trade-tensions/
12. Semiconductor Engineering, e-beam inspection essential for advanced nodes (single-column throughput hours-to-days/wafer; multibeam ~28% throughput gain, ~53% logic adoption 2024) + Averroes, EUV stochastic-defect detection (ppt-level stochastics, 2026-27 High-NA era timeline) — https://semiengineering.com/e-beam-inspection-proves-essential-for-advanced-nodes/
