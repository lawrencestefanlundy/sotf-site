---
type: concept
slug: trapped-ion
canonical_name: Trapped Ion
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
related_concepts:
- quantum-computing
- superconducting-qubits
- photonic-quantum-computing
- quantum-error-correction
- photonic-integrated-circuits
- quantum-communications
sources:
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2025-01-23-eth-zurich-spinout-raises-42m-to-scale-trapped-ion-quantum-c]]'
frontier:
- What are the measured fidelity and rate of inter-module links (ion shuttling, photonic or Bell-pair mediated), and do they meet the assumptions used in the distributed bivariate bicycle code simulations 2026 06 05 distributed quantum error correction with bivariate bicycle ?
- How many ions can share a trap before nonlinear motional-mode coupling dominates the error budget in practice, and do the proposed design rules (anisotropy tuning, waveform shaping) hold at that size 2026 06 04 nonlinear coupling between motional modes in trapped ion qua?
- Does the 3.8x compiler improvement in logical clock speed translate into a competitive logical operation rate against superconducting or neutral-atom machines, or does shuttling remain the binding constraint 2026 05 04 architecting scalable trapped ion quantum computers using su?
- Do the >50% gate error reductions from robust pulse design on a four-qubit register survive scaling to registers of tens of individually addressed ions 2026 06 16 high performance gates on trapped ion qubits using counterpr?
- Does laser-driven (IonQ/Quantinuum/AQT) or microwave/electronic-control (Oxford Ionics/Universal Quantum/eleQtron) win the integration race — or do they converge?
- When does interconnect/networking (photonic links between trap modules), not qubit count, become the openly-acknowledged binding bottleneck? (see quantum computing modalities prediction)
- Can integrated PHOTONIC light delivery (on-chip waveguides for cooling/gates/readout) reach production fidelity, or does electronic control make on-chip lasers unnecessary?
- Is there a fund-shaped, independent enabling-layer business (photonic I/O chips, trap MEMS, control ASICs, vacuum/packaging) or does each full-stack vendor vertically integrate it?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 23
last_reorg_date: '2026-05-13'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Later (5-10yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-01-23-eth-zurich-spinout-raises-42m-to-scale-trapped-ion-quantum-c
  title: ETH Zurich spinout raises $4.2m to scale trapped ion quantum computer - eeNews Europe
  date: '2025-01-23'
  kind: web
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
- slug: 2024-12-04-cubits-in-a-fridge-why-is-nobody
  title: Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)
  date: '2024-12-04'
  kind: substack
neighbors:
- slug: quantum-computing
  name: Quantum Computing
  path: /compute/quantum-computing/quantum-computing/
  macro: compute
- slug: superconducting-qubits
  name: Superconducting Qubits
  path: /compute/quantum-computing/superconducting-qubits/
  macro: compute
- slug: photonic-quantum-computing
  name: Photonic Quantum Computing
  path: /compute/quantum-computing/photonic-quantum-computing/
  macro: compute
- slug: quantum-error-correction
  name: Quantum Error Correction
  path: /compute/quantum-computing/quantum-error-correction/
  macro: compute
- slug: photonic-integrated-circuits
  name: Photonic Integrated Circuits
  path: /photonic-systems/pic-platforms/photonic-integrated-circuits/
  macro: photonic-systems
- slug: quantum-communications
  name: Quantum Communications
  path: /communications/quantum-comms/quantum-communications/
  macro: communications
---
**Trapped-ion quantum computing holds individual atomic ions in electromagnetic traps and entangles them through their shared motion, giving the best-in-class gate fidelities and all-to-all connectivity of any qubit platform, but current systems have fewer than 60 qubits and the route to error-corrected scale now runs through modular shuttling and inter-module links rather than bigger ion chains.**

## Summary

A trapped-ion quantum computer stores each qubit in the internal electronic states of a single charged atom, typically in the hyperfine structure of the ion, held in vacuum by radio-frequency electrodes (a Paul trap) and cooled with laser light. Because the ions in a trap repel one another they form a crystal with shared collective vibrational (motional) modes, and those modes act as a bus: a laser pulse that couples spin to motion, canonically the Mølmer-Sørensen gate, entangles any pair of ions in the crystal regardless of their position. That gives the platform its two defining properties, effective all-to-all connectivity within a trap and very high gate fidelity, at the cost of gates that are slow relative to solid-state qubits and control that is laser-intensive.

