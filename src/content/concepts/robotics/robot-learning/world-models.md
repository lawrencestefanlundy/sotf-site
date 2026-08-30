---
type: concept
slug: world-models
canonical_name: World Models (for robotics & autonomy)
aliases:
- world model
- world models
kind: technology
parent_concepts:
- physical-ai
related_concepts:
- vision-language-action-models
- sim-to-real-robot-data
sources:
- '[[2025-02-05-you-like-ai-agents-you-are-gonna]]'
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2026-07-01-sensifai-memo-streaming-physical-ai]]'
frontier:
- 'Physical consistency: learned video world models look photoreal but don''t guarantee physically valid contacts, the very thing robots need most.'
- Do world models become the cheap data engine that breaks the robot data bottleneck, or a complement that never fixes contact physics?
last_updated: '2026-06-13'
tags:
- concept
- technology
- robotics
- ai
- world-models
mention_count: 34
sources_7d: 0
sources_30d: 8
recent_mentions:
- slug: 2026-07-01-sensifai-memo-streaming-physical-ai
  title: SensifAI — Purpose-Built Silicon for Streaming Physical AI (funding memo)
  date: '2026-07-01'
  kind: web
- slug: 2025-02-05-you-like-ai-agents-you-are-gonna
  title: Decentralised AI (Feat. Richard Blythman of Naptha)
  date: '2025-02-05'
  kind: substack
- slug: 2025-01-27-ai-for-nuclear-fusion-feat-martin
  title: AI for Nuclear Fusion (Feat. Martin Riedmiller, Google DeepMind)
  date: '2025-01-27'
  kind: substack
neighbors:
- slug: vision-language-action-models
  name: Vision-Language-Action (VLA) Models
  path: /robotics/robot-learning/vision-language-action-models/
  macro: robotics
- slug: sim-to-real-robot-data
  name: Sim-to-Real, Robot Simulation & Synthetic Data
  path: /robotics/robot-learning/sim-to-real-robot-data/
  macro: robotics
---
A learned, generative predictive model of how the environment evolves: given an observation (and optionally an action), it predicts future observations (usually video) and/or latent states. Two uses: **planning** (imagine outcomes of candidate actions) and **synthetic data generation** (roll out novel trajectories to train policies without a physical robot).

## How it differs from a VLA

A [VLA](/robotics/robot-learning/vision-language-action-models/) maps observation + instruction -> *action* (it acts). A world model maps observation (+action) -> *future observation* (it imagines/predicts). Increasingly paired: the world model dreams training data or candidate futures, the VLA or an inverse-dynamics model extracts the actions.

## Leading players

- **NVIDIA Cosmos** (Cosmos 3, May 2026) — the platform play: world foundation models generating physics-based video from text/image/sensor inputs, + tokenizers + data-curation. Mixture-of-transformers; Nano/Super/Edge variants. Adopters: 1X, Agility, Figure, Skild.
- **1X World Model** — a 14B video model fine-tuned to the NEO embodiment; text prompt -> predicted future video -> inverse-dynamics -> motor commands. ~11s/rollout (a planning/data tool, not yet closed-loop control). Claims generalisation without large teleop datasets.
- **Wayve GAIA-2** (driving) — multi-view latent-diffusion world model generating rare/dangerous scenarios for AV testing. The most *productionised* world model; driving is the proving ground. See **Wayve**.
- **DeepMind Genie-style** — action-controllable interactive world models from video (research frontier).

## The bet (and its weakness)

World models are the bet that **video is the cheap, abundant data robotics lacks**: learn dynamics from internet/robot video, then generate unlimited photoreal rollouts instead of hand-tuning a physics simulator. The weakness is the same one everywhere in this cluster: learned video models don't guarantee physical consistency, so contact-rich physics (the part robots most need, [Dexterous Manipulation & Robot Hands](/robotics/embodiment/dexterous-manipulation/)) is exactly what they're worst at. They complement [physics simulation](/robotics/robot-learning/sim-to-real-robot-data/), they don't replace it. Confidence the world-model-as-data-engine thesis pays off: ~55%.

## Connections

[Physical AI (robotics cluster hub)](/robotics/robot-learning/physical-ai/) · [Vision-Language-Action (VLA) Models](/robotics/robot-learning/vision-language-action-models/) · [Sim-to-Real, Robot Simulation & Synthetic Data](/robotics/robot-learning/sim-to-real-robot-data/) · **Robot Autonomy Destination** · **Wayve**
