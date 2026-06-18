---
type: concept
slug: analog-in-memory-compute
canonical_name: Analog In-Memory Compute
aliases:
- analog in-memory computing
- analog compute-in-memory
- analog CIM
- AIMC
parent_concepts:
- in-memory-computing
related_concepts:
- charge-domain-compute
- sram-cim
- adc-bottleneck
- memcapacitor
- rram-reram
- digital-in-memory-compute
- von-neumann-bottleneck
- memory-wall
sources: []
frontier:
- Does any analog CIM chip reach credible datacentre production (not edge) before end-2029?
- Does the ADC tax fall fast enough to keep analog ahead of digital IMC on system-level energy?
last_updated: '2026-06-16'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-16-cim-landscape-2026
  title: 'Compute-in-memory landscape 2026: efficiency claims, the digital-readout shift, IDM PIM'
  date: '2026-06-16'
  kind: web
neighbors:
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /sotf-site/compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: sram-cim
  name: SRAM Compute-in-Memory
  path: /sotf-site/memory/emerging-memory/sram-cim/
  macro: memory
- slug: adc-bottleneck
  name: ADC Bottleneck (analog in-memory compute)
  path: /sotf-site/compute/compute-architecture/adc-bottleneck/
  macro: compute
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
- slug: rram-reram
  name: RRAM / ReRAM
  path: /sotf-site/memory/emerging-memory/rram-reram/
  macro: memory
- slug: digital-in-memory-compute
  name: Digital In-Memory Compute
  path: /sotf-site/memory/emerging-memory/digital-in-memory-compute/
  macro: memory
- slug: von-neumann-bottleneck
  name: Von Neumann Bottleneck
  path: /sotf-site/compute/compute-architecture/von-neumann-bottleneck/
  macro: compute
- slug: memory-wall
  name: The Memory Wall
  path: /sotf-site/compute/compute-architecture/memory-wall/
  macro: compute
---
Compute-in-memory where the multiply-accumulate is done by analog physics inside the memory array, not by digital logic. The array holds the weights; apply the inputs as voltages or charges and read the summed current or charge, and the matrix-vector multiply happens in one physical step (Ohm and Kirchhoff for resistive devices, charge-sharing for capacitive).

## The energy ceiling, and its tax

Analog AIMC offers the highest theoretical efficiency (100+ TOPS/W claimed) because it collapses the [Von Neumann Bottleneck](/sotf-site/compute/compute-architecture/von-neumann-bottleneck/): no weight movement, the MAC happens in place. The catch is the [ADC Bottleneck (analog in-memory compute)](/sotf-site/compute/compute-architecture/adc-bottleneck/) (every analog result must be digitised, and the converters dominate area and power), plus limited effective precision (~4 to 6 bit), device variability, and conductance or charge drift. Those are the reasons analog CIM has stayed edge-bound through roughly 2029 (see **Hbm Free Inference Architectures**).

## Sub-families

Contrast [Digital In-Memory Compute](/sotf-site/memory/emerging-memory/digital-in-memory-compute/) (digital MAC, no ADC tax, lower ceiling, production-ready).

## Cluster role

*Hand-authored synthesis, 16 June 2026.*

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
