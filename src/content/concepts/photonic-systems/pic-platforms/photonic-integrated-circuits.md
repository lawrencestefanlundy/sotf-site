---
type: concept
slug: photonic-integrated-circuits
canonical_name: Photonic Integrated Circuits
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- pic-platforms
related_concepts: []
companies_using:
- ayar-labs
- bright-photonics
- coherent-corp
- globalfoundries-siph
- hyperlight
- imec
- infinera
- intel-silicon-photonics
- ipronics
- leti-cea-leti-silicon-photonics
- ligentec
- linkra
- lionix-international
- lumentum
- mirico
- photondelta
- poet-technologies
- quintessent
- rockley-photonics
- scintil-photonics
- sicoya
- teramount
- tsmc-photonics
- xanadu
ideas_referencing: []
sources:
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 63
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 3
---

# Photonic Integrated Circuits

*Kind: technology · Attio deal count: 58*

## Physics / mechanism

Photonic integrated circuits (PICs) route, modulate, and detect light on a chip using waveguides, splitters, modulators, and photodetectors fabricated in a common substrate. Silicon photonics dominates volume production—waveguide losses ~1–2 dB/cm, modulators hitting 50–100+ Gb/s per lane via Mach-Zehnder or ring resonator architectures. InP platforms enable monolithic laser integration but at higher cost and smaller wafer size (typically 3-inch vs. 300 mm Si). Silicon nitride (SiN) offers ultra-low loss (~0.1 dB/cm) for sensing and LiDAR. Key metrics: insertion loss, modulation bandwidth, coupling efficiency to fiber, and yield on MPW shuttles. Leading fabs: IMEC, GlobalFoundries (GF Fotonix), Intel, TSMC, Leti.

## Competitive landscape


| Platform | Advantage | Limitation |
|---|---|---|
| Silicon photonics | CMOS-compatible, high volume, low cost | No native laser, two-photon absorption at high power |
| InP | Monolithic laser + modulator integration | Small wafers, expensive, niche foundry base |
| Silicon nitride | Ultralow loss, wide transparency window | No active modulation, passive-only without heterogeneous integration |

## Cloudberry relevance

Competing interconnect approaches: electrical SerDes (reaching physical limits above 1.6 Tb/s per package), free-space optical, and co-packaged optics hybrids. Adjacent material bets include lithium niobate on insulator (LNOI)—thin-film LN pushing >100 GHz EO bandwidth—and III-V-on-Si heterogeneous bonding startups.


GF's Fotonix 300 mm BiCMOS-photonics platform is a direct LP-fund touchpoint—portfolio companies building datacenter transceivers, optical compute interconnects, or photonic sensing can access qualified volume manufacturing without fabless risk. Deal-flow priority: startups designing on SiPh or SiN targeting AI cluster interconnects, optical gyroscopes, or quantum photonics where GF or a tier-2 European foundry is the production path. Lunar Ventures' deep-tech seed exposure surfaces early PIC IP plays worth tracking into Series A.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
