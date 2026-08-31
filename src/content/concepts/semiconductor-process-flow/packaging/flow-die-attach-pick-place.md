---
type: concept
slug: flow-die-attach-pick-place
canonical_name: Die attach / pick-and-place (process step)
seq: 43
phase: assembly
related_concepts:
- bonding-dicing-equipment
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
parent_concepts:
- packaging
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
- slug: bonding-dicing-equipment
  name: Bonding & Dicing Equipment
  path: /manufacturing/equipment-processes/bonding-dicing-equipment/
  macro: manufacturing
---
> Step 43 of 56 in the semiconductor flow (Assembly). Prev: [Wafer dicing / singulation (process step)](/semiconductor-process-flow/packaging/flow-wafer-dicing-singulation/) · Next: [Wire bonding (process step)](/semiconductor-process-flow/packaging/flow-wire-bonding/)

## What this step does
After the wafer is singulated into individual dies, a die bonder picks each known-good die off the diced tape and places it onto a substrate, leadframe, or another die, then fixes it in place with an adhesive that is cured. This is the gateway from wafer-level work into package assembly, and it sets the placement accuracy budget for everything downstream. The sub-processes inside the step:
- Pick: a collet or ejector lifts the die off the dicing tape without cracking it (thinned dies are fragile).
- Align and place: machine vision registers the die and the bond site; the head places to a target accuracy (microns for standard work, sub-micron for advanced).
- Attach: apply die-attach paste or pre-applied die-attach film (DAF), then thermal or UV cure; high-end flows use thermo-compression bonding (TCB) or, at the frontier, hybrid bonding (no adhesive, direct copper-to-copper plus oxide).

## Where it sits and why it matters
This is where assembly economics and packaging architecture get decided. Standard die attach is a commodity throughput business. But the AI buildout has bifurcated the step: HBM stacks, 2.5D logic-on-interposer and chiplet packages need TCB and hybrid bonding at placement accuracies an order of magnitude tighter than mainstream tools. That frontier is where pricing power and growth have concentrated, while legacy high-speed die bonders ride the broader unit cycle.

## Equipment market
Core die-bonder equipment is roughly a USD 1.0-1.5B annual market, growing low-to-mid single digits in the mainstream tier but far faster (20%+ CAGR) in the TCB/hybrid-bonding frontier [1][6]. Treat the wide report-mill range ($0.98B to $4.8B for "die bonder equipment") as noise from inconsistent scope definitions; the conservative ~$1B figure for classic die bonders is the defensible anchor [1][6]. Hybrid-bonding equipment alone is ~$165M in 2025 heading toward ~$600M+ by 2030-2032 at >20% CAGR [4].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Besi (BE Semiconductor) | Netherlands | ~24-39% (scope-dependent) | Hybrid-bonding leader; 63% gross margin; AI/2.5D order surge [2][6] |
| ASMPT | Singapore / Hong Kong | ~20% | TCB + high-end die bonders; AP revenue $532M, +30% YoY [3] |
| Kulicke & Soffa | US / Singapore | mid-single % in die attach | Wire-bond leader pivoting into TCB for advanced packaging [3] |
| Shinkawa (Yamaha) | Japan | niche/high-precision | Acquired by Yamaha Motor; precision and flip-chip [6] |
| Fasford, Toray Eng., Panasonic | Japan | niche each | Mechanical robustness, automotive 20-yr tool life [6] |

Concentration note: a tight oligopoly. Besi and ASMPT capture the bulk of the value, with Besi dominant in the hybrid-bonding frontier and ASMPT leading TCB. European exposure is unusually strong here (Besi is Dutch), a rarity in back-end equipment.

