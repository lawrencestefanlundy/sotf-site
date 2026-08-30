---
type: concept
slug: dexterous-manipulation
canonical_name: Dexterous Manipulation & Robot Hands
aliases:
- dexterous manipulation
- robot hands
- in-hand manipulation
kind: technology
parent_concepts:
- physical-ai
related_concepts:
- tactile-sensing
- robot-actuators
- vision-language-action-models
- sim-to-real-robot-data
sources:
- '[[2026-05-15-robot-autonomy-destination-rlwrld-releases-rldx-1-a]]'
frontier:
- 'The four-way hand trade-off (anthropomorphic + durable + cheap + sensorised) is unsolved: tendon-driven = dexterous but fragile/expensive; direct-drive = robust but bulky.'
- Is dexterity gated more by hardware (hands/touch) or by software (policies/data)? Both, and they're coupled.
last_updated: '2026-06-13'
tags:
- concept
- technology
- robotics
- manipulation
mention_count: 1
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-05-15-robot-autonomy-destination-rlwrld-releases-rldx-1-a
  title: RLWRLD releases RLDX-1, a dexterity-first foundation model for robot hands
  date: '2026-05-15'
  kind: web
neighbors:
- slug: tactile-sensing
  name: Tactile Sensing & Electronic Skin
  path: /robotics/embodiment/tactile-sensing/
  macro: robotics
- slug: robot-actuators
  name: Robot Actuators (the muscle layer)
  path: /robotics/embodiment/robot-actuators/
  macro: robotics
- slug: vision-language-action-models
  name: Vision-Language-Action (VLA) Models
  path: /robotics/robot-learning/vision-language-action-models/
  macro: robotics
- slug: sim-to-real-robot-data
  name: Sim-to-Real, Robot Simulation & Synthetic Data
  path: /robotics/robot-learning/sim-to-real-robot-data/
  macro: robotics
---
Contact-rich manipulation: in-hand reorientation, fine grasping, tool use, handling deformables. It requires high-frequency closed-loop control fusing vision *and* touch under contact dynamics that are hard to sense, model, and simulate. **The bottleneck for useful robots.** Locomotion is largely solved; hands are not. ~85% confidence this is *the* gating problem for general-purpose robots.

## Why it's the bottleneck (five coupled reasons)

1. **Sensing** — robots lack the dense, fast, multimodal touch humans have ([Tactile Sensing & Electronic Skin](/robotics/embodiment/tactile-sensing/)); hands move faster than current tactile readout can process.
2. **Control** — high DOF + stiff contact dynamics make control/RL hard (needs the ~200Hz System-1 policies from [Vision-Language-Action (VLA) Models](/robotics/robot-learning/vision-language-action-models/)).
3. **Simulation** — can't cheaply generate contact-rich training data ([Sim-to-Real, Robot Simulation & Synthetic Data](/robotics/robot-learning/sim-to-real-robot-data/); 5,000+ real demos for deformables).
4. **Data** — teleoperating a 20+ DOF hand is itself hard (embodiment gap, operator fatigue), so demonstration data is scarce.
5. **Hardware** — the anthropomorphic/durable/cheap/sensorised four-way trade-off is unsolved ([Robot Actuators (the muscle layer)](/robotics/embodiment/robot-actuators/)).

This is the mechanism behind **Robot Autonomy Destination**: the data bottleneck is specifically a *contact/tactile* bottleneck, which is why video-pretraining (good for "what to do") doesn't fix the physical "how."

## Hand landscape (DOF / actuation / cost / tactile)

- **Shadow Dexterous Hand** — ~24 DOF, tendon-driven, fingertip tactile options. Research gold standard, ~£100k+ class.
- **Wonik Allegro V4/V5** — 16 DOF, direct-drive, ~$17k. The affordable research workhorse for in-hand RL.
- **PSYONIC Ability Hand** — prosthesis-origin, ~6 motors, fingertip touch, low cost.
- **Clone "Hand of Clone"** — 27 DOF, hydraulic myofiber muscles. Most biomimetic, the wildcard (production claims unproven).
- **Tesla Optimus Gen3** — 22 DOF/hand, ~25 actuators relocated to the forearm (the notable engineering move).
- **2025 wave (mostly Chinese: TESOLLO, Unitree Dex5, ROBOTERA, PaXini)** — 12-20 DOF, mostly direct-drive, all shipping with tactile. Rapid cost-down.

## Connections

[Physical AI (robotics cluster hub)](/robotics/robot-learning/physical-ai/) · [Tactile Sensing & Electronic Skin](/robotics/embodiment/tactile-sensing/) · [Robot Actuators (the muscle layer)](/robotics/embodiment/robot-actuators/) · **Robot Autonomy Destination** · **Tactile Sensing Silicon** · [Humanoid Robots](/robotics/embodiment/humanoid-robots/)
