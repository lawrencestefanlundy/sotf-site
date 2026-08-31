---
type: concept
slug: flow-logic-synthesis
canonical_name: Logic synthesis (process step)
seq: 5
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
- '[[2026-05-12-semianalysis-eda-rtl-to-silicon]]'
mention_count: 15
parent_concepts:
- flow-rtl-design
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-05-12-semianalysis-eda-rtl-to-silicon
  title: 'The EDA Primer: From RTL to Silicon'
  date: '2026-05-12'
  kind: web
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
> Step 5 of 56 in the semiconductor flow (Design). Prev: [Functional verification & emulation (process step)](/semiconductor-process-flow/design/flow-functional-verification/) · Next: [Design-for-test (DFT) (process step)](/semiconductor-process-flow/design/flow-design-for-test-dft/)

## Where it sits and why it matters
Synthesis is the first step where the design is committed to a specific foundry process (the cell library is process-specific), so it is the gate through which all downstream physical work flows. Quality-of-results here (timing slack, area, leakage) sets the ceiling for the whole back-end. It is also one of the stickiest points in the entire EDA toolchain: synthesis constraints, scripts and reference flows are deeply embedded in a customer's methodology, and the output feeds directly into the same vendor's place-and-route, making switching costs unusually high. This is why the synthesis seat is a strategic anchor that vendors use to pull through the rest of the digital implementation flow.

## Equipment market
There is no physical equipment at this step. The "tool" market here is the digital design and implementation slice of EDA software. Total EDA (plus IP) was roughly $18B in 2025 and growing at ~13% CAGR, with the broader EDA software market often cited at $14-17B for 2024-2025 and a 9-11% CAGR to the mid-2030s [1][2][3]. Digital design and implementation (synthesis + place-and-route + physical verification) is the largest software sub-segment; IC physical design and verification alone is cited around $4.3B [4]. Standalone logic synthesis is a fraction of that (rough estimate, low-single-digit $B at most as a discrete licence line; it is usually bundled into broader implementation suites, so a clean number is not published).

| Vendor | HQ | Est. share (synthesis) | Notable |
|--------|-----|------|---------|
| Synopsys | USA | ~84-85% [5] | Design Compiler (incumbent), Fusion Compiler, DSO.ai (AI-driven optimisation) |
| Cadence | USA | secondary alternative [5] | Genus Synthesis, Cerebrus (AI flow), pulled through by Innovus P&R |
| Siemens EDA | Germany/USA | small | Precision RTL synthesis (stronger in FPGA/verification than ASIC synthesis) |
| YosysHQ | Austria | niche/open-source | Yosys + ABC; FPGA and open-PDK ASIC flows (OpenLane), not used at leading-edge |

Concentration note: synthesis is the most concentrated tool category in EDA. Synopsys Design Compiler is reported at ~84-85% share, a near-monopoly that has held for years; Cadence Genus is the only credible commercial alternative [5]. The Big-3 (Synopsys ~31%, Cadence ~30%, Siemens ~13%) take >90% of all EDA revenue [1][6].

## Materials & consumables
No physical consumables. The recurring-revenue analogues are: (1) the foundry standard-cell and IP libraries the synthesiser maps onto (TSMC/Samsung/Intel PDKs, plus Synopsys/Cadence/Arm library IP), and (2) the EDA licences themselves, sold as time-based subscriptions (typically 3-year terms) rather than perpetual. That subscription model is the "consumable": ~90%+ of EDA revenue recurs, which is the core of the duopoly's quality. A newer consumable dynamic is AI-tool compute: DSO.ai and Cerebrus reportedly drive 3-5x token/compute consumption per design project, an emerging metered-usage layer on top of seat licences [5].

## Volumes, revenue, profitability
"Volume" is design starts, not units: a few thousand serious ASIC/SoC tape-outs per year worldwide, of which leading-edge (sub-7nm) is a few hundred, and Synopsys claims involvement in ~100% of 3nm tape-outs and 2nm test chips [5]. The revenue pool attributable purely to synthesis is modest in absolute terms (rough estimate, low-single-digit $B) but strategically outsized because it anchors the much larger implementation suite. Profitability is exceptional: software gross margins are high (Cadence GAAP gross margin ~86%, Synopsys ~74% blended including IP/hardware), and non-GAAP operating margins are 37% (Synopsys FY2024) to ~42% (Cadence FY2024) [5][7][8]. The margin is earned by the tool vendor, not the foundry or fabless customer; it is among the most profitable software in the semiconductor stack.

## Competitive landscape & value capture
The moat is methodology lock-in plus correlated tool quality: a customer's golden synthesis scripts, library characterisation and sign-off correlation are tuned to one vendor's engine, and synthesis pulls through that vendor's place-and-route and timing sign-off. Value accrues overwhelmingly to Synopsys, with Cadence the durable number two; this has been stable for over a decade and is reinforced by AI flows that further entangle the design. EU/seed-relevant: the only structural challenger is open-source (Yosys, maintained largely by YosysHQ GmbH in Austria, with the ABC engine), which is real for FPGA and open-PDK/academic ASIC flows but has no foothold at the leading edge where the money is; a seed bet here is a tooling-around-open-source or AI-synthesis play, not a frontal assault. Routing line: the value pool is a high-margin software duopoly compounding at ~13%, so the cleanest exposure is public markets (own SNPS / CDNS directly, holding the synthesis monopoly and the implementation suite it pulls through). Early-stage exposure (Lunar / angel) is only credible via AI-native or open-source-adjacent EDA startups, high-risk because the incumbents absorb AI fast. There is no hardware/materials wedge at this software-only step, so it is orthogonal to a pre-seed deep-tech materials mandate.