## Materials & consumables
The step consumes die-attach paste (silver-filled epoxy or sinter paste for power/thermal), die-attach film (DAF), and increasingly dicing-die-attach film (DDF, a two-in-one tape that serves both singulation and bonding). The die-attach materials market is roughly $2.0-2.5B in 2025 at ~5.5-8% CAGR; the DDF film slice alone is ~$2.3B in 2025 heading to ~$4.4B by 2034 at ~7.3% CAGR [5][7][8]. Vendors: Henkel (Loctite, ~18-20% of die-attach materials) leads; Resonac (ex-Hitachi Chemical), Nitto Denko, Dexerials and Lintec together hold ~52-58% [5]. Recurring-revenue note: unlike the lumpy capex of die bonders, materials are a per-wafer consumable that scales with production volume, so this is the stickier, more annuity-like layer of the step.

## Volumes, revenue, profitability
Volumes scale with die count, not wafer count: a single advanced package can stack 8-12+ HBM dies, and chiplet packages place many dies per substrate, so die-placement operations run into the trillions per year industry-wide. The combined revenue pool for the step (equipment + materials) is roughly $3-4B/yr. Profitability splits sharply: Besi posted 2025 gross margin of 63.3% and operating margin of 29.3% on EUR 591M revenue, the kind of margin that signals a frontier-tool monopoly-ish position [2]. ASMPT, weighted toward mainstream plus TCB, runs leaner at ~38% gross margin [3]. Materials vendors (Henkel, Resonac) earn typical specialty-chemical margins, lower headline gross than frontier equipment but with the annuity quality. The margin accrues to the firm holding the accuracy frontier: hybrid bonding for Besi, TCB for ASMPT and K&S.

## Market drivers, constraints & trends
Net read: the served market (equipment + materials) accelerates over the next 2-5 years, but the growth is concentrated in the AI-packaging frontier and paced by two architecture inflections, not the broad unit cycle.

- **Drivers**
  - AI advanced-packaging capex is the dominant pull: TSMC is quadrupling CoWoS toward ~130k wafers/month by late 2026, roughly 10x its 2023 footprint, with die bonders and hybrid bonders called out as capacity-constrained bottlenecks [9][10]. Advanced packaging overall is forecast at ~$65B by 2027 (+74% vs 2021) [9].
  - HBM stack heights pushing past 12-16 layers force every stack onto thermo-compression bonding (TCB) today, multiplying high-precision placements per package [11][12].
  - K&S is expanding TCB to support ~$400M annual system sales and lifting FY26 capex; ASMPT's fluxless AOR TCB is winning HBM qualification, a direct read on frontier demand [12][3].
  - Power/automotive: SiC MOSFET migration and 800V EV architectures (junction temps >200C) force silver-sinter die attach, the fastest-growing material slice at ~10-15% CAGR; >65% of sinter demand is power electronics [13].
- **Constraints**
  - Demand is tightly coupled to one cycle (AI/HBM datacentre capex); a hyperscaler capex pause re-rates the frontier tier hard, and mainstream die bonders already ride a slow unit cycle.
  - Equipment is lumpy capex, not annuity, so the equipment pool is cyclical even while materials stay sticky.
  - Hybrid-bonding adoption is being deferred (see below), so the highest-margin tool category grows from a small base and is exposed to slip risk.
- **Trends & inflections to watch**
  - Hybrid bonding postponed: JEDEC lifted the HBM4 height limit to 775um, letting HBM4 stay on microbumps/TCB; mass hybrid-bonding adoption now slides to HBM5 ~2028-2029 [11]. Tripwire: SK Hynix's $3.87B Indiana hybrid-bonding plant reaching production in 2028 [11] confirms the shift on schedule.
  - Pitch scaling: 6um hybrid-bond pitch is the 2026 high-volume standard, with 4um and 3um in test for late-2026 deployments [14]. Tripwire: a 3um-pitch die-to-wafer line qualified for production confirms the density curve accelerating.
  - In-line metrology folding into the bonder head (e.g. real-time X-ray die-to-wafer alignment correction) [14]. Tripwire: a metrology-integrated bonder shipped in volume signals the accuracy frontier (and its pricing power) moving again.

## Connections
[Bonding & Dicing Equipment](/manufacturing/equipment-processes/bonding-dicing-equipment/)

