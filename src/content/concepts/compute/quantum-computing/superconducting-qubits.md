---
type: concept
slug: superconducting-qubits
canonical_name: Superconducting Qubits
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
related_concepts: []
sources:
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2025-09-18-qphox-and-rigetti-awarded-58m-contract-from-afrl-to-enable-o]]'
- '[[2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 41
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 15
recent_mentions:
- slug: 2026-06-12-hku-sic-cryogenic-neuromorphic-chip-10mk
  title: HKU world-first cryogenic neuromorphic chip at 10 mK (silicon carbide, impact-ionisation spiking)
  date: '2026-06-12'
  kind: web
- slug: 2025-09-18-qphox-and-rigetti-awarded-58m-contract-from-afrl-to-enable-o
  title: QphoX and Rigetti awarded $5.8M Contract from AFRL to enable optical networks of superconducting qubits - TU Delft
  date: '2025-09-18'
  kind: web
- slug: 2024-12-04-cubits-in-a-fridge-why-is-nobody
  title: Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)
  date: '2024-12-04'
  kind: substack
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
- slug: 2023-05-24-launching-state-of-the-future
  title: '💡 E01: Launching State of the Future: The Worlds First Deep Tech Tracker'
  date: '2023-05-24'
  kind: substack
neighbors: []
---
## Physics / mechanism

Superconducting qubits exploit Josephson junctions — tunnel junctions between two superconductors separated by a thin insulator — to create artificial two-level quantum systems. Below ~20 mK, Cooper-pair tunnelling produces nonlinear inductance, making energy levels anharmonic and addressable at microwave frequencies (4–8 GHz). Key qubit types: transmon (dominant; anharmonicity ~200–300 MHz), fluxonium (longer T1, up to ~1 ms demonstrated). Gate fidelities: single-qubit >99.9%, two-qubit ~99.5% (IBM Heron, Google Willow, 2024). Coherence times T1/T2 now routinely 100–500 µs on best devices. Scaling bottleneck is cryogenic wiring fan-out and materials-limited coherence (TLS defects at interfaces, substrate, and junction oxide).

## Competitive landscape

The primary qubit modality competitors are trapped ions (higher fidelity, slower gates, room-temperature laser control), photonic qubits (room-temp, hard to make deterministic gates), neutral atoms (fast reconfigurable arrays, early-stage error correction), and spin qubits in silicon (CMOS-compatible, short coherence currently). Superconducting qubits lead on gate speed (~10–100 ns) and ecosystem maturity.

| Modality | Gate speed | Coherence | CMOS integration |
|---|---|---|---|
| Superconducting | ~10–100 ns | 100–500 µs | Partial (via fab) |
| Trapped ion | ~1–10 µs | Seconds | No |
| Spin (Si) | ~1–100 ns | ~1 ms | High potential |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
