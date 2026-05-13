---
type: concept
slug: power-management-ic
canonical_name: Power Management ICs (PMIC)
aliases: []
kind: technology
parent_concepts:
- energy-power
- power-electronics
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

Power Management ICs convert, regulate, and distribute electrical power within a system. Core functions: DC-DC conversion (buck, boost, buck-boost), LDO regulation, battery charging, load switching, and sequencing. Key parameters: conversion efficiency (90–98% for modern switchers), switching frequency (1–10 MHz range for compact inductors), quiescent current (sub-100 nA for IoT), output voltage accuracy (±1–2%), and transient response. Advanced PMICs integrate multiple rails, fuel gauging, and telemetry on a single die. Leading nodes are 40–180 nm BCD (Bipolar-CMOS-DMOS), balancing high-voltage tolerance with logic density. SoC-integrated PMICs from Apple, Qualcomm, and MediaTek handle >20 rails per package. Discrete market leaders: Texas Instruments, Renesas, Infineon, Monolithic Power Systems.

## Competitive landscape

The primary competitive axis is integration depth: discrete PMICs vs. co-packaged power vs. fully integrated on-SoC power delivery. GaN-based power stages (EPC, Navitas, GaN Systems) threaten silicon at higher frequencies and voltages. Switched-capacitor (charge pump) architectures compete where magnetics are prohibited. Soft-switching topologies challenge hard-switching in efficiency-critical applications.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
