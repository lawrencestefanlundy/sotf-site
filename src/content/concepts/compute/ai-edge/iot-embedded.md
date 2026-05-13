---
type: concept
slug: iot-embedded
canonical_name: IoT & Embedded
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- ai-edge
related_concepts: []
companies_using:
- anjay-avsystem
- arm-holdings
- avsystem
- blues-wireless
- bouffalo-lab
- embedded-planet-bytesatwork
- espressif-systems
- favoriot
- foundriesio
- golioth
- husarion
- inferrix-formerly-neuralet
- infineon-technologies
- lacuna-space
- memfault
- menderio-northerntech
- myriota
- nordic-semiconductor
- nxp-semiconductors
- pantacor
- particle-industries
- percepio
- qubitro
- rad-memory-formerly-rad-chip
- raspberry-pi-ltd
- renode-antmicro
- sensorfu
- sequans-communications
- sequitur-labs
- silicon-laboratories-silicon-labs
- silicon-labs
- soracom
- stmicroelectronics
- telink-semiconductor
- tinyml-foundation-edge-impulse
- toit-acquired-by-toitware-now-part-of-toitlang
- toit-acquired-by-toitware
- wiznet
- zenseact-antmicro
- zephyr-project-eclipse-foundation-zephyr-rtos
- zephyr-project-nordic-rtos
- zerynth
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 3
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# IoT & Embedded

*Kind: technology · Attio deal count: 3*

## Physics / mechanism

IoT and embedded systems span microcontrollers (MCUs), sensors, edge processors, and the connectivity stacks linking them to cloud or fog compute. Core compute is 32-bit ARM Cortex-M or RISC-V cores running at 10–500 MHz, with power envelopes from sub-µW (energy harvesting nodes) to ~100 mW (edge ML inference). Flash/SRAM integration, analog front-ends, and mixed-signal IP define differentiation. Connectivity layers—BLE 5.x, 802.15.4/Thread, LoRaWAN, NB-IoT—add protocol overhead. State-of-the-art: TSMC 22nm/GF 22FDX MCUs achieving <10 µA deep-sleep, on-device ML inference via NPU tiles (e.g., Ambiq Apollo, Nordic nRF54), and MEMS sensor fusion at <1 mW. Security (TrustZone, PSA Certified) is now table-stakes.

## Competitive landscape


Key axis of competition is power vs. compute density. Nordic, STM, NXP, and Renesas dominate general-purpose MCUs. Ambiq and Syntiant attack ultra-low-power ML inference. RISC-V cores (SiFive, Andes) threaten ARM licensing economics at the low end.

| Approach | Power floor | ML capability |
|---|---|---|
| ARM Cortex-M (STM32, NXP) | ~1 µA sleep | Soft, CMSIS-NN |
| Ultra-LP custom (Ambiq) | ~10 nA sleep | Dedicated NPU |
| RISC-V MCU (GigaDevice, WCH) | ~0.5 µA sleep | Minimal |

## Cloudberry relevance
GF's 22FDX platform is purpose-built for IoT: FD-SOI with back-bias tuning enables MCU and RF co-integration at power levels unobtainable on bulk CMOS. This makes GF a natural process partner for portfolio companies building differentiated ultra-LP MCUs, sensor ASICs, or edge-inference chips. Deal-flow signal: founders choosing 22FDX over TSMC 28nm for power-sensitive IoT silicon are often pre-Series A and fundable. Lunar Ventures' software-adjacent bets (e.g., embedded OS, OTA infra) create co-investment surface.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
