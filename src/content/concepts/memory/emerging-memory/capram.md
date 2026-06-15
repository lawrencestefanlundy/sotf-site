---
type: concept
slug: capram
canonical_name: CapRAM (SEMRON)
aliases:
- capram
- sempacitor
kind: technology
parent_concepts:
- memcapacitor
- in-memory-computing
related_concepts:
- memcapacitor
- charge-domain-compute
- 3d-monolithic-integration
- adc-bottleneck
sources:
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
frontier:
- Does CapRAM reach a product-grade test chip (named partner) or a Series A by mid-2027 — the near-dated checkpoint in the SEMRON thesis?
- Is the 20× chip-level energy claim a full-chip (ADC-inclusive) number or array-only?
- Does the CapRAM weight-write mechanism hold retention/endurance at the standard-CMOS interface, or drift like floating-gate flash?
last_updated: '2026-06-14'
tags:
- concept
- semron
- memcapacitor
- product-brand
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /sotf-site/compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: 3d-monolithic-integration
  name: 3D Monolithic Integration
  path: /sotf-site/compute/compute-architecture/3d-monolithic-integration/
  macro: compute
- slug: adc-bottleneck
  name: ADC Bottleneck (analog in-memory compute)
  path: /sotf-site/compute/compute-architecture/adc-bottleneck/
  macro: compute
---
## What it is

CapRAM computes a multiply-accumulate using a **variable capacitor** rather than a resistor or transistor. The weight is stored as a programmable capacitance; applying an input modulates charge; charge accumulates to produce the analog MAC result. Because the mechanism is capacitive (see [Charge-Domain Compute](/sotf-site/compute/non-conventional/charge-domain-compute/)):

- it draws **near-zero static current** (no continuous current path like resistive RRAM/PCM), the root of the ~20× chip-level energy-efficiency claim;
- capacitance is set by geometry, so it is **precise, linear, and temperature-stable** relative to resistive analog;
- the devices are **non-volatile** and **stack vertically** via [3D Monolithic Integration](/sotf-site/compute/compute-architecture/3d-monolithic-integration/), so compute density scales by adding layers rather than by buying leading-edge lithography.

## Scientific lineage

## Status