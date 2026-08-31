---
type: concept
slug: silicon-spin-qubits
canonical_name: Silicon Spin Qubits (Intel, Quantum Motion)
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
related_concepts: []
sources:
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
frontier:
- What two-qubit gate fidelity is achieved on 300 mm foundry-fabricated devices, and how does it vary across dies and wafers rather than within a single hero device?
- Do the noise-suppression techniques that delivered single-qubit fidelity above 99.6% under a strong field gradient extend to exchange-based two-qubit gates at the same overhead?
- Does coherent electron shuttling remain viable as the connectivity layer once the real two-level-fluctuator density along long channels is mapped?
- In the cross-platform energy efficiency framework, where do silicon spin qubits actually land relative to superconducting, trapped-ion, neutral-atom and photonic systems?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 13
last_reorg_date: '2026-05-13'
scorecard:
  viability: 2
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Later (5-10yr)
  verdict: Too early to say
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2024-12-04-cubits-in-a-fridge-why-is-nobody
  title: Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)
  date: '2024-12-04'
  kind: substack
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
neighbors: []
---
**Silicon spin qubits encode quantum information in single electron spins held in gate-defined quantum dots on silicon chips, betting that CMOS foundry manufacturing beats every other qubit platform on scaling; foundry-made devices have now reached coherent operation of eight qubits, with two-qubit gate fidelity and device-to-device variability the unresolved blockers.**

## Summary

A silicon spin qubit is a single electron (or hole) trapped in an electrostatically defined quantum dot in a silicon device, with the two spin states serving as the computational basis. Dots are formed and tuned by metal gates on top of a silicon channel, exactly the structure of a MOSFET: the 2026 eight-qubit demonstration describes an eight-dot linear array tuned as four double-dot pairs, fabricated in a 300 mm CMOS-compatible foundry process. Two-qubit gates come from the exchange interaction between neighbouring dots, controlled by the voltage on the barrier gate between them. Readout is done by charge sensing; the eight-qubit device used a cascaded charge-sensing protocol to measure the central four qubits.

The platform's appeal is twofold. First, coherence: isotopically purified, nuclear-spin-free silicon is intrinsically favourable for electron spin qubits, and the foundry device showed Ramsey dephasing times up to 41(2) microseconds and Hahn-echo coherence up to 1.31(4) milliseconds. Second, manufacturability: the claim throughout the literature is that spin qubits can leverage the existing semiconductor infrastructure rather than build a new one.

The parameters that decide the technology are all noise and uniformity parameters. Charge noise, widely attributed to individual two-level fluctuators in the oxide and interfaces, is the dominant performance limit; under a strong magnetic field gradient it is transduced into magnetic noise and destabilises qubit operation on timescales comparable to data acquisition. Uniformity is the second axis: three-dimensional device simulation of nanosheet double dots finds that millivolt-level bias variation on plunger and middle barrier gates is enough to push two-qubit gate fidelity below 99%. Because nearest-neighbour exchange only connects adjacent dots, architectures add coherent electron shuttling to move spins between distant patches, as in the shuttling-based SpinBus design and hybrid shuttling-connected patch layouts studied for magic-state distillation.

## Viability (2/5)

The blockers are named explicitly in the same literature. Low two-qubit entangling gate fidelity is described as the key barrier to large-scale integration, and simulation shows millivolt-scale gate-bias variation is sufficient to drop fidelity below the 99% threshold commonly targeted for fault tolerance. Charge noise from two-level fluctuators remains the dominant limit and the fluctuator landscape of a given device is currently unmapped. Compilation work also treats high sensitivity to static defects as a first-order architectural constraint. Eight physical qubits with an unresolved entangling-gate fidelity problem is early evidence with serious obstacles, not a credible near-term machine.

**TLDR: Coherence and foundry fabrication are demonstrated at eight qubits; two-qubit gate fidelity under realistic variability is not.**

## Drivers (3/5)

Supply side, the driver is explicit and repeated: silicon spin qubits are pursued because they can fully leverage the well-developed semiconductor infrastructure, and the 2026 result was executed in a 300 mm CMOS-compatible foundry process rather than a university cleanroom. A second, weaker supply-side driver is energy: spin qubits are one of five platforms analysed in a 2026 framework for benchmarking quantum computer energy efficiency, which suggests energy per algorithm is becoming a comparison axis, though the excerpt does not give the platform's ranking. A third driver is the arrival of design and simulation tooling: 3D Poisson/Schroedinger plus many-body device simulation for gate design, hardware-tailored resource estimation and defect-aware compilation.

