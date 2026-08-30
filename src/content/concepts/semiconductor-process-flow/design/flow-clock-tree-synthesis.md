---
type: concept
slug: flow-clock-tree-synthesis
canonical_name: Clock tree synthesis (process step)
seq: 9
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
mention_count: 8
sources_7d: 0
sources_30d: 1
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
> Step 9 of 56 in the semiconductor flow (Design). Prev: [Placement (process step)](/semiconductor-process-flow/design/flow-placement/) · Next: [Routing (process step)](/semiconductor-process-flow/design/flow-routing/)

## What this step does
Clock tree synthesis (CTS) builds the physical network that delivers the clock signal from its source to every flip-flop and clocked element on the chip, after cells have been placed but before signal routing. The goal is to get the clock edge to thousands or millions of registers at as close to the same instant as possible (low skew) with controlled insertion delay, while not blowing the power budget (the clock network is often the single largest dynamic-power consumer on a digital chip). The unit sub-processes inside it:
- Clock-source and sink identification, clustering of clock endpoints
- Buffer and inverter insertion to balance the tree (or build a clock mesh/H-tree for tight-skew blocks)
- Skew and insertion-delay balancing across the clusters
- Clock-gating cell integration for power, and useful-skew optimisation (deliberately skewing to steal timing slack)
- Concurrent clock-and-data optimisation (resizing/moving data-path cells alongside the clock), then post-CTS timing analysis handoff to routing

## Where it sits and why it matters
CTS sits in the middle of physical implementation (place-and-route), downstream of [Placement (process step)](/semiconductor-process-flow/design/flow-placement/) and feeding [Routing (process step)](/semiconductor-process-flow/design/flow-routing/). It matters because the clock network gates the chip's maximum frequency and a large share of its power: bad skew either fails timing (the chip will not run at spec) or forces conservative guard-banding that leaves performance on the table. Modern tools fold CTS into "concurrent" optimisation engines (Cadence calls its flagship Clock Concurrent Optimization, CCOpt) so the clock and the data path are optimised together rather than in sequence, which is the main quality differentiator at advanced nodes [1][2]. It is a make-or-break step for power-performance-area (PPA), but commercially it is not a product you can buy on its own.

## Equipment market
No physical equipment. The relevant pool is the digital implementation (place-and-route) slice of EDA software, and CTS has no independent merchant market: it ships as a feature inside the P&R tool, not as a standalone licence. The category sits within EDA, roughly $16.5B in 2025 growing ~8% (some trackers put total EDA+IP nearer $18B at ~13%) [3][4]. IC physical design and verification (placement, routing, CTS, timing closure, DRC/LVS) is the largest EDA segment by component at ~37-38% of the market in 2025, so order-of-magnitude $6B, of which CTS is an embedded sub-feature with no separately published number [5].

| Vendor | HQ | Est. share (P&R suite that contains CTS) | Notable |
|--------|-----|------|---------|
| Synopsys | USA | co-leader [1][6] | IC Compiler II and Fusion Compiler (CTS engine inside); DSO.ai for AI-driven PPA |
| Cadence | USA | co-leader, gained 10-15pp 2015-2020 [1] | Innovus with CCOpt (Clock Concurrent Optimization); Cerebrus AI flow |
| Siemens EDA | Germany/USA | small in digital P&R | Aprisa place-and-route (stronger in analog/custom and verification) |
| OpenROAD / open-source | USA (academic) | niche / non-commercial | TritonCTS 2.0 CTS engine inside the RTL-to-GDSII flow; used at mature nodes and in research [7] |

Concentration note: P&R is the one EDA tool category that saw meaningful share movement in the last decade. Cadence Innovus took 10-15 percentage points off Synopsys IC Compiler II between 2015 and 2020, then the two stabilised as Synopsys countered with Fusion Compiler; "everything else is locked" [1]. So unlike synthesis (a Synopsys near-monopoly) or signoff, the CTS-bearing P&R suite is a genuine two-horse race, with Siemens a distant third and the Big-3 taking >90% of all EDA revenue [6].

## Materials & consumables
No physical consumables. The recurring-revenue analogues: (1) the foundry standard-cell libraries the tool inserts clock buffers and gating cells from (TSMC/Samsung/Intel PDKs plus Synopsys/Cadence/Arm library IP), and (2) the EDA licences themselves, sold as multi-year time-based subscriptions, not perpetual. That subscription model is the "consumable", and >90% of EDA revenue recurs, which is the core of the duopoly's quality. An emerging metered layer is AI optimisation: AI-enhanced renewals reportedly carry a ~20% revenue uplift, and Cadence's AI flow (Cerebrus) reached 1,000+ tapeouts and 100% penetration of its top-10 digital customers, a usage-based dynamic stacking on top of seat licences [1].

