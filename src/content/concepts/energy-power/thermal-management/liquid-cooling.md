---
type: concept
slug: liquid-cooling
canonical_name: Liquid Cooling (cold plate, immersion, two-phase)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- energy-power
- thermal-management
related_concepts: []
companies_using:
- aavid-boyd-corporation
- achronix-accelsius
- alfa-laval
- aquila-group-brofos
- asetek
- coolcentric-now-part-of-motivair
- coolit-systems
- dcx-data-center-exchange-chilldyne
- envalior-dsm-firmenich-coolstream
- fujitsu
- grc-green-revolution-cooling
- hisilicon-huawei-cloud
- iceotope
- jetcool-technologies
- liquid-stack-formerly-allied-control
- midas-green-technologies
- nautilus-data-technologies
- phononic
- rheinmetall-electronics-henkel-bergquist-tie-in-stulz
- submer
- supermicro
- tmgcore
- vertiv
- wiwynn
- zutacore
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


# Liquid Cooling (cold plate, immersion, two-phase)

*Kind: technology*

## Physics / mechanism

Cold plate, immersion, and two-phase liquid cooling all exploit water's ~25× higher volumetric heat capacity versus air to remove heat flux that air cooling can no longer handle. Cold plates circulate dielectric fluid or water-glycol through machined channels bonded to a heat source; thermal resistance typically 0.01–0.05 °C·cm²/W depending on channel geometry and flow rate. Single-phase immersion submerges hardware directly in dielectric fluid (Novec, mineral oil); two-phase immersion adds a boiling/condensation cycle, leveraging latent heat to reach effective heat transfer coefficients >10,000 W/m²·K. Driving adoption: GPU/ASIC TDPs crossing 700 W per chip, rack densities hitting 100 kW+, and air cooling's practical ceiling around 30–40 kW/rack.

## Competitive landscape

---

## Cloudberry relevance

Air cooling (fans, heat pipes, vapor chambers) competes below ~30 kW/rack and remains cheaper at scale. Microfluidic on-chip cooling (DARPA ICECOOL heritage) targets die-level integration but lacks commercial maturity. Heat pipes and thermosiphons occupy a middle tier. The competitive axis is cost-per-watt-removed versus deployment complexity.

| Approach | Heat flux limit | Integration complexity | CapEx barrier |
|---|---|---|---|
| Air + vapor chamber | ~100 W/cm² | Low | Low |
| Cold plate (single-phase) | ~500 W/cm² | Medium | Medium |
| Two-phase immersion | >1000 W/cm² | High | High |

---

As GPU clusters and photonic co-packaged optics push per-chip power into the hundreds of watts, thermal management becomes a co-design constraint, not a commodity. Cloudberry's semiconductor and photonics portfolio companies face this directly—GF processes power-hungry RF and photonics dies where junction temperature governs reliability. Deal-flow angles: cooling IP licensors, dielectric fluid chemistry, cold plate manufacturers integrating into chiplet packaging, and software optimising dynamic thermal-power trade-offs in HPC deployments.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
