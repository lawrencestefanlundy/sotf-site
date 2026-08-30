---
type: concept
slug: flow-metrology-cd-overlay
canonical_name: Metrology (CD, overlay, film, OCD) (process step)
seq: 37
phase: control
related_concepts:
- metrology-testing
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
- slug: metrology-testing
  name: Metrology & Testing
  path: /manufacturing/equipment-processes/metrology-testing/
  macro: manufacturing
- slug: semiconductor-metrology-inspection
  name: Semiconductor Metrology & Inspection
  path: /manufacturing/equipment-processes/semiconductor-metrology-inspection/
  macro: manufacturing
---
> Step 37 of 56 in the semiconductor flow (Control). Prev: [Copper electroplating (ECD) (process step)](/semiconductor-process-flow/frontend/flow-copper-electroplating-ecd/) · Next: [Defect inspection & review (process step)](/semiconductor-process-flow/test-metrology/flow-defect-inspection/)

## What this step does
Metrology measures the wafer to confirm that the previous process step hit its target dimensions, alignment and material properties. Unlike inspection (next step), which hunts for random defects, metrology quantifies systematic parameters and feeds them back to tune the litho, etch and deposition tools. It runs hundreds of times across a flow, more often than any single deposition or etch step. The unit sub-processes:
- Critical dimension (CD): measuring feature widths, gate lengths and line spacing, historically by CD-SEM, increasingly by optical and scatterometry methods.
- Overlay: measuring layer-to-layer misalignment, the single most failure-prone parameter at advanced nodes.
- Film/thickness metrology: optical (ellipsometry, reflectometry) and X-ray measurement of deposited film thickness, composition and stress.
- Optical critical dimension (OCD) / scatterometry: model-based reconstruction of 3D feature shape (FinFET fins, gate-all-around nanosheets, deep DRAM/3D-NAND structures) from diffracted light, non-destructively.

## Where it sits and why it matters
Process control is the feedback loop that makes sub-3nm manufacturing economically possible. As feature shapes go fully 3D (GAA nanosheets, 3D-DRAM, hybrid-bonded stacks), you cannot etch what you cannot measure: metrology gates yield. The reason this step captures outsized value is that it is run constantly, is bought as a tool-plus-software-plus-service package, and the accuracy bar rises every node, so incumbents with the recipe libraries and reference data compound their lead. It is the most defensible, highest-margin niche in all of wafer fab equipment.

## Equipment market
Process control (metrology + inspection combined) was roughly USD 9-10.3bn in 2024 depending on definition [1][2], growing at a ~6-8% CAGR through the early 2030s [2][3]. Metrology proper (CD, overlay, film, OCD, the scope of this page) is the larger and faster sub-pool within that, distinct from defect inspection (next step). KLA holds ~60%+ of the whole process-control market and rising [5].

| Vendor | HQ | Est. share (process control) | Notable |
|---|---|---|---|
| KLA | US (Milpitas, CA) | ~57% in 2023, ~63% by 2024 [5] | Dominant in overlay (Archer IBO), film, and >90% of some thin-film metrology niches [6] |
| Applied Materials | US | ~10-12% (est.) | eBeam metrology, integrated metrology, broad WFE leverage |
| Onto Innovation | US (Wilmington, MA) | high-single to low-double digit | Standalone OCD, slightly outgrowing KLA; won TSMC/Samsung/Intel GAA nodes [6] |
| Nova Ltd | Israel (Rehovot) | high-single digit | Integrated OCD + materials metrology; strong but narrow [6] |
| Hitachi High-Tech | Japan | mid-single digit | CD-SEM leader |
| ASML | Netherlands | small but strategic | YieldStar diffraction-based overlay, attached to its litho install base |

Concentration note: KLA alone takes the majority; KLA + Applied + Onto + Thermo Fisher + Hitachi held ~58% in 2025 by one count, but that understates KLA's grip inside metrology specifically, where it is closer to two-thirds [1][5][6]. This is among the most concentrated layers in the entire flow.

## Materials & consumables
Metrology is overwhelmingly capital equipment, not consumables, but it has a large and sticky recurring tail. Each tool consumes calibration standards and reference wafers, but the real recurring revenue is service contracts, software/recipe licensing, applications support and spares. KLA's installed base throws off high-margin service revenue that grows even when tool sales dip; the package (hardware + recipe library + service) is what locks customers in. There is no merchant chemical/materials pool here the way there is in CMP or ECD; value sits in the tool and the software.

