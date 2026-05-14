---
type: concept
slug: optical-inter-satellite-links
canonical_name: Optical Inter-Satellite Links
aliases: []
kind: technology
parent_concepts:
- life-frontier
- in-orbit
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Free-space laser links between satellites. A terminal on each spacecraft points a narrow optical beam (typically 1550 nm, eye-safe, dense with DWDM-compatible infrastructure) at a counterpart. Pointing, acquisition, and tracking (PAT) hardware compensates for relative motion; fine-steering mirrors and fast tip-tilt loops hold beam alignment to sub-microradian precision. No atmosphere means no turbulence penalty at inter-satellite ranges. State of the art: SpaceX Starlink Gen2 terminals run ~100 Gbps per link; Tesat-Spacecom LCT-series have 1.8 Gbps heritage on GEO; NIST/LLCD demonstrated ~622 Mbps lunar distances. Key bottlenecks are PAT latency, SWAP (size, weight, power), and photon-efficient coherent modem integration.

## Competitive landscape

RF crosslinks (Ka/V-band) are the incumbent—mature, omnidirectional, but bandwidth-limited (~1 Gbps realistic) and spectrum-congested. Optical wins on throughput-per-watt and unregulated spectrum but loses on acquisition time and all-weather tolerance (irrelevant in space, critical for ground terminals). Microwave phased arrays offer beamforming flexibility at lower data rates. Quantum key distribution over the same optical terminal is a near-term overlay.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
