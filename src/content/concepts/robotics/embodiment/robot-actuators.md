---
type: concept
slug: robot-actuators
canonical_name: Robot Actuators (the muscle layer)
aliases:
- robot actuators
- actuators
- servo motors robotics
kind: technology
parent_concepts:
- physical-ai
related_concepts:
- dexterous-manipulation
- tactile-sensing
- power-electronics
sources:
- '[[2025-04-23-what-if-ai-can-already-feel]]'
- '[[2026-06-08-semianalysis-unitree-robotics]]'
- '[[2026-07-16-robotics-labour-augmentation-the-us-58-9-billion-humanoid]]'
- '[[2026-07-16-robotics-labour-augmentation-humanoid-robot-bom-cost]]'
- '[[2026-07-08-robotics-labour-augmentation-tesla-optimus-hardware]]'
- '[[2026-06-10-robotics-labour-augmentation-humanoid-robotics-company]]'
- '[[2026-06-13-usgs-mcs-rare-earths-supply-concentration]]'
- '[[2026-07-13-robotics-labour-augmentation-global-emerging-robotics]]'
- '[[2026-06-13-iea-critical-minerals-export-controls-2025]]'
- '[[2026-01-14-humanoid-actuator-supply-chain-after-ces-spotlight-korean]]'
- '[[2026-07-26-humanoid-duty-cycle-thermal-constraint]]'
- '[[2026-06-02-america-spins-on-westmag]]'
- '[[2026-05-18-humanoid-actuator-supply-chain-humanoid-robots-in-2026]]'
frontier:
- 'Backdrivability (feel forces through the mechanism) vs industrial repeatability: incumbents optimised for the wrong property for teleop/dexterity.'
- Is there a Cloudberry-shaped SILICON wedge here, or is it mechanical engineering on commodity motor-control ICs?
last_updated: '2026-06-13'
tags:
- concept
- technology
- robotics
- actuators
mention_count: 34
sources_7d: 0
sources_30d: 4
recent_mentions:
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-26-unitree-ipo-shipment-and-segment-data
  title: 'Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-16-robotics-labour-augmentation-the-us-58-9-billion-humanoid
  title: The US$58.9 Billion Humanoid Robot Opportunity Starts With Actuators, Sensors, And Batteries
  date: '2026-07-16'
  kind: web
- slug: 2026-07-16-robotics-labour-augmentation-humanoid-robot-bom-cost
  title: 'Humanoid Robot BOM Cost Analysis: Actuators, Sensors and Batteries Market Focus'
  date: '2026-07-16'
  kind: web
- slug: 2026-07-13-robotics-labour-augmentation-global-emerging-robotics
  title: 'Global Emerging Robotics Market 2027–2037: Value Capture and BOM Decomposition'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-08-robotics-labour-augmentation-tesla-optimus-hardware
  title: 'Tesla Optimus Hardware Specifications: Actuators, Hands & Sensors 2026'
  date: '2026-07-08'
  kind: web
- slug: 2026-06-13-usgs-mcs-rare-earths-supply-concentration
  title: USGS Mineral Commodity Summaries — Rare Earths (2025 / 2026 editions)
  date: '2026-06-13'
  kind: web
- slug: 2026-06-13-iea-critical-minerals-export-controls-2025
  title: China's rare-earth & magnet export controls (Apr 2025 onward) — IEA + trade-press synthesis
  date: '2026-06-13'
  kind: web
neighbors:
- slug: dexterous-manipulation
  name: Dexterous Manipulation & Robot Hands
  path: /robotics/embodiment/dexterous-manipulation/
  macro: robotics
- slug: tactile-sensing
  name: Tactile Sensing & Electronic Skin
  path: /robotics/embodiment/tactile-sensing/
  macro: robotics
- slug: power-electronics
  name: Power Electronics
  path: /energy-power/power-electronics/power-electronics/
  macro: energy-power
---
The part that moves: servo motors, harmonic/cycloidal drives, quasi-direct-drive (QDD), series-elastic actuators (SEA), tendon systems, and (experimentally) hydraulic artificial muscles. A humanoid has ~20-50 actuators; this layer is a real cost, weight, thermal, and reliability constraint (Tesla paused Optimus production late-2025 partly on motor overheating).

## The teleop/dexterity divergence from industrial

Industrial automation optimises **repeatability** (hit the same position to 0.01mm via high-ratio harmonic drives, which are opaque to force). Teleop and [dexterity](/robotics/embodiment/dexterous-manipulation/) need **backdrivability and torque transparency** (the operator/policy must feel what the robot touches), which favours QDD and SEA. The incumbents (ABB, Fanuc, KUKA, maxon, Faulhaber) spent decades optimising for the wrong property. Schaeffler is now a humanoid actuator supplier (to **Neura**); Clone Robotics bets on hydraulic myofiber muscles.

## Connections

[Physical AI (robotics cluster hub)](/robotics/robot-learning/physical-ai/) · [Dexterous Manipulation & Robot Hands](/robotics/embodiment/dexterous-manipulation/) · [Tactile Sensing & Electronic Skin](/robotics/embodiment/tactile-sensing/) · **Robot Autonomy Destination** · **Neura Robotics** · **Mems Sensing Actuation**
