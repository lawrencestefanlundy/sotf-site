---
type: concept
slug: single-photon-detectors
canonical_name: Single Photon Detectors
aliases: []
parent_concepts:
- imaging
- sensing
related_concepts:
- avalanche-photodiode
- image-sensors
- quantum
sources:
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
auto_stub: false
last_updated: 2026-08-03
tags:
- concept
mention_count: 4
descendants:
- spad
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2024-12-04-cubits-in-a-fridge-why-is-nobody
  title: Silicon Spin Quantum Computing (Feat. Himadri Majumdar, SemiQon)
  date: '2024-12-04'
  kind: substack
neighbors:
- slug: avalanche-photodiode
  name: Avalanche Photodiode (APD / SPAD)
  path: /photonic-systems/modulators-detectors/avalanche-photodiode/
  macro: photonic-systems
- slug: image-sensors
  name: Image Sensors
  path: /sensing/imaging/image-sensors/
  macro: sensing
- slug: quantum
  name: Quantum technologies
  path: /compute/quantum-computing/quantum/
  macro: compute
---
## Primer (web-enriched 2026-08-03)

A **SPAD** is an avalanche photodiode biased above breakdown ("Geiger mode"), so a single photon triggers a self-sustaining avalanche and a digital pulse. That makes it a photon *counter* with picosecond timing rather than an analogue light-level sensor — the basis for time-of-flight ranging, fluorescence-lifetime imaging (FLIM), Raman spectroscopy, quantum optics and photon-counting imaging.

The commercially interesting shift is **compute under the pixel**: 3D-stacking digital logic beneath the SPAD array so counting, timing and histogramming happen on-chip before data leaves the sensor. Both independents and incumbents are now competing on this ground.

### Market structure — the incumbent is STMicroelectronics

This corrects a long-standing framing error in **Image Sensor Silicon**, which anchored its incumbent argument on Sony's ~50% CMOS-image-sensor share. That is the mainstream CIS roof and does not describe SPAD.

- ****Stmicroelectronics**** leads, on CMOS-integrated SPAD, vertical manufacturing, and huge consumer + automotive ranging volume. 28 nm FD-SOI integration, sub-40 ps timing.
- ****Sony Semiconductor Solutions**** — mass production of a 512x512 SPAD for LiDAR and AR headsets since Jan 2024.
- ****Hamamatsu Photonics**** — strong in scientific and medical instrumentation.
- **Canon** — CES Jan 2026 prototype: 2/3", ~2.1 MP, **156 dB (~26 stops)** via "weighted photon counting" (estimate total arrivals from time-to-first-photon). Computation applied at the counting layer. Canon states it aims for mass production.

**The absorption read:** incumbents are not absent from computational SPAD. They are building it, at volume, aimed at automotive and consumer. Independents cluster in scientific, quantum and medical instrumentation, where volumes are inherently low.

### The independent cohort

Note the lineage concentration: **Edinburgh (Robert Henderson's lab) and EPFL (Charbon) produce most of the European independents.**

### Open question

Why have the incumbents not fully internalised in-pixel-compute SPAD, and can they? Canon's weighted-photon-counting prototype suggests they are moving on exactly this ground. This is the single question that decides whether **Image Sensor Silicon** is a theme or a thesis, and it remains unresolved.

*Full scan, sources and source-quality flags:.*
