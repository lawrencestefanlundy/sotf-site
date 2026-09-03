---
type: concept
slug: flow-osat-assembly-test-services
canonical_name: OSAT (outsourced assembly & test) services (process step)
seq: 53
phase: osat
related_concepts:
- osat
- advanced-packaging
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
parent_concepts:
- packaging
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
- slug: osat
  name: OSAT (Outsourced Semiconductor Assembly & Test)
  path: /manufacturing/packaging/osat/
  macro: manufacturing
- slug: advanced-packaging
  name: Advanced Packaging
  path: /manufacturing/packaging/advanced-packaging/
  macro: manufacturing
---
> Step 53 of 56 in the semiconductor flow (OSAT). Prev: [Advanced packaging: 3D stacking & hybrid bonding (process step)](/semiconductor-process-flow/packaging/flow-advanced-pkg-3d-hybrid-bonding/) · Next: [Final test (ATE) (process step)](/semiconductor-process-flow/test-metrology/flow-final-test-ate/)

## What this step does
OSAT is the outsourced service layer that takes finished wafers from a foundry or IDM and turns them into packaged, tested chips ready to ship. It is not a single tool step but a contract-manufacturing business that owns most of the back-end flow under one roof and sells it as a service. The sub-processes it runs inside its own factories include:
- Wafer thinning, dicing/singulation, and die sorting
- Die attach / pick-and-place, wire bonding or flip-chip bumping
- Molding/encapsulation, solder-ball/BGA attach, marking
- Increasingly, advanced packaging (2.5D/3D, fan-out, chiplet integration)
- Final test on ATE handlers, burn-in, and reliability screening

