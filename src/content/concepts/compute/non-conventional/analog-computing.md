---
type: concept
slug: analog-computing
canonical_name: Analog Computing
aliases: []
kind: technology
parent_concepts:
- compute
- non-conventional
related_concepts: []
sources:
- '[[2023-09-18-e15-in-conversation-with-wisear-on]]'
- '[[2023-09-28-e16-in-conversation-with-shiv-malik]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2023-09-24-e16-in-conversation-with-john-waite]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 14
descendants:
- adc-bottleneck
- charge-domain-compute
- coherent-ising-machine
- coupled-oscillator-networks
- fdtd-calibration-wall
- near-field-rf-coupling
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2025-02-12-wen-babelfish-feat-aron-of-semron
  title: 'Edge AI: Analog Chips (feat. Aron Kirschen, SEMRON)'
  date: '2025-02-12'
  kind: substack
- slug: 2023-09-28-e16-in-conversation-with-shiv-malik
  title: '☎️ E17: In Conversation with Shiv Malik, CEO of Pool.io on the State of Data Unions 🤝₿'
  date: '2023-09-28'
  kind: substack
- slug: 2023-09-24-e16-in-conversation-with-john-waite
  title: '☎️ E16: In Conversation with John Waite, Co-Founder and CEO of Phycobloom and a Breakthrough Energy Fellow on the State of Biofuels and Algae Fuel 🌱⛽'
  date: '2023-09-24'
  kind: substack
- slug: 2023-09-18-e15-in-conversation-with-wisear-on
  title: '☎️ E15: In Conversation with Wisear on The State of Hearables, Brain Computer Interfaces and Augmented Reality 👂🎧🧠'
  date: '2023-09-18'
  kind: substack
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
- slug: 2023-08-31-e13-chiplets-how-chip-lego-is-driving
  title: '🔮 E13: Chiplets - How Chip Lego is Driving AI Progress'
  date: '2023-08-31'
  kind: substack
- slug: 2023-08-25-e12-nanomechanical-computing-gears
  title: '🔮E12: Nanomechanical Computing- Gears of Space War? Old Ideas at New Scales'
  date: '2023-08-25'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
neighbors: []
---
## Physics / mechanism

Analog computing encodes information as continuous physical quantities—voltage, current, charge, optical intensity—rather than discrete bits. Computation occurs via physical law: matrix-vector multiplication maps directly onto Kirchhoff's current law in resistive crossbar arrays, or onto interference in photonic meshes. Key parameters: energy-per-MAC (multiply-accumulate), precision (typically 4–8 effective bits vs. digital's 32), throughput density, and drift/noise floors. State of the art: memristor crossbars demonstrate sub-fJ/MAC at 8-bit equivalent precision; analog photonic accelerators (MIT, Lightmatter) hit >TOPS/W at inference workloads. Core limitation is weight-programming accuracy and device-to-device variability, both active research targets.

## Competitive landscape

Digital ASIC accelerators (Tenstorrent, Groq, Cerebras) dominate on programmability and precision; neuromorphic (Intel Loihi, IBM NorthPole) overlaps on event-driven, low-power inference. Photonic digital interconnect is adjacent but distinct. In-memory computing (SRAM/DRAM analog) competes at the edge.

| Approach | Energy/MAC | Precision | Programmability |
|---|---|---|---|
| Analog crossbar | <1 fJ | 4–8 bit | Low |
| Digital ASIC | ~1–10 pJ | 8–32 bit | High |
| Analog photonic | <0.1 pJ | ~6 bit | Medium |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

## Merged from root duplicate (analog-computing.md at concepts/ root, 2026-06-10)

# Analog / In-Memory Computing

Performing the multiply-accumulate of neural inference inside the memory array (memristor, SRAM, capacitor or flash crossbars) rather than shuttling data to a digital ALU, trading numerical precision for a large energy-per-MAC win. The architectural answer to the memory-bound-AI problem that **Memcapacitor Compute Memory Bound Ai** and **Hbm Free Inference Architectures** bet on; adjacent to but distinct from digital [Processing-in-Memory (PIM)](/sotf-site/memory/emerging-memory/processing-in-memory/).
