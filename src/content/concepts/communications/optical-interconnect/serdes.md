---
type: concept
slug: serdes
canonical_name: Serdes
aliases: []
parent_concepts:
- optical-interconnect
- communications
related_concepts: []
sources:
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2026-07-28-laser-on-a-chip-w-matt-crowley-scintil]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2026-07-31-etched-research-sprint]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 14
frontier:
- Has the reported MediaTek 336G SerDes win on Google TPU v9 been confirmed by either party, and at what lane count and aggregate bandwidth does the shipped interface run?
- What is the measured energy per bit and reach (package, board, cable) of 336G-class electrical SerDes, and at what distance does it lose to optical interconnect?
- Do learned surrogates such as Mach42's reproduce SerDes-relevant behaviour (jitter, eye closure, long-tail transient response) to silicon-correlated accuracy, or only on smoother analogue blocks?
- Which merchant SerDes vendors are qualified at 300G-plus per lane on leading-edge nodes, and what is the resulting concentration risk for custom accelerator programmes?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-31-etched-research-sprint
  title: Etched research sprint — tape-out speed, HBM supply, customer orders (4-lane web sweep)
  date: '2026-07-31'
  kind: web
- slug: 2026-07-28-laser-on-a-chip-w-matt-crowley-scintil
  title: Laser on a Chip w/ Matt Crowley @ Scintil Photonics
  date: '2026-07-28'
  kind: substack
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
neighbors: []
---
## Physics / mechanism

A SerDes (serialiser/deserialiser) is the mixed-signal circuit block that converts a wide, slow parallel bus inside a chip into a small number of very high-rate serial lanes for transmission off-die, and reverses the conversion at the receiver. It is the electrical layer that sits underneath chip-to-chip, package-to-package and rack-scale interconnect standards, and in optical links it is the block that drives and recovers data from the electro-optical front end.

The headline parameter is per-lane signalling rate, quoted in Gb/s. MediaTek's offer to Google for TPU v9 was reported as a 336G SerDes solution, i.e. a per-lane rate of 336 Gb/s <sup class="ref"><a href="https://www.semidoped.com/p/daily-update-june-23rd-2026" title="Semi Doped — Daily Update, June 23rd 2026" rel="noopener">ref</a></sup>. Aggregate interface bandwidth is the lane rate multiplied by lane count; the same report describes MediaTek design wins framed at 2.4T, the aggregate scale at which accelerator interconnect is now specified <sup class="ref"><a href="https://www.semidoped.com/p/daily-update-june-23rd-2026" title="Semi Doped — Daily Update, June 23rd 2026" rel="noopener">ref</a></sup>.

## Competitive landscape

The sources support only a narrow view: SerDes as merchant IP supplied into custom accelerator programmes, where winning the interface block is a route into a large ASIC design win. MediaTek's 336G offering is presented as the lever that secured Google TPU v9 orders, implying competition is between IP vendors on lane rate and readiness rather than between architectures <sup class="ref"><a href="https://www.semidoped.com/p/daily-update-june-23rd-2026" title="Semi Doped — Daily Update, June 23rd 2026" rel="noopener">ref</a></sup>. No source here compares electrical SerDes against co-packaged optics or other optical-interconnect approaches, so the position of SerDes relative to those alternatives is not established by this evidence base.

## Evidence base

## Frontier (open questions)

*Synthesised 2026-08-31 from 5 KB sources by the resynth pipeline; citations are KB source slugs.*
