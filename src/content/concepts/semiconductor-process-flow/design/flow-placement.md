---
type: concept
slug: flow-placement
canonical_name: Placement (process step)
seq: 8
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
- '[[2025-09-23-the-compute-gradient]]'
- '[[2025-08-12-ai-and-junior-white-collar-automation]]'
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 125
parent_concepts:
- flow-rtl-design
sources_7d: 0
sources_30d: 22
recent_mentions:
- slug: 2026-06-02-agentic-runtime-silicon-necessity
  title: Deep-research dossier — does the stateful agent runtime / control-plane layer need a novel silicon primitive?
  date: '2026-06-02'
  kind: web
- slug: 2026-03-17-compute-specialisation-equilibrium-aws-cerebras
  title: AWS-Cerebras Disaggregated Inference via Amazon Bedrock
  date: '2026-03-17'
  kind: web
- slug: 2026-02-26-compute-specialisation-equilibrium-callosum-heterogeneous
  title: 'Callosum: Heterogeneous Intelligence Infrastructure'
  date: '2026-02-26'
  kind: web
- slug: 2026-02-23-compute-specialisation-equilibrium-custom-silicon
  title: Custom Silicon Inflection 2026
  date: '2026-02-23'
  kind: web
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-09-23-the-compute-gradient
  title: The Compute Gradient
  date: '2025-09-23'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2025-08-12-ai-and-junior-white-collar-automation
  title: 'AI and Junior White Collar Automation: Update after EIG’s New Report'
  date: '2025-08-12'
  kind: substack
neighbors:
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
---
> Step 8 of 56 in the semiconductor flow (Design). Prev: [Floorplanning & power planning (process step)](/semiconductor-process-flow/design/flow-floorplanning-power/) · Next: [Clock tree synthesis (process step)](/semiconductor-process-flow/design/flow-clock-tree-synthesis/)

## What this step does
Placement is the stage of physical implementation (place-and-route, P&R) where the place-and-route tool assigns a physical location on the die to every standard cell in the synthesised netlist, inside the floorplan handed over from the previous step. It is an optimisation problem with hundreds of millions of cells competing on timing, wirelength, congestion and power, so the result sets how routable the chip is and how much of its timing budget survives. Done badly, no amount of downstream routing can recover the design. The unit sub-processes inside it:
- Global placement (spread cells coarsely to minimise total wirelength and balance density)
- Legalisation (snap cells onto legal rows/sites, remove overlaps)
- Detailed placement (local cell swaps and shifts to recover timing and reduce congestion)
- Timing-driven and congestion-driven optimisation (cell sizing, buffering, in-place restructuring)
- Placement of physical-only cells (tap cells, decap, filler) and handoff to clock-tree synthesis

## Where it sits and why it matters
Placement sits in the middle of the digital back-end, between floorplanning and clock-tree synthesis, and it is the first point where the abstract netlist becomes a real geometry. The same tool that does placement does routing, signoff timing and physical verification, so the customer is buying a flow, not a feature. That sequential dependency is the lock-in: change the placement engine and you re-run route, signoff and verification, so customers almost never switch mid-design. Placement is also the part of the flow where AI has bitten hardest, because it is a huge combinatorial search that reinforcement learning can attack directly.

## Equipment market
There is no physical "equipment" here; the value is software licences and compute. The relevant pool is the place-and-route / physical implementation slice of EDA. Total EDA software was about $17.2bn in 2024, growing ~10% CAGR to the early 2030s [1][2]. IC physical design and verification (the bucket P&R sits in) is the single largest component, roughly 38% of EDA spend in 2025 [3], which puts the physical-implementation pool very roughly in the $5-6bn/yr range (estimate, derived from [1][3], not a directly reported figure). P&R is the one EDA category that has seen real share movement in a decade [4].

| Vendor | HQ | Est. share of P&R / phys. impl. | Notable |
|--------|-----|-------------------------------|---------|
| Synopsys | USA | ~45-50% (rough est.) | Fusion Compiler, IC Compiler II (ICC2); DSO.ai layered on top |
| Cadence | USA | ~40-45% (rough est.) | Innovus; gained 10-15pp on Synopsys 2015-2020 then stabilised [4]; Cerebrus / Cerebrus AI Studio |
| Siemens EDA | Germany/USA | low single digits in P&R | Aprisa P&R; ~13% of total EDA but weak in digital impl. [2] |

Concentration note: this is a duopoly. Synopsys (~31% of all EDA) and Cadence (~30%) together hold over 60% of total EDA and an even higher combined share of advanced-node P&R, with Siemens a distant third [2][5]. At 7nm and below, placement is effectively a two-horse race between Synopsys and Cadence. Per-segment P&R shares above are estimates; vendors do not break out P&R revenue separately.

