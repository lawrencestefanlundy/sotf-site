---
type: concept
slug: printed-circuit-board
canonical_name: Printed Circuit Board
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2026-06-13-sovereign-electronics-manufacturing-the-achilles-heel-of]]'
- '[[2024-01-23-normal-computing-first-thermodynamic-computer]]'
- '[[2025-04-15-nature-comm-thermodynamic-computing-system]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 14
frontier:
- Does the EDIP earmark translate into measurable new European bare-board capacity, or does environmental permitting keep the 2.3% share flat?
- Can the data-scarcity problem in PCB design automation be solved without proprietary vendor datasets, given that PCB-QA currently spans only 8 open-source projects and 480 question-answer pairs?
- Do board-based reconfigurable surfaces at around 100 GHz survive the move from bond-wired bare-die proof of concept to manufacturable panels, or does switch integration force a semiconductor process?
- How expensive is mitigation of reflective backscatter leakage from PCB traces, in shielding cost or layout constraint, once the NSF ReBac work quantifies the channel?
- Can PCB-based reconfigurable surfaces retain the 100 GHz wideband performance demonstrated at prototype scale once switch parasitics and control routing are scaled to full apertures 2026 06 05 a 100 ghz wideband reconfigurable intelligent surface based ?
- Do buffer-parameterised surrogate models generalise to IC buffer technologies outside their training distribution without retraining, and with what error on eye height and eye width 2026 06 05 buffer parameterized machine learning surrogate models for c?
- What electron lifetime and coherence can monolithic PCB Paul traps reach, and does the 2.13 ms lifetime limit stem from board materials, vacuum or RF heating 2026 07 22 monolithic printed circuit board rf trap for electrons?
- What accuracy do current language models achieve on PCB-QA, and which design-file representations (schematic, netlist, layout, SPICE output) are the binding constraint 2026 06 24 pcb qa evaluating llms over the first printed circuit board ?
- At what distance and through what enclosure materials does reflective backscatter recovery of user activity remain reliable, and which PCB layout countermeasures suppress it 2026 07 27 nsf 2555491 collaborative research satc 20 res model?
scorecard:
  viability: 4
  drivers: 3
  novelty: 2
  diffusion: 5
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-13-sovereign-electronics-manufacturing-the-achilles-heel-of
  title: The Achilles' heel of European defence—printed circuit board. Why environmental regulations are strangling PCB production in EU
  date: '2026-06-13'
  kind: web
- slug: 2025-04-15-nature-comm-thermodynamic-computing-system
  title: Thermodynamic computing system for AI applications
  date: '2025-04-15'
  kind: web
- slug: 2024-01-23-normal-computing-first-thermodynamic-computer
  title: Normal Computing Unveils the First-ever Thermodynamic Computer
  date: '2024-01-23'
  kind: web
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
neighbors: []
---
**The printed circuit board is the laminated, etched-copper substrate that mechanically holds and electrically interconnects almost every electronic component ever shipped, and its current interest lies less in the substrate itself than in three live pressures: how far its cheap lithography can be pushed (100 GHz surfaces, trapped-electron qubits), how badly its design tooling lags integrated-circuit EDA, and how concentrated its manufacturing has become outside Europe.**

## Summary

A printed circuit board is a rigid insulating laminate carrying patterned copper layers. Components are soldered to pads; signals travel along etched traces and through plated vias between layers. The manufacturing process is subtractive photolithography at a coarse resolution compared with semiconductor fabrication, which is exactly why it is cheap and why it is the default substrate for anything that is not a chip. The parameters that decide what a PCB can do are layer count, minimum trace and gap width, dielectric loss at the operating frequency, and the tolerance stack of drilling and lamination.