The engineering detail matters because it decides scaling. Entangling gates need counterpropagating beams that couple to motion; single-qubit gates traditionally use copropagating beams to avoid that coupling, so machines carry two beam geometries and the associated hardware and calibration overhead. As chains grow, the motional spectrum crowds and low-order nonlinear resonances between modes, arising from third-order Coulomb terms, start to dominate the gate error budget in monolithic or global-mode designs. Residual thermal motion also leaks into control error: axial motion of an ion across the curvature of its addressing beam shows up as effective amplitude noise.

The consensus answer to those limits is modularity. The Quantum Charge-Coupled Device (QCCD) architecture splits the machine into many small traps and physically shuttles ions between them, so gate zones stay small while the machine grows. Above the hardware sits quantum error correction: today's ion error rates of roughly 10^-3 to 10^-4 are five to six orders of magnitude away from the 10^-9 that practical applications are reckoned to need, so logical qubits built from many physical ions are mandatory, and the surface code is the standard candidate. Because ion modules have internal all-to-all connectivity, they are also natural hosts for higher-rate quantum LDPC codes such as bivariate bicycle codes, partitioned across processors linked by shared Bell pairs.

The parameters that decide the platform are therefore: physical two-qubit error rate; number of ions per trap before spectral crowding bites; shuttling and reconfiguration time, which sets the logical clock speed; the fidelity and rate of inter-module links; and the qubit overhead of whichever code is chosen. Architecture-level studies are now explicitly co-designing trap capacity and compilation against these, with one topology-aware compiler reported to beat existing QCCD compilers by an average of 3.8x in logical clock speed.

## Viability (3/5)

The near-term evidence is solid. Gate set tomography on a four-qubit register shows dynamically corrected pulses cutting gate error by more than 50%, with robust counterpropagating gates often beating copropagating ones, which removes one of the standing arguments for dual beam geometries. Single-ion control is mature enough to be used as a scientific instrument: programmable simulation of spin-dependent electron transfer in a synthetic chiral lattice quantum simulation of spin dependent electron transfer in a, engineered non-Markovian dissipation, and feedback cooling below the Doppler limit using fluorescence imaged onto a knife edge.

The gap is at scale. Systems have fewer than 60 qubits, logical-qubit demonstrations are restricted to small codes, and there is explicitly no clarity on how QCCD systems should be designed for practical-scale error correction. The physics obstacles are named rather than solved: nonlinear motional-mode coupling grows with system size and can limit gate performance in monolithic and global-mode architectures, with mitigation currently taking the form of design rules such as detuning from resonances, tuning trap anisotropy and shaping waveforms. Encouragingly, a microscopic noise model of multi-qubit gates finds that phonon heating, motional dephasing and photon scattering map onto error channels compatible with a scalable rotated surface code, and that spurious two-qubit errors between uncoupled qubits are typically much smaller than between gate-coupled ones. That is a theory result with experimentally relevant parameters, not a demonstration.

**TLDR: Unambiguously works at small scale with the field's best fidelities; the scaled, error-corrected version is still a set of architecture papers.**

## Drivers (3/5)

On the supply side, quantum had a standout quarter in Q2 2026 with 21 companies funded and six raising at least $100M, spanning all major qubit modalities including trapped ion, plus cryogenic control electronics, chip test and networking <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>. Ion-specific rounds visible in the sources are much smaller, for instance an ETH Zurich spinout raising $4.2m to scale a trapped-ion machine <sup class="ref"><a href="https://news.google.com/rss/articles/CBMiowFBVV95cUxQbE0zeFExSGJuY3BYZXp6MjAxTVV2QW5MQWdFTlRFNUtrZDJqWDRxMERYMGV6SUFueTBOd1dnWGQxd1g4V0tDTHE2Q055bF9WR2xiREdhZFJuT3lVWXNwVGloRWJFNlMzUktTdjVnRDEtZDNrbXRJLXloYTFlSzkxWFR1YnRHOFFJTVRnS2NidXZsMWdZZGh1eUhtQl9TdWx2aEkw?oc=5" title="ETH Zurich spinout raises $4.2m to scale trapped ion quantum computer - eeNews Europe" rel="noopener">ref</a></sup>, which suggests the platform's capital is concentrated in a few incumbents rather than spread across many new entrants. Research output is another supply signal: the sources include a steady stream of 2026 work on gates, noise characterisation, cooling, architecture and compilation, much of it from national laboratory and university groups.

