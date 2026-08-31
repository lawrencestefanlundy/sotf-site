---
type: concept
slug: immersion-cooling
canonical_name: Immersion Cooling
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-05-05-thermal-stack-arms-race-ai-datacenter-liquid-cooling-market]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 17
frontier:
- Does OCP or any hyperscaler publish numerical acceptance thresholds and a stated service life for immersion fluid compatibility, converting v1.5 from methodology into a qualification standard?
- What share of new AI training datacentre commissionings at or above 50 MW per site specify immersion versus direct-to-chip, and does either exceed 50% by 2027?
- Do soak-and-inspect results for Type 1 components correlate with field failure rates over multi-year deployment, or does the absence of electrical testing miss degradation modes?
- Which fluid chemistries pass compatibility testing across the full component taxonomy, and what cost per kW does that impose relative to direct-to-chip?
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-05-05-thermal-stack-arms-race-ai-datacenter-liquid-cooling-market
  title: AI Datacenter Liquid Cooling Market to Reach USD 17.8 Billion by 2036
  date: '2026-05-05'
  kind: web
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
neighbors: []
---
## Physics / mechanism

Immersion cooling removes heat from servers by placing components in direct contact with a cooling fluid rather than passing heat through a sealed cold plate loop. Because the fluid wets every surface of the board, including devices that were never designed for liquid exposure, the governing engineering question shifts from thermal resistance to material compatibility: what the fluid does to polymers, adhesives, solders, labels and thermal interface materials over time ocp component compatibility v15.

The Open Compute Project's Component Compatibility Testing Guidelines address this by classifying server components into types and assigning each a test path. Thermal interface materials are Type 1, defined as not electrically functional, so their qualification route is soak exposure in the candidate fluid followed by physical inspection rather than electrical characterisation ocp component compatibility v15. The document is explicit that it "does not define mandatory requirements, acceptance thresholds, certification criteria, or qualification procedures" and must not be read as establishing service life, so it functions as a shared test methodology rather than a pass/fail standard ocp component compatibility v15.

The practical consequence is that immersion deployment risk sits less in the thermal design than in the absence of an agreed reliability threshold. Two vendors can run the same soak-and-inspect protocol and reach different conclusions about whether a part is fluid-compatible, because the guideline deliberately declines to set acceptance criteria ocp component compatibility v15.

## Competitive landscape

Immersion is one of several liquid cooling routes competing for AI datacentre thermal budgets. As of May 2026, direct-to-chip and immersion were both described as driving innovation with no single winner identified, in a market forecast to reach USD 17.8 billion by 2036 thermal stack arms race ai datacenter liquid cooling market. Direct-to-chip confines the fluid to a sealed loop and leaves the rest of the board air-exposed, avoiding the component compatibility problem that immersion has to solve through soak testing; immersion in exchange contacts every heat source directly. The sources do not resolve which approach wins at scale.

## Evidence base

- Direct-to-chip and immersion cooling are both cited as innovation drivers in AI datacentre thermal management, with no single winner identified as of 5 May 2026 thermal stack arms race ai datacenter liquid cooling market.
- The AI datacentre liquid cooling market is forecast to reach USD 17.8 billion by 2036 thermal stack arms race ai datacenter liquid cooling market.
- OCP published Component Compatibility Testing Guidelines v1.5 for immersion fluids in June 2026, shared publicly in a 20 July 2026 interview ocp component compatibility v15.
- The v1.5 guideline explicitly disclaims mandatory requirements, acceptance thresholds, certification criteria and qualification procedures, and does not establish service life ocp component compatibility v15.
- Thermal interface materials are classified as Type 1 (not electrically functional), with a test path of soak exposure plus physical inspection ocp component compatibility v15.
- Supporting detail derives from the OCP Advanced Cooling Solutions workstream deck dated 4 February 2025; v1.5 quotes in the source are search-indexed rather than read from the gated PDF ocp component compatibility v15.

## Frontier (open questions)

- Does OCP or any hyperscaler publish numerical acceptance thresholds and a stated service life for immersion fluid compatibility, converting v1.5 from methodology into a qualification standard?
- What share of new AI training datacentre commissionings at or above 50 MW per site specify immersion versus direct-to-chip, and does either exceed 50% by 2027?
- Do soak-and-inspect results for Type 1 components correlate with field failure rates over multi-year deployment, or does the absence of electrical testing miss degradation modes?
- Which fluid chemistries pass compatibility testing across the full component taxonomy, and what cost per kW does that impose relative to direct-to-chip?

*Synthesised 2026-08-31 from 4 KB sources by the resynth pipeline; citations are KB source slugs.*
