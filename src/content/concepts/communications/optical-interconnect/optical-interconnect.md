---
type: concept
slug: optical-interconnect
canonical_name: Optical Interconnect
aliases:
- optical-interconnects
- Optical Interconnects
kind: technology
parent_concepts:
- communications
- optical-interconnect
related_concepts:
- optical-circuit-switching
- optical-packet-switching
sources:
- '[[2026-05-30-optical-interconnect-ma-ledger]]'
- '[[2026-05-30-opsydia-glass-waveguide-packaging]]'
- '[[2026-05-30-intel-glass-substrates-program]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
frontier:
- ''
last_updated: '2026-05-07'
tags:
- concept
- technology
mention_count: 23
descendants:
- datacenter-network-stack
- lpo-linear-pluggable-optics
- optical-circuit-switching
- optical-interconnect
- optical-io-chip-level
- optical-packet-switching
- pluggable-transceivers
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 6
recent_mentions:
- slug: 2026-05-30-optical-interconnect-ma-ledger
  title: Optical-interconnect / photonic-packaging M&A ledger (2019-2026)
  date: '2026-05-30'
  kind: web
- slug: 2026-04-15-semianalysis-isscc-2026
  title: 'ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More'
  date: '2026-04-15'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
- slug: 2026-05-30-opsydia-glass-waveguide-packaging
  title: Opsydia — Oxford spinout, laser-written glass waveguides, pre-Series A (Jul 2025)
  date: '2025-07-30'
  kind: web
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
- slug: 2026-05-30-intel-glass-substrates-program
  title: Intel Unveils Industry-Leading Glass Substrates (+ Jan 2026 EMIB+glass demo status)
  date: '2023-09-18'
  kind: web
neighbors:
- slug: optical-circuit-switching
  name: Optical Circuit Switching (OCS)
  path: /sotf-site/communications/optical-interconnect/optical-circuit-switching/
  macro: communications
- slug: optical-packet-switching
  name: Optical Packet Switching (OPS)
  path: /sotf-site/communications/optical-interconnect/optical-packet-switching/
  macro: communications
---
## Physics / mechanism

Optical interconnects transmit data as photons rather than electrons, eliminating RC delay and resistive loss that cap copper at ~112 Gbps/lane in practice. Light is modulated (typically via Mach-Zehnder or ring-resonator modulators), propagated through waveguides or free-space, and detected by photodiodes. Key parameters: bandwidth-distance product, energy per bit (target <1 pJ/bit at scale), insertion loss, and integration density. Silicon photonics platforms (Intel, Cisco/Acacia, Coherent) now ship 400G–800G pluggable transceivers; co-packaged optics (CPO) moves the optical engine onto the package substrate, targeting <5 pJ/bit and eliminating the PCB SerDes hop. Volume CPO deployment is 2025–2027 for hyperscale switches.

## Competitive landscape

Copper electrical interconnects (PAM4 at 112G/lane, moving to 224G) remain dominant inside the package and at short reach; they compete on cost and integration maturity. Multimode fiber + VCSEL arrays dominate <100 m. The real architectural contest is CPO vs. near-package optics vs. linear-drive pluggables. Polymer waveguides (Samtec, Fraunhofer) target board-level optical PCB as a middle path.

| Approach | Reach | Energy/bit | Maturity |
|---|---|---|---|
| Copper (224G PAM4) | <1 m | ~5 pJ | Production |
| Pluggable (800G-DR8) | 2 km | ~8–12 pJ | Production |
| Co-packaged optics | on-package | <3 pJ target | Early sampling |

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

*Kind: technology*

## Physics / mechanism

Optical interconnects transmit data as photons rather than electrons, using modulated laser light through waveguides, fibre, or free-space paths. Key components: laser source (VCSEL or edge-emitter), modulator (electro-optic or electro-absorption), waveguide (SiPh, InP, polymer), and photodetector. Critical parameters: bandwidth-distance product, energy-per-bit (target <1 pJ/bit at scale), insertion loss, and latency. Co-packaged optics (CPO) integrates photonics at the package level, cutting electrical trace losses. Current SoA: 800G per-lane transceiver modules; CPO at 3.2 Tbps aggregate in hyperscaler pilots. Silicon photonics enables CMOS-fab compatibility but struggles with efficient laser integration due to indirect bandgap.

## Competitive landscape

Copper electrical interconnects dominate at <1 m; they hit bandwidth-density and power walls past ~112 Gbps PAM4. Competing/adjacent approaches include advanced packaging (UCIe, HBM, chiplets via EMIB/Foveros) for die-to-die links, and emerging wireless/THz interconnects for niche board-level use. Within photonics: InP monolithic outperforms SiPh on laser integration but loses on cost; lithium niobate on insulator (LNOI) modulators (>100 GHz bandwidth, low Vπ) are increasingly displacing SiPh modulators in coherent and CPO applications.

| Approach | Bandwidth density | Energy/bit | Fab compatibility |
|---|---|---|---|
| Copper (112G PAM4) | ~1 Tbps/mm² | ~5–10 pJ/bit | CMOS native |
| Silicon photonics | ~10 Tbps/mm² | ~1–2 pJ/bit | CMOS compatible |
| InP monolithic | ~20 Tbps/mm² | <1 pJ/bit | Bespoke III-V |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