On the demand side the sources do not support an assessment. There is no procurement, revenue, customer or cloud-usage evidence here. The only demand-adjacent evidence is scientific: researchers are using ion machines as simulators for open-system and light-matter problems, and in one case a variational Dicke-model study notes that implementation on actual trapped-ion computers is limited by noise. That is a real but small market.

**TLDR: Capital is flowing across all qubit modalities including ions; the sources say almost nothing about end-user demand.**

## Novelty (3/5)

What the sources do not provide is a head-to-head number against superconducting qubits, so the size of the edge is unstated here. They do point to the counter-weakness: the whole QCCD architecture literature is preoccupied with logical clock speed, which is why a compiler improvement of 3.8x in that metric is worth a paper. Ions are being optimised for speed, not fidelity, which is a fair summary of where their disadvantage lies. There is also active hedging on the platform boundary: a proposed charge-induced-dipole gate between a Rydberg-excited neutral atom and a trapped ion would give a roughly 5 kHz atom shuttle to accelerate short-distance QCCD links and enable hybrid qLDPC memories, with circuit-level Monte Carlo simulations reporting orders of magnitude more operations than atom-only or ion-only architectures at fixed code distance and logical error rate. That is a proposal, but it implies neither platform alone is expected to win outright.

**TLDR: Best fidelity and native all-to-all connectivity, which buys code choice other platforms lack; the sources do not quantify the margin over rivals.**

## Diffusion (2/5)

The first barrier is that the target design does not exist. There is no clarity on how QCCD systems should be laid out for practical-scale error correction, and the current research activity consists of tuning hardware trap capacity and compilation against surface-code requirements in simulation. A distributed alternative, partitioning a **144,12,12** bivariate bicycle code across 4, 6 or 12 processors linked by shared Bell pairs in a star network, is likewise a simulation study whose conclusions depend on a scaling factor standing in for the unknown extra noise of nonlocal operations. Committing capital to a fab-like process before that choice settles is hard.

The second barrier is control complexity. Individually addressed ion processors need per-ion laser beams whose curvature couples to residual axial motion and injects amplitude noise, requiring dedicated spectroscopic protocols to separate that from native control noise. Removing the dual copropagating and counterpropagating beam geometry via robust pulses is progress precisely because that overhead is a scaling tax. Countervailing signals exist for trap fabrication: a monolithic printed-circuit-board Paul trap, requiring no assembly, has been demonstrated for electrons rather than ions, achieving lifetimes of 2.13 ms and secular frequencies up to 90 MHz. Cheap monolithic traps are the kind of thing that would eventually make ion hardware reproducible, but a millisecond lifetime is a long way from a component.

**TLDR: Nothing about ion machines is manufacturable at volume yet, and the architecture that would be built is still undecided.**

## Impact (3/5)

Present-day impact is scientific and measurable. Single-ion processors have been used to probe the microscopic origin of chiral-induced spin selectivity by tuning nearest- and next-nearest-neighbour couplings in a donor-bridge-acceptor model, identifying interference among spin-dependent pathways as the mechanism quantum simulation of spin dependent electron transfer in a, and to show that a non-Markovian dissipation channel can move a single qubit's steady state into a regime inaccessible under Markovian dissipation. There are also spin-out benefits: fast pulse sequences that prepare non-thermal Fock-state mixtures of ion motion for displacement metrology beyond the standard quantum limit, with preparation error at or below 10% up to a Lamb-Dicke parameter of about 0.5.

The large prize is the error-corrected machine, and the sources frame it only as a requirement: practical applications need error rates below 10^-9, which is why logical qubits are needed at all. No source here quantifies the economic value of reaching that point, names an application with a resource estimate, or gives a market size. So the score reflects demonstrated research-instrument value plus a credible but unquantified endpoint, not a judgement that the endpoint is worth a specific amount.

