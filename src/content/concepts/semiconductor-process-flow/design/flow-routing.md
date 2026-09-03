---
type: concept
slug: flow-routing
canonical_name: Routing (process step)
seq: 10
phase: design
related_concepts:
- eda-design-tools
created: 2026-06-20
last_updated: '2026-08-31'
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
- '[[2026-07-28-laser-on-a-chip-w-matt-crowley-scintil]]'
mention_count: 293
parent_concepts:
- flow-rtl-design
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Underrated
scorecard_status: draft
frontier:
- Do the higher qudit levels used as spectral buses retain coherence long enough that the 2L+1 versus 3L primitive saving survives as a fidelity saving on real hardware, or does the shorter lifetime of higher levels cancel the depth advantage?
- Does the 15 to 30 per cent congestion reduction from affine derandomisation, and the Theta(log N) routing number, hold on physically realisable acousto-optic lattices with finite move times, or only in the idealised matching model?
- Will the single-photon switching community actually adopt consistent reporting of speed, efficiency and fidelity, and when it does, which platform among quantum dots, neutral atoms, superconducting qubits and colour centres leads?
- At what routing density does the sub-kelvin thermal conductivity of the substrate, spanning 5x10^-2 down to 8x10^-4 W/m.K at 300 mK depending on material, become the binding limit on co-integrating control and readout with qubits?
sources_7d: 4
sources_30d: 14
recent_mentions:
- slug: 2026-08-20-callosum-100m-seed-announcement
  title: Callosum announces $100M seed led by Atomico (round coverage + Companies House filings)
  date: '2026-08-20'
  kind: web
- slug: 2026-08-05-uk-neocloud-landscape-sweep
  title: UK neocloud landscape sweep — filling the coverage gap under the neocloud/serving map
  date: '2026-08-05'
  kind: web
- slug: 2026-07-28-laser-on-a-chip-w-matt-crowley-scintil
  title: Laser on a Chip w/ Matt Crowley @ Scintil Photonics
  date: '2026-07-28'
  kind: substack
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
neighbors:
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
---
**Routing is the design step that decides which physical path an information carrier takes between the elements that must interact, and in quantum and wave-based substrates it has stopped being a back-end detail and become one of the main determinants of how much useful computation a chip can do.**

## Summary

In any layered design flow, routing is the step that turns a placed set of functional elements into a set of physical paths connecting them. Placement decides where things sit; routing decides how they talk. On a conventional die that is a wiring and congestion problem. The evidence base assembled here covers a different and harder version of the same step: routing where the carrier is a fragile quantum state, a single photon, a spin wave, or an entangled pair, and where every extra hop costs fidelity, depth or energy rather than just area.

The recurring structure is the same across platforms. Hardware offers limited connectivity (nearest-neighbour couplers, a fixed number of inter-module ports, a finite set of optical channels). Any operation between non-adjacent elements must therefore be transported. On superconducting-style hardware the default transport primitive is SWAP insertion, which inherits both depth overhead and path congestion, and compilers built on abstract SWAP models are reported to impose several times the routing overhead in circuit depth or duration. The 2026 literature attacks this from three directions at once: better compilers that route to the native gate set rather than to an idealised CX model; new routing primitives that avoid moving the computational state at all, for example using higher qudit levels as spectral buses so that a length-L nonlocal operation costs 2L+1 rather than 3L primitives; and topology engineering, where routing number and congestion are set by the spectral properties of the interconnect graph, with Ramanujan hypergraph constructions giving a routing number of Theta(log N) and affine derandomisation on Cayley graphs giving 15 to 30 per cent congestion reduction.

The parameters that decide the outcome are therefore: the connectivity degree and spectral gap of the substrate; the overhead multiplier of the transport primitive; congestion when multiple routes overlap; the physical cost per hop (fidelity loss in entanglement routing, insertion loss and crosstalk in photonics, heat in cryogenic interconnect); and whether the routing decision is made statically at compile time or dynamically online. At the physical layer these show up as hard numbers: on-chip spectral routing of retrieved telecom photons at up to 20 MHz with inter-channel crosstalk below 10^-4 in thin-film lithium niobate, and sub-kelvin substrate thermal conductivity spanning nearly two orders of magnitude between high-resistivity silicon at 5x10^-2 W/m.K and low-resistivity silicon at 8x10^-4 W/m.K at 300 mK, which bounds how densely on-chip routing can be packed in an integrated cryogenic system.

