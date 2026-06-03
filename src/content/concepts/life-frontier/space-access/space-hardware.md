---
type: concept
slug: space-hardware
canonical_name: Space Hardware
aliases:
- spacecraft hardware
- satellite hardware
kind: category
parent_concepts:
- life-frontier
- space-access
related_concepts:
- rad-hard-ics
- space-grade-fpgas
- space-propulsion
- reusable-launch
sources: []
frontier:
- Can COTS-based (commercial off-the-shelf) satellite buses achieve acceptable reliability for LEO megaconstellation missions without traditional rad-hard qualification?
- What is the power-density limit for solar panels in GEO without active thermal management at high albedo?
- How do attitude-control systems scale down to sub-1 kg cubesat form factors without reaction wheels?
last_updated: 2026-06-02
tags:
- concept
- category
mention_count: 0
descendants: []
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: rad-hard-ics
  name: Rad-Hard ICs
  path: /sotf-site/life-frontier/space-access/rad-hard-ics/
  macro: life-frontier
- slug: space-grade-fpgas
  name: Space-Grade FPGAs
  path: /sotf-site/life-frontier/space-access/space-grade-fpgas/
  macro: life-frontier
- slug: space-propulsion
  name: Space Propulsion
  path: /sotf-site/life-frontier/space-access/space-propulsion/
  macro: life-frontier
- slug: reusable-launch
  name: Reusable Launch (SpaceX, Rocket Lab Neutron)
  path: /sotf-site/life-frontier/space-access/reusable-launch/
  macro: life-frontier
---
Space hardware refers to the physical platform systems that make up a spacecraft: the bus (structural chassis, power, attitude control, thermal management, communications) and the payload (sensors, instruments, propulsion). Unlike terrestrial electronics, space hardware must withstand total ionising dose (TID), single-event effects (SEE), extreme thermal cycling (−150°C to +120°C in LEO), vacuum outgassing, and launch vibration loads — all without maintenance access.

**Power systems** dominate mass budget. GaAs triple-junction solar cells achieve ~30% efficiency (vs ~22% for silicon) and are space-heritage qualified. Li-ion batteries handle eclipse periods; battery specific energy is the binding constraint on power budgets for small sats.

**Attitude determination and control systems (ADCS)** use combinations of reaction wheels, magnetorquers, star trackers, and sun sensors. Pointing accuracy requirements cascade directly from payload needs (e.g. <0.01° for optical EO vs <1° for communications).

**Investment relevance:** the most interesting fundable space is subsystem innovation — novel materials for thermal management, AI-driven on-board processing, or new reaction-wheel designs for small form factors. The bus market itself is consolidating.

## Frontier

- Can COTS-based satellite buses achieve acceptable reliability for LEO megaconstellations without traditional rad-hard qualification?
- What is the power-density limit for GEO solar panels without active thermal management at high albedo?
- How do ADCS systems scale below 1 kg for cubesat form factors without reaction wheels?

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
