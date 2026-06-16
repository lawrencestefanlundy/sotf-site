---
type: concept
slug: trapped-ion
canonical_name: Trapped Ion
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
related_concepts: []
sources:
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2025-01-23-eth-zurich-spinout-raises-42m-to-scale-trapped-ion-quantum-c]]'
frontier:
- ''
last_updated: '2026-05-02'
tags:
- concept
- technology
mention_count: 10
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 4
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
neighbors: []
---
## Physics / mechanism

Trapped-ion qubits confine individual ions—typically ytterbium (Yb⁺) or barium (Ba⁺)—in RF Paul traps using oscillating electromagnetic fields. Laser or microwave pulses drive qubit transitions between hyperfine or optical states. Gate fidelities now routinely exceed 99.9% for two-qubit operations; coherence times reach minutes to hours, orders of magnitude beyond superconducting qubits. Current systems from IonQ, Quantinuum, and Oxford Ionics operate at 20–50 physical qubits with algorithmic qubit counts (AQSC) used as the practical performance metric. Key bottleneck is gate speed (~1 ms vs ~10 ns for superconducting), limiting circuit throughput. Scaling requires photonic interconnects between trap modules or monolithic MEMS trap integration.

## Competitive landscape

Superconducting qubits (IBM, Google) dominate on speed and fab scalability but trail on fidelity and coherence. Neutral atoms (Atom Computing, QuEra) offer similar coherence with faster Rydberg gates but lower demonstrated fidelity. Photonic QC (PsiQuantum, Xanadu) is room-temperature but probabilistic. Silicon spin qubits are CMOS-compatible but early-stage on fidelity.

| Modality | Two-qubit fidelity | Coherence | Gate speed |
|---|---|---|---|
| Trapped ion | >99.9% | Minutes–hours | ~1 ms |
| Superconducting | ~99.5% | ~100 µs | ~10–50 ns |
| Neutral atom | ~99.5% | Seconds | ~100 µs |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
