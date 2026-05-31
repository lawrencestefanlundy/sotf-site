---
type: concept
slug: physics-native-compute
canonical_name: Physics-Native Compute
aliases:
- physics-based ASIC
- physics-as-compute
- substrate-class compute
kind: category
parent_concepts:
- compute-paradigms
- non-conventional-computing
related_concepts:
- coherent-ising-machine
- stochastic-ising-machines
- thermodynamic-computing
- probabilistic-computing
- neuromorphic-computing
- analog-computing
- memristors
- reversible-computing
- coupled-oscillator-networks
sources: []
frontier:
- Which substrate class (deterministic CIM, stochastic p-bit, thermodynamic, neuromorphic) ships chip-integrable production silicon first?
- Does the Litman 2025 SDPA-EOT result drive convergent positioning across substrate classes around transformer inference primitives?
- Which compiler stack (MLIR, TVM, IREE) becomes the canonical front-end for physics-native hardware?
- Does mature-foundry-positioning hold as a structural edge once Cerebras / Nvidia free CoWoS allocation in 2027?
last_updated: '2026-05-27'
tags:
- concept
- category
- compute
- non-conventional
- ising-machine
- thermodynamic
- neuromorphic
descendants:
- coupled-oscillator-networks
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: coherent-ising-machine
  name: Coherent Ising Machine
  path: /sotf-site/compute/non-conventional/coherent-ising-machine/
  macro: compute
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /sotf-site/compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: thermodynamic-computing
  name: Thermodynamic Computing
  path: /sotf-site/compute/non-conventional/thermodynamic-computing/
  macro: compute
- slug: probabilistic-computing
  name: Probabilistic Computing
  path: /sotf-site/compute/non-conventional/probabilistic-computing/
  macro: compute
- slug: neuromorphic-computing
  name: Neuromorphic Computing
  path: /sotf-site/compute/non-conventional/neuromorphic-computing/
  macro: compute
- slug: analog-computing
  name: Analog Computing
  path: /sotf-site/compute/non-conventional/analog-computing/
  macro: compute
- slug: memristors
  name: Memristors
  path: /sotf-site/compute/non-conventional/memristors/
  macro: compute
- slug: reversible-computing
  name: Reversible Computing
  path: /sotf-site/compute/non-conventional/reversible-computing/
  macro: compute
- slug: coupled-oscillator-networks
  name: Coupled Oscillator Networks
  path: /sotf-site/compute/non-conventional/coupled-oscillator-networks/
  macro: compute
---
The umbrella category. Hardware where **the physics of the substrate, not arithmetic on a digital processor, does the computation**. The user encodes a problem into the substrate's energy landscape, applies an input, and reads the answer out after the substrate has relaxed (or sampled). No iteration in software. No CUDA-equivalent. The chip *is* the algorithm.

## Substrate-class taxonomy

Four families sit under this umbrella. Each implements energy-minimisation (or distribution-sampling) in a different physical medium.

Adjacent substrate-classes (different physics, similar architectural inversion):

| Family | Dynamics | KB concept |
|---|---|---|
| Memristive analog matmul | In-memory matrix multiplication via conductance crossbar | [Memristors](/sotf-site/compute/non-conventional/memristors/) |
| Reversible / adiabatic | Computation without energy dissipation (Landauer limit) | [Reversible Computing](/sotf-site/compute/non-conventional/reversible-computing/) |
| Photonic analog | Optical interference for matmul or Ising | (in [Analog Computing](/sotf-site/compute/non-conventional/analog-computing/)) |
| Quantum annealing | Tunneling through energy barriers in superconducting qubits | (in `quantum-computing/` folder) |

## What unites them

## What distinguishes them from digital AI accelerators

Cerebras, Groq, H100 still iterate arithmetically. They run the *same algorithm* faster. Physics-native compute runs a *different algorithm* — physics does the work. Different category. The architectural inversion is the moat (or the failure mode, depending on whether the calibration loop dominates the speed budget).

Pre-seed and seed deals in this category are still rare enough that:
- Substrate-class first-mover gets a category-defining position
- The mature-foundry path (90nm, 130nm, 65nm, GF 22FDX) is uncrowded — see [Mature Foundry Positioning](/sotf-site/compute/compute-architecture/mature-foundry-positioning/)
- The compiler-build risk is structural across the category; teams that solve it first win disproportionately
- Strategic acquirers exist at each substrate-class transition (Lightmatter for analog photonic, NTT for CIM, Cerebras / Groq for AI inference primitive, Cadence / Synopsys for EDA-side optimisation)

## Sources

<!-- dataview block stripped for public site -->