## Market drivers, constraints & trends
Net read: the synthesis-anchored implementation pool is set to keep compounding faster than its long-run ~10% trend, with a re-rate already underway from AI-priced tools, though China is the offset.

- **Drivers** — Custom-silicon design starts are exploding: TrendForce puts custom AI-ASIC shipment growth at 44.6% in 2026 versus 16.1% for merchant GPUs, with every hyperscaler plus OpenAI and Anthropic now taping out their own chips [10][11]. Each new SoC owner is a fresh full-flow seat. AI-priced tools lift revenue per seat without new headcount: Synopsys cites ~20% renewal uplift from DSO.ai, and Cerebrus added ~50 new logos in a single quarter with 1,000+ tape-outs to date [9][12]. Synopsys's ~$35B Ansys close (2025) bundles synthesis into a silicon-to-systems multi-die platform [9].
- **Constraints** — China is the live drag: US controls now require licences for all EDA sales to China (~16% of Synopsys, ~12% of Cadence FY24 revenue), and both guide flat-to-down there [13][14]. The category is also already a near-monopoly, so growth is paced by end-market design starts, not share gains. Open-source (Yosys) and AI-RTL startups cap pricing power at the low end over time.
- **Trends & inflections to watch** — Agentic RTL generation (ChipAgents raised $21M Series A, 97.4% on VerilogEval) compresses front-end effort and could shift value from per-seat licences toward metered tokens [15]. Multi-die/chiplet flows (UCIe, 2nm) multiply blocks synthesised per system. Tripwire: a quarter where AI-tool token/consumption revenue is broken out and exceeds 10% of digital-design revenue would confirm the metered re-rate; a second is custom-ASIC design starts holding >40% growth into 2027 [10][12].

## Connections
- [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/) (cluster page for the design-tools layer)
- **Eda Chip Design** (thesis)
- Prev: [Functional verification & emulation (process step)](/semiconductor-process-flow/design/flow-functional-verification/) · Next: [Design-for-test (DFT) (process step)](/semiconductor-process-flow/design/flow-design-for-test-dft/)

## Sources
1. SemiAnalysis, EDA Market Primer (total EDA+IP ~$18B 2025, ~13% CAGR, synthesis share, margins, tape-out share) — https://newsletter.semianalysis.com/p/eda-market-primer
2. Precedence Research, EDA Software Market ($14.55B 2025 → $34.71B 2035, 9.08% CAGR) — https://www.precedenceresearch.com/electronic-design-automation-software-market
3. Mordor Intelligence, EDA Tools Market — https://www.mordorintelligence.com/industry-reports/electronic-design-automation-eda-tools-market
4. Dataintelo / market reports, IC physical design & verification segment (~$4.29B) — https://dataintelo.com/report/electronic-design-automation-eda-market
5. SemiAnalysis, EDA Market Primer (Design Compiler ~84-85% synthesis share; Genus secondary; DSO.ai/Cerebrus token consumption; operating margins) — https://newsletter.semianalysis.com/p/eda-market-primer
6. Silicon UK / market data (Big-3 shares: Synopsys 31%, Cadence 30%, Siemens 13%, 2024) — https://www.silicon.co.uk/e-regulation/china-chip-design-620616
7. Synopsys FY2024 results (segments, gross margin ~74%) — https://www.prnewswire.com/news-releases/synopsys-posts-financial-results-for-fourth-quarter-and-fiscal-year-2024-302322901.html
8. Cadence FY2024 metrics (gross margin ~86%, operating margin ~29% GAAP / ~42.5% non-GAAP) — https://secure.macrotrends.net/stocks/charts/CDNS/cadence-design-systems/operating-margin
9. SemiAnalysis / Klover.ai, Synopsys AI strategy + Ansys $35B + AI renewal uplift (~20%) — https://www.klover.ai/synopsys-ai-strategy-analysis-of-dominance-in-tools-services-for-semiconductor-design-manufacturing/
10. TrendForce, custom AI-ASIC shipment growth 44.6% vs 16.1% GPU in 2026; ASIC 27.8% of AI servers — https://www.techtimes.com/articles/317225/20260526/custom-ai-chips-outpace-nvidia-gpu-growth-2026-asic-shipments-set-triple-gpu-rate.htm
11. Tom's Hardware, custom AI ASIC state of play May 2026 (hyperscalers + OpenAI/Anthropic design wins) — https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia
12. Cadence FY2025 8-K / commentary, Cerebrus ~50 new logos in Q1, 1,000+ tape-outs to date — https://www.sec.gov/Archives/edgar/data/0000813672/000081367225000046/cdns4282025ex9901.htm
13. EE Times, US restricts EDA software sales to China (licences for all sales) — https://www.eetimes.com/u-s-restricts-eda-software-sales-to-china/
14. TrendForce, China revenue at risk from US EDA curbs (Synopsys ~16%, Cadence ~12% of FY24) — https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/
15. Sacra, ChipAgents $21M Series A, agentic RTL generation, 97.4% VerilogEval — https://sacra.com/c/chipagents/