- Owning idea: **Legacy Assembly Commoditised** (commodity assembly (recorded pass)).

## Sources
1. Mordor Intelligence, Die Bonder Equipment Market 2025-2030. https://www.mordorintelligence.com/industry-reports/die-bonder-equipment-market
2. Besi, Q4-25 and Full Year 2025 Results (rev EUR 591.3M, GM 63.3%, OM 29.3%). https://www.besi.com/investor-relations/press-releases/details/be-semiconductor-industries-nv-announces-q4-25-and-full-year-2025-results/
3. ASMPT, 2025 Annual Results (group rev US$1.76B, AP rev US$532.1M +30.2%, GM 37.8%, TCB +146% YoY). https://www.asmpt.com/en/investor-relations/news-events/asmpt-announces-2025-annual-results/
4. MarketsandMarkets / Valuates, Hybrid Bonding Equipment Market (~$165M 2025 to ~$600M+ by 2030-2032, >20% CAGR). https://www.marketsandmarkets.com/PressReleases/hybrid-bonding.asp
5. Persistence Market Research / Business Research Insights, Die Attach Materials & Paste Market (~$2.0-2.5B 2025; Henkel ~18-20%, Resonac/Nitto/Dexerials/Lintec ~52-58%). https://www.persistencemarketresearch.com/market-research/die-attach-materials-market.asp
6. OpenPR / MarketResearchFuture, Die Bonder Equipment Market players (Besi, ASMPT, K&S, Shinkawa, Toray, Fasford, Panasonic). https://www.marketresearchfuture.com/reports/die-bonder-equipment-market-32406
7. Precedence Research, Dicing Die Attach Film Market ($2.32B 2025 to $4.39B 2034, 7.34% CAGR). https://www.precedenceresearch.com/dicing-die-attach-film-market
8. Archive Market Research, Die Attach Material (~$1,015M, 5.5% CAGR 2025-2033). https://www.archivemarketresearch.com/reports/die-attach-material-838951
9. FinancialContent / TechInsights, Advanced packaging outlook (~$65B by 2027, +74% vs 2021; die bonders/hybrid bonders capacity-constrained). https://markets.financialcontent.com/stocks/article/tokenring-2026-2-5-tsmc-to-quadruple-advanced-packaging-capacity-reaching-130000-cowos-wafers-monthly-by-late-2026
10. FinancialContent, TSMC doubling/quadrupling CoWoS capacity through 2026 (~130k wafers/mo by late 2026, ~10x 2023). https://markets.financialcontent.com/wral/article/tokenring-2026-1-1-the-great-packaging-pivot-how-tsmc-is-doubling-cowos-capacity-to-break-the-ai-supply-bottleneck-through-2026
11. Semiconductor Engineering, HBM4 Sticks With Microbumps, Postponing Hybrid Bonding (775um JEDEC height; HBM5 hybrid bonding ~2028-2029; SK Hynix $3.87B Indiana plant prod 2028). https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/
12. Kulicke & Soffa FY2026 Q2 8-K + ASMPT AOR TCB (TCB to ~$400M annual system sales, FY26 capex ~$12M to ~$22M; fluxless active-oxide-removal TCB for HBM). https://www.sec.gov/Archives/edgar/data/0000056978/000005697826000018/ex991liveq22026.htm
13. IndexBox / GMI, Silver sinter die attach for SiC/EV (sinter-paste segment ~10-15% CAGR to 2033-2035; >65% demand from power electronics; 800V + Tj>200C forcing sinter). https://www.gminsights.com/industry-analysis/silver-paste-market
14. FinancialContent / Semiconductor Engineering, Hybrid-bond pitch roadmap + in-bonder metrology (6um HVM 2026, 4um/3um in test late 2026; X-ray die-to-wafer alignment in bonder head). https://markets.financialcontent.com/stocks/article/tokenring-2026-1-30-beyond-the-shrink-how-6-micrometer-hybrid-bonding-is-resurrecting-moores-law-for-the-ai-era
