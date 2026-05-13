---
type: concept
slug: gw-scale-power-delivery
canonical_name: GW-Scale Power Delivery (HVDC, sub-station to rack)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- energy-power
- power-electronics
related_concepts: []
companies_using:
- abb
- amantys-now-part-of-infineon
- ampacimon
- amperesand
- bloom-energy
- copper-labs
- dcx-dc-systems
- delta-electronics
- eaton
- elum-energy
- enertechnos
- ge-vernova
- giga-tronics-acuity-rebranded-as-datagryd
- gridbeyond
- gridmatic
- hitachi-energy
- infineon-technologies
- legrand
- ls-electric
- nexans
- prysmian-group
- schneider-electric
- seti
- siemens-energy
- solaredge-commercial-industrial-division
- starkpower
- tbea
- turntide-technologies
- vertiv
- vicor-corporation
- voltserver
- wolfspeed
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

# GW-Scale Power Delivery (HVDC, sub-station to rack)

*Kind: technology*

## Physics / mechanism

HVDC transmission moves bulk power at ±320–800 kV DC, cutting resistive losses to ~3% per 1,000 km versus ~7% for HVAC equivalents. At the hyperscale campus level, medium-voltage DC (MVDC) distribution at 6–24 kV feeds campus substations; from there, 480 V AC or 400 V DC bus architectures deliver to rack. Modern rack power density has crossed 100 kW (liquid-cooled GPU clusters) with roadmaps to 200–300 kW by 2027. The critical loss budget runs: transmission → step-down transformer → switchgear → UPS/rectifier → PDU → VRM, each stage adding 1–3% loss. End-to-end efficiency from grid to silicon is typically 85–90%; every point recovered at GW scale is tens of MW of avoided capacity.

## Competitive landscape

---

## Cloudberry relevance

The main competing topology is legacy HVAC + on-site transformation, which remains cheaper to permit and operates within existing utility frameworks. 48 V DC bus architectures (Google, OCP) compete at the rack level by eliminating one conversion stage. Solid-state transformers (SSTs) threaten conventional copper wound units by enabling direct MVDC-to-rack conversion with faster fault isolation. Fuel cells and on-site gas turbines compete as behind-the-meter generation, sidestepping grid interconnect queues entirely.

| Approach | Efficiency gain | Capex premium | Deployment readiness |
|---|---|---|---|
| HVDC + MVDC campus | High | High | Near-term (utility-scale) |
| 48 V DC bus | Medium | Low | Deployed (hyperscalers) |
| Solid-state transformer | High | Very high | 2–3 yr to volume |

---

Power delivery infrastructure is a direct dependency on semiconductor fab utilisation and AI cluster buildout — both core Cloudberry theses. Deal flow angles include: wide-bandgap device makers (SiC/GaN) enabling higher-frequency SSTs and more efficient VRMs; advanced packaging for high-density power modules; and photonics-based sensing for real-time fault detection in MVDC switchgear. GlobalFoundries' SiC and power IC roadmap sits directly inside this stack, making power conversion IP a credible co-investment lens alongside compute substrate plays.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
