---
type: concept
slug: photonic-compute
canonical_name: Photonic Compute
aliases:
- photonic processor
- optical computing
kind: technology
parent_concepts:
- photonic-systems
- photonic-compute
related_concepts: []
sources:
- '[[2025-03-12-project-mayhem-ai-inward-collapse]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-03-29-oxford-spinout-lumai-secures-11m-grant-to-power-optical-comp]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 16
descendants:
- diffractive-deep-neural-networks
- optical-neural-networks
- photonic-compute
- photonic-compute-memory
- photonic-tensor-cores
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 3
recent_mentions:
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
- slug: 2025-03-12-project-mayhem-ai-inward-collapse
  title: what happens when we hollow out work?
  date: '2025-03-12'
  kind: substack
- slug: 2023-07-23-analog-computing-the-once-and-future
  title: '🔮 E09: Analog Computing: The Once and Future King'
  date: '2023-07-23'
  kind: substack
- slug: 2023-07-14-e08-optical-computing
  title: '🔮E08: Optical Computing'
  date: '2023-07-14'
  kind: substack
- slug: 2023-03-29-oxford-spinout-lumai-secures-11m-grant-to-power-optical-comp
  title: Oxford spinout Lumai secures £1.1m grant to power optical computing revolution - Oxford University Innovation
  date: '2023-03-29'
  kind: web
neighbors: []
---
## Physics / mechanism

Photonic compute uses light instead of electrons to perform matrix-vector multiplications—the dominant operation in neural network inference. Photons propagate through Mach-Zehnder interferometer (MZI) meshes or microring resonator arrays; weight encoding happens via phase shifts or amplitude modulation. Core advantage: multiply-accumulate operations execute at the speed of light with near-zero dynamic power. Key figures of merit are TOPS/W (demonstrated >1000× over GPU in optical domain, though O/E/O conversion erodes this), bandwidth density (>10 Tbps/mm² on-chip), and precision (typically 4–8 bit equivalent). State of the art: Lightmatter's Passage interconnect, Luminous's in-memory photonic arrays, MIT/Stanford silicon photonics platforms. Integration with CMOS at 300mm wafers remains the manufacturing bottleneck.

## Competitive landscape

Competing approaches: in-memory SRAM/DRAM compute (Mythic, Analog Devices), analog resistive (Mythic, Syntiant), neuromorphic (Intel Loihi, IBM NorthPole). Adjacent: silicon photonics for interconnect (Ayar Labs, Celestial AI) often overlaps with compute claims. Electro-optic modulators and III-V bonding techniques (InP, GaAs) are enabling adjacent material plays.

| Approach | Latency | Power | Maturity |
|---|---|---|---|
| Photonic MZI mesh | Sub-ns | ~10 fJ/MAC optical | Pre-production |
| Analog SRAM compute | ~10 ns | ~1 pJ/MAC | Production (edge) |
| Digital GPU/TPU | ~100 ns | ~10 pJ/MAC | Mature |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
