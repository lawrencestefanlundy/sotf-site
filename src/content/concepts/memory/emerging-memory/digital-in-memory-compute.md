---
type: concept
slug: digital-in-memory-compute
canonical_name: Digital In-Memory Compute
aliases:
- digital in-memory computing
- digital compute-in-memory
- D-IMC
- digital CIM
parent_concepts:
- in-memory-computing
related_concepts:
- analog-in-memory-compute
- sram-cim
- adc-bottleneck
- processing-in-memory
- von-neumann-bottleneck
sources: []
frontier:
- Does "digital IMC plus 3D stacking" close the energy gap to analog before analog scales out of the edge?
last_updated: '2026-06-16'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: analog-in-memory-compute
  name: Analog In-Memory Compute
  path: /sotf-site/memory/emerging-memory/analog-in-memory-compute/
  macro: memory
- slug: sram-cim
  name: SRAM Compute-in-Memory
  path: /sotf-site/memory/emerging-memory/sram-cim/
  macro: memory
- slug: adc-bottleneck
  name: ADC Bottleneck (analog in-memory compute)
  path: /sotf-site/compute/compute-architecture/adc-bottleneck/
  macro: compute
- slug: processing-in-memory
  name: Processing-in-Memory (PIM)
  path: /sotf-site/memory/emerging-memory/processing-in-memory/
  macro: memory
- slug: von-neumann-bottleneck
  name: Von Neumann Bottleneck
  path: /sotf-site/compute/compute-architecture/von-neumann-bottleneck/
  macro: compute
---
Compute-in-memory that keeps the multiply-accumulate digital, performed by logic embedded in or tightly bound to the SRAM array rather than by analog summation. Because there is no analog step, it sidesteps the [ADC Bottleneck (analog in-memory compute)](/sotf-site/compute/compute-architecture/adc-bottleneck/) and the precision, variability and drift problems of [Analog In-Memory Compute](/sotf-site/memory/emerging-memory/analog-in-memory-compute/).

## The tradeoff

Digital IMC is production-ready and foundry-compatible (standard SRAM plus logic), with full numerical precision and deterministic behaviour. The price is that it is still bound by the CMOS energy floor, so its efficiency ceiling is lower than analog. It trades peak TOPS/W for manufacturability. This is the scalable, lower-risk cut of in-memory compute, and the one most likely to ship at volume first.

## Cluster members

## Cluster role

*Hand-authored synthesis, 16 June 2026.*

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
