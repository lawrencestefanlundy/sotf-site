---
type: concept
slug: simulation
canonical_name: Simulation
aliases:
- computational simulation
- engineering simulation
- CAE
parent_concepts: []
related_concepts:
- physics-ai
- neural-operators
- plasma-simulation
- machine-learning
sources:
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2023-05-25-interview-ben-mildenhall-co-inventor]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-11-12-atomic-energy-can-nuclear-power-our]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
frontier:
- How much of the classical-solver market does the ML-surrogate layer capture vs sit on top of?
last_updated: 2026-06-22
tags:
- concept
mention_count: 661
descendants:
- neural-operators
- physics-ai
- plasma-simulation
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
  date: '2026-07-10'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-physics-ai-comp-landscape
  title: Physics-AI / ML-surrogate simulation competitive landscape (Zenithon comp set beyond PhysicsX)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-16-cim-landscape-2026
  title: 'Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM'
  date: '2026-06-16'
  kind: web
- slug: 2026-06-16-phasecraft-appointed-by-arpa-e-to-advance-catalyst-simulatio
  title: Phasecraft Appointed by ARPA-E to Advance Catalyst Simulation Frameworks for Hydrogen Electrolysis - Quantum Computing Report
  date: '2026-06-16'
  kind: web
- slug: 2026-06-13-private-fusion-2026-update
  title: Private fusion — 2026 progress update (Helion Polaris D-T, CFS $863M)
  date: '2026-06-13'
  kind: web
neighbors:
- slug: physics-ai
  name: Physics AI
  path: /ai-software/ai-applications/physics-ai/
  macro: ai-software
- slug: neural-operators
  name: Neural Operators
  path: /ai-software/ai-applications/neural-operators/
  macro: ai-software
- slug: plasma-simulation
  name: Plasma Simulation
  path: /ai-software/ai-applications/plasma-simulation/
  macro: ai-software
- slug: machine-learning
  name: Machine Learning
  path: /ai-software/models-inference/machine-learning/
  macro: ai-software
---
Parent concept for computational simulation / CAE — predicting physical-system behaviour numerically (CFD, FEA, multiphysics, plasma) instead of building and testing. The incumbent world is first-principles solvers (**Ansys** now in **Synopsys**, **COMSOL**, Dassault SIMULIA, Altair/Siemens). The disruption is [Physics AI](/ai-software/ai-applications/physics-ai/): [neural-operator](/ai-software/ai-applications/neural-operators/) surrogates that collapse solve time from days to seconds.

Sub-clusters tracked in the KB:
- [Physics AI](/ai-software/ai-applications/physics-ai/) — the ML-surrogate category (the funded wave).
- [Plasma Simulation](/ai-software/ai-applications/plasma-simulation/) — fusion + low-temperature (semiconductor) plasma.
- [Neural Operators](/ai-software/ai-applications/neural-operators/) — the underlying method (DeepONet / FNO / PINN).

Primary deal context: **Zenithon** (Lunar portfolio); landscape in physics ai comp landscape.
