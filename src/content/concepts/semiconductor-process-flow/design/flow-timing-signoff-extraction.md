---
type: concept
slug: flow-timing-signoff-extraction
canonical_name: Timing signoff & parasitic extraction (process step)
seq: 11
phase: design
related_concepts:
- eda-design-tools
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
neighbors:
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
---
> Step 11 of 56 in the semiconductor flow (Design). Prev: [Routing (process step)](/semiconductor-process-flow/design/flow-routing/) · Next: [Physical verification (DRC/LVS/DFM) (process step)](/semiconductor-process-flow/design/flow-physical-verification-drc-lvs/)

## What this step does
After routing, the design has real wires with real resistance and capacitance. This step turns that physical layout into the final, sign-offable proof that the chip will run at frequency across every process, voltage and temperature (PVT) corner, then feeds those numbers into the last timing check before tape-out. It is the "golden" gate: foundries and IP vendors trust specific tools' numbers, so the choice of tool is not really a choice.

- **Parasitic extraction (RC extraction)**: read the routed layout, compute resistance and capacitance of every net, write a SPEF file. Field-solver accuracy at advanced nodes.
- **Static timing analysis (STA)**: propagate arrival/required times across millions of paths, check setup/hold, recovery/removal, across multi-corner multi-mode (MCMM) scenarios. No vectors, no simulation.
- **Signal-integrity and noise**: crosstalk delay and glitch, derived from the same parasitics.
- **Power and EM/IR signoff** (often bundled): dynamic/leakage power, voltage drop, electromigration.

## Where it sits and why it matters
This is the verdict step of physical implementation. Routing (Step 10) produced the geometry; here the geometry is judged. If signoff timing fails, the design loops back to placement, routing or even synthesis. Because the foundry's golden parasitic models (the tech files) are calibrated against one or two extraction tools, and because customers will not re-qualify a flow lightly, the tools at this step are the most locked-in in all of EDA. Signoff STA (PrimeTime) is frequently cited as the single most entrenched product in the industry.

## Equipment market
This is pure software; "equipment" means the EDA tool licences. The whole EDA software market was roughly $15-21B in 2024-2026 depending on the source, growing ~8-11% CAGR [1][2][3]. Signoff (timing + extraction + power/EM-IR) is a slice of the implementation/signoff segment; IC physical design and verification together held ~40% of EDA in 2024 [3]. A defensible estimate for the timing-signoff + extraction tool pool specifically is low single-digit billions of dollars per year, well under 10% of total EDA, but with margins and stickiness far above the EDA average.

| Vendor | HQ | Est. share (this step) | Notable |
|---|---|---|---|
| Synopsys | Sunnyvale, US | STA ~90%+ at advanced nodes; extraction ~50% | PrimeTime (golden STA), StarRC (golden RC extraction), PrimePower/PrimeShield [4][7] |
| Cadence | San Jose, US | STA the only real #2; extraction ~50% | Tempus (STA), Quantus (RC extraction), Voltus (power/EM-IR) [5][7] |
| Siemens EDA | Wilsonville, US / DE | Niche in this step | Stronger in physical verification (Calibre) than in golden STA/extraction [7] |
| Ansys (now Synopsys) | US | Power/EM-IR adjacency | RedHawk-SC for IR-drop/EM signoff; folded into Synopsys 2025 [3][7] |

Concentration note: this is a duopoly bordering on a Synopsys monopoly in golden STA. PrimeTime is the reference other tools are checked against; Tempus is the only credible alternative, and even Tempus users often keep PrimeTime as the final arbiter. Extraction is a cleaner Synopsys/Cadence split.

## Materials & consumables
No physical consumables. The recurring "consumable" is the licence itself, almost entirely time-based (subscription/term) revenue, which is what gives EDA its predictable, software-like financials. The genuinely consumed input is the foundry's signoff tech file / extraction deck (the calibrated RC models and corner definitions): produced by the foundry, certified against the specific tool, and re-issued every node. That certification is the moat. A startup tool cannot self-declare golden status; TSMC, Samsung and Intel decide which extractor is trusted, and they pick the incumbents. Net effect: revenue is recurring and high-retention, churn is rare because re-qualifying a signoff flow risks silicon.

