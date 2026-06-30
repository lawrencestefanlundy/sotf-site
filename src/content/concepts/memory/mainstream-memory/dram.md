---
type: concept
slug: dram
canonical_name: DRAM
aliases: []
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts: []
sources: []
frontier:
- Does CXMT convert its 12%-of-global-HBM-*wafer*-share (2028, SemiAnalysis) into competitive HBM *bit* share, or does ~25% 8-hi stacking yield cap it as low-grade domestic supply?
- Does Chinese domestic DRAM (CXMT ~11%→17% of global capacity by 2028) tip commodity DDR5 into oversupply and break the ASP super-cycle?
last_updated: '2026-06-23'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors: []
---
## Physics / mechanism

DRAM stores each bit as charge on a capacitor paired with an access transistor (1T1C cell). Read is destructive—sense amplifiers detect sub-100 fV charge differentials and rewrite. Refresh cycles every ~64 ms prevent leakage-induced data loss, consuming ~10–15% of active power. DRAM scales via process node and cell capacitance engineering (MIM, MIS, stacked trench). Current SOTA: SK Hynix HBM3E at 1.2 TB/s bandwidth, Samsung DDR5 at 7200 MT/s per pin, 10 nm-class (1β/1γ) nodes. Cell capacitance must hold ~10 fF minimum despite shrinking geometry—the central materials and integration challenge as nodes compress below 10 nm.

## Competitive landscape

DRAM competes directly with SRAM (faster, 6T, no refresh, 50–100× area penalty) and emerging non-volatile alternatives for specific tiers. HBM is DRAM repackaged for AI compute bandwidth. Key competitive pressures come from MRAM (persistent, radiation-hard, latency-competitive but density-limited), FeRAM (low power, niche embedded), and CXL-attached DRAM pools blurring memory-storage boundaries.

## DRAM makers: volumes, revenue & HBM-capacity contribution (mid-2026)

DRAM is a ~$170B+ market in the 2026 super-cycle (HBM ≈ one-third of value), and it is an oligopoly: three IDMs hold the overwhelming majority of bits, with CXMT the rising fourth and Nanya the commodity tail. Sizing is what routes this: the structure (a handful of public giants) makes **public markets the first-class route**; everything else is a downstream line. Data below from the SemiAnalysis Memory Model and the HBM state-of-play synthesis (**2026 06 23 Semianalysis Cxmt Set To Challenge Dram Incumbents**, **2026 06 01 Hbm State Of Play**).

**2025 DRAM revenue (SemiAnalysis):** Samsung ~$72.3B · SK Hynix ~$52.1B · Micron ~$37.2B · **CXMT ~$8.6B** · Nanya ~$3.4B TTM (pure-play commodity, no HBM; Q1-26 revenue +582% YoY on the ASP spike).

**HBM revenue share (Counterpoint, Q3 2025):** SK Hynix **57%** · Samsung **22%** · Micron **21%**. 2026 HBM *bit* projection: SK Hynix ~50% · Samsung ~28% · Micron the balance · CXMT negligible (sub-scale, yield-gated).

**HBM revenue trajectory:** ~$4B (2023) → ~$17B (2024) → ~$35B (2025) → ~$33B (2026, UBS) → ~$100B TAM by 2028 (~40% CAGR). 1GB of HBM eats ~3–4× the wafer area of DDR5, so HBM ≈ 23% of global DRAM wafers in 2026, the mechanism that drains commodity DRAM tight and feeds **Tech Inflation Silicon Shock**.

### Contribution to HBM wafer capacity

The supply side of the super-cycle: global HBM wafer capacity scales ~50× from 2022→2027E, and CXMT enters as a visible (teal) sliver only from 2026E.

![Global HBM Wafer Capacity by maker, 2022–2027E](../../../sources/reports/assets/2026-06-23-global-hbm-wafer-capacity.png)

| kwspm | 2022 | 2023 | 2024 | 2025 | 2026E | 2027E |
|-------|------|------|------|------|-------|-------|
| Samsung | ~3 | ~58 | ~130 | ~120 | ~215 | ~258 |
| SK Hynix | ~12 | ~32 | ~80 | ~140 | ~210 | ~248 |
| Micron | – | – | ~52 | ~65 | ~110 | ~155 |
| **CXMT** | – | – | – | ~5 | ~30 | ~55 |
| **Total** | **~15** | **~90** | **~262** | **~330** | **~565** | **~716** |

*By-maker splits read off the SemiAnalysis stacked chart (approximate); CXMT's column (5/30/55 kwspm) is the SemiAnalysis text figure. kwspm = thousand wafer starts per month.*

### CXMT: the China entrant

China's largest DRAM maker and #4 globally by capacity. SemiAnalysis models it from ~265 kwspm DRAM (2025) → ~500 kwspm (2028), lifting its share of **global DRAM capacity from ~13% (2025) to ~17% (2027–28)** and **global DRAM bit shipment from 9% to 12% in 2027**. On HBM specifically, capacity goes 5 → 30 → 55 → 100 kwspm (2025→2028), lifting its global HBM wafer-supply share *"from 1% in 2025 to 12% in 2028."* The IPO (Shanghai STAR) values it ~$27B and raises ~$4.1B for DRAM/HBM expansion. The catch is yield, not capacity: HBM3 8-hi at ~25% overall yield (see [HBM (High-Bandwidth Memory)](/sotf-site/memory/mainstream-memory/hbm/), **Cxmt**): wafer share is not competitive bit share.

## Investibility & routes

| Technology | Density | Latency | Non-volatile |
|---|---|---|---|
| DRAM | High | ~50–100 ns | No |
| SRAM | Low | <1 ns | No |
| MRAM | Medium | ~3–10 ns | Yes |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
