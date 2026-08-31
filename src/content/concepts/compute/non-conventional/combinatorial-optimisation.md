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
sources:
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
frontier:
- Does the reported improvement over classical optimisation schemes on the 150-qubit Heron chance-constrained knapsack runs survive comparison against a state-of-the-art stochastic-programming solver on the same instances 2026 05 05 a quantum approach to stochastic optimization in insurance u?
- Can any quantum optimisation heuristic avoid the dequantisation pattern where a classical counterpart matches its solution quality and converges faster 2026 05 14 feedback based quantum optimization and its classical counte?
- Is there a constraint-handling method that works for global equality constraints spanning all variables without either penalty-induced landscape distortion or crippling Trotter error 2026 05 05 constraint preserving xy mixers under trotterized adiabatic ?
- Do decomposition frameworks that split problems into qubit-sized subproblems retain solution quality as instance size grows, or does the classical stitching stage become the binding constraint 2026 05 14 neural qaoa2 differentiable joint graph partitioning and par?
- For which problem classes and instance sizes do physics-native solvers (Ising machines, quantum annealers, photonic CO accelerators) consistently beat best-in-class classical heuristics (branch-and-bound, simulated annealing, CPLEX) without cherry-picking benchmarks?
- Is the investable wedge the hardware substrate, the problem-mapping software layer, or the vertical application (logistics, drug discovery, financial portfolio, chip design)?
- As LLM-based combinatorial solvers (using reinforcement learning on graph-structured problems) mature, does physics-native CO retain a defensible energy or latency moat?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 61
scorecard:
  viability: 2
  drivers: 4
  novelty: 2
  diffusion: 2
  impact: 4
  timing_band: Later (5-10yr)
  verdict: Overrated
scorecard_status: draft
sources_7d: 0
sources_30d: 6
recent_mentions:
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
neighbors:
- slug: quantum-annealing
  name: Quantum Annealing
  path: /compute/quantum-computing/quantum-annealing/
  macro: compute
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: coherent-ising-machine
  name: Coherent Ising Machine
  path: /compute/non-conventional/coherent-ising-machine/
  macro: compute
- slug: probabilistic-computing
  name: Probabilistic Computing
  path: /compute/non-conventional/probabilistic-computing/
  macro: compute
- slug: thermodynamic-computing
  name: Thermodynamic Computing
  path: /compute/non-conventional/thermodynamic-computing/
  macro: compute
- slug: physics-native-compute
  name: Physics-Native Compute
  path: /compute/non-conventional/physics-native-compute/
  macro: compute
---
**Combinatorial optimisation is the search for the best arrangement among exponentially many discrete options, and it has become the main testing ground for non-conventional compute (quantum annealers, gate-based QAOA variants, probabilistic bit hardware, tensor-network engines), where the current published record shows working demonstrations at tens to a few hundred variables but no settled advantage over classical solvers.**

## Summary

Combinatorial optimisation covers problems where the answer is a discrete configuration: which items to put in a knapsack, what order to visit cities in, how to cut a graph, which assets to hold, how to schedule cars through a paint shop. The number of candidate configurations grows exponentially with problem size, so exact solution is hopeless beyond modest sizes and practice relies on heuristics, relaxations and problem-specific preprocessing. In the non-conventional compute world these problems matter because almost all of them can be rewritten as the ground state of an Ising-type energy function, which is exactly what several unconventional hardware substrates natively minimise.

The rewriting step is where much of the engineering sits. The standard target is QUBO (quadratic unconstrained binary optimisation), with generalisations to higher-order binary forms (HOBO/PUBO) and to d-valued variables on qudits (QUDO, tensor QUDO), each with different variable counts and constraint-handling costs. Encoding choice dominates resource cost: the naive one-hot formulation of the travelling salesman problem needs O(n^2) qubits, while a compact binary register brings it to O(n log n). Constraints are handled either by penalty terms, which enlarge the problem and distort the energy landscape, or by constraint-preserving mixers such as XY-mixers that confine the evolution to the feasible subspace but incur Trotterisation error on gate-based hardware. Classical preprocessing that prunes candidate arcs before encoding cuts decision-variable counts for both classical and quantum solvers.

The solver side is a crowded field rather than a single technology. Gate-based variational methods (QAOA and its parameterisation variants, Grover-mixer QAOA for higher-order problems, feedback-based schemes), analog quantum annealing, quantum Markov chain Monte Carlo built on many-body-localised dynamics, probabilistic-bit hardware, and classical or GPU-based Ising and tensor-network engines all attack the same Ising target. Scalability is generally bought with decomposition: partition the problem into qubit-sized subproblems, solve locally, stitch classically.

The parameters that decide the outcome are: qubits or spins per problem variable after encoding; how constraints are enforced and what that does to the landscape; trainability of the variational parameters, which is governed by barren-plateau structure now being characterised analytically through dynamical Lie algebras; and, decisively, what a well-tuned classical baseline achieves on the same instance.

## Viability (2/5)

