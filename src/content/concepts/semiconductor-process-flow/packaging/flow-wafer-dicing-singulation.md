---
type: concept
slug: flow-wafer-dicing-singulation
canonical_name: Wafer dicing / singulation (process step)
seq: 42
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
neighbors:
- slug: bonding-dicing-equipment
  name: Bonding & Dicing Equipment
  path: /manufacturing/equipment-processes/bonding-dicing-equipment/
  macro: manufacturing
---
> Step 42 of 56 in the semiconductor flow (Assembly). Prev: [Wafer backgrinding / thinning (process step)](/semiconductor-process-flow/packaging/flow-wafer-backgrind-thinning/) · Next: [Die attach / pick-and-place (process step)](/semiconductor-process-flow/packaging/flow-die-attach-pick-place/)

## What this step does
After backgrind has thinned the wafer, dicing cuts the finished wafer into individual dies (chips) ready for packaging. The wafer is mounted on adhesive dicing tape stretched over a frame, cut along the scribe streets between dies, then the tape is expanded so good dies can be picked. The choice of cutting method drives die strength, edge quality and throughput. Sub-processes inside the step:
- Wafer mount on dicing tape/frame, plus alignment to the street grid.
- Singulation by one of three methods: mechanical blade saw, laser (ablation, or DISCO/Hamamatsu "Stealth Dicing" which focuses the laser inside the wafer), or plasma (dry-etch through the streets).
- Cleaning/rinse of cut debris and post-dice inspection of kerf and die-edge chipping.

## Where it sits and why it matters
Dicing is the first hard transition from wafer-scale to die-scale, and it is where a fully-yielded wafer can still be lost. Mechanical sawing causes micro-cracks and chipping that weaken thin dies and limit how small the kerf (cut width, hence lost silicon) can go. As wafers thin to 20-50 um for HBM stacks, CMOS image sensors and power devices, laser and plasma methods grow because they preserve die strength and cut narrow streets. The step matters economically because one vendor, DISCO, captures most of the value across both the tool and the recurring blade.

## Equipment market
Dicing-equipment (saws plus laser/plasma tools) revenue is roughly USD 2.5-2.6bn in 2024 and growing high-single-digits; the narrower wafer-dicing-saw segment was put at ~USD 2.55bn in 2024 [1]. The adjacent thin-wafer-processing-and-dicing tool market is ~USD 0.77bn in 2025 at ~6.4% CAGR, with plasma dicing the fastest sub-segment at ~7.2% [4]. Treat these report-mill totals as order-of-magnitude, not precise.

| Vendor | HQ | Est. share (dicing tools) | Notable |
|---|---|---|---|
| DISCO | Japan | ~70-80% saws; ~50% all dicers+grinders | Near-monopoly; blade, laser, Stealth Dicing; consumables flywheel [1][2][3] |
| Tokyo Seimitsu (Accretech) | Japan | ~8-9%, clear #2 | Strong in stealth/laser dicing; ~USD 250-260m systems sales [5] |
| Plasma-Therm | USA | small but leading plasma | Mosaic-class plasma dicing; Corial R&D brand [4] |
| SPTS Technologies (KLA) | UK/USA | small, plasma niche | Mosaic plasma dicing for advanced packaging [4] |
| Han's Laser / Panasonic | China / Japan | small | Laser-ablation and plasma challengers [4] |

Concentration note: this is one of the most concentrated tool markets in all of semis. DISCO's share of dicers-plus-grinders is roughly 4x its nearest competitor [5]; sawing is effectively a DISCO/Accretech duopoly with DISCO dominant.

## Materials & consumables
The step consumes diamond dicing blades and dicing tape/film, plus DI water and detergents for cooling and debris removal. Blades are the high-frequency wear item: the wafer-dicing-saw-blade market was ~USD 1.2bn in 2024, projected ~USD 1.8bn by 2032 at ~7% CAGR [1]. DISCO makes its own diamond abrasive blades, so each installed saw pulls a recurring blade/spares stream. Roughly 30-35% of DISCO's revenue is consumables and services, structurally higher-margin and stickier than the tool sale itself [2]. Plasma dicing shifts consumable spend toward etch gases (e.g. SF6/C4F8) and masking rather than blades.