The sources here use PCBs in two distinct ways. First, as a low-cost fabrication platform for physics that previously needed custom processes: a peer-reviewed continuous-variable thermodynamic computer built from RLC unit cells on a board and run as a parallelised Langevin sampler <sup class="ref"><a href="https://www.nature.com/articles/s41467-025-59011-x" title="Thermodynamic computing system for AI applications" rel="noopener">ref</a></sup>; a radio-frequency higher-order topological metasurface of split-ring resonators demonstrated at 1.5 to 1.7 GHz explicitly to avoid "expensive processing techniques"; a monolithic single-board Paul trap for electrons requiring no assembly, with observed trapped lifetimes of 2.13 ms and secular frequencies up to 90 MHz; and a reconfigurable intelligent surface operating around 100 GHz, where the authors list fabrication limits, switch size relative to unit cell, switch parasitics and control complexity as the binding constraints.

Second, as a design and manufacturing problem in its own right. Signal integrity analysis on board interconnects is now hard enough that machine-learning surrogates are being built to predict eye height and eye width across buffer technologies over interconnects with 44 design parameters. Generative AI has been applied heavily to integrated-circuit design automation but thinly to boards, with domain-specific data scarcity and poor integration with existing PCB tools identified as the blockers. The first text-based PCB question-answer benchmark, 480 pairs derived from 8 open-source hardware projects, appeared in mid-2026 pcb qa evaluating llms over the first printed circuit board.

The third pressure is industrial. Europe's share of global bare-board PCB production is reported to have fallen from 16% in 2000 to roughly 2.3% in 2022, with environmental and regulatory barriers cited as constraints on rebuilding domestic capacity, making boards a chokepoint for defence electronics <sup class="ref"><a href="https://tstronic.eu/en/the-achilles-heel-of-european-defence-printed-circuit-board-why-environmental-regulations-are-strangling-pcb-production-in-eu-and-how-to-secure-electronics-assembly" title="The Achilles' heel of European defence—printed circuit board. Why environmental regulations are strangling PCB productio" rel="noopener">ref</a></sup>. Boards are also now a documented attack surface: illuminating a device with a low-power radio signal allows an eavesdropper to read backscatter from internal cables and PCB traces and infer user activity, a class of vulnerability the NSF began funding work on in July 2026.

## Viability (4/5)

Nothing in the sources casts doubt on PCBs as a working manufacturing technology. What the sources do establish is where the ceiling sits. Normal Computing's board-level stochastic processing unit reached peer review in Nature Communications with RLC unit cells acting as a parallelised Langevin sampler <sup class="ref"><a href="https://www.nature.com/articles/s41467-025-59011-x" title="Thermodynamic computing system for AI applications" rel="noopener">ref</a></sup>, but the PCB form was acknowledged at the time of the 8-cell prototype as not scalable because of component size, and the programme moved to silicon <sup class="ref"><a href="https://www.businesswire.com/news/home/20240123141100/en/Normal-Computing-Unveils-the-First-ever-Thermodynamic-Computer" title="Normal Computing Unveils the First-ever Thermodynamic Computer" rel="noopener">ref</a></sup>. That is the pattern: boards get you a credible physical demonstration fast, then you leave.

At high frequency the limits are explicit. The 100 GHz reconfigurable surface required orthogonal-polarisation slot-coupled patches and subarray partitioning specifically to work around fabrication limits, switch parasitics and the fact that available switches are large relative to the unit cell, with bare-die AlGaAs switches attached by optimised bond wires. Beyond-diagonal RIS designs need multi-layer boards for their interconnections, and a graph-theoretic paper exists precisely to identify which architectures can be squeezed onto double-layer PCBs. The trapped-electron board trap works but at 2.13 ms lifetimes, which is a characterisation result, not a qubit platform. The score reflects proven-but-bounded: mature below roughly 100 GHz and above roughly 100 micron features, demonstration-grade at the edges.

**TLDR: The substrate is beyond question; the frontier extensions in these sources are working but single-demonstration and near their physical ceiling.**

## Drivers (3/5)

