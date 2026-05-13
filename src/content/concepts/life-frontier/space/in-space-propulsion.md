---
type: concept
slug: in-space-propulsion
canonical_name: In-Space Propulsion (transfer stages, OTVs)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- space
related_concepts: []
companies_using:
- aether-industries
- astroscale
- atomos-space
- cislunar-industries
- d-orbit
- dawn-aerospace
- exotrail
- hyimpulse
- impulse-space
- launcher-now-part-of-vast
- momentus
- morpheus-space
- northrop-grumman-mission-extension-vehicle
- ohb-system
- orbit-fab
- pale-blue-space-bd-subsidiary
- skyrora
- spaceflight-industries-sherpa-otv
- spacetech-gmbh-spee-3d-otv-studies
- starfire-industries
- thales-alenia-space
- thrustme
- turion-space
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

# In-Space Propulsion (transfer stages, OTVs)

*Kind: technology*

## Physics / mechanism

In-space propulsion covers any system that moves a spacecraft once it has left the launch vehicle — orbit raising, station-keeping, lunar/interplanetary transfer, and deorbit. Orbital transfer vehicles (OTVs) are reusable or expendable upper stages that execute high-delta-v maneuvers between orbits. Key parameter is specific impulse (Isp): chemical bipropellants (MMH/NTO, LOX/LH2) deliver Isp ~300–460 s; electric propulsion (Hall-effect, gridded ion) reaches 1,500–10,000 s but at low thrust, suiting slow spirals. Cold/warm gas and green monopropellants (AF-M315E, LMP-103S) sit below 250 s Isp, used for fine attitude control. Emerging options — nuclear thermal (Isp ~900 s), solar thermal, and rotating detonation engines — are at TRL 3–5.

## Competitive landscape

| Approach | Isp (s) | Thrust class | Maturity |
|---|---|---|---|
| Chemical biprop | 300–460 | High (N–kN) | Flight-proven |
| Hall / gridded ion | 1,500–10,000 | Low (mN–N) | Flight-proven (SmallSat scale) |
| Nuclear thermal | ~900 | Medium | TRL 3–4, regulatory risk |

## Cloudberry relevance

Adjacent competitive pressure comes from launch vehicles with reusable upper stages (Starship obviating dedicated OTVs for many trajectories), on-orbit servicing architectures (Northrop MEV, Astroscale), and propellant depots that decouple propulsion mass from launch. The critical substitution risk is Starship point-to-point in-space transfer reducing the OTV market before it scales.

Cloudberry relevance sits at the component and materials layer: propellant feed valves, MEMS thrusters, and power-processing units all require advanced semiconductor packaging and MEMS fabs — potential GlobalFoundries-adjacent supply chain plays. OTV platforms need radiation-hardened SoCs and photonic sensor systems for autonomous rendezvous. Deal-flow angles: propulsion-adjacent deeptech startups supplying PPUs, flow controllers, or GaN-based power electronics to OTV primes.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
