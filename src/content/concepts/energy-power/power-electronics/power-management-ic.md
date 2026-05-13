---
type: concept
slug: power-management-ic
canonical_name: Power Management ICs (PMIC)
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
- adagio-semiconductor
- ams-osram-power-ics-division
- analog-devices
- arigami
- chargepoint-technology-silanna-semiconductor
- efficient-power-conversion-epc
- enovix-power-ic-integration
- enpirion-intel-psg
- eta-compute
- infineon-technologies
- inphi-marvell
- intelesens-nexperia-power-management
- mediatek
- monolithic-power-systems-mps
- movella-mcube-lineage-bel-fuse-power-solutions
- nordic-semiconductor
- parabellum-energy
- qorvo-active-products-power-division
- qualcomm-power-management-division
- renesas-electronics
- richtek-technology
- semtech
- silergy-hangzhou-silan-silergy-corp
- stmicroelectronics
- texas-instruments
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


# Power Management ICs (PMIC)

*Kind: technology*

## Physics / mechanism

Power Management ICs convert, regulate, and distribute electrical power within a system. Core functions: DC-DC conversion (buck, boost, buck-boost), LDO regulation, battery charging, load switching, and sequencing. Key parameters: conversion efficiency (90–98% for modern switchers), switching frequency (1–10 MHz range for compact inductors), quiescent current (sub-100 nA for IoT), output voltage accuracy (±1–2%), and transient response. Advanced PMICs integrate multiple rails, fuel gauging, and telemetry on a single die. Leading nodes are 40–180 nm BCD (Bipolar-CMOS-DMOS), balancing high-voltage tolerance with logic density. SoC-integrated PMICs from Apple, Qualcomm, and MediaTek handle >20 rails per package. Discrete market leaders: Texas Instruments, Renesas, Infineon, Monolithic Power Systems.

## Competitive landscape

The primary competitive axis is integration depth: discrete PMICs vs. co-packaged power vs. fully integrated on-SoC power delivery. GaN-based power stages (EPC, Navitas, GaN Systems) threaten silicon at higher frequencies and voltages. Switched-capacitor (charge pump) architectures compete where magnetics are prohibited. Soft-switching topologies challenge hard-switching in efficiency-critical applications.

## Cloudberry relevance

| Approach | Efficiency | Integration | Frequency range |
|---|---|---|---|
| Si BCD PMIC | 90–96% | High | 1–10 MHz |
| GaN power stage | 95–99% | Low–mid | 10–100 MHz |
| Switched-capacitor | 85–95% | High | 10–100 MHz |


GF's BCD and 180 nm analog processes are direct PMIC manufacturing substrates—deal flow in fabless PMIC startups targeting AI edge, satellite, and EV subsystems is natural. Photonics co-packaged optics demand tight on-package power delivery, creating whitespace for specialized PMICs. Lunar Ventures' seed exposure to European analog/mixed-signal teams makes early PMIC-adjacent bets plausible. Watch: PMICs for chiplet power domains and cryogenic compute.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
