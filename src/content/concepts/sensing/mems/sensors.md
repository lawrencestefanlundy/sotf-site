---
type: concept
slug: sensors
canonical_name: Sensors
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- mems
related_concepts: []
companies_using:
- ambu
- ams-osram
- arbe-robotics
- atomica-formerly-imt-masken-und-teilungen
- bosch-sensortec
- hamamatsu-photonics
- hectronic-novelda
- infineon-technologies
- mynaric
- pixart-imaging
- prophesee
- quanergy-systems
- quside
- senseering
- sensirion
- serelay
- silo-ai-vtt-sensor-spin-outs-sensordynamics-lineage
- sitime
- smartec-semiconductor
- sony-semiconductor-solutions
- stmicroelectronics
- uhnder
- vayyar-imaging
- xsens-part-of-mcube-movella
ideas_referencing: []
sources:
- '[[2023-09-18-e15-in-conversation-with-wisear-on]]'
- '[[2025-09-23-the-compute-gradient]]'
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2025-04-23-what-if-ai-can-already-feel]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-05-31-three-underrated-technologies-from]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-05-08-nasa-fuel-cell-tests-pave-way-for-energy-storage-on-moon]]'
- '[[2026-05-06-putting-the-super-into-a-supersite-for-earth-observation]]'
- '[[2025-01-06-radiant-acquires-nilt]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 118
last_reorg_date: '2026-05-13'
sources_7d: 8
sources_30d: 20
---

# Sensors

*Kind: technology · Attio deal count: 73*

## Physics / mechanism

Sensors transduce a physical quantity (pressure, photons, temperature, chemical concentration, acceleration) into an electrical signal. The core physics depends on the modality: piezoresistive/capacitive for MEMS pressure/inertial, photoelectric effect for image sensors and LiDAR receivers, electrochemical for gas/biosensors, pyroelectric/bolometric for thermal IR. Key parameters: sensitivity (signal/input unit), noise floor (NEP for optical, μg/√Hz for IMUs), bandwidth, drift, and power. State of the art: Sony/Samsung BSI CMOS image sensors at sub-micron pixels; Bosch MEMS IMUs at <10 μg/√Hz noise; uncooled VOx bolometers at NETD <30 mK. Integration trend is sensor fusion on-chip with edge inference.

## Competitive landscape


MEMS sensors (Bosch, STMicro, TDK/InvenSense) dominate inertial/pressure at commodity margins. Photonic sensors—silicon photonics-based LiDAR, integrated spectrometers, optical gyros—compete on performance-per-power at higher ASP. Emerging: quantum sensors (atomic interferometry, NV-center magnetometers) threaten MEMS in navigation accuracy but remain pre-commercial. Chemical/biosensors fragment by vertical. The meaningful battleground is CMOS-integration density vs. heterogeneous packaging of III-V or LN-on-Si for photonic modalities.

| Modality | Key metric | Integration path |
|---|---|---|
| MEMS inertial | Noise floor μg/√Hz | Monolithic CMOS |
| Photonic (LiDAR/spectro) | NEP, angular res | Si photonics / III-V flip-chip |
| Quantum | ppb sensitivity, drift | Hybrid, nascent fab |

## Cloudberry relevance
Sensors sit at the entry point of every edge-compute and autonomy stack—hardware that commoditises slowly because physics limits set hard moats. For Cloudberry, the angle is photonic and MEMS sensors manufacturable on advanced CMOS nodes or GlobalFoundries-compatible PDKs: startups building integrated spectrometers, on-chip LiDAR receivers, or photonic gyros are natural pipeline. Lunar Ventures' early-stage exposure surfaces university spin-outs in quantum sensing before they need fab-scale capital.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
