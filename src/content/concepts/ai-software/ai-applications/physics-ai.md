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
frontier:
- Does the horizontal foundation-physics-model approach (one model, many domains) beat vertical depth, or do the deepest-data verticals (plasma, structural, CFD) stay defensible?
- Which vertical's proprietary calibration-data moat compounds fastest?
last_updated: 2026-08-07
tags:
- concept
descendants:
- neural-operators
mention_count: 6
sources_7d: 0
sources_30d: 2
recent_mentions:
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

## The structural question
The bet that divides the field: does a **horizontal foundation physics model** generalise across domains (the PhysicsX/Luminary thesis), or do the **deepest-data verticals** stay defensible because the moat is proprietary calibration data + domain chemistry, not the neural-net architecture (the Zenithon thesis)? NVIDIA NVentures hedges by backing both sides (PhysicsX, Luminary, Vinci). See **Zenithon Seed To A Strategy** for the vertical-depth argument.

## The unasked question: who is contractually allowed to hold the calibration data (added 7 Aug 2026)

If the vertical thesis is right and the moat is proprietary calibration data, then the binding constraint is **contractual, not technical** — and the field mostly does not price it. In semiconductor fabs the default is that the customer keeps everything: **Pdf Solutions** paid $130M for **secureWISE**, a zero-trust layer used by 100+ equipment vendors across 190+ fabs, built precisely so vendors can touch tools without keeping data. Ownership is not the issue; *use rights* are — broad cross-customer training rights are the clause counsel strikes, and strikes hardest for the best customers.

- **Dataset size must be read against the parameter space.** A dataset that is tiny relative to the claimed combinatorial space means the moat is the physics encoding, not the data — and the company cannot claim both.
- **Neutrality is the real counter-position.** **Applied Materials** and **Lam Research** cannot pool data across competing fabs because they sell to all of them; a small neutral vendor sometimes can win rights a giant cannot. That advantage has a clock on it — new-material fabs have not yet priced these rights.