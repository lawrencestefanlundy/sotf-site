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
- slug: 2026-06-11-amazon-finally-reports-its-annual-water-use-at-data-centers-
  title: Amazon — finally — reports its annual water use at data centers - Latitude Media
  date: '2026-06-11'
  kind: web
- slug: 2026-06-08-google-buys-compute-from-spacex-broadcoms-outlook-apples-ai-
  title: Google Buys Compute From SpaceX, Broadcom’s Outlook, Apple’s AI Politics
  date: '2026-06-08'
  kind: web
- slug: 2026-04-09-wi-fi-7-orders-set-to-overtake-wi-fi-6-as-businesses-upgrade
  title: Wi-Fi 7 orders set to overtake Wi-Fi 6 as businesses upgrade networks - digitimes
  date: '2026-04-09'
  kind: web
- slug: 2026-03-19-worldwide-enterprise-wlan-grew-139-driven-by-wi-fi-7-deploym
  title: Worldwide enterprise WLAN grew 13.9% driven by Wi-Fi 7 deployments - International Data Corporation
  date: '2026-03-19'
  kind: web
- slug: 2026-02-10-uk-chip-startup-fractile-to-expand-uk-operations-with-100m-i
  title: UK chip startup Fractile to expand UK operations with £100m investment - Data Center Dynamics
  date: '2026-02-10'
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
