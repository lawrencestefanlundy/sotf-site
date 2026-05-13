---
type: concept
slug: superconducting-qubits
canonical_name: Superconducting Qubits
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
- alice-bob
- amazon-web-services-aws-amazon-braket
- atlantic-quantum
- bleximo
- delft-circuits
- google-quantum-ai
- ibm-quantum
- iqm-quantum-computers
- kiutra
- maybell-quantum
- microsoft-azure-quantum-superconducting-track
- nord-quantique
- origin-quantum
- oxford-quantum-circuits-oqc
- qiskit-ibm-backed-ecosystem-q-next-chicago-quantum-exchange
- qolab
- qruise
- quanscient
- quantum-machines
- quantware
- rigetti-computing
- riken-ntt-quantum-computing-research
- spinq-shenzhen-spinq-technology
- zurich-instruments
ideas_referencing: []
sources:
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2025-09-18-qphox-and-rigetti-awarded-58m-contract-from-afrl-to-enable-o]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 19
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 3
---

# Superconducting Qubits

*Kind: technology · Attio deal count: 12*

## Physics / mechanism

Superconducting qubits exploit Josephson junctions — tunnel junctions between two superconductors separated by a thin insulator — to create artificial two-level quantum systems. Below ~20 mK, Cooper-pair tunnelling produces nonlinear inductance, making energy levels anharmonic and addressable at microwave frequencies (4–8 GHz). Key qubit types: transmon (dominant; anharmonicity ~200–300 MHz), fluxonium (longer T1, up to ~1 ms demonstrated). Gate fidelities: single-qubit >99.9%, two-qubit ~99.5% (IBM Heron, Google Willow, 2024). Coherence times T1/T2 now routinely 100–500 µs on best devices. Scaling bottleneck is cryogenic wiring fan-out and materials-limited coherence (TLS defects at interfaces, substrate, and junction oxide).

## Competitive landscape


The primary qubit modality competitors are trapped ions (higher fidelity, slower gates, room-temperature laser control), photonic qubits (room-temp, hard to make deterministic gates), neutral atoms (fast reconfigurable arrays, early-stage error correction), and spin qubits in silicon (CMOS-compatible, short coherence currently). Superconducting qubits lead on gate speed (~10–100 ns) and ecosystem maturity.

| Modality | Gate speed | Coherence | CMOS integration |
|---|---|---|---|
| Superconducting | ~10–100 ns | 100–500 µs | Partial (via fab) |
| Trapped ion | ~1–10 µs | Seconds | No |
| Spin (Si) | ~1–100 ns | ~1 ms | High potential |

## Cloudberry relevance
Cloudberry relevance is indirect but real. Superconducting qubit scaling demands advanced fab: sub-nm junction control, low-loss dielectrics, through-silicon vias — directly in GlobalFoundries' capability envelope. Deal-flow angles: cryo-CMOS control ASICs, specialty substrate suppliers (high-resistivity silicon, sapphire), Josephson junction process IP, and packaging for dilution-refrigerator integration. Lunar Ventures' early-stage scope overlaps with European qubit hardware spinouts. Worth tracking as a customer vertical for fab-adjacent portfolio companies rather than qubit OEMs themselves.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
