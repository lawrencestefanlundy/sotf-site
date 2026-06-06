---
type: concept
slug: memory
canonical_name: Memory
aliases: []
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources:
- '[[2023-09-18-e15-in-conversation-with-wisear-on]]'
- '[[2025-09-23-the-compute-gradient]]'
- '[[2025-08-12-ai-and-junior-white-collar-automation]]'
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2025-04-23-what-if-ai-can-already-feel]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2023-05-24-launching-state-of-the-future]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2023-06-30-e06-the-model-t-moment-for-bits-llms]]'
- '[[2023-05-25-interview-ben-mildenhall-co-inventor]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-10-13-e19-trusted-execution-environments]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-02-25-data-driven-vc-is-over]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 451
descendants:
- agentic-workload-retrieval
- computational-storage
- cxl
- dram
- embedded-non-volatile-memory
- feram
- hbm
- in-memory-computing
- memcapacitor
- memory
- mram
- nand-flash
- pcm-phase-change-memory
- photonic-memory
- rram-reram
- sram
- storage-class-memory
last_reorg_date: '2026-05-14'
sources_7d: 4
sources_30d: 9
recent_mentions:
- slug: 2026-06-04-q-memory-site
  title: Q-Memory — company website (q-memory.tech)
  date: '2026-06-04'
  kind: web
- slug: 2026-06-04-tmr-sensors-sub-pt-detectivity-biomagnetic-review
  title: Tunnel-magnetoresistance sensors with sub-pT detectivity for detecting bio-magnetic fields
  date: '2026-06-04'
  kind: web
- slug: 2026-06-04-globalfoundries-emram-22fdx-availability
  title: GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform
  date: '2026-06-04'
  kind: web
- slug: 2026-06-03-tendrils-compute
  title: Tendrils Compute — company site (about / background / jobs)
  date: '2026-06-03'
  kind: web
- slug: 2026-06-02-agentic-runtime-silicon-necessity
  title: Deep-research dossier — does the stateful agent runtime / control-plane layer need a novel silicon primitive?
  date: '2026-06-02'
  kind: web
- slug: 2026-06-01-hbm-state-of-play
  title: HBM state of play (mid-2026) — technology, supercycle, three-supplier standing
  date: '2026-06-01'
  kind: web
- slug: 2026-06-01-ncsc-nsa-qkd-vs-pqc
  title: 'NCSC / NSA position: QKD not endorsed, post-quantum cryptography is the recommended mitigation'
  date: '2026-06-01'
  kind: web
- slug: 2026-05-30-osat-market-structure
  title: OSAT market structure 2024-2025 — rankings, advanced-packaging split, photonic assembly
  date: '2026-05-30'
  kind: web
neighbors: []
---
## Physics / mechanism

Memory stores binary state via a physical mechanism that can be written, held, and read non-destructively. DRAM uses capacitor charge (leaks, needs refresh every ~64 ms, ~10 ns latency, ~50 fJ/bit). SRAM uses cross-coupled inverters (faster, ~1 ns, ~1 pJ/bit, no refresh, large cell area). NAND flash exploits floating-gate or charge-trap transistor threshold-voltage shift (non-volatile, ~100 µs program, ~100K erase cycles). Emerging NVM candidates — MRAM, RRAM, PCM, FeRAM — target the gap: non-volatile + byte-addressable + sub-100 ns write. MRAM (STT or SOT) is closest to production at scale; GlobalFoundries offers embedded MRAM (eMRAM) on 22FDX.

## Competitive landscape

DRAM and NAND dominate by volume (Samsung, SK Hynix, Micron). SRAM is embedded in logic; no standalone market. The contested space is storage-class memory and embedded NVM for edge AI / IoT. PCM (Intel Optane, now discontinued) showed the latency-density trade-off is hard to commercialise. FeRAM (Infineon, TI) wins in ultra-low-power write cycles. RRAM competes on process simplicity. The real battle is embedded NVM for MCUs and neuromorphic inference accelerators.

| Type | Latency | Non-volatile | Endurance |
|------|---------|--------------|-----------|
| SRAM | ~1 ns | No | Unlimited |
| eMRAM | ~10 ns | Yes | 10⁸ cycles |
| FeRAM | ~50 ns | Yes | 10¹⁴ cycles |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
