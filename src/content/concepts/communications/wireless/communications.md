---
type: concept
slug: communications
canonical_name: Communications
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- communications
- wireless
related_concepts: []
companies_using:
- aalyria-technologies
- anova-technologies
- bridgesat-now-part-of-laser-light-communications
- cobham-satcom-now-part-of-cobham-advanced-electronics-soluti
- cohere-technologies
- eutelsat
- gatehouse-satcom
- inmarsat
- iridium-communications
- isotropic-systems-now-isotropic-networks
- kinis
- mynaric
- nanowave-technologies
- orbcomm
- persistent-systems
- sateliot
- ses
- siae-microelettronica
- silvus-technologies
- starlink-spacex
- tesat-spacecom
- thuraya-telecommunications
- transcelestial
- undulating-formerly-known-as-rivada-space-networks
- viasat
ideas_referencing: []
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2025-10-09-a-specific-theory-of-sovereign-ai]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2025-09-02-13-drop-in-employment-for-young-workers]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-04-24-i-am-artemis-peter-rossoni]]'
- '[[2022-11-15-qualcomm]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 96
descendants:
- direct-to-cell-leo
- leo-mega-constellations
- optical-inter-satellite-links
- space-communications
last_reorg_date: '2026-05-13'
sources_7d: 6
sources_30d: 19
---

# Communications

*Kind: technology · Attio deal count: 26*

## Physics / mechanism

Communications encompasses the transmission of information across a medium — electrical, optical, or wireless — governed by Shannon's channel capacity theorem: C = B·log₂(1 + S/N). Key parameters: bandwidth (Hz), spectral efficiency (bits/s/Hz), latency (µs–ms), power per bit (pJ/bit), and BER targets (10⁻¹² for optical). Current SOTA: coherent optical transceivers at 800G per wavelength (ZR/ZR+), pushing toward 1.6T; PCIe 6.0 and UCIe for die-to-die; 5G NR at sub-6 GHz and mmWave (26/28/39 GHz). Ethernet roadmap targets 1.6T ports by 2026. Power efficiency is the binding constraint — AI cluster interconnects now consume 10–15% of total rack power.

## Competitive landscape


Optical interconnects (silicon photonics, InP, GaAs) compete against copper (DAC/PAC cables viable to ~7m, 112G PAM4) and wireless (mmWave, terahertz for short-range). At the architecture level, compute-near-memory approaches reduce communication distance entirely. Key players: Coherent, II-VI/Coherent, Marvell, Broadcom (DSPs), Ayar Labs (optical I/O chiplets), Celestial AI, Eliyan (UCIe PHY). CPO (co-packaged optics) vs. pluggable is the structural tension — GPO still dominates volume but CPO wins on watt/bit at scale.

| Approach | Range | Power (pJ/bit) | Maturity |
|---|---|---|---|
| Copper DAC | <7 m | ~10 | Production |
| Silicon photonics | m–km | ~3–5 | Scaling |
| InP coherent | >80 km | ~15–30 | Production |

## Cloudberry relevance
For Cloudberry, communications is the pull-through market for the core thesis: GF's photonics PDK (GF Fotonix, 300mm SiPh) directly enables transceiver and LiDAR chiplets. Deal-flow targets: CPO startups fabbing on GF, novel III-V-on-Si integration, and terahertz sources for 6G front-haul. Lunar portfolio exposure through fabless interconnect IP plays. The AI infrastructure capex cycle — $200B+ datacenter spend in 2024–2026 — makes optical interconnect the highest-conviction adjacent bet.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
