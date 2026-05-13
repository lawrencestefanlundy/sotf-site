---
type: concept
slug: sub-thz-6g
canonical_name: Sub-THz / 6G (>100 GHz)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- communications
- wireless
related_concepts: []
companies_using:
- airgain-mmtron
- blu-wireless
- ericsson
- gapwaves
- huawei-wireless-research
- imst-gmbh
- infineon-technologies
- interdigital
- jedar-robotics-jedar-now-teranova-eu-project-spinoff-context
- keysight-technologies
- millimeter-wave-products-miwv-filtronic
- mixcomm
- movandi
- nokia-bell-labs
- ntt-docomo
- peraso-technologies
- pharrowtech
- qualcomm
- rohde-schwarz
- samsung-electronics-networks
- sivers-semiconductors
- soracom-docomo-ventures-portfolio-teraspan-networks
- teranova-eu-h2020-consortium-lead-comsenter-uc-berkeley-spin
- wiliot-context-note-exclude-replacing-with-waveye-vayyar
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

# Sub-THz / 6G (>100 GHz)

*Kind: technology*

## Physics / mechanism

Sub-THz covers roughly 100 GHz–1 THz; 6G standardisation targets 100–300 GHz sub-bands (D-band: 110–170 GHz, H-band: 220–330 GHz). Propagation follows free-space path loss ∝ f², so link budgets tighten fast — 10 dB/km atmospheric absorption peaks near 183 GHz and 325 GHz water-vapour lines. Available channel bandwidths reach 10–100 GHz, enabling >100 Gbps point-to-point at short range (<1 km). Key enablers: III-V HEMTs (InP, GaN) pushing fT/fmax above 500/700 GHz; SiGe BiCMOS reaching ~300 GHz fmax at lower cost; photonic-assisted THz generation via uni-travelling-carrier photodiodes hitting 1 mW+ at 300 GHz. IMT-2030 (6G) candidate bands lock in circa 2025–2026.

## Competitive landscape

The primary competition is millimetre-wave 5G (24–71 GHz FR2), which has established ecosystem, lower path loss, and mature CMOS support. Optical FSO (free-space optical) competes for the same high-capacity short-haul backhaul use case with lower absorption but weather sensitivity. Within sub-THz, InP dominates performance, SiGe BiCMOS attacks cost, and GaN targets power. Integrated photonic approaches (III-V on Si) threaten to commoditise signal generation.

## Cloudberry relevance

| Approach | Frequency ceiling | Integration cost | Maturity |
|---|---|---|---|
| InP HEMT | >500 GHz | High | Pilot |
| SiGe BiCMOS | ~300 GHz | Medium | Early prod. |
| Photonic THz (UTC-PD) | ~1 THz | Medium-high | Lab/pilot |


Cloudberry's GlobalFoundries-LP mandate directly intersects here: GF's 22FDX and SiGe BiCMOS platforms are positioned for sub-THz front-end integration, and fabless startups needing a qualified, accessible process node are natural deal-flow. Photonics-assisted THz generation aligns with photonics portfolio theses. Watch for seed/Series A teams building D-band chipsets, phased-array front-ends, or THz sensing (materials characterisation, security imaging) — the latter de-risks from 6G timeline uncertainty.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
