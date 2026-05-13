---
type: concept
slug: backside-power-delivery
canonical_name: Backside Power Delivery (BPD)
aliases: []
kind: technology
parent_concepts:
- compute
- compute-architecture
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

Backside power delivery networks (BSPDN) route VDD/VSS rails through the wafer's back surface rather than the traditional front-side BEOL stack. Conventional frontside PDN consumes 2–4 routing layers and forces a tradeoff between power mesh density and signal routing. BPD separates these concerns: after thinning the wafer to ~10–50 µm, buried power rails (BPR) or through-silicon vias connect to a dedicated backside metal stack. IR-drop improves by ~30–50%; standard cell height can shrink ~10–15% because VDD/VSS rails no longer occupy cell abutment boundaries. Intel's PowerVia (demonstrated 2023) and TSMC's BSPDN (roadmapped for N2P/A16) are the leading implementations. IMEC targets <100 nm BPR pitch at the research level.

## Competitive landscape

Frontside PDN optimisation (wider rails, more meshes) is the incumbent approach but hits physical limits below 3 nm. Buried power rails within the active layer (TSMC N2, Samsung SF2) are a partial solution—less disruptive but smaller benefit. Foveros/SoIC chiplet stacking can redistribute power through the package rather than the die, trading latency for integration flexibility. Direct bonding (Cu-Cu hybrid bonding) enables sub-µm pitch power delivery in 3D stacks and increasingly overlaps with BPD architectures.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
