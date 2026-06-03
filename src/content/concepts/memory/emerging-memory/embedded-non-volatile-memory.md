---
type: concept
slug: embedded-non-volatile-memory
canonical_name: Embedded Non-Volatile Memory
aliases:
- eNVM
- embedded NVM
- embedded non-volatile memory
parent_concepts:
- memory
related_concepts:
- mram
- feram
- rram-reram
- pcm-phase-change-memory
- hafnium-oxide-photonic
- in-memory-computing
sources: []
frontier:
- Which NVM technology — MRAM, FeRAM/FeFET, or RRAM — takes embedded-flash's socket below 22nm, and which foundry qualification comes first (TSMC eMRAM, GF FeRAM, or a fabless IP licensor)?
- At what node does retention-endurance co-optimisation become a hard ceiling for FeFET in automotive-grade eNVM (AEC-Q100 Level 1 requires 10-year retention at 150°C)?
- Can compute-in-memory (CIM) architectures move eNVM from a storage function to an active compute substrate, and does that make it the same market as in-memory computing?
last_updated: 2026-06-02
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: mram
  name: MRAM (STT/SOT-MRAM)
  path: /sotf-site/memory/mainstream-memory/mram/
  macro: memory
- slug: feram
  name: FeRAM (Ferroelectric)
  path: /sotf-site/memory/mainstream-memory/feram/
  macro: memory
- slug: rram-reram
  name: RRAM / ReRAM
  path: /sotf-site/memory/emerging-memory/rram-reram/
  macro: memory
- slug: pcm-phase-change-memory
  name: Phase-Change Memory (PCM)
  path: /sotf-site/memory/emerging-memory/pcm-phase-change-memory/
  macro: memory
- slug: hafnium-oxide-photonic
  name: Hafnium Oxide (HfO₂) Photonics
  path: /sotf-site/materials/functional-layers/hafnium-oxide-photonic/
  macro: materials
- slug: in-memory-computing
  name: In-Memory Computing
  path: /sotf-site/memory/emerging-memory/in-memory-computing/
  macro: memory
---
Embedded non-volatile memory (eNVM) refers to NVM arrays integrated monolithically on the same die as logic, in contrast to stand-alone (discrete) memory chips. In a standard SoC the eNVM holds firmware, model weights, calibration constants, and secure boot keys. The dominant incumbent is embedded flash (eFlash), which uses floating-gate or charge-trap transistors; it does not scale cleanly below 28 nm because the tunnel oxide cannot be thinned without catastrophic leakage, and the high programming voltages it requires (12–18 V) are incompatible with advanced-node transistors.

The scaling wall is the core investment signal. As logic migrates to 22 nm and below — driven by edge-AI, automotive MCUs, and IoT — eFlash cannot follow, opening sockets for alternatives. The main contenders are: MRAM (high endurance, fast write, radiation-hard, scales to 22 nm BEOL), FeRAM / FeFET (ultralow write energy via spontaneous polarisation in HfO₂, CMOS-compatible BEOL), RRAM/ReRAM (resistive switching, high density, natural analog compute substrate), and PCM (high density, multibit per cell).

CMOS-compatibility and BEOL integration are the killer feature requirements: an eNVM that demands a separate mask or exotic front-end chemistry cannot be economically embedded. [Ferroelectric HfO2](/sotf-site/materials/functional-layers/ferroelectric-hfo2/) is significant here because HfO₂ is already a gate-dielectric material in sub-28 nm nodes — FeRAM and FeFET inherit that integration path at zero added process complexity.

**Ememory Technology** licenses embedded OTP/MTP and has the broadest foundry coverage for legacy nodes. **Antaios** targets MRAM-based eNVM. The **Ferroelectric Memory Share** thesis models HfO₂-based FeFET capturing ≥5% of embedded NV units by 2030. The **Emerging Nvm** theme maps which NVM wins which socket across automotive, edge-AI, and IoT.

## Frontier

- Which NVM technology — MRAM, FeRAM/FeFET, or RRAM — takes embedded-flash's socket below 22 nm, and which foundry qualification comes first (TSMC eMRAM, GF FeRAM, or a fabless IP licensor)?
- At what node does retention-endurance co-optimisation become a hard ceiling for FeFET in automotive-grade eNVM (AEC-Q100 Level 1 requires 10-year retention at 150 °C)?
- Can compute-in-memory (CIM) architectures move eNVM from a storage function to an active compute substrate, and does that create the same market as [In-Memory Computing](/sotf-site/memory/emerging-memory/in-memory-computing/)?
