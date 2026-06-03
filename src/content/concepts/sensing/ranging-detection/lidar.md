---
type: concept
slug: lidar
canonical_name: LiDAR
aliases: []
kind: technology
parent_concepts:
- sensing
- ranging-detection
related_concepts: []
sources:
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-05-31-companiesmarketcap]]'
- '[[2026-05-30-companiesmarketcap]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 29
last_reorg_date: '2026-05-13'
sources_7d: 3
sources_30d: 9
recent_mentions:
- slug: 2026-05-31-companiesmarketcap
  title: companiesmarketcap.com
  date: '2026-05-31'
  kind: web
- slug: 2026-05-30-companiesmarketcap
  title: companiesmarketcap.com
  date: '2026-05-30'
  kind: web
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors: []
---
## Physics / mechanism

LiDAR (Light Detection and Ranging) emits pulsed or modulated laser light and measures time-of-flight (ToF) or phase shift of returned photons to reconstruct 3D point clouds. Core variants: mechanical spinning (360° FoV, legacy), MEMS-mirror scanning (miniaturised, lower reliability ceiling), optical phased arrays (OPA, solid-state, CMOS-compatible), and FMCW (frequency-modulated continuous wave, coherent detection, simultaneous velocity via Doppler). Key parameters: range (automotive target ≥200 m), angular resolution (<0.1°), frame rate (>10 Hz), eye-safety class (905 nm vs 1550 nm tradeoffs), and photon detection efficiency. FMCW at 1550 nm is current performance frontier—Aeva, Aurora, Luminar pushing silicon photonics and InGaAs APD/SPAD receiver integration. Point cloud density now >1M points/sec in top-tier systems.

## Competitive landscape

Competing sensing modalities for depth/environment mapping:

| Modality | Range | Resolution | Key weakness |
|---|---|---|---|
| Camera + ML (pseudo-LiDAR) | Unbounded | High 2D, depth inferred | Depth accuracy degrades, lighting-dependent |
| Radar (77 GHz / 4D imaging) | >300 m | Low angular | No fine geometry, poor object classification |
| Structured light / ToF camera | <10 m | Medium | Short range, sunlight interference |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
