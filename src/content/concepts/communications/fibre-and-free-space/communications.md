---
type: concept
slug: communications
canonical_name: Communications
aliases: []
kind: technology
parent_concepts:
- communications
- fibre-and-free-space
related_concepts: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2025-09-02-13-drop-in-employment-for-young-workers]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-05-30-optical-interconnect-ma-ledger]]'
- '[[2026-04-24-i-am-artemis-peter-rossoni]]'
- '[[2026-05-13-20-years-of-space-communications-and-navigation]]'
- '[[2022-11-15-qualcomm]]'
- '[[2026-06-01-ncsc-nsa-qkd-vs-pqc]]'
- '[[2025-04-15-nature-comm-thermodynamic-computing-system]]'
- '[[2026-06-01-nibras-ucl-chipstart]]'
- '[[2025-11-17-hms-networks-acquires-industrial-communications-business-fro]]'
- '[[2026-05-14-nasa-draws-on-industry-for-mars-telecommunications-network]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 140
descendants:
- 5g-nr-advanced
- beamforming-ics
- communications
- communications-equipment
- dark-fibre-submarine-cables
- datacenter-network-stack
- dect-nr
- diffractive-deep-neural-network
- fiber-optics
- free-space-optics
- free-space-photonics
- iot-connected-devices
- lpo-linear-pluggable-optics
- mmwave
- networking-wireless
- optical-circuit-switching
- optical-interconnect
- optical-io-chip-level
- optical-packet-switching
- phased-array-antennas
- pluggable-transceivers
- qkd
- quantum-communication
- quantum-communications
- quantum-networks
- quantum-repeaters
- rf-wireless
- software-defined-radio
- sub-thz-6g
- timing-clock-generation
last_reorg_date: '2026-05-14'
sources_7d: 20
sources_30d: 55
recent_mentions:
- slug: 2026-06-01-ncsc-nsa-qkd-vs-pqc
  title: 'NCSC / NSA position: QKD not endorsed, post-quantum cryptography is the recommended mitigation'
  date: '2026-06-01'
  kind: web
- slug: 2026-06-01-nibras-ucl-chipstart
  title: UCL EEE ventures selected for national ChipStart programme (incl. Nibras Communications)
  date: '2026-06-01'
  kind: web
- slug: 2026-05-30-optical-interconnect-ma-ledger
  title: Optical-interconnect / photonic-packaging M&A ledger (2019-2026)
  date: '2026-05-30'
  kind: web
- slug: 2026-05-14-nasa-draws-on-industry-for-mars-telecommunications-network
  title: NASA Draws on Industry for Mars Telecommunications Network
  date: '2026-05-14'
  kind: web
- slug: 2026-05-13-20-years-of-space-communications-and-navigation
  title: 20 Years of Space Communications and Navigation
  date: '2026-05-13'
  kind: web
- slug: 2026-04-24-i-am-artemis-peter-rossoni
  title: 'I Am Artemis: Peter Rossoni'
  date: '2026-04-24'
  kind: web
- slug: 2025-12-19-lfg-for-semiconductors
  title: LFG (for semiconductors)
  date: '2025-12-19'
  kind: substack
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
neighbors: []
---
## Physics / mechanism

Communications encompasses the transmission of information across a medium — electrical, optical, or wireless — governed by Shannon's channel capacity theorem: C = B·log₂(1 + S/N). Key parameters: bandwidth (Hz), spectral efficiency (bits/s/Hz), latency (µs–ms), power per bit (pJ/bit), and BER targets (10⁻¹² for optical). Current SOTA: coherent optical transceivers at 800G per wavelength (ZR/ZR+), pushing toward 1.6T; PCIe 6.0 and UCIe for die-to-die; 5G NR at sub-6 GHz and mmWave (26/28/39 GHz). Ethernet roadmap targets 1.6T ports by 2026. Power efficiency is the binding constraint — AI cluster interconnects now consume 10–15% of total rack power.

## Competitive landscape

Optical interconnects (silicon photonics, InP, GaAs) compete against copper (DAC/PAC cables viable to ~7m, 112G PAM4) and wireless (mmWave, terahertz for short-range). At the architecture level, compute-near-memory approaches reduce communication distance entirely. Key players: Coherent, II-VI/Coherent, Marvell, Broadcom (DSPs), Ayar Labs (optical I/O chiplets), Celestial AI, Eliyan (UCIe PHY). CPO (co-packaged optics) vs. pluggable is the structural tension — GPO still dominates volume but CPO wins on watt/bit at scale.

| Approach | Range | Power (pJ/bit) | Maturity |
|---|---|---|---|
| Copper DAC | <7 m | ~10 | Production |
| Silicon photonics | m–km | ~3–5 | Scaling |
| InP coherent | >80 km | ~15–30 | Production |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
