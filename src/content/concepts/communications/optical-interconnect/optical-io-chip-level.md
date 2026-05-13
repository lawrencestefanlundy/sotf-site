---
type: concept
slug: optical-io-chip-level
canonical_name: Optical I/O at Chip Level
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- communications
- optical-interconnect
related_concepts: []
companies_using:
- ayar-labs
- broadcom
- celestial-ai
- finisair-ii-vi-coherent
- hamamatsu-photonics
- hyperlight
- inphotec
- intel-intel-foundry-silicon-photonics-group
- lightmatter
- lionix-international
- marvell-technology
- nubis-communications
- openlight
- phix-photonics-assembly
- photondelta-effect-photonics
- poet-technologies
- quintessent
- ranovus
- rockley-photonics
- salience-labs
- scintil-photonics
- sicoya-acquired-by-cj-optronics
- sicoya-globalfoundries-co-packaged-optics-program
- sievert-larsen-associates-lumentum
- teramount
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

# Optical I/O at Chip Level

*Kind: technology*

## Physics / mechanism

Optical I/O at chip level replaces copper bumps or wirebonds with photonic links integrated at the package edge or directly on-die, moving data as photons rather than electrons. Key components: laser source (on-chip VCSEL or hybrid III-V), modulator (ring resonator or Mach-Zehnder), waveguide (SiN or Si), and photodetector. Bandwidth density target is >1 Tb/s/mm²; current co-packaged optics (CPO) hits ~3.2 Tb/s per device at <5 pJ/bit. On-die integration (monolithic or 3D-bonded) pushes toward <1 pJ/bit. Principal bottleneck: laser integration on silicon—hybrid bonding of InP dies is the leading workaround. Intel IPG, Ayar Labs, Ranovus, and Broadcom are primary execution benchmarks.

## Competitive landscape

---

## Cloudberry relevance

The direct competitor is copper-based die-to-die interconnect (UCIe, HBM stacks, CXL over SerDes)—mature, cheap, but energy and bandwidth-density limited beyond ~112G NRZ. Competing photonic approaches include edge-coupled fiber attach (CPO at module level rather than die level), plasmonic modulators (higher bandwidth, integration immaturity), and THz wireless die-to-die (research stage). Silicon photonics on 300mm CMOS wafers is the dominant integration path; SiN is preferred for low-loss passive routing.

| Approach | Bandwidth density | Energy (pJ/bit) | CMOS compatibility |
|---|---|---|---|
| Cu SerDes (112G) | ~0.1 Tb/s/mm² | 10–20 | Native |
| CPO (module-level) | ~0.5 Tb/s/mm² | 3–6 | Partial |
| On-chip optical I/O | >1 Tb/s/mm² (target) | <1 (target) | Hybrid bonding |

---

Cloudberry's GlobalFoundries-LP mandate maps directly: GF runs a SiPho platform (45SPCLO) and is a natural manufacturing partner or acquirer for optical I/O IP. Deal-flow angles include laser integration startups (III-V bonding, VCSEL arrays), EDA/PDK tooling for photonic-electronic co-design, and packaging houses enabling known-good-die photonic assembly. Ayar Labs-style fabless plays needing a CMOS-native SiPho foundry are the archetype. Lunar Ventures' seed exposure to compute infrastructure makes optical I/O a logical follow-on thesis.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
