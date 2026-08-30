---
type: concept
slug: digital-twin
canonical_name: Digital Twin
aliases:
- digital twins
parent_concepts: []
related_concepts:
- datacenter-network-stack
last_updated: '2026-07-01'
tags:
- concept
sources:
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2023-05-25-interview-ben-mildenhall-co-inventor]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2024-11-12-atomic-energy-can-nuclear-power-our]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-12-18-digital-twins-for-chip-manufacturing-rd-faces-unexpected-set]]'
- '[[2026-07-27-embedd-bsp-generation]]'
- '[[2025-07-21-intel-18a-details-cost-future-of-dram-4f2-vs-3d-backside-pow]]'
- '[[2023-01-10-eth-zurich-spin-offs-digital-twins-new-cancer-treatments-and]]'
mention_count: 72
sources_7d: 0
sources_30d: 18
recent_mentions:
- slug: 2026-07-27-embedd-bsp-generation
  title: Embedd — BSP, driver and devicetree generation from chip documentation
  date: '2026-07-27'
  kind: web
- slug: 2025-12-18-digital-twins-for-chip-manufacturing-rd-faces-unexpected-set
  title: Digital Twins for Chip Manufacturing R&D Faces Unexpected Setback - IEEE Spectrum
  date: '2025-12-18'
  kind: web
- slug: 2025-07-21-intel-18a-details-cost-future-of-dram-4f2-vs-3d-backside-pow
  title: Intel 18A Details & Cost, Future of DRAM 4F2 vs 3D, Backside Power Adoption (or Not), China’s FlipFET, Digital Twins from Atoms to Fabs, and More
  date: '2025-07-21'
  kind: web
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
- slug: 2025-01-27-ai-for-nuclear-fusion-feat-martin
  title: AI for Nuclear Fusion (Feat. Martin Riedmiller, Google DeepMind)
  date: '2025-01-27'
  kind: substack
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
- slug: 2024-11-12-atomic-energy-can-nuclear-power-our
  title: 'Nuclear Fission: A Primer'
  date: '2024-11-12'
  kind: substack
- slug: 2023-05-25-interview-ben-mildenhall-co-inventor
  title: '☎️ Interview: Ben Mildenhall, Co-Inventor of Neural Radiance Fields (NeRFs) on the State of the Neural Rendering, Generative AI, and the Metaverse #007'
  date: '2023-05-25'
  kind: substack
neighbors:
- slug: datacenter-network-stack
  name: Datacenter Optical Networking — Plain-English Stack Primer
  path: /communications/optical-interconnect/datacenter-network-stack/
  macro: communications
---
A calibrated, executable software model of a physical system used to simulate, predict and optimise its behaviour before (or instead of) acting on the real thing. In the datacentre context the KB separates two axes that get conflated (see **Datacentre Operational Twin**):

- **Physical / facility twin** — power, thermal, airflow, buildout (CFD-based). Incumbents: **Cadence** Reality, NVIDIA Omniverse DSX, Ansys/**Synopsys**, Schneider/**Vertiv**.
- **Compute + networking performance twin** — throughput, GPU utilisation, fabric congestion, traffic arrivals. Thinner ground: **Keysight** KAI (emulation-for-validation), **Alphatango** (runtime closed-loop), open-source ASTRA-sim / Vidur as the baseline.
- **Design-time vs runtime** is the orthogonal cut: build-it-right (EDA) vs run-it-right (operations).
