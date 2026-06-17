---
type: concept
slug: ai-accelerator
canonical_name: AI Accelerator
aliases: []
kind: technology
parent_concepts:
- compute
- conventional-logic
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2024-yole-emerging-memories-2024]]'
- '[[2024-yole-thermal-management-2024]]'
- '[[2024-02-26-micron-hbm3e-volume-production]]'
- '[[2024-yole-advanced-packaging-2024]]'
- '[[2024-idtechex-thermal-interface-materials-2026-2036]]'
- '[[2026-01-08-semianalysis-apple-tsmc]]'
- '[[2024-tsmc-cowos-roadmap-disclosure]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 72
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 4
recent_mentions:
- slug: 2026-01-08-semianalysis-apple-tsmc
  title: 'Apple-TSMC: The Partnership That Built Modern Semiconductors'
  date: '2026-01-08'
  kind: web
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2024-yole-advanced-packaging-2024
  title: Yole Group — Advanced Packaging 2024 Market Analysis
  date: '2024-12-01'
  kind: web
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
- slug: 2024-yole-thermal-management-2024
  title: Yole Group — Thermal Management 2024 Market Analysis
  date: '2024-10-01'
  kind: web
neighbors: []
---
## Physics / mechanism

Dedicated silicon (or silicon-adjacent) die optimised for the tensor/matrix operations that dominate neural-network workloads. Core mechanism: replace von-Neumann memory-bandwidth bottlenecks with massive parallelism — thousands of MAC units operating concurrently on weight matrices. Key architectural levers are on-chip SRAM capacity (TSMC N3/N4 designs now carry 100–200 MB on-die), interconnect bandwidth (HBM3e at ~1.2 TB/s per stack), and compute density (H100 at ~4 petaFLOPS BF16, Trainium2 at ~3.5 petaFLOPS). The frontier is moving from monolithic GPU dies toward chiplet-based disaggregation (AMD MI300X, Intel Gaudi 3) and wafer-scale integration (Cerebras WSE-3 at 900K cores, 44 GB on-wafer SRAM). Process nodes: bleeding-edge training silicon is on TSMC 3/4nm; inference increasingly targets mature nodes (16/28nm) for cost.

## Competitive landscape

Nvidia GPU dominates training (~80% market share by revenue). Competing vectors: custom ASICs (Google TPU v5, AWS Trainium, Meta MTIA) for hyperscaler captive workloads; inference-optimised chips (Groq LPU, Tenstorrent, Hailo, Axelera) targeting edge and cloud inference; analog/in-memory compute (Mythic, Syntiant) for ultra-low-power edge. Photonic accelerators (Lightmatter, Luminous) remain pre-revenue but claim 10–100× energy efficiency for specific linear-algebra kernels.

| Axis | GPU (Nvidia) | Custom ASIC | Photonic |
|---|---|---|---|
| Flexibility | High | Low | Very low |
| Power efficiency | Moderate | High | Potentially extreme |
| Maturity | Production | Production (captive) | Pre-commercial |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
