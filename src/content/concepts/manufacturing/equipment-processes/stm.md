---
type: concept
slug: stm
canonical_name: STM (Scanning Tunneling Microscopy)
aliases:
- scanning tunneling microscopy
- scanning probe microscopy
parent_concepts:
- electron-scale-metrology
related_concepts:
- arpes
- electron-scale-metrology
sources: []
frontier:
- Can in-situ STM on growing films achieve useful throughput at industrial scale?
last_updated: 2026-05-27
tags:
- concept
- semiconductors
- condensed-matter
public_expressions:
- IBM
- STM
mention_count: 37
sources_7d: 0
sources_30d: 8
recent_mentions: []
neighbors:
- slug: arpes
  name: ARPES (Angular-Resolved Photoemission Spectroscopy)
  path: /manufacturing/equipment-processes/arpes/
  macro: manufacturing
- slug: electron-scale-metrology
  name: Electron-scale metrology
  path: /manufacturing/equipment-processes/electron-scale-metrology/
  macro: manufacturing
---
Atomically-sharp metallic tip held a few angstroms above a conducting surface; tunneling current between tip and sample images individual atoms and their local electronic state. Invented at IBM Zürich in 1981 (Binnig + Rohrer, Nobel 1986).

## What it measures

- **Topography** (atom-by-atom imaging)
- **Local density of states** (electronic structure at the level of an individual atom site)
- **Spectroscopy** (dI/dV vs V — reveals band gap, surface states, defects)

## Why semiconductors care now

If you can measure local electronic state at an interface during growth, you can iterate material stacks 50–100× faster than averaged-electrical-measurement workflows. See [Electron-scale metrology](/manufacturing/equipment-processes/electron-scale-metrology/).

## Status in semiconductor toolchains

## Limitations

- Slow (atom-by-atom scanning)
- Requires conducting or semi-conducting samples
- Surface-only
- UHV required for clean measurements
