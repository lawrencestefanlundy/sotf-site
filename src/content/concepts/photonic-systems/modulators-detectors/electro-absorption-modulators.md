---
type: concept
slug: electro-absorption-modulators
canonical_name: Electro-Absorption Modulators (EAM)
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
- bpw-photonics
- effect-photonics
- fraunhofer-hhi
- fujitsu-optical-components
- hisilicon-huawei
- ii-vi-incorporated-coherent-corp
- innolight-technology
- inphi-acquired-by-marvell
- kaiam-corporation
- leonardo-electronics-formerly-compound-semiconductor-centre
- linkra-photonics
- lumentum
- macom-technology-solutions
- mitsubishi-electric
- oclaro-now-part-of-lumentum
- photonic-technologies
- raybow-opto
- sicoya-acquired-by-samsung
- sifco-shenzhen-shengkai-opto
- smart-photonics
- source-photonics
- sumitomo-electric-industries
- thorlabs
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

# Electro-Absorption Modulators (EAM)

*Kind: technology*

## Physics / mechanism

Electro-absorption modulators exploit the Franz-Keldysh effect (bulk semiconductors) or quantum-confined Stark effect (QCSE, quantum wells/dots) to shift a material's absorption edge under applied electric field, switching light on/off without carrier injection. Key materials: InGaAsP/InP and Ge-on-Si. Applied reverse bias (typically 1–4 V) red-shifts the bandgap, increasing absorption at the operating wavelength. QCSE devices achieve extinction ratios of 6–10 dB, insertion loss ~3–5 dB, 3-dB bandwidth >50 GHz, and drive voltages below 2 V — critical for energy-per-bit targets sub-1 pJ/bit at 100G+ per lane. Monolithic integration with DFB lasers yields EML (electro-absorption modulated laser) modules dominant in datacenter optics.

## Competitive landscape

---

## Cloudberry relevance

EAMs compete primarily with Mach-Zehnder modulators (MZM). MZMs offer lower chirp and broader bandwidth but require mm-scale footprint and higher drive voltage (3–6 V). Silicon ring resonators are compact and CMOS-compatible but thermally sensitive. Lithium niobate thin-film modulators (TFLN) now achieve >100 GHz bandwidth with sub-1 V·cm drive, emerging as the high-performance threat. Germanium EAMs on silicon are the integration play inside SiPh platforms — co-packaged optics roadmaps at hyperscalers lean heavily on Ge-EAM arrays for 800G/1.6T lanes.

| Modulator | BW (GHz) | Vπ or drive (V) | Footprint |
|---|---|---|---|
| Ge-EAM (SiPh) | 50–67 | 1–2 | ~10 µm |
| TFLN MZM | >100 | <1 | ~3–5 mm |
| Si ring | 30–50 | ~1 | ~5 µm |

---

Co-packaged optics and 1.6T datacom transceivers are pulling hard on Ge-EAM IP inside SiPh foundry platforms — directly relevant to GlobalFoundries' SiPh offering (GF Fotonix). Deal-flow angles: EAM IP companies licensing into foundry PDKs, startups building EML or co-packaged modules, and Ge-on-Si epitaxy process players. Lunar Ventures' seed-stage portfolio may surface fabless photonics startups where EAM integration is a differentiator worth diligencing on modulator architecture before Series A.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
