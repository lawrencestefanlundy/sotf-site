---
type: concept
slug: advanced-packaging
canonical_name: Advanced Packaging
aliases: []
kind: technology
parent_concepts:
- manufacturing
- packaging
related_concepts: []
sources:
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-03-14-semianalysis-patel-bottlenecks]]'
- '[[2026-05-30-osat-market-structure]]'
- '[[2024-yole-advanced-packaging-2024]]'
- '[[2026-05-30-intel-glass-substrates-program]]'
- '[[2024-tsmc-cowos-roadmap-disclosure]]'
- '[[2025-01-06-asu-selected-as-home-and-partner-for-chips-and-science-act-f]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 90
descendants:
- heterogeneous-integration
- osat
last_reorg_date: '2026-05-13'
sources_7d: 4
sources_30d: 11
recent_mentions:
- slug: 2026-05-30-osat-market-structure
  title: OSAT market structure 2024-2025 — rankings, advanced-packaging split, photonic assembly
  date: '2026-05-30'
  kind: web
- slug: 2026-03-14-semianalysis-patel-bottlenecks
  title: SemiAnalysis (Dylan Patel) — the three shifting bottlenecks to scaling AI compute (logic/litho, memory, power)
  date: '2026-03-14'
  kind: web
- slug: 2026-02-12-how-to-invest-in-ai-sovereignty-sovereign
  title: How to Invest in AI Sovereignty — Sovereign Albion w/ Andrew Bennett
  date: '2026-02-12'
  kind: substack
- slug: 2025-12-19-lfg-for-semiconductors
  title: LFG (for semiconductors)
  date: '2025-12-19'
  kind: substack
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
neighbors: []
---
## Physics / mechanism

Advanced packaging integrates multiple chiplets, dies, or subsystems into a single module by stacking or tiling them with high-density interconnects—bypassing the reticle-size and yield limits of monolithic SoCs. Key mechanisms: 2.5D interposers (silicon or organic) route signals laterally between dies; 3D stacking bonds dies vertically via through-silicon vias (TSVs) or hybrid bonding. Hybrid bonding achieves <1 µm pitch (vs. ~100 µm for flip-chip bumps), cutting interconnect energy to ~0.1 pJ/bit. Bandwidth density reaches 1–10 TB/s/mm² in leading implementations. Key enablers: wafer-level fan-out, die-to-wafer bonding, redistribution layers (RDL). TSMC CoWoS, Intel EMIB/Foveros, Samsung X-Cube, and ASE/Amkor on the OSAT side define the current envelope.

## Competitive landscape

Monolithic scaling (continued 2nm/1.6nm) competes at the process level but hits cost and yield walls above ~200 mm² die area. PCB-level MCMs are the low-density legacy alternative. Key differentiators across approaches:

| Approach | Interconnect pitch | Bandwidth density | Integration flexibility |
|---|---|---|---|
| Hybrid bonding (3D) | <1 µm | >1 TB/s/mm² | Die-to-wafer only |
| Silicon interposer (2.5D) | 10–40 µm | ~100 GB/s/mm² | Heterogeneous mix |
| Organic substrate / fan-out | 2–10 µm | ~10 GB/s/mm² | Cost-optimised |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
