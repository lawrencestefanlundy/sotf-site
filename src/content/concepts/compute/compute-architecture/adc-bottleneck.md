---
type: concept
slug: adc-bottleneck
canonical_name: ADC Bottleneck (analog in-memory compute)
aliases:
- adc-overhead
- analog-to-digital-bottleneck
kind: concept
parent_concepts:
- in-memory-computing
- analog-computing
related_concepts:
- charge-domain-compute
- sram-cim
- memcapacitor
sources:
- '[[2024-yole-emerging-memories-2024]]'
frontier:
- Does any analog-CIM vendor publish a full-chip (not array-only) TOPS/W that holds up once ADC + DAC + SRAM buffering are counted? This is the number to demand before believing a 20× claim.
- Does charge-domain + clever ADC sharing / time-multiplexing get the ADC below ~50% of array energy at production precision (8-bit), or does it stay the dominant cost?
- Does the move to lower precision (4-bit, ternary) shrink the ADC enough to change the economics, and do models tolerate it?
last_updated: '2026-06-14'
tags:
- concept
- analog-computing
- in-memory-compute
- counter-thesis
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
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
---
## The mechanism

Analog CIM does the multiply-accumulate (MAC) inside the memory array, in the analog domain — that part is genuinely cheap (see [Charge-Domain Compute](/sotf-site/compute/non-conventional/charge-domain-compute/)). But the analog result has to be converted back to digital before it can be used by the next layer, accumulated, or moved. That conversion is done by **analog-to-digital converters (ADCs)** at the periphery of each array column, plus **digital-to-analog converters (DACs)** to drive inputs in.

ADCs are expensive in exactly the dimensions analog CIM is trying to win:

- **Energy.** A precise ADC can consume more energy per conversion than the entire analog MAC it is reading. Across a large array, ADCs routinely account for the majority (often cited as 50–90%) of total tile energy.
- **Area.** ADCs are large relative to bitcells, so they cap how much of the die is actually compute.
- **Precision scaling.** ADC cost grows steeply with bit-precision (~2× energy per extra bit). Getting to 8-bit-equivalent accuracy — which most production models need — is where the cost explodes.

## Why it is the load-bearing risk

## How the leaders address it

## The test to apply

Before accepting any analog-CIM efficiency claim: demand a **full-chip, ADC-inclusive, 8-bit (or stated-precision) TOPS/W**, ideally third-party measured. If a vendor only quotes array-level numbers, the ADC bottleneck has not been answered.
