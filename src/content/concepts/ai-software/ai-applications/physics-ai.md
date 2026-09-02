---
type: concept
slug: physics-ai
canonical_name: Physics AI
aliases:
- physics-AI
- AI-for-simulation
- ML-surrogate simulation
- scientific machine learning
- SciML
parent_concepts:
- simulation
related_concepts:
- neural-operators
- plasma-simulation
- machine-learning
sources:
- '[[2026-06-22-physics-ai-comp-landscape]]'
- '[[2026-09-01-physics-ai-incumbent-consolidation-and-horizontal-repricing]]'
frontier:
- Does the horizontal foundation-physics-model approach (one model, many domains) beat vertical depth, or do the deepest-data verticals (plasma, structural, CFD) stay defensible?
- Which vertical's proprietary calibration-data moat compounds fastest?
last_updated: 2026-09-01
tags:
- concept
descendants:
- neural-operators
mention_count: 7
sources_7d: 1
sources_30d: 3
recent_mentions:
- slug: 2026-09-01-physics-ai-incumbent-consolidation-and-horizontal-repricing
  title: 'Physics AI: the two structural facts — Synopsys closed Ansys, and PhysicsX repriced at ~$2.4B'
  date: '2026-09-01'
  kind: web
- slug: 2026-06-22-physics-ai-comp-landscape
  title: Physics-AI / ML-surrogate simulation competitive landscape (Zenithon comp set beyond PhysicsX)
  date: '2026-06-22'
  kind: web
neighbors:
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
The category of replacing (or accelerating) slow first-principles physics solvers — CFD, FEA, multiphysics, plasma — with **machine-learning surrogate models** (often [neural operators](/ai-software/ai-applications/neural-operators/): DeepONet, FNO, PINN-class) trained against the solver, turning "days/months per simulation" into "seconds per inference." The pitch is the same everywhere: compress the design/test iteration loop in physical engineering.

## The competitive landscape (2026)
**Horizontal platforms** (breadth across aerospace/automotive/materials):
- **PhysicsX** — the category anchor; $300M Series C @ ~$2.4B (June 2026, Temasek), NVIDIA + Siemens backed. CFD-led.
- **Luminary Cloud** — "Physics AI," $72M Series B (Sutter Hill / NVIDIA NVentures); Shift pre-trained models.
- **Neural Concept** — 3D deep-learning surrogates in CAD/sim; $100M Series C (Goldman Sachs Growth).
- **Pasteur Labs** — "simulation intelligence," extreme-physics framing (nuclear/aerospace/defense).
- **Navier** — agentic ML-CFD; the "automate the engineer" wedge.

**Semiconductor-vertical** (where **Zenithon** actually competes):
- **Vinci** (chip design + sim), **Cognichip** (chip design), **SixSense** (fab defect/yield), **SandBox Semiconductor** (etch/dep recipe opt), **Zenithon** (plasma process surrogate).

**Incumbents / displacement target:** **Ansys** (now **Synopsys**), **COMSOL**, **Lam** Semiverse, **Applied Materials** AIx.

## The structural question — the bet lives on **Physics Ai Solver Displacement**

Does a **horizontal foundation physics model** generalise across domains (the PhysicsX / Luminary thesis), or do the **deepest-data verticals** stay defensible because the moat is proprietary calibration data and domain chemistry rather than the neural-net architecture (the Zenithon thesis)? NVIDIA NVentures hedges by backing both sides (PhysicsX, Luminary, Vinci).

**That question, the contractual data-rights argument that turns on it, and the screening tests it implies are now the theme page **Physics Ai Solver Displacement**** — moved there 1 Sep 2026 so this page describes the category and the idea page carries the bet. See also **Zenithon Seed To A Strategy** for the vertical-depth argument as it applies to one company.