One caution on scope. The supplied sources do not cover routing as practised in conventional CMOS physical design, and they do not cover the classical EDA toolchain. They also contain a namespace collision: quantum algorithms for the capacitated vehicle routing problem concern routing as an optimisation workload, not as a step in a fabrication or design flow. Everything below is an assessment of routing as a design and interconnect step in quantum and wave-based hardware, because that is what the evidence supports.

## Viability (3/5)

The strongest experimental evidence is optical. A full-stack continuous-variable platform with one hundred inputs demonstrates programmable routing of quantum states across 101 input modes at a 100 MHz clock, with a cloud interface and an open-source SDK. Thin-film lithium niobate shows frequency-selective routing of retrieved photons at up to 20 MHz with crosstalk below 10^-4, alongside 23.3 plus or minus 0.5 per cent on-chip storage efficiency for 100 ns storage and an entanglement-witness violation exceeding 11 standard deviations. Magnonic routing elements have been fabricated by single-step direct laser writing in yttrium iron garnet, with phase-coherent propagation over hundreds of wavelengths and complete periodic power transfer in coupled waveguides, then cascaded into multi-stage programmable networks.

Against that, the routing schemes with the largest claimed leverage are not yet hardware results. Swap-free qudit bus routing is verified by proofs of decodability, reversibility and correctness plus Cirq simulations, and carries a state-count lower bound of d greater than or equal to 2^(K+1) for exact overlap routing at fan-in K. Fidelity-guaranteed entanglement routing is evaluated on synthetic 100-node topologies. The nonreciprocal spin-photon routing platform is a proposal, with residual backscattering estimated at around 100 Hz. A review of emitter-based single-photon switching explicitly calls for consistent reporting of speed, efficiency and fidelity, which is a plain statement that the field cannot currently be compared like for like. Three is the honest score: the step demonstrably works, the improvements to it are largely unvalidated on hardware.

**TLDR: Routing works and is demonstrated end to end in photonics; the schemes that would remove its overhead are mostly simulation and theory.**

## Drivers (4/5)

On the demand side, the sources are consistent that monolithic scaling is running out and that this converts routing into the binding constraint. Distributed quantum computing is framed as the alternative to monolithic scaling, which shifts compilation from placing and routing within one module to placing, routing and scheduling across modules. Modular multi-QPU compilation must simultaneously respect local coupling, cross-QPU traffic, per-QPU communication port counts and interconnect link-load congestion. In the classical datacentre, AI traffic is described as making multicast a binding constraint on optical circuit switching, which is a routing-capability problem rather than a bandwidth problem. Quantum networking adds a demand driver of its own: applications need end-to-end Bell pairs above a per-request fidelity threshold, which routing must guarantee.

On the supply side, hardware breakthroughs enabling high-precision native gates beyond CX, such as sqrt(iSWAP) and ZZ(theta), have opened a gap that compiler strategies have not yet filled, and Canopus is presented as the framework to close it. Reconfigurable neutral-atom lattices and 3D acousto-optic lens architectures supply a physically movable substrate on which routing is a scheduling problem with a capacity-depth tradeoff. Tooling is being shipped in Python and Qiskit. The concentration of independent 2026 work on the same problem is itself a supply signal.

**TLDR: Demand is created by the shift to modular and distributed architectures; supply is a compiler and topology research wave already producing usable frameworks.**

## Novelty (3/5)

The baseline being beaten is explicit in most papers: three-CX-unrolled SWAP insertion on a nearest-neighbour coupling graph. Against it, the qudit spectral-bus scheme reduces a length-L nonlocal operation from 3L to 2L+1 logical routing primitives while keeping overlapping routes distinguishable by bus labels, and extends to Boolean fan-in at depth 2L + D_g + O(1). On the topology side, Ramanujan hypergraph routing achieves a routing number of Theta(log N) with L = O(log N) overlay layers, and affine derandomisation on Cayley graphs over Z_n^2 yields 15 to 30 per cent congestion reduction, with an abelian Alon-Boppana barrier proving that fixed-degree Cayley graphs on that group cannot be Ramanujan. For fermionic simulation, dynamically reorienting the Jordan-Wigner transformation gives O(sqrt(N)) depth matching fermionic swap networks, falling to O(log N) on reconfigurable qubit arrays and O(1) in lattice-surgery surface-code architectures, with no space overhead.

