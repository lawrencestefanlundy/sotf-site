---
type: concept
slug: flow-floorplanning-power
canonical_name: Floorplanning & power planning (process step)
seq: 7
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
parent_concepts:
- flow-rtl-design
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
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
---
> Step 7 of 56 in the semiconductor flow (Design). Prev: [Design-for-test (DFT) (process step)](/semiconductor-process-flow/design/flow-design-for-test-dft/) · Next: [Placement (process step)](/semiconductor-process-flow/design/flow-placement/)

## What this step does
Floorplanning is the first physical-implementation task: the gate-level netlist from synthesis is turned into a coarse two-dimensional layout. The engineer fixes the die size and aspect ratio, places the large hard blocks (memories, analog IP, third-party cores), reserves channels for buses, and builds the power-delivery network so every cell can be fed current without unacceptable voltage droop. It is the single highest-leverage decision in the back end: a bad floorplan cannot be rescued by good placement or routing downstream, and it sets the achievable power, performance and area (PPA) envelope for the whole chip.
- Die sizing, block partitioning and macro placement
- I/O and pad-ring planning
- Power grid / power-distribution-network (PDN) synthesis (rails, straps, rings)
- IR-drop and electromigration budgeting
- Pin assignment and channel reservation for later routing
- Power-domain and multi-voltage planning (UPF/CPF intent)

## Where it sits and why it matters
It is the bridge between the logical world (synthesis, [Logic synthesis (process step)](/semiconductor-process-flow/design/flow-logic-synthesis/)) and the physical world (placement, routing, signoff). Floorplanning and power planning run inside the same monolithic place-and-route (P&R) tool that carries the design through the next several steps, so the buyer rarely buys this step on its own. That matters commercially: value is captured at the level of the full "digital implementation" platform licence, not a standalone floorplanning product. The step is also where AI is biting first, because the search space (where to put blocks, how to shape the grid) is exactly what reinforcement-learning optimisers are good at.

## Equipment market
There is no physical equipment. The "tool" is software: the digital implementation / P&R suite. The wider electronic-design-automation (ESD) industry ran at roughly USD 4.7bn revenue in Q2 2024 (about an USD 18-19bn annual run-rate) per SEMI/ESD Alliance [1], and most market trackers put 2024 EDA at USD 17-18bn growing ~9-11% CAGR to 2032-33 [2][3]. IC physical design and verification, the bucket that contains floorplanning, placement, routing and signoff, is the largest single category at roughly 38-40% of EDA [4]; layout/routing/timing-closure alone is cited at ~32% of the tools market [4]. So the P&R-centric pool that this step lives inside is on the order of USD 5-7bn (rough estimate, derived from those shares, not a directly reported line).

| Vendor | HQ | Est. share of P&R/digital impl. | Notable |
|---|---|---|---|
| Synopsys | US (Sunnyvale) | ~40-50% | Fusion Compiler (flagship P&R), IC Compiler II, DSO.ai RL optimiser |
| Cadence | US (San Jose) | ~40-50% | Innovus (gained 10-15pp vs ICC2 2015-20), Cerebrus AI chip explorer |
| Siemens EDA | US/DE (Mentor) | low single digit in digital P&R | Aprisa P&R; stronger in verification/DFT than digital impl. |
| OpenROAD / open-source | US (academic, UCSD-led) | de minimis commercially | Free RTL-to-GDS; democratising effect at the bottom |

Concentration note: at the company level Synopsys ~31%, Cadence ~30%, Siemens ~13% of all EDA in 2024, a ~60%+ combined "two-and-a-half-player" structure [5][3]. In digital place-and-route specifically it is effectively a Synopsys/Cadence duopoly; Siemens is a distant third here despite its overall #3 position. Share is roughly stable since Fusion Compiler closed the gap Innovus had opened.

