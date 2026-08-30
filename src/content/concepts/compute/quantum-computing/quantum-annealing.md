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
mention_count: 39
sources_7d: 0
sources_30d: 5
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
The cryogenic member of the Ising-machine family. A quantum annealer encodes a problem as an Ising Hamiltonian across superconducting flux qubits, starts the system in the ground state of a strong transverse field, then slowly turns that field down. If the evolution is slow enough, the adiabatic theorem says the system stays in its ground state and ends up in the ground state of your problem — the answer.

The claimed advantage over classical annealing is **tunnelling**: where a thermal annealer must climb over an energy barrier to escape a local minimum, a quantum system can pass through it. Whether that mechanism delivers a practical speedup on problems anyone cares about has been contested for over a decade, and the contest is not going the technology's way.

## Where it stands

****D Wave Quantum**** is effectively the whole commercial field. Its sixth-generation **Advantage2** (~4,400 qubits) reached general availability in **May 2025**. Reported customer usage of Advantage2 systems grew **314%** year on year.

The scientific story is more turbulent:

- **March 2025** — D-Wave published in *Science*, reporting that Advantage2 simulated the non-equilibrium dynamics of a spin glass faster and more accurately than Oak Ridge's Frontier supercomputer could, with chief scientist Mohammad Amin claiming problems "that cannot be solved classically" ([Physics World](https://physicsworld.com/a/d-wave-systems-claims-quantum-advantage-but-some-physicists-are-not-convinced/), [HPCwire](https://www.hpcwire.com/2025/03/13/d-wave-reports-quantum-supremacy-stirs-immediate-challenge-and-rebuttal/)).
- **Within days** — two independent groups, in Switzerland and the US, posted arXiv preprints reporting the same calculations classically.
- **July 2026** — the Flatiron Institute matched the *Science* paper's spin-glass dynamics using 3D tensor networks with belief propagation, **on a laptop, with open-source software** ([TechTimes](https://www.techtimes.com/articles/321190/20260721/d-wave-said-classical-computers-could-not-match-its-quantum-chip-laptop-just-did.htm)).
- D-Wave has **formally rebutted**, arguing the classical method does not reproduce the full result and that the hardest instances and highest-order measurements remain out of classical reach.

## The honest read

**This is the canonical cautionary tale for the whole Ising-machine field, and it should be read as such rather than as a story about quantum.** A well-funded company with real hardware, real customers and a *Science* paper made a specific advantage claim, and within sixteen months a laptop reproduced it. The pattern — impressive physics demonstration, quiet classical catch-up, receding advantage claim — has now repeated enough times to be the base rate. Anyone underwriting a physical Ising machine ([Coherent Ising Machine](/compute/non-conventional/coherent-ising-machine/), [Stochastic / Ising Machines](/compute/non-conventional/stochastic-ising-machines/), [Thermodynamic Computing](/compute/non-conventional/thermodynamic-computing/)) is betting they escape a pattern that has caught every predecessor.

Note what the strongest surviving claim actually is: the *hardest instances* and *highest-order measurements*. That is a retreat to a narrow technical frontier, not a commercial position. And the demonstration was **spin-glass simulation** — physics, where the hardware is a natural analogue of the problem — not the optimisation problems the machines are sold for.

Two structural points also matter for the room-temperature families, because both cut in their favour:

- **Cryogenics is a genuine cost and integration burden.** ~15 mK dilution refrigerators are why the room-temperature pitch works, and it is the one uncontested advantage its competitors have.
- **Embedding overhead is worse here than anywhere.** D-Wave's qubits are physically connected in a fixed sparse lattice, so a logical problem variable often needs a *chain* of physical qubits to reach its neighbours. Overhead grows severely with connectivity density — dense problems can consume the machine before they are solved. See [Combinatorial Optimisation](/compute/non-conventional/combinatorial-optimisation/).

## Relationship to the neighbours

Same Ising target, different escape mechanism. [Coherent Ising Machine](/compute/non-conventional/coherent-ising-machine/) and oscillator-based machines relax deterministically; [Stochastic / Ising Machines](/compute/non-conventional/stochastic-ising-machines/) and [Thermodynamic Computing](/compute/non-conventional/thermodynamic-computing/) escape minima by thermal sampling; a quantum annealer escapes by tunnelling. The room-temperature families exist substantially because the cryogenic one proved expensive and its advantage proved contestable — which is why every one of their pitches opens by naming D-Wave.

## Evaluation test

1. **Simulation or optimisation?** Spin-glass physics is the home fixture. Commercial optimisation is the away one, and the records differ.
2. **Has a classical method matched it, and how long did that take?** The gap has been shrinking, and the July 2026 result set a new low bar for the effort required.
3. **What did embedding cost?** Logical variables versus physical qubits consumed is the number that reveals whether a demo scales.
4. **Usage or production?** Growth in access hours is not the same as workloads that would be paid for at unsubsidised prices.