The honest read is that these are meaningful but incremental against a baseline that everyone agrees is bad: a 33 per cent primitive-count reduction, a 15 to 30 per cent congestion reduction, a log-factor improvement contingent on hardware that can reconfigure. The genuinely novel claims are structural rather than numeric. Removing state transport entirely by routing control information through orthogonal spectral buses is a different model of what routing is. Eliminating lossy splitters in multicast optical switching by using multi-layer phase modulation, and adding wavelength selectivity for space-wavelength routing, changes the scaling limit rather than the constant. Neither has been shown at scale on hardware.

**TLDR: Real, quantified gains over the SWAP baseline, but mostly constant factors and asymptotics rather than a change of regime.**

## Diffusion (3/5)

Diffusion splits cleanly. Software routing improvements have a short path to users: frameworks are being built directly on Python and Qiskit, the optical platform ships a cloud interface and an open-source SDK, and a routing framework explicitly designed to be applicable across diverse ISAs via a canonical two-qubit representation is engineered for portability. Reinforcement-learning compilation policies are pitched as generalising across circuits rather than being tuned per instance, which lowers the integration cost further.

The hardware-side barriers are substantial. Exact congestion relief is proved to require local Hilbert-space expansion, meaning the qudit route cannot be adopted by a fixed two-level device at all, and the state-count requirement grows as d greater than or equal to 2^(K+1) with fan-in. Cryogenic integration constrains how much routing can be co-located with qubits, since substrate thermal conductivity at 300 mK varies from 5x10^-2 W/m.K for high-resistivity silicon down to 8x10^-4 W/m.K for low-resistivity silicon and around 2x10^-3 W/m.K for borosilicate and sapphire. And the single-photon switching literature cannot yet be compared across platforms because speed, efficiency and fidelity are not consistently reported, which is a direct obstacle to procurement decisions.

**TLDR: Compiler-layer routing diffuses easily through existing SDKs; substrate-layer routing needs hardware that does not yet exist in volume.**

## Impact (4/5)

The scale of the prize is set by the size of the tax. Existing scalable routing methods impose several times the routing overhead in circuit depth or duration, and routing is characterised as a critical stage for both near-term and fault-tolerant machines. On depth-limited hardware, depth spent on transport is depth not spent on computation, so a routing improvement is close to a one-for-one improvement in the size of problem a given device can run. The same logic applies across the stack: entanglement routing that meets per-request fidelity thresholds is the difference between a quantum network that can serve applications and one that can only move Bell pairs, and multicast capability without lossy splitters is the difference between an optical circuit switch that scales with AI traffic and one that does not.

The qualifier is that this value is entirely conditional on the underlying platforms mattering. Routing improvements have no standalone market; they are a multiplier on whatever quantum, photonic or magnonic computing turns out to be worth. Within that conditionality the leverage is high and the sources support it, which is why this scores 4 rather than 5. Nothing here demonstrates that improved routing has yet changed an application-level outcome on real hardware.

**TLDR: Routing overhead is currently a multiple of the useful work, so removing it converts directly into machine capability.**

## Timing Soon (2-5yr)

The software layer is already moving. Unified routing frameworks across diverse ISAs, port- and congestion-aware modular compilers and RL-based distributed compilation policies were all published within days of each other in May 2026 and are implemented in mainstream toolchains. Improvements of this kind can reach users as soon as vendors adopt them, which puts them in the 0 to 2 year window.

The structural changes are slower. Swap-free qudit routing requires local Hilbert-space expansion on the physical device. Theta(log N) routing on reconfigurable atom lattices depends on multi-layer 3D acousto-optic architectures. The O(1) fermion-routing depth result is conditional on lattice-surgery surface-code architectures, which is fault-tolerant-era hardware. Photonic and magnonic routing fabrics are at the level of demonstrated building blocks and cascaded meshes rather than products. Two to five years is the band in which the compiler gains should be measurable in delivered quantum volume and the first hardware-native routing primitives should be demonstrated, not the band in which they are standard.