## Materials & consumables
Software has no physical consumables, but the recurring-revenue equivalents matter more than the licence. The buyer also pays for: time-based tool licences (multi-year, increasingly cloud/peak-usage metered), maintenance and support, the standard-cell and IP libraries the floorplan is built around (placed macros are bought IP), and the foundry process design kit (PDK, supplied by the fab). Roughly 80-90%+ of EDA revenue is recurring subscription / time-based licence, which is the whole reason the margins below are so high. The IP attach (memories, PLLs, I/O) sold alongside the implementation tool is a second recurring pool the same two vendors dominate.

## Volumes, revenue, profitability
Unit volume is not the right metric; the relevant count is design starts / tape-outs per year (low tens of thousands of advanced-node projects globally) times a high per-seat licence, not a per-wafer unit. The revenue pool for the digital-implementation slice that this step anchors is ~USD 5-7bn (rough estimate from the 38-40% physical-design share of a ~USD 17-18bn market [4][2]). Profitability is among the best in all of semis: Cadence posted ~86% gross margin and ~32% EBIT margin in 2024 [6]; Synopsys runs ~74-75% gross and mid-to-high-20s% EBIT [6]. The margin is earned by the tool vendor, not the chip designer, because the software is written once and licensed many times against a captive, switching-cost-locked base.

