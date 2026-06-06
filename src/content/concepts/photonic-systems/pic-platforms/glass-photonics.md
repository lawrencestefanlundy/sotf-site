---
type: concept
slug: glass-photonics
canonical_name: Glass Photonics
aliases:
- glass waveguides
- femtosecond laser direct-write photonics
- laser-written glass waveguides
- glass-based PICs
kind: technology
parent_concepts:
- photonic-integrated-circuits
- pic-platforms
related_concepts:
- glass-interposers
- silicon-photonics
- polymer-photonics
- co-packaged-optics
- photonic-wire-bonding
- photonic-quantum
sources:
- '[[2026-05-30-intel-optoscribe-acquisition]]'
- '[[2026-05-30-intel-glass-substrates-program]]'
- '[[2026-05-30-ephos-funding-glass-photonic-chips]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
frontier:
- Does femtosecond laser-write throughput scale to production volume, or stay the binding constraint (same axis that sank polymer 2PP)?
- Does a glass-substrate prime (Corning/Absolics/AGC) or Intel (post-Optoscribe) absorb glass photonics, foreclosing the startup category?
- Is the curvature-radius limit fatal for dense routing, or is wide-bend point-to-point enough for chiplet interconnect?
last_updated: '2026-05-30'
tags:
- concept
- technology
- photonics
- glass
sources_7d: 0
sources_30d: 3
recent_mentions: []
neighbors:
- slug: glass-interposers
  name: Glass Interposers
  path: /sotf-site/manufacturing/packaging/glass-interposers/
  macro: manufacturing
- slug: silicon-photonics
  name: Silicon Photonics
  path: /sotf-site/photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
- slug: polymer-photonics
  name: Polymer Photonics
  path: /sotf-site/photonic-systems/pic-platforms/polymer-photonics/
  macro: photonic-systems
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: photonic-wire-bonding
  name: Photonic Wire Bonding
  path: /sotf-site/manufacturing/packaging/photonic-wire-bonding/
  macro: manufacturing
- slug: photonic-quantum
  name: Photonic Quantum
  path: /sotf-site/compute/quantum-computing/photonic-quantum/
  macro: compute
---
*The photonic-active cousin of [Glass Interposers](/sotf-site/manufacturing/packaging/glass-interposers/). Glass-interposers = glass carrying **electrical** routing; glass-photonics = glass carrying **light**.*

> **Stack context:** glass photonics is **one option in Layer 1 (fibre-to-chip optical coupling)** of the PIC packaging stack, competing with polymer [Photonic Wire Bonding](/sotf-site/manufacturing/packaging/photonic-wire-bonding/) and edge/grating coupling. It is *not* a [Silicon Photonics](/sotf-site/photonic-systems/pic-platforms/silicon-photonics/) replacement — SiPh is the active platform; glass is the coupling/passive-routing medium around it. Full landscape: **2026 05 30 Pic Packaging Approaches Landscape**.

## Physics / mechanism

Glass photonics writes optical waveguides *inside* a glass substrate (typically fused silica or borosilicate) using **femtosecond laser direct-write**: ultrafast pulses locally raise the refractive index along a 3D path, defining a waveguide buried in the bulk. This is fundamentally different from silicon photonics, which patterns waveguides lithographically *on the surface* of a silicon-on-insulator wafer.

**The load-bearing limit: curvature radius.** Laser-written glass waveguides cannot take tight bends (like an optical fibre, bend too hard and light leaks). So **no compact ring resonators, no dense routing**. Glass is structurally confined to passive routing + the fibre interface + wide-bend point-to-point links. It does not win modulators (TFLN/BTO territory). For meter-scale chiplet-interconnect substrates this matters less; for dense PICs it is disqualifying (**Photonics Material Class War**).

## Competitive landscape — the glass-photonics cohort

Adjacent but different category: **Akhetonics** (Germany, all-optical general-purpose compute chip, ~€8.3M raised) appears as an "Optoscribe competitor" in databases but is optical *compute*, not glass interconnect/packaging — though it *consumes* a laser-etched glass interposer + photonic wire bonding (Fraunhofer-IZM SPOC project).

Contrast with the *electrical* glass-substrate primes (Corning, Absolics/SKC, AGC, Samsung, KCC, LG) tracked under [Glass Interposers](/sotf-site/manufacturing/packaging/glass-interposers/) — those carry copper, not light.

## Evidence base

## Companies / organisations using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)