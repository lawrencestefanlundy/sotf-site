---
type: concept
slug: iot-connected-devices
canonical_name: IoT & Connected Devices
aliases: []
kind: market
domain:
- cloudberry
- sotf
parent_concepts:
- communications
- wireless
related_concepts: []
companies_using:
- accelercomm
- aeris-communications
- airgain
- arm-holdings
- augury
- ayla-networks
- castor
- coiote-avsystem
- eaidk-gizwits
- espressif-systems
- everynet
- friendly-technologies
- haltian
- helium-nova-labs
- memfault
- myriota
- nabto
- nordic-semiconductor
- onomondo
- particle-industries
- pillar-technologies-pillar
- quectel-wireless-solutions
- rayven
- relayr
- samsara
- semtech
- sequans-communications
- silicon-laboratories
- silicon-labs
- soracom
- sternum
- stmicroelectronics
- talkpool
- tuya-smart
- u-blox
- wirepas
- wyld-networks
- wzzard-advantech
- zariot
- zenseact-imagimob
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- market
mention_count: 57
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 1
---

# IoT & Connected Devices

*Kind: market · Attio deal count: 57*

## Physics / mechanism

IoT & Connected Devices encompasses networked physical hardware—sensors, actuators, edge compute nodes—that collect, process, and transmit data. The stack runs from silicon (MCUs, SoCs, RF transcanceivers) through firmware and connectivity protocols (Bluetooth LE, Zigbee, Matter, LTE-M, NB-IoT, Wi-Fi 6) to cloud ingestion. Key parameters: power budget (µA sleep / mA active), latency, data throughput, and unit cost at scale. Market sits at ~$500B (2024) growing ~12% CAGR. Dominant silicon vendors: Nordic Semi, Silicon Labs, STMicro, NXP, Qualcomm. Edge inference increasingly on-device via dedicated NPUs (Arm Ethos, Ambiq). Connectivity fragmentation remains the primary integration tax.

## Competitive landscape


Adjacent pressure comes from three directions: (1) purpose-built ASIC/ASSP designs undercutting general MCU margins; (2) cellular IoT (NB-IoT/LTE-M) displacing short-range mesh in industrial; (3) Wi-Fi 7 / UWB consolidating positioning + data onto fewer radios.

| Dimension | Short-range mesh | Cellular IoT | Wired (IO-Link/TSN) |
|---|---|---|---|
| Power | µW–mW | mW–100mW | Line-powered |
| Coverage | <100m | Wide-area | Fixed topology |
| Cost/node | $1–5 | $5–15 | $10–50 |

## Cloudberry relevance
Cloudberry relevance concentrates at the silicon and photonics interface: custom RF front-ends, photonic sensing (LiDAR, optical gas sensors), and advanced packaging enabling multi-die IoT SoCs—all manufacturable on GlobalFoundries' 22FDX and 45CLO nodes. Deal-flow angles: sensor ASIC startups needing GF process access, photonic-sensor fusion companies, and energy-harvesting IC developers reducing battery dependency. Lunar Ventures' enterprise-software adjacency surfaces IoT platform companies where hardware differentiation is the moat.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
