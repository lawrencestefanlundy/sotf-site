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
sources:
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
scorecard:
  viability: 3
  drivers: 3
  novelty: 2
  diffusion: 2
  impact: 3
  timing_band: Unclear
  verdict: Overrated
scorecard_status: draft
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2024-12-04-cubits-in-a-fridge-why-is-nobody
  title: Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)
  date: '2024-12-04'
  kind: substack
neighbors:
- slug: combinatorial-optimisation
  name: Combinatorial Optimisation
  path: /compute/non-conventional/combinatorial-optimisation/
  macro: compute
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: coherent-ising-machine
  name: Coherent Ising Machine
  path: /compute/non-conventional/coherent-ising-machine/
  macro: compute
- slug: thermodynamic-computing
  name: Thermodynamic Computing
  path: /compute/non-conventional/thermodynamic-computing/
  macro: compute
- slug: probabilistic-computing
  name: Probabilistic Computing
  path: /compute/non-conventional/probabilistic-computing/
  macro: compute
- slug: physics-native-compute
  name: Physics-Native Compute
  path: /compute/non-conventional/physics-native-compute/
  macro: compute
---
**Quantum annealing uses a slowly varying transverse-field Ising Hamiltonian in analog hardware (chiefly D-Wave machines) to find low-energy solutions of binary optimisation problems, and after two decades it remains a usable, commercially accessible device whose advantage over good classical solvers is still narrow, contested and problem-specific.**

## Summary

Quantum annealing (QA) attacks combinatorial optimisation by physics rather than by circuits. A problem is first rewritten as a quadratic unconstrained binary optimisation (QUBO) problem, equivalently an Ising spin model, so that the answer is the ground state of an energy function. The hardware is initialised in the easy ground state of a strong transverse field and the Hamiltonian is then swept slowly towards the problem Ising Hamiltonian; if the sweep is slow relative to the minimum energy gap, the system should stay in the ground state and be read out as the solution. Quantum fluctuations, rather than the thermal fluctuations of classical simulated annealing, drive the escape from local minima. This is analog, not gate-based, computation: there is no error correction, and noise and small gaps set the limits.

The parameters that decide whether QA is useful are mostly unglamorous. First, formulation cost: constraints must be folded in as quadratic penalty terms, whose weights have to be tuned, and penalty-free reformulations are an active research line precisely because penalties waste qubits and distort the landscape. Second, embedding overhead: the QUBO graph must be mapped onto the fixed sparse hardware graph, which inflates qubit counts and degrades performance as instances grow. Third, the spectral gap and freeze-out dynamics, which determine whether the anneal is adiabatic at all and which are largely invisible to direct hardware measurement, motivating dedicated numerical toolboxes. Fourth, scheduling tricks: reverse annealing, pauses, quench-based mid-anneal readout, all of which have narrow optimal windows.

In practice almost every applied study in the current literature is hybrid: the instance is decomposed or clustered, subproblems go to a D-Wave QPU or to D-Wave's hybrid solvers, and the results are compared against Gurobi, simulated annealing and metaheuristics. The term also increasingly denotes an algorithm rather than a machine: simulated quantum annealing and path-integral formulations run on classical CPUs, on molecular-dynamics frameworks, and on probabilistic p-bit hardware, and in at least one benchmark the classical path-integral variant beat the quantum hardware pipeline.

So the assessment question is not whether the machines run. They run, at hundreds to thousands of qubits, and outside groups can book time on them. The question is whether the physical annealer beats the best classical alternative on any problem anyone cares about, at a size anyone cares about.

## Viability (3/5)

QA is unambiguously past the demonstration stage as a *device*. Independent groups run D-Wave Advantage and Advantage2 systems on Max-Cut, number partitioning, clustering, traffic assignment, protein-like lattice problems, atomic structure calculations and generative-model training, and report results rather than failures to execute. Reverse annealing, pauses and quench readout are real, tunable operational knobs that measurably improve output quality.

What stops this being a 4 is scaling behaviour on a physically decoded benchmark. On a greenhouse heater-scheduling QUBO, direct QPU execution recovered the exact optimum for horizons H=10 and H=12, but the exact-hit rate fell from 5/10 to 2/10 and then to 0/10 at H=14, with much higher variance than classical baselines, while the D-Wave Leap Hybrid BQM workflow was less reliable than classical simulated annealing under 15 to 60 second time limits. Embedding overhead is explicitly identified as the binding constraint when instance size doubles. Noise remains the primary limiter, though there is experimental evidence that annealer noise is metastable and can therefore be partly designed around.

**TLDR: The hardware works and is routinely used by third parties, but solution quality collapses with modest increases in problem size.**

## Drivers (3/5)

Supply side: the sources describe an effectively single-vendor analog ecosystem. D-Wave hardware (Advantage, Advantage2), its QPU access modes and its Leap hybrid BQM solvers appear in nearly every applied paper. Adjacent supply is diversifying rather than reinforcing: neutral-atom machines solving maximum weighted independent set inside a Monte Carlo tree search, Ising p-bit processors built from magnetic tunnel junctions, and classical path-integral implementations all target the same QUBO market without being quantum annealers.

