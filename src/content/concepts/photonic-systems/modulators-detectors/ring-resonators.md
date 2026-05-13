---
type: concept
slug: ring-resonators
canonical_name: Ring Resonators
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- photonic-systems
- modulators-detectors
related_concepts: []
companies_using:
- accelink-technologies
- ayar-labs
- bright-photonics
- celestial-ai
- coherent-corp
- effect-photonics
- ephos
- freedom-photonics
- globalfoundries
- hisilicon-huawei
- imec-photon-delta-ecosystem
- imec
- intel-silicon-photonics
- ligentec
- lightmatter
- lionix-international
- lumentum
- luxtera-cisco
- marvell-technology
- psiquantum
- quintessent
- sicoya-samsung
- sparrow-quantum
- vpiphotonics
- xanadu-quantum-technologies
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

# Ring Resonators

*Kind: technology*

## Physics / mechanism

A ring resonator is a closed-loop optical waveguide evanescently coupled to a straight bus waveguide. Light at resonant wavelengths (where the round-trip path equals an integer multiple of the guided wavelength) builds up via constructive interference and is dropped from the bus. Key parameters: free spectral range (FSR = λ²/nₘL), Q-factor (10⁴–10⁶ in silicon photonics, >10⁷ in SiN), extinction ratio (>20 dB achievable), and coupling gap (100–300 nm, lithography-limited). State of the art: silicon ring modulators at 100+ Gb/s per channel; thermal tuning via integrated microheaters adds ~10 mW per ring. Primary integration platforms are Si (220 nm SOI), SiN, and LiNbO₃ thin-film.

## Competitive landscape

Direct competitors for filtering/modulation: Mach-Zehnder interferometers (MZIs), arrayed waveguide gratings (AWGs), and Fabry-Pérot cavities. MZIs offer broader bandwidth and lower thermal sensitivity but larger footprint; AWGs suit dense WDM demux but are passive-only; FP cavities deliver high finesse but are harder to integrate. For sensing, whispering-gallery-mode resonators (microspheres, microdisks) compete on Q but lack planar fab compatibility.

## Cloudberry relevance

| Approach | Footprint | Tunability | CMOS-compatible |
|---|---|---|---|
| Ring resonator | ~10 µm² | High (thermo/electro) | Yes |
| MZI | ~1000 µm² | Moderate | Yes |
| AWG | ~10⁴ µm² | Low | Yes |


Rings are a bellwether technology for silicon photonics co-packaged optics (CPO) and LiDAR — two deal-flow categories Cloudberry tracks directly. GlobalFoundries' 45RFSOI and 45CLO processes include validated photonic design kits where ring-based modulators are first-order building blocks. Any foundry-adjacent startup building optical interconnects, optical compute accelerators, or integrated sensing will have ring resonator IP at the core. Assess Q-factor roadmap, thermal stabilisation IP, and process node lock-in as the key diligence levers.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