## Competitive landscape & value capture
The moat is among the deepest in technology: decades of engineering, qualified flows certified by every foundry against each process node, customer training, and brutal switching costs (re-qualifying a design flow on a competitor's tool can cost a tape-out). New AI optimisers (DSO.ai, Cerebrus) deepen rather than threaten the moat: they sit on top of the incumbent engines and claim ~10x productivity / ~20% PPA gains, raising the value of the platform the customer is already locked into. Value accrues overwhelmingly to the two US incumbents. EU / seed-relevant angle is thin: there is no European P&R challenger of scale; the live European activity is the imec-coordinated EU Chips Design Platform (subsidised access to commercial + open-source EDA for fabless SMEs) and OpenROAD-style open-source flows that lower the floor for startups rather than attack the high end.

## Market drivers, constraints & trends
Net read: the served digital-implementation pool is accelerating, pulled up by AI-accelerator design starts and a step-specific shift (backside power, multi-die) that makes floorplanning harder and stickier.

- **Drivers**
  - AI-accelerator demand is multiplying advanced-node design starts, the true unit driver for this step: TSMC's N2 family has logged ~1.5x the tape-outs 3nm had at the same point [9], and Cadence raised 2026 guidance to ~17% YoY with core EDA up 18%, citing advanced digital implementation at AI-infrastructure customers [10].
  - The AI-EDA sub-segment (RL optimisers like DSO.ai/Cerebrus, now agentic) is forecast at ~24% CAGR to 2032 [11], and these tools sit directly on floorplanning/PPA search, raising the value of the platform per seat.
  - Multi-die / 3D-IC re-architects floorplanning into system-level chiplet+interposer planning (Cadence Integrity 3D-IC, Synopsys 3DIC Compiler), a higher-priced flow than single-die P&R [12].

- **Constraints**
  - Two-vendor concentration plus brutal switching/certification costs cap who captures the upside, but also cap new-entrant growth; the pool grows with the incumbents, not around them (see body).
  - China is ~12-16% of incumbent revenue and a policy football: BIS restricted EDA sales to China in May 2025, then reversed in July 2025 [13]. A re-imposed control is a live downside to the served market.
  - Demand tracks the semiconductor capex cycle and design-start volume; a fabless slowdown outside AI would slow seat growth.

- **Trends & inflections to watch**
  - Backside power delivery (BSPDN) at 2nm forces BPDN-aware floorplanning and PDN re-architecture, a genuine tool-content increase for THIS step [14]. Tripwire: foundry 2nm BSPDN reaches volume production with EDA-certified backside-aware P&R flows shipping (TSMC/Intel, 2026-2027).
  - Agentic EDA moving from point-optimiser to full-flow autonomy (Cadence InnoStack/AgentStack for digital implementation) [10]. Tripwire: an incumbent reports a named customer taping out a 2nm-class design through an agentic implementation flow at production quality.
  - Cerebrus-class RL is past 1,000 tape-outs [15]. Tripwire: AI-optimiser attach disclosed as a distinct double-digit % of implementation-tool revenue on an earnings call.

## Connections
- [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/)
- [Logic synthesis (process step)](/semiconductor-process-flow/design/flow-logic-synthesis/)
- [Design-for-test (DFT) (process step)](/semiconductor-process-flow/design/flow-design-for-test-dft/)
- [Placement (process step)](/semiconductor-process-flow/design/flow-placement/)

- Owning idea: **Eda Chip Design** (EDA design-tool layer).

## Sources
1. SEMI / ESD Alliance, "Electronic System Design Industry Posts $4.7 Billion in Revenue in Q2 2024" — https://www.semi.org/en/semi-press-releases/electronic-system-design-industry-posts-dollar-4.7-billion-in-revenue-in-q2-2024-esd-alliance-reports
2. Persistence Market Research, EDA market forecast to 2033 (USD ~18.2bn 2026, ~9.1% CAGR) — https://www.persistencemarketresearch.com/market-research/electronic-design-automation-eda-market.asp
3. Silicon UK / market trackers on EDA 2024 vendor shares (Synopsys 31%, Cadence 30%, Siemens 13%) — https://www.silicon.co.uk/e-regulation/china-chip-design-620616
4. Data Bridge / market trackers on IC physical design & verification share (~38-40% of EDA; layout/routing/timing ~32%) — https://www.databridgemarketresearch.com/reports/global-electronic-design-automation-eda-tools-market
5. SemiAnalysis, "EDA Market Primer" (P&R competitive structure; Innovus vs ICC2/Fusion Compiler) — https://newsletter.semianalysis.com/p/eda-market-primer
6. Stock-analysis profitability data, Cadence 2024 (~86% GM, ~32% EBIT) & Synopsys (~74-75% GM) — https://www.stock-analysis-on.net/NASDAQ/Company/Synopsys-Inc/Ratios/Profitability
7. Synopsys DSO.ai (AI-driven digital implementation optimiser) — https://www.synopsys.com/ai/ai-powered-eda/dso-ai.html
8. imec, EU Chips Design Platform (European subsidised EDA access) — https://www.imec-int.com/en/press/imec-coordinates-eu-chips-design-platform
9. WccfTech / TSMC, N2 recording ~1.5x the tape-outs of 3nm at the same point — https://wccftech.com/tsmc-2nm-process-recording-1-5-times-more-tape-outs-than-3nm/
10. Cadence Q1 FY2026 results / commentary (2026 guidance raised ~17% YoY, core EDA +18%, advanced digital implementation; InnoStack/AgentStack agentic platform) — https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000044/cdns04272026ex9901.htm
11. MarketsandMarkets, AI EDA market (~24.4% CAGR 2026-2032) — https://www.marketsandmarkets.com/Market-Reports/ai-eda-market-212473295.html
12. Cadence Integrity 3D-IC platform (multi-die / chiplet system planning + Innovus-based floorplanning); Synopsys 3DIC Compiler — https://www.cadence.com/en_US/home/explore/what-is-3dic.html
13. Design&Reuse, "Synopsys, Cadence, and Siemens resume EDA supply to China" (May 2025 BIS restriction, July 2025 reversal; China ~12-16% of revenue) — https://www.design-reuse.com/news/202528998-synopsys-cadence-and-siemens-resume-eda-supply-to-china/
14. SemiEngineering, "Backside Power Delivery Gears Up For 2nm Devices" (BPDN-aware floorplanning; EDA flows for backside routing) — https://semiengineering.com/backside-power-delivery-gears-up-for-2nm-devices/
15. Cadence Cerebrus Intelligent Chip Explorer (RL chip explorer, 1,000+ tape-outs) — https://www.cadence.com/en_US/home/tools/digital-design-and-signoff/soc-implementation-and-floorplanning/cerebrus-intelligent-chip-explorer.html