## Volumes, revenue, profitability
The metrology revenue pool is the multi-billion-dollar slice of the ~USD 9-10bn process-control market [1][2]. KLA's whole company did USD 9.8bn in FY2024 and USD 12.16bn in FY2025 (+24% YoY), with semiconductor process control ~89% of revenue [5][7]. The economics are exceptional and are the reason to care about this step:
- KLA gross margin ~60% (FY2024), targeting 63-64%; operating margin ~32-33%; free-cash-flow margin ~31%, top-tier of the S&P 500 [4][5][7].
- Onto Innovation: FY2025 revenue ~USD 1.0bn, non-GAAP gross margin ~55%, non-GAAP operating margin ~25% [8].
- Nova Ltd: FY2025 revenue ~USD 881m, with metrology-leader margins in the same band [6].

The margin is earned by the equipment-plus-software layer. No one else in the value chain (chemicals, gases, the fabs themselves) earns these margins on this step.

## Competitive landscape & value capture
The moat is data and recipes, not just optics. Overlay and OCD are model-based: the tool is only as good as the reference library and machine-learning models built from years of customer process data, which compounds with install base. Switching costs are brutal because a metrology recipe is qualified into a specific fab process. That is why KLA's share rises every node rather than eroding, and why challengers (Onto, Nova) win only by owning a specific sub-segment (standalone OCD, integrated OCD) rather than attacking head-on.

European/seed angle: Europe punches above its weight in this layer. ASML (NL) owns diffraction-based overlay via YieldStar; Carl Zeiss (DE) supplies the optics core; Bruker (X-ray metrology), Semilab (HU), Nikon Metrology, and France's UnitySC (advanced-packaging metrology, acquired by Merck KGaA Oct 2024, now a EUR 20m Saint-Ismier site) cluster in the gaps [9]. The white space for a seed-stage European bet is not standalone wafer metrology (KLA-locked) but the adjacent frontier where incumbents are weakest: in-line/in-situ metrology, AI-driven virtual metrology (inferring measurements from sensor data to cut physical measurement steps), and advanced-packaging metrology (hybrid-bonding, TSV, HBM stacks) where the install base is younger and recipe lock-in has not yet set.

## Market drivers, constraints & trends
Net read: accelerating. The served market grows faster than WFE because process control is taking a rising share of every fab dollar, and the AI/3D transitions all add measurement steps.

- **Drivers**
  - Process-control intensity is rising structurally: from ~7.4% of WFE in 2025 toward ~9% by 2030, so this step grows faster than the equipment market it sits inside [10]. The 2nm node captures a meaningfully greater share of WFE than 3nm, a step-function increase in addressable spend per dollar of customer capex [10].
  - 3D device transitions multiply measurement steps: GAA nanosheets, backside power delivery and High-NA EUV all need denser CD/overlay/OCD sampling, with metrology called out as a key enabling building block for High-NA [11][12].
  - Advanced packaging is the fastest sub-pool: KLA's advanced-packaging process-control revenue is guided from ~USD 635m (2025) to ~USD 1bn (2026) [13]; HBM4 and custom stacks are more metrology-intensive than HBM3E [14].

- **Constraints**
  - Cyclicality and capex concentration: the pool tracks leading-edge and HBM capex, which is concentrated in a handful of buyers (TSMC, Samsung, Intel, the HBM makers) and swings with the cycle.
  - China is the largest WFE buyer but its spend is forecast to fall from ~USD 50bn (2024) to ~USD 36-38bn (2025-26), and export controls now restrict advanced metrology/inspection tools into China, capping that channel [15][16].
  - Domestic Chinese metrology suppliers (still <10% value share, mostly >=28nm) are scaling toward 20-25% by 2035, eroding the mature-node tail over time [16].

- **Trends & inflections to watch**
  - AI-driven virtual/in-line metrology that infers measurements to cut physical steps, the main software re-rate axis. Tripwire: an incumbent quantifies virtual-metrology revenue or a fab discloses measured measurement-step reduction at 2nm.
  - Hybrid bonding below 10um: sub-micron bond-interface metrology becomes a discrete pool. Tripwire: KLA hits its ~USD 1bn 2026 advanced-packaging target and HBM4 ramps in volume [13][14].
  - High-NA EUV in production. Tripwire: a foundry confirms High-NA volume wafers in 2026, pulling new mask + on-wafer metrology demand [12].

## Connections
- [Metrology & Testing](/manufacturing/equipment-processes/metrology-testing/)
- [Semiconductor Metrology & Inspection](/manufacturing/equipment-processes/semiconductor-metrology-inspection/)
- **Semiconductor Metrology Wedge**
- **Advanced Packaging Metrology**
- Adjacent flow steps: [Copper electroplating (ECD) (process step)](/semiconductor-process-flow/frontend/flow-copper-electroplating-ecd/), [Defect inspection & review (process step)](/semiconductor-process-flow/test-metrology/flow-defect-inspection/)

