---
type: concept
slug: quantum-compilers
canonical_name: Quantum Compilers
aliases: []
kind: technology
parent_concepts:
- compute
- quantum-computing
related_concepts: []
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
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Quantum compilers translate high-level quantum algorithms into hardware-executable gate sequences, managing qubit topology constraints, gate decomposition, and error-mitigation scheduling. The core problem is mapping abstract circuits onto physical connectivity graphs while minimising circuit depth and two-qubit gate count—both directly drive decoherence-limited fidelity. Key parameters: SWAP overhead (typically 3–5× circuit depth inflation on near-term devices), T-gate synthesis cost, and routing time. State of the art includes Qiskit Transpiler, tket (Quantinuum), and BQSKit; research compilers achieve 20–40% depth reduction over naive mapping on 100+ qubit devices via heuristic and ML-guided routing. Compilation time scales poorly with qubit count—exponential for optimal solutions, hence heuristic dominance.

## Competitive landscape

Dominant stacks: Qiskit (IBM, open-source, device-specific), tket (Quantinuum, hardware-agnostic, commercially licensed), Pytket extensions, and PennyLane (Xanadu, differentiable/photonic focus). Microsoft Q# targets Majorana/topological hardware with distinct noise assumptions. Adjacent: error correction code compilers (surface code schedulers, lattice surgery compilers) are a distinct but converging layer. Pulse-level compilers (Qiskit Pulse, QubiC) operate below gate abstraction.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
