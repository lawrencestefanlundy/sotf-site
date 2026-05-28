---
type: concept
slug: fdtd-calibration-wall
canonical_name: FDTD-to-Hardware Calibration Wall
aliases:
- calibration wall
- simulation-to-hardware gap
- sim2real for analog compute
parent_concepts:
- analog-computing
- non-conventional-computing
related_concepts:
- coherent-ising-machine
- stochastic-ising-machines
- memristors
- probabilistic-computing
sources: []
frontier:
- Has any published precedent closed the FDTD-to-realised-J gap to <5% on a >=N=64 coupled-oscillator Ising substrate?
- Does FPGA pre-distortion preserve nanosecond latency at production scale, or does the calibration loop dominate the budget?
- 'Per-chip vs population calibration: does each fabricated chip need its own profile, or can a population model close the gap?'
last_updated: 2026-05-22
tags:
- concept
- compute
- analog-computing
- calibration
sources_7d: 0
sources_30d: 2
recent_mentions: []
neighbors:
- slug: coherent-ising-machine
  name: Coherent Ising Machine
  path: /sotf-site/compute/non-conventional/coherent-ising-machine/
  macro: compute
- slug: stochastic-ising-machines
  name: Stochastic / Ising Machines
  path: /sotf-site/compute/non-conventional/stochastic-ising-machines/
  macro: compute
- slug: memristors
  name: Memristors
  path: /sotf-site/compute/non-conventional/memristors/
  macro: compute
- slug: probabilistic-computing
  name: Probabilistic Computing
  path: /sotf-site/compute/non-conventional/probabilistic-computing/
  macro: compute
---
The structural reason analog computing companies die. The simulator (FDTD electromagnetic, SPICE circuit, or whatever physics model the architecture uses) predicts one thing; the fabricated chip behaves differently. The gap is typically 5-15% of the modelled response, and that delta often eats the entire performance claim the company is built on.

## The pattern

Every analog accelerator company follows the same trajectory:

1. **Architecture validated in simulation** — clean ODE / circuit model produces ideal results
2. **First silicon (or PCB) arrives** — measured response differs from simulation
3. **Per-chip calibration burden discovered** — every fabricated unit needs its own correction profile
4. **Drift discovered** — temperature, age, bias history all move the calibration target
5. **Calibration latency dominates** — the correction loop eats the headline speed claim
6. **Pivot, downsize, or die**

## Notable casualties

| Company | Substrate | Outcome | Cause |
|---|---|---|---|
| Mythic AI | Analog flash matrix-mul | Pivoted, downsized | Per-cell conductance drift + die-to-die variability eroded the analog speedup |
| HP Labs memristor | Resistive RAM crossbars | Team disbanded | Sneak paths, write variability, decade of papers without commercial scale |
| Lightelligence | Photonic Ising → photonic matmul | Pivoted to interconnect | Mach-Zehnder interferometer mesh calibration at scale |
| Lightmatter (early) | Photonic Ising machine | Pivoted to optical matrix-mul, then interconnect | Same MZ calibration class |

## Notable survivors (and how they survived)

| Company | Substrate | Survival mechanism |
|---|---|---|
| **Ntt Research** CIM | Photonic OPO + fibre loop | Pushed calibration into digital measurement-feedback at ms latency; works but loses 1000x on per-solve time |
| **D Wave** | Cryogenic superconducting | Different physics class — calibration happens via slow annealing, not a fast realised-J target |
| Toshiba SBM, Fujitsu DA | Digital simulation of Ising | Avoided the wall by not building analog hardware |

## DD signals to listen for

- "We've simulated the calibration loop end-to-end including realistic noise and drift" → strong
- "FPGA pre-distortion is in the M1 milestone" without algorithm spec → weak
- "We'll figure it out at scale" → fatal
- "Each chip needs ~1 hour of VNA calibration" → operational but tractable
- "Each chip needs days of calibration" → not viable at production volume
- "Calibration drifts daily with temperature" → unworkable for edge deployment

## Sources

<!-- dataview block stripped for public site -->
