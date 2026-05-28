---
type: concept
slug: thermodynamic-computing
canonical_name: Thermodynamic Computing
aliases:
- Physics-Based ASICs
- Thermodynamic AI
- Stochastic Processing
kind: technology
parent_concepts:
- compute
- non-conventional
related_concepts:
- probabilistic-computing
- stochastic-ising-machines
- analog-computing
- neuromorphic-computing
sources:
- '[[2023-02-13-thermodynamic-ai-fluctuation-frontier]]'
- '[[2024-01-23-normal-computing-first-thermodynamic-computer]]'
- '[[2024-10-28-aria-scaling-compute-normal-computing]]'
- '[[2025-04-15-nature-comm-thermodynamic-computing-system]]'
- '[[2025-07-14-solving-compute-crisis-physics-based-asics]]'
- '[[2025-08-12-normal-computing-cn101-tape-out]]'
- '[[2026-03-25-normal-computing-samsung-catalyst-50m]]'
frontier:
- When does the first independent benchmark of a thermodynamic chip running a real production workload publish?
- Does the 1000x (Normal) / 10,000x (Extropic) energy-efficiency claim survive contact with peer review?
- What is the programming model? Without a CUDA-equivalent, who actually writes software for these chips at scale?
- Process node and foundry for CN101 — when does this become public?
- Does the AR + diffusion mixed-architecture trend in frontier labs erode the diffusion-model bull case before CN201 ships?
last_updated: '2026-05-27'
tags:
- concept
- technology
- physics-based-asics
- thermodynamic-ai
mention_count: 0
last_reorg_date: '2026-05-27'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: probabilistic-computing
  name: Probabilistic Computing
  path: /sotf-site/compute/non-conventional/probabilistic-computing/
  macro: compute
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /sotf-site/compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: analog-computing
  name: Analog Computing
  path: /sotf-site/compute/non-conventional/analog-computing/
  macro: compute
- slug: neuromorphic-computing
  name: Neuromorphic Computing
  path: /sotf-site/compute/non-conventional/neuromorphic-computing/
  macro: compute
---
*Verified 2026-05-27 against primary sources*

## Physics / mechanism

Thermodynamic computing exploits **stochastic fluctuations in physical systems** as the computational substrate. Rather than enforcing deterministic logic and dissipating energy to suppress thermal noise (as conventional CMOS does), thermodynamic chips engineer the noise itself to perform computation.

The mathematical model is **Langevin dynamics** — stochastic differential equations (SDEs) describing systems under combined deterministic and random forces. The hardware is built to be a direct physical realisation of these equations, so the chip's natural evolution implements the sampling algorithm.

Key grounding: the **fluctuation-dissipation theorem** couples noise and dissipation, so a properly engineered noisy system can do useful Monte Carlo–style sampling work at energy levels far below what's needed to fight noise as an error source.

**Two distinct unit-cell families currently in silicon:**

- **Multi-level continuous-state units** (Normal Computing's "s-units" — 32-bit state variables, see **Normal Computing**). Each unit cell represents a 32-bit continuous state evolving under Langevin dynamics. The Carnot architecture connects tiles of 64 s-units via a network-on-chip.
- **Single-bit probabilistic units (p-bits)** (Extropic's TSU, plus academic Tohoku/Purdue/UCSB work). Each cell fluctuates between binary states at controllable probabilities. Builds Boltzmann-machine sampling natively.

Both target the same workload class — **sampling-heavy AI** (diffusion models, Bayesian inference, energy-based models) plus **stochastic scientific computing** (molecular dynamics, materials simulation). What does not benefit: standard supervised deep learning, matrix multiplication for forward inference of conventional NNs.

## Why now (as of May 2026)

1. **First silicon shipped.** Normal Computing's **CN101** taped out June 2025 (**2025 08 12 Normal Computing Cn101 Tape Out**); Extropic's **X0** proof-of-concept Q1 2025; Extropic's **Z1** production chip targets early 2026. Both companies have moved from theory to silicon within the same window.
2. **Diffusion-model demand inflection.** Image, video, and 3D generative workloads dominate consumer AI cost. Sampling these distributions on GPUs is the bottleneck thermodynamic chips claim to solve.
3. **Government endorsement.** UK Government's ARIA agency funded Normal Computing UK as 1 of 12 teams in the £100M Scaling Compute programme — explicit goal of 1000x AI hardware cost reduction (**2024 10 28 Aria Scaling Compute Normal Computing**). Suraj Bramhavar (ARIA programme director, ex-Sync Computing) personally co-authored Normal's coalition paper (**2025 07 14 Solving Compute Crisis Physics Based Asics**).
4. **Strategic-LP money flowing.** Samsung Catalyst Fund led Normal's $50M strategic round March 2026 (**2026 03 25 Normal Computing Samsung Catalyst 50M**) — signals foundry interest. (Note: process node / foundry partner for CN101 remains undisclosed as of May 2026.)

## Competitive landscape

| Approach | Companies | Energy claim | Maturity | Target workload |
|---|---|---|---|---|
| **Thermodynamic continuous-state** | **Normal Computing** | ~1000x vs GPU (press); "orders of magnitude" (their technical blog) | CN101 silicon June 2025; CN201 2026 | Diffusion, Bayesian inference, matrix inversion |
| **Thermodynamic / p-bit single-state (TSU)** | **Extropic** | ~10,000x vs GPU (system-level analysis) | X0 proof Q1 2025; Z1 production early 2026 | Image / video generation, robotics control |
| **CMOS p-bit (academic)** | Tohoku / Purdue / Aalto labs | ~1 fJ/op at room temp | ~1k p-bit research chips | Combinatorial optimisation, Bayesian sampling |
| **Quantum annealing** | D-Wave | μJ range with cryo overhead | Commercial, >5000 qubits | Combinatorial optimisation |
| **Classical Ising / annealer** | Fujitsu DAU, Hitachi CMOS annealer, Toshiba SQBM+ | n/a | Commercial | QUBO / Ising-form optimisation |
| **Neuromorphic / spiking** | Intel Loihi, BrainScaleS, SynSense | Varies | Research / pilot | Event-driven inference |
| **GPU Monte Carlo (baseline)** | NVIDIA, AMD | pJ/op, mature toolchain | TRL 9 | General ML sampling |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- When does the **first independent benchmark** of a thermodynamic chip running a real production workload publish?
- Does the 1000x (Normal) / 10,000x (Extropic) **energy-efficiency claim survive peer review** on a non-cherry-picked workload?
- What is the **programming model**? Without a CUDA-equivalent, who actually writes software for these chips at scale? PyTorch backend, dedicated compiler, or domain-specific stack?
- **Process node and foundry** for CN101 — when does this become public, and does it implicate Samsung Foundry given the Catalyst lead?
- Does the **AR + diffusion mixed-architecture trend** in frontier labs erode the diffusion-model bull case before CN201 ships?
- Two thermodynamic startups raising in 2026 — **category emergence or fashion cycle**?

*Concept page rewritten 2026-05-27 against primary sources. Previous content was Sonnet-auto-mapped 2026-05-04 and contained inaccuracies (described Normal's units as "SPUs" — that's the older PCB prototype; the silicon architecture is Carnot with "s-units"; said neither company had "disclosed volume silicon" — outdated since CN101 tape-out August 2025).*
