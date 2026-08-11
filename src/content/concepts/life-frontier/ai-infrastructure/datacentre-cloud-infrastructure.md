---
type: concept
slug: datacentre-cloud-infrastructure
canonical_name: Datacentre & Cloud Infrastructure
aliases: []
kind: market
parent_concepts:
- life-frontier
- ai-infrastructure
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- market
mention_count: 108
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-10-how-ais-demand-for-compute-could-disrupt-america
  title: How AI's Demand for Compute could Disrupt America
  date: '2026-08-10'
  kind: web
- slug: 2026-08-06-the-electrician-shortage-slowing-the-ai-boom---latitude-medi
  title: The electrician shortage slowing the AI boom - Latitude Media
  date: '2026-08-06'
  kind: web
- slug: 2026-08-05-stealthium-gpu-powered-security-intelligence-site-docs-compe
  title: Stealthium — GPU-Powered Security Intelligence (site + docs + competitive context)
  date: '2026-08-05'
  kind: web
- slug: 2026-08-05-which-ldes-companies-are-poised-to-land-the-next-big-contrac
  title: Which LDES companies are poised to land the next big contracts? - Latitude Media
  date: '2026-08-05'
  kind: web
- slug: 2026-08-05-uk-neocloud-landscape-sweep
  title: UK neocloud landscape sweep — filling the coverage gap under the neocloud/serving map
  date: '2026-08-05'
  kind: web
- slug: 2026-08-03-perimeter-compute-wants-to-turn-spare-office-power-into-edge
  title: Perimeter Compute wants to turn spare office power into edge AI data centers - Latitude Media
  date: '2026-08-03'
  kind: web
- slug: 2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-
  title: The Inference Engineering Masterclass — Philip Kiely & Ali Taha, Baseten
  date: '2026-08-03'
  kind: web
- slug: 2026-07-31-memory-optics-packaging-chips-act-targets-ais-compute-bottle
  title: 'Memory, optics, packaging: CHIPS Act targets AI''s compute bottleneck - Electronics360'
  date: '2026-07-31'
  kind: web
neighbors: []
---
## Physics / mechanism

Datacentres are large-scale compute, storage, and networking facilities. Hyperscale operators (AWS, Azure, GCP, Meta, Oracle) dominate, running facilities at 100 MW–1 GW+ per campus. Key parameters: PUE (Power Usage Effectiveness, best-in-class ~1.2), rack density (now routinely 30–60 kW/rack for AI workloads, pushing toward 100+ kW with liquid cooling), bandwidth (400G/800G optical interconnects between switches), and latency (<1 µs intra-rack, ~5 µs cross-fabric). AI inference/training is the dominant growth driver; NVIDIA H100/H200/B200 clusters define the current deployment frontier. Global datacentre power demand is expected to exceed 1,000 TWh annually by 2026.

## Competitive landscape

The primary tension is hyperscale vs. sovereign/edge vs. colocation. Hyperscalers commoditise compute; colocation players (Equinix, Digital Realty) sell interconnection density. Edge computing fragments the model but hasn't displaced core. On the silicon layer: merchant silicon (Broadcom Tomahawk/Jericho) competes with custom ASICs (Google TPU, Microsoft Maia, Amazon Trainium). Cooling: air vs. direct liquid (DLC) vs. immersion—immersion scales better at high rack density but has higher capex and operational friction.

| Layer | Incumbent | Challenger |
|---|---|---|
| Compute | NVIDIA GPU | Custom ASIC / RISC-V accelerator |
| Networking | Broadcom + InfiniBand | Ultra Ethernet Consortium / photonic switching |
| Cooling | CRAC air cooling | Direct liquid / immersion |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