## Volumes, revenue, profitability
"Volume" is seat-years and peak-core licences, not units. Every advanced tape-out (hundreds to low thousands of leading-edge designs a year, plus a long tail of mature-node designs) passes through signoff, and large SoC teams run hundreds of PrimeTime/Tempus cores in parallel for MCMM closure, which is why this step sells deep into each account. The revenue pool for timing-signoff + extraction is best estimated in the low single-digit billions per year, captured almost entirely by Synopsys and Cadence. Profitability is exceptional: Synopsys group gross margin ~78-80% (Design Automation segment higher) and Cadence non-GAAP operating margin ~42-45% in 2024-2025 [6][8][9]. Signoff is the higher-margin end even within EDA because the products are mature, R&D is incremental, and pricing power comes from golden status. The margin is earned by the tool vendor; foundries earn the calibration leverage but not the licence revenue.

## Competitive landscape & value capture
The moat is reference status plus switching cost: golden-tool certification by foundries, decades of correlation data, and the career-ending downside of a missed timing path. That is why this is the hardest step in the flow to disrupt head-on. Value accrues almost entirely to Synopsys and Cadence. There is no meaningful European or seed-stage incumbent in golden STA or extraction; the openings for newcomers are adjacent and assistive rather than replacement: AI-driven timing-ECO and closure optimisation that sits on top of PrimeTime/Tempus, cloud-burst licensing for peak MCMM runs, and faster field solvers for emerging structures (3D/backside-power, photonics, advanced packaging) where the incumbents' decks are still maturing. A seed team would have to be bought or partnered in, not compete on golden status.

## Market drivers, constraints & trends
Net read: a steadily accelerating served market. Signoff is the most defensible slice of an EDA pool growing ~9-9.4% to ~$43B by 2034 [10], and every structural shift in chip design (more corners, more dies, more parasitics) sells deeper into the same locked-in tools.

- **Drivers**
  - Design complexity is compounding: GAA + backside power + multi-die produce a roughly ten-fold rise in design-rule checks versus 7nm, and chiplet/2.5D-3D growth (3D-IC packaging ~$33B by 2030, ~15% CAGR) forces new multi-die timing, thermal and cross-die parasitic signoff that single-die flows cannot do [11][12].
  - Verification/signoff intensity is rising faster than wafer volume: semiconductor R&D intensity is climbing toward ~9% and EDA's share of that R&D is expanding through node-transition pricing and AI-tool premiums [13].
  - MCMM closure sells by the core: large SoC teams run hundreds of PrimeTime/Tempus cores in parallel, so more corners and modes expand peak-core licensing without new logos [10][13].

- **Constraints**
  - Cyclicality and geopolitics: China was ~16% of Synopsys and ~12% of Cadence FY24 revenue, and the May 2025 US export-control whipsaw (imposed, rescinded six weeks later) shows how fast this pool can be gated [14][15].
  - Pure-software TAM cap: signoff stays a low-single-digit-billion slice of EDA, and assistive AI that closes timing faster can compress per-design runtime/seats even as it adds value [13].
  - Foundry-certification lock-in cuts both ways: it protects incumbents but caps any new-entrant share, so the pool grows only as fast as design starts and complexity, not as fast as new vendors can enter [16].

- **Trends & inflections to watch**
  - AI/agentic signoff is moving from copilot to autonomous ECO and closure (Synopsys.ai, Cadence Cerebrus). Tripwire: a named foundry certifies an AI-assisted extraction/STA flow as golden at <=2nm [13][16].
  - Field-solver extraction for non-planar GAA/CFET and backside-power layouts is being rebuilt; rule-based decks lose accuracy. Tripwire: a TSMC/Samsung 2nm PDK ships requiring full 3D field-solver MOL/FEOL extraction by 2027 [11][16].
  - Multi-die signoff becoming its own product line (Siemens Innovator 3D IC + Calibre 3D Stress, Jun 2025). Tripwire: a hyperscaler tapes out a stacked AI accelerator whose signoff is priced as a separate multi-die tier [12][17].