Demand side, the supplied sources contain no market, procurement, funding or customer data for this platform, so no assessment of pull is possible from them. The one 2024 commentary source observes only that quantum computers in general remain largely confined to research labs and early pilot programmes <sup class="ref"><a href="https://stateofthefuture.substack.com/p/cubits-in-a-fridge-why-is-nobody" title="Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)" rel="noopener">ref</a></sup>. The score reflects documented supply-side motivation only.

**TLDR: Supply-side driver is strong and well documented (existing CMOS fabs); the sources say essentially nothing about demand.**

## Novelty (3/5)

What silicon spin qubits are better than, on the sources' own account, is every platform that requires bespoke fabrication: the pitch is high coherence, controllability and CMOS manufacturability in one package. Millisecond Hahn-echo coherence in a foundry-fabricated device is a real datum, not a projection. There is also methodological novelty within the platform: using a single shuttled electron as a scanning probe to localise individual two-level fluctuators along a channel, with no extra hardware and better scaling than earlier defect-localisation methods.

The 'by how much' cannot be answered from these sources. The energy efficiency study compares superconducting qubits, silicon spin qubits, trapped ions, neutral atoms and photonic qubits within a single framework, but the available excerpt gives no per-platform numbers. No source here provides a qubit-count, fidelity or logical-error comparison between silicon spin qubits and the competing platforms, so the comparative advantage remains asserted rather than measured. Anyone underwriting the platform on 'it will scale like CMOS' is currently buying an argument, not a demonstrated crossover.

**TLDR: Genuinely different on footprint, coherence and manufacturability, but the sources contain no head-to-head comparison against rival platforms.**

## Diffusion (2/5)

Two adoption barriers dominate. The first is uniformity and yield. If millivolt-level bias variation on plunger and barrier gates can drive two-qubit fidelity below 99%, then the value of foundry fabrication depends entirely on process control that the supplied sources do not quantify at wafer scale. The second is defects. Compilation frameworks for error-corrected spin qubit architectures explicitly build in defect-handling and initial-mapping strategies because of high sensitivity to static defects, using a 2D surface code with qubit teleportation and comparing shortest-path against rotation-based routing, with shortest-path better in sparse low-defect settings. That is a stack designed around an expectation of dead qubits.

The encouraging diffusion signal is that the surrounding ecosystem is arriving before the hardware: resource estimation tied to a silicon-processor Hamiltonian with realistic parameters and 1/f non-Markovian noise, covering surface, colour and biased codes and 5-to-1 and 15-to-1 distillation, propagated to system-level overheads for spin dynamics, integer factorisation and quantum chemistry; commercial-grade device TCAD; and practical calibration routes for defect-aware operation. Tooling readiness does not compensate for eight qubits, hence the low score.

**TLDR: The software and architecture stack is being built, but device variability and static defects mean yield, not physics, decides adoption.**

## Impact (4/5)

The upside case is not incremental. Resource estimation for this platform is already framed against integer factorisation, quantum chemistry and spin dynamics, with logical-fidelity targets translated back into hardware performance constraints. A qubit that is fabricated on a 300 mm CMOS line and can leverage the existing semiconductor supply chain would change the capital structure of building a fault-tolerant machine, not just its specification. Energy consumption per algorithm is also becoming a competitive dimension, and spin qubits are treated as a serious contender in that framing.

Two qualifications. First, most of the value is generic to fault-tolerant quantum computing rather than specific to silicon; the platform captures it only if it wins or co-wins. Second, the sources give no market sizing, cost figures or customer commitments, so the magnitude of value is inferred from the applications named in the resource-estimation work rather than measured. The score reflects the size of the prize conditional on the physics and yield problems being solved, which the viability score prices separately.

**TLDR: If the manufacturability thesis holds, this is a route to fault-tolerant quantum computing on existing fab capacity; the applications named are large ones.**

## Timing Later (5-10yr)