**TLDR: Compiler-level routing gains are landing now; the primitives that would remove routing overhead structurally need hardware that is two to five years out.**

## Overrated or underrated? Underrated

Routing is treated as plumbing and reported as a compiler footnote while qubit counts get the headlines, yet by the field's own account it consumes several times the depth of the computation it enables. A machine whose routing overhead falls by a factor of two is, for practical purposes, a substantially larger machine, and it is achieved by software and topology choices rather than by fabricating more qubits. That asymmetry between cost and leverage is the definition of underrated. The concentration of independent work on the problem in 2026, spanning compilers, graph theory, qudit hardware models, entanglement networks, photonics and cryogenic packaging, suggests the field has worked this out even if the outside narrative has not.

Two caveats keep this from being a stronger call. First, the biggest claimed wins are proofs and simulations, not hardware results, and one of them is proved to require a hardware change that most platforms cannot make. Second, the physical-layer routing work has a measurement problem: a review of the single-photon switching field had to argue for reporting speed, efficiency and fidelity at all, which means cross-platform claims should be treated with caution until that changes. The sources support no assessment whatsoever of routing as a step in conventional semiconductor physical design, and nothing here should be read as one.

## Prediction

By 31 December 2027, no experimental hardware demonstration of swap-free qudit spectral-bus routing achieving the claimed 2L+1 primitive count for a nonlocal operation over a path of length L greater than or equal to 3 will have been published, leaving the result at the simulation stage reported in May 2026.

## Evidence base

- Compilers relying on abstract three-CX-unrolled SWAP models impose several times the routing overhead in circuit depth or duration, motivating routing frameworks built on canonical two-qubit representations for advanced ISAs such as sqrt(iSWAP) and ZZ(theta) (5 May 2026).
- A swap-free routing framework using higher qudit levels as orthogonal spectral buses needs 2L+1 logical routing primitives for a length-L nonlocal operation against a 3L baseline, with Boolean fan-in at depth 2L + D_g + O(1) and a state-count lower bound d greater than or equal to 2^(K+1); verified by proofs and Cirq simulation (4 May 2026).
- Routing on Ramanujan (d,r)-regular hypergraphs achieves a routing number of Theta(log N), with multi-layer 3D acousto-optic stacking using L = O(log N) overlay layers and affine derandomisation giving 15 to 30 per cent congestion reduction (5 May 2026).
- A full-stack continuous-variable optical platform with one hundred inputs demonstrated programmable routing of quantum states across 101 input modes at a 100 MHz clock, with a cloud interface and the open-source mqc3 SDK (8 May 2026).
- An erbium-doped thin-film lithium niobate microring memory achieved frequency-selective storage and routing of retrieved photons at up to 20 MHz with inter-channel crosstalk below 10^-4, 23.3 plus or minus 0.5 per cent on-chip storage efficiency for 100 ns storage, and a 277.6 plus or minus 52.6 s comb lifetime (15 May 2026).
- Measured sub-kelvin substrate thermal conductivity at 300 mK spans high-resistivity silicon at 5x10^-2 W/m.K, borosilicate and sapphire at 2x10^-3 W/m.K, and low-resistivity silicon at 8x10^-4 W/m.K, setting the thermal budget for on-chip routing in integrated cryogenic quantum systems (8 May 2026).

## Open questions

- Do the higher qudit levels used as spectral buses retain coherence long enough that the 2L+1 versus 3L primitive saving survives as a fidelity saving on real hardware, or does the shorter lifetime of higher levels cancel the depth advantage?
- Does the 15 to 30 per cent congestion reduction from affine derandomisation, and the Theta(log N) routing number, hold on physically realisable acousto-optic lattices with finite move times, or only in the idealised matching model?
- Will the single-photon switching community actually adopt consistent reporting of speed, efficiency and fidelity, and when it does, which platform among quantum dots, neutral atoms, superconducting qubits and colour centres leads?
- At what routing density does the sub-kelvin thermal conductivity of the substrate, spanning 5x10^-2 down to 8x10^-4 W/m.K at 300 mK depending on material, become the binding limit on co-integrating control and readout with qubits?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
