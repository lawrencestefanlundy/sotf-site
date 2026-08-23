---
type: concept
slug: nand-flash
canonical_name: NAND Flash
aliases:
- 3D NAND
- BiCS
- V-NAND
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources:
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-04-08-tech-inflation-silicon-shock-gartner-forecasts-worldwide]]'
- '[[2026-07-03-tech-inflation-silicon-shock-ai-server-demand-continues-to]]'
- '[[2026-07-07-high-bandwidth-flash-the-full-report]]'
- '[[2026-01-13-semianalysis-interconnects-beyond-copper]]'
- '[[2026-04-15-semianalysis-isscc-2026]]'
frontier:
- Does the $/bit/layer curve keep bending far enough to keep 3D NAND ahead of QLC-DRAM and emerging NVM?
- Does a startup (e.g. SEMRON) ever ride the 3D-NAND cost curve for compute, or is it structurally an incumbent-only learning curve?
last_updated: '2026-07-07'
tags:
- concept
- technology
mention_count: 48
last_reorg_date: '2026-05-14'
sources_7d: 1
sources_30d: 11
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-10-inference-silicon-deep-research
  title: 'Deep research: measured vs claimed inference-silicon economics (adversarially verified, 23/25 claims confirmed)'
  date: '2026-07-10'
  kind: web
- slug: 2026-07-07-high-bandwidth-flash-the-full-report
  title: 'High Bandwidth Flash: The Full Report'
  date: '2026-07-07'
  kind: web
- slug: 2026-07-03-tech-inflation-silicon-shock-ai-server-demand-continues-to
  title: AI Server Demand Continues to Support Memory Prices in 3Q26, but Gains Moderate as Consumer Demand Weakens and High Base Effects Take Hold
  date: '2026-07-03'
  kind: web
- slug: 2026-04-15-semianalysis-isscc-2026
  title: 'ISSCC 2026: NVIDIA & Broadcom CPO, HBM4 & LPDDR6, TSMC Active LSI, Logic-Based SRAM, UCIe-S and More'
  date: '2026-04-15'
  kind: web
- slug: 2026-04-08-tech-inflation-silicon-shock-gartner-forecasts-worldwide
  title: Gartner Forecasts Worldwide Semiconductor Revenue to Exceed $1.3 Trillion in 2026
  date: '2026-04-08'
  kind: web
- slug: 2026-01-13-semianalysis-interconnects-beyond-copper
  title: Interconnects Beyond Copper, 1,000 CFETs, SK Hynix Next-Gen NAND, 2D Materials, and More
  date: '2026-01-13'
  kind: web
- slug: 2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth
  title: '🔮E14: The Real AI Bottleneck: High Bandwidth Memory (HBM)'
  date: '2023-09-08'
  kind: substack
neighbors: []
---
## Physics / mechanism

NAND flash stores data as charge in floating-gate or charge-trap transistors stacked in 3D arrays (3D NAND). Each cell holds 1–4 bits (SLC/MLC/TLC/QLC) by controlling discrete threshold-voltage states. Tunneling oxide thickness (~7–10 nm) governs endurance (P/E cycles: SLC ~100k, QLC ~1k) and retention (10-year spec at 40°C). Leading-edge nodes stack 200–300+ layers (Samsung V-NAND, SK Hynix, Micron). Raw bit density exceeds 10 Tb/in². Controllers manage ECC, wear-leveling, and FTL. Interface: NVMe/PCIe Gen5 for enterprise SSDs, pushing sequential read >14 GB/s at sub-20 µs latency.

## Competitive landscape

NAND competes directly with NOR flash (lower density, byte-addressable, dominates code storage / MCU boot), DRAM (volatile, 10× faster, 10× costlier/bit), and emerging non-volatile memories targeting the gap between them.

## Adjacent memory technologies

| Technology | Density | Endurance | Latency |
|---|---|---|---|
| 3D NAND (QLC) | Very high | ~1k P/E | ~100 µs |
| NOR Flash | Low | ~100k P/E | ~100 ns (read) |
| MRAM / PCM / RRAM | Mid | 10⁶–10⁸ | ~100 ns–1 µs |

Adjacent pressure comes from CXL-attached DRAM tiers blurring the storage/memory boundary, and from computational storage (processing-in-flash) reducing data-movement penalties.

## The four-maker structure + AI supercycle (2026)

NAND is a **5–6 player oligopoly** (looser than the 3-player DRAM/HBM club): Samsung (~29%), SK Hynix (incl. Solidigm), and the ****Kioxia** + **Sandisk** bloc** (~30% combined, produced jointly through **Flash Ventures** at Yokkaichi + Kitakami, aligned to 2034), plus Micron and China's YMTC. Do not confuse NAND with HDD: **Western Digital** and **Seagate** are hard-disk-drive makers, not NAND, though they ride the same AI-storage supercycle as the cheapest bulk medium.

The technology race is **vertical layer count**: 3D NAND stacks charge-trap cells in a monolithic column, and density scales by adding layers (string-stacked decks), not by shrinking in-plane. BiCS / V-NAND have moved 218 → **300+ layers** (Kioxia/Sandisk 10th-gen sample-shipping Jul 2026), with nanoimprint patterning (Canon NIL, via Kioxia) as a cheaper-than-EUV path. The metric that matters is **$/bit/layer** on the string-stack learning curve.

**AI-storage supercycle + the DRAM crowd-out.** NAND is caught in the same shortage as DRAM: HBM consumes ~3x the wafer per bit of commodity DRAM and ~23% of DRAM wafer output, and capacity reallocation plus AI data-lake demand has NAND ASPs rising fast (SanDisk up ~4,000%+ since its Feb-2025 spin). Two spillovers: (1) commodity NAND ASPs inflate alongside DRAM (see the second-order section on **Hbm Bottleneck**); (2) as flash gets expensive, bulk/cold data pushes *down* to nearline HDD, which is why **Western Digital** + **Seagate** also get a bid. Storage-tiering economics tracked on **Memory Disaggregation Storage Non Area**.

## Semron: computing inside 3D NAND

## Investment routes

Scaled exposure is **public**: the NAND makers (**Sandisk**, **Kioxia**, Samsung, SK Hynix, Micron) and the HDD duopoly the shortage pushes demand toward (**Western Digital**, **Seagate**) — full route reads on **Hbm Bottleneck**. The **startup-winnable** frontier is upstream and adjacent, not commodity NAND itself: specialty process materials / equipment (advanced dielectrics, high-aspect-ratio etch, ALD chemistries), storage-controller CIM, and NAND-adjacent emerging NVM (hafnium-oxide FeFETs, MRAM/RRAM/PCM, see **Emerging Nvm**). Commodity NAND fabrication is incumbent-and-capital-locked, so the venture/angel line sits in the enabling layers, never the cell itself.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
