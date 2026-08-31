---
type: concept
slug: foundry-design
canonical_name: Foundry Design
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 1
descendants:
- eda-design-tools
- foundry
- mpw-multi-project-wafer
- pdk-process-design-kit
- specialty-foundries
frontier:
- Does the learned compliant manifold contain devices matching the performance of unconstrained inverse designs, and what is the measured figure-of-merit penalty relative to a penalty-term or filter-based baseline on the same component?
- Does the trained manifold transfer between foundry rule decks with different minimum feature and spacing values, or must a new generative model be trained per process?
- Have manifold-derived designs been fabricated and characterised, with measured DRC clean rates and measured versus simulated spectra reported?
- How does the approach extend beyond planar silicon photonic components to multi-layer stacks, curvilinear rule sets, and non-photonic layouts?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Foundry design in this context is the set of geometric constraints a fabrication facility imposes on submitted layouts: minimum feature size, minimum spacing, and related manufacturability rules that a process can reliably resolve. A layout that violates these rules either fails design rule checking (DRC) at tape-out or is fabricated with geometry that differs materially from the simulated design, breaking the correspondence between predicted and measured performance. In nanophotonics this coupling is acute, because device function derives from sub-wavelength geometry rather than from a discrete circuit netlist.

The tension is sharpest for inverse design, where a topology optimiser is free to distribute material across a pixelated design region to maximise a physical figure of merit. This approach yields ultra-compact and high-performance components, but optimised structures frequently violate constraints on minimum feature size and spacing. Conventional remedies act as post hoc or auxiliary corrections: penalty terms added to the objective, projection and blurring filters applied to the density field, or heuristic binarisation schedules that push grey-scale material distributions towards fabricable two-level geometry. Each restricts the accessible design space, requires extensive hyperparameter tuning, and does not guarantee compliance at every point along the optimisation trajectory.

An alternative is to change the parameterisation rather than the objective. A generative model is trained to span a manifold of DRC-compliant geometries, and optimisation is then performed in the latent coordinates of that manifold, so every candidate evaluated by the electromagnetic solver is compliant by construction. The key parameters shift from filter radii and penalty weights to the expressivity and coverage of the learned manifold: whether it contains the high-performance solutions the unconstrained optimiser would have found, and whether the latent space is smooth enough for gradient-based search.

## Competitive landscape

| Approach | Compliance guarantee | Cost |
| --- | --- | --- |
| Penalty terms in objective | Soft, not enforced during optimisation | Hyperparameter tuning of weights |
| Projection / blurring filters | Approximate, tied to filter radius | Restricts accessible design space |
| Heuristic binarisation schedules | Compliance only near convergence | Schedule tuning; trajectory may be non-compliant |
| Generative manifold reparameterisation | Intrinsic, by construction of the search space | Requires training a generative model of compliant geometries |

The comparison rests on a single source and reflects that work's framing of prior art; independent benchmarking across foundry rule decks is not established by the available material.

## Evidence base

- Enforcing foundry design rules during nanophotonic inverse design is described as a major unsolved challenge, with optimised devices frequently violating minimum feature size and spacing constraints.
- Existing fabrication-constrained methods (penalty terms, projection filters, heuristic binarisation schedules) restrict the accessible design space, require extensive hyperparameter tuning, and often fail to guarantee compliance throughout the optimisation trajectory.
- A framework was introduced that enforces design rules intrinsically by reparameterising the design space with a generative model, restricting optimisation to a learned manifold of DRC-compliant geometries.
- The paradigm was validated on representative silicon photonic components, including broadband power splitters.
- The work was published 2026-02-03 under physics.optics, authored by Emir Salih Magden.

## Frontier (open questions)

- Does the learned compliant manifold contain devices matching the performance of unconstrained inverse designs, and what is the measured figure-of-merit penalty relative to a penalty-term or filter-based baseline on the same component?
- Does the trained manifold transfer between foundry rule decks with different minimum feature and spacing values, or must a new generative model be trained per process?
- Have manifold-derived designs been fabricated and characterised, with measured DRC clean rates and measured versus simulated spectra reported?
- How does the approach extend beyond planar silicon photonic components to multi-layer stacks, curvilinear rule sets, and non-photonic layouts?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
