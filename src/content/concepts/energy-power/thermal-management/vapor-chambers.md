---
type: concept
slug: vapor-chambers
canonical_name: Vapor Chambers
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- energy-power
- thermal-management
related_concepts: []
companies_using:
- aavid-boyd-corporation
- amec-thermasol
- asia-vital-components-avc
- celsia-technologies
- cooler-chips-coolerchips
- cooler-master
- cooler-systems-international-csi
- delta-electronics
- enertron
- fujikura
- furukawa-electric
- iceotope-technologies
- jentech-precision-industrial
- laird-thermal-systems
- momentive-formerly-henkel-ems-thermal-div
- novark-technologies
- sunonwealth-electric-machine-industry-sunon
- tat-technologies-thermal-division
- thermacore-a-kennametal-company
- thermal-management-technologies-tmt-korea
- tn-nhit-advanced-thermal-tnat
- vaporize-thermal
- wakefield-vette
- wieland-thermal-solutions-formerly-graftech-tmt
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


# Vapor Chambers

*Kind: technology*

## Physics / mechanism

Vapor chambers are planar two-phase heat spreaders. A sealed evacuated cavity contains a small charge of working fluid (typically water, though ethanol or ammonia for lower temps). The evaporator side absorbs localized heat flux, vaporizing the fluid; vapor expands across the cavity and condenses at cooler regions; a sintered-powder, mesh, or micropillar wick structure returns condensate via capillary action. Effective thermal conductivity reaches 10,000–50,000 W/m·K in-plane—20–100× copper. State of the art: sub-0.3 mm total thickness (smartphone-grade), operating heat fluxes >300 W/cm², isothermal spread <2°C ΔT across 100 mm. Key parameters are wick permeability, capillary pressure limit, and vapor-core aspect ratio.

## Competitive landscape

Heat pipes (1D, tubular, lower cost) are the incumbent for many applications. Loop heat pipes offer longer transport distances. Graphite and graphene composite spreaders (anisotropic, k ~700–1500 W/m·K in-plane) are solid-state alternatives with no reliability risk but lower absolute performance. Thermoelectric coolers add active pumping but consume power and are expensive at scale.

## Cloudberry relevance

| Technology | Effective k (W/m·K) | Moving parts / fluid | Cost index |
|---|---|---|---|
| Vapor chamber | 10,000–50,000 | Fluid, passive | Medium |
| Copper heat pipe | 5,000–20,000 | Fluid, passive | Low |
| Graphite composite | 700–1,500 | None | Low–Medium |


Relevance sits at the intersection of advanced packaging and thermal co-design—a chokepoint as chiplet density and photonic integration (co-packaged optics, EIC/PIC stacks) drive die-level heat flux beyond what IHS copper handles. GF's heterogeneous integration roadmap surfaces thermal as a first-class constraint. Deal-flow angles: wick microstructure fabrication (MEMS-adjacent, possible GF process node synergy), novel working fluids, and startups embedding vapor chambers directly into substrate or interposer layers.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
