---
type: concept
slug: near-field-rf-coupling
canonical_name: Near-Field RF Coupling (as compute substrate)
aliases:
- near-field-coupled microstrip antennas
- RF-substrate Ising machine
parent_concepts:
- coherent-ising-machine
- analog-computing
related_concepts:
- coherent-ising-machine
- fdtd-calibration-wall
- mature-foundry-positioning
sources: []
frontier:
- Has any prior team (Chinese RIS / metamaterial, US defence lab, EU H2020 deliverable) demonstrated antenna-array Ising at >=N=64 with published calibration data?
- At what frequency does the trade-off between unit-cell footprint and coupling-range distance optimise (32 GHz vs 60 GHz vs 77 GHz)?
- Does 3D-stacking via glass interposers (Ephos-class) actually preserve the wireless coupling advantage or reintroduce vertical crosstalk?
last_updated: 2026-05-22
tags:
- concept
- compute
- rf
- antenna
- ising-machine
sources_7d: 0
sources_30d: 2
recent_mentions: []
neighbors:
- slug: coherent-ising-machine
  name: Coherent Ising Machine
  path: /sotf-site/compute/non-conventional/coherent-ising-machine/
  macro: compute
- slug: fdtd-calibration-wall
  name: FDTD-to-Hardware Calibration Wall
  path: /sotf-site/compute/non-conventional/fdtd-calibration-wall/
  macro: compute
---
## Why hasn't this been done before

Six reasons (descending importance):

1. **Cultural orthogonality.** Antenna engineers minimise coupling. CIM researchers came from optics. Nobody crossed both.
2. **Wired-coupling lower resistance.** The non-optical CIM community (Roychowdhury Berkeley, Chris Kim Minnesota, Shukla Notre Dame) all went wired electrical because SPICE-model-friendly and VNA-testable. Radiative coupling needs full-wave FDTD simulation which is computationally expensive and outside standard IC EDA flow.
3. **Reconfigurability harder for radiative.** Wired J is set by switchable lumped components. Radiative J is set by fabrication geometry + per-tile resonance modulation; the inverse design problem (find varactor states such that realised J ≈ target J) is non-trivial.
4. **Adjacent RIS field optimises for radiation.** Reconfigurable Intelligent Surfaces (RIS) and metamaterial antenna arrays do use varactor-tuned dipole/patch arrays, but the objective is radiation (steer a beam, shape a wavefront) not internal energy minimisation. Mapping RIS to Ising solver has not been formally published.
5. **Tooling cost.** Full-wave EM simulation at array scale only became affordable at 16-tile / 64-tile in the last few years.
6. **Calibration wall.** Anyone who tried hit the [FDTD-to-Hardware Calibration Wall](/sotf-site/compute/non-conventional/fdtd-calibration-wall/) and didn't publish the failure.

## Prior art to verify in DD

Aggressive prior-art search needed in three places:
- **Chinese RIS / metamaterial Ising literature** (last 3 years, large active community, English visibility weak)
- **US defence labs** — MIT Lincoln Lab, JHU APL, DARPA TRIAD / MORPH / OPTIMA programmes (would publish little but final reports may list dead branches)
- **EU H2020 / Horizon Europe** photonic + RF unconventional-computing project deliverables

If those return clean, the "no one's been here before" claim survives. If a 2022 Chinese paper or DARPA final report turns up doing exactly this, the IP wedge collapses fast.

## Adjacent prior art (known)

- **SWIM** (YIG + microwave components, Nature Comm Phys 2023) — microwave-band Ising machine, different physical medium (yttrium iron garnet), <100 spins
- **50-spin SAW Ising machine** (Nature Comm Phys 2025) — surface acoustic wave, microwave-band, <100 spins
- **Nature Electronics 65nm CMOS varactor Ising (2025)** — wired coupled-oscillator with varactor tuning, closest direct prior art on the coupling-modulation mechanism

## Why now (technology readiness)

- 5G mmWave silicon (24-40 GHz) pushed CMOS-RF and RF-SOI processes into production at GF, TSMC, Samsung with mature design kits (Sivers Wireless, Movandi, WiFi 7)
- Intel Agilex 9 RF DACs shipping since 2023 — the control layer needed to programme antenna-array varactors at GHz speeds is off-the-shelf
- Full-wave FDTD simulators on commodity HPC enable 64-tile + 256-tile EM characterisation at affordable cost

## Sources

<!-- dataview block stripped for public site -->
