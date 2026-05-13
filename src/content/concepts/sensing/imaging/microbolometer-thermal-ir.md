---
type: concept
slug: microbolometer-thermal-ir
canonical_name: Microbolometer / Thermal IR
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- imaging
related_concepts: []
companies_using:
- adasky
- atomica-formerly-imt-masken-und-teilungen-sige-semiconductor
- bae-systems-fast-labs-infrared-imaging
- brilliantly
- dali-technology
- exosens-photonis-group
- flir-systems-teledyne-flir
- guide-infrared
- heimann-sensor
- hikmicro-hikvision-subsidiary
- infiray-iray-technology
- ino-institut-national-doptique
- leonardo-drs
- lynred-formerly-sofradir-ulis
- meridian-innovation
- nippon-avionics-nec
- omnivision-omnivision-technologies
- opgal-optronic-industries
- pixpolar
- scd-semi-conductor-devices
- seek-thermal
- tenum
- thermoteknix
- xenics
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

# Microbolometer / Thermal IR

*Kind: technology*

## Physics / mechanism

Microbolometers are uncooled thermal infrared detectors. Incident LWIR photons (8–14 µm) heat a thermally isolated membrane—typically vanadium oxide (VOx) or amorphous silicon (a-Si)—whose resistance changes measurably with temperature (TCR: −2 to −3 %/K for VOx). A ROIC (readout integrated circuit) samples each pixel's resistance change; no photon-to-electron conversion occurs, so no cooling is required. Arrays are monolithically integrated via MEMS post-processing on standard CMOS ROICs. Current SoA: 12 µm pixel pitch, 1920×1080 formats, NETD <30 mK, f/1.0. Key suppliers: FLIR/Teledyne, Lynred, BAE Systems, INO, Seek Thermal, Hikvision.

## Competitive landscape

Cooled photon detectors (InSb, HgCdTe/MCT) deliver NETD <10 mK and higher frame rates but require Stirling or Peltier cooling, adding cost, weight, and MTTR risk—dominant in military targeting, astronomy. Quantum well infrared photodetectors (QWIPs) occupy a middle ground. For MWIR (3–5 µm), InAsSb detectors outperform microbolometers on sensitivity but not on SWaP-C. Graphene and 2D-material bolometers are pre-commercial. Pyroelectric detectors (LiTaO₃) are lower-cost but pixel-limited.

## Cloudberry relevance

| Detector | Cooling | NETD | Cost |
|---|---|---|---|
| Microbolometer | None | 30–50 mK | $$ |
| MCT/InSb | Cryo | <10 mK | $$$$ |
| Pyroelectric | None | ~100 mK | $ |


Cloudberry relevance sits at the ROIC and pixel-process layer. GF's 300 mm CMOS fabs are credible ROIC foundries; any fabless microbolometer startup needing volume ROIC production is natural deal-flow. Pixel-level MEMS differentiation—novel absorber materials, metamaterial absorbers, 2D materials—maps to Cloudberry's advanced-materials thesis. Automotive ADAS, drone-based sensing, and industrial process control are the near-term volume drivers justifying Series A/B bets.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
