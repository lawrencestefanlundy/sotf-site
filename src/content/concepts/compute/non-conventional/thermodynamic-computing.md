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
- '[[2025-07-14-solving-compute-crisis-physics-based-asics]]'
- '[[2024-10-28-aria-scaling-compute-normal-computing]]'
- '[[2025-08-12-normal-computing-cn101-tape-out]]'
- '[[2023-02-13-thermodynamic-ai-fluctuation-frontier]]'
- '[[2024-01-23-normal-computing-first-thermodynamic-computer]]'
- '[[2025-04-15-nature-comm-thermodynamic-computing-system]]'
mention_count: 10
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2025-08-12-normal-computing-cn101-tape-out
  title: Normal Computing Announces Tape-Out of World's First Thermodynamic Computing Chip
  date: '2025-08-12'
  kind: web
- slug: 2025-07-14-solving-compute-crisis-physics-based-asics
  title: Solving the compute crisis with physics-based ASICs
  date: '2025-07-14'
  kind: web
- slug: 2025-04-15-nature-comm-thermodynamic-computing-system
  title: Thermodynamic computing system for AI applications
  date: '2025-04-15'
  kind: web
- slug: 2024-10-28-aria-scaling-compute-normal-computing
  title: Normal Computing Selected for ARIA's £50M Scaling Compute Programme to Revolutionize AI Hardware Costs
  date: '2024-10-28'
  kind: web
- slug: 2024-01-23-normal-computing-first-thermodynamic-computer
  title: Normal Computing Unveils the First-ever Thermodynamic Computer
  date: '2024-01-23'
  kind: web
- slug: 2023-02-13-thermodynamic-ai-fluctuation-frontier
  title: Thermodynamic AI and the Fluctuation Frontier
  date: '2023-02-13'
  kind: web
neighbors:
- slug: probabilistic-computing
  name: Probabilistic Computing
  path: /compute/non-conventional/probabilistic-computing/
  macro: compute
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: analog-computing
  name: Analog Computing
  path: /compute/non-conventional/analog-computing/
  macro: compute
- slug: neuromorphic-computing
  name: Neuromorphic Computing
  path: /compute/non-conventional/neuromorphic-computing/
  macro: compute
---
a-digital-thermodynamic-computer-for-generative-ai]]'
- '<sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>'
- '<sup class="ref"><a href="https://aria.org.uk/insights/developing-a-world-first-thermodynamic-computing-chip/" title="Normal Computing Selected for ARIA's £50M Scaling Compute Programme to Revolutionize AI Hardware Costs" rel="noopener">ref</a></sup>'
- '<sup class="ref"><a href="https://www.normalcomputing.com/blog/normal-computing-announces-tape-out-of-worlds-first-thermodynamic-computing-chip" title="Normal Computing Announces Tape-Out of World's First Thermodynamic Computing Chip" rel="noopener">ref</a></sup>'
- '<sup class="ref"><a href="https://arxiv.org/abs/2302.06584" title="Thermodynamic AI and the Fluctuation Frontier" rel="noopener">ref</a></sup>'
- '<sup class="ref"><a href="https://www.businesswire.com/news/home/20240123141100/en/Normal-Computing-Unveils-the-First-ever-Thermodynamic-Computer" title="Normal Computing Unveils the First-ever Thermodynamic Computer" rel="noopener">ref</a></sup>'
- '<sup class="ref"><a href="https://www.nature.com/articles/s41467-025-59011-x" title="Thermodynamic computing system for AI applications" rel="noopener">ref</a></sup>'
- ''
- '**Idea Evidence 2026 07 21**'
deal_count: 0
frontier:
- When does the first independent benchmark of a thermodynamic chip running a real
 production workload publish?
- Does the 1000x (Normal) / 10,000x (Extropic) energy-efficiency claim survive contact
 with peer review?
- What is the programming model? Without a CUDA-equivalent, who actually writes software
 for these chips at scale?