## Volumes, revenue, profitability
Every wafer that reaches packaging is diced, so unit volume tracks total wafer starts (~order of magnitude 200m+ 200mm-equivalent wafers/yr industry-wide; dicing per-wafer cost is small but universal). The revenue pool is the ~USD 2.5bn tool layer plus the ~USD 1.2bn blade layer, with tape adding several hundred million more. The margin sits overwhelmingly with DISCO: company-level operating margins run roughly the high-30s to low-40s percent (quarterly readings ~38-44% across FY2025), on FY2025 net sales of ~JPY 393bn (ended March 2025) [2][3]. That is a software-like margin profile earned on hardware, the signature of a near-monopoly with a captive consumable.

## Market drivers, constraints & trends
Net read: the equipment-plus-consumable pool grows mid-to-high-single-digits structurally, but with a fatter laser/plasma tail and a real AI-capex cyclical kicker, so the served market accelerates above its long-run trend into 2026-2027.

- **Drivers**
  - HBM is the immediate forcing function: global HBM wafer starts head to ~540k wafers/month by end-2025, and HBM4 16-hi stacks at a 775um height limit roughly double the dicing passes per finished unit versus 8-hi, multiplying dicing-tool and consumable pull per bit [6][7]. HBM demand grew ~130% in 2025 and is forecast ~70% in 2026 [6].
  - Advanced packaging is the broader pull: the pool grows ~9.6% CAGR to >USD 80bn by 2030, with CoWoS capacity stepping 75k (2025) to 135k wpm (2026); each 2.5D/chiplet unit adds individualisation and board-singulation steps for DISCO's KKM tools [6][8].
  - SiC/power electrification shifts mix to laser: hard (Mohs 9.5) wide-bandgap wafers saw poorly, and the 150mm-to-200mm transition pulls in stealth/ultrafast-laser dicing; SiC was already ~37% of dicing-service value in 2025 [9][10].

- **Constraints**
  - Severe cyclicality and concentration: the served market now rides AI capex, so a CoWoS/HBM digestion pause would hit dicing tool orders hard, with DISCO's ~38-44% margins amplifying any down-leg [3][6].
  - Geopolitical: allied export controls on China (a large equipment-revenue source for the top-5 SME makers) can cut a meaningful demand slice at a stroke [11].
  - Glass-substrate fragility is a yield headwind, not yet a volume driver: glass cracks during and after singulation, large-scale panel adoption slips to ~2028+ [8].

- **Trends & inflections to watch**
  - Blade-to-laser/plasma displacement: laser is ~6x faster (3-5 vs 25 min/wafer) at ~15um kerf, and stealth lifts die strength to ~877 MPa; the stealth-dicing tool segment grows ~8% to ~USD 300m by 2033. Tripwire: DISCO laser-saw cumulative shipments (4,000 units as of Feb 2026, the second 2,000 added in 6yr vs 18yr for the first) re-accelerating [4][9][12].
  - Panel-level packaging at 310x310mm and glass cores. Tripwire: a named OSAT/foundry qualifying glass-panel singulation in volume (watch SCHMID/TSMC PLP milestones, 2026-2027) [8].
  - Plasma dicing into sub-10um-pitch chiplets. Tripwire: plasma share moving decisively above its ~10% 2025 base as 3D-IC mix rises [6].

## Connections
- [Bonding & Dicing Equipment](/manufacturing/equipment-processes/bonding-dicing-equipment/)

- Owning idea: **Back End Wafer Prep Equipment**, **Advanced Packaging Market** (back-end wafer-prep growth story).

