---
type: concept
slug: charge-domain-compute
canonical_name: Charge-Domain Compute
aliases:
- charge-based compute
- capacitive compute
- switched-capacitor compute
kind: technology
parent_concepts:
- analog-computing
- in-memory-computing
related_concepts:
- memcapacitor
- sram-cim
- adc-bottleneck
- analog-computing
sources:
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
frontier:
- Does charge-domain's noise/linearity advantage over current-domain hold at scaled nodes and across temperature, or does it need compensation circuitry that eats the energy win?
- Does the ADC still dominate energy even when the multiply itself is near-free in the charge domain — i.e. does charge-domain move the bottleneck rather than remove it?
last_updated: '2026-06-14'
tags:
- concept
- analog-computing
- in-memory-compute
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
- slug: sram-cim
  name: SRAM Compute-in-Memory
  path: /sotf-site/memory/emerging-memory/sram-cim/
  macro: memory
- slug: adc-bottleneck
  name: ADC Bottleneck (analog in-memory compute)
  path: /sotf-site/compute/compute-architecture/adc-bottleneck/
  macro: compute
- slug: analog-computing
  name: Analog Computing
  path: /sotf-site/compute/non-conventional/analog-computing/
  macro: compute
---
## Current-domain vs charge-domain

In **current-domain** analog CIM, weights are stored as conductances (resistances) in a crossbar; applying input voltages produces currents that sum on a wire (Ohm's law + Kirchhoff's law = analog MAC). The problem: the devices draw continuous static current, conductance is hard to set precisely and drifts, and device-to-device variability injects noise. RRAM, PCM, and floating-gate flash (Mythic) all live here, and all fought variability and endurance.

## Two implementations

Both share the charge-domain advantage (precision, linearity, low static power); they differ on the storage element (dedicated non-volatile device vs standard volatile SRAM) and therefore on density and process complexity.

## The catch

Charge-domain makes the *multiply* nearly free, but the result still has to be read out of the analog domain into digital — and the analog-to-digital converters do not get cheaper just because the MAC moved to the charge domain. The [ADC Bottleneck (analog in-memory compute)](/sotf-site/compute/compute-architecture/adc-bottleneck/) is the binding constraint on all analog CIM, charge-domain included. Charge-domain moves the energy bottleneck from the array to the periphery; whether it *removes* it at scale is the open question.
