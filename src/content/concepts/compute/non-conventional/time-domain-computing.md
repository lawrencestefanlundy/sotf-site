---
type: concept
slug: time-domain-computing
canonical_name: Time-Domain Computing
aliases:
- time-domain compute
- temporal compute
- unary computing
- race logic
- pulse-interval encoding
kind: technology
parent_concepts:
- compute-paradigms
related_concepts:
- logic
- conventional-logic
- beyond-cmos-logic
- compute-in-memory
sources: []
frontier:
- Has any time-domain design shown measured throughput per mm² competitive with a digital accelerator on a real inference workload, rather than on a dot product?
- Does the mature-node claim survive contact with a full chip — i.e. is the area saved by unary arithmetic given back in time, latency, or conversion circuitry?
- What does a software toolchain for a time-domain substrate actually look like, and has anything real been ported to one?
last_updated: '2026-07-27'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: logic
  name: Compute & Logic
  path: /compute/conventional-logic/logic/
  macro: compute
- slug: conventional-logic
  name: Conventional Logic
  path: /compute/conventional-logic/conventional-logic/
  macro: compute
- slug: beyond-cmos-logic
  name: Beyond Cmos Logic
  path: /compute/non-conventional/beyond-cmos-logic/
  macro: compute
- slug: compute-in-memory
  name: Compute in Memory
  path: /compute/non-conventional/compute-in-memory/
  macro: compute
---
Computing where the **value of a datum is the length of a time interval** — typically the delay between two pulses — rather than a voltage level interpreted as a binary digit. Arithmetic is done by delaying, racing and combining edges. The family includes race logic, unary and stochastic computing, and pulse-interval encoding.

## Why anyone bothers
The pitch is always the same trade: a time-encoded operation needs far fewer transistors than its binary equivalent, because the "computation" is largely propagation rather than switching. That buys three claimed advantages:

1. **Transistor-count and energy reduction** per operation — less switching activity, so lower power per useful operation.
2. **Node independence** — if computation depends on propagation time rather than density, performance does not require sub-5nm nodes. This is the sovereignty and cost angle: mature-node fabs, shorter qualification cycles, a much larger addressable foundry base.
3. **Memory pressure relief** — schemes that operate directly on compressed representations claim large reductions in intermediate memory traffic, which is where inference actually spends its energy.

## Why it stays niche
Time is a serial resource. Classical unary and stochastic schemes buy area by spending latency, and the cost grows with operand dynamic range, so a scheme that looks brilliant on a dot product can lose badly on a full workload. Conversion between time-encoded and conventional domains is not free. And the software problem is severe: an architecture with no toolchain is a research result, not a product — the **Compute Specialisation Equilibrium** thesis holds that the binding brake on new silicon is mask/NRE capital and workload churn, not porting labour, but a substrate this unusual pays both.

## Evaluation test
The claim to interrogate is never the ratio, it is the baseline and the workload. A transistor-count or memory-reduction number quoted against "a GPU" on a dot product tells you almost nothing about throughput per mm² per watt on real inference. Ask for the node, the die, the precision, the baseline part, and which figures are measured on silicon rather than simulated.
