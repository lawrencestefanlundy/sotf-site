---
type: concept
slug: high-na-euv-lithography
canonical_name: High-NA EUV Lithography
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- lithography
related_concepts: []
companies_using:
- applied-materials
- asml
- carl-zeiss-smt
- cymer-asml-subsidiary
- entegris
- fraunhofer-iof
- hoya-corporation
- imec
- inpria-jsr-subsidiary
- intel
- jsr-corporation
- kla-corporation
- lam-research
- mentor-siemens-eda
- mycronic
- onto-innovation
- photronics
- samsung-electronics
- shin-etsu-chemical
- synopsys
- tno
- tok-tokyo-ohka-kogyo
- trumpf
- tsmc
ideas_referencing: []
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


# High-NA EUV Lithography

*Kind: technology*

## Physics / mechanism

High-NA EUV lithography increases the numerical aperture of the projection optics from 0.33 (standard EUV) to 0.55, shrinking the minimum half-pitch from ~13 nm to ~8 nm. The optical path uses anamorphic mirrors — 4× demagnification in one axis, 8× in the other — to manage the larger chief-ray angle (up to 17° at mask level) without untenable mask 3D effects. Light source remains 13.5 nm laser-produced tin plasma. ASML's EXE:5000 series is the only commercial platform; first tools shipped to Intel and imec in 2023–24. Throughput is currently ~20 wafers/hour versus ~160 for high-volume standard EUV, with cost-per-wafer roughly 4–5× higher. Stochastic defect budgets and pellicle availability remain unresolved production blockers.

## Competitive landscape

Competing patterning routes for the same pitch range: multi-patterning on standard EUV (SAQP/SADP stacks), directed self-assembly (DSA), and nanoimprint (NIL, Canon). Multi-patterning adds overlay error and process steps but runs on installed base. DSA handles periodic dense patterns but lacks design flexibility. NIL offers low cost-per-wafer but struggles with defectivity and mix-and-match integration.

## Cloudberry relevance

| Approach | Min half-pitch | Throughput | Ecosystem maturity |
|---|---|---|---|
| High-NA EUV | ~8 nm | ~20 wph | Pre-HVM |
| Standard EUV multi-patterning | ~12 nm | ~100+ wph | HVM |
| Nanoimprint (NIL) | ~14 nm | ~80 wph | Niche/display |


Cloudberry's semiconductor focus sits primarily at the enablement layer below leading-edge logic — materials, photonics, packaging — rather than IDM capex. High-NA matters because it cascades demand into resists (high-sensitivity EUV chemistries), pellicle materials (high-transmission membranes), and metrology. Lunar Ventures and Cloudberry both see deal-flow in EUV-adjacent materials and inspection startups where a €5–20M seed is viable; the lithography tool itself is a single-vendor, billion-euro-capex story outside LP fund scope.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
