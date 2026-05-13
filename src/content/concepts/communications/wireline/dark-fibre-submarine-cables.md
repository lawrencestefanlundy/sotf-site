---
type: concept
slug: dark-fibre-submarine-cables
canonical_name: Dark Fibre / Submarine Cables
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
- alcatel-submarine-networks-asn
- amazon-aws-global-infrastructure
- aqua-comms
- artic-connect-far-north-fiber
- bscs-baltic-sea-cable-system-arelion
- bulk-infrastructure-bulk-fibre-networks
- bulk-infrastructure
- cinia
- crosslake-fibre
- eunetworks
- eutelsat-eunetworks
- exa-infrastructure
- global-telecom-technology-gtt-communications
- globalinfratel-fibertelecom-open-fiber
- google-global-network-infrastructure
- google-google-cloud-subsea-cables
- hmn-technologies-formerly-huawei-marine
- iec-telecom-te-subcom-te-connectivity
- iq-networks-formerly-openreach-wholesale-dark-fibre
- itc-global-now-part-of-speedcast
- lumen-technologies-dark-fibre-iq-fibre
- lumen-technologies
- meta-project-waterworth-sunbird
- meta-submarine-cable-investments
- nec-corporation-marine-network-systems
- nec-corporation-submarine-networks-division
- nexans
- prysmian-group
- quintillion-networks
- quintillion
- seaborn-networks
- subcom
- surf-suisse-underwater-research-foundation-surf-network
- tampnet
- tele2-com-hem-tele2-netnodt2-infrastructure
- wasabee
- zayo-group
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

# Dark Fibre / Submarine Cables

*Kind: technology*

## Physics / mechanism

Submarine cables carry ~95% of intercontinental internet traffic. A cable system bundles multiple fibre pairs; each fibre pair runs dense-wavelength-division multiplexing (DWDM), currently 100–200 wavelength channels per fibre, each channel at 100–400 Gbps, pushing total system capacity past 1 Pb/s on leading routes (e.g., 2Africa, Marea). Dark fibre is provisioned but unlit capacity — bought or leased and driven by the buyer's own transponders. Key parameters: chromatic dispersion (ps/nm·km), polarisation-mode dispersion, OSNR budget, amplifier spacing (~50–80 km via erbium-doped fibre amplifiers). Spatial division multiplexing (SDM) via multi-core or few-mode fibre is the next inflection, targeting 10× capacity without new cable lay.

## Competitive landscape

Terrestrial dark fibre IRUs compete directly for enterprise and carrier connectivity within continents. Low-earth-orbit constellations (Starlink, Telesat Lightspeed) compete on latency-sensitive thin routes but remain capacity-constrained and cost-uncompetitive for bulk throughput. Integrated subsea cable + landing station ownership (hyperscaler consortia: Google, Meta, Microsoft) increasingly displaces traditional carrier-neutral operators. Coherent transceiver technology — the silicon photonics DSP/modulator stack — is where margin is captured, not in the glass.

## Cloudberry relevance

| Approach | Latency | Capacity | CapEx/Tbps |
|---|---|---|---|
| Submarine fibre | 5–150 ms intercontinental | Pb/s class | Falling |
| LEO satellite | 20–40 ms | Tb/s class | High |
| Terrestrial fibre | 1–50 ms regional | Tb/s class | Moderate |


Cloudberry's photonics and advanced-materials angle sits at the coherent transceiver layer: silicon-photonics PICs, InP modulators, ultra-low-noise EDFAs, and DSP ASICs that monetise every submarine fibre route. GlobalFoundries' silicon photonics process (45SPCLO) is directly in this stack. Deal-flow: fabless coherent optics startups, novel fibre materials (low-loss hollow-core), and submarine repeater component suppliers where compound-semiconductor content intersects GF-compatible manufacturing.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