Demand side: the pull is real but so far academic. Named application domains in the last quarter alone include city-wide traffic flow with up to tens of thousands of vehicles, multi-agent route planning on Barcelona instances with up to 10,000 vehicles, Steiner TSP with time windows and pickup-delivery for last-mile and reverse logistics, greenhouse control, lattice protein folding, molecular generative design for drug discovery, atomic hyperfine structure constants, and database query optimisation. The sources contain no revenue, funding or customer-count figures, so the strength of paying demand cannot be assessed from them.

**TLDR: Supply is a single dominant commercial platform with open cloud access; demand is broad academic pull from logistics, materials and drug discovery, with no commercial procurement evidence in the sources.**

## Novelty (2/5)

The strongest positive result in the set is binary compressed sensing. Across 19,775 experiments with nine classical solvers, D-Wave recovered sparse binary signals inside the 'relaxation gap' below the Donoho-Tanner l1 phase transition, a regime where the l0 solution exists but convex relaxations fail. At n=32, k=5, m/n=0.19 the annealer achieved 7% exact recovery while Approximate Message Passing (asymptotically Bayes-optimal for Gaussian matrices) and eight other solvers scored 0% over 250 combined trials, Fisher exact p=0.018. That is better than the alternative, but 7% versus 0% at n=32, and at n=64 embedding overhead already limits the QPU to hybrid parity with AMP.

Against that: on the greenhouse control QUBO, classical simulated annealing and classical path-integral simulated quantum annealing both produced feasible near-optimal solutions in every repetition while the D-Wave hybrid workflow did not outperform them, and the authors state the results do not indicate quantum advantage. The large-scale Advantage2 Ising spin-glass annealing dynamics previously claimed beyond classical reach have been reproduced to state-of-the-art accuracy with lattice-specific tensor networks and belief propagation using modest computational resources, scalably in two and three dimensions and up to hundreds of qubits. In routing, D-Wave hybrid solvers sit alongside Gurobi and simulated annealing rather than above them. Theoretically the paradigm is at least not weaker than gate-based computing: the global transverse-field Ising model can simulate arbitrary quantum circuits with polynomial overhead, though the overheads are large relative to real hardware.

**TLDR: One narrow, statistically thin win over Bayes-optimal classical inference; losses or ties elsewhere; the headline beyond-classical spin-glass claim has been challenged.**

## Diffusion (2/5)

Access is the easy part: hybrid cloud solvers are called routinely from ordinary optimisation pipelines, and toolchains for generating instances, building QUBO matrices and benchmarking against Gurobi and metaheuristics are being published openly. The barriers are upstream. Problems must be recast as QUBO, which forces constraint handling into quadratic penalties with a tuned weight; in multi-agent routing a single penalty parameter controls the coverage-overlap trade-off and Pareto-optimal solutions appear only in the hard-penalty regime. Traffic instances required Leiden clustering to partition vehicles into independently solvable communities purely to contain combinatorial growth. Analytically derived penalty parameters and penalty-free encodings are active research topics rather than settled engineering.

On top of that, the practitioner has to tune annealing schedules: reverse annealing helps, but only within a narrow optimal window of reverse distance, pause duration and annealing time tied to freeze-out points. A blunt statement of the diffusion problem comes from a competing approach: practical problem instances for QUBO plus quantum annealing remain out of reach for existing hardware. Until an operator can hand over an industrial instance and get a better answer than Gurobi without a physics team, adoption stays in pilots.

**TLDR: Cloud access is easy, but every real instance needs QUBO reformulation, penalty tuning and decomposition before it fits, and the payoff for that work is not yet established.**

## Impact (3/5)

If a general QUBO advantage materialised, the value would be large and broad: the sources map QA onto NP-hard problems that are genuinely load-bearing in industry, including last-mile and reverse logistics routing with time windows and capacity limits, city-scale traffic assignment, database query optimisation, global minimisation of potential energy surfaces in materials and structure search, and molecular generative design, where quantum-annealing-trained models produced compounds with higher validity and drug-likeness than fully classical equivalents.

The demonstrated impact is much smaller than that ceiling. The compressed-sensing win is confined to a specific phase-diagram wedge at n=32; the control benchmark shows no advantage and degradation by H=14; and one of the field's most cited scaling results is now contested by tensor networks. A real secondary impact is scientific: QA hardware is a working analog platform for probing Kibble-Zurek physics, spin-glass dynamics and metastable noise, and that value survives even if optimisation advantage never arrives.

**TLDR: The addressable problem set is enormous, but demonstrated value per instance is currently marginal and concentrated in narrow regimes.**

## Timing Unclear

