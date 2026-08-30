---
type: concept
slug: neural-operators
canonical_name: Neural Operators
aliases:
- neural operator
- DeepONet
- FNO
- Fourier Neural Operator
- PINN
- physics-informed neural network
- operator learning
parent_concepts:
- physics-ai
related_concepts:
- plasma-simulation
- simulation
- machine-learning
sources: []
frontier:
- Can operator-learning surrogates generalise out-of-distribution (new chemistries/geometries), or do they stay locked to the training distribution?
- Does the architecture commoditise, leaving proprietary training data as the only moat?
last_updated: 2026-06-22
tags:
- concept
mention_count: 36
sources_7d: 0
sources_30d: 8
recent_mentions: []
neighbors:
- slug: plasma-simulation
  name: Plasma Simulation
  path: /ai-software/ai-applications/plasma-simulation/
  macro: ai-software
- slug: simulation
  name: Simulation
  path: /ai-software/ai-applications/simulation/
  macro: ai-software
- slug: machine-learning
  name: Machine Learning
  path: /ai-software/models-inference/machine-learning/
  macro: ai-software
---
The ML method underpinning the [physics-AI](/ai-software/ai-applications/physics-ai/) wave: networks that learn a *mapping between function spaces* (an operator), so a single trained model approximates the solution of a family of PDEs across many inputs, rather than re-solving each case. The two canonical architectures:
- **DeepONet** (deep operator network) — Lu Lu / Karniadakis lineage; a **Zenithon** advisor (Lu Lu) is the pioneer.
- **FNO** (Fourier Neural Operator) — Zongyi Li / Anima Anandkumar lineage; also a Zenithon advisor (Zongyi Li).
- **PINNs** (physics-informed neural networks) — embed the governing equations in the loss; often combined with the above.

## Why it matters competitively
The architectures are increasingly **commodity** (open libraries, published papers). So in the comp landscape, defensibility does **not** come from the neural net — it comes from **proprietary training data** (real calibrated simulator + experimental data) and **domain depth**. This is the core of the **Zenithon Seed To A Strategy** argument and the moat lesson from **Quantemol**.

## The hard limit (out-of-distribution wall)
Neural-operator surrogates interpolate well **in-distribution** and fail outside it; transfer to unseen physical variables has been shown to fail (see zenithon fusion to semiconductor transfer and synthetic data). Since commercial value usually sits in *new* recipes/geometries (= OOD), this is the central technical risk for any surrogate business: mitigated only by dense training-space coverage + calibrated uncertainty quantification.
