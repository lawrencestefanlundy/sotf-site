---
type: concept
slug: 22fdx
canonical_name: 22fdx
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2024-yole-emerging-memories-2024]]'
- '[[2026-06-22-beyond-cmos-device-layer-research]]'
- '[[2025-26-lapedus-next-gen-ferroelectric-memory]]'
- '[[2026-06-04-globalfoundries-emram-22fdx-availability]]'
- '[[2026-06-15-gf-investor-day-2026]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 28
frontier:
- Does any named third-party customer ship a 22FDX FeFET or 22FDX FeRAM product in volume by end-2027, as the Yole 2024 trajectory implies 2024 yole emerging memories 2024, or does the mid-2026 "no design wins" finding hold 2025 26 lapedus next gen ferroelectric memory?
- What are the published endurance and retention specifications of the GF/Fraunhofer 22FDX 1T1C FeRAM, and how do they compare with the roughly 10^12 cycles reported for TSMC and Samsung FeFET demonstrators?
- Has GF ReRAM on 22FDX been qualified for production, with disclosed macro sizes and retention specs, and has the announced roll-out to FinFET and BCD platforms produced a released PDK?
- What share of 22FDX wafer revenue is attributable to eNVM-bearing designs, and does GF disclose it against the 2028 targets in the Investor Day 2026 deck 2026 06 15 gf investor day 2026?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-26-lapedus-next-gen-ferroelectric-memory
  title: Next-Gen Ferroelectric Memory Still A Work In Progress
  date: '2026-06-23'
  kind: web
- slug: 2026-06-22-beyond-cmos-device-layer-research
  title: Beyond-CMOS device layer — grounded research (MRAM/FeFET beachhead + capture base rate)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-06-04-globalfoundries-emram-22fdx-availability
  title: GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform
  date: '2026-06-04'
  kind: web
- slug: 2024-yole-emerging-memories-2024
  title: Yole Group — Emerging Non-Volatile Memories 2024
  date: '2024-10-15'
  kind: web
neighbors: []
---
## Physics / mechanism

22FDX is GlobalFoundries' 22nm fully-depleted silicon-on-insulator (FD-SOI) platform. The transistor channel sits in a thin undoped silicon layer over a buried oxide, so the channel is fully depleted in operation without the fin geometry used by FinFET nodes. GlobalFoundries positions the platform within a "feature-rich, not node-leading" specialty-foundry strategy rather than as a density-scaling node <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>.

The distinguishing feature for system designers is the embedded non-volatile memory (eNVM) portfolio built on top of the platform. Embedded MRAM is a productised offering on 22FDX: spin-transfer-torque MRAM with a perpendicular magnetic tunnel junction, technology licensed from Everspin, available as custom macros from 2 Mb to 32 Mb, surviving 260 °C solder reflow and specified for more than 10 years retention at 125 °C <sup class="ref"><a href="https://www.design-reuse.com/news/3730-globalfoundries-announces-availability-of-embedded-mram-on-leading-22fdx-fd-soi-platform/" title="GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform" rel="noopener">ref</a></sup>. The macro is a binary bit-cell optimised for bistable switching, retention and endurance, and is positioned as a replacement for flash and SRAM in code and working-memory roles <sup class="ref"><a href="https://www.design-reuse.com/news/3730-globalfoundries-announces-availability-of-embedded-mram-on-leading-22fdx-fd-soi-platform/" title="GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform" rel="noopener">ref</a></sup>. eMRAM on 22FDX entered production in February 2020, built in Dresden.

The pull toward eNVM on this platform comes from the embedded flash scaling wall. 28/22nm is the last node for embedded flash, which requires 6 to 8 extra masks against roughly 3 for MRAM; the constraint is mask-count economics rather than pure physics, and it is the stated reason foundries and IDMs are moving to MRAM, RRAM and FeRAM. GlobalFoundries' public eNVM portfolio spans eMRAM, ReRAM and flash across FDX, FinFET, BCD and other platforms, with the offering framed around always-on, offline-inference-capable IoT edge devices requiring deterministic wake-up and low latency <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>.

Ferroelectric work on 22FDX is a second track. GlobalFoundries and Fraunhofer have integrated a 1T1C FeRAM at 22FDX with sub-1V operation at 8 nm film thickness and stable retention at 150 °C; this is capacitor-based FeRAM rather than FeFET **2025 26 Lapedus Next Gen Ferroelectric Memory**. Yole's 2024 emerging-memory report tracks a 22FDX FeFET trajectory from sample grade toward volume customer adoption in 2026 to 2027 **2024 Yole Emerging Memories 2024**, a timeline that sits in tension with survey evidence of no high-volume production and no reported ferroelectric design wins as of mid-2026 **2025 26 Lapedus Next Gen Ferroelectric Memory**.

