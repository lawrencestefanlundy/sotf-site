---
type: concept
slug: rf-wireless
canonical_name: RF & Wireless
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
mention_count: 44
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-02-03-broadcom-unveils-enterprise-grade-silicon-for-wi-fi-8-aps-an
  title: Broadcom unveils enterprise-grade silicon for Wi-Fi 8 APs and Ethernet switches - Telecompaper
  date: '2026-02-03'
  kind: web
- slug: 2025-12-15-ethernet-roadmap-sets-a-new-course-for-connectivity-in-2026-
  title: Ethernet roadmap sets a new course for connectivity in 2026 - Electronic Products & Technology
  date: '2025-12-15'
  kind: web
- slug: 2023-09-04-survey-shows-growing-need-for-multi-network-access---elektor
  title: Survey Shows Growing Need for Multi-Network Access - Elektor Magazine
  date: '2023-09-04'
  kind: web
- slug: 2020-06-17-why-5g-nr-u-is-such-an-important-chapter-in-cellular-connect
  title: Why 5G NR-U is such an ‘important chapter’ in cellular connectivity - RCR Wireless News
  date: '2020-06-17'
  kind: web
- slug: 2019-07-22-huawei
  title: Huawei
  date: '2019-07-22'
  kind: web
neighbors: []
---
## Physics / mechanism

RF & wireless covers electromagnetic signal transmission in the 3 kHz–300 GHz range. Signals propagate via oscillating E/M fields; key parameters are frequency, bandwidth, path loss, noise figure, and linearity (IP3). Antenna efficiency, impedance matching, and modulation scheme (QAM, OFDM, MIMO) determine system throughput. Current 5G NR sub-6 GHz achieves ~4 Gbps peak; mmWave (24–100 GHz) pushes 10+ Gbps but with severe path loss (~20 dB/decade above 28 GHz). Front-end components—PAs, LNAs, filters, switches—are the performance bottleneck. GaAs, GaN, and SiGe BiCMOS dominate RF front-end ICs; bulk CMOS integration at mmWave remains lossy but cost-driven.

## Competitive landscape

Primary competition is between III-V (GaAs/GaN, high performance, expensive), SiGe BiCMOS (mid-tier, integrated), and advanced CMOS nodes (cheap, scaling-challenged for RF). Optical/photonic interconnects compete at short range (data center, chip-to-chip). Wi-Fi 7 (6 GHz, 46 Gbps theoretical) competes with cellular for indoor coverage. Satellite LEO constellations (Starlink, OneWeb) pressure terrestrial 5G for rural broadband. Ultra-wideband (UWB) competes in precision positioning. Terahertz (100 GHz–3 THz) is the emerging frontier, still pre-commercial.

| Approach | Frequency range | Key tradeoff |
|---|---|---|
| GaN RF | 1–100 GHz | High power, expensive substrate |
| SiGe BiCMOS | 1–77 GHz | Integration density vs noise |
| Advanced CMOS (5 nm) | sub-6 GHz | Cost efficient, poor mmWave efficiency |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
