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
- '[[2025-01-23-eth-zurich-spinout-raises-42m-to-scale-trapped-ion-quantum-c]]'
frontier:
- Does laser-driven (IonQ/Quantinuum/AQT) or microwave/electronic-control (Oxford Ionics/Universal Quantum/eleQtron) win the integration race — or do they converge?
- When does interconnect/networking (photonic links between trap modules), not qubit count, become the openly-acknowledged binding bottleneck? (see [[quantum-computing-modalities]] prediction)
- Can integrated PHOTONIC light delivery (on-chip waveguides for cooling/gates/readout) reach production fidelity, or does electronic control make on-chip lasers unnecessary?
- Is there a fund-shaped, independent enabling-layer business (photonic I/O chips, trap MEMS, control ASICs, vacuum/packaging) or does each full-stack vendor vertically integrate it?
last_updated: '2026-06-16'
tags:
- concept
- technology
mention_count: 11
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 5
recent_mentions:
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
  path: /sotf-site/compute/quantum-computing/quantum-computing/
  macro: compute
- slug: superconducting-qubits
  name: Superconducting Qubits
  path: /sotf-site/compute/quantum-computing/superconducting-qubits/
  macro: compute
- slug: photonic-quantum-computing
  name: Photonic Quantum Computing
  path: /sotf-site/compute/quantum-computing/photonic-quantum-computing/
  macro: compute
- slug: quantum-error-correction
  name: Quantum Error Correction
  path: /sotf-site/compute/quantum-computing/quantum-error-correction/
  macro: compute
- slug: photonic-integrated-circuits
  name: Photonic Integrated Circuits
  path: /sotf-site/photonic-systems/pic-platforms/photonic-integrated-circuits/
  macro: photonic-systems
- slug: quantum-communications
  name: Quantum Communications
  path: /sotf-site/communications/quantum-comms/quantum-communications/
  macro: communications
---
## Physics / mechanism

Trapped-ion qubits confine individual ions — typically ytterbium (Yb⁺), barium (Ba⁺) or calcium (Ca⁺) — in RF Paul traps using oscillating electromagnetic fields. Qubit transitions (hyperfine or optical states) are driven either by **lasers** or by **microwaves** (with a magnetic-field gradient). Two-qubit gate fidelities now routinely exceed 99.9% and the best published figure is **99.99%** (IonQ Tempo); coherence times reach minutes to hours, orders of magnitude beyond superconducting qubits, and every ion is identical (no fabrication-variability problem). The structural weaknesses are **gate speed** (~1 ms vs ~10 ns for superconducting, capping circuit throughput) and **wiring/optics overhead** per ion — which is what makes *integration* the whole game (below). Performance is increasingly quoted as logical-qubit counts: Quantinuum's Helios showed 48 logical qubits via color-code QEC; IonQ/Oxford Ionics target 256 physical qubits in 2026 and >10,000 (networked) by 2027. **2026 06 16 Trapped Ion Landscape 2026**

## Where it stands (2026) — context

Trapped ion is, alongside superconducting, the most commercially mature modality, and arguably leads on the metrics that matter for fault tolerance (fidelity, coherence, all-to-all connectivity). The field has split into **two control philosophies**, and the competitive question is which scales:

- **Laser-driven gates** (IonQ, Quantinuum, AQT) — the established route; highest fidelities, but needs lots of precisely-aligned optics per ion.
- **Microwave / electronic control** (Oxford Ionics, Universal Quantum, eleQtron) — drives gates with on-chip electronics/microwave fields instead of lasers, betting that semiconductor-fab-style electronic control scales better than optics.

**The binding constraint is shifting from qubit count to integration and interconnect.** Two scaling paths, not mutually exclusive: (1) **QCCD** (quantum charge-coupled device) — shuttle ions between zones on a single chip (Quantinuum's approach); (2) **photonic networking** — entangle ions across separate trap modules over optical links (the route to >10k qubits in every public roadmap). This is why the modalities thesis predicts interconnect/networking becomes the openly-acknowledged "next wall" — see **Quantum Computing Modalities**.

Conventional ion traps deliver control light with **bulk free-space optics** — large optical tables, mirrors, manual alignment — which does not scale past a lab. The frontier is putting the optics *on the trap chip*: integrated **waveguides, grating couplers, splitters and modulators** delivering multi-wavelength light (Doppler cooling, state prep, gates, readout) to each zone. Demonstrated 375–866 nm delivery in alumina and silicon-nitride waveguides; leading groups are MIT Lincoln Laboratory, ETH Zurich, Sandia and UC Berkeley (integrated optical MEMS). **2026 06 16 Trapped Ion Landscape 2026**

## Competitive landscape — trapped-ion vendors

### vs other modalities

Superconducting ([Superconducting Qubits](/sotf-site/compute/quantum-computing/superconducting-qubits/) — IBM, Google) leads on speed and fab scalability but trails on fidelity/coherence. Neutral atoms (Atom Computing, QuEra, **Planqc**) offer similar coherence with faster Rydberg gates, lower demonstrated fidelity. Photonic QC ([Photonic Quantum Computing](/sotf-site/compute/quantum-computing/photonic-quantum-computing/) — PsiQuantum, Xanadu) is room-temperature but probabilistic. Silicon spin is CMOS-compatible but early on fidelity.

| Modality | Two-qubit fidelity | Coherence | Gate speed |
|---|---|---|---|
| Trapped ion | >99.9% (best 99.99%) | Minutes–hours | ~1 ms |
| Superconducting | ~99.5% | ~100 µs | ~10–50 ns |
| Neutral atom | ~99.5% | Seconds | ~100 µs |

## Investability & routes

Substance first: if trapped ion is a winning modality, the durable value is split between (a) the **full-stack machines** — already captured by scaled players (IonQ is public; Quantinuum is heading to a ~$20B+ IPO; Oxford Ionics sold for $1.075B), so this layer is largely *not* a pre-seed opportunity; and (b) the **enabling hardware layer** — photonic I/O chips, ion-trap MEMS, control ASICs, vacuum/packaging — which is where new, capital-efficient companies can still form. Per **Quantum Computing Modalities**, the enabling silicon/photonics is the fund-shaped layer in a non-photonic modality, not the machine itself.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