## Competitive landscape

| Platform | eNVM status |
|---|---|
| GF 22FDX (22nm FD-SOI) | eMRAM in production since Feb 2020, Dresden; ReRAM named as multi-platform offering with 22FDX as lead; 1T1C FeRAM integrated with Fraunhofer <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup> **2025 26 Lapedus Next Gen Ferroelectric Memory** |
| TSMC 22nm | eMRAM in volume production; 16nm qualifying, automotive 2025 |
| Samsung 28nm FD-SOI | eMRAM in mass production since 2019, quoted at roughly 1000x faster and 1/400 write energy versus its eFlash |
| Embedded flash at ≥40nm | Retains more than 50% of embedded NV units via 3D stacking; 28/22nm is the last flash node **2024 Yole Emerging Memories 2024** |

22FDX therefore competes not on gate density but on the combination of FD-SOI body biasing economics and a qualified eNVM menu at a node where embedded flash has run out. Its nearest direct rival on the FD-SOI axis is Samsung's 28nm FD-SOI eMRAM, which reached mass production earlier. Against TSMC's 22nm eMRAM the differentiation is platform breadth rather than memory technology, since both are MRAM-based. On the ferroelectric axis, TSMC and Samsung device demonstrations report higher measured endurance (both around 10^12 cycles) than the productised GF/Fraunhofer FeRAM disclosures, but TSMC's FeFET is not offered as a foundry service to third parties **2025 26 Lapedus Next Gen Ferroelectric Memory**.

## Evidence base

- eMRAM on 22FDX entered production in February 2020 at Dresden; GF's original announcement dates to 20 September 2017 with a production-ready relaunch in March 2020 <sup class="ref"><a href="https://www.design-reuse.com/news/3730-globalfoundries-announces-availability-of-embedded-mram-on-leading-22fdx-fd-soi-platform/" title="GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform" rel="noopener">ref</a></sup>.
- The 22FDX eMRAM is STT-MRAM with a perpendicular MTJ licensed from Everspin, offered as 2 Mb to 32 Mb custom macros, surviving 260 °C solder reflow with more than 10-year retention at 125 °C <sup class="ref"><a href="https://www.design-reuse.com/news/3730-globalfoundries-announces-availability-of-embedded-mram-on-leading-22fdx-fd-soi-platform/" title="GLOBALFOUNDRIES Announces Availability of Embedded MRAM on Leading 22FDX FD-SOI Platform" rel="noopener">ref</a></sup>.
- 28/22nm is the last node for embedded flash: 6 to 8 extra masks versus roughly 3 for MRAM, an economic rather than physical limit.
- GF's Investor Day 2026 deck (101 slides, FY2025 financials, 2028 and long-term targets) names a "broad eNVM portfolio (eMRAM, ReRAM, FLASH) across FDX, FinFET, BCD, and more" <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>.
- GlobalFoundries and Fraunhofer integrated a 1T1C FeRAM at 22FDX with sub-1V operation at 8 nm film thickness and stable retention at 150 °C; the productised ferroelectric work is capacitor-based, not FeFET **2025 26 Lapedus Next Gen Ferroelectric Memory**.
- Yole's 2024 report projects GF 22FDX FeFET reaching volume customer adoption in 2026 to 2027, with FeFET plus HfO2-FeRAM rising from under 0.5% of embedded NV units in 2024 to at least 5% by 2030 **2024 Yole Emerging Memories 2024**.
- A mid-2026 survey of the ferroelectric-memory frontier reports sampling and R&D across the field with no high-volume production and no reported design wins **2025 26 Lapedus Next Gen Ferroelectric Memory**.

## Frontier (open questions)

- Does any named third-party customer ship a 22FDX FeFET or 22FDX FeRAM product in volume by end-2027, as the Yole 2024 trajectory implies **2024 Yole Emerging Memories 2024**, or does the mid-2026 "no design wins" finding hold **2025 26 Lapedus Next Gen Ferroelectric Memory**?
- What are the published endurance and retention specifications of the GF/Fraunhofer 22FDX 1T1C FeRAM, and how do they compare with the roughly 10^12 cycles reported for TSMC and Samsung FeFET demonstrators?
- Has GF ReRAM on 22FDX been qualified for production, with disclosed macro sizes and retention specs, and has the announced roll-out to FinFET and BCD platforms produced a released PDK?
- What share of 22FDX wafer revenue is attributable to eNVM-bearing designs, and does GF disclose it against the 2028 targets in the Investor Day 2026 deck <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>?

*Synthesised 2026-08-31 from 5 KB sources by the resynth pipeline; citations are KB source slugs.*
