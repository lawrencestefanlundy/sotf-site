---
type: concept
slug: vision-language-action-models
canonical_name: Vision-Language-Action (VLA) Models
aliases:
- VLA
- VLA models
- robot foundation models
kind: technology
parent_concepts:
- physical-ai
related_concepts:
- world-models
- sim-to-real-robot-data
- dexterous-manipulation
- low-power-edge-compute
sources:
- '[[2026-06-23-dataintelo-vla-models-market]]'
- '[[2026-06-23-state-of-robotics-2026]]'
- '[[2026-06-23-kaiso-vla-models-market]]'
frontier:
- Cross-embodiment ACTION transfer is a fundamental unsolved challenge (a policy trained on one body rarely transfers to a different-DOF body).
- Is there a data-scaling law? No demonstrated step-change where more data alone yields reliable open-world dexterous autonomy (mid-2026).
last_updated: '2026-06-13'
tags:
- concept
- technology
- robotics
- ai
- foundation-models
mention_count: 5
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-06-23-dataintelo-vla-models-market
  title: 'Dataintelo: Vision-Language-Action Models market report'
  date: '2026-06-23'
  kind: web
- slug: 2026-06-23-state-of-robotics-2026
  title: 'Robotics Center: State of Robotics 2026'
  date: '2026-06-23'
  kind: web
- slug: 2026-06-23-kaiso-vla-models-market
  title: 'Kaiso Research: Vision-Language-Action (VLA) Models market analysis'
  date: '2026-06-23'
  kind: web
neighbors:
- slug: world-models
  name: World Models (for robotics & autonomy)
  path: /robotics/robot-learning/world-models/
  macro: robotics
- slug: sim-to-real-robot-data
  name: Sim-to-Real, Robot Simulation & Synthetic Data
  path: /robotics/robot-learning/sim-to-real-robot-data/
  macro: robotics
- slug: dexterous-manipulation
  name: Dexterous Manipulation & Robot Hands
  path: /robotics/embodiment/dexterous-manipulation/
  macro: robotics
---
The robot "brain": a single neural network that ingests camera images + a natural-language instruction and emits robot actions, end-to-end. Lineage is VLM -> VLA: take a web-pretrained vision-language model (inheriting semantic grounding), bolt on an action head trained on robot trajectories.

## The key architectural axis

- **Single-network end-to-end** (RT-2, OpenVLA): one transformer emits action tokens. Simpler; bottlenecked by slow VLM inference for high-frequency control.
- **Dual-system (System 2 / System 1)**: a slow VLM planner (~7-10 Hz) + a fast visuomotor policy (~200 Hz, usually a diffusion or flow-matching transformer). Now the consensus design for humanoid/whole-body control. Used by Figure Helix, NVIDIA GR00T, Gemini Robotics 1.5.

## Leading models (mid-2026)

- **Physical Intelligence π0 / π0.5** — π0 weights open; π0.5 (CoRL 2025) is the most credible open-world generalisation result (cleans unseen homes, noisily). Flow-matching action expert.
- **Google DeepMind Gemini Robotics 1.5 / -ER 1.5** — dual model; the ER reasoning model is open to devs; "Motion Transfer" across embodiments.
- **NVIDIA GR00T N1->N1.7** — the open humanoid foundation model; the point is data-efficiency (GR00T-Dreams synthetic data "36 hours vs 3 months"). Adopters: Boston Dynamics, Agility, XPENG.
- **Figure Helix** (closed), **Skild Brain** (closed, "omni-bodied", least verified), **1X** (paired with its [world model](/robotics/robot-learning/world-models/)).

Open weights: π0, GR00T, OpenVLA, Gemini-ER (reasoning only). Closed: Helix, Skild, π0.5 (paper not weights). NVIDIA is deliberately the open-infra player (to sell GPUs).

## What works vs fails

Works: language grounding, short-horizon pick-place/sort in semi-structured settings, modest transfer to new objects, π0.5-class noisy open-world generalisation. Fails: cross-embodiment action transfer, fine spatial/temporal reasoning, robustness to noise/lighting/distractors/paraphrase, long-horizon tasks, and anything contact-rich ([Dexterous Manipulation & Robot Hands](/robotics/embodiment/dexterous-manipulation/)). New "action hallucination" failure literature is emerging.

## Data sources

Teleop demonstrations (dominant, expensive, doesn't scale, the **Teleoperation Bridge** argument), pooled cross-robot datasets (Open X-Embodiment ~970k trajectories; DROID ~76k), web/VLM pretraining for semantics, egocentric human video (the emerging cheap-data bet), and synthetic/[world-model](/robotics/robot-learning/world-models/) data.

## Why it matters here

This is the layer **Robot Foundation Models** bets on (value capture: commoditising from below via open releases). Generalisation is improving fast (~80% confidence) but maybe not as fast as valuations imply (~60%). The honest read: no GPT-3 moment yet, which is why **Robot Autonomy Destination** stays contested.

## Connections

[Physical AI (robotics cluster hub)](/robotics/robot-learning/physical-ai/) · **Robot Foundation Models** · [World Models (for robotics & autonomy)](/robotics/robot-learning/world-models/) · [Sim-to-Real, Robot Simulation & Synthetic Data](/robotics/robot-learning/sim-to-real-robot-data/) · **Robot Autonomy Destination** · **Teleoperation Bridge** · runs on **Nvidia Jetson**