## Volumes, revenue, profitability
"Volume" is design starts, not units: a few thousand serious digital ASIC/SoC tape-outs per year worldwide, of which leading-edge (sub-7nm) is a few hundred, and every one of them runs CTS as a mandatory step in the P&R flow. The revenue pool attributable purely to CTS is not separable (it is a feature inside a tool that is itself inside a suite), but the host P&R/physical-design segment is the largest in EDA (~$6B, rough estimate from the ~37-38% share) [5]. Profitability is exceptional and earned by the tool vendor, not the foundry or fabless customer: software gross margins are high (Cadence ~86%), and non-GAAP operating margins run 37% (Synopsys FY2024) to ~42.5% (Cadence FY2024, highest of the Big-3) [1][8]. This is among the most profitable software in the semiconductor stack.

## Market drivers, constraints & trends
Net read: the served market (the digital-implementation EDA slice CTS rides inside) is accelerating, pulled by AI design demand and the rising clock-distribution difficulty of multi-die parts, with a single sharp tail risk in China export policy.

- **Drivers**
  - AI/datacentre design demand is lifting the host suite directly: Cadence Q1 FY2026 revenue grew 18.7% YoY to $1.474B with a record $8.0B backlog, and it raised full-year 2026 guidance to ~17% growth on AI-driven tool adoption [10][11]. The faster-growing AI-EDA layer is forecast at ~24% CAGR ($4.27B 2026 to $15.85B 2032) [12].
  - 3D-IC / multi-die is the strongest CTS-specific tailwind: inter-die skew and delay alignment across stacked dies is a hard new clock problem, and Cadence's 3D-IC-linked System Design & Analysis grew 18% YoY [11][13]. More dies per design means more independent clock trees to balance and cross-couple.
  - GAA + backside power delivery (Intel 18A in production; PowerVia/PowerDirect) reshape the clock and power mesh, forcing tools to re-learn the flow and re-characterise libraries, which deepens methodology lock-in on the incumbent P&R engine [14][15].
- **Constraints**
  - China export controls are the dominant risk: BIS curbs imposed Q3 2025 then rescinded already dented Synopsys' China business; China was ~16% of Synopsys and ~12% of Cadence FY2024 revenue, all now licence-gated case by case [16][17].
  - Commoditisation at the bottom: open-source TritonCTS (OpenROAD) covers mature-node CTS for free, capping pricing power outside the leading edge.
  - Cyclicality and concentration: design starts track the broader semi cycle, and the AI-renewal uplift depends on a handful of leading-edge customers continuing to tape out.
- **Trends & inflections to watch**
  - Agentic AI flows (Cadence AgentStack/ChipStack, Synopsys agentic 3DIC Compiler) move CTS toward usage-metered revenue on top of seat licences. Tripwire: a vendor disclosing AI/agentic design as a separately reported, double-digit revenue line by FY2027 [11][18].
  - High-NA EUV node ramp (Intel 14A risk production 2027, first GAA+High-NA node) seeds a fresh wave of leading-edge design starts. Tripwire: first 14A customer tapeouts reported through an incumbent P&R flow in 2027 [19].
  - Backside-power adoption broadening beyond Intel. Tripwire: TSMC/Samsung backside-power node entering volume design starts, each needing re-tuned clock/power-mesh CTS methodology [14].

## Connections
- [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/) (cluster page for the design-tools layer)
- Prev: [Placement (process step)](/semiconductor-process-flow/design/flow-placement/) · Next: [Routing (process step)](/semiconductor-process-flow/design/flow-routing/)

- Owning idea: **Eda Chip Design** (EDA design-tool layer).

