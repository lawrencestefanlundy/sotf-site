---
type: concept
slug: energy-harvesting
canonical_name: Energy Harvesting
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- energy-power
- energy-storage
related_concepts: []
companies_using:
- ambient-photonics
- analog-devices-adi
- atmosic-technologies
- dracula-technologies
- e-peas
- enocean
- epishine
- everactive
- imprint-energy
- kinergizer
- kinetic-energy-harvesting-keh-pavegen
- mouser-renesas-electronics
- nowi-energy
- powercast
- powerspot-formerly-yank-technologies
- psikick-acquired-by-everactive-legacy-noted
- reactec
- sceye
- solea-energy
- stmicroelectronics
- tectus-enerbee
- texas-instruments
- wevolver-nexperia-reference-nexperia
- wiliot
ideas_referencing: []
sources:
- '[[2025-04-16-the-state-of-photonic-computing]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 14
descendants:
- batteries-energy-storage
- energy-generation
- energy-harvesting
- energy-materials
- energy-power
- flow-batteries
- lithium-sulphur-batteries
- pem-electrolysers
- perovskite-solar
- renewable-electricity
- sodium-ion-batteries
- solar-photovoltaic
- solid-oxide-fuel-cells
- solid-state-batteries
- tandem-solar-cells
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 2
---

# Energy Harvesting

*Kind: technology · Attio deal count: 11*

## Physics / mechanism

Energy harvesting converts ambient environmental energy—thermal gradients, mechanical vibration, RF fields, or photons—into usable electrical power. Core mechanisms: thermoelectric (Seebeck effect, ZT ≥ 1.5–2.0 in best-in-class BiTe alloys), piezoelectric (PZT, AlN on MEMS; output 10–500 µW/cm² at resonance), photovoltaic (indoor OPV/perovskite reaching 25–30% under fluorescent spectra), and RF rectenna (sub-µW to low-µW at –20 dBm input). Target envelope: µW to low-mW continuous power for always-on IoT nodes, wearables, and distributed sensors. Key constraint is power density vs. source intermittency; duty-cycled loads and ultra-low-power MCUs (sub-µA sleep) define the system budget.

## Competitive landscape


Primary competition is the coin cell and thin-film primary battery—cheap, predictable, but replacement-cost-heavy at scale (billions of nodes). Secondary competition: energy-dense rechargeable (LiFePO4 micro-cells) combined with BLE duty cycling, which often beats harvesting on $/node deployed. Adjacent spaces include wireless power transfer (AirFuel, Qi, long-range RF beamforming) and fuel cells for industrial sensors. Material adjacencies: GaN-on-Si for rectenna efficiency, AlScN piezo films (higher coupling coefficient than AlN), and halide perovskite for flexible PV.

| Approach | Power density | Lifetime | Integration cost |
|---|---|---|---|
| Thermoelectric | ~50 µW/cm²/K | >10 yr | Medium |
| Piezoelectric MEMS | 10–500 µW/cm² | 5–10 yr | Low–Medium |
| Indoor PV (OPV) | 20–100 µW/cm² | 3–7 yr | Low |

## Cloudberry relevance
Cloudberry's angle is the semiconductor substrate layer: AlScN piezo films and GaN rectennas are foundry-compatible processes adjacent to GlobalFoundries' specialty nodes. Deal-flow targets include MEMS-first fabless teams needing advanced nitride process access, and ultra-low-power mixed-signal IP vendors enabling sub-threshold harvesting ASICs. Lunar Ventures' software-hardware portfolio companies in industrial IoT and edge sensing create natural co-investment pipeline where eliminating battery maintenance is a hard customer requirement, not a feature.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
