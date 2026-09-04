---
type: concept
slug: tactile-sensing
canonical_name: Tactile Sensing & Electronic Skin
aliases:
- tactile sensing
- electronic skin
- e-skin
- touch sensing
kind: technology
parent_concepts:
- physical-ai
- sensing
related_concepts:
- dexterous-manipulation
- robot-actuators
- mems
- low-power-edge-compute
sources:
- '[[2026-07-13-humanoid-actuator-supply-chain-chinese-dexterous-hands-in]]'
frontier:
- The bottleneck is shifting from the transducer to getting dense, high-frequency tactile data OFF the skin and processed at the edge fast enough to close a 200Hz loop (the readout/near-sensor IC).
- 'Which transduction wins: optical (resolution) vs magnetic (robust 3-axis) vs MEMS (cheap/volume)? Likely segmented, not one winner.'
last_updated: '2026-06-13'
tags:
- concept
- technology
- robotics
- sensing
- tactile
mention_count: 5
sources_7d: 2
sources_30d: 2
recent_mentions:
- slug: 2026-07-13-humanoid-actuator-supply-chain-chinese-dexterous-hands-in
  title: 'Chinese Dexterous Hands in 2026: Buyer''s Guide & Comparison'
  date: '2026-07-13'
  kind: web
neighbors:
- slug: dexterous-manipulation
  name: Dexterous Manipulation & Robot Hands
  path: /robotics/embodiment/dexterous-manipulation/
  macro: robotics
- slug: robot-actuators
  name: Robot Actuators (the muscle layer)
  path: /robotics/embodiment/robot-actuators/
  macro: robotics
- slug: mems
  name: MEMS
  path: /sensing/mems/mems/
  macro: sensing
---
Giving robots a sense of touch: contact location, normal/shear force, slip, texture, sometimes temperature/vibration. The under-built modality and arguably the missing sense for [dexterity](/robotics/embodiment/dexterous-manipulation/). Market ~$4.0bn (2025) -> ~$8.4bn (2030), ~16% CAGR (Mordor); robotics ~38% of demand.

## Approaches & leading products

- **Optical / camera-based (GelSight-type)** — a camera images a deformable gel; very high *spatial* resolution but bulky, latency, fragile. GelSight (commercial leader) + Meta's DIGIT 360 (18+ modalities, research).
- **Magnetic / Hall-effect** — magnet on soft substrate over Hall sensors, tracks 3-axis force. XELA uSkin is the leader (just integrated into the TESOLLO DG-5F hand). Robust, multi-axis, scalable.
- **Capacitive** — mature (touchscreens), lower resolution, drift.
- **Barometric / MEMS** — off-the-shelf MEMS barometers as cheap force cells; MEMS held ~37.5% of the tactile market in 2024. Cheapest path to volume. Tacterion (DE, flexible), Contactile (AU, 3D force + slip).
- **Biomimetic fluid (BioTac)** — SynTouch is small (~16 staff) but alive (NOT acquired/discontinued, a corrected assumption); BioTac remains a reference research sensor.

## The investable angle (the readout, not the transducer)

The bottleneck is shifting from the transducer to **getting dense, high-frequency tactile data off the skin and processed at the edge** fast enough to close a ~200Hz control loop. High-res skin generates a torrent of data; on-/near-sensor processing (neuromorphic, MEMS-integrated) and the analog-front-end/readout IC are where differentiation and value capture sit. This is the most semiconductor-adjacent angle in the whole robotics cluster, and the basis of the **Tactile Sensing Silicon** thesis. Ties to **Mems Sensing Actuation** (deal coverage) and **Low Power Edge Compute**.

## Connections

[Physical AI (robotics cluster hub)](/robotics/robot-learning/physical-ai/) · [Dexterous Manipulation & Robot Hands](/robotics/embodiment/dexterous-manipulation/) · **Tactile Sensing Silicon** · **Mems Sensing Actuation** · **Robot Autonomy Destination** · [Robot Actuators (the muscle layer)](/robotics/embodiment/robot-actuators/)
