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
- '[[2026-05-24-mose2-exciton-polariton-all-optical-switch]]'
- '[[2025-07-14-solving-compute-crisis-physics-based-asics]]'
- '[[2023-03-29-oxford-spinout-lumai-secures-11m-grant-to-power-optical-comp]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 44
descendants:
- diffractive-deep-neural-network
- diffractive-deep-neural-networks
- optical-neural-networks
- photonic-compute
- photonic-compute-memory
- photonic-tensor-cores
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 12
recent_mentions:
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2025-07-14-solving-compute-crisis-physics-based-asics
  title: Solving the compute crisis with physics-based ASICs
  date: '2025-07-14'
  kind: web
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
neighbors: []
---
## Physics / mechanism

## Company landscape (2026)

Two axes split the field: **free-space vs integrated-photonic (PIC)**, and **analog matmul vs all-optical-digital vs workload-specific**. Most players do analog matmul for AI inference; the contrarians are Akhetonics (all-optical digital) and Optalysys (FHE/crypto). *(Web-verified 2026-05-30; funding/status confidence-flagged on each company page.)*

### Integrated PIC · all-optical DIGITAL (contrarian)
| **Akhetonics** | DE | all-optical general-purpose **digital** processor (no electronics in compute path); €6M, 2024 | prototype |

### Integrated PIC · workload-specific
| **Optalysys** | UK | optical accelerator for **FHE / homomorphic encryption**; ~$50M+ (raise early 2026) | active |

### Pivoted / defunct / mis-categorised (do not treat as live optical-compute)
- **Salience Labs** — **pivoted** photonic compute → optical *switches* ($30M Series A 2025); now a switch-layer play.
- **Lighton** — **pivoted** to generative-AI **software** (Euronext-listed); optical hardware deprioritised.
- **Luminous Computing** — **effectively defunct** (photonics team gutted 2023; asset auctions). The old "$120M, Bill-Gates-backed" reference is stale.
- **Celestial Ai** — **interconnect, not compute** (Photonic Fabric; being acquired by Marvell ~$3.25B).
- **Taalas** — **not optical** (model-specific ASIC etched in silicon).

### vs other compute approaches
| Approach | Latency | Power | Maturity |
|---|---|---|---|
| Photonic MZI mesh / free-space | Sub-ns | ~10 fJ/MAC optical | Pre-production |
| Analog SRAM compute | ~10 ns | ~1 pJ/MAC | Production (edge) |
| Digital GPU/TPU | ~100 ns | ~10 pJ/MAC | Mature |

Adjacent (not optical compute): in-memory SRAM (Mythic), neuromorphic (Loihi, NorthPole), and the **thermodynamic** plays (**Normal Computing**, extropic). Optical *interconnect* (Ayar, NcodiN) and *switching* (OCS/OPS) are separate layers — see [Datacenter Optical Networking — Plain-English Stack Primer](/sotf-site/communications/optical-interconnect/datacenter-network-stack/).

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