**TLDR: Real scientific value already; the sources assert rather than demonstrate the value of the fault-tolerant endpoint.**

## Timing Later (5-10yr)

Two clocks run at different speeds. Small ion systems are already productive instruments, and control improvements are landing continuously, including the more than 50% gate error reduction from robust pulse design measured in June 2026. That capability is available now.

The fault-tolerant machine is further out. As of May 2026 systems had fewer than 60 qubits, logical-qubit demonstrations were confined to small codes, and the design of QCCD systems for practical-scale error correction was an open question being explored in simulation. Two of the more promising scaling routes, distributed qLDPC codes over Bell-pair-linked modules and hybrid atom-ion interconnects, were proposals with circuit-level simulations, not hardware. Closing a five-to-six order of magnitude error gap while multiplying qubit count by orders of magnitude, starting from designs still being selected, does not plausibly complete inside five years. The sources do not state a timeline, so this band is an inference from the size of the remaining gap.

**TLDR: Useful as a simulator now; the error-corrected machine is gated on architecture decisions that were still open in mid-2026.**

## Overrated or underrated? Fairly rated

Trapped ions deserve their reputation as a leading platform, and the 2026 literature is doing the right work: measuring the specific noise mechanisms that will bite at scale rather than chasing qubit-count headlines. Nonlinear motional-mode coupling has been modelled and turned into design rules, axial-motion-induced control noise has been isolated spectroscopically, and a microscopic multi-qubit gate noise model has been shown to be compatible with a scalable rotated surface code. That is what a platform on a real engineering path looks like.

The position to hold is that the interesting question has moved off the ion and onto the interconnect. Fewer than 60 qubits per system and no settled QCCD design for practical error correction mean the platform's future is decided by shuttling rates, Bell-pair links between modules and possibly hybridisation with neutral atoms. Anyone underwriting trapped ions on gate fidelity alone is underwriting the wrong variable; anyone dismissing them on qubit count is measuring the wrong thing too.

## Prediction

By mid-2028, published trapped-ion error-correction demonstrations will still rely on modular shuttling or inter-module links rather than a single monolithic chain of more than 100 entangled ions, and headline physical two-qubit error rates will remain at or above 10^-4.

## Evidence base

- Trapped-ion systems had fewer than 60 qubits as of May 2026, with error rates of 10^-3 to 10^-4 against an application requirement below 10^-9, and no settled design for practical-scale QEC on QCCD hardware.
- A topology-aware compilation method for surface codes on QCCD systems outperformed existing QCCD compilers by an average of 3.8x in logical clock speed (May 2026).
- Gate set tomography on a four-qubit trapped-ion register showed more than 50% error reduction from robust dynamically corrected pulses, with counterpropagating robust gates often beating copropagating ones (June 2026).
- A microscopic noise model of multi-qubit trapped-ion gates found phonon heating, motional dephasing and photon scattering to be compatible with a scalable rotated surface code, with uncoupled-qubit errors much smaller than gate-coupled ones (May 2026).
- The **144,12,12** bivariate bicycle code was simulated partitioned across 4, 6 and 12 all-to-all-connected processors linked by shared Bell pairs, an architecture the authors identify as feasible on trapped-ion and neutral-atom platforms (June 2026).
- A proposed atom-ion controlled-Z gate would give a ~5 kHz atom shuttle for short-distance QCCD links, with circuit-level Monte Carlo showing orders of magnitude more operations than atom-only or ion-only architectures at fixed code distance and logical error rate (July 2026).
- Quantum funding had a standout Q2 2026 with 21 companies funded and six at $100M or above, covering all major qubit modalities including trapped ion <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>.

## Open questions

- What are the measured fidelity and rate of inter-module links (ion shuttling, photonic or Bell-pair mediated), and do they meet the assumptions used in the distributed bivariate bicycle code simulations?
- How many ions can share a trap before nonlinear motional-mode coupling dominates the error budget in practice, and do the proposed design rules (anisotropy tuning, waveform shaping) hold at that size?
- Does the 3.8x compiler improvement in logical clock speed translate into a competitive logical operation rate against superconducting or neutral-atom machines, or does shuttling remain the binding constraint?
- Do the >50% gate error reductions from robust pulse design on a four-qubit register survive scaling to registers of tens of individually addressed ions?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
