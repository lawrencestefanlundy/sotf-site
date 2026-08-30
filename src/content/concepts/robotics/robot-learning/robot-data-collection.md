---
type: concept
slug: robot-data-collection
canonical_name: Robot Data Collection (the data-supply stack)
aliases:
- robot data collection
- robot data supply
- robot training data
kind: technology
parent_concepts:
- physical-ai
related_concepts:
- vision-language-action-models
- world-models
- sim-to-real-robot-data
- tactile-sensing
- dexterous-manipulation
sources:
- '[[2026-robot-data-supply-funding-wave]]'
frontier:
- Which data source actually scales to a robot 'GPT-3 moment'? EgoScaler hints at a log-linear scaling law for egocentric video; no manipulation scaling law demonstrated yet.
- Tactile/contact is the one BINDING sensor modality (not in video or teleop pose); everything else (depth, RGB, proprioception) is solved/commodity.
last_updated: '2026-06-13'
tags:
- concept
- technology
- robotics
- data
- sensors
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: vision-language-action-models
  name: Vision-Language-Action (VLA) Models
  path: /robotics/robot-learning/vision-language-action-models/
  macro: robotics
- slug: world-models
  name: World Models (for robotics & autonomy)
  path: /robotics/robot-learning/world-models/
  macro: robotics
- slug: sim-to-real-robot-data
  name: Sim-to-Real, Robot Simulation & Synthetic Data
  path: /robotics/robot-learning/sim-to-real-robot-data/
  macro: robotics
- slug: tactile-sensing
  name: Tactile Sensing & Electronic Skin
  path: /robotics/embodiment/tactile-sensing/
  macro: robotics
- slug: dexterous-manipulation
  name: Dexterous Manipulation & Robot Hands
  path: /robotics/embodiment/dexterous-manipulation/
  macro: robotics
---
> The substrate under [Physical AI (robotics cluster hub)](/robotics/robot-learning/physical-ai/): how you actually MANUFACTURE the training data for robot foundation/world models, since there is no internet-of-robot-actions to scrape. This is the picks-and-shovels layer; the investability router is **Robot Data Supply Stack**.

## It's a stack, not a versus

The central 2026 reframe: it is not teleop vs sim vs video. Each source supplies a different property and you need all of them: **teleop = fidelity** (native, on-distribution, expensive), **simulation = scale** (cheap, but contact-physics-poor), **human video = diversity** (internet-scale priors, but the embodiment gap), **world models = counterfactuals** (dreamed rollouts, but physically inconsistent), **tactile = the missing modality** (force/slip/contact, absent from all the others). The investment question (→ **Robot Data Supply Stack**) is which *layer* has a defensible wedge.

## The nine data sources

1. **Teleoperation capture** — leader-follower rigs (ALOHA ~$20-32k; Mobile ALOHA +base). Gold-standard data; cost curve ~$340/hr (2024) → ~$118/hr (2026), but ~300-1,200 demos/task = $50-150k. The 1:many operator-scaling software (PATO) is the prize. See **Teleoperation Bridge**.
2. **Handheld / wearable capture** — UMI (handheld gripper + GoPro, no robot needed), DexUMI (hand exoskeleton for dexterous capture), data gloves (SenseGlove R1). The cheap-data frontier, but the methodology is open-sourced from academia faster than a hardware moat forms.
3. **Egocentric human video** — Ego4D, Apple EgoDex (829 hrs, hand pose), EgoScaler (20,854 hrs, hinted log-linear scaling law); captured on Meta Aria Gen 2. Diversity at scale, but human→robot transfer is bounded by the embodiment gap (works for intent/navigation, not yet reliable for manipulation).
4. **Simulation & synthetic** — Isaac Sim/Lab, Genesis; vendor layer Lightwheel (SimReady assets). NVIDIA-adjacent. See [Sim-to-Real, Robot Simulation & Synthetic Data](/robotics/robot-learning/sim-to-real-robot-data/).
5. **World-model-generated** — NVIDIA Cosmos / GR00T-Dreams, 1X world model, DeepMind Genie 3. Dreamed rollouts, gated by physical consistency (grasping/contact unreliable). See [World Models (for robotics & autonomy)](/robotics/robot-learning/world-models/).
6. **Real-world fleet self-reinforcing loop** (more usage gives more data, which improves the product and drives more usage) — Figure (watch humans), 1X (embody robots, teleop in homes), Tesla (simulate), Neura (build a gym). Most claimed, fewest real: nobody has a proven *manipulation* self-reinforcing loop yet (Tesla/Waymo have it for driving).
7. **Tactile / contact capture** — the under-built modality; force/slip/shear during teleop or via instrumented grippers/skins. Where the 2026 capital is rushing (PaXini, DAIMON). See [Tactile Sensing & Electronic Skin](/robotics/embodiment/tactile-sensing/).
8. **Sensors as substrate** — tactile (binding) > force-torque > event cameras (niche-binding) > depth/LiDAR/RGB/proprioception (commodity). Tactile is the one binding constraint on data quality.
9. **Data-as-a-service / data engine** — Encord (the multimodal platform, the venture-scale layer) vs annotation services (Objectways, the commodity/services trap).

## Why it matters

## Connections

[Physical AI (robotics cluster hub)](/robotics/robot-learning/physical-ai/) · **Robot Data Supply Stack** · **Teleoperation Bridge** · **Robot Foundation Models** · [World Models (for robotics & autonomy)](/robotics/robot-learning/world-models/) · [Sim-to-Real, Robot Simulation & Synthetic Data](/robotics/robot-learning/sim-to-real-robot-data/) · [Tactile Sensing & Electronic Skin](/robotics/embodiment/tactile-sensing/) · **Tactile Sensing Silicon** · **Robot Autonomy Destination**
