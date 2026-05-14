---
type: concept
slug: gw-scale-power-delivery
canonical_name: GW-Scale Power Delivery (HVDC, sub-station to rack)
aliases: []
kind: technology
parent_concepts:
- energy-power
- power-electronics
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
recent_mentions: []
neighbors: []
---
## Physics / mechanism

HVDC transmission moves bulk power at ±320–800 kV DC, cutting resistive losses to ~3% per 1,000 km versus ~7% for HVAC equivalents. At the hyperscale campus level, medium-voltage DC (MVDC) distribution at 6–24 kV feeds campus substations; from there, 480 V AC or 400 V DC bus architectures deliver to rack. Modern rack power density has crossed 100 kW (liquid-cooled GPU clusters) with roadmaps to 200–300 kW by 2027. The critical loss budget runs: transmission → step-down transformer → switchgear → UPS/rectifier → PDU → VRM, each stage adding 1–3% loss. End-to-end efficiency from grid to silicon is typically 85–90%; every point recovered at GW scale is tens of MW of avoided capacity.

## Competitive landscape

---

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
