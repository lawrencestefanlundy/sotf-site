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
sources_30d: 1
recent_mentions:
- slug: 2026-04-09-the-rise-of-flexible-data-centers---latitude-media
  title: The rise of flexible data centers - Latitude Media
  date: '2026-04-09'
  kind: web
- slug: 2025-10-29-how-the-worlds-first-flexible-ai-factory-will-work-in-tandem
  title: How the world’s first flexible AI factory will work in tandem with the grid - Latitude Media
  date: '2025-10-29'
  kind: web
- slug: 2025-10-21-frontier-forum-the-new-power-map-for-ai-infrastructure---lat
  title: 'Frontier Forum: The new power map for AI infrastructure - Latitude Media'
  date: '2025-10-21'
  kind: web
- slug: 2025-09-16-the-case-against-relying-on-behind-the-meter-power-for-data-
  title: The case against relying on behind-the-meter power for data centers - Latitude Media
  date: '2025-09-16'
  kind: web
- slug: 2025-09-08-a-status-update-on-data-center-flexibility---latitude-media
  title: A status update on data center flexibility - Latitude Media
  date: '2025-09-08'
  kind: web
- slug: 2025-06-25-distinguishing-signal-from-noise-in-the-data-center-market--
  title: Distinguishing signal from noise in the data center market - Latitude Media
  date: '2025-06-25'
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
