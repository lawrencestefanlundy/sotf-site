---
type: concept
slug: electric-motors-drives
canonical_name: Electric Motors & Drives
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
- additive-drives
- borgwarner
- cascadia-motion
- danfoss
- emotors
- enstroj
- equipmake
- heliox
- infineon-technologies
- intellidrives
- kinetic-traction-systems
- levc-geely-electric-drivetrains
- magnax
- mavel
- molabo
- nidec-corporation
- phi-power
- rimac-technology
- saietta-group
- siemens
- stmicroelectronics
- turntide-technologies
- yasa-mercedes-benz-subsidiary
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 2
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---


# Electric Motors & Drives

*Kind: technology · Attio deal count: 2*

## Physics / mechanism

Electric motors convert electrical energy to mechanical torque via electromagnetic induction or permanent-magnet interaction. Key topologies: induction motors (AC, squirrel-cage), brushless DC (BLDC), permanent magnet synchronous motors (PMSM), and switched reluctance motors (SRM). Performance is governed by torque density (Nm/kg), efficiency (peak >97% in SiC-driven PMSM systems), and thermal limits set by winding insulation class. Drives—the inverter + control stack—determine dynamic response; field-oriented control (FOC) and direct torque control (DTC) are standard. State of art: 10–20 kW/kg in aerospace-grade axial-flux motors; EV traction motors hit 96–98% peak efficiency with SiC MOSFET inverters at 800V bus.

## Competitive landscape

---

## Cloudberry relevance

The real competitive axis is motor topology vs. magnet supply-chain risk. PMSMs dominate on efficiency but depend on rare-earth NdFeB; SRMs and induction motors trade efficiency for supply-chain independence. Adjacent: linear motors (semiconductor fab stages, hyperloop), piezoelectric actuators (precision positioning, no magnets), and hydraulic actuators (heavy aerospace, declining). The drive semiconductor substrate is the sharpest battleground—Si IGBT → SiC MOSFET → GaN is the migration path, each step enabling higher switching frequency, smaller passives, and better partial-load efficiency.

| Topology | Peak η | Magnet dependency | Torque density |
|---|---|---|---|
| PMSM | ~98% | High (NdFeB) | High |
| SRM | ~94% | None | Medium |
| Induction | ~96% | None | Medium |

---

Cloudberry's entry point is the semiconductor substrate enabling the drive, not the motor itself. SiC and GaN power devices are the value-capture layer—GlobalFoundries' SiC roadmap and fabs like Wolfspeed and onsemi are reference points for deal benchmarking. Advanced magnetic materials (amorphous cores, soft magnetic composites) touch the advanced-materials thesis directly. Watch for startups vertically integrating axial-flux motor design with custom power electronics—that's where IP moats form. Rare-earth magnet alternatives (MnBi, ferrite-enhanced designs) are an adjacent materials bet worth tracking.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
