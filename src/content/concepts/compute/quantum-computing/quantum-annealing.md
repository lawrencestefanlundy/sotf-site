---
type: concept
slug: quantum-annealing
canonical_name: Quantum Annealing
aliases:
- quantum annealing
- QA
parent_concepts:
- quantum-computing
related_concepts:
- combinatorial-optimisation
- stochastic-ising-machines
- coherent-ising-machine
- thermodynamic-computing
- probabilistic-computing
- physics-native-compute
sources: []
frontier:
- At what problem size and density does a quantum annealer outperform best-in-class classical heuristics (simulated annealing, CPLEX) on commercially relevant instances, and has that crossover been demonstrated outside benchmark suites?
- Does coherent quantum annealing (superconducting qubits with tunable couplers) provide a genuine advantage over classical Ising-machine emulators (CMOS, FPGA-based SIM) for sparse graphs typical of logistics and finance problems?
- What is the viable path to room-temperature quantum-annealing hardware, and is gate-native (QAOA on gate-model QPU) or dedicated annealing the better long-run substrate for combinatorial problems?
last_updated: 2026-06-02
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: combinatorial-optimisation
  name: Combinatorial Optimisation
  path: /sotf-site/compute/non-conventional/combinatorial-optimisation/
  macro: compute
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /sotf-site/compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: coherent-ising-machine
  name: Coherent Ising Machine
  path: /sotf-site/compute/non-conventional/coherent-ising-machine/
  macro: compute
- slug: thermodynamic-computing
  name: Thermodynamic Computing
  path: /sotf-site/compute/non-conventional/thermodynamic-computing/
  macro: compute
- slug: probabilistic-computing
  name: Probabilistic Computing
  path: /sotf-site/compute/non-conventional/probabilistic-computing/
  macro: compute
- slug: physics-native-compute
  name: Physics-Native Compute
  path: /sotf-site/compute/non-conventional/physics-native-compute/
  macro: compute
---
Quantum annealing is a metaheuristic optimisation technique that exploits quantum mechanical tunnelling to escape local minima when searching the energy landscape of a combinatorial problem. It maps a problem onto an Ising Hamiltonian — a network of binary spins with pairwise couplings — and evolves the system from an initial quantum superposition toward its ground state by slowly reducing a transverse magnetic field (the quantum fluctuation term). The goal is for the system to settle in, or near, the lowest-energy configuration, which corresponds to the optimal or near-optimal solution.

The physics distinguishing it from classical simulated annealing: tunnelling allows the system to pass through energy barriers rather than over them, which in theory enables faster escape from local minima at low temperature. Whether this translates to a practical advantage on real problem instances remains the central open question — benchmark evidence is mixed and highly instance-dependent.

The dominant hardware platform is the superconducting flux-qubit architecture pioneered by **D Wave Systems** (Advantage system: ~5,000 qubits with Pegasus graph topology). **Qilimanjaro Quantum Tech** is developing coherent quantum annealing processors. Classical digital annealers — CMOS or FPGA chips that emulate Ising dynamics without quantum coherence — are built by **Fujitsu Digital Annealer Division** and others; they reach thousands of spins at room temperature, making hardware comparison with true quantum annealers non-trivial.

In the KB, quantum annealing sits within the **Extreme Low Power Compute** thesis as the "Ising/annealing" substrate vertical — investable where there is a demonstrated energy-per-operation advantage on a specific customer problem class, not as a general-purpose compute bet. Its closest conceptual siblings are [Stochastic / Ising Machines](/sotf-site/compute/non-conventional/stochastic-ising-machines/) (classical probabilistic emulation) and [Coherent Ising Machine](/sotf-site/compute/non-conventional/coherent-ising-machine/) (photonic or optical-parametric Ising machines).

## Frontier

- At what problem size and density does a quantum annealer outperform best-in-class classical heuristics (simulated annealing, CPLEX) on commercially relevant instances, and has that crossover been demonstrated outside benchmark suites?
- Does coherent quantum annealing (superconducting qubits with tunable couplers) provide a genuine advantage over classical Ising-machine emulators (CMOS, FPGA-based SIM) for sparse graphs typical of logistics and finance problems?
- What is the viable path to room-temperature quantum-annealing hardware, and is gate-native (QAOA on gate-model QPU) or dedicated annealing the better long-run substrate for combinatorial problems?
