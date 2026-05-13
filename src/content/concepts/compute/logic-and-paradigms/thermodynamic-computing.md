---
type: concept
slug: thermodynamic-computing
canonical_name: Thermodynamic Computing (Extropic, Normal)
aliases: []
kind: technology
parent_concepts:
- compute
- logic-and-paradigms
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
---
## Physics / mechanism

Thermodynamic computing exploits thermal noise—stochastic fluctuations in physical systems—as a computational resource rather than treating it as an error source. Extropic's approach uses analog circuits operating near thermal equilibrium where Boltzmann-distributed states naturally sample probability distributions; Normal Computing's "stochastic processing units" (SPUs) implement matrix operations via thermodynamic fluctuations in electrical networks. Key parameters: energy-per-sample (targeting sub-fJ regimes), convergence time for Langevin dynamics, and signal-to-noise fidelity. The physics grounds in fluctuation-dissipation theorem—noise and dissipation are coupled, so you can do useful work sampling posteriors without the overhead of deterministic arithmetic. Current hardware is pre-production ASIC/FPGA demonstrators; neither company has disclosed volume silicon.

## Competitive landscape

Competes directly with probabilistic/stochastic computing (IBM, MIT probabilistic bits), quantum annealing (D-Wave), and Ising-machine accelerators (Fujitsu DAU, Toshiba SQBM+). Adjacent: analog/neuromorphic (Intel Loihi, BrainScaleS), which also escapes von Neumann overhead but via spiking rather than thermodynamic sampling. Classical GPU/TPU Monte Carlo remains the cost baseline.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
