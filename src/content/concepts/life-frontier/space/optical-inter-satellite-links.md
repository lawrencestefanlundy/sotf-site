---
type: concept
slug: optical-inter-satellite-links
canonical_name: Optical Inter-Satellite Links
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- space
related_concepts: []
companies_using:
- aac-clyde-space-hyperion-technologies
- airbus-defence-and-space-edrs
- bridgecomm
- cailabs
- fibertek
- general-atomics-electromagnetic-systems
- hangzhou-zhongke-microelectronics-hzme
- hensoldt-optronics-formerly-cassidian-optronics
- hyperion-technologies-now-aac-clyde
- laser-light-communications
- leostella
- mynaric
- nict-national-institute-of-information-and-communications-te
- obsidian-sensors
- optical-space-networks-osn
- sa-photonics
- skyloom
- sony-space-communications-division
- space-micro
- spacex-starlink
- tesat-spacecom
- thales-alenia-space
- wuhan-optical-valley-aerospace-information-wovai
- xenesis
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---


# Optical Inter-Satellite Links

*Kind: technology*

## Physics / mechanism

Free-space laser links between satellites. A terminal on each spacecraft points a narrow optical beam (typically 1550 nm, eye-safe, dense with DWDM-compatible infrastructure) at a counterpart. Pointing, acquisition, and tracking (PAT) hardware compensates for relative motion; fine-steering mirrors and fast tip-tilt loops hold beam alignment to sub-microradian precision. No atmosphere means no turbulence penalty at inter-satellite ranges. State of the art: SpaceX Starlink Gen2 terminals run ~100 Gbps per link; Tesat-Spacecom LCT-series have 1.8 Gbps heritage on GEO; NIST/LLCD demonstrated ~622 Mbps lunar distances. Key bottlenecks are PAT latency, SWAP (size, weight, power), and photon-efficient coherent modem integration.

## Competitive landscape

RF crosslinks (Ka/V-band) are the incumbent—mature, omnidirectional, but bandwidth-limited (~1 Gbps realistic) and spectrum-congested. Optical wins on throughput-per-watt and unregulated spectrum but loses on acquisition time and all-weather tolerance (irrelevant in space, critical for ground terminals). Microwave phased arrays offer beamforming flexibility at lower data rates. Quantum key distribution over the same optical terminal is a near-term overlay.

## Cloudberry relevance

| Approach | Throughput | Spectrum licence | Maturity |
|---|---|---|---|
| RF Ka-band crosslink | ~1 Gbps | Required | High |
| Optical ISL (direct detect) | 10–100 Gbps | None | Mid |
| Optical ISL (coherent) | 100 Gbps–1 Tbps | None | Emerging |


Photonic integrated circuits for coherent modems, PAT ASICs, and rad-hard driver electronics are direct semiconductor plays. GF's silicon photonics PDK (45RFSOI, 45CLO) is directly relevant to integrating laser drivers and TIAs at scale. Deal-flow: fabless startups building low-SWAP coherent terminal chips, PAT controller SoCs, or space-qualified PIC foundry services. Lunar Ventures' deep-tech angle and GF-LP fund access to process nodes creates a credible wedge into terminal chipset suppliers before primes vertically integrate.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