The demonstrations in these sources are genuine hardware results, not simulations only, but the scales are modest. A chance-constrained knapsack scheme ran on IBM Heron processors with circuits up to depth 177 and 3,443 gates on as many as 150 qubits, with results the authors describe as indicating improvement over classical optimisation schemes. A compact-encoding TSP framework reached best average success rates of 100%, 100% and 95.5% on 4, 5 and 6 city instances in simulation, with a two-qubit divide-and-conquer approximation of a 5-city instance run on SpinQ NMR machines. A probabilistic optimisation algorithm was demonstrated on a 64x64 perimeter-gated single-photon avalanche diode array in 0.35 micron CMOS, on 26-spin Sherrington-Kirkpatrick instances. Other results are noiseless simulations at 7, 9 and 12 qubits or two-qubit theory.

The more serious viability constraint is that the classical counterparts hold up. A direct comparison of feedback-based quantum optimisation against its classical analogue found that quantum algorithms could be advantageous in solution quality while classical algorithms converged faster, and that one of the classical algorithms showed significant scalability on higher-order binary problems. Constraint handling also remains unresolved: for problems with a single global equality constraint spanning all variables, Trotter errors impair XY-mixers enough that penalty methods are preferable. The engineering works; the value proposition is not yet demonstrated.

**TLDR: Hardware runs are real but small, and the closest classical comparisons are not losing.**

## Drivers (4/5)

On the supply side, the substrates are diverse and several are cheap to iterate. The same Ising target is being attacked with gate-based superconducting processors, NMR devices, programmable quantum simulators capable of Floquet Ising dynamics, stochastic CMOS nanodevices and large GPU clusters running tensor-network contraction. That breadth means progress does not depend on any single hardware roadmap, which is the main reason to score this dimension high.

**TLDR: Demand is specific and industrial; supply is a wide, well-funded research and hardware pipeline.**

## Novelty (2/5)

Where the sources quantify an improvement, the baseline is almost always internal to the field. Compact binary encoding beats one-hot on qubit count, O(n log n) against O(n^2). Grover-mixer QAOA improves monotonically with circuit depth on higher-order problems where transverse-field QAOA does not. A parameter-free algorithm keeps the spectral gap essentially flat where X, XX and X+sXX driver schedules show unpredictable gap reductions or collapses. Adding small PT-symmetric non-Hermitian terms greatly raises the probability of reaching the ground state after annealing in a two-qubit model. These are real advances in method, but they measure quantum against quantum.

The largest quantified deltas in this set belong to classical and hybrid machinery. Distributed multi-GPU tensor-network contraction delivers 7 to 173 times extra speedup beyond slicing within an 8-GPU DGX H100 node, and 42 to 67,869 times extra speedup at 1,024 H100 GPUs. Reinforcement learning on the qubit allocation problem cuts SWAP overhead by 65 to 85% against existing quantum compilers. And the one head-to-head study here reports classical counterparts converging faster than the quantum method they mimic. Until an advantage claim survives against a strong classical baseline on the same instance, this dimension cannot be scored higher.

**TLDR: The algorithmic ideas are new; the demonstrated margins are over other unconventional methods, not over tuned classical solvers.**

## Diffusion (2/5)

The adoption barriers are visible in the papers themselves. Every problem needs a hand-built formulation, and the review of QUDO, T-QUDO and HOBO explicitly discusses the limitations of each encoding and the mappings between them. Constraint handling has no default answer: penalty terms inflate problem size and distort the landscape, while constraint-preserving mixers break down for global constraints under Trotterisation. Variational methods carry a trainability risk that is only now being characterised analytically through dynamical Lie algebras and barren-plateau bounds. Understanding of why a given data management instance is hard for an annealer still requires numerical spectral analysis outside the reach of hardware measurement.

Two things lower the barrier. First, the field has converged on hybrid architectures where the quantum part is an optional accelerator inside a classical pipeline: clustering-based decomposition into qubit-compatible subproblems with classical refinement, learned graph partitioning plus parameter initialisation across 183 QUBO, Ising and MaxCut instances from 21 to 1,000 variables. Second, some of the supporting work is directly usable classically: arc-pruning preprocessing improves computational time and optimality gaps for classical solvers on TSPLIB benchmarks as well as quantum ones. That is a route to adoption of the pipeline without adoption of the hardware. The sources contain no evidence of production use, so the score stays low.

**TLDR: No deployment evidence in these sources; encoding, constraints and trainability all remain bespoke per problem.**

## Impact (4/5)

The breadth of the application list in these sources is the argument. The same Ising formulation covers routing (TSP), portfolio construction, manufacturing scheduling (multi-car paint shop), network flow, insurance underwriting under risk tolerance, satisfiability and resource allocation, and data management. Stochastic variants, where item weights are distributions rather than numbers, become intractable classically at relatively small sizes, which is where the marginal value of a better solver is highest.

