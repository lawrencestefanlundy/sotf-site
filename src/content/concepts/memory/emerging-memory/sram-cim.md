---
type: concept
slug: sram-cim
canonical_name: SRAM Compute-in-Memory
aliases:
- sram-compute-in-memory
- sram-in-memory-compute
- digital-sram-cim
kind: technology
parent_concepts:
- in-memory-computing
- memory
related_concepts:
- charge-domain-compute
- memcapacitor
- adc-bottleneck
- sram
sources: []
frontier:
- Does SRAM's density disadvantage (large 6T/8T bitcell, volatile) cap model size on-die enough that it loses the datacentre-decode socket to denser non-volatile devices?
- Analog SRAM-CIM (EnCharge, charge-domain) vs digital SRAM-CIM (Fractile-style) — which wins, and does the ADC bottleneck decide it?
- Does keeping the whole model in SRAM (Fractile's DRAM-less pitch) actually pencil out at frontier model sizes, or only for smaller models?
last_updated: '2026-06-14'
tags:
- concept
- in-memory-compute
- sram
mention_count: 1
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: charge-domain-compute
  name: Charge-Domain Compute
  path: /compute/non-conventional/charge-domain-compute/
  macro: compute
- slug: memcapacitor
  name: Memcapacitor
  path: /memory/emerging-memory/memcapacitor/
  macro: memory
- slug: adc-bottleneck
  name: ADC Bottleneck (analog in-memory compute)
  path: /compute/compute-architecture/adc-bottleneck/
  macro: compute
- slug: sram
  name: SRAM
  path: /memory/mainstream-memory/sram/
  macro: memory
---
## Why SRAM

The cost is **density and volatility**:

- An SRAM bitcell (6T, sometimes 8T/10T for CIM) is large compared with a 1T1R RRAM cell or a stacked memcapacitor. So SRAM-CIM stores fewer weights per mm².
- SRAM is **volatile** — it loses state on power-off and burns standby leakage to hold weights. For always-on edge inference that is a real penalty; for plugged-in datacentre decode it matters less.

## Analog vs digital SRAM-CIM

## Where it sits against memcapacitor

SRAM-CIM and memcapacitor are the two charge-friendly CIM bets, and they trade off cleanly:

The honest read: SRAM-CIM is the safer, better-funded path to volume; memcapacitor is the higher-ceiling, higher-risk path that wins only if 3D monolithic growth yields. See **Memcapacitor Compute Memory Bound Ai** for the device-class survival question.
