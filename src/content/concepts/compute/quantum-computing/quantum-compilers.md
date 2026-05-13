---
type: concept
slug: quantum-compilers
canonical_name: Quantum Compilers
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
- algorithmic
- classiq
- google-quantum-ai
- horizon-quantum-computing
- ibm-quantum
- ionq
- iqm-quantum-computers
- microsoft-azure-quantum
- multiverse-computing
- oxford-quantum-circuits-oqc
- parityqc
- pasqal
- planqk
- q-next-argonne-unitary-fund-affiliated
- qmware
- qu-co-now-pasqal-de
- quanscient
- quantinuum
- quera-computing
- quix-quantum
- rigetti-computing
- riverlane
- strangeworks
- xanadu
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


# Quantum Compilers

*Kind: technology*

## Physics / mechanism

Quantum compilers translate high-level quantum algorithms into hardware-executable gate sequences, managing qubit topology constraints, gate decomposition, and error-mitigation scheduling. The core problem is mapping abstract circuits onto physical connectivity graphs while minimising circuit depth and two-qubit gate count—both directly drive decoherence-limited fidelity. Key parameters: SWAP overhead (typically 3–5× circuit depth inflation on near-term devices), T-gate synthesis cost, and routing time. State of the art includes Qiskit Transpiler, tket (Quantinuum), and BQSKit; research compilers achieve 20–40% depth reduction over naive mapping on 100+ qubit devices via heuristic and ML-guided routing. Compilation time scales poorly with qubit count—exponential for optimal solutions, hence heuristic dominance.

## Competitive landscape

Dominant stacks: Qiskit (IBM, open-source, device-specific), tket (Quantinuum, hardware-agnostic, commercially licensed), Pytket extensions, and PennyLane (Xanadu, differentiable/photonic focus). Microsoft Q# targets Majorana/topological hardware with distinct noise assumptions. Adjacent: error correction code compilers (surface code schedulers, lattice surgery compilers) are a distinct but converging layer. Pulse-level compilers (Qiskit Pulse, QubiC) operate below gate abstraction.

## Cloudberry relevance

| Tool | Hardware focus | Optimisation approach |
|------|---------------|----------------------|
| tket | Agnostic | Heuristic + peephole |
| Qiskit Transpiler | IBM superconducting | SABRE routing + ML |
| BQSKit | Agnostic | Numerical instantiation |


Cloudberry relevance is indirect but real. Compiler capability gates hardware adoption cycles—a photonic or semiconductor qubit platform (relevant to GF-LP portfolio thesis) lives or dies partly on compiler ecosystem maturity. Deal-flow angle: compiler IP embedded in quantum hardware startups (control stack, full-stack plays) is a defensibility signal. Lunar Ventures' early-stage mandate may surface compiler-layer companies; worth tracking as a diligence lens on any quantum hardware investment rather than a primary investment category.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
