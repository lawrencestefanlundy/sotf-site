---
type: concept
slug: quantum-software
canonical_name: Quantum Software
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
related_concepts: []
sources:
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 7
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2024-12-16-willow-and-the-race-to-quantum-advantage
  title: Willow and The Race to Quantum Advantage (Feat. Kris Kaczmarek)
  date: '2024-12-16'
  kind: substack
neighbors: []
---
## Physics / mechanism

Quantum software encompasses the layers above quantum hardware: gate-level circuit compilers, error-correction code implementations, variational algorithms (VQE, QAOA), quantum simulation frameworks, and SDK/middleware stacks (Qiskit, Cirq, PennyLane, Braket). It operates by mapping computational problems onto qubit operations, managing decoherence budgets via transpilation and noise-aware scheduling. Current NISQ-era devices (50–1000+ physical qubits, gate fidelities 99.0–99.9% for two-qubit gates on leading superconducting and trapped-ion platforms) force software to do heavy lifting: error mitigation, circuit depth reduction, and classical co-processing. Fault-tolerant regimes—requiring ~1000 physical qubits per logical qubit under surface codes—remain 5–10 years from commercial utility. Software stacks therefore define practical capability more than raw qubit count today.

## Competitive landscape

The primary competitive axis is classical HPC/GPU acceleration for the same target workloads (quantum chemistry, optimisation, ML inference). NVIDIA cuQuantum and GPU-accelerated tensor network simulators increasingly erode near-term quantum advantage claims. Adjacent segments: quantum-classical hybrid middleware (Quantinuum TKET, Q-CTRL), quantum-native compilers targeting specific hardware (IonQ, IBM), and domain-specific libraries for finance or pharma. The moat question is whether software locks to hardware vendor or abstracts across it.

| Layer | Key Players | Hardware Lock-in |
|---|---|---|
| SDK/Middleware | Qiskit, Cirq, PennyLane | Low–Medium |
| Compiler/Optimisation | TKET, Q-CTRL Fire Opal | Medium |
| Domain Applications | Quantinuum, QC Ware | High |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
