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
- Does photonic compute ship as more than a MAC / interconnect co-processor by 2028?
- Can photonic memory leave lab-stage and remove the electronic-working-memory dependency?
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 88
descendants:
- diffractive-deep-neural-network
- diffractive-deep-neural-networks
- optical-neural-networks
- photonic-compute
- photonic-compute-memory
- photonic-tensor-cores
last_reorg_date: '2026-05-13'
sources_7d: 3
sources_30d: 13
recent_mentions:
- slug: 2026-07-31-inference-silicon-roster-sprint
  title: 'Inference-silicon roster verification sprint: 10 companies for the competitive-analysis capital map'
  date: '2026-07-31'
  kind: web
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
neighbors: []
---
## Physics / mechanism

## Company landscape (2026)

### Free-space-fed · DIGITAL encoding
| **Olix** | UK | oTPU — **free-space optics + novel ~100 GHz electro-absorption SLM** (likely Ge/SiGe at GF 12nm), bit-perfect digital encoding, >25GB SRAM + 3TB DRAM (no HBM); **$160M raised, $75M round live ~$850-900M pre** (founder transcript corrects the press "$220M/>$1B") | active; first clusters target Q4'27 |

**Lane record (11 Jul 2026):** no all-optical digital player has publicly demonstrated ≥1 GHz system clock; best-ever bistable-VCSEL cascade is 2 stages (Kawaguchi/Katayama, NAIST, wound down ~2016).

### Integrated PIC · workload-specific
| **Optalysys** | UK | optical accelerator for **FHE / homomorphic encryption**; ~$50M+ (raise early 2026) | active |

### Pivoted / defunct / mis-categorised (do not treat as live optical-compute)
- **Salience Labs** — **pivoted** photonic compute → optical *switches* ($30M Series A 2025); now a switch-layer play.
- **Lighton** — **pivoted** to generative-AI **software** (Euronext-listed Nov 2024); optical hardware (OPU random projections, once in the Jean Zay TOP500 machine) discontinued in all but name. The instructive failure: the fixed random matrix its hardware computed wasn't a workload anyone paid for.
- **Fathom Computing** (US) — free-space NN *training* in light; demoed 2018-19, dormant since (~$6M raised). *(untracked — dead)*
- **Luminous Computing** — **effectively defunct** (photonics team gutted 2023; asset auctions). The old "$120M, Bill-Gates-backed" reference is stale.
- **Celestial Ai** — **interconnect, not compute** (Photonic Fabric; being acquired by Marvell ~$3.25B).
- **Taalas** — **not optical** (model-specific ASIC etched in silicon).

### vs other compute approaches
| Approach | Latency | Power | Maturity |
|---|---|---|---|
| Photonic MZI mesh / free-space | Sub-ns | ~10 fJ/MAC optical | Pre-production |
| Analog SRAM compute | ~10 ns | ~1 pJ/MAC | Production (edge) |
| Digital GPU/TPU | ~100 ns | ~10 pJ/MAC | Mature |

Adjacent (not optical compute): in-memory SRAM (Mythic), neuromorphic (Loihi, NorthPole), and the **thermodynamic** plays (**Normal Computing**, extropic). Optical *interconnect* (Ayar, NcodiN) and *switching* (OCS/OPS) are separate layers — see [Datacenter Optical Networking — Plain-English Stack Primer](/communications/optical-interconnect/datacenter-network-stack/).

## Investment relevance (all routes)
The market read and routing live on **Photonic Compute Market** (interconnect/IO → public markets; workload-native + enabling-layer EU pre-seed → venture routes). GlobalFoundries' silicon photonics PDK (GF Fotonix, 300mm) is a manufacturing hook — companies fabbing on GF get photonic IP access without captive fab risk, and a GF tape-out commitment is a seriousness signal for any early-stage entrant. Enterprise-software exposure (Lunar lens) intersects where photonic inference sits behind API abstractions.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Does photonic compute ship as more than a MAC / interconnect co-processor by 2028?
- Can photonic memory leave lab-stage and remove the electronic-working-memory dependency?

## Update 10 Jul 2026 — the buyer-KPI test

Placed in the **Inference Economics** frame (the 2 customer KPIs): photonic INTERCONNECT moves the datacentre tokens/watt KPI at system level and is where photonic value has actually settled (Lightmatter Passage, Celestial→Marvell $3.25B, the Salience pivot); photonic COMPUTE has yet to publish a buyable number on either KPI, failing the edge envelope on laser static power (Roelkens, 6 Jul 2026: no credible path; µW static needs hero photonic-crystal cavity lasers — **2026 07 06 Lawrence Re Quick Question On Laser Logic**) and inheriting an OEO conversion tax analogous to the [ADC Bottleneck (analog in-memory compute)](/compute/compute-architecture/adc-bottleneck/) in the datacentre. Company mapping: **2026 07 10 Two Kpi Approach Map**.

**The depth ceiling — the single most useful benchmark on this page.** The basic photonic functional unit is a **Mach-Zehnder interferometer**, performing an SU(2) matrix multiplication. Losses accumulate as they are stacked, capping the achievable **depth**, and depth sets the matrix size that can be mapped onto the chip.

| | Matrix size |
|---|---|
| NVIDIA GPU core (8-bit / 4-bit, CUDA-optimised) | **256 × 256** |
| Photonic state of the art | **8 - 32** |

The 8 figure traces to the original **Lightmatter** / **Lightelligence** work; later results go slightly higher with caveats. **This is a component-level gap, not an integration or packaging problem** — which is why packaging progress (co-packaged optics, foundry access) does not by itself close it. Two routes exist: accept a fixed depth and optimise energy/latency around it, or improve components to raise depth.

**Where the latency actually comes from.** Two conversions must be reasoned about separately:
1. **Digital-to-analog (DAC/ADC)** — the real source. Board-level parts run kHz-MHz, so **microseconds**. Giga-samples/sec needs a **custom analog ASIC** (done in transceivers), but a **large bank** of such ADCs has not been built.
2. **Electronic-to-photonic** — **not** a meaningful latency contributor; high-speed and compact, mature off the back of the transceiver industry.

**All-optical latency floor** is photon transit: roughly *c* divided by refractive index (~50-70% of *c*), so a couple of millimetres ≈ 1 ns. Going sub-nanosecond means shrinking footprint, pushing toward costlier optical lithography or **e-beam, which is not CMOS-standard**.

**Latency is usually the wrong axis.** Bandwidth scales with modulation rate (picosecond-class modulation → data every ~10 ps) and again with wavelength-division multiplexing, which is what optical communications already exploits.

**Linear versus nonlinear.** Linear operations are coherent, dissipate no energy and are straightforward on silicon photonics — the natural target. Nonlinear operations need new materials or device engineering with no clear advantage over digital. Hence photonic chips are **not general-purpose**: the discipline is deciding, per computation, whether the optical domain earns its place. The conversion penalty falls sharply when data is **already analog** (sensing) or **already optical** (LiDAR, cameras, optical networks).

