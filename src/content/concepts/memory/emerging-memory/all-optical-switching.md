---
type: concept
slug: all-optical-switching
canonical_name: All-Optical Switching
aliases:
- AOS
- all optical switching
- single-pulse switching
- single-shot switching
- helicity-independent switching
- HIS
- helicity-dependent switching
- HDS
- ultrafast optical switching
- opto-magnetic switching
- Co/Gd switching
parent_concepts:
- magneto-optical
related_concepts:
- magneto-optical
- photonic-memory
- thin-film-magnetics
- spintronics
sources:
- '[[2026-05-24-mose2-exciton-polariton-all-optical-switch]]'
- '[[2024-08-30-optical-dram-integrated-magneto-photonic-non-volatile-multi]]'
frontier:
- Does single-pulse AOS stay deterministic below ~500 nm device width? Switching goes stochastic above it, and sub-500 nm is where the density argument lives.
- Can the write source (an ultrafast laser) be integrated and manufacturable on a PIC, or does it stay a benchtop femtosecond system?
- Does AOS get paired with integrated OPTICAL readout, rather than the electrical Hall readout the best demos still use?
last_updated: '2026-07-15'
tags:
- concept
- core-concept
mention_count: 8
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-07-26-ai-backend-network-optics-2026
  title: 'Dell''Oro: AI back-end switching past $100B by 2030, optical transport $16B in 2025'
  date: '2026-07-26'
  kind: web
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2024-08-30-optical-dram-integrated-magneto-photonic-non-volatile-multi
  title: Integrated magneto-photonic non-volatile multi-bit memory
  date: '2024-08-30'
  kind: web
neighbors:
- slug: magneto-optical
  name: Magneto-Optical Memory
  path: /memory/emerging-memory/magneto-optical/
  macro: memory
- slug: photonic-memory
  name: Photonic Memory
  path: /memory/emerging-memory/photonic-memory/
  macro: memory
- slug: thin-film-magnetics
  name: Thin Film Magnetics
  path: /materials/functional-layers/thin-film-magnetics/
  macro: materials
- slug: spintronics
  name: Spintronics
  path: /memory/emerging-memory/spintronics/
  macro: memory
---
## The mechanism

An ultrafast (femtosecond-scale) optical pulse dumps energy into a ferrimagnetic film and drives the two magnetic sublattices out of equilibrium at different rates. In the right material (canonically **Co/Gd** and **GdFeCo**), the magnetisation reverses deterministically from a single pulse. The switching is **helicity-independent** in these ferrimagnets, meaning the pulse doesn't need circular polarisation of a particular handedness, which matters a lot for building a real device.

Speed is the headline: this is a picosecond-scale write, which is where the "~1,000x faster than HBM cell activation" class of claim comes from. It is non-volatile and low-energy, because you are not holding a charge, you are flipping a domain and walking away.

## Where it actually is (Jul 2026)

The strongest integrated result is **single-pulse AOS of Co/Gd on a SiN waveguide at 90% contrast** (arXiv 2511.02440, Nov 2025, TU Eindhoven / LioniX). Two caveats define the frontier:

1. **Readout is electrical (Hall), not optical.** The write is integrated; the read is not. This is the class-wide gap.
2. **Switching goes stochastic above ~500 nm device width.** Deterministic behaviour lives below that, which is both the constraint and, awkwardly, exactly where the density argument needs it to work.

## Why it isn't sufficient on its own

AOS solves the **write**. It does not solve **addressing** (how one diffraction-limited port serves many nm-scale domains) or **readout**. A company that has AOS working has the least-hard of the three problems solved. Worth remembering when a founder leads with switching speed: the binding constraint is downstream of the thing being demoed.

## Research lineage