## Sources
1. Market.us, Semiconductor Process Control Equipment Market (USD 10.34bn 2024; ~58.4% top-5 share 2025; ~6-8% CAGR) — https://market.us/report/semiconductor-process-control-equipment-market/
2. Data Bridge Market Research, Semiconductor Process Control Equipment Market (~6.10% CAGR 2025-2032) — https://www.databridgemarketresearch.com/reports/global-semiconductor-process-control-equipment-market
3. Mordor Intelligence, Semiconductor Metrology and Inspection Equipment Market — https://www.mordorintelligence.com/industry-reports/semiconductor-metrology-and-inspection-equipment-market
4. KLA Corporation FY2024 Annual Report / 10-K (gross margin 60%, operating margin ~32.5%) — https://ir.kla.com/sec-filings/all-sec-filings/content/0001193125-24-224805/d842113dars.pdf
5. R. Castellano, "KLA's Market Share Growth in Process Control" (~57% 2023 rising to ~63% 2024) — https://drrobertcastellano.substack.com/p/klas-market-share-growth-in-process
6. SemiAnalysis, "How Onto Innovation Is Gaining Market Share From KLA" (>90% thin-film niches; Onto/Nova sub-segment positions; Nova FY2025 ~USD 881m) — https://newsletter.semianalysis.com/p/how-onto-innovation-is-gaining-market
7. KLA Corporation FY2025 Q4/full-year results (revenue USD 12.16bn, +24% YoY; GM target 63-64%) — https://ir.kla.com/news-events/press-releases/detail/500/kla-corporation-reports-fiscal-2025-fourth-quarter-and-full
8. Onto Innovation 2025 full-year results (revenue ~USD 1.005bn; non-GAAP GM 54.6%, op margin 25.4%) — https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Reports-2025-Fourth-Quarter-and-Full-Year-Results/default.aspx
9. Yole Group, "Underappreciated EU suppliers lead the semiconductor equipment market" + Merck/UnitySC metrology site — https://www.yolegroup.com/strategy-insights/underappreciated-eu-suppliers-lead-the-semiconductor-equipment-market/
10. StockStory, "KLAC Q3 Deep Dive: AI, Advanced Packaging, and Process Control" (process-control intensity ~7.4% of WFE 2025 → ~9% by 2030; 2nm captures meaningfully greater WFE share than 3nm) — https://stockstory.org/us/stocks/nasdaq/klac/news/earnings-call/klac-q3-deep-dive-ai-advanced-packaging-and-process-control-drive-growth-and-guidance
11. SemiAnalysis, "Clash of the Foundries: Gate All Around + Backside Power at 2nm" (GAA + backside power node timelines, N2 2025 / A16 H2-2026, Intel 18A) — https://newsletter.semianalysis.com/p/clash-of-the-foundries
12. Semiconductor Engineering, "EUV's Future Looks Even Brighter" (High-NA EUV volume path; metrology a key enabling building block) — https://semiengineering.com/euvs-future-looks-even-brighter/
13. The Globe and Mail / Zacks, "Can KLA's Advanced Packaging Strength Support $1B Revenue Target?" (advanced-packaging process-control revenue ~USD 635m 2025 → ~USD 1bn 2026) — https://www.theglobeandmail.com/investing/markets/stocks/MKSI/pressreleases/1804180/can-klas-advanced-packaging-strength-support-1b-revenue-target/
14. R. Castellano, "Camtek Faces HBM Cycle Reset — But Is Poised for Leadership in Hybrid Bonding and AI Packaging" (HBM4 more metrology-intensive than HBM3E; Camtek FY2025 ~USD 496m, ~50% AI) — https://drrobertcastellano.substack.com/p/camtek-faces-hbm-cycle-reset-but
15. Mark LaPedus, "What's The Outlook For The Semi Equipment Biz in '26?" + SEMI fab investment data (China WFE ~USD 50bn 2024 → ~USD 36-38bn 2025-26) — https://marklapedus.substack.com/p/whats-the-outlook-for-the-semi-equipment
16. Baker McKenzie Sanctions Blog, US Commerce expanded controls incl. metrology/inspection tools; domestic Chinese share <10% (mostly >=28nm), projected 20-25% by 2035 — https://sanctionsnews.bakermckenzie.com/us-department-of-commerce-significantly-expands-controls-targeting-indigenous-production-of-advanced-semiconductors-in-china/

> Note: equipment market sizes here are report-mill figures cross-checked against KLA/Onto/Nova filings; treat the absolute TAM as approximate and the company financials as primary. Share figures for vendors other than KLA are rough estimates triangulated from filings and analyst commentary, not exact.
