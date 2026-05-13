---
type: concept
slug: thermoelectric
canonical_name: Thermoelectric
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
- alphabet-energy
- european-thermodynamics
- everredtronics
- evident-thermoelectrics
- ferrotec
- gentherm
- gmz-energy
- hi-z-technology
- ii-vi-marlow-coherent
- kelvin-thermal-energy
- laird-thermal-systems
- micropelt
- nextgen-nano
- perpetua-power-source-technologies
- phononic
- romny-scientific
- savent-technologies
- spark-thermionics
- tecteg-mfr
- tegway
- termo-gen-ab
- thermagon-parker-hannifin-division
- thermotek
ideas_referencing: []
sources:
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 10
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
---


# Thermoelectric

*Kind: technology · Attio deal count: 7*

## Physics / mechanism

Thermoelectrics convert a temperature gradient directly into electrical voltage (Seebeck effect) or drive heat flow using electrical current (Peltier effect). The figure of merit ZT = S²σT/κ governs efficiency, where S is the Seebeck coefficient, σ electrical conductivity, and κ thermal conductivity. Commercial bismuth telluride (Bi₂Te₃) modules sit at ZT ≈ 0.8–1.0, yielding ~5–8% conversion efficiency at ΔT ~200 K. Research materials—half-Heuslers, skutterudites, PbTe alloys, GeTe—push ZT to 1.5–2.5 in lab conditions. Nanostructuring and phonon engineering (grain boundary scattering, rattler atoms) are the dominant levers to suppress κ without degrading σ. Solid-state, no moving parts, long MTBF.

## Competitive landscape


Competing cooling approaches: vapour-compression refrigeration (COP 2–4×, but mechanically complex), heat pipes (passive, no conversion), and phase-change materials (latent heat storage, not active). On the power-generation side, organic Rankine cycles and piezoelectrics compete for waste-heat harvesting at different temperature regimes.

| Approach | Efficiency | Scalability | Moving parts |
|---|---|---|---|
| Thermoelectric | 5–8% | Chip-to-kW | None |
| Vapour-compression | 30–50% (cooling COP) | kW–MW | Yes |
| ORC (waste heat) | 10–20% | kW–MW | Yes |

## Cloudberry relevance
Relevance sits at the semiconductor packaging layer: on-chip Peltier spot-cooling for hotspot management in advanced nodes is a live problem as power densities exceed 100 W/cm². GlobalFoundries-adjacent fabs want monolithic or heterogeneous thermoelectric integration. Deal-flow angles: materials startups targeting thin-film Bi₂Te₃ or CMOS-compatible thermoelectric stacks, and IoT/edge-sensor companies using TEG harvesters to eliminate batteries in harsh-environment deployments.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