## Materials & consumables
No physical consumables. The recurring spend is the software itself: P&R sells as time-based licences (3-year terms are typical) plus the compute and cloud cycles AI placement burns. The "consumable" analogue is licence renewals and AI-tool token/compute consumption. SemiAnalysis notes 95%+ customer retention combined with 3-7% annual contractual escalators in the digital flow, and that AI-enhanced renewals (DSO.ai-style) carry roughly a 20% revenue uplift over the baseline contract [4]. The required process design kit (PDK) and standard-cell library come from the foundry, not the EDA vendor, but they are inputs to placement rather than a sold consumable.

## Volumes, revenue, profitability
"Units" are tapeouts and design starts, not wafers; the AI-placement adoption proxy is commercial tapeouts. Synopsys DSO.ai passed 100 commercial tapeouts (first in Aug 2021) [6]; Cadence Cerebrus passed 1,000+ production designs by early 2025 [4][7]. The revenue pool is the ~$5-6bn physical-implementation slice (estimate) inside the $17bn EDA market [1][3]. Margins are why this is a great business: company-level FY2024 gross margins are ~84% at Synopsys and ~86% at Cadence, with non-GAAP operating margins of ~37% (Synopsys) and ~42.5% (Cadence) [8][9][10][11]. The margin is earned by the two EDA vendors; the chip designer pays the licence and captures the design value downstream.

## Competitive landscape & value capture
The moat is the flow, not any single tool. Placement is locked in by sequential dependency (re-running it forces re-run of route + signoff), deep methodology embedding (scripts, constraints, reference flows), and tight coupling to foundry-certified reference flows at each node. AI placement has not broken the duopoly; if anything it has reinforced it, because both incumbents folded reinforcement learning into their own engines. Google's AlphaChip (Nature 2021, addendum 2024) showed RL could generate superhuman macro placement and is open-sourced, but it has been absorbed as a capability inside Synopsys DSO.ai and Cadence Cerebrus rather than spawning a viable standalone challenger [12][13]. There is no European or seed-stage player of consequence in P&R itself; the open-source RTL-to-GDS flow OpenROAD is real and improving but is not a commercial threat at advanced nodes. Seed-relevant adjacency exists only one layer out (AI optimisation wrappers, verification, analog/RF tooling), not in core placement.

## Market drivers, constraints & trends
Net read: the P&R/physical-implementation slice grows faster than the broad EDA market this cycle, because the two forces lifting it (more design starts and harder-to-place geometries) compound, but it carries real China-policy tail risk. Total EDA is now put at ~$19-21bn (2025-26) on ~8% CAGR to ~$31bn by 2031, and the AI-EDA layer that wraps placement grows far faster, ~24% CAGR ($4.3bn 2026 to ~$15.9bn 2032) [14][15][16].

- **Drivers**
  - Custom-silicon explosion: custom ASIC AI-server shipments grow ~45% YoY in 2026 (nearly triple merchant-GPU growth), and every hyperscaler/Tier-2 accelerator is a new design start that re-runs placement on the same licensed flow [17][18].
  - Geometry difficulty: GAA + backside power + multi-die push a ~10x rise in design-rule checks vs 7nm, so each placement job consumes more tool runtime, more AI optimisation cycles and higher-tier licences [14].
  - AI-renewal uplift: RL/agentic placement layers (DSO.ai, Cerebrus) carry ~20% revenue uplift over baseline contracts on 95%+ retention, so the same customer base re-rates upward [4][16].

- **Constraints**
  - China export controls: a 29 May 2025 BIS directive briefly halted all EDA sales to China (Synopsys ~$990m/16%, Cadence ~$550m/12% of FY24 revenue), lifted again Jul 2025 but now a recurring policy switch on a tenth-plus of revenue [19][20].
  - Duopoly capex intensity: both incumbents reinvest >30% of revenue in R&D to stay node-certified, so margin expansion is capped even as revenue compounds [15].
  - Cyclicality and design-start sensitivity: the served market tracks tapeout/design-start volume, which softens with semiconductor capex cycles.

- **Trends & inflections to watch**
  - Agentic autonomy: Cadence pushed ChipStack to L5 and Synopsys shipped an L4 AgentEngineer flow in 2026; tripwire — either incumbent reporting a placement-to-signoff loop run with no human-in-the-loop on a production tapeout [21][22].
  - Multi-die / 3D-IC placement: placement is extending to cross-die co-placement; tripwire — a foundry-certified 3D-IC reference flow citing AI co-placement at A16/N2 by end-2026 [14].
  - Democratisation of design: Arm CSS-style platforms lowering the ASIC entry bar; tripwire — a Tier-2 cloud or enterprise taping out a first custom accelerator on a commodity AI-P&R flow [18].

## Connections
[EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/)

- Owning idea: **Eda Chip Design** (EDA design-tool layer).

