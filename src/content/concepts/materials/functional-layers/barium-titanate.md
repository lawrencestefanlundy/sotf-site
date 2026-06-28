---
type: concept
slug: barium-titanate
canonical_name: Barium Titanate
aliases:
- bto
- batio3
kind: material
parent_concepts:
- materials
- functional-layers
related_concepts:
- lithium-niobate-tfln
- lithium-tantalate-tflt
- silicon-nitride
- heterogeneous-photonic-integration
sources:
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-05-02-hybrid-bto-sin-ultra-low-power-tuning-acs-photonics]]'
- '[[2026-05-02-self-buffered-bto-epitaxy-on-oxide-insulator-light-sci-app-2]]'
- '[[2026-05-02-bto-permittivity-pockels-coefficients-mhz-thz-nature-materia]]'
- '[[2026-05-02-bto-pockels-modulator-on-silicon-photonics-jlt-2019]]'
frontier:
- ''
last_updated: '2026-06-07'
tags:
- concept
- material
mention_count: 49
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 14
recent_mentions:
- slug: 2026-05-02-hybrid-bto-sin-ultra-low-power-tuning-acs-photonics
  title: Hybrid BTO-SiN ultra-low power tuning (ACS Photonics)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-self-buffered-bto-epitaxy-on-oxide-insulator-light-sci-app-2
  title: 'Self-buffered BTO epitaxy on oxide insulator (Light: Sci & App 2025)'
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-bto-permittivity-pockels-coefficients-mhz-thz-nature-materia
  title: BTO permittivity & Pockels coefficients MHz-THz (Nature Materials 2025)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-bto-pockels-modulator-on-silicon-photonics-jlt-2019
  title: BTO Pockels modulator on silicon photonics (JLT 2019)
  date: '2026-05-02'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
neighbors:
- slug: lithium-niobate-tfln
  name: Lithium Niobate (TFLN)
  path: /sotf-site/materials/functional-layers/lithium-niobate-tfln/
  macro: materials
- slug: lithium-tantalate-tflt
  name: Thin-Film Lithium Tantalate (TFLT)
  path: /sotf-site/materials/functional-layers/lithium-tantalate-tflt/
  macro: materials
- slug: silicon-nitride
  name: Silicon Nitride
  path: /sotf-site/materials/substrates/silicon-nitride/
  macro: materials
- slug: heterogeneous-photonic-integration
  name: Heterogeneous Photonic Integration
  path: /sotf-site/photonic-systems/pic-platforms/heterogeneous-photonic-integration/
  macro: photonic-systems
---
## Physics / mechanism

Barium Titanate (BaTiO3, BTO) is a ferroelectric oxide with one of the largest known Pockels coefficients (>358 pm/V on optimised platforms vs. ~30 pm/V for lithium niobate). Used as a thin-film electro-optic layer integrated with silicon photonics or silicon nitride, BTO modulators show VπL of 0.2 V·cm and tuning at sub-µW power — orders of magnitude better than LN. Frequency response measured continuously from 100 MHz to 330 GHz. Foundry-compatible processes for BTO thin films on oxide insulators are advancing rapidly; the gating step is a production-grade, qualified BTO process at a major foundry (UCL/Altro is targeting GlobalFoundries collaboration). 2-3 BTO startups emerging every 6 months.

## Competitive landscape

*Adjacent material classes / techniques.*

## Yield, integration & material quality

Expert read from **George Li** (ex-Harvard BTO thin-film grower; **2026 06 07 George Bto Question Feb Call**) — the load-bearing constraints behind BTO's slow path to production, and why the headline Pockels spec overstates the practical case:

- **Monolithic BTO is a yield problem, not a capex problem.** BTO thin films are hard to grow well, and even when you get a film the **ferroelectric domains orient randomly across the wafer** (distribution varies with thickness, deposition, and epitaxy). **Monolithic etched waveguides therefore effectively require poling.** With no foundry or wafer supply chain to absorb the process risk, a company funds both the process and the ecosystem from scratch (e.g. **PsiQuantum** running their own MBE machines for wafers, the "bottomless pit").
- **The manufacturable path is heterogeneous, not monolithic.** SiN strip-loaded on top of BTO (the PsiQuantum route, also the GF SiN-on-BTO hybrid stack) **does not etch the BTO, so it sidesteps the domain problem entirely.** The trade-off: you **lose the raw-BTO on-paper specs** (real performance falls short of the >358 pm/V headline), but it is **much cheaper** than monolithic BTO. George: "monolithic BTO probably doesn't make a lot of sense."
- **Wafer availability is not production-grade quality.** **La Luce Cristallina**'s 200mm BTO wafers are **sputtered, multi-crystalline films, not single-crystal** (George, ~3 yrs ago: worse than Harvard-grown; doubts a single-crystal thin film within 3 years). Sputtered films are useful as a heterogeneous-deposition method onto Si/SiN, not as a monolithic waveguide layer.
- **Demand pull (2026):** a datacom systems CEO does not need BTO for 400G/800G today (SiPho + TFLN are good enough); BTO's near-term entry is the quantum corner (low-loss, fast switching). See **Photonics Material Class War** — BTO as a 2028-plus niche behind TFLN.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Does any foundry list a **single-crystal** (not sputtered) BTO process module on a public PDK by 2028? (Leading indicator for **Photonics Material Class War** prediction 3.)
- Does the heterogeneous SiN-on-BTO route recover enough of BTO's raw EO advantage to beat TFLN on Vπ·L *in production*, or does the spec gap erase the headline win?
- First **non-quantum** (datacom/telecom) BTO design-in, and at what data rate? (Pull today is quantum-leaning; volume pull is absent.)
- Can sputtered/poled multi-crystalline films ever reach production-grade photonic loss, or is single-crystal MBE the only viable route?

## Primer (web-enriched)

*Sourced 2026-05-02. See `sources/web/` for full citations.*

Barium Titanate (BaTiO3, BTO) is a ferroelectric oxide with one of the largest known Pockels coefficients (>358 pm/V on optimised platforms vs. ~30 pm/V for lithium niobate). Used as a thin-film electro-optic layer integrated with silicon photonics or silicon nitride, BTO modulators show VπL of 0.2 V·cm and tuning at sub-µW power — orders of magnitude better than LN. Frequency response measured continuously from 100 MHz to 330 GHz. Foundry-compatible processes for BTO thin films on oxide insulators are advancing rapidly; the gating step is a production-grade, qualified BTO process at a major foundry (UCL/Altro is targeting GlobalFoundries collaboration). 2-3 BTO startups emerging every 6 months.

## Further reading

- [BTO permittivity & Pockels coefficients MHz-THz (Nature Materials 2025)](https://www.nature.com/articles/s41563-025-02158-1) — tier 1
- [Self-buffered BTO epitaxy on oxide insulator (Light: Sci & App 2025)](https://www.nature.com/articles/s41377-025-02081-9) — tier 1
- [BTO Pockels modulator on silicon photonics (JLT 2019)](https://opg.optica.org/jlt/abstract.cfm?uri=jlt-37-5-1456) — tier 1
- [Hybrid BTO-SiN ultra-low power tuning (ACS Photonics)](https://pubs.acs.org/doi/10.1021/acsphotonics.9b00558) — tier 1
