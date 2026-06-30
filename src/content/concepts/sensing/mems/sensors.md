---
type: concept
slug: sensors
canonical_name: Sensors
aliases: []
kind: technology
parent_concepts:
- sensing
- mems
related_concepts: []
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
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 271
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 31
recent_mentions:
- slug: 2026-06-29-sentinel-1-shows-ground-displacement-after-venezuela-earthqu
  title: Sentinel-1 shows ground displacement after Venezuela earthquakes
  date: '2026-06-29'
  kind: web
- slug: 2026-06-29-nasa-seeks-industry-input-to-accelerate-lunar-surface-techno
  title: NASA Seeks Industry Input to Accelerate Lunar Surface Technologies
  date: '2026-06-29'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-21-st-nxp-mems-acquisition
  title: STMicroelectronics to acquire NXP's MEMS sensor business for up to $950M
  date: '2026-06-21'
  kind: web
- slug: 2026-06-21-yole-mems-market-momentum
  title: MEMS market regains momentum — Bosch, STMicroelectronics and TDK navigate the post-inventory growth era (Status of the MEMS Industry 2025)
  date: '2026-06-21'
  kind: web
- slug: 2026-06-20-launch-cost-curve-web
  title: Launch-cost curve + LEO deployment + constellation compute (web bundle)
  date: '2026-06-20'
  kind: web
- slug: 2026-06-17-nawah-vacnt-technology
  title: NAWAH Architectured Nanomaterials — VACNT technology & positioning
  date: '2026-06-17'
  kind: web
- slug: 2026-06-13-smr-datacentre-baseload-research
  title: SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)
  date: '2026-06-13'
  kind: web
neighbors: []
---
## Physics / mechanism

Sensors transduce a physical quantity (pressure, photons, temperature, chemical concentration, acceleration) into an electrical signal. The core physics depends on the modality: piezoresistive/capacitive for MEMS pressure/inertial, photoelectric effect for image sensors and LiDAR receivers, electrochemical for gas/biosensors, pyroelectric/bolometric for thermal IR. Key parameters: sensitivity (signal/input unit), noise floor (NEP for optical, μg/√Hz for IMUs), bandwidth, drift, and power. State of the art: Sony/Samsung BSI CMOS image sensors at sub-micron pixels; Bosch MEMS IMUs at <10 μg/√Hz noise; uncooled VOx bolometers at NETD <30 mK. Integration trend is sensor fusion on-chip with edge inference.

## Competitive landscape

MEMS sensors (Bosch, STMicro, TDK/InvenSense) dominate inertial/pressure at commodity margins. Photonic sensors—silicon photonics-based LiDAR, integrated spectrometers, optical gyros—compete on performance-per-power at higher ASP. Emerging: quantum sensors (atomic interferometry, NV-center magnetometers) threaten MEMS in navigation accuracy but remain pre-commercial. Chemical/biosensors fragment by vertical. The meaningful battleground is CMOS-integration density vs. heterogeneous packaging of III-V or LN-on-Si for photonic modalities.

| Modality | Key metric | Integration path |
|---|---|---|
| MEMS inertial | Noise floor μg/√Hz | Monolithic CMOS |
| Photonic (LiDAR/spectro) | NEP, angular res | Si photonics / III-V flip-chip |
| Quantum | ppb sensitivity, drift | Hybrid, nascent fab |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
