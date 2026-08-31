---
type: concept
slug: flow-routing
canonical_name: Routing (process step)
seq: 10
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
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 274
parent_concepts:
- flow-rtl-design
sources_7d: 0
sources_30d: 15
recent_mentions:
- slug: 2026-08-05-uk-neocloud-landscape-sweep
  title: UK neocloud landscape sweep — filling the coverage gap under the neocloud/serving map
  date: '2026-08-05'
  kind: web
- slug: 2026-07-27-optimal-compute-vega-investor-briefing
  title: Optimal Compute / VEGA — Investor Briefing, July 2026 (7-page DocSend)
  date: '2026-07-27'
  kind: web
- slug: 2026-07-26-ai-native-app-retention-margins
  title: AI-native application retention and gross margin benchmarks, mid-2026
  date: '2026-07-26'
  kind: web
- slug: 2026-07-22-fog-computing-middleware-amd-advancing-ai-2026-open-ai-rack
  title: 'AMD Advancing AI 2026: Open AI Rack and Agent Computer architecture'
  date: '2026-07-22'
  kind: web
- slug: 2026-07-20-ai-inference-economics-column
  title: Money Stuff-style column on AI model pricing, open weights and datacentre monetisation
  date: '2026-07-20'
  kind: web
- slug: 2026-07-15-kimi-k3-launch-moonshot
  title: Kimi K3 — Moonshot launch post (architecture, quantisation, serving requirements)
  date: '2026-07-15'
  kind: web
- slug: 2026-07-02-semianalysis-ectc2026-advanced-packaging
  title: 'ECTC 2026 Roundup: EMIB-T Roadmap, Custom HBM, HBM4 Packaging Challenges, Microfluidic Cooling, Photonic Interconnects, and More'
  date: '2026-07-02'
  kind: web
- slug: 2026-06-24-fog-computing-middleware-qualcomm-to-acquire-modular
  title: Qualcomm to Acquire Modular
  date: '2026-06-24'
  kind: web
neighbors:
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
---
> Step 10 of 56 in the semiconductor flow (Design). Prev: [Clock tree synthesis (process step)](/semiconductor-process-flow/design/flow-clock-tree-synthesis/) · Next: [Timing signoff & parasitic extraction (process step)](/semiconductor-process-flow/design/flow-timing-signoff-extraction/)

## What this step does
Routing draws the actual metal wires that connect every placed gate, flop, and clock pin on the die, turning a placed netlist into a physically connected layout. It runs after placement and clock-tree synthesis and is the last big optimisation loop before signoff. A modern routing run is millions of nets across 15-plus metal layers, solved without violating spacing, width, via, antenna, and design-rule constraints. The unit sub-processes inside it:
- **Global routing** — partition the die into a coarse grid and assign each net to grid cells / routing layers, balancing congestion against capacity (the maze-on-a-grid problem).
- **Track assignment** — map global-route segments onto specific metal tracks.
- **Detailed routing** — fill in exact wire geometry, vias, and DRC-clean connections at full resolution (the most compute-heavy sub-step at advanced nodes).
- **Search-and-repair / ECO routing** — iterate to clear remaining DRC violations and absorb late engineering-change orders.

## Where it sits and why it matters
Routing is the heart of the place-and-route (P&R) flow inside digital implementation. It is where final timing, congestion, and design-rule reality settle, so it gates whether a chip can be taped out at all. At 3nm and 2nm, routing dominates implementation runtime and is the step that breaks first, which is exactly why the tooling is concentrated and sticky: a foundry-certified router that closes timing on the latest node is close to non-substitutable for a tape-out team.

## Equipment market
There is no physical equipment here. The "tool" is software: the P&R / digital-implementation engine that contains the router. Routing is not sold standalone; it ships inside the full-flow implementation product. Total EDA + IP revenue is roughly **$18B in 2025**, growing to **$28-31B by 2030** [1][7]. Industry CAGR is **~9%** [2]. The software segment that houses physical design / P&R was about **$8.4B, or ~52% of EDA, in 2025** [1]; routing-bearing digital implementation is a meaningful slice of that but is not separately disclosed (treat any standalone "routing TAM" as an estimate, low single-digit $B).

Tool-level share in advanced-node digital implementation (the product that carries the router), 7nm and below [7]:

| Vendor | HQ | Est. share (adv-node P&R) | Notable |
|---|---|---|---|
| Cadence | San Jose, US | ~50-55% | Innovus / Genus full flow; ~4x faster global router rebuild; 25 new digital full-flow logos in 2025 |
| Synopsys | Sunnyvale, US | ~40-45% | Fusion Compiler + ICC2; unified physical synthesis; TSMC-certified N2P/A16 |
| Siemens EDA | US/Germany | low single digit in P&R | Strong in signoff (Calibre), weak in digital routing |
| Others / open-source | mixed | ~5-10% | OpenROAD / TritonRoute, academic + low-volume |

