---
type: concept
slug: small-modular-reactors
canonical_name: Small Modular Reactors (SMRs)
aliases:
- SMR
- SMRs
- advanced nuclear fission
- microreactors
- advanced fission
kind: technology
parent_concepts:
- energy-power
- generation
related_concepts:
- datacentre-cloud-infrastructure
- ai-thermal-management
sources:
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2023-08-18-e11-in-conversation-with-lux-capital]]'
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2023-04-04-learnings-from-a-deep-tech-horizon]]'
- '[[2024-11-20-nuclear-fusion-the-state-of-play]]'
- '[[2023-09-24-e16-in-conversation-with-john-waite]]'
- '[[2024-11-12-atomic-energy-can-nuclear-power-our]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-06-13-smr-datacentre-baseload-research]]'
- '[[2026-02-16-energy-buildout-keeps-pace-interconnection-queue-and-grid]]'
- '[[2025-12-09-energy-buildout-keeps-pace-gas-turbine-capacity-constraints]]'
- '[[2026-05-09-energy-buildout-keeps-pace-behind-the-meter-gas-turbine]]'
frontier:
- Does any non-LWR SMR (molten-salt, HTGR/TRISO, sodium-fast, heat-pipe) reach commercial operation this decade, or do only de-risked LWR designs (GE Hitachi BWRX-300, Rolls-Royce, NuScale) actually get built by 2032?
- Is the HALEU (high-assay low-enriched uranium) fuel supply chain the binding constraint? Most advanced designs need HALEU; near-term Western supply is thin (Centrus, Urenco ramp), Russia is the incumbent supplier. Whoever owns qualified HALEU/TRISO fabrication has the chokepoint.
- Do hyperscaler datacentre PPAs (Google-Kairos, Amazon-X-energy, Microsoft-Constellation, Meta) actually convert to delivered MWe, or do they slip the way first-of-kind nuclear always has?
- 'Factory-built economics: does the modular/learning-curve promise (build in a factory, ship LEGO modules) materialise, or does first-of-a-kind cost (NuScale''s cancelled UAMPS project at ~$89/MWh and rising) keep killing projects?'
- 'Where is the deep-tech, venture-shaped wedge, if any? The reactor itself is utility/government/strategic-funded and capital-intensive ($1B+ to first unit) — wrong cheque size for a pre-seed fund. The candidate wedges are upstream/adjacent: HALEU/TRISO fuel materials, structural/cladding materials qualification, radiation-hard instrumentation and sensors, reactor I&C / control silicon, and digital-twin/simulation.'
last_updated: '2026-06-13'
tags:
- concept
- technology
mention_count: 19
descendants: []
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-13-smr-datacentre-baseload-research
  title: SMR / advanced-nuclear for datacentre baseload — research sweep (Jun 2026)
  date: '2026-06-13'
  kind: web
- slug: 2026-05-09-energy-buildout-keeps-pace-behind-the-meter-gas-turbine
  title: 'Behind-the-meter gas turbine workaround cannot scale: fuel cells offer potential but at 40% higher LCOE than gas turbines currently'
  date: '2026-05-09'
  kind: web
- slug: 2026-02-16-energy-buildout-keeps-pace-interconnection-queue-and-grid
  title: Interconnection queue and grid constraints hard-capping datacentre construction timelines
  date: '2026-02-16'
  kind: web
- slug: 2025-12-09-energy-buildout-keeps-pace-gas-turbine-capacity-constraints
  title: 'Gas turbine capacity constraints: delivery windows pushed 5-7 years, peak power crunch 2028-29'
  date: '2025-12-09'
  kind: web
- slug: 2025-01-27-ai-for-nuclear-fusion-feat-martin
  title: AI for Nuclear Fusion (Feat. Martin Riedmiller, Google DeepMind)
  date: '2025-01-27'
  kind: substack
- slug: 2024-11-20-nuclear-fusion-the-state-of-play
  title: 'Nuclear Fusion: A Primer'
  date: '2024-11-20'
  kind: substack
- slug: 2024-11-12-atomic-energy-can-nuclear-power-our
  title: 'Nuclear Fission: A Primer'
  date: '2024-11-12'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
neighbors:
- slug: datacentre-cloud-infrastructure
  name: Datacentre & Cloud Infrastructure
  path: /life-frontier/ai-infrastructure/datacentre-cloud-infrastructure/
  macro: life-frontier
- slug: ai-thermal-management
  name: Ai Thermal Management
  path: /energy-power/thermal-management/ai-thermal-management/
  macro: energy-power
---
## Physics / mechanism

SMRs are nuclear fission reactors **smaller** (50-300 MWe per module vs 1,000-1,600 MWe for traditional plants) and **modular** (factory-built, shipped as units, assembled on site — "Ford assembly line for nuclear"). Architecture varies widely, and maturity tracks that variance (atomic energy can nuclear power our):

- **Light-Water Reactors (LWR-SMR)** — most mature, proven PWR/BWR physics scaled down, ~15-16 MPa, ~315 °C. GE Hitachi BWRX-300 (300 MWe), Rolls-Royce SMR (470 MWe), NuScale VOYGR (250 MWe/module, the only US-design-certified SMR). Challenge is cost, not physics.
- **High-Temperature Gas-Cooled (HTGR)** — helium-cooled, ~750 °C, TRISO fuel; enables industrial process heat + hydrogen. X-energy Xe-100 (80 MWe), General Atomics EM2, USNC MMR.
- **Molten-Salt (MSR)** — atmospheric pressure, >600 °C, liquid or salt-cooled solid fuel. Terrestrial Energy IMSR, Moltex SSR, Seaborg CMSR, Copenhagen Atomics, Kairos KP-FHR (fluoride-salt-cooled, TRISO — Google's 500 MWe partner).
- **Sodium-Fast (SFR)** — low pressure, ~500 °C, closed fuel cycle. TerraPower Natrium (345 MWe + molten-salt thermal storage to 500 MWe), ARC-100.
- **Heat-pipe microreactors** — newest, 1-25 MWe, simplest. Westinghouse eVinci, Oklo Aurora, Los Alamos Kilopower lineage.

Key advantage cluster: capacity factor >90% (true baseload, vs 35-45% wind / 15-30% solar), tiny land footprint (15-20 acres vs 1,500-2,000 for solar+storage equivalent), 60-80 year life, fuel ~10% of LCOE (price stability), and high-grade process heat the non-nuclear alternatives cannot supply. See **Baseload Power** for why those properties matter now.

## Market driver — datacentre power is the catalyst

Decarbonisation and energy security are secondary. The catalyst is **AI datacentre firm-power demand** (atomic energy can nuclear power our, **Ai Power Thermal Binding**): Google-Kairos (500 MWe, ~$2B incl. dedicated manufacturing), Amazon-X-energy (4× Xe-100), Microsoft-Constellation (Three Mile Island restart, ~$65/MWh PPA benchmark), Meta (load-following AI-datacentre design). Hyperscalers are becoming the anchor customers next-gen nuclear never had. Global nuclear is ~10% of electricity, ~$350-400B/yr, 440 reactors; IAEA sees capacity potentially doubling by 2050 mostly via SMRs, and datacentres are demand *outside* those forecasts.

## Companies using

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
