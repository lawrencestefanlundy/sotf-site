---
type: concept
slug: datacentre-cloud-infrastructure
canonical_name: Datacentre & Cloud Infrastructure
aliases: []
kind: market
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- ai-infrastructure
related_concepts: []
companies_using:
- amazon-web-services-aws
- amazon-web-services
- amd
- arista-networks
- beeks-group
- celestica
- coreweave
- crusoe-energy
- datavita
- delta-electronics
- equinix
- exaion-edf-subsidiary
- exodigo
- gcore
- google-cloud
- gridline-formerly-arcus-power
- hetzner-online
- iceotope
- intel
- koios-formerly-datacenterlight
- liqid
- microsoft-azure
- nvidia
- ori-industries
- oriole-networks
- ovhcloud
- oxide-computer-company
- oxide-computer
- phaidra
- quanta-cloud-technology-qct
- scaleway
- submer
- supermicro-super-micro-computer
- swan-computing
- vast-data
- vertiv
- virtual-cable-uds-enterprise
- vultr
- weka
ideas_referencing: []
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
sources_30d: 3
---

# Datacentre & Cloud Infrastructure

*Kind: market · Attio deal count: 108*

## Physics / mechanism

Datacentres are large-scale compute, storage, and networking facilities. Hyperscale operators (AWS, Azure, GCP, Meta, Oracle) dominate, running facilities at 100 MW–1 GW+ per campus. Key parameters: PUE (Power Usage Effectiveness, best-in-class ~1.2), rack density (now routinely 30–60 kW/rack for AI workloads, pushing toward 100+ kW with liquid cooling), bandwidth (400G/800G optical interconnects between switches), and latency (<1 µs intra-rack, ~5 µs cross-fabric). AI inference/training is the dominant growth driver; NVIDIA H100/H200/B200 clusters define the current deployment frontier. Global datacentre power demand is expected to exceed 1,000 TWh annually by 2026.

## Competitive landscape


The primary tension is hyperscale vs. sovereign/edge vs. colocation. Hyperscalers commoditise compute; colocation players (Equinix, Digital Realty) sell interconnection density. Edge computing fragments the model but hasn't displaced core. On the silicon layer: merchant silicon (Broadcom Tomahawk/Jericho) competes with custom ASICs (Google TPU, Microsoft Maia, Amazon Trainium). Cooling: air vs. direct liquid (DLC) vs. immersion—immersion scales better at high rack density but has higher capex and operational friction.

| Layer | Incumbent | Challenger |
|---|---|---|
| Compute | NVIDIA GPU | Custom ASIC / RISC-V accelerator |
| Networking | Broadcom + InfiniBand | Ultra Ethernet Consortium / photonic switching |
| Cooling | CRAC air cooling | Direct liquid / immersion |

## Cloudberry relevance
Cloudberry's angle is the enabling layer, not the datacentre itself. Co-packaged optics, silicon photonics interconnects, and GaN/SiC power conversion are the high-value insertion points where deep-tech semi portfolio companies land. GlobalFoundries' 45RFSOI and photonics PDK make it a natural fab partner for optical transceiver and LiDAR-adjacent startups entering the datacentre interconnect market. Compute density pressure is a durable demand signal for advanced packaging and chiplet plays in the Cloudberry pipeline.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
