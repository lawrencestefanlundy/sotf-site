---
type: concept
slug: iot-connected-devices
canonical_name: IoT & Connected Devices
aliases: []
kind: market
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
- market
mention_count: 57
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2023-09-04-survey-shows-growing-need-for-multi-network-access---elektor
  title: Survey Shows Growing Need for Multi-Network Access - Elektor Magazine
  date: '2023-09-04'
  kind: web
- slug: 2021-03-05-we-strive-to-continuously-deliver-an-efficient-iot-architect
  title: '''We strive to continuously deliver an efficient IoT architecture, i.e. the one ensuring unicity and authenticity of device, integrity of the firmware installed on it, and confidentiality of data.'' - Industrial Engineering News Europe'
  date: '2021-03-05'
  kind: web
neighbors: []
---
## Physics / mechanism

IoT & Connected Devices encompasses networked physical hardware—sensors, actuators, edge compute nodes—that collect, process, and transmit data. The stack runs from silicon (MCUs, SoCs, RF transcanceivers) through firmware and connectivity protocols (Bluetooth LE, Zigbee, Matter, LTE-M, NB-IoT, Wi-Fi 6) to cloud ingestion. Key parameters: power budget (µA sleep / mA active), latency, data throughput, and unit cost at scale. Market sits at ~$500B (2024) growing ~12% CAGR. Dominant silicon vendors: Nordic Semi, Silicon Labs, STMicro, NXP, Qualcomm. Edge inference increasingly on-device via dedicated NPUs (Arm Ethos, Ambiq). Connectivity fragmentation remains the primary integration tax.

## Competitive landscape

Adjacent pressure comes from three directions: (1) purpose-built ASIC/ASSP designs undercutting general MCU margins; (2) cellular IoT (NB-IoT/LTE-M) displacing short-range mesh in industrial; (3) Wi-Fi 7 / UWB consolidating positioning + data onto fewer radios.

| Dimension | Short-range mesh | Cellular IoT | Wired (IO-Link/TSN) |
|---|---|---|---|
| Power | µW–mW | mW–100mW | Line-powered |
| Coverage | <100m | Wide-area | Fixed topology |
| Cost/node | $1–5 | $5–15 | $10–50 |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
