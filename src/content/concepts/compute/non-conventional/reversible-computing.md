---
type: concept
slug: reversible-computing
canonical_name: Reversible Computing
aliases: []
kind: technology
parent_concepts:
- compute
- non-conventional
related_concepts: []
sources:
- '[[2025-02-25-data-driven-vc-is-over]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 6
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
- slug: 2025-02-25-data-driven-vc-is-over
  title: data-driven VC is over
  date: '2025-02-25'
  kind: substack
- slug: 2024-10-22-state-of-the-future-part-deux
  title: 'An AI Thesis: State of the Future! Part Deux'
  date: '2024-10-22'
  kind: substack
neighbors: []
---
## Physics / mechanism

Landauer's principle sets a thermodynamic floor: erasing one bit dissipates at minimum kT·ln2 (~3×10⁻²¹ J at 300 K). Conventional CMOS discards logical state at every gate transition, burning ~100–1000× that floor. Reversible computing preserves logical state through bijective operations—inputs recoverable from outputs—so entropy doesn't increase and, in principle, energy can be recaptured. Implementations span adiabatic CMOS (charge recycled via resonant LC tanks, ~10–50% energy reduction demonstrated), quantum computing (inherently unitary/reversible gates), and ballistic/mechanical proposals. Practical adiabatic circuits operate at lower clock frequencies (MHz range vs. GHz) to allow quasi-static switching; the energy-delay product often fails to beat optimized conventional CMOS below ~10 nm nodes. No commercial silicon product ships as "reversible" today; best demonstrated systems are research-grade ASICs and FPGA overlays.

## Competitive landscape

Adiabatic CMOS is the nearest practical path but competes directly with standard low-power design techniques—clock gating, power gating, near-threshold voltage operation—which achieve 10–100× dynamic power reduction without frequency penalties. Neuromorphic architectures (Intel Loihi, IBM NorthPole) attack the same energy-per-inference metric via sparsity rather than reversibility. Cryogenic RSFQ (rapid single-flux-quantum) logic is reversible-adjacent and achieves ~10⁻¹⁹ J/op but requires 4 K operation.

| Approach | Energy/op | Temperature | Maturity |
|---|---|---|---|
| Adiabatic CMOS | ~fJ–pJ | 300 K | Research/demo |
| RSFQ / cryo | ~aJ–fJ | 4 K | Early commercial |
| Near-threshold CMOS | ~fJ | 300 K | Production |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
