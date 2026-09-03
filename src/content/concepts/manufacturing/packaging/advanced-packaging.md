---
type: concept
slug: advanced-packaging
canonical_name: Advanced Packaging
aliases: []
kind: technology
parent_concepts:
- manufacturing
- packaging
related_concepts: []
sources:
- '[[2026-07-03-thats-a-learning-curve-mate-not-rsi]]'
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2026-04-14-the-photonic-foundry-fallacy]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2026-06-19-the-housefab-always-wins]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2026-04-24-state-of-the-future-friday-four-002]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
scorecard:
  viability: 4
  drivers: 4
  novelty: 3
  diffusion: 4
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 191
descendants:
- 3d-monolithic-integration
- heterogeneous-integration
- micro-transfer-printing
- osat
sources_7d: 2
sources_30d: 7
recent_mentions:
- slug: 2026-09-02-vertical-power-delivery-thermal-limits
  title: 'Vertical power delivery: the thermal limit at the 48V-to-point-of-load stage'
  date: '2026-09-02'
  kind: web
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-31-chips-act-equity-deals-us-gains-10-stake-in-intel-874m-for-s
  title: 'CHIPS Act Equity Deals: U.S. Gains 10% Stake in Intel, $874M for Seven Companies - News and Statistics - IndexBox'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-31-memory-optics-packaging-chips-act-targets-ais-compute-bottle
  title: 'Memory, optics, packaging: CHIPS Act targets AI''s compute bottleneck - Electronics360'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-31-tim-market-sizing-refresh
  title: TIM market sizing refresh — the definitional 2x split and the real addressable slot
  date: '2026-07-31'
  kind: web
- slug: 2026-07-30-commerce-dept-signs-874-million-in-chips-act-incentives-with
  title: Commerce Dept. Signs $874 Million in CHIPS Act Incentives With Seven Companies - Yahoo Finance
  date: '2026-07-30'
  kind: web
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-14-boschs-sic-fab-deal-adds-to-a-resurgence-in-chips-act-fundin
  title: Bosch's SiC fab deal adds to a resurgence in CHIPS Act funding - Electronics360
  date: '2026-07-14'
  kind: web
neighbors: []
---
**Advanced packaging is the set of techniques for wiring multiple dice together inside one package (2.5D interposers, 3D stacks, flip-chip, co-packaged optics) instead of shrinking one big die, and it has become the main lever for scaling AI compute now that monolithic scaling has stalled.**

## Summary

Advanced packaging covers everything that happens between the finished silicon die and the socket: bonding several dice side by side on a passive silicon interposer (2.5D), stacking active dice directly on top of one another with through-silicon vias (3D), flip-chip attachment of high-speed electrical interfaces to a photonic or electronic die, and co-packaging optics with the compute. The purpose is to build systems larger than the reticle limit while keeping yield tolerable, because a system assembled from small known-good dice loses less silicon to defects than one enormous die. The sources describe this as the standard route to "complex heterogeneous systems beyond the limits of monolithic scaling", and treat multi-chiplet GPUs and 2.5D FPGAs as existing device classes rather than proposals.

The physics that decides it is interconnect and heat. Crossing between dice costs more energy and latency than staying on one die, so inter-die connection density and latency constrain the architecture and force a bespoke routing design. In multi-chiplet GPUs, memory splits into local and remote HBM regions across the interposer, and remote traffic for a single matrix multiplication can vary by up to 58x depending on kernel and placement choices. Heat is the second constraint: a stack contains materials whose feature sizes span many orders of magnitude, and the back-end-of-line metallisation structures repeated billions of times across a stack are described as a near insurmountable hurdle for analysis at the speed a design flow needs. Power delivery follows: through-silicon via placement determines effective resistance and IR drop across a 3D stack.

The parameters that decide how far this goes are therefore not fabrication alone. They are: how small a chiplet can economically be, which today is bounded near 100 mm2 by the area overhead of electrostatic discharge protection and inter-chiplet signalling circuitry; how much interconnect bandwidth per unit footprint the package substrate can carry while still dissipating heat; whether design tools can predict thermal, power and routing behaviour early enough to be useful; and whether software can be made to respect the resulting non-uniform memory system.

A distinct branch is packaging as an enabler for non-silicon dice: a flip-chip platform delivering 13 high-speed and 32 low-speed signals to a thin-film lithium niobate photonic chip with bandwidth to 50 GHz, and architectures that assume co-packaged optics as a given.

## Viability (4/5)

The sources treat 2.5D and 3D integration as deployed technology. Die stacking "has enabled 2.5D FPGAs by integrating multiple active dice on a passive silicon interposer for improved yield and capacity", and multi-chiplet GPUs with local and remote HBM regions across an interposer are the baseline for optimisation work rather than a hypothesis. Flip-chip electrical interfacing to a centimetre-sized photonic die has been demonstrated with measured low bonding loss and low inter-channel crosstalk to 50 GHz, driving a working 2x8 switch and a 20 Gbit/s transmitter.