On demand, the sources show pull from several directions at once: sub-terahertz 6G coverage surfaces that need a low-cost, scalable substrate, ultra-low-power multimodal sensing platforms under sub-100 mW budgets thinking fast thinking slow adaptive multimodal transformer, research groups seeking cheap GHz-range photonic platforms, and rising signal-integrity complexity in ordinary product design. None of these is a step change in volume; they are incremental additions to an already vast base.

On supply, the one sharp driver documented is European industrial policy. The collapse from 16% of global bare-board output in 2000 to about 2.3% in 2022, with regulatory barriers cited as a constraint on domestic capacity growth, is framed as a defence vulnerability, and an EU PCB earmark under EDIP resolved as of 23 June 2026 <sup class="ref"><a href="https://tstronic.eu/en/the-achilles-heel-of-european-defence-printed-circuit-board-why-environmental-regulations-are-strangling-pcb-production-in-eu-and-how-to-secure-electronics-assembly" title="The Achilles' heel of European defence—printed circuit board. Why environmental regulations are strangling PCB productio" rel="noopener">ref</a></sup>. That is a policy driver rather than a market one, and the source is a single low-tier industry piece. There is also a nascent driver on the tooling side, where a survey identifies board design automation as the neglected half of hardware GenAI. Whether either converts into capital deployment is not shown by these sources.

**TLDR: Demand is broad and dull; the sharp driver is defence sovereignty in Europe, and the sources are thin on the supply response.**

## Novelty (2/5)

Judged as a technology, a PCB is not new and none of the sources claim it is. The defensible novelty claims are substitutional. The topological metasurface work argues that PCB technology replaces expensive processing techniques and restricted material parameters for radio-frequency photonic higher-order topological insulators, at 1.5 to 1.7 GHz. The electron trap replaces assembled Paul-trap electrode structures with a single board, eliminating assembly steps and the associated tolerance errors. The 100 GHz surface argues PCB is attractive against custom semiconductor fabrication on cost and scalability grounds even at sub-terahertz frequencies. In each case the delta is cost and turnaround rather than performance, and the sources do not quantify it.

The genuinely new thing in this evidence set is not the board but the tooling layer above it. PCB-QA is described as the first PCB design question-answer dataset, 480 pairs from 8 open-source hardware projects, and it is being used to test whether models can read schematics and netlists in native forms such as graphical PDFs and KiCAD files at all. That is a first-benchmark stage of maturity, comparable to where IC design automation stood before, and it is worth contrasting with the packaging layer above, where chiplet approaches took a decade from the 2011 Virtex-7 to a $3 billion market in 2021, just 0.5% of a $600 billion semiconductor total <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e13-chiplets-how-chip-lego-is-driving" title="🔮 E13: Chiplets - How Chip Lego is Driving AI Progress " rel="noopener">ref</a></sup>.

**TLDR: The substrate is decades-old commodity; the novelty is in what it displaces, namely bespoke microfabrication and manual assembly.**

## Diffusion (5/5)

The sources treat PCBs as the default. The NSF backscatter side-channel awards justify their scope on the basis that billions of consumer and industrial products share the same internal cabling and trace structures. Researchers in unrelated fields reach for boards without argument, from thermodynamic samplers <sup class="ref"><a href="https://www.nature.com/articles/s41467-025-59011-x" title="Thermodynamic computing system for AI applications" rel="noopener">ref</a></sup> to metasurfaces to quantum traps. No adoption barrier exists for the substrate itself.

The real diffusion barriers sit adjacent. For automated design, the survey names domain-specific data scarcity and limited integration with existing PCB tools as the blockers, and the benchmark work shows that models must contend with heterogeneous native file formats rather than a single canonical text representation. For manufacturing, the barrier is regulatory and capital-intensity in Europe, where environmental regulation is described as constraining domestic capacity growth <sup class="ref"><a href="https://tstronic.eu/en/the-achilles-heel-of-european-defence-printed-circuit-board-why-environmental-regulations-are-strangling-pcb-production-in-eu-and-how-to-secure-electronics-assembly" title="The Achilles' heel of European defence—printed circuit board. Why environmental regulations are strangling PCB productio" rel="noopener">ref</a></sup>. Board designs also diffuse unevenly at the frontier: BD-RIS architectures that need many interconnections push into multi-layer stack-ups that increase fabrication difficulty, which is why the planar double-layer subset is being characterised separately.

