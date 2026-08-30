---
type: concept
slug: sim-to-real-robot-data
canonical_name: Sim-to-Real, Robot Simulation & Synthetic Data
aliases:
- sim-to-real
- robot simulation
- synthetic data robotics
kind: technology
parent_concepts:
- physical-ai
related_concepts:
- world-models
- vision-language-action-models
- dexterous-manipulation
sources: []
frontier:
- Contact-rich/deformable physics fidelity is the bottleneck (visual fidelity is largely solved). Teams still see 20-40% drops on contact-rich transfer.
- Does sim+synthetic genuinely close the data gap, or only for the easy (rigid, locomotion) subset?
last_updated: '2026-06-13'
tags:
- concept
- technology
- robotics
- simulation
- data
mention_count: 4
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: world-models
  name: World Models (for robotics & autonomy)
  path: /robotics/robot-learning/world-models/
  macro: robotics
- slug: vision-language-action-models
  name: Vision-Language-Action (VLA) Models
  path: /robotics/robot-learning/vision-language-action-models/
  macro: robotics
- slug: dexterous-manipulation
  name: Dexterous Manipulation & Robot Hands
  path: /robotics/embodiment/dexterous-manipulation/
  macro: robotics
---
Train policies in fast, cheap simulation, then transfer to physical robots. The **sim-to-real gap** is the performance drop on transfer, caused by physics mismatch (especially contact/friction), sensing, and appearance. **Domain randomisation** (randomise textures, masses, friction, lighting) makes the real world look like just another sample, forcing robust policies. This is the data-supply answer to the robot data bottleneck, the flip side of the **teleop-data** answer.

## Tooling

- **NVIDIA Isaac Sim 5.0 / Isaac Lab 2.2** (open-sourced 2025) — GPU-native, photoreal (Omniverse/USD), large-scale parallel RL; the de-facto framework by adoption. Pairs with [Cosmos](/robotics/robot-learning/world-models/) for synthetic data and **Jetson** for deploy.
- **Genesis** (open-source, Genesis AI) — unified multi-physics, pure-Python, differentiable tactile; headline "10-80x faster" claim is benchmark-dependent, treat with caution.
- **MuJoCo / MJX** (DeepMind) — the gold standard for contact-dynamics accuracy; the reference others benchmark against.

## Why contact-rich / deformable sim is still hard

Contact is stiff, discontinuous, and numerically nasty: real contact involves deformation, micro-slip, adhesion, and stochastic surface effects that solvers approximate poorly. Deformables (cloth, cable, food, soft tissue) compound it. Hard numbers from the 2025-26 literature: photoreal-sim teams still see **20-40% drops on contact-rich tasks**, and deformable/complex-contact tasks can need **5,000+ real demonstrations** because sim approximates them badly.

## Is sim+synthetic closing the data gap?

Partially and unevenly. **Closing well:** locomotion, navigation, rigid pick-and-place, perception (domain randomisation works). **Still open:** dexterous, contact-rich, deformable manipulation, the high-value tasks. Visual fidelity is largely solved; **physics fidelity is the bottleneck.** So "sim+synthetic closes the data gap" is marketing for the hardest manipulation, which is exactly why the data bottleneck in **Robot Autonomy Destination** is sticky, and why **native teleop data** still matters. Confidence sim is materially reducing real-data needs for a subset of tasks: ~75%.

## Connections

[Physical AI (robotics cluster hub)](/robotics/robot-learning/physical-ai/) · [World Models (for robotics & autonomy)](/robotics/robot-learning/world-models/) · [Vision-Language-Action (VLA) Models](/robotics/robot-learning/vision-language-action-models/) · [Dexterous Manipulation & Robot Hands](/robotics/embodiment/dexterous-manipulation/) · **Robot Autonomy Destination** · **Teleoperation Bridge**