The state of the art in the supplied sources, as of mid-2026, is coherent control of eight foundry-fabricated qubits with readout on the central four and single-qubit gates above 99.6% under adaptive control. The two-qubit gate is not yet reliably above the 99% threshold once realistic process and bias variation are included, and the magic-state and code overheads that stand between physical and logical qubits are being estimated rather than measured.

Nothing in these sources supplies a vendor roadmap or a dated milestone, so the band is a trajectory judgement with low confidence. Near-term (0-2 years) the observable outputs will be larger tuned arrays, two-qubit fidelity numbers on foundry devices, and defect maps of real channels. Anything resembling an error-corrected logical qubit on this platform sits beyond that, and if uniformity across a wafer turns out to be the binding constraint it could sit well beyond ten years.

**TLDR: Eight-qubit foundry devices exist now; useful error-corrected operation is many orders of magnitude of qubit count and one fidelity threshold away.**

## Overrated or underrated? Too early to say

The core claim, that silicon spin qubits inherit CMOS scaling, is now partially tested rather than purely rhetorical: the devices are being made in a 300 mm foundry process and eight of them work together with millisecond echo coherence. That is a meaningful step and it distinguishes this platform from a lab curiosity. But the decisive number, two-qubit gate fidelity in a manufactured device across a population of devices, is absent from these sources, while simulation says the tolerance is millivolts. Until that number is published for foundry-made arrays, both bull and bear cases are underdetermined.

My working position: the platform is behind on demonstrated scale and is compensating with a manufacturability argument whose payoff arrives only after uniformity is proven. The healthiest sign is that the community is attacking the right problem rather than the easy one, mapping individual charge defects, suppressing transduced noise in closed loop, and designing compilers that assume defective qubits. Judge it again when a foundry lot, not a hero device, reports two-qubit fidelities.

## Prediction

By 31 December 2027, no publication will report coherent operation of more than 32 silicon spin qubits on a single foundry-fabricated 300 mm device, measured against the eight-qubit state of the art of June 2026.

## Evidence base

- 2 June 2026: an eight-dot linear array made in a 300 mm CMOS-compatible foundry process was fully tuned and coherently controlled, with T2* up to 41(2) microseconds and Hahn-echo T2 up to 1.31(4) ms, and readout of the central four qubits via cascaded charge sensing.
- 27 July 2026: open- and closed-loop suppression of transduced charge noise gave more than a twofold improvement in inhomogeneous coherence time, a tenfold improvement in Rabi oscillation quality and single-qubit gate fidelity above 99.6% under a strong decoherence field gradient.
- 2 July 2026: 3D device simulation of nanosheet-based double quantum dots found millivolt-level bias variation on plunger and middle barrier gates reduces two-qubit gate fidelity below the 99% threshold, with low two-qubit fidelity named as the key barrier to large-scale integration.
- 29 May 2026: hardware-tailored resource estimation built a silicon-processor noise model with realistic parameters and 1/f non-Markovian noise, comparing SpinBus shuttling, dense nearest-neighbour and hybrid architectures, surface, colour and biased codes, and 5-to-1 and 15-to-1 magic-state distillation for factoring and chemistry workloads.
- 27 July 2026: charge noise from two-level fluctuators is identified as the dominant performance limit, with fluctuator locations generally unknown; shuttling a single spin over varying distances is proposed as a scalable way to localise them and enable defect-aware calibration.
- 28 July 2026: a compilation framework for error-corrected spin qubit architectures based on the snakes-on-a-plane model with 2D surface codes and qubit teleportation had to add explicit defect-handling and mapping strategies because of high sensitivity to static defects.

## Open questions

- What two-qubit gate fidelity is achieved on 300 mm foundry-fabricated devices, and how does it vary across dies and wafers rather than within a single hero device?
- Do the noise-suppression techniques that delivered single-qubit fidelity above 99.6% under a strong field gradient extend to exchange-based two-qubit gates at the same overhead?
- Does coherent electron shuttling remain viable as the connectivity layer once the real two-level-fluctuator density along long channels is mapped?
- In the cross-platform energy efficiency framework, where do silicon spin qubits actually land relative to superconducting, trapped-ion, neutral-atom and photonic systems?

---
*Assessment drafted 2026-08-31 from up to 10 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