## Sources
1. SemiAnalysis, EDA Market Primer (Innovus +10-15pp vs ICC2 2015-2020 then stabilised on Fusion Compiler; "everything else is locked"; CCOpt; Cerebrus 1,000+ tapeouts / 100% top-10 penetration; ~20% AI renewal uplift; operating margins 37.3% SNPS / 42.5% CDNS FY2024) — https://newsletter.semianalysis.com/p/eda-market-primer
2. Cadence, Innovus Clock Concurrent Optimization (CCOpt) for CTS — https://www.cadence.com/en_US/home/training/all-courses/86198.html
3. The Business Research Company, EDA Market 2025 ($16.52B 2025 → $17.85B 2026, 8.1% CAGR) — https://www.thebusinessresearchcompany.com/report/electronic-design-automation-eda-global-market-report
4. SemiAnalysis / Precedence Research, total EDA(+IP) sizing (~$18B at ~13%; software $14.55B 2025 → $34.71B 2035, 9.08% CAGR) — https://www.precedenceresearch.com/electronic-design-automation-software-market
5. Mordor Intelligence / market trackers, IC physical design and verification ~37-38% of EDA in 2025 (placement, routing, timing closure, DRC/LVS) — https://www.mordorintelligence.com/industry-reports/electronic-design-automation-eda-tools-market
6. Silicon UK / market data (Big-3 shares: Synopsys 31%, Cadence 30%, Siemens 13%, 2024) — https://www.silicon.co.uk/e-regulation/china-chip-design-620616
7. OpenROAD documentation, Clock Tree Synthesis based on TritonCTS 2.0 — https://openroad.readthedocs.io/en/latest/main/src/cts/README.html
8. Macrotrends, Cadence operating/gross margin (gross ~86%, non-GAAP operating ~42.5%) — https://secure.macrotrends.net/stocks/charts/CDNS/cadence-design-systems/operating-margin
9. arXiv, CTS-Bench: Benchmarking Graph Coarsening Trade-offs for GNNs in Clock Tree Synthesis (academic ML-for-CTS line) — https://arxiv.org/html/2602.19330
10. Cadence, Reports First Quarter 2026 Financial Results (Q1 FY2026 revenue $1.474B, +18.7% YoY; record $8.0B backlog) — https://www.businesswire.com/news/home/20260426710019/en/Cadence-Reports-First-Quarter-2026-Financial-Results
11. StockTitan / Cadence Q1 FY2026 (raised FY2026 outlook to ~17% growth; AgentStack across chip/3D-IC/system; System Design & Analysis +18% YoY; IP +22%) — https://www.stocktitan.net/news/CDNS/cadence-reports-first-quarter-2026-financial-91y9vl2rdx3g.html
12. MarketsandMarkets, AI EDA Market 2026-2032 ($4.27B 2026 → $15.85B 2032, ~24.4% CAGR) — https://www.marketsandmarkets.com/Market-Reports/ai-eda-market-212473295.html
13. Semiconductor Engineering, What Is 3D-IC Technology (cross-die timing/synchronisation, inter-die delay and skew modelling for multi-die clock alignment) — https://semiengineering.com/what-is-3d-ic-technology-fundamentals-architecture-and-design-concepts/
14. Semiconductor Engineering, VLSI 2026: Intel 18A Platform (improved clock distribution; GAA + PowerVia backside power; routing/power-mesh re-learning for EDA tools) — https://semiengineering.com/vlsi-2026-intel-18a-platform-momentum-from-devices-to-routed-designs/
15. Synopsys Blog, What are Gate-All-Around (GAA) Transistors (high-quality IP and EDA flows essential for GAA design) — https://www.synopsys.com/blogs/chip-design/what-are-gate-all-around-gaa-transistors.html
16. TrendForce, China Revenue at Risk as US Curbs Slam EDA Giants (Synopsys ~16% / Cadence ~12% of FY2024 revenue from China; licence requirement for all China sales) — https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/
17. Synopsys, Form 10-Q FY2026 (BIS restrictions imposed Q3 2025 then rescinded negatively impacted China business; challenging near-term China environment) — https://www.sec.gov/Archives/edgar/data/0000883241/000088324126000018/snps-20260430.htm
18. Futurum, Synopsys Converge 2026 / multi-physics design (agentic automation in 3DIC Compiler, sign-off engines upstream for chiplet design) — https://futurumgroup.com/insights/synopsys-converge-is-the-new-synopsys-ready-to-own-multi-physics-design/
19. Tom's Hardware, Intel Foundry roadmap / 14A (risk production 2027, first node with High-NA EUV and 2nd-gen RibbonFET GAA; early 14A PDK shared with lead customers) — https://www.tomshardware.com/pc-components/cpus/intel-foundry-roadmap-update-new-18a-pt-variant-that-enables-3d-die-stacking-14a-process-node-enablement
