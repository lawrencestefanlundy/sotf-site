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
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2025-09-17-ai-power-thermal-binding-ai-datacenter-power-demand]]'
- '[[2026-06-17-femtoai-company-profile]]'
- '[[2026-04-28-thermal-stack-arms-race-global-diamond-heat-spreaders]]'
- '[[2026-04-24-thermal-stack-arms-race-global-thermal-management-market-to]]'
- '[[2026-04-10-thermal-stack-arms-race-liquid-cooling-for-ai-data-centers]]'
- '[[2025-12-17-ai-power-thermal-binding-power-availability-remains-the]]'
- '[[2026-03-03-ai-power-thermal-binding-nvidia-vera-rubin-and-feynman]]'
- '[[2024-yole-thermal-management-2024]]'
- '[[2024-02-26-micron-hbm3e-volume-production]]'
- '[[2024-yole-advanced-packaging-2024]]'
- '[[2026-06-17-qualcomm-tenstorrent-talks]]'
- '[[2024-idtechex-thermal-interface-materials-2026-2036]]'
- '[[2026-01-08-semianalysis-apple-tsmc]]'
- '[[2026-06-17-femtoai-spu-ces2026]]'
- '[[2024-tsmc-cowos-roadmap-disclosure]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 83
last_reorg_date: '2026-05-14'
sources_7d: 1
sources_30d: 9
recent_mentions:
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-17-femtoai-company-profile
  title: femtoAI (formerly Femtosense) — company profile, funding, leadership
  date: '2026-06-17'
  kind: web
- slug: 2026-06-17-qualcomm-tenstorrent-talks
  title: Qualcomm in advanced talks to acquire Tenstorrent at $8-10B (reported)
  date: '2026-06-17'
  kind: web
- slug: 2026-06-17-femtoai-spu-ces2026
  title: femtoAI to Highlight its Sparse Processing Unit Edge AI Accelerator at CES 2026
  date: '2026-06-17'
  kind: web
- slug: 2026-04-28-thermal-stack-arms-race-global-diamond-heat-spreaders
  title: Global Diamond Heat Spreaders Emerging for AI Chip Cooling
  date: '2026-04-28'
  kind: web
- slug: 2026-04-24-thermal-stack-arms-race-global-thermal-management-market-to
  title: Global Thermal Management Market to Reach £22bn by 2030, Driven by AI and Data Centres
  date: '2026-04-24'
  kind: web
- slug: 2026-04-10-thermal-stack-arms-race-liquid-cooling-for-ai-data-centers
  title: Liquid Cooling For AI Data Centers Market Growth Analysis - Size and Forecast 2026-2030
  date: '2026-04-10'
  kind: web
- slug: 2026-03-03-ai-power-thermal-binding-nvidia-vera-rubin-and-feynman
  title: NVIDIA Vera Rubin and Feynman roadmap confirmed at GTC 2025 with HBM4 support
  date: '2026-03-03'
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