**TLDR: Already universal; the diffusion question is not the board but the tooling and the geography of supply.**

## Impact (4/5)

Because the technology is already everywhere, the interesting impact is at the margins rather than in adoption. Supply security is the largest of them: if bare-board production is a chokepoint for defence electronics and one region holds roughly 2.3% of global output, then board capacity is a strategic variable rather than a procurement line item <sup class="ref"><a href="https://tstronic.eu/en/the-achilles-heel-of-european-defence-printed-circuit-board-why-environmental-regulations-are-strangling-pcb-production-in-eu-and-how-to-secure-electronics-assembly" title="The Achilles' heel of European defence—printed circuit board. Why environmental regulations are strangling PCB productio" rel="noopener">ref</a></sup>. Design cost is the second: signal integrity work currently requires costly data generation and retraining for every buffer technology shift, and surrogate models that generalise across technologies would cut that directly. Automating layout and validation is a large addressable cost given how much of hardware development it consumes.

The third is negative impact and it is broad. If PCB traces and internal cables leak keystroke-level information to a remote radio interrogator through walls and without line of sight, the design assumption that an enclosure protects internal signalling fails across an installed base of billions of devices, which is why two coordinated NSF awards of roughly $300,000 each were made in July 2026 to model and mitigate it. Against that, the enabling impact for exotic hardware is real but modest: boards accelerate research demonstrations, and at least one documented programme then left the board behind for silicon <sup class="ref"><a href="https://www.businesswire.com/news/home/20240123141100/en/Normal-Computing-Unveils-the-First-ever-Thermodynamic-Computer" title="Normal Computing Unveils the First-ever Thermodynamic Computer" rel="noopener">ref</a></sup>.

**TLDR: High but largely incumbent value; the marginal impact is in supply security, design cost and a newly exposed attack surface.**

## Timing Now (0-2yr)

There is no future arrival date for PCBs. The three live questions are all current. Industrial policy has already moved, with an EU earmark for PCBs resolving under EDIP by 23 June 2026 <sup class="ref"><a href="https://tstronic.eu/en/the-achilles-heel-of-european-defence-printed-circuit-board-why-environmental-regulations-are-strangling-pcb-production-in-eu-and-how-to-secure-electronics-assembly" title="The Achilles' heel of European defence—printed circuit board. Why environmental regulations are strangling PCB productio" rel="noopener">ref</a></sup>. Security research on trace backscatter started with awards dated 25 July 2026. Design-automation benchmarking began in mid-2026 with the first dataset of its kind.

The frontier applications are on longer clocks and the sources do not date them. A 100 GHz board-based surface exists as a proof of concept with bond-wired bare-die switches, and a board electron trap holds electrons for milliseconds; neither is a product timeline. Treat the substrate as Now and the frontier uses as unclear.

**TLDR: The substrate is deployed at scale today; every open question in these sources is being contested in 2026, not in the 2030s.**

## Overrated or underrated? Underrated

Underrated, but for unglamorous reasons. Attention and capital in hardware automation have gone to integrated circuits and hardware description languages, while the board layer, which every one of those chips must sit on, has only just acquired its first evaluation dataset and a survey enumerating why models cannot yet read its file formats. That is an unusually large gap between economic footprint and tooling investment. The same neglect shows up industrially: a fall from 16% to roughly 2.3% of global bare-board output over two decades happened without much strategic notice until defence procurement forced the issue <sup class="ref"><a href="https://tstronic.eu/en/the-achilles-heel-of-european-defence-printed-circuit-board-why-environmental-regulations-are-strangling-pcb-production-in-eu-and-how-to-secure-electronics-assembly" title="The Achilles' heel of European defence—printed circuit board. Why environmental regulations are strangling PCB productio" rel="noopener">ref</a></sup>.

