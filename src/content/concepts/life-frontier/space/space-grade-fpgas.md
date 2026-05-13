---
type: concept
slug: space-grade-fpgas
canonical_name: Space-Grade FPGAs
aliases: []
kind: technology
parent_concepts:
- life-frontier
- space
related_concepts: []
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
## Physics / mechanism

FPGAs hardened for space use radiation-tolerant logic fabrics that survive total ionizing dose (TID) and single-event effects (SEE) in LEO/GEO/deep-space environments. Two dominant hardening approaches: radiation-hardened-by-process (RHBP), where foundry implants and SOI substrates suppress charge collection, and radiation-hardened-by-design (RHBD), using triple-modular redundancy (TMR) and scrubbing in commercial-process FPGAs. Key vendors — Microchip (RTG4, 150 krad TID, 1.26M logic elements, 28nm FD-SOI derivative), Xilinx/AMD (Kintex Ultrascale XT via SEAKR integrators), Cobham/Aeroflex legacy parts — define the state of the art. Clock rates run 200–400 MHz; power budgets 2–15 W depending on utilization and SEL mitigation. Reprogrammability is the core value: payload logic updates on-orbit without hardware swap.

## Competitive landscape

Competing approaches: ASICs offer better rad-hard performance per watt but require $10–50M NRE and multi-year schedules, viable only at high volume. Rad-hard microprocessors (LEON4, RAD750) handle control-plane tasks but lack parallelism for DSP/image processing. RHBD on COTS FPGAs (Xilinx Artix, Intel Cyclone) cuts cost 10×, acceptable for LEO CubeSats below 10 krad missions. Emerging: SRAM-based FPGAs with on-orbit scrubbing vs. flash-based non-volatile architectures (Microchip ProASIC3, Lattice iCE) trade reprogrammability for upset immunity.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