What is not yet solved is design-time prediction. Thermal analysis of stacks is described as facing a near insurmountable hurdle at the required speed and accuracy, with material properties deviating significantly from bulk values at these sizes; multi-die routing architecture questions are "unanswered" for lack of accurate modelling tools; power delivery network analysis needed a 5 to 6 order of magnitude GPU speedup over conventional direct solvers to be usable at early design stages. The technology works; the engineering discipline around it is being built in public, which is why the score is 4 and not 5.

**TLDR: In production for GPUs and FPGAs; the unresolved parts are analysis tooling and thermal headroom, not feasibility.**

## Drivers (4/5)

On demand, the sources are consistent: large language models drive the need for capacity and bandwidth that a single die cannot supply. Mixture-of-experts inference is bottlenecked by memory bandwidth for non-contiguous expert weights and by scatter-gather routing traffic, motivating a 3D heterogeneous multi-chiplet design mixing FeFET non-volatile and DRAM chiplets. Separately, "rising pressure on DRAM availability and contract pricing" from generative AI and hyperscale data centre expansion is cited as the motivation for radically different memory architectures built on co-packaged optics. The general framing is that packaging "provides abundant interconnection resources for 2.5D/3D heterogeneous integration, thereby enabling larger-scale VLSI systems with higher energy efficiency in data movement".

On supply, the enabling capabilities in evidence are silicon interposers (modelled at a 45 nm interposer node with 7 nm active dice), TSVs for 3D power and signal delivery, and flip-chip bonding platforms extending to non-silicon photonic substrates. The sources do not give capacity, cost or throughput figures for packaging lines, so the supply-side constraint that matters most commercially is not assessable here.

**TLDR: Demand is AI memory and compute scaling; supply is interposer, TSV and flip-chip capability plus a maturing tool layer.**

## Novelty (3/5)

The benefits over monolithic integration are stated qualitatively across the corpus: modularity, yield, capacity and performance. No source quantifies the yield or cost delta against a hypothetical single large die, so the central economic claim for advanced packaging is not evidenced here.

Where numbers exist, they are within-domain comparisons and they are substantial. A spoof-surface-plasmon-polariton interconnect on a 50 um oxide layer over silicon achieved 0.015 dB/cm insertion loss, a 10 dB crosstalk reduction within 5 GHz and 2.5x the bandwidth of a standard microstripline of the same footprint, with a fourfold temperature reduction relative to an FR4 substrate, in full-wave simulation. A chiplet-contiguous memory layout cut remote HBM traffic by 13.0x on Qwen 3 30B and 20.7x on Llama 3.1 70B GEMMs versus 4 KB interleaving, and by 3.3x and 3.7x over coarse locality-aware placement, without OS or hardware changes. A fibre delay-line memory concept claims elimination of redundant weight storage across 10,000 accelerators and over 70% lower weight-delivery energy than HBM3e, though this is a case-study evaluation, not hardware. Score of 3 reflects strong local results against a poorly quantified baseline.

**TLDR: Clear quantified gains within the packaging domain; the head-to-head advantage over monolithic dice is asserted rather than measured in these sources.**

## Diffusion (4/5)

Adoption at the top of the market is under way, which is why the barriers being written about are second-order. Four are visible in the sources. First, minimum economic chiplet size: conventional ESD protection and inter-chiplet signalling impose area overhead identified as a major constraint on reducing chiplet size below 100 mm2, though SPICE and parasitic-extraction analysis suggests both can be substantially simplified in future 2.5D/3D packaging, which would improve composability and reusability of small chiplets. Second, tooling: multi-die routing architecture questions remain open because accurate versatile models did not exist until open-source CAD tools were extended for the purpose, and thermal and PDN analysis both required new methods to become tractable.

Third, software: the non-uniform memory system created by packaging is exposed to the programmer, and optimal placement granularity varies widely across workloads, making locality-aware placement incompatible with fixed page-granularity interleaving until the layout is redesigned. Fourth, security: a communication-oriented chiplet with an antenna or contactless coupling structure can be repurposed as an internal observation platform, and captured signals were experimentally shown to correlate with the activity of a neighbouring victim chiplet. This is a genuine new attack surface for multi-vendor chiplet supply chains, and the sources give no evidence of countermeasures yet.

**TLDR: Already diffusing in high-end GPUs and FPGAs; the residual barriers are EDA tooling, chiplet-level I/O overhead, software locality and a new security surface.**

## Impact (4/5)

If packaging continues to scale, the sources point to three compounding effects: larger-scale VLSI systems with better data-movement energy efficiency; heterogeneous memory hierarchies that mix technologies within one stack, such as FeFET non-volatile and DRAM chiplets tuned separately to attention and expert routing; and integration of entirely different material systems, with flip-chip packaging serving as the missing electrical interface for thin-film lithium niobate photonics that then delivers sub-34 ps switching and 50 GHz electro-optic comb generation.

