---
type: concept
slug: thermoelectric
canonical_name: Thermoelectric
aliases: []
kind: technology
parent_concepts:
- energy-power
- ai-thermal-management
related_concepts: []
sources:
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 23
last_reorg_date: '2026-05-13'
sources_7d: 2
sources_30d: 7
recent_mentions:
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
neighbors: []
---
## Physics / mechanism

Thermoelectrics convert a temperature gradient directly into electrical voltage (Seebeck effect) or drive heat flow using electrical current (Peltier effect). The figure of merit ZT = S²σT/κ governs efficiency, where S is the Seebeck coefficient, σ electrical conductivity, and κ thermal conductivity. Commercial bismuth telluride (Bi₂Te₃) modules sit at ZT ≈ 0.8–1.0, yielding ~5–8% conversion efficiency at ΔT ~200 K. Research materials—half-Heuslers, skutterudites, PbTe alloys, GeTe—push ZT to 1.5–2.5 in lab conditions. Nanostructuring and phonon engineering (grain boundary scattering, rattler atoms) are the dominant levers to suppress κ without degrading σ. Solid-state, no moving parts, long MTBF.

## Competitive landscape

Competing cooling approaches: vapour-compression refrigeration (COP 2–4×, but mechanically complex), heat pipes (passive, no conversion), and phase-change materials (latent heat storage, not active). On the power-generation side, organic Rankine cycles and piezoelectrics compete for waste-heat harvesting at different temperature regimes.

| Approach | Efficiency | Scalability | Moving parts |
|---|---|---|---|
| Thermoelectric | 5–8% | Chip-to-kW | None |
| Vapour-compression | 30–50% (cooling COP) | kW–MW | Yes |
| ORC (waste heat) | 10–20% | kW–MW | Yes |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
