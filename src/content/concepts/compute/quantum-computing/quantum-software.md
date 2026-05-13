---
type: concept
slug: quantum-software
canonical_name: Quantum Software
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
- 1qb-information-technologies-1qbit
- algorithmiq
- amazon-braket-aws
- classiq-technologies
- entropica-labs
- google-quantum-ai
- ibm-quantum
- ionq
- kipu-quantum
- microsoft-azure-quantum
- multiverse-computing
- q-ctrl
- qc-ware
- qilimanjaro-quantum-tech
- qmware
- qu-co-acquired-pasqal-software
- quandela
- quantinuum
- quantum-brilliance
- quantum-dice
- quera-computing
- rigetti-computing
- strangeworks
- xanadu
- zapata-ai-zapata-computing
ideas_referencing: []
sources:
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 5
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
---

# Quantum Software

*Kind: technology · Attio deal count: 3*

## Physics / mechanism

Quantum software encompasses the layers above quantum hardware: gate-level circuit compilers, error-correction code implementations, variational algorithms (VQE, QAOA), quantum simulation frameworks, and SDK/middleware stacks (Qiskit, Cirq, PennyLane, Braket). It operates by mapping computational problems onto qubit operations, managing decoherence budgets via transpilation and noise-aware scheduling. Current NISQ-era devices (50–1000+ physical qubits, gate fidelities 99.0–99.9% for two-qubit gates on leading superconducting and trapped-ion platforms) force software to do heavy lifting: error mitigation, circuit depth reduction, and classical co-processing. Fault-tolerant regimes—requiring ~1000 physical qubits per logical qubit under surface codes—remain 5–10 years from commercial utility. Software stacks therefore define practical capability more than raw qubit count today.

## Competitive landscape


The primary competitive axis is classical HPC/GPU acceleration for the same target workloads (quantum chemistry, optimisation, ML inference). NVIDIA cuQuantum and GPU-accelerated tensor network simulators increasingly erode near-term quantum advantage claims. Adjacent segments: quantum-classical hybrid middleware (Quantinuum TKET, Q-CTRL), quantum-native compilers targeting specific hardware (IonQ, IBM), and domain-specific libraries for finance or pharma. The moat question is whether software locks to hardware vendor or abstracts across it.

| Layer | Key Players | Hardware Lock-in |
|---|---|---|
| SDK/Middleware | Qiskit, Cirq, PennyLane | Low–Medium |
| Compiler/Optimisation | TKET, Q-CTRL Fire Opal | Medium |
| Domain Applications | Quantinuum, QC Ware | High |

## Cloudberry relevance
Cloudberry's angle is indirect but real. Quantum software drives demand for photonic interconnects (qubit networking), cryogenic control ASICs, and advanced packaging—all within GF's process roadmap and Cloudberry's core thesis. Portfolio companies building photonic or semiconductor components for quantum hardware need software-defined benchmarks to qualify performance. Monitoring which software stacks gain traction signals which hardware architectures will attract capital, shaping deal-flow prioritisation in the quantum hardware supply chain rather than software-layer bets directly.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
