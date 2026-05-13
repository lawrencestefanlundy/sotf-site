---
type: concept
slug: solid-state-circuit-breakers
canonical_name: Solid-State Circuit Breakers
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
- amantys
- atom-power
- blixt-tech
- cet-power
- eaton-corporation
- epri-commercialisation-spinouts
- flex-power-control
- grid-invent
- heliox
- ideal-power
- infineon-technologies
- littelfuse
- mersen
- mitsubishi-electric
- nexans-innopower-jv
- on-semiconductor-onsemi
- schneider-electric
- sensata-technologies
- sic-power-sicpower
- siemens
- terence-energy
- turntide-technologies
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


# Solid-State Circuit Breakers

*Kind: technology*

## Physics / mechanism

Solid-state circuit breakers (SSCBs) replace electromechanical contacts with power semiconductor switches—typically SiC MOSFETs, GaN HEMTs, or IGBTs—to interrupt fault currents in microseconds rather than the 10–100 ms of conventional breakers. Interruption relies on gate-controlled channel pinch-off; energy stored in line inductance is dissipated via a transient-voltage-suppression (TVS) clamp or active snubber. Key parameters: trip time (<10 µs for SiC implementations), on-state resistance (contributing conduction losses, typically 1–5 mW·Ω range at ratings), voltage hold-off (currently 1.5–10 kV SiC devices), and I²t withstand. State of the art: 1.2–3.3 kV SiC-based SSCBs at 500–2000 A continuous; bidirectional topologies for DC microgrids. ABB, Eaton, Littelfuse, and startups like Atom Power and Cree/Wolfspeed ecosystem plays are active.

## Competitive landscape

Electromechanical MCBs/ACBs remain dominant on cost ($/A protected) and zero conduction loss. Hybrid breakers (mechanical contact + parallel semiconductor for energy absorption) split the difference—faster than pure mechanical, cheaper than pure solid-state. Fuses compete on simplicity at low cost but are non-resettable. Key differentiator is application: SSCBs win where fast fault isolation, remote reconfiguration, or high cycle rate matters (EV charging, shipboard DC, data-center 400 V DC bus).

## Cloudberry relevance

| Type | Trip time | Conduction loss | Reclosable |
|---|---|---|---|
| Electromechanical MCB | 10–100 ms | ~0 | Yes |
| Hybrid breaker | 1–5 ms | Low | Yes |
| SSCB (SiC) | <10 µs | Moderate | Yes |


Cloudberry / GlobalFoundries-LP lens: SSCBs are a pull-through market for wide-bandgap wafer capacity—SiC and GaN device demand scales directly with SSCB adoption in EV infrastructure, grid-edge storage, and defense microgrids. Deal-flow angles include fabless SiC power IC designers dependent on foundry access (GF's FDX or partner SiC nodes), gate-driver ASIC plays, and monolithic integration of protection logic. Lunar Ventures' software-defined hardware angle maps to programmable trip-curve firmware layered on SSCB platforms.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
