---
type: concept
slug: lunar-teleoperation
canonical_name: Lunar Teleoperation
aliases:
- lunar teleop
- moon teleop
kind: framework
domain:
- sotf
- lunar
parent_concepts:
- life-frontier
- space
related_concepts:
- edge-ai
- autonomous-systems
companies_using:
- anthrotronix
- astrobotic-technology
- clearpath-robotics-a-rockwell-automation-company
- comex
- gitai-usa
- gitai
- honeybee-robotics
- intuitive-machines
- iris-automation-iris-robotics-for-space
- ispace-europe-ispace-technologies-us-eu-subsidiary
- ispace-japan
- jaxa-toyota-lunar-cruiser-toyota-motor-corporation
- kepler-communications
- kongsberg-discovery-kongsberg-maritime
- lunar-outpost
- motiv-space-systems
- oceaneering-space-systems
- robots-in-space-ris
- rollin-justin-dlr-robotics-german-aerospace-center
- space-applications-services
- space-machine-engineering-sme
- spacebit
- ssl-maxar-space-systems
- xcorporeal-xarc-xplore-inc
ideas_referencing: []
sources: []
frontier:
- Latency budget — what closed-loop control is feasible at 1.3-2.7s round-trip?
- Hardware stack (compute, sensors, comms) compatible with lunar surface conditions
- Operator UX paradigm — how do you pilot through latency? Predictive control?
last_updated: '2026-05-04'
tags:
- concept
- framework
- research
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---


# Lunar Teleoperation

*Active research thread. Half-day per week. Connected to State of the Future writing + Telekine DD work.*

## What it is

Operating robots and equipment on the lunar surface from Earth despite the Earth-Moon round-trip latency (~1.3-2.7 seconds). Distinct from full autonomy (where the on-board AI decides) and from low-latency teleoperation (where humans drive directly). It's a hybrid: human strategic intent + AI tactical execution + delayed-feedback human-in-the-loop oversight.

## Why now

Three converging signals:

1. **NASA Artemis + commercial lunar landers** create a market for surface operations from 2026-2030.
2. **CHIPS Act + space industrial policy** funds rad-hard / lunar-grade compute and sensors.
3. **Foundation models + closed-loop control** are bridging the human-in-the-loop / autonomous gap on Earth (Wayve, Tesla FSD lineage). The same architectures may transfer to lunar with latency adapters.

## Open research questions

| Question | Notes |
|----------|-------|
| Latency budget | What closed-loop control is feasible at 2.6s round-trip? Predictive layers, on-board safety reflex, delayed human approval — the architecture that handles all three. |
| Hardware stack | Lunar surface: ±150°C thermal cycle, vacuum, radiation, dust. What compute/comms hardware survives? |
| Operator UX | How does a human pilot through latency? Tesla / Wayve patterns vs. surgical robotics vs. drone teleop. |
| Mission economics | Hours of operator time vs. autonomy hours — what's the human-cost-per-task crossover? |
| Comms architecture | Direct-to-Earth vs. lunar-orbit-relay vs. mesh networks |

## Active threads

- **Telekine DD work** — Lunar Ventures pipeline; specific company doing teleoperation for industrial/extreme environments.
- **Stan Boland conversations** — Wayve founder, autonomous systems lineage. Relevance: foundation-model-based driving stacks may port to teleop.
- **Wayve latency adaptation** — open question, worth a direct conversation.
- **Global Foundries lunar-grade silicon** — does GF have a rad-hard process? Worth asking the LP.

## Connection to investing

Not a Cloudberry deal yet (most lunar-teleop plays are too far out for Fund I). But:

- Could become a **State of the Future** Friday Four piece — frame the hybrid-autonomy thesis.
- Telekine via Lunar Ventures.
- Long-term — Cloudberry could back a teleop hardware enabler (compute, sensors) when the market timing is right.

## Sources

<!-- dataview block stripped for public site -->

## Frontier

See open research questions table above.
