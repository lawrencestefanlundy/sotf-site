---
type: concept
slug: networking-wireless
canonical_name: Networking & Wireless
aliases: []
kind: technology
parent_concepts:
- communications
- wireless
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 12
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Wireless communication encodes information onto electromagnetic carriers via modulation (AM/FM/QAM/OFDM), propagating through free space or guided media. Key parameters: carrier frequency (GHz–THz), bandwidth (MHz–GHz), spectral efficiency (bits/s/Hz), link budget (EIRP, path loss, noise figure), and latency. Wi-Fi 7 (802.11be) delivers ~46 Gbps theoretical via 320 MHz channels and multi-link operation. 5G NR (FR2, mmWave) hits ~4 Gbps peak but suffers severe path loss above 28 GHz, demanding dense small-cell deployment. 6G targets sub-THz bands (100–300 GHz), sub-ms latency, and integrated sensing+comms. Antenna count (massive MIMO, 64–256 elements) and beamforming DSP are now primary performance levers.

## Competitive landscape

5G/NR mmWave, Wi-Fi 7, and UWB compete directly for indoor/short-range high-throughput use cases. Satellite constellations (Starlink, OneWeb) address wide-area low-latency differently. At the component level: GaAs/GaN RF front-ends (Skyworks, Qorvo) vs. bulk CMOS RF (MediaTek, Qualcomm) trade efficiency for integration. Sub-THz links compete with FSO (free-space optical) for last-mile backhaul.

| Approach | Throughput | Range | Integration cost |
|---|---|---|---|
| mmWave 5G (28/39 GHz) | ~4 Gbps | 100–300 m | High (GaN FEM) |
| Wi-Fi 7 (6 GHz) | ~10 Gbps indoor | <50 m | Medium (CMOS) |
| Sub-THz (100–300 GHz) | >100 Gbps (lab) | <10 m | Emerging (InP/SiGe) |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
