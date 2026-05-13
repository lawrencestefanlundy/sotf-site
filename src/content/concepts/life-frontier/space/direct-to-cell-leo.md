---
type: concept
slug: direct-to-cell-leo
canonical_name: Direct-to-Cell / LEO SOS (Lynk, AST SpaceMobile)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- space
related_concepts: []
companies_using:
- apple-emergency-sos-via-satellite
- ast-spacemobile
- bullitt-group
- echostar-hughes-jupiter
- ericsson
- eutelsat-oneweb
- garmin
- globalstar
- inmarsat-bgan-isatphone
- iridium-communications
- lynk-global
- mangata-networks
- mediatek
- nokia-wing-ntn
- ntn-global-formerly-terra-bella-swarm-spinout-concept
- omnispace
- oq-technology
- qualcomm
- rakuten-mobile-rakuten-symphony
- satellogic-fossa-systems
- satellogic-kineis
- satellogic-sateliot
- skylo-technologies
- spacex-starlink-direct-to-cell
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


# Direct-to-Cell / LEO SOS (Lynk, AST SpaceMobile)

*Kind: technology*

## Physics / mechanism

Direct-to-cell (D2C) LEO connectivity uses low-earth-orbit satellites (altitude 400–600 km) to communicate directly with unmodified LTE/5G handsets — no specialist terminal required. The key constraint is link budget: a phone antenna has ~0 dBi gain, so satellites need large phased arrays (AST SpaceMobile's BlueBird blocks carry ~64 m² aperture) and aggressive beamforming to close the link. Lynk operates narrowband (SMS/data bursts, ~1–2 kbps); AST targets broadband (up to ~14 Mbps per beam in early trials). Both use standard 3GPP NTN (non-terrestrial network) extensions (Rel-17/18). Current SOS-mode deployments — Apple/Globalstar, T-Mobile/SpaceX — are separately architected but inform the same regulatory and spectrum pathway.

## Competitive landscape

---

## Cloudberry relevance

The primary competitor set is existing NTN constellations (Iridium, Globalstar, Inmarsat) requiring proprietary hardware, plus SpaceX's T-Mobile partnership using Starlink V2 Mini as a third distinct architecture. Terrestrial small-cell densification is an indirect substitute for coverage gaps. The critical differentiator is spectrum licensing (AWS-3, PCS, 700 MHz band access) — AST holds bilateral agreements with carriers across 45+ countries. Starlink D2C leads on constellation scale; Lynk leads on regulatory precedent (first FCC Part 25 D2C license).

| Player | Aperture | Throughput | Model |
|---|---|---|---|
| AST SpaceMobile | ~64 m² | ~14 Mbps | Carrier wholesale |
| SpaceX/Starlink | ~25 m² (est.) | ~2–4 Mbps | Carrier partnership |
| Lynk | Small | ~2 kbps | SOS/messaging |

---

Cloudberry's angle is upstream: D2C satellites are aperture-constrained, driving demand for high-density III-V phased-array ICs, advanced packaging, and GaN/SiGe RFIC at foundry scale — directly in GlobalFoundries' mixed-signal and RF process lanes. Radiant/Lunar portfolio companies in radiation-tolerant logic or photonic sensing feed the same supply chain. Deal-flow targets: beamforming ASIC designers, compact high-efficiency power management for large-aperture arrays, and space-qualified interconnect material startups.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
