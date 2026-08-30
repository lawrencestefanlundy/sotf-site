---
type: concept
slug: arpes
canonical_name: ARPES (Angular-Resolved Photoemission Spectroscopy)
aliases:
- angular-resolved photoemission
- photoemission spectroscopy
parent_concepts:
- electron-scale-metrology
related_concepts:
- stm
- electron-scale-metrology
sources: []
frontier:
- In-situ ARPES on growth platforms — Pauli-specific or already capable at SLAC, IMEC, PNNL?
last_updated: 2026-05-27
tags:
- concept
- semiconductors
- condensed-matter
mention_count: 38
sources_7d: 0
sources_30d: 6
recent_mentions: []
neighbors:
- slug: stm
  name: STM (Scanning Tunneling Microscopy)
  path: /manufacturing/equipment-processes/stm/
  macro: manufacturing
- slug: electron-scale-metrology
  name: Electron-scale metrology
  path: /manufacturing/equipment-processes/electron-scale-metrology/
  macro: manufacturing
---
Shine high-energy photons (UV or soft X-ray) at a material surface; photoelectrons fly out; measure their energy + emission angle in a hemispherical detector. From the energy-vs-momentum spectrum you reconstruct the **electronic band structure E(k)** of the material directly.

Used for ~40 years in condensed-matter physics, primarily on exotic materials (high-Tc superconductors, topological insulators, manganites). The Pioneer of the technique is zhi-xun-shen at Stanford.

## Why semiconductors care now

If you measure band structure *during* heteroepitaxial growth, you close the materials-discovery feedback loop. See [Electron-scale metrology](/manufacturing/equipment-processes/electron-scale-metrology/).

## Status in semiconductor toolchains

## Limitations

- Requires UHV (ultra-high vacuum)
- Surface-sensitive (penetrates 1–10 nm)
- Sample size: traditionally lab-scale (mm to cm), not wafer-scale