The caveat that keeps this off 5 is that the value accrues to whichever solver wins, not necessarily to the unconventional hardware. The CO-MAP result is instructive: a 65 to 85% reduction in SWAP overhead against existing compilers came from treating compilation as combinatorial optimisation and applying reinforcement learning, with no quantum solver involved. Similarly, exact tensor network contraction underpins circuit simulation, error correction and combinatorial optimisation at once, and its recent gains are pure classical parallelism engineering. High impact for the problem class; unallocated between substrates.

**TLDR: The problem class sits under logistics, finance, manufacturing, databases and compilers; a real speedup would be broadly valuable.**

## Timing Later (5-10yr)

Two clocks run at different speeds. The classical and hybrid side delivers already: GPU tensor-network contraction speedups measured on current hardware, learned partitioning and initialisation benchmarked to 1,000 variables, preprocessing that improves classical solver performance on standard benchmarks, and reinforcement learning improvements to compilers.

The quantum-hardware clock is slower. The largest hardware run reported here is 150 qubits on IBM Heron with 3,443 gates; other hardware results are 26 spins and a two-qubit implementation of a 5-city TSP. Meanwhile encoding overhead, even after compaction to O(n log n), and unresolved global-constraint handling mean the effective problem size lags the qubit count. None of the sources gives a roadmap or a date, so the band is an inference from the gap between demonstrated scale and industrial instance sizes rather than a claim any paper makes.

**TLDR: Hybrid and classical pipeline gains land now; a defensible quantum advantage on industrial instances is not close in these results.**

## Overrated or underrated? Overrated

Specifically: quantum hardware as the route to better combinatorial optimisation is overrated relative to the evidence here, while the formulation and pipeline layer around it is undervalued. The strongest, cleanest numbers in this source set come from classical machinery: distributed tensor-network contraction, reinforcement learning on compilation, and arc-pruning preprocessing that helps classical solvers as much as quantum ones. The one paper that constructs a like-for-like classical analogue of a quantum optimiser finds the classical version converging faster and scaling well on higher-order problems. That is the pattern to watch: quantum optimisation heuristics keep generating classical descendants that perform comparably without the hardware.

The hedge is that the field is not standing still on the physics either. Parameter-free schemes that stabilise the spectral gap where standard driver schedules collapse, analytic barren-plateau characterisation via dynamical Lie algebras, and intrinsically stochastic nanodevice arrays that learn around their own device variation rather than being calibrated flat all address real failure modes rather than papering over them. Judge this on time-to-solution against a tuned classical baseline on an identical instance, and treat any result that omits that comparison as uninformative.

## Prediction

By 31 December 2027, no published result will demonstrate a quantum processor solving a combinatorial optimisation instance of 1,000 or more decision variables with a verified time-to-solution advantage over a tuned classical solver run on the same instance.

## Evidence base

- 4 May 2026: compact binary-register encoding cuts TSP data-qubit requirements from O(n^2) to O(n log n), with 100%, 100% and 95.5% best average success rates on 4, 5 and 6 city instances, and a two-qubit divide-and-conquer run of a 5-city instance on SpinQ NMR hardware.
- 5 May 2026: a chance-constrained knapsack scheme ran on IBM Heron processors at circuit depths up to 177 and 3,443 gates on up to 150 qubits, with results the authors say indicate improvement over classical optimisation schemes.
- 5 May 2026: for problems with a single global equality constraint spanning all variables, Trotter errors significantly impair XY-mixer performance and penalty-based methods are preferable.
- 14 May 2026: benchmarking feedback-based quantum optimisation against classical counterparts found quantum advantageous in solution quality but slower to converge, with one classical algorithm showing significant scalability on higher-order unconstrained binary problems.
- 14 May 2026: formulating qubit allocation as a combinatorial optimisation problem and solving it with a reinforcement learning policy cut SWAP overhead by 65 to 85% versus existing quantum compilers on MQTBench and Queko circuits.
- 2 June 2026: distributed multi-GPU tensor-network contraction gave 7 to 173 times extra speedup beyond slicing on an 8-GPU DGX H100 node and 42 to 67,869 times at 1,024 H100 GPUs.
- 5 June 2026: the Probabilistic Approximate Optimization Algorithm was demonstrated on a 64x64 perimeter-gated SPAD array in 0.35 micron CMOS, reaching high approximation ratios on 26-spin Sherrington-Kirkpatrick instances with 2p parameters up to p = 17 layers.

## Open questions

- Does the reported improvement over classical optimisation schemes on the 150-qubit Heron chance-constrained knapsack runs survive comparison against a state-of-the-art stochastic-programming solver on the same instances?
- Can any quantum optimisation heuristic avoid the dequantisation pattern where a classical counterpart matches its solution quality and converges faster?
- Is there a constraint-handling method that works for global equality constraints spanning all variables without either penalty-induced landscape distortion or crippling Trotter error?
- Do decomposition frameworks that split problems into qubit-sized subproblems retain solution quality as instance size grows, or does the classical stitching stage become the binding constraint?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
