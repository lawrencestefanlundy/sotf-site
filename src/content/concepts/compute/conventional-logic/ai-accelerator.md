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
- '[[2024-yole-advanced-packaging-2024]]'
- '[[2024-idtechex-thermal-interface-materials-2026-2036]]'
- '[[2024-tsmc-cowos-roadmap-disclosure]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 49
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-05-16-ainews-cerebras-60b-ipo-slowly-then-all-at-once
  title: '[AINews] Cerebras'' $60B IPO: Slowly, then All at Once'
  date: '2026-05-16'
  kind: web
- slug: 2026-05-15-weekly-dose-of-optimism-193
  title: 'Weekly Dose of Optimism #193'
  date: '2026-05-15'
  kind: web
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2025-10-29-how-the-worlds-first-flexible-ai-factory-will-work-in-tandem
  title: How the world’s first flexible AI factory will work in tandem with the grid - Latitude Media
  date: '2025-10-29'
  kind: web
- slug: 2025-10-21-frontier-forum-the-new-power-map-for-ai-infrastructure---lat
  title: 'Frontier Forum: The new power map for AI infrastructure - Latitude Media'
  date: '2025-10-21'
  kind: web
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2025-06-25-distinguishing-signal-from-noise-in-the-data-center-market--
  title: Distinguishing signal from noise in the data center market - Latitude Media
  date: '2025-06-25'
  kind: web
- slug: 2025-05-19-us-department-of-commerce-rescinds-biden-administrations-ai-
  title: U.S. Department of Commerce Rescinds Biden Administration’s AI Diffusion Export Control Rule and Issues New Guidance on Huawei, Chips for AI Purposes, and Diligence Expectations - Crowell & Moring LLP
  date: '2025-05-19'
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