## Sources
1. Aspirenis / market sizing summary — EDA $17.2bn (2024), ~10.5% CAGR to 2032. https://www.persistencemarketresearch.com/market-research/electronic-design-automation-eda-market.asp
2. TrendForce via Silicon UK — Synopsys ~31%, Cadence ~30%, Siemens ~13% EDA share (2024). https://www.silicon.co.uk/e-regulation/china-chip-design-620616
3. EDA market by component — IC physical design & verification ~38% of EDA (2025). https://www.psmarketresearch.com/market-analysis/electronic-design-automation-market
4. SemiAnalysis, EDA Market Primer — P&R is the only category with real share movement; retention 95%+, 3-7% escalators, ~20% AI renewal uplift; Cadence Cerebrus 1,000+ tapeouts; Synopsys/Cadence FY24 operating margins. https://newsletter.semianalysis.com/p/eda-market-primer
5. Klover.ai — Synopsys EDA dominance analysis. https://www.klover.ai/synopsys-ai-strategy-analysis-of-dominance-in-tools-services-for-semiconductor-design-manufacturing/
6. EE Times — AI-powered chip design mainstream; DSO.ai 100 commercial tapeouts. https://www.eetimes.com/ai-powered-chip-design-goes-mainstream/
7. Cadence — Cerebrus AI Studio / Cerebrus Intelligent Chip Explorer (1,000+ production designs). https://www.cadence.com/en_US/home/tools/digital-design-and-signoff/soc-implementation-and-floorplanning/cadence-cerebrus-ai-studio.html
8. Synopsys FY2024 10-K — revenue $6.127bn, gross margin ~84.1%. https://www.sec.gov/Archives/edgar/data/0000883241/000088324124000024/snps-20241031.htm
9. Synopsys Q4/FY2024 results press release — operating margin context. https://investor.synopsys.com/news/news-details/2024/Synopsys-Posts-Financial-Results-for-Fourth-Quarter-and-Fiscal-Year-2024/default.aspx
10. Cadence FY2024 results — revenue $4.641bn, gross margin ~86%, non-GAAP operating margin 42.5%. https://www.gurufocus.com/news/2702619/cadence-design-systems-exceeds-q4-2024-expectations-with-124-eps-and-1356-billion-revenue
11. Cadence FY2024 CFO commentary (8-K). https://www.sec.gov/Archives/edgar/data/0000813672/000081367225000016/cfocommentary2182025ex9902.htm
12. Nature — A graph placement methodology for fast chip design (AlphaChip), 2021 + 2024 addendum. https://www.nature.com/articles/s41586-021-03544-w
13. Google DeepMind — How AlphaChip transformed computer chip design (open-sourced, adopted by external chipmakers). https://deepmind.google/blog/how-alphachip-transformed-computer-chip-design/
14. SemiEngineering — AI's growing impact on chip design & EDA; GAA + backside power + multi-die ~10x rise in DRCs vs 7nm; TSMC N2 HVM 2H 2025; Synopsys A16/N2P backside-routing certification. https://semiengineering.com/ai-growing-impact-on-chip-design-and-eda-tools/
15. PS Market Research — EDA market sizing & forecast (~$19-21bn 2025-26, ~8% CAGR to ~$31bn 2031; >30% R&D reinvestment by incumbents). https://www.psmarketresearch.com/market-analysis/electronic-design-automation-market
16. MarketsandMarkets — AI EDA market $4.27bn (2026) to $15.85bn (2032), ~24.4% CAGR. https://www.marketsandmarkets.com/Market-Reports/ai-eda-market-212473295.html
17. Tom's Hardware — Custom AI ASIC state of play (May 2026); custom ASIC shipments +44.6% YoY 2026, ~27.8% of AI-server market. https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia
18. Arm Newsroom — How Arm CSS/CSA democratize custom AI silicon (chiplet platforms lowering ASIC entry bar). https://newsroom.arm.com/blog/how-arms-css-platform-democratizes-custom-ai-silicon
19. TrendForce — China revenue at risk as US curbs hit EDA giants; 29 May 2025 BIS directive halting all EDA sales to China; Synopsys $989.5m/16%, Cadence $550m/12% of FY24 revenue. https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/
20. AInvest — EDA's rebound as US lifts EDA-to-China export restrictions (Jul 2025), revenue-recovery path for Synopsys/Cadence. https://www.ainvest.com/news/eda-rebound-synopsys-cadence-poised-growth-trade-tensions-ease-2507/
21. Futurum Group — Cadence and Synopsys accelerate the agentic EDA race at Computex 2026 (Cadence ChipStack L5, Synopsys L4 AgentEngineer). https://futurumgroup.com/insights/cadence-and-synopsys-accelerate-agentic-eda-race-at-computex/
22. Synopsys news — Outlines vision for engineering the future; L4 agentic design-and-verification workflow via AgentEngineer (11 Mar 2026). https://news.synopsys.com/2026-03-11-Synopsys-Outlines-Vision-for-Engineering-the-Future