## Sources
1. Market Research Future / Mordor / Valuates summaries, wafer dicing saws ~USD 2.55bn 2024; blades ~USD 1.2bn 2024, ~7% CAGR; DISCO ~70-80% saw share. https://www.marketresearchfuture.com/reports/wafer-dicing-saws-market-23843 ; https://www.mordorintelligence.com/industry-reports/dicing-equipment-market
2. DISCO consumables ~30-35% of revenue; FY2024 ~JPY 307.5bn revenue (razor-and-blade model). https://www.tradingview.com/news/gurufocus:68564a0d3094b:0-disco-corp-the-precision-toolmaker-quietly-dominating-the-semiconductor-boom/ ; https://umbrex.com/resources/company-profiles/disco-corp/
3. DISCO FY2025 net sales ~JPY 393.3bn; operating-margin readings ~38-44% across FY2025 quarters. https://quartr.com/companies/disco-corporation_15573 ; https://www.macrotrends.net/stocks/charts/DSCSY/disco-corp/operating-margin
4. Thin-wafer-processing-and-dicing market ~USD 0.77bn 2025, ~6.4% CAGR; plasma dicing ~7.2% CAGR; Plasma-Therm/SPTS plasma, Stealth Dicing SD engine by Hamamatsu. https://www.mordorintelligence.com/industry-reports/thin-wafer-processing-and-dicing-equipment-market ; https://www.spts.com/markets/advanced-packaging/plasma-dicing ; https://www.disco.co.jp/eg/solution/library/laser/stealth.html
5. Accretech ~8-9% share / ~USD 250-260m systems sales, clear #2; DISCO ~4x nearest competitor. https://finance.yahoo.com/news/disco-corp-wonderful-japanese-hidden-095449035.html ; https://www.accretech.com/en/company/business.html
6. HBM wafer starts ~540k wpm by end-2025; HBM4 16-hi at 775um height limit ~doubles dicing passes vs 8-hi; HBM demand +130% 2025 / +70% 2026 (TrendForce); advanced packaging ~9.6% CAGR to >USD 80bn by 2030; CoWoS 75k (2025) to 135k wpm (2026); plasma ~10.5% product-type share 2025. https://finance.yahoo.com/news/wafer-dicing-services-market-set-133000319.html ; https://www.snsinsider.com/reports/semiconductor-plasma-dicing-tape-market-8441
7. Wafer dicing services market USD 617.5m 2025 to USD 932.9m 2035 (~4.21% CAGR); HBM4 2,048 IO, <10um bump pitch; SiC ~37.5% of dicing-service value 2025; laser ~42% by technology. https://www.globenewswire.com/news-release/2025/12/11/3203897/0/en/Wafer-Dicing-Services-Market-Set-to-Exceed-US-932-9-Million-by-2035-Astute-Analytica.html
8. Glass-substrate panel-level packaging: cracking during/after singulation a key limiter; 310x310mm PLP progress (SCHMID/TSMC); large-scale glass adoption ~2028+; CoPoS/glass core wafer-utilisation gains. https://www.trendforce.com/news/2026/05/19/news-equipment-maker-schmid-flags-tsmc-panel-level-packaging-push-310x310mm-progress-glass-integration-under-review/ ; https://www.aminext.blog/en/post/glass-substrate-advanced-packaging-2026-trend
9. SiC dicing: Mohs 9.5 hardness defeats blades (debris/thermal damage); ultrafast-laser precision layered stealth dicing emerging mainstream; 150-to-200mm SiC cost down 20-35%. https://pmc.ncbi.nlm.nih.gov/articles/PMC9315561/ ; http://www.hanslaserus.com/knowledge/breaking-through-sic-wafer-dicing-challenges-with-di-sync-laser-stealth-technology/
10. Semiconductor wafer singulation review (technological advancements and emerging trends, Crit. Rev. Solid State Mater. Sci. 2025). https://www.tandfonline.com/doi/full/10.1080/10408436.2025.2578023
11. Allied export controls on China cut a large equipment-revenue slice; top-5 allied SME suppliers sold ~USD 38bn to Chinese firms (CSIS/ITIF). https://www.csis.org/analysis/true-impact-allied-export-controls-us-and-chinese-semiconductor-manufacturing-equipment ; https://itif.org/publications/2025/11/10/decoupling-risks-semiconductor-export-controls-harm-us-chipmakers-innovation/
12. DISCO cumulative laser-saw shipments exceeded 4,000 units as of Feb 2026 (second 2,000 added in 6yr vs 18yr for the first); DISCO ~60%+ stealth-dicing-laser share 2025; AI offsets EV slump, FY raised; wafer laser stealth dicing machine market ~USD 150m 2024 to ~USD 300m 2033 (~8% CAGR). https://www.disco.co.jp/eg/news/corp/20260302.html ; https://www.powersemiconductorsweekly.com/2026/03/02/disco-laser-saw-shipments-surpass-4000-units-amid-growing-semiconductor-demand/ ; https://www.verifiedmarketreports.com/product/wafer-laser-stealth-dicing-machine-market/
