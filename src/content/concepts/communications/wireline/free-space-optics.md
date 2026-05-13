---
type: concept
slug: free-space-optics
canonical_name: Free-Space Optics
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- communications
- wireline
related_concepts: []
companies_using:
- airbus-defence-space-spacedatahighway-edrs
- arcsec-formerly-ghent-based-spin-off
- ball-aerospace-now-bae-systems
- bridgecomm
- cailabs
- fsona-networks
- general-atomics-coherent-solutions-ga-ems
- iridium-satellite-optical-crosslinks-rd
- laser-light-communications
- lumentum
- mynaric
- nssol-ntt-group-space-optical-comms
- optical-physics-company-opc
- orbits-lightwave-part-of-zortrax-ecosystem
- plaintree-systems-optical-zonu-aoptix-heritage
- sa-photonics
- siklu-part-of-ceragon
- siro-satellite-internet-via-relay-optics
- skyloom-global
- spacex-starlink-laser-inter-satellite-links
- tesat-spacecom
- transcelestial-technologies
- warpspace
- xenomatix-now-part-of-fso-sensing-ecosystem
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


# Free-Space Optics

*Kind: technology*

## Physics / mechanism

Free-space optics (FSO) transmits data as modulated optical beams through air or vacuum—no fiber, no RF spectrum license. A laser (typically 1550 nm, eye-safe, exploits low atmospheric absorption) is collimated, pointed at a receiver aperture, and detected by an APD or PIN photodiode. Key parameters: link distance (100 m–10 km terrestrial, multi-thousand km LEO-to-ground), atmospheric attenuation (fog: 50–300 dB/km; clear air: <1 dB/km), pointing-acquisition-tracking (PAT) precision (sub-µrad for space links), and modulation scheme (OOK, DPSK, coherent QAM). Commercial terrestrial systems hit 10–100 Gbps today; NASA's LLCD/LCRD demonstrated 622 Mbps lunar-orbit, and TBIRD achieved 200 Gbps LEO downlink in 2022—current state-of-the-art for space FSO.

## Competitive landscape

Fiber wins on reliability and distance where infrastructure exists; RF (microwave, mmWave) wins in fog/low-visibility and non-line-of-sight. FSO's niche is last-mile backhaul, inter-satellite links (ISL), and secure point-to-point where spectrum licensing or trenching is prohibitive.

## Cloudberry relevance

| Dimension | FSO | Fiber | mmWave RF |
|---|---|---|---|
| Bandwidth | 10–200 Gbps | 100 Gbps–Tbps | 1–10 Gbps |
| Weather sensitivity | High (fog) | None | Moderate (rain) |
| Deploy speed | Hours | Weeks–months | Days |


Cloudberry relevance is direct: FSO terminal hardware is semiconductor-dense—InP/GaAs laser arrays, SiPh coherent receivers, MEMS or liquid-crystal beam-steering, and custom PAT ASICs. GlobalFoundries' RF and photonics PDKs (45CLO, 9WG) are plausible fabrication paths for integrated FSO front-ends. Deal-flow targets: startups fabbing integrated coherent terminals, beam-steering chiplets for LEO ISLs, or atmospheric-compensation ICs. Space FSO is a rare high-margin photonics volume driver outside datacom.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