The caution is against over-reading the frontier demonstrations. Boards are a fast route to a publishable physical prototype, and researchers use them for that reason, but the thermodynamic computing case shows the standard trajectory: board prototype for the peer-reviewed system paper, silicon for anything that has to scale <sup class="ref"><a href="https://www.nature.com/articles/s41467-025-59011-x" title="Thermodynamic computing system for AI applications" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.businesswire.com/news/home/20240123141100/en/Normal-Computing-Unveils-the-First-ever-Thermodynamic-Computer" title="Normal Computing Unveils the First-ever Thermodynamic Computer" rel="noopener">ref</a></sup>. Do not confuse the value of PCB as a research instrument with the value of PCB as an end platform for high-frequency or quantum systems. The investable propositions here are capacity, tooling and test, not exotic physics on FR-4.

## Prediction

By 31 December 2027, published figures for Europe's share of global bare-board PCB production will still be below 5%, despite the EU earmark for PCBs that resolved under EDIP on 23 June 2026.

## Evidence base

- Europe's share of global bare-board PCB production is reported to have fallen from 16% in 2000 to roughly 2.3% in 2022, with regulatory barriers constraining capacity growth; an EU PCB earmark resolved under EDIP on 23 June 2026 <sup class="ref"><a href="https://tstronic.eu/en/the-achilles-heel-of-european-defence-printed-circuit-board-why-environmental-regulations-are-strangling-pcb-production-in-eu-and-how-to-secure-electronics-assembly" title="The Achilles' heel of European defence—printed circuit board. Why environmental regulations are strangling PCB productio" rel="noopener">ref</a></sup>.
- A continuous-variable thermodynamic computer built from RLC unit cells on a printed circuit board, run as a parallelised Langevin sampler, was published in Nature Communications on 15 April 2025; the board form was pre-silicon and acknowledged as unscalable at the 8-cell prototype stage in January 2024 <sup class="ref"><a href="https://www.nature.com/articles/s41467-025-59011-x" title="Thermodynamic computing system for AI applications" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.businesswire.com/news/home/20240123141100/en/Normal-Computing-Unveils-the-First-ever-Thermodynamic-Computer" title="Normal Computing Unveils the First-ever Thermodynamic Computer" rel="noopener">ref</a></sup>.
- A wideband PCB-based reconfigurable intelligent surface operating around 100 GHz was demonstrated using AlGaAs SP3T bare-die switches and optimised bond-wire interconnections, with fabrication limits, switch size and parasitics named as the binding constraints (published 24 May 2026).
- A monolithic single-board RF Paul trap for electrons, requiring no assembly, achieved trapped-electron lifetimes of 2.13 ms and secular frequencies up to 90 MHz (22 July 2026).
- PCB-QA, described as the first PCB design question-answer dataset, comprises 480 manually created question-answer pairs from 8 open-source hardware projects and tests whether LLMs can read schematics and netlists in native formats (24 June 2026).
- Two coordinated NSF SaTC awards of $299,999 and $300,000, dated 25 July 2026, fund modelling and mitigation of reflective backscatter side channels in which a remote low-power radio can recover typing from reflections off internal cables and PCB traces, through walls and without line of sight.

## Open questions

- Does the EDIP earmark translate into measurable new European bare-board capacity, or does environmental permitting keep the 2.3% share flat?
- Can the data-scarcity problem in PCB design automation be solved without proprietary vendor datasets, given that PCB-QA currently spans only 8 open-source projects and 480 question-answer pairs?
- Do board-based reconfigurable surfaces at around 100 GHz survive the move from bond-wired bare-die proof of concept to manufacturable panels, or does switch integration force a semiconductor process?
- How expensive is mitigation of reflective backscatter leakage from PCB traces, in shielding cost or layout constraint, once the NSF ReBac work quantifies the channel?

---
*Assessment drafted 2026-08-31 from up to 14 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
