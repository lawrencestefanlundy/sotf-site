---
type: concept
slug: heterogeneous-photonic-integration
canonical_name: Heterogeneous Photonic Integration
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
- effect-photonics
- fraunhofer-hhi
- hokkaido-university-spin-off-teraphox
- hyperlight
- ii-vi-coherent-corp
- intel-foundry-services-intel-ifs-silicon-photonics
- ligentec
- lightelligence
- lumentum
- marvell-technology
- nexus-photonics
- openlight-photonics
- photon-spot-actinix-scintil-photonics
- photonix-formfactor-photonics-phix-photonics-assembly
- poet-technologies
- quintessent
- ranovus
- rockley-photonics
- sicoya-acquired-by-semikron-danfoss-spun-from-tu-berlin
- siepic-voyant-photonics
- smart-photonics
- sparrow-quantum
- xanadu
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

# Heterogeneous Photonic Integration

*Kind: technology*

## Physics / mechanism

Heterogeneous photonic integration combines dissimilar material platforms—typically III-V (InP, GaAs, GaN) active layers bonded or epitaxially grown onto silicon or silicon nitride passive waveguide circuits—to co-locate light generation, amplification, modulation, and detection on a single chip. The mechanism relies on evanescent coupling or butt-coupling between the gain medium and low-loss passive waveguide after direct wafer bonding or die-to-wafer bonding. Key figures of merit: coupling efficiency >90%, on-chip laser threshold currents <5 mA, propagation loss <0.5 dB/cm in SiN, and co-integration with germanium photodetectors at >50 GHz bandwidth. State of the art: Intel, Marvell (via Inphi), and imec-led consortia ship heterogeneous silicon photonic transceivers at 400G–800G; research labs demonstrate 1.6T co-packaged optics using this architecture.

## Competitive landscape

Monolithic III-V photonics (InP PICs) competes on performance but loses on cost and CMOS fab compatibility. Silicon-only photonics lacks gain entirely. Thin-film lithium niobate (TFLN) competes on modulation bandwidth (>100 GHz EO) but still needs an external laser. Quantum dot on silicon is an emerging monolithic alternative, avoiding bonding steps at the cost of yield immaturity.

## Cloudberry relevance

| Approach | Gain on-chip | CMOS compatible | Modulation BW |
|---|---|---|---|
| Heterogeneous III-V/Si | Yes | Partial | ~50 GHz |
| Monolithic InP | Yes | No | ~100 GHz |
| TFLN + external laser | No | No | >100 GHz |


GlobalFoundries operates a qualified silicon photonics PDK (GF Fotonix, 300 mm), making heterogeneous integration a direct adjacency—startups building bonded laser dies or chiplets targeting GF's passive platform are natural Cloudberry deal-flow. Watch for companies solving the bonding yield bottleneck, supplying III-V chiplets, or offering EDA/design tools for heterogeneous co-design. Co-packaged optics demand for AI datacenter switching accelerates the commercialisation timeline materially.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
