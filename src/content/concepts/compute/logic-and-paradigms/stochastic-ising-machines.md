---
type: concept
slug: stochastic-ising-machines
canonical_name: Stochastic / Ising Machines
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- logic-and-paradigms
related_concepts: []
companies_using:
- 1qbit
- annealing-cloud-web-ntt-research-ntt-data
- anyon-systems
- cerebras-systems
- d-wave-systems
- denso
- excelitas-technologies-formerly-memcomputing-mpi
- extropic
- fujitsu
- hitachi
- inphi-acquired-by-marvell
- lightsolver
- nec
- normal-computing
- optalysys
- q-next-zuchongzhi-group-origin-quantum
- quadrant-biosciences-kognia-formerly-memcomputing
- quera-computing
- rain-neuromorphics
- sbquantum
- speartip-formerly-turing
- spiden-formerly-spin-q
- tetramem
- toshiba
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

# Stochastic / Ising Machines

*Kind: technology*

## Physics / mechanism

Ising machines map combinatorial optimization problems onto the ground-state search of an Ising Hamiltonian (H = −Σ J_ij σ_i σ_j − Σ h_i σ_i). Physical implementations include coupled parametric oscillators (OPO-based coherent Ising machines, CIM), CMOS oscillator networks, memristor crossbars, and quantum annealing (D-Wave). Stochastic versions inject controlled noise to escape local minima — probabilistic bits (p-bits) built from stochastic MTJ devices operating at room temperature. Current SoA: Fujitsu Digital Annealer handles ~100k fully-connected spins in CMOS; NTT/Stanford CIM demonstrated 2,000 spins at optical clock rates; D-Wave Advantage runs ~5,000 qubits but restricted topology. Target problem classes: QUBO, MaxCut, portfolio optimisation, drug docking, logistics.

## Competitive landscape

| Approach | Substrate | Spins / Scale | Maturity |
|---|---|---|---|
| CMOS Ising / Digital Annealer | Standard CMOS | 10k–100k | Commercial (Fujitsu, Toshiba) |
| Coherent Ising Machine (OPO) | Photonics + FPGA | 2k–10k | Lab / early product |
| Quantum Annealing (D-Wave) | Superconducting | ~5k qubits | Commercial, niche |
| p-bit / MTJ stochastic | Spintronics | <1k (scaling) | Research |

## Cloudberry relevance

Principal competition for near-term deployment is GPU/TPU heuristics (simulated annealing, TABU) and gate-model NISQ. Photonic CIM is the most credible differentiated path — leverages III-V or LiNbO₃ modulators, FPGA co-processors, and telecom-band components already in supply chains.


Cloudberry angle: photonic CIM startups sit squarely in the photonics + advanced materials thesis. GF's 45RFSOI and 22FDX nodes are candidate substrates for integrated CMOS-Ising or p-bit arrays — potential foundry partnership narrative. Watch for spinouts from NTT, Caltech, and Sherbrooke. Deal-flow signal: teams combining integrated photonics with algorithm co-design for logistics or biotech verticals are earliest to revenue and easiest to diligence against classical solver benchmarks.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