- Process node and foundry for CN101 — when does this become public?
- Does the AR + diffusion mixed-architecture trend in frontier labs erode the diffusion-model
 bull case before CN201 ships?
last_updated: '2026-05-27'
tags:
- concept
- technology
- physics-based-asics
- thermodynamic-ai
mention_count: 10
last_reorg_date: '2026-05-27'
---

# Thermodynamic Computing

*Kind: technology · Verified 2026-05-27 against primary sources*

## Physics / mechanism

Thermodynamic computing exploits **stochastic fluctuations in physical systems** as the computational substrate. Rather than enforcing deterministic logic and dissipating energy to suppress thermal noise (as conventional CMOS does), thermodynamic chips engineer the noise itself to perform computation.

The mathematical model is **Langevin dynamics** — stochastic differential equations (SDEs) describing systems under combined deterministic and random forces. The hardware is built to be a direct physical realisation of these equations, so the chip's natural evolution implements the sampling algorithm.

Key grounding: the **fluctuation-dissipation theorem** couples noise and dissipation, so a properly engineered noisy system can do useful Monte Carlo–style sampling work at energy levels far below what's needed to fight noise as an error source.

**Two distinct unit-cell families currently in silicon:**

- **Multi-level continuous-state units** (Normal Computing's "s-units" — 32-bit state variables, see **Normal Computing**). Each unit cell represents a 32-bit continuous state evolving under Langevin dynamics. The Carnot architecture connects tiles of 64 s-units via a network-on-chip.
- **Single-bit probabilistic units (p-bits)** (Extropic's TSU, plus academic Tohoku/Purdue/UCSB work). Each cell fluctuates between binary states at controllable probabilities. Builds Boltzmann-machine sampling natively.

Both target the same workload class — **sampling-heavy AI** (diffusion models, Bayesian inference, energy-based models) plus **stochastic scientific computing** (molecular dynamics, materials simulation). What does not benefit: standard supervised deep learning, matrix multiplication for forward inference of conventional NNs.

## Why now (as of May 2026)

1. **First silicon shipped.** Normal Computing's **CN101** taped out June 2025 (<sup class="ref"><a href="https://www.normalcomputing.com/blog/normal-computing-announces-tape-out-of-worlds-first-thermodynamic-computing-chip" title="Normal Computing Announces Tape-Out of World's First Thermodynamic Computing Chip" rel="noopener">ref</a></sup>); Extropic's **X0** proof-of-concept Q1 2025; Extropic's **Z1** production chip targets early 2026. Both companies have moved from theory to silicon within the same window.
2. **Diffusion-model demand inflection.** Image, video, and 3D generative workloads dominate consumer AI cost. Sampling these distributions on GPUs is the bottleneck thermodynamic chips claim to solve.
3. **Government endorsement.** UK Government's ARIA agency funded Normal Computing UK as 1 of 12 teams in the £100M Scaling Compute programme — explicit goal of 1000x AI hardware cost reduction (<sup class="ref"><a href="https://aria.org.uk/insights/developing-a-world-first-thermodynamic-computing-chip/" title="Normal Computing Selected for ARIA's £50M Scaling Compute Programme to Revolutionize AI Hardware Costs" rel="noopener">ref</a></sup>). Suraj Bramhavar (ARIA programme director, ex-Sync Computing) personally co-authored Normal's coalition paper (<sup class="ref"><a href="https://arxiv.org/abs/2507.10463" title="Solving the compute crisis with physics-based ASICs" rel="noopener">ref</a></sup>).
4. **Strategic-LP money flowing.** Samsung Catalyst Fund led Normal's $50M strategic round March 2026 (<sup class="ref"><a href="https://fortune.com/2026/03/25/normal-computing-raises-50m-from-samsung-catalyst-ai-chip-costs-power-demands/" title="Normal Computing raises $50M led by Samsung Catalyst to accelerate silicon design and solve AI hardware energy crisis" rel="noopener">ref</a></sup>) — signals foundry interest. (Note: process node / foundry partner for CN101 remains undisclosed as of May 2026.)

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
