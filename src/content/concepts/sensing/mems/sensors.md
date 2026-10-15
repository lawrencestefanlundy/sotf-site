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
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-10-15-us-optical-chip-gyroscope-gets-2000-fold-sensitivity-boost-d
  title: US optical chip gyroscope gets 2,000-fold sensitivity boost, detects slow rotation
  date: '2026-10-15'
  kind: web
- slug: 2026-10-14-new-chip-scale-gyroscope-measures-rotation-with-unprecedente
  title: New chip-scale gyroscope measures rotation with unprecedented sensitivity
  date: '2026-10-14'
  kind: web
- slug: 2026-10-14-new-360-degree-air-defense-radar-with-detection-range-exceed
  title: New 360-degree air defense radar with detection range exceeding 205 miles can transform warfare
  date: '2026-10-14'
  kind: web
- slug: 2026-10-13-new-topological-microscope-tip-reveals-evidence-of-2d-alterm
  title: New topological microscope tip reveals evidence of 2D altermagnetism
  date: '2026-10-13'
  kind: web
- slug: 2026-10-12-from-nonmagnetic-to-magnetic-a-2d-semiconductor-with-electri
  title: 'From nonmagnetic to magnetic: A 2D semiconductor with electrically tunable magnetism'
  date: '2026-10-12'
  kind: web
- slug: 2026-10-12-21-us-military-satellites-blast-at-15660-mph-to-hunt-missile
  title: 21 US military satellites blast at 15,660 mph to hunt missile threats from space
  date: '2026-10-12'
  kind: web
- slug: 2026-10-11-ultraviolet-laser-creates-new-defects-in-diamond-without-dis
  title: Ultraviolet laser creates new defects in diamond without disturbing quantum centers
  date: '2026-10-11'
  kind: web
- slug: 2026-10-10-ultraviolet-laser-pulses-engineer-diamond-defects-selectivel
  title: Ultraviolet laser pulses engineer diamond defects selectively, leaving quantum qubits intact
  date: '2026-10-10'
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
