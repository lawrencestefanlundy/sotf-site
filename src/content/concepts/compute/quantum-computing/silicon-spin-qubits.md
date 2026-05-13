---
type: concept
slug: silicon-spin-qubits
canonical_name: Silicon Spin Qubits (Intel, Quantum Motion)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- quantum-computing
related_concepts: []
companies_using:
- archer-materials
- atlantic-quantum
- delft-circuits
- diraq
- emergence-quantum
- equal1
- hrl-laboratories
- imec
- intel
- kiutra
- microsoft-station-q-azure-quantum
- ntt-research
- qibo-qilimanjaro
- quantum-brilliance
- quantum-motion
- quantum-si
- quobly
- qutech-tu-delft-tno
- riken-riken-center-for-quantum-computing
- samsung-advanced-institute-of-technology-sait
- silicon-quantum-computing-sqc
- siquance-cea-leti-spinout
- spin-q-spinq-technology
- tsmc-research
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Silicon Spin Qubits (Intel, Quantum Motion)

*Kind: technology*

## Physics / mechanism

Silicon spin qubits encode quantum information in the spin state (↑/↓) of single electrons or holes confined in gate-defined quantum dots fabricated on silicon or Si/SiGe heterostructures. Confinement is electrostatic; qubit control uses microwave pulses via exchange coupling or electron dipole spin resonance (EDSR). Key parameters: T2* coherence ~1–100 µs (isotopically purified ²⁸Si pushes toward the upper bound), single-qubit gate fidelities >99.9% demonstrated at single-dot level, two-qubit fidelities 96–99% in best academic results. Intel's Horse Ridge cryogenic controller + Tunnel Falls 12-qubit chip and Quantum Motion's CMOS-native foundry approach represent the industrial frontier. Operating temperature: 50–300 mK (some demonstrations at 1K). Qubit density potential is high; dot pitch ~50 nm is compatible with existing fab nodes.

## Competitive landscape

Competing modalities: superconducting transmons (Google, IBM) have faster gates (~10–100 ns) but lower T2 and require dilution temps; trapped ions offer >99.9% two-qubit fidelity but poor scalability density; photonic qubits (PsiQuantum) sidestep coherence but demand extreme loss specs. Within solid-state spin: NV centers in diamond offer room-temp operation but poor uniformity; germanium spin qubits (Delft) show higher hole mobility and easier spin-orbit control.

## Cloudberry relevance

| Modality | Two-qubit fidelity | Scalability path | Fab compatibility |
|---|---|---|---|
| Si spin qubit | 96–99% | CMOS foundry | High |
| Superconducting | 99%+ | Custom fab | Low |
| Trapped ion | 99.9%+ | Optical/vacuum | None |


GlobalFoundries is a direct strategic adjacency — Si spin qubits require advanced CMOS gate stacks, high-uniformity ²⁸Si substrates, and cryo-CMOS control integration, all within GF's process capability envelope. Cloudberry's semiconductor materials and fab depth creates genuine technical diligence edge here. Deal-flow angles: substrate suppliers (isotopic Si, SiGe epi), cryo-CMOS IP for classical control, EDA tooling adapted for quantum-classical co-design, and fabless qubit startups needing a foundry partner conversation.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
