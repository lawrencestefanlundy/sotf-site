---
type: concept
slug: fiber-optics
canonical_name: Fiber Optics
aliases: []
kind: technology
parent_concepts:
- communications
- fibre-and-free-space
related_concepts: []
sources:
- '[[2025-09-23-the-compute-gradient]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 13
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-09-23-the-compute-gradient
  title: The Compute Gradient
  date: '2025-09-23'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors: []
---
## Physics / mechanism

Fiber optics transmit data as photons through total internal reflection in a glass or polymer core (refractive index ~1.45 for silica) clad in a lower-index material. Single-mode fiber (SMF, core ~9 µm) dominates long-haul; multimode (50–62.5 µm core) suits short-reach datacenter links. Attenuation in SMF sits around 0.2 dB/km at 1550 nm. Modern coherent systems using DP-QAM push >800 Gbps per wavelength; DWDM aggregates 80–160 channels per fiber. Hollow-core fiber (HCPCF) is the current frontier—sub-0.1 dB/km demonstrated, near-zero nonlinearity, ~30% lower latency than SMF.

## Competitive landscape

Copper interconnects (DAC/AOC cables) dominate <2 m links on cost; silicon photonics co-packaged with ASICs is compressing the distance at which fiber becomes necessary. Free-space optical (FSO) and mmWave compete for last-mile and inter-satellite links. Plastic optical fiber (POF) addresses automotive/consumer on cost. The real competitive tension is fiber *plus* integrated photonics versus all-electrical SerDes scaling—fiber wins on reach and energy-per-bit above ~1 m in high-bandwidth-density scenarios.

| Approach | Reach | $/Gbps | Limitation |
|---|---|---|---|
| SMF + coherent | >1000 km | Low at scale | Transceiver cost |
| Silicon photonics | <2 km | Falling fast | Coupling loss |
| Copper DAC | <7 m | Very low | Power, bandwidth density |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