## Connections
[EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/) · [Routing (process step)](/semiconductor-process-flow/design/flow-routing/) · [Physical verification (DRC/LVS/DFM) (process step)](/semiconductor-process-flow/design/flow-physical-verification-drc-lvs/)

- Owning idea: **Eda Chip Design** (EDA design-tool layer).

## Sources
1. Precedence Research, EDA software market (~$14.55B 2025, ~9% CAGR to 2035) — https://www.precedenceresearch.com/electronic-design-automation-software-market
2. Mordor Intelligence, EDA Tools market (~$20.78B 2026, 8.1% CAGR) — https://www.mordorintelligence.com/industry-reports/electronic-design-automation-eda-tools-market
3. Grand View Research, EDA software market (IC physical design & verification ~40% share 2024) — https://www.grandviewresearch.com/industry-analysis/electronic-design-automation-eda-software-market
4. Synopsys, PrimeTime / StarRC product pages — https://www.synopsys.com/implementation-and-signoff/signoff/primetime.html · https://www.synopsys.com/implementation-and-signoff/signoff/starrc.html
5. Cadence, Tempus Timing Signoff — https://www.cadence.com/en_US/home/tools/digital-design-and-signoff/silicon-signoff/tempus-timing-signoff-solution.html
6. Macrotrends, Synopsys gross/operating margin (gross ~78-80% 2020-2024) — https://www.macrotrends.net/stocks/charts/SNPS/synopsys/profit-margins
7. SemiAnalysis, EDA Market Primer (PrimeTime 90%+ at advanced nodes; Calibre 85%+ in physical verification; vendor shares) — https://newsletter.semianalysis.com/p/eda-market-primer
8. Cadence, FY2024 results (non-GAAP operating margin 42.5%) — https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr-ir/2025/cadence-reports-fourth-quarter-and-fiscal-year-2024-financial.html
9. Cadence, FY2025 results (non-GAAP operating margin ~44.6%) — https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx
10. TimesTech / Towards Packaging, EDA market to ~$43.07B by 2034 at 9.4% CAGR — https://timestech.in/electronic-design-automation-market-size-worth-usd-43-07-billion-by-2034-cagr-9-4/
11. Siemens EDA, Mastering parasitic extraction at the 3nm node (GAA/3D-IC field-solver requirements, hybrid xACT engine) — https://blogs.sw.siemens.com/calibre/2024/02/12/mastering-parasitic-extraction-at-the-3-nm-process-node/
12. GlobeNewswire / Research and Markets, EDA Tools 2025-2031 (~10x DRC rise GAA vs 7nm; 3D-IC packaging ~$33B by 2030 ~15% CAGR; Siemens Innovator 3D IC + Calibre 3D Stress Jun 2025; +30% multi-die thermal/SI tool adoption) — https://www.globenewswire.com/news-release/2026/02/05/3233268/28124/en/Electronic-Design-Automation-Tools-EDA-Research-Report-2026-Market-Share-Analysis-Industry-Trends-Statistics-Growth-Forecasts-Report-2025-2031.html
13. Scuttleblurb, Cadence/Synopsys and the future of chip design (R&D intensity toward ~9%, EDA share of R&D expanding via verification intensity + AI-tool premiums + node-transition pricing) — https://scuttleblurb.substack.com/p/cdns-snps2
14. TrendForce, China revenue at risk under US EDA curbs (Synopsys ~16% / Cadence ~12% of FY24 revenue from China) — https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/
15. CNBC, US lifts chip-software curbs on China six weeks after imposing them (Jul 2025) — https://www.cnbc.com/2025/07/03/us-lifts-chip-software-curbs-on-china-amid-trade-truce-synopsys-says-.html
16. Synopsys, Expanding AI capabilities for EDA (Synopsys.ai Copilot; AI agents across timing/power/parasitics) — https://investor.synopsys.com/news/news-details/2025/Synopsys-Announces-Expanding-AI-Capabilities-for-its-Leading-EDA-Solutions/default.aspx
17. Semiconductor Engineering, Backside power delivery creates fab-tool and thermal barriers (frontside-backside via alignment, over-polish parasitic/yield effects, CFET roadmap) — https://semiengineering.com/backside-power-delivery-creates-fab-tool-thermal-dissipation-barriers/
