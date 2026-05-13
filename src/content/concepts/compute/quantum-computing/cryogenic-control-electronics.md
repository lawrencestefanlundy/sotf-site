---
type: concept
slug: cryogenic-control-electronics
canonical_name: Cryogenic Control Electronics
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- quantum-computing
related_concepts: []
companies_using:
- atlantic-quantum
- bleximo
- bluefors
- cryogenic-control-systems-cryocon
- delft-circuits
- emergence-quantum
- entanglement-industries
- formfactor-hpd
- ibm-quantum
- intel-horse-ridge
- keysight-technologies
- leoni-quantum-solutions-formerly-part-of-leoni
- maybell-quantum
- nmqc-national-instruments-quantum-china
- orizon-quantum-formerly-coldquanta-spin-off-lineage
- qblox
- quantum-machines
- quantware
- rohde-schwarz
- scalinq
- seeqc
- semiqon
- yukawa-institute-qunasys-spin-q-ctrl-au-cryogenic-division
- zurich-instruments
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


# Cryogenic Control Electronics

*Kind: technology*

## Physics / mechanism

Cryogenic control electronics (cryo-CMOS) refers to classical semiconductor circuits operated at 4 K or below to co-locate qubit control logic with quantum processors, eliminating the thermal bottleneck imposed by coaxial cable bundles running from room-temperature racks. At 4 K, CMOS threshold voltage shifts ~100–150 mV, carrier freeze-out becomes a concern below ~1 K, and 1/f noise changes character — all parameters that must be characterised per node. Leading cryo-CMOS multiplexers achieve ~1 mW/qubit power budgets at 4 K; the 15–20 mW cooling capacity of a dilution refrigerator's 4 K stage is the hard constraint. Intel's Horse Ridge II and QuTech's work on 22 nm FD-SOI demonstrate gate fidelity-compatible drive signals at scale. SiGe BiCMOS is competitive above 4 K for low-noise amplification. TSMC 28 nm and GlobalFoundries 22FDX have both been characterised in academic cryo literature.

## Competitive landscape

The dominant alternative is room-temperature electronics with high-bandwidth coaxial interconnects — works below ~100 qubits, impractical at 1000+. SiGe HBT offers superior noise figure for readout chains but higher power. Photonic interconnects (microwave-to-optical transduction) aim to sidestep the thermal budget entirely but remain pre-product. InP HEMT is standard for 4 K LNA readout but not integration-friendly.

## Cloudberry relevance

| Approach | Power/channel | Integration density | Maturity |
|---|---|---|---|
| Cryo-CMOS (22FDX/28nm) | ~1–5 mW | High | Pilot |
| SiGe HBT | ~2–10 mW | Medium | Lab |
| Room-temp + coax | ~50–200 mW equiv. | Low | Production |


GF 22FDX has explicit cryo characterisation data, making it the most investable node for cryo-CMOS startups — direct relevance to the GF-LP fund's LP relationship and fab access leverage. Deal-flow sits at the intersection of quantum computing stack companies (control IC designers), EDA tool vendors adding cryo PDKs, and packaging players solving the 4 K interconnect density problem. Lunar Ventures' quantum-adjacent portfolio and Cloudberry's semiconductor depth together cover the full stack from process node to system architecture.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
