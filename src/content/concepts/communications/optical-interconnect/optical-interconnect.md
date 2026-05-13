---
type: concept
slug: optical-interconnect
canonical_name: Optical Interconnect
aliases:
- optical-interconnects
- Optical Interconnects
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- communications
- optical-interconnect
related_concepts: []
companies_using:
- accelink-technologies
- avicena
- ayar-labs
- broadcom
- celestial-ai
- coherent-corp
- ekinops
- hamamatsu-photonics
- hiefo-hi-europe-fiber-optics
- ii-vi-coherent-finisar-heritage
- innolight-technology
- intel-silicon-photonics
- ipronics
- lightmatter
- lionix-international
- lumentum
- marvell-technology
- nexus-photonics
- photonics-planar-integration-technology-phix
- quintessent
- ranovus
- rockley-photonics
- scintil-photonics
- sicoya
- smart-photonics
- effect-photonics
- hgc-hon-hai-foxconn-interconnect-technology
- hisilicon-huawei
- imec
- intel-intel-foundry-ifs-optical
- nubis-communications
- optoscribe
- photonicsworld-formerly-compass-photonics
- poet-technologies
- vlc-photonics
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-07'
tags:
- concept
- technology
mention_count: 13
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 3
---

# Optical Interconnect

*Kind: technology · Attio deal count: 9*

## Physics / mechanism

Optical interconnects transmit data as photons rather than electrons, eliminating RC delay and resistive loss that cap copper at ~112 Gbps/lane in practice. Light is modulated (typically via Mach-Zehnder or ring-resonator modulators), propagated through waveguides or free-space, and detected by photodiodes. Key parameters: bandwidth-distance product, energy per bit (target <1 pJ/bit at scale), insertion loss, and integration density. Silicon photonics platforms (Intel, Cisco/Acacia, Coherent) now ship 400G–800G pluggable transceivers; co-packaged optics (CPO) moves the optical engine onto the package substrate, targeting <5 pJ/bit and eliminating the PCB SerDes hop. Volume CPO deployment is 2025–2027 for hyperscale switches.

## Competitive landscape


Copper electrical interconnects (PAM4 at 112G/lane, moving to 224G) remain dominant inside the package and at short reach; they compete on cost and integration maturity. Multimode fiber + VCSEL arrays dominate <100 m. The real architectural contest is CPO vs. near-package optics vs. linear-drive pluggables. Polymer waveguides (Samtec, Fraunhofer) target board-level optical PCB as a middle path.

| Approach | Reach | Energy/bit | Maturity |
|---|---|---|---|
| Copper (224G PAM4) | <1 m | ~5 pJ | Production |
| Pluggable (800G-DR8) | 2 km | ~8–12 pJ | Production |
| Co-packaged optics | on-package | <3 pJ target | Early sampling |

## Cloudberry relevance
Cloudberry's GF-LP fund sits directly upstream: GF's silicon photonics process (45RFSOI-derived, 45CLO) is a credible CPO foundry node, making portfolio bets on photonic chiplets, laser integration (III-V bonding), and EDA/design tooling acutely relevant. Deal-flow angles include modulator startups, photonic packaging specialists, and DSP-less linear-drive architectures. Lunar Ventures' deep-tech lens catches pre-Series A optical compute and sensing plays that feed the same substrate roadmap.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*

## Merged from `optical-interconnects` (archived 2026-05-07)

*Plural variant of the same concept. Optical interconnect = singular canonical.*

# Optical Interconnects

*Kind: technology · Attio deal count: 18*

## Physics / mechanism

Optical interconnects transmit data as photons rather than electrons, using modulated laser light through waveguides, fibre, or free-space paths. Key components: laser source (VCSEL or edge-emitter), modulator (electro-optic or electro-absorption), waveguide (SiPh, InP, polymer), and photodetector. Critical parameters: bandwidth-distance product, energy-per-bit (target <1 pJ/bit at scale), insertion loss, and latency. Co-packaged optics (CPO) integrates photonics at the package level, cutting electrical trace losses. Current SoA: 800G per-lane transceiver modules; CPO at 3.2 Tbps aggregate in hyperscaler pilots. Silicon photonics enables CMOS-fab compatibility but struggles with efficient laser integration due to indirect bandgap.

## Competitive landscape


Copper electrical interconnects dominate at <1 m; they hit bandwidth-density and power walls past ~112 Gbps PAM4. Competing/adjacent approaches include advanced packaging (UCIe, HBM, chiplets via EMIB/Foveros) for die-to-die links, and emerging wireless/THz interconnects for niche board-level use. Within photonics: InP monolithic outperforms SiPh on laser integration but loses on cost; lithium niobate on insulator (LNOI) modulators (>100 GHz bandwidth, low Vπ) are increasingly displacing SiPh modulators in coherent and CPO applications.

| Approach | Bandwidth density | Energy/bit | Fab compatibility |
|---|---|---|---|
| Copper (112G PAM4) | ~1 Tbps/mm² | ~5–10 pJ/bit | CMOS native |
| Silicon photonics | ~10 Tbps/mm² | ~1–2 pJ/bit | CMOS compatible |
| InP monolithic | ~20 Tbps/mm² | <1 pJ/bit | Bespoke III-V |

## Cloudberry relevance
Cloudberry/GlobalFoundries LP context is direct: GF has a SiPh platform (90nm SiPh PDK) and is a credible CPO foundry candidate. Deal-flow angles: fabless SiPh startups needing a CMOS-adjacent foundry, LNOI modulator companies, CPO integration IP plays, and photonic sensing crossovers (LiDAR, quantum). Lunar Ventures' compute-infrastructure thesis overlaps at the AI accelerator interconnect bottleneck. The hyperscaler capex cycle into CPO creates a 2025–2027 pull for component and IP suppliers — early-stage entry window is now.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
