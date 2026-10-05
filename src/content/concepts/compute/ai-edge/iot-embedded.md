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
- slug: 2026-10-02-dect-nr-private-5g-for-industrial-iot-networks---wiot-groupc
  title: 'DECT NR+: Private 5G for Industrial IoT Networks - wiot-group.com'
  date: '2026-10-02'
  kind: web
- slug: 2026-09-29-new-tech-tuesdays-industrial-wi-fi-7-for-factory-connectivit
  title: 'New Tech Tuesdays: Industrial Wi-Fi 7 for Factory Connectivity - Electronic Design'
  date: '2026-09-29'
  kind: web
- slug: 2026-08-25-embedd-pre-seed-inelectronics
  title: Embedd raises EUR 2.3m for semiconductor integration software
  date: '2026-08-25'
  kind: web
- slug: 2026-08-24-embedd-pre-seed-siliconangle
  title: Chip software automation startup Embedd raises $2.7M
  date: '2026-08-24'
  kind: web
- slug: 2026-08-12-celona-takes-private-5g-into-the-industrial-wi-fi-fight-with
  title: Celona takes private 5G into the industrial Wi-Fi fight – with AI in the middle - rcrwireless.com
  date: '2026-08-12'
  kind: web
- slug: 2026-04-10-hms-networks-introduces-cost-efficient-can-fd-to-ethernet-ga
  title: HMS Networks introduces cost-efficient CAN-FD-to-Ethernet-gateway for scalable industrial networking - Electronics360
  date: '2026-04-10'
  kind: web
- slug: 2022-12-26-dect-forum-adds-nordic-semiconductor-and-wirepas-to-membersh
  title: DECT Forum Adds Nordic Semiconductor and Wirepas to Membership - eetasia.com
  date: '2022-12-26'
  kind: web
- slug: 2022-12-16-nordic-semiconductor-and-wirepas-join-dect-forum-as-full-mem
  title: Nordic Semiconductor and Wirepas Join DECT Forum as Full Members - businesswire.com
  date: '2022-12-16'
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
