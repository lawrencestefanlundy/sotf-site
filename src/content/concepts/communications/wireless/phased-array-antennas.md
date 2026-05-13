---
type: concept
slug: phased-array-antennas
canonical_name: Phased-Array Antennas
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- communications
- wireless
related_concepts: []
companies_using:
- aeternum-formerly-ignitenet-context-tarana-wireless
- anokiwave
- arralis
- aselsan
- ball-aerospace-bae-systems-division
- eravant-formerly-sage-millimeter
- huawei-wireless-networks-bu
- hybrid-communication-hcc
- intellian-technologies
- isotropic-systems-now-oneweb-eutelsat-subsidiary-context
- marvell-technology
- metawave
- movella-formerly-mcube-memsic-spin-off-context-aside-alcan-s
- pharad
- phasor-solutions
- raytheon-technologies-rtx
- rfaxis
- samsung-electronics-networks-division
- satcom-direct-kymeta
- satixfy
- starlink-spacex
- thinkom-solutions
- viasat
- waveup-wafer-level-packaging-spin-context-gapwaves
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Phased-Array Antennas

*Kind: technology*

## Physics / mechanism

Phased-array antennas steer beams electronically by controlling the phase (and amplitude) of signals fed to each element in an array. Constructive interference reinforces radiation in the target direction; destructive interference suppresses sidelobes. Key parameters: element count (32–4096+ in production systems), phase resolution (4–6 bits typical), scan angle (±60° standard), EIRP, noise figure, and fractional bandwidth. Steering latency is microseconds vs. milliseconds for mechanical gimbals. SoA mmWave phased arrays (24–77 GHz) integrate T/R modules in advanced CMOS or SiGe BiCMOS at 16–28nm nodes; companies like Anokiwave, Movella, and Marvell ship multi-channel beamformer ICs at volume. Satellite comms (LEO terminals), 5G base stations, automotive radar, and AESA defense radars are the primary volume markets.

## Competitive landscape

Competing and adjacent approaches: mechanical steering (cheap, slow, no beam-splitting), switched-beam arrays (lower cost, coarser control), and optical phased arrays (OPAs) for LiDAR and free-space optical comms. Metasurface/RIS (reconfigurable intelligent surfaces) offer passive beam manipulation without active T/R chains but lack full beam-forming flexibility.

## Cloudberry relevance

| Approach | Steering speed | Cost driver | Maturity |
|---|---|---|---|
| Mechanical gimbal | ~100 ms | Mechanical BOM | High |
| Phased array (RF) | ~1 µs | RFIC die area | High |
| Optical phased array | ~1 ns | Photonic foundry NRE | Early commercial |


Cloudberry's angle: phased-array ICs are a volume driver for specialty RF CMOS and SiGe processes—nodes where GlobalFoundries competes directly. OPA convergence with photonic integrated circuits (PICs) is a near-term deal-flow vector: startups integrating III-V gain with silicon photonics for OPA LiDAR or free-space comms land squarely in the Cloudberry / Lunar Ventures sweet spot. Watch for spin-outs from Imec, Fraunhofer IHF, and MIT Lincoln Lab commercialising mmWave T/R chiplets.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
