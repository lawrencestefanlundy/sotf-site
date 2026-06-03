---
type: concept
slug: combinatorial-optimisation
canonical_name: Combinatorial Optimisation
aliases:
- combinatorial optimization
- combinatorial optimisation
- CO
parent_concepts:
- compute-paradigms
related_concepts:
- quantum-annealing
- stochastic-ising-machines
- coherent-ising-machine
- probabilistic-computing
- thermodynamic-computing
- physics-native-compute
sources: []
frontier:
- For which problem classes and instance sizes do physics-native solvers (Ising machines, quantum annealers, photonic CO accelerators) consistently beat best-in-class classical heuristics (branch-and-bound, simulated annealing, CPLEX) without cherry-picking benchmarks?
- Is the investable wedge the hardware substrate, the problem-mapping software layer, or the vertical application (logistics, drug discovery, financial portfolio, chip design)?
- As LLM-based combinatorial solvers (using reinforcement learning on graph-structured problems) mature, does physics-native CO retain a defensible energy or latency moat?
last_updated: 2026-06-02
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: quantum-annealing
  name: Quantum Annealing
  path: /sotf-site/compute/quantum-computing/quantum-annealing/
  macro: compute
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /sotf-site/compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: coherent-ising-machine
  name: Coherent Ising Machine
  path: /sotf-site/compute/non-conventional/coherent-ising-machine/
  macro: compute
- slug: probabilistic-computing
  name: Probabilistic Computing
  path: /sotf-site/compute/non-conventional/probabilistic-computing/
  macro: compute
- slug: thermodynamic-computing
  name: Thermodynamic Computing
  path: /sotf-site/compute/non-conventional/thermodynamic-computing/
  macro: compute
- slug: physics-native-compute
  name: Physics-Native Compute
  path: /sotf-site/compute/non-conventional/physics-native-compute/
  macro: compute
---
Combinatorial optimisation (CO) is the class of problems that seek the best solution from a finite but exponentially large set of discrete configurations — scheduling, routing, portfolio selection, protein folding, chip placement, and logistics are canonical instances. What makes them hard is that exhaustive search is infeasible at scale, and for NP-hard problems (travelling salesman, max-cut, graph colouring) no polynomial-time exact algorithm is known.

Classical solvers fall into two families: exact methods (branch-and-bound, integer linear programming via CPLEX or Gurobi) that find provably optimal solutions but scale poorly, and heuristics (simulated annealing, genetic algorithms, tabu search) that find near-optimal solutions in practical time. The gap between the two is the core engineering tradeoff.

The deep-tech investment angle is the claim that physics-native hardware — systems that physically encode a CO problem in an energy landscape and let the physics find the minimum — can deliver large advantages in energy efficiency and time-to-solution for specific problem classes. The principal substrates being developed are: [Quantum Annealing](/sotf-site/compute/quantum-computing/quantum-annealing/) (superconducting flux qubits mapping problem to Ising Hamiltonian), [Stochastic / Ising Machines](/sotf-site/compute/non-conventional/stochastic-ising-machines/) (CMOS or FPGA Ising emulators running probabilistic bit-flip dynamics), [Coherent Ising Machine](/sotf-site/compute/non-conventional/coherent-ising-machine/) (optical parametric oscillators or photonic networks), and photonic-compute accelerators.

The unresolved question for investment is whether the advantage is at the hardware substrate level (defensible moat) or at the application-mapping software layer, where a well-tuned classical solver still competes.

## Frontier

- For which problem classes and instance sizes do physics-native solvers (Ising machines, quantum annealers, photonic CO accelerators) consistently beat best-in-class classical heuristics without cherry-picking benchmarks?
- Is the investable wedge the hardware substrate, the problem-mapping software layer, or the vertical application (logistics, drug discovery, financial portfolio, chip design)?
- As LLM-based combinatorial solvers (using reinforcement learning on graph-structured problems) mature, does physics-native CO retain a defensible energy or latency moat?