The most consequential claim, that packaging plus co-packaged optics could displace part of the DRAM hierarchy under current pricing pressure, is a proposal with a case-study evaluation rather than a result. Scoring 4 rather than 5 reflects that the sources demonstrate impact on component metrics and architectural options, not on delivered system-level cost or performance in the field.

**TLDR: It is the substrate for continued AI hardware scaling and for integrating photonics and novel memory; the value is large but the sources quantify it only in fragments.**

## Timing Now (0-2yr)

2.5D interposer FPGAs and multi-chiplet GPUs are treated throughout as existing hardware to be modelled and optimised, not as future devices. Software-side gains are available immediately because they need no OS or hardware change.

The items with a longer fuse are those framed as future or prospective by their own authors: simplified ESD and signalling in "future 2.5D/3D packaging technologies" enabling sub-100 mm2 chiplets, metastructure interconnects still at full-wave simulation stage, and optical delay-line memory at case-study stage. Expect the interesting commercial questions over the next two years to be about tools, thermal budgets and chiplet interface standards rather than about whether packaging works.

**TLDR: The packaging itself is shipping; the tooling, chiplet miniaturisation and security responses are the 2 to 5 year work.**

## Overrated or underrated? Fairly rated

The headline direction is not in dispute and is already priced in: monolithic scaling has run out of room, and 2.5D/3D integration is how large systems get built. Treating advanced packaging as an emerging bet would be a misreading of this evidence base.

The underrated part is the supporting layer. Three separate 2026 papers exist because standard analysis was too slow or too inaccurate to use: multiscale thermal modelling of BEOL structures replicated billions of times, effective-resistance analysis for TSV planning needing a 5 to 6 order of magnitude speedup to fit an early-stage flow, and multi-die routing architecture exploration that required extending open-source CAD before the questions could even be posed. Add the software layer, where a layout change alone bought a 20.7x reduction in remote HBM traffic, and the cross-chiplet side-channel surface, which is demonstrated but unaddressed. Value is migrating from the bonding step to thermal, power, interface and security co-design.

## Prediction

By December 2028, locality-aware cross-chiplet data placement of the kind that cut remote HBM traffic by 13.0x to 20.7x in will be a documented, user-visible feature of at least one mainstream GPU or accelerator software stack rather than a research prototype.

## Evidence base

- 2026-06-15: 2.5D FPGAs already integrate multiple active dice on a passive silicon interposer for yield and capacity, but inter-die connection density and latency force a bespoke routing architecture, modelled by HSPICE at a 7 nm node with a 45 nm interposer 
- 2026-06-15: remote HBM traffic for a fixed GEMM varies by up to 58x across the multi-chiplet design space, and a 2D block-swizzle CTA traversal cut remote traffic by up to 5.1x over the best 1D traversal 
- 2026-06-15: a chiplet-contiguous global memory layout reduced remote HBM traffic by 13.0x on Qwen 3 30B and 20.7x on Llama 3.1 70B GEMMs versus 4 KB interleaving, with no OS or hardware changes 
- 2026-06-05: ESD protection and inter-chiplet signalling area overhead is a major constraint on reducing chiplet size below 100 mm2, and SPICE plus parasitic extraction indicates both can be substantially simplified in future 2.5D/3D packaging 
- 2026-06-16: a flip-chip platform delivered 13 high-speed and 32 low-speed signals to a centimetre-sized thin-film lithium niobate chip with low bonding loss and crosstalk to 50 GHz, enabling a 2x8 switch at ~3 dB insertion loss, under -20 dB crosstalk and switching under 34 ps 
- 2026-05-08: signals captured through a communication-oriented chiplet's antenna or contactless coupling interface were experimentally shown to correlate with the activity of a neighbouring victim chiplet in the same package or stack 
- 2026-07-08: GPU-accelerated effective-resistance analysis for 3D IC power delivery networks achieved a 5 to 6 order of magnitude speedup over a conventional direct solver with negligible error, making early-stage TSV planning tractable 

## Open questions

- Can the ESD and inter-chiplet signalling simplifications proposed in survive real reliability qualification, and does chiplet area genuinely fall below 100 mm2 as a result?
- What is the thermal ceiling on 3D logic-on-logic stacks once the multiscale effects described in are accounted for, as opposed to bulk-property estimates?
- Does the cross-chiplet side-channel leakage demonstrated in force shielding, isolation or certification requirements on multi-vendor chiplet marketplaces, and at what area and cost penalty?
- Do simulated interconnect gains such as the 2.5x bandwidth and fourfold thermal improvement of the spoof-plasmonic structure survive fabrication at package scale?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