Concentration note: the Big-3 hold **>85-90% of total EDA** (Synopsys ~31%, Cadence ~30%, Siemens ~13%) [1], and inside advanced-node routing it is effectively a **Cadence-Synopsys duopoly** with no third vendor above ~5% [7].

## Materials & consumables
No physical consumables. The recurring-revenue equivalent is the licence itself. EDA is sold as **time-based subscriptions / term licences** (roughly 70-83% of revenue is recurring time-based arrangements) [7], so routing capability is consumed as multi-year seats plus peak-load cloud bursting. The "consumable" that scales with usage is compute: detailed routing is embarrassingly parallel and increasingly run on large CPU farms and cloud, which is why both incumbents push cloud P&R and AI-driven optimisation (Cadence Cerebrus, Synopsys DSO.ai) as usage-expanding add-ons.

## Volumes, revenue, profitability
Volume is measured in design starts and licensed seats, not units. There are only a few hundred advanced-node tape-outs a year, but each consumes deep, multi-seat, multi-year implementation licences, so revenue per advanced customer is very high and very sticky. The revenue pool attributable specifically to routing cannot be cleanly isolated; it is embedded in the digital-implementation product line inside Cadence's ~$5.3B and Synopsys's ~$8B (incl. Ansys) 2025 revenue [7].

Margins of the value-capturing layer are excellent and are the real signal:
- **Synopsys FY2025:** gross margin **~74%**, operating/EBIT margin **~26%** [4][5].
- **Cadence 2024-25:** gross margin **~86%**, operating margin **~32-34%** [6].
The pure-EDA software margin (Cadence's ~86% gross) is the cleaner read on routing economics; Synopsys's lower blended gross reflects IP and hardware. The margin sits with the two software vendors; the customer (the fabless designer / IDM) captures none of it and pays to remove tape-out risk.

## Competitive landscape & value capture
The moat is the strongest in the whole design flow: foundry certification per node, decades of accumulated DRC/QoR tuning, customer methodology lock-in, and a router that must close timing on bleeding-edge rules. Switching a live tape-out router mid-node is near-unthinkable, which is why share barely moves except across node transitions (Cadence's 2015-2020 Innovus gains, then re-stabilisation when Synopsys shipped Fusion Compiler) [7]. Value accrues almost entirely to **Cadence and Synopsys**; they are price-makers with subscription revenue and rising AI-add-on attach.

## Market drivers, constraints & trends
Net read: a steady ~8-9% software pool with a faster AI-and-3D overlay that can re-rate the routing-bearing slice well above the headline.

- **Drivers**
  - AI/datacentre silicon is the demand engine: hyperscaler custom chips (NVIDIA, AMD, Apple, plus in-house inference ASICs) are pulling design teams into deeper, multi-seat implementation licences, with Cadence reporting record backlog and accelerating AI demand into 2026 [10][14]. The AI-EDA layer specifically is forecast to grow from ~$4.3B (2026) to ~$15.9B (2032), a ~24% CAGR [10].
  - Every node transition sells genuinely new router capability: N2/18A are in production AI flows and 1.4nm pathfinding is being demoed, with GAA plus backside power delivery turning routing into a higher-dimensional PPA problem the duopoly charges more to solve [11].
  - Agentic/AI-driven optimisation (Cerebrus, DSO.ai, Cadence ChipStack) is a usage- and ASP-expanding attach, with vendors citing 3-10x productivity claims that justify price, not deflate it [13].

- **Constraints**
  - China export-control whiplash is the live swing risk: ~16% of Synopsys and ~12% of Cadence FY24 revenue is China; a May 2025 ban was rescinded within six weeks, but the policy optionality remains [12].
  - Open-source EDA (OpenROAD/TritonRoute) plus state-subsidised AI place-and-route engines aimed at localising flows below 3nm are a slow commoditisation cap at the low/mature-node edge [8][9].
  - The pool is gated by scarce advanced-design talent and a fixed handful of advanced tape-outs a year; routing growth rides design-start cyclicality, not unit volume [7].

- **Trends & inflections to watch**
  - 3D-IC / chiplet routing is the structural new axis: cross-die routing across 50M-plus pins, with the chiplet market forecast at ~23% CAGR to 2034 [15][16]. Tripwire: a Cadence/Synopsys 3D-IC implementation product crosses double-digit % of digital-implementation bookings (watch FY26-27 calls).
  - Agentic "autonomous router" closing real tape-outs unsupervised would step-change seat economics. Tripwire: a named foundry-certified tape-out closed end-to-end by an agentic flow at N2 or below [13][14].
  - Open-source router reaches advanced-node viability. Tripwire: an OpenROAD-based flow taping out a 7nm-or-below commercial part at volume [8].

## Connections
[EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/) · [Clock tree synthesis (process step)](/semiconductor-process-flow/design/flow-clock-tree-synthesis/) · [Timing signoff & parasitic extraction (process step)](/semiconductor-process-flow/design/flow-timing-signoff-extraction/)

- Owning idea: **Eda Chip Design** (EDA design-tool layer).