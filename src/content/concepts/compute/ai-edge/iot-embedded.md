---
type: concept
slug: iot-embedded
canonical_name: IoT & Embedded
aliases: []
kind: technology
parent_concepts:
- compute
- ai-edge
related_concepts: []
sources: []
frontier: []
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 3
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-10-13-i-have-no-mouth-and-i-must-scream
  title: “I have no mouth and I must scream”
  date: '2026-10-13'
  kind: web
- slug: 2026-10-02-dect-nr-private-5g-for-industrial-iot-networks---wiot-groupc
  title: 'DECT NR+: Private 5G for Industrial IoT Networks - wiot-group.com'
  date: '2026-10-02'
  kind: web
- slug: 2026-09-29-new-tech-tuesdays-industrial-wi-fi-7-for-factory-connectivit
  title: 'New Tech Tuesdays: Industrial Wi-Fi 7 for Factory Connectivity - Electronic Design'
  date: '2026-09-29'
  kind: web
- slug: 2026-09-28-the-microwatt-chip-race-the-ai-hardware-podcast-s2e11
  title: The Microwatt Chip Race // The AI Hardware Podcast S2E11
  date: '2026-09-28'
  kind: web
- slug: 2026-09-25-how-low-can-ai-power-go-the-ai-hardware-show-s2e11
  title: How Low Can AI Power Go? // The AI Hardware Show S2E11
  date: '2026-09-25'
  kind: web
- slug: 2026-09-21-six-chips-fighting-for-the-edge-the-ai-hardware-podcast-s2e1
  title: Six Chips Fighting for the Edge // The AI Hardware Podcast S2E10
  date: '2026-09-21'
  kind: web
- slug: 2026-08-25-embedd-pre-seed-inelectronics
  title: Embedd raises EUR 2.3m for semiconductor integration software
  date: '2026-08-25'
  kind: web
- slug: 2026-08-24-embedd-pre-seed-siliconangle
  title: Chip software automation startup Embedd raises $2.7M
  date: '2026-08-24'
  kind: web
neighbors: []
---
## Physics / mechanism

IoT and embedded systems span microcontrollers (MCUs), sensors, edge processors, and the connectivity stacks linking them to cloud or fog compute. Core compute is 32-bit ARM Cortex-M or RISC-V cores running at 10–500 MHz, with power envelopes from sub-µW (energy harvesting nodes) to ~100 mW (edge ML inference). Flash/SRAM integration, analog front-ends, and mixed-signal IP define differentiation. Connectivity layers—BLE 5.x, 802.15.4/Thread, LoRaWAN, NB-IoT—add protocol overhead. State-of-the-art: TSMC 22nm/GF 22FDX MCUs achieving <10 µA deep-sleep, on-device ML inference via NPU tiles (e.g., Ambiq Apollo, Nordic nRF54), and MEMS sensor fusion at <1 mW. Security (TrustZone, PSA Certified) is now table-stakes.

## Competitive landscape

Key axis of competition is power vs. compute density. Nordic, STM, NXP, and Renesas dominate general-purpose MCUs. Ambiq and Syntiant attack ultra-low-power ML inference. RISC-V cores (SiFive, Andes) threaten ARM licensing economics at the low end.

| Approach | Power floor | ML capability |
|---|---|---|
| ARM Cortex-M (STM32, NXP) | ~1 µA sleep | Soft, CMSIS-NN |
| Ultra-LP custom (Ambiq) | ~10 nA sleep | Dedicated NPU |
| RISC-V MCU (GigaDevice, WCH) | ~0.5 µA sleep | Minimal |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
