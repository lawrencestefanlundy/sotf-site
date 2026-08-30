---
type: concept
slug: physical-ai
canonical_name: Physical AI (robotics cluster hub)
aliases:
- physical ai
- embodied ai
- embodied intelligence
kind: category
parent_concepts:
- robotics-autonomous-systems
related_concepts:
- humanoid-robots
- vision-language-action-models
- world-models
- sim-to-real-robot-data
- dexterous-manipulation
- tactile-sensing
- robot-actuators
- robot-data-collection
sources:
- '[[2025-04-23-what-if-ai-can-already-feel]]'
- '[[2025-03-26-on-educating-our-children-in-the]]'
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2025-10-21-ceva-introduces-wi-fi-7-1x1-client-ip-to-power-smarter-more-]]'
- '[[2026-robot-data-supply-funding-wave]]'
- '[[2026-04-20-robot-autonomy-destination-bessemer-venture-partners]]'
- '[[2026-08-06-the-year-ai-science-and-the-physical-ai-industry-came-alive]]'
- '[[2026-04-20-physical-ai-deploys-this-decade-bessemer-predicts-robotics]]'
- '[[2026-07-01-sensifai-memo-streaming-physical-ai]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-06-13-sovereign-electronics-manufacturing-reshoring-digest]]'
- '[[2026-04-27-physical-ai-that-moves-the-world-qasar-younis-peter-ludwig-a]]'
frontier:
- Is there a robotics scaling law (data->capability) yet? No, as of mid-2026 (the missing GPT-3 moment).
- 'Which layer of the stack captures durable value: foundation models, OEMs, or the picks-and-shovels (sim, compute, sensing, actuation)?'
last_updated: '2026-06-13'
tags:
- concept
- category
- robotics
- physical-ai
- hub
descendants:
- dexterous-manipulation
- humanoid-robots
- robot-actuators
- robot-data-collection
- sim-to-real-robot-data
- tactile-sensing
- vision-language-action-models
- world-models
mention_count: 75
sources_7d: 0
sources_30d: 7
recent_mentions:
- slug: 2026-08-06-the-year-ai-science-and-the-physical-ai-industry-came-alive
  title: The Year AI Science and the Physical AI Industry Came Alive
  date: '2026-08-06'
  kind: web
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-26-unitree-ipo-shipment-and-segment-data
  title: 'Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-01-sensifai-memo-streaming-physical-ai
  title: SensifAI — Purpose-Built Silicon for Streaming Physical AI (funding memo)
  date: '2026-07-01'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-robot-data-supply-funding-wave
  title: 'Robot data-supply & sensor layer funding wave (2025-26): PitchBook, Encord, PaXini, DAIMON'
  date: '2026-06-13'
  kind: web
- slug: 2026-06-13-sovereign-electronics-manufacturing-reshoring-digest
  title: 'Western/European electronics manufacturing reshoring (PCB/PCBA): market + why-now digest'
  date: '2026-06-13'
  kind: web
neighbors:
- slug: humanoid-robots
  name: Humanoid Robots
  path: /robotics/embodiment/humanoid-robots/
  macro: robotics
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
- slug: dexterous-manipulation
  name: Dexterous Manipulation & Robot Hands
  path: /robotics/embodiment/dexterous-manipulation/
  macro: robotics
- slug: tactile-sensing
  name: Tactile Sensing & Electronic Skin
  path: /robotics/embodiment/tactile-sensing/
  macro: robotics
- slug: robot-actuators
  name: Robot Actuators (the muscle layer)
  path: /robotics/embodiment/robot-actuators/
  macro: robotics
- slug: robot-data-collection
  name: Robot Data Collection (the data-supply stack)
  path: /robotics/robot-learning/robot-data-collection/
  macro: robotics
---
> **The hub page for the robotics / physical-AI cluster.** "Physical AI" is the industry framing (pushed hardest by NVIDIA/Jensen Huang) that AI moves from the digital world into the physical one: robots, AVs, any agent that perceives and acts on reality. Substance ~85%, marketing the rest: the enabling stack is real and two segments (surgical, defense) have real revenue, but the "ChatGPT moment for robotics" claim is not yet earned (no demonstrated scaling law; contact-rich dexterity unsolved). This page maps the cluster and states the spine; the sub-pages carry the detail.

## The spine (one paragraph)

The thing that was missing in robotics for decades was cognition, not actuators, and foundation models supplied it. That unlocked a genuine inflection (VLA deployment adoption <5% 2024 -> ~40% 2026). But general-purpose open-world dexterity stays bottlenecked, specifically on **contact/tactile data and control** that isn't in internet video and isn't well-simulated. So the near-term reality is humans-in-the-loop deployment (**Teleoperation Bridge**) while autonomy compounds (**Robot Autonomy Destination**), and the durable value accrues to the data/sim self-reinforcing loop (more usage gives more data, which improves the product and drives more usage) + the component picks-and-shovels, not the OEMs (margin-compressing) or commoditised open models.

## The three-computer framework (the load-bearing mental model, and a GPU funnel)

1. **Train** (datacentre GPUs) — the foundation model / policy. See [Vision-Language-Action (VLA) Models](/robotics/robot-learning/vision-language-action-models/).
2. **Simulate** (Omniverse + Cosmos) — synthetic data + digital-twin validation. See [Sim-to-Real, Robot Simulation & Synthetic Data](/robotics/robot-learning/sim-to-real-robot-data/), [World Models (for robotics & autonomy)](/robotics/robot-learning/world-models/).
3. **Deploy** (Jetson/Thor onboard) — runs the model on the robot. See **Nvidia Jetson**.
Each step is, conveniently, an NVIDIA platform.

## The bottleneck stack (most -> least solved)

locomotion ✅ → navigation/perception ✅ → semantic grounding (VLAs) 🟡 → world models / synthetic data 🟡 → **contact-rich manipulation ❌ → [dexterity / hands](/robotics/embodiment/dexterous-manipulation/) ❌ → [tactile readout at the edge](/robotics/embodiment/tactile-sensing/) ❌**. The unsolved end is where the deep-tech / semiconductor-adjacent alpha sits.

## Cluster map

**Market spine:** **Robotics Autonomous Systems** (the $38B+ market) · this hub.

**Concepts (technologies):** [Humanoid Robots](/robotics/embodiment/humanoid-robots/) · [Vision-Language-Action (VLA) Models](/robotics/robot-learning/vision-language-action-models/) · [World Models (for robotics & autonomy)](/robotics/robot-learning/world-models/) · [Sim-to-Real, Robot Simulation & Synthetic Data](/robotics/robot-learning/sim-to-real-robot-data/) · [Dexterous Manipulation & Robot Hands](/robotics/embodiment/dexterous-manipulation/) · [Tactile Sensing & Electronic Skin](/robotics/embodiment/tactile-sensing/) · [Robot Actuators (the muscle layer)](/robotics/embodiment/robot-actuators/) · [Robot Data Collection (the data-supply stack)](/robotics/robot-learning/robot-data-collection/)

## Routing (all-vehicles)

## Sources

<!-- dataview block stripped for public site -->
