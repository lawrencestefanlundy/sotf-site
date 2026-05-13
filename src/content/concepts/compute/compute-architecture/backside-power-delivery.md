---
type: concept
slug: backside-power-delivery
canonical_name: Backside Power Delivery (BPD)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- compute-architecture
related_concepts: []
companies_using:
- 3d-micromac
- ansys
- applied-materials
- atomica-formerly-hsg-imit
- besi-be-semiconductor-industries
- brewer-science
- cadence-design-systems
- disco-corporation
- ev-group-evg
- fraunhofer-izm
- imec
- intel
- kulicke-soffa
- lam-research
- pdf-solutions
- pseudolithic
- rapidus
- samsung-foundry
- semsysco
- siemens-eda-mentor
- suss-microtec
- synopsys
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

# Backside Power Delivery (BPD)

*Kind: technology*

## Physics / mechanism

Backside power delivery networks (BSPDN) route VDD/VSS rails through the wafer's back surface rather than the traditional front-side BEOL stack. Conventional frontside PDN consumes 2–4 routing layers and forces a tradeoff between power mesh density and signal routing. BPD separates these concerns: after thinning the wafer to ~10–50 µm, buried power rails (BPR) or through-silicon vias connect to a dedicated backside metal stack. IR-drop improves by ~30–50%; standard cell height can shrink ~10–15% because VDD/VSS rails no longer occupy cell abutment boundaries. Intel's PowerVia (demonstrated 2023) and TSMC's BSPDN (roadmapped for N2P/A16) are the leading implementations. IMEC targets <100 nm BPR pitch at the research level.

## Competitive landscape

Frontside PDN optimisation (wider rails, more meshes) is the incumbent approach but hits physical limits below 3 nm. Buried power rails within the active layer (TSMC N2, Samsung SF2) are a partial solution—less disruptive but smaller benefit. Foveros/SoIC chiplet stacking can redistribute power through the package rather than the die, trading latency for integration flexibility. Direct bonding (Cu-Cu hybrid bonding) enables sub-µm pitch power delivery in 3D stacks and increasingly overlaps with BPD architectures.

## Cloudberry relevance

| Approach | IR-drop gain | Process complexity | Maturity |
|---|---|---|---|
| Frontside PDN optimisation | Baseline | Low | HVM |
| Buried power rails | ~15–20% | Medium | N2/SF2 |
| Full BSPDN | ~30–50% | High | 2025–2026 |


BPD is a foundry-differentiation lever—it determines which fabs can sustain scaling economics past 2 nm. For Cloudberry, the deal-flow angles sit in process equipment (wafer thinning, backside litho alignment), metrology (sub-surface defect inspection), and EDA tooling for co-optimised front/back routing. GlobalFoundries is not a leading-edge scaling player, but portfolio companies building chiplets or advanced packaging on GF nodes need BPD-aware PDN IP and interconnect materials—a direct sourcing conversation.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
