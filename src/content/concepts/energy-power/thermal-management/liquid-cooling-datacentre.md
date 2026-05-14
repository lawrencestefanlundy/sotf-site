---
type: concept
slug: liquid-cooling-datacentre
canonical_name: Liquid Cooling at Datacentre Scale
aliases: []
kind: technology
parent_concepts:
- energy-power
- ai-thermal-management
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

Liquid cooling removes heat by circulating fluid directly to or near heat sources, exploiting water's ~3,500× higher volumetric heat capacity versus air. Three dominant architectures: cold-plate (direct-to-chip, coolant never contacts silicon), single-phase immersion (dielectric fluid bath, servers submerged, fluid remains liquid), and two-phase immersion (dielectric boils at chip surface, latent heat of vaporisation does heavy lifting, vapour recondenses and returns). Cold-plate systems handle 100–200 kW/rack routinely; two-phase immersion can manage 250+ kW/rack with PUE approaching 1.03. Key parameters: thermal resistance (junction-to-coolant), dielectric fluid GWP, pump OPEX, and compatibility with existing server OEM warranties. Hyperscalers (Meta, Microsoft, Google) and co-lo operators are deploying at scale; Vertiv, Coolit, LiquidStack, and Asetek lead hardware supply.

## Competitive landscape

Air cooling is the incumbent—cheap, familiar, no leak risk, but hard-capped around 30–50 kW/rack and breaking down fast as GPU TDPs exceed 700 W per accelerator. Rear-door heat exchangers are a half-measure bridge. Thermoelectric cooling (Peltier) is niche, low-efficiency. Microfluidic on-package cooling (TSMC, Intel research) is the emerging frontier—cooling integrated at wafer level, blurring the line between packaging and thermal management. Comparison:

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