Availability is a Now question and already answered: D-Wave QPUs and hybrid solvers are being used by third-party groups across at least eight distinct application domains within a single quarter of published work in mid-2026. Usefulness is the open question, and the evidence points in both directions simultaneously: a statistically significant but tiny advantage at n=32 in compressed sensing, no advantage and collapse at H=14 in control, and a prior beyond-classical claim being walked back by classical simulation.

The improvement levers on the table (reverse annealing schedules, penalty-free encodings, noise-aware design exploiting metastability, exotic non-Hermitian qubit architectures) are incremental or theoretical, and none carries a roadmap or date in these sources. Assigning a 2-5 or 5-10 year band would be invention on my part. The honest band is Unclear, and the resolution will come from head-to-head benchmarks rather than from hardware announcements.

**TLDR: The hardware is bookable today, but nothing in the sources dates the arrival of a durable practical advantage.**

## Overrated or underrated? Overrated

Judged against the claim that quantum annealing is a working commercial optimisation advantage, the current evidence does not carry it. The single cleanest well-controlled applied benchmark in this set explicitly concludes that the results do not indicate quantum advantage, with the hybrid workflow losing to plain simulated annealing and the QPU's exact-hit rate falling to 0/10 by H=14. The field's flagship beyond-classical spin-glass dynamics claim has been matched by tensor networks with belief propagation on modest resources and, worse for the claim, in a way that scales in both two and three dimensions. Meanwhile the classical impersonator, path-integral simulated quantum annealing, keeps performing well.

That said, this is not a dismissal. The compressed-sensing result is the most interesting piece of evidence in years for a specific reason: it is not a speed claim but a *solvability* claim, recovery inside the relaxation gap where nine classical methods including asymptotically Bayes-optimal AMP score zero, with an energy-landscape mechanism (deep true ground state, shallow trapping basins) consistent with tunnelling. If that structural signature generalises to larger n and to other problem families, the assessment flips quickly. Underrated, in other words, as a physics platform and as a probe of where quantum fluctuations help; overrated as a product you should be buying to run your logistics.

## Prediction

By 31 December 2027, no demonstration of a D-Wave quantum annealer outperforming the best available classical solver on an application-decoded QUBO instance of more than 1,000 problem variables will have survived independent classical replication, on the pattern already set by the tensor-network refutation of the Advantage2 spin-glass claim.

## Evidence base

- 28 May 2026: on a greenhouse heater-scheduling QUBO, direct D-Wave QPU runs recovered the exact optimum for H=10 and H=12 but exact-hit rates fell 5/10 to 2/10 to 0/10 at H=14, and the Leap Hybrid BQM workflow did not outperform classical simulated annealing under 15 to 60 second limits; the authors state the results do not indicate quantum advantage.
- 2 June 2026: across 19,775 experiments, D-Wave achieved 7% exact recovery of sparse binary signals at n=32, k=5, m/n=0.19 where AMP and eight other classical solvers scored 0% over 250 combined trials (Fisher exact p=0.018), inside the relaxation gap below the Donoho-Tanner transition; at n=64 embedding overhead limited the QPU.
- 29 May 2026: large-scale Advantage2 Ising spin-glass annealing dynamics previously claimed beyond classical reach were reproduced to state-of-the-art accuracy using lattice-specific tensor networks with belief propagation and modest resources, scalably in 2D and 3D on systems of hundreds of qubits.
- 3 July 2026: a systematic study on a D-Wave Advantage system found that combining forward and reverse annealing consistently improved solution quality and efficiency on Max-Cut, number partitioning and sparse clustering, with gains larger than simply extending annealing time but confined to a narrow parameter regime near freeze-out points.
- 30 June 2026: multi-agent route planning was proved NP-hard by reduction from weighted set packing and solved as a QUBO on Barcelona instances of up to 10,000 vehicles, with D-Wave hybrid solvers evaluated alongside Gurobi and simulated annealing rather than above them.
- 8 May 2026: molecules generated by deep generative models trained with a D-Wave quantum annealer in the loop, using a Neural Hash Function for regularisation and binarisation, showed higher validity and drug-likeness than fully classical equivalents.
- 2 July 2026: the global transverse-field Ising model was shown to simulate arbitrary quantum circuits with polynomial overhead in time, qubit number and energy scale for non-monotonic schedules, though the overheads are large relative to feasible hardware.

## Open questions

- Does the compressed-sensing relaxation-gap advantage survive at n=128 and beyond once embedding overhead is properly accounted for, or does it vanish exactly where it becomes commercially interesting?
- Is the H=14 collapse in the greenhouse benchmark a noise/gap limit intrinsic to analog annealing, or an artefact of the Leap Hybrid BQM workflow and time limits used?
- Can any quantum-annealing dynamics result be shown to resist belief-propagation tensor-network simulation in two and three dimensions, and at what qubit count?
- Do penalty-free encodings and reverse-annealing schedules compound into a scaling improvement, or only shift the constant factor at fixed problem size?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
