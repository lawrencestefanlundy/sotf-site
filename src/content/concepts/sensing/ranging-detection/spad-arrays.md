---
type: concept
slug: spad-arrays
canonical_name: SPAD Arrays
aliases: []
kind: technology
parent_concepts:
- sensing
- ranging-detection
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
recent_mentions: []
neighbors: []
---
## Physics / mechanism

A Single-Photon Avalanche Diode (SPAD) is a reverse-biased p-n junction operated above breakdown voltage (Geiger mode). A single photon triggers a self-sustaining avalanche; quenching circuitry resets the diode in nanoseconds. Arrays integrate thousands to millions of SPADs (SiPMs in analog sum mode; dSiPMs with per-pixel TDCs for time-stamped data). Key parameters: photon detection efficiency (PDE, 50–60% peak in Si at 520 nm), dark count rate (DCR, <100 cps/μm² at RT for best-in-class), timing jitter (sub-100 ps FWHM), and fill factor (10–80%, boosted by microlenses). Leading processes: TSMC 40 nm BSI, STMicroelectronics 40 nm, Tower Jazz. Array sizes now reach 400×400 pixels with per-SPAD TDCs at 10 ps resolution.

## Competitive landscape

Direct competitors: linear APD arrays (lower sensitivity, no photon counting), SiPM analog arrays (no spatial/timing resolution per pixel), EMCCD/sCMOS (higher pixel count but microsecond-scale timing). For LiDAR, dToF SPAD arrays compete with FMCW coherent LiDAR (no avalanche noise floor but requires narrow-linewidth laser + complex DSP) and iToF (Sony, TI; lower cost, worse range/ambient rejection).

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