## Where it sits and why it matters
OSAT is the commercial home of the whole back end. Fabless designers and many IDMs do not own assembly/test capacity, so they buy it as a service. The captive alternative is an IDM or foundry doing its own packaging (TSMC's CoWoS being the most important example). The strategic question for this step is the split between captive and outsourced, and where the AI/HPC packaging value goes: TSMC keeping the highest-margin 2.5D/3D work in-house is the single biggest threat to OSAT value capture, while mainstream and trailing-edge packaging stays firmly outsourced.

## Equipment market
OSATs are the largest buyers of back-end (assembly + test) equipment. The semiconductor assembly and packaging equipment market was about $9.1B in 2024, growing toward ~$21B by 2034 at roughly 8-9% CAGR [1]. This is the capital that sits inside OSAT factories, not a market OSATs sell into.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| ASMPT | Singapore/HK | leader in die/wire bonders | broadest back-end portfolio, TCB push |
| Kulicke & Soffa | US/Singapore | wire-bond leader | dominant ball/wedge bonders, thermo-compression |
| BE Semiconductor (Besi) | Netherlands | flip-chip/hybrid-bond leader | hybrid bonding for 3D, partner with AMAT |
| DISCO | Japan | ~dominant in dicing/grinding | dicing saws, grinders, near-monopoly in some lines |
| Tokyo Electron / Applied Materials | Japan / US | growing in adv. packaging | front-end giants extending into packaging |

Concentration note: tool supply is far more concentrated than OSAT service supply. A handful of vendors control each tool category (DISCO in dicing/grinding, Besi in hybrid bonding, K&S/ASMPT in bonding), and those vendors earn foundry-like margins. OSATs are price-takers on equipment and price-takers to their customers, which is the structural squeeze.

## Materials & consumables
Every package OSATs build consumes bill-of-materials items, and this is recurring revenue for the materials makers, not the OSATs. The semiconductor/IC packaging materials market was roughly $40-44B in 2024 [5], a pool larger than the entire top-10 OSAT revenue. Main categories and representative vendors:
- Organic substrates (~$18B, ~40%+ of materials [5]) - Ibiden, Shinko, Unimicron, AT&S
- Leadframes - Mitsui High-tec, Haesung, ASM Pacific
- Bonding wire (gold/copper) - Tanaka, Heraeus, MK Electron
- Encapsulation / mold compound (EMC) - Sumitomo Bakelite, Resonac (ex-Hitachi Chemical), Henkel
- Underfill, die-attach, solder balls, plating chemicals - Henkel, Indium, Senju
Recurring-revenue note: materials are consumed per unit, so the materials makers (especially substrate and EMC suppliers) capture a steadier, higher-margin annuity than the OSATs that buy them. Substrate scarcity for AI packages has been a real bottleneck and a pricing-power moment for Ibiden/Shinko.

## Volumes, revenue, profitability
The top-10 OSATs generated about $41.6B in revenue in 2024, up ~3% year on year [2]. ASE led with ~$18.5B (~45% of the top-10), Amkor ~$6.3B, JCET ~$5.0B (+19% YoY), Tongfu ~$3.3B, PowerTech mid-single-digit share [2]. Margins are the headline story: Amkor ran ~14.5-14.8% gross margin and ~5-8% operating margin through 2024, with full-year net sales of $6.3B and gross profit of $933M (~14.8%) [3][4]. ASE's blended group gross margin was ~16.3% in 2024 [6]. Compare that to TSMC at ~55%+ gross margin. OSAT is capital-intensive (constant tool reinvestment), labor- and materials-heavy, and sells a commoditized service to powerful customers, so the margin is thin by structure. Whoever earns the real margin here is the tool vendor (DISCO, Besi, K&S) and the materials maker (Ibiden, Sumitomo Bakelite), not the OSAT.

## Market drivers, constraints & trends
Net read: the served market (back-end equipment + packaging-materials pool) is accelerating on AI packaging, but the value-capture share inside that pool is shifting toward materials and a few tool vendors, not the OSAT service layer.

**Drivers**
- AI/HPC packaging is the engine. CoWoS-class capacity is expanding ~33% in 2026 with NVIDIA booking over half of TSMC's allocation through 2026-27, spilling overflow to ASE/Amkor/UMC [8]. The OSAT market is put near $52B in 2025 growing ~9% CAGR [9].
- Test intensity rises faster than units: more test steps per chiplet package plus system-level test push the test-equipment pool from ~$16.0B (2026) to ~$21.6B by 2031 [10].
- Memory packaging (HBM4, 16-Hi) and electrification/automotive functional-safety test add a second, non-AI demand part lifting Powertech, JCET and others [9][10].

**Constraints**
- ABF substrate is the live chokepoint: Ajinomoto holds ~95% of the film and is raising prices ~30% in Q3 2026, with the supply gap stretching to end-2027 as AI build-ups go 11+11/13+13 layers [11]. Scarcity is a margin event for substrate makers, not OSATs.
- TSMC keeping the highest-margin 2.5D/3D in-house caps OSAT value capture [8]; tool supply is concentrated (DISCO, Besi, K&S/ASMPT earn the real margin).
- US controls on advanced-packaging equipment and HBM, plus China domestic-substitution build-out (Tongfu RMB4.4B raise, JCET XDFOI 2.5D), bifurcate the market and pressure pricing [12].

**Trends & inflections to watch**
- Hybrid bonding sub-10um: HBM4 stays on microbumps, postponing the inflection. Tripwire: an HBM5/20-layer-plus maker committing to die-to-wafer hybrid bonding (Besi hybrid-bond revenue already EUR36M 2023 to ~EUR476M 2026) [13].
- Glass-core / panel-level packaging. Tripwire: TSMC CoPoS small-volume trial in 2027 and ASE glass panel-level commercial ramp by Q4 2027 confirming the cost-down path [14].

## Connections
- [OSAT (Outsourced Semiconductor Assembly & Test)](/manufacturing/packaging/osat/) - the business-model cluster this step instantiates
- [Advanced Packaging](/manufacturing/packaging/advanced-packaging/) - the technology mix shift reshaping OSAT margins
- **Advanced Packaging Market** - the AP thesis (where the growth and better margins sit)
- **Back End Test Equipment No Wedge** - the test side, feeding into [Final test (ATE) (process step)](/semiconductor-process-flow/test-metrology/flow-final-test-ate/)

## Sources
1. Precedence Research, semiconductor assembly and packaging equipment market ($9.06B 2024 to $20.96B 2034). https://www.precedenceresearch.com/semiconductor-assembly-and-packaging-equipment-market
2. TrendForce / I-Connect007, Top 10 OSAT Companies of 2024 ($41.56B, ASE/Amkor/JCET ranking). https://www.trendforce.com/presscenter/news/20250513-12577.html
3. Amkor Q1-Q3 2024 8-K margin detail (~14.5-14.8% GM, 5-8% OM). https://www.sec.gov/Archives/edgar/data/0001047127/000104712724000089/amkr3312024erex-991.htm
4. Amkor FY2024 results ($6.32B sales, $933M GP, $3.1B AP revenue). https://ir.amkor.com/news-releases/news-release-details/amkor-technology-reports-financial-results-fourth-quarter-and-10
5. Market Research Future / SEMI, IC packaging materials market (~$40-44B 2024; substrates ~$18B). https://www.marketresearchfuture.com/reports/semiconductor-ic-packaging-materials-market-26595
6. ASE Technology FY2024 results (revenue NT$595.4B, group GM ~16.3%). https://beyondspx.com/quote/ASX/news/ase-technology-holding-reports-q4-and-full-year-2024-results-projects-strong-2025-leap-revenue-growt
7. Yole Group, advanced packaging market ($46B 2024 to $79.4B 2030, 9.6% CAGR). https://www.yolegroup.com/press-release/advanced-packaging-market-set-to-reach-79-4-billion-by-2030/
8. DIGITIMES / financialcontent, TSMC CoWoS ~33% capacity expansion 2026, NVIDIA booking >half through 2026-27, overflow to ASE/Amkor/UMC. https://www.digitimes.com/news/a20251210PD218/tsmc-cowos-capacity-nvidia-equipment.html
9. Market Research Reports / DIGITIMES, OSAT market ~$52B 2025, ~9% CAGR; ASE FOWLP/SiP + Powertech HBM/DRAM capacity adds 2026. https://www.marketresearchreports.com/blog/2026/05/28/top-10-osat-companies-world-updated-2026
10. Mordor Intelligence / Teradyne, semiconductor test-equipment market $16.04B 2026 to $21.59B 2031 (~6.1% CAGR); rising test intensity + SLT for chiplets. https://www.mordorintelligence.com/industry-reports/semiconductor-test-equipment-market
11. AtlasPCB / DIGITIMES, Ajinomoto ~95% ABF film share, ~30% price hike Q3 2026, supply gap to end-2027 as AI packages go 11+11/13+13. https://www.atlaspcb.com/news/news-ajinomoto-abf-substrate-price-increase-2026/
12. TrendForce / DIGITIMES, China OSAT build-out (Tongfu RMB4.4B raise, JCET XDFOI 2.5D mass production) amid US advanced-packaging SME + HBM controls. https://www.trendforce.com/news/2026/01/19/news-chinas-osat-giants-step-up-tongfu-microelectronics-to-raise-rmb-4-4b-jcet-backs-chip-fund/
13. SemiEngineering / 36Kr, HBM4 stays on microbumps postponing hybrid bonding to HBM5/20-layer+; Besi hybrid-bond revenue EUR36M 2023 to ~EUR476M 2026. https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/
14. WccfTech / TrendForce / 3DInCites, glass-core + panel-level packaging: TSMC CoPoS small-volume trial 2027, mass production 2028-29; ASE glass PLP commercial ramp by Q4 2027. https://wccftech.com/tsmc-accelerates-copos-packaging-replace-cowos-as-glass-core-substrates-cut-costs-boost-wafer-utilizatio/
