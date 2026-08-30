---
type: concept
slug: flow-rtl-design
canonical_name: RTL design (HDL) (process step)
seq: 3
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
> Step 3 of 56 in the semiconductor flow (Design). Prev: [Semiconductor IP licensing (process step)](/semiconductor-process-flow/design/flow-ip-licensing-cores/) · Next: [Functional verification & emulation (process step)](/semiconductor-process-flow/design/flow-functional-verification/)

## What this step does
Register-transfer-level (RTL) design is where the chip's intended behaviour is written as code in a hardware description language (Verilog/SystemVerilog or VHDL), describing what each clock cycle does to data moving between registers. It is the first step where a human (now increasingly an AI assistant) authors the actual logic, sitting between the licensed IP blocks (step 2) and the verification that proves the code is correct (step 4). Sub-processes inside it:
- Micro-architecture and module partitioning (deciding the block structure before any code).
- HDL coding of datapath and control logic (the RTL itself).
- Lint and clock-domain-crossing checks (catching coding errors before verification).
- Logic synthesis: compiling RTL into a gate-level netlist mapped to the target library, with timing/power/area (PPA) optimisation.
- AI-assisted RTL generation, completion, and debug (the newest sub-layer).

## Where it sits and why it matters
RTL is the productivity chokepoint of front-end design. Verification, the next step, routinely eats 50-70% of a project's engineering effort, and almost every bug it chases originates in RTL. So errors and inefficiency here cascade downstream into the most expensive part of the flow. This is exactly why the AI-for-design wave hit RTL and verification first: it is the highest-labour, highest-leverage point in the chain, and the place where a 10x productivity claim is most credible.

## Equipment market
"Equipment" here is software seats, not fab tools. The whole EDA market sits at roughly $16-19B in 2025 by independent counts, and the ESD Alliance/SEMI EDMD tracker (the KB's preferred tier-2 figure on **Eda Chip Design**) puts it near $21.7B annualised, growing ~10% YoY [1][4]. Front-end design (RTL authoring, synthesis, simulation, verification) is roughly a third of that, on the order of $5-7B, and front-end RTL is cited as the fastest-growing slice at ~9.35% CAGR through 2031, though that segment split comes from a report-mill source and should be treated as directional, not precise [2].

| Vendor | HQ | est. share (total EDA) | notable |
|---|---|---|---|
| Synopsys | US | ~31% | Synopsys.ai Copilot for generative RTL; DC/Fusion Compiler synthesis; absorbing Ansys ($35B, closed Jul 2025) |
| Cadence | US | ~30% | Joules RTL Design Studio, Cerebrus, JedAI; acquired ChipStack (Nov 2025), now ChipStack AI Super Agent |
| Siemens EDA | DE/US | ~13% | Tessent RTL Pro; design-for-test integration; part of Siemens DI |
| Smaller / open | mixed | remainder | Yosys and other open-source synthesis; point tools |

Concentration note: the Big Three take ~60-74% of all EDA revenue, and the concentration is even tighter in front-end where the synthesis-plus-verification flows are deeply coupled and switching is painful [3][4].

## Materials & consumables
There is no physical consumable at this step. The recurring spend is the licence itself: EDA is sold as time-based seat licences and increasingly as cloud/consumption subscriptions, which is what makes it ~90%+ recurring revenue for the vendors. The "consumables" analogue is therefore renewal and seat expansion as design teams grow, plus compute (front-end simulation and synthesis are CPU-hungry, pushing work to cloud EDA, a small but fast-growing sub-market). Standard-cell and IP libraries consumed during synthesis come from step 2 ([Semiconductor IP licensing (process step)](/semiconductor-process-flow/design/flow-ip-licensing-cores/)) and the foundry PDK, not from this step.

## Volumes, revenue, profitability
Volume is measured in engineering seats and tape-outs, not units. The revenue pool is the front-end share of EDA, roughly $5-7B of the ~$16-21B whole, with RTL/synthesis the densest part of front-end spend. The margin profile is software-grade and among the best in semiconductors: the Big Three run gross margins around 85-90% and operating margins in the 25-40% range depending on R&D intensity and acquisition load. The margin is earned by the seat-licence incumbents (Synopsys, Cadence, Siemens), not by the design teams using the tools, and that is the structural fact that governs value capture here.

## Market drivers, constraints & trends
Net read: the front-end pool grows faster than the EDA whole, because the AI-RTL layer adds a new consumption line on top of seat growth, and the served market is accelerating but cyclical-by-customer.

- **Drivers** — Custom-silicon proliferation is the demand engine: every hyperscaler and AI-chip startup (Cerebras, Groq, Tenstorrent) commissions purpose-built designs, each a fresh front-end project [11]. Cadence Q1 2026 core EDA grew 18% YoY and Synopsys design-automation revenue rose sharply on AI/HPC tape-outs at 2nm and below [12][13]. The AI-EDA sub-layer specifically is modelled at ~24% CAGR ($4.3B 2026 to ~$15.9B 2032), far above the ~9% whole-market rate [10]. Chiplet/multi-die designs multiply the number of RTL blocks and verification runs per system [11].
- **Constraints** — China is the sharpest: the May 2025 US export ban (rescinded six weeks later) showed how fast ~70% of China EDA revenue can be switched off, and re-imposition is a live tail risk [14]. Verification still eats 50-70% of effort, and the engineer pool is the binding capacity limit on design-starts. Big-Three concentration caps where new value accrues; thin AI-RTL co-pilots get absorbed, not scaled.
- **Trends & inflections to watch** — Natural-language-to-RTL is the structural shift, but functional correctness on VerilogEval still sits near 60%, below production trust [15]; tripwire: a vendor flow shipping NL-to-RTL with audited >85% functional correctness re-rates the productivity story. Agentic multi-tool orchestration is arriving (Siemens Fuse, March 2026; Cadence ChipStack) [11]; tripwire: a consumption/agent-priced tier disclosed as a distinct revenue line in any Big-Three 10-Q signals the model shift from seats to usage.

## Connections
- Cluster: [EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/)
- Thesis: **Eda Chip Design**
- Flow: [Semiconductor IP licensing (process step)](/semiconductor-process-flow/design/flow-ip-licensing-cores/) (prev) · [Functional verification & emulation (process step)](/semiconductor-process-flow/design/flow-functional-verification/) (next)