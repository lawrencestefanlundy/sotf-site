---
type: concept
slug: substrate-bt-abf
canonical_name: BT / ABF Substrates
aliases: []
kind: material
domain:
- cloudberry
- sotf
parent_concepts:
- manufacturing
- packaging
related_concepts: []
companies_using:
- ajinomoto-fine-techno
- ats-austria-technologie-systemtechnik
- averatek-corporation
- daeduck-electronics
- elite-material-co-emc
- ibiden-co-ltd
- kinsus-interconnect-technology
- kyocera-corporation
- lg-innotek
- mitsubishi-gas-chemical
- nan-ya-pcb
- nano-dimension
- samsung-electro-mechanics
- schweizer-electronic
- semco-simmonds-electronics
- shennan-circuits-scc
- shinko-electric-industries
- taiyo-ink-taiyo-holdings
- tripod-technology
- ttm-technologies
- unimicron-technology
- ventec-international-group
- zhen-ding-technology
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- material
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# BT / ABF Substrates

*Kind: material*

## Physics / mechanism

Buildup (BF) and Ajinomoto Buildup Film (ABF) substrates are organic laminate interposers sitting between a flip-chip die and the PCB. ABF is a thermoset epoxy-based dielectric film developed by Ajinomoto; it enables fine-pitch copper redistribution layers (RDL) via semi-additive processing (SAP). Key parameters: line/space currently 2 µm/2 µm in leading HVM (down from 10/10 µm circa 2015), layer count 8–20+ for advanced packages, CTE ~13–17 ppm/°C (mismatch with silicon ~2.3 ppm drives warpage engineering). Substrate core is typically BT (bismaleimide-triazine) resin reinforced with glass cloth — mechanically stiff, low-loss at RF. Total substrate stack: BT core + multiple ABF buildup layers. Dominant suppliers: Ibiden, Shinko, AT&S, Unimicron. Severe capacity constraints drove ~$10B capex cycle 2021–2024. HVM yield at 2 µm L/S remains below 90% at most fabs.

## Competitive landscape

ABF's principal competitor at finer pitches is glass core substrates (Corning, AGC) — better CTE match to silicon, lower loss tangent, but immature SAP ecosystem. Silicon interposers (TSMC CoWoS, Intel EMIB) offer <1 µm RDL but at 5–10× cost. Fan-out panel-level packaging (FOPLP) eliminates the substrate entirely but struggles with die placement accuracy at scale. Embedded die approaches (AT&S ECP) compress z-height. For RF/mmWave, LTCC and liquid crystal polymer (LCP) substrates compete on loss but not density.

## Cloudberry relevance

| Approach | L/S capability | Cost index | Maturity |
|---|---|---|---|
| ABF substrate | 2–5 µm | 1× | HVM |
| Glass core substrate | 1–2 µm | 1.5–2× | Pilot |
| Si interposer (CoWoS) | <1 µm | 5–10× | HVM (limited) |


ABF substrate supply is a systemic constraint on AI accelerator packaging — any portfolio company in chiplet integration, advanced packaging IP, or heterogeneous compute touches this bottleneck. Cloudberry/GF-LP angle: GF does not lead-edge logic but does advanced packaging; substrate alternatives (glass core, panel-level) are credible deep-tech bets with materials + process IP moats. Watch AT&S (European incumbent), startups attacking panel-scale SAP, and novel dielectric material plays reducing CTE mismatch — all fit the advanced-materials / photonics-adjacent thesis where Cloudberry has conviction.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
