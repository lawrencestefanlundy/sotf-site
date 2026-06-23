---
type: concept
slug: hbm
canonical_name: HBM (High-Bandwidth Memory)
aliases:
- High Bandwidth Memory
- HBM3E
- HBM4
kind: technology
parent_concepts:
- memory
- mainstream-memory
related_concepts:
- dram
- cowos
- hbm-cowos-bottleneck
- advanced-packaging
- hybrid-bonding
- tsv-through-silicon-via
sources:
- '[[2026-06-01-hbm-state-of-play]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- Does Samsung's SF4 in-house base-die HBM4 yield cross the ~60% breakeven, or does the TSMC-base-die route (SK Hynix + Micron) keep the cost/yield edge?
- 'HBM4 volume-leadership: does Samsung''s first-to-qualify headline convert to bit-share, or does SK Hynix''s reliability edge hold the volume + profit lead?'
- Does a >25% peak-to-trough DRAM ASP correction land in any 4-quarter window through 2027 (= supercycle broken)?
- Does memory-compression / quantisation (HBM-bytes-per-token) bend the demand curve before supply catches up in 2027?
last_updated: '2026-06-22'
tags:
- concept
- technology
- hbm
- memory
- supercycle
last_reorg_date: '2026-05-14'
public_expressions:
- 000660.KS
- 005930.KS
- MU
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: dram
  name: DRAM
  path: /sotf-site/memory/mainstream-memory/dram/
  macro: memory
- slug: cowos
  name: CoWoS (TSMC)
  path: /sotf-site/manufacturing/packaging/cowos/
  macro: manufacturing
- slug: hbm-cowos-bottleneck
  name: HBM / CoWoS Bottleneck
  path: /sotf-site/compute/compute-architecture/hbm-cowos-bottleneck/
  macro: compute
- slug: advanced-packaging
  name: Advanced Packaging
  path: /sotf-site/manufacturing/packaging/advanced-packaging/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /sotf-site/manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: tsv-through-silicon-via
  name: TSV / Through-Silicon Via
  path: /sotf-site/manufacturing/packaging/tsv-through-silicon-via/
  macro: manufacturing
---
*the memory denominator for **Hbm Bottleneck**. Research base: **2026 06 01 Hbm State Of Play** (mid-2026), **2026 05 07 Hbm Supercycle Thesis Update**.*

## What it is (physics / mechanism)

HBM stacks DRAM dies vertically over a base die, connects them with through-silicon vias (TSVs), and co-packages the stack next to the accelerator on a silicon interposer (2.5D). The short TSV interconnects replace long PCB traces, cutting energy per bit to ~3-4 pJ/bit (vs ~15 pJ/bit GDDR6).

The load-bearing point: **bandwidth scales by bus width, not clock.** HBM3E runs a 1,024-bit-per-stack interface; HBM4 doubles I/O to 2,048-bit, which is why throughput roughly doubles at HBM4 even at modest per-pin speeds. You widen the bus rather than chase frequency.

**HBM only delivers its bandwidth when co-integrated on the interposer next to the GPU, and that interposer is TSMC CoWoS.** So HBM is welded to advanced packaging: see [HBM / CoWoS Bottleneck](/sotf-site/compute/compute-architecture/hbm-cowos-bottleneck/). Multiple analysts argue CoWoS, not the memory die, is the actual gating constraint (Nvidia booked ~55% of TSMC's 2026 CoWoS capacity; lead times 50-104 weeks).

## Generation roadmap

| Gen | Pin speed | Bandwidth / stack | Capacity / stack | Status (mid-2026) |
|---|---|---|---|---|
| HBM2E | ~3.6 Gb/s | ~460 GB/s | up to 16GB | legacy (A100 era) |
| HBM3 | ~6.4 Gb/s | ~819 GB/s | up to 24GB | H100 |
| HBM3E | ~8-9.6 Gb/s | ~1.2 TB/s | 24GB (8-hi) / 36GB (12-hi) | mainstream 2024-2026 |
| HBM4 | 6.4 Gb/s JEDEC base, vendors push 11-13 | ~2.0-3.3 TB/s (pin-speed dependent) | 36GB (12-hi) / 48-64GB (16-hi) | ramping 2026 |
| HBM4E / C-HBM4E | ~12.8 Gb/s | ~3+ TB/s | larger | 2027; ~40% of 2027 HBM demand (TrendForce) |

The HBM4 per-stack bandwidth quoted as 2.0 / 2.8 / 3.3 TB/s is a pin-speed-quoting artefact (different vendors quote different speeds), not a contradiction. Samsung demoed 13 Gb/s → 3.3 TB/s at ISSCC Feb 2026; Micron ships >11 Gb/s → >2.8 TB/s.

**At the accelerator level** the stacks aggregate: an H100 (HBM3) reads memory at 3.35 TB/s, an H200 (HBM3E) 4.8 TB/s, a Blackwell B200 (HBM3E) ~8 TB/s (NVIDIA datasheets). A DDR5 channel, by contrast, moves only tens of GB/s, which is why AI accelerators pay the HBM premium at all, and why the [The Memory Wall](/sotf-site/compute/compute-architecture/memory-wall/) binds despite it (compute has outgrown even HBM, +60,000x vs +100x bandwidth over 20yr, **2024 Gholami Ai And Memory Wall**).

**The structural HBM4 shift: the passive base die becomes a LOGIC base die.** This opens customer-specific customisation (controllers, near-memory compute) and turns HBM from a commodity into a design-win business. The competitive fault line is the foundry split: **SK Hynix and Micron use TSMC (N12-class) base dies; Samsung uses its own SF4 (4nm) foundry base die.** That split is why yields diverge (below).

## The market and the supercycle

- **Revenue trajectory:** ~$4B (2023) → ~$17B (2024) → ~$35B (2025, Micron TAM) → ~$32.7B (2026, UBS), roughly **one-third of total DRAM value**, scaling toward a ~$100B TAM by 2028 (~40% CAGR). *(Ignore generic market-research trackers quoting $3-9B; they fail bit-growth × ASP math.)*
- **Demand growth:** +130% YoY (2025), ~+70-77% (2026), +68% (2027) per TrendForce.
- **Why it drains the whole DRAM market:** 1GB of HBM consumes ~3-4× the wafer capacity of standard DDR5. AI is set to take ~20% of global DRAM wafer capacity in 2026, which is what pulls commodity DRAM tight and feeds **Tech Inflation Silicon Shock**.
- **Supercycle signals:** SK Hynix sold out its entire 2026 output (booked back in Oct 2025), inventory collapsed from ~17 weeks (late 2024) to 2-4 weeks, DRAM ASP +80-90% in Q1 2026 (Counterpoint), Samsung hiked memory prices up to 60%, HBM3E carries a ~20% price hike for 2026, HBM4 a >30% premium. Customers are pre-paying and co-investing. Both SK Hynix and Samsung warn of shortage through 2027+.
- **Read:** Bernstein calls it a "DRAM super-cycle"; the duration is structural (tied to ~$650B AI infra capex in 2026, +80% YoY), not a consumer cycle. This is a rerate, not a boom-bust, unless the bear triggers fire.

## The three suppliers (who is best placed, and why)

**Market share (HBM revenue, Counterpoint Q3 2025): SK Hynix 57% · Samsung 22% · Micron 21%.** 2026 bit-output projection: SK Hynix ~50%, Samsung ~28%, Micron the balance.

**SK Hynix — best-placed overall (~75% confidence).** Share leader, Nvidia's primary HBM supplier (Nvidia ~15% of its revenue), sold out through 2026 into 2027. The durable edge is execution: ~80-90% HBM3E yields, MR-MUF packaging (<2°C thermal delta across a 12-hi stack), and the mature, low-cost, high-yield TSMC N12 base-die path carried into HBM4. Q1 2026 record sales; crossed ~$1T market cap. Weakness: lost the HBM4 first-to-ship headline to Samsung this cycle, and share is eroding off a 60%+ peak.

**Samsung — best-in-class HBM4 performance, riskiest path.** Won the HBM4 first-mover sprint on paper (passed Nvidia's 11 Gb/s bar, demoed 13 Gb/s / 3.3 TB/s at ISSCC, began full HBM4 shipments Feb 2026, set to lead Vera-Rubin-specific HBM4 supply). The vertical-integration story (DRAM + own foundry + packaging) matters more as HBM4 moves to a logic base die. But SemiAnalysis is explicit: Samsung still lags SK Hynix on reliability/stability, and its in-house SF4 base die + 1c DRAM runs only ~50-60% yield (below ~60% breakeven), a margin/execution risk. **Net: Samsung wins the headline, SK Hynix likely wins the volume.**

**Micron — solid #3, the US/Western hedge, and a 2026 surprise.** At GTC (Mar 2026) Micron announced high-volume HBM4 36GB 12-high for Nvidia Vera Rubin (>11 Gb/s, >2.8 TB/s) and is sampling 48GB 16-high, using a low-cost internal CMOS base die. The only US-based supplier, so it carries the CHIPS-aligned structural angle (ties to **Sovereignty Semi Bifurcation**). 2026 supply fully booked; FY26 capex ~$20B; >50% gross margin. *(Divergence flag: an earlier TrendForce note framed Micron as "limited to mid-tier Rubin CPX"; Micron's own IR contradicts it. Trust the primary.)*

## Routes (how to express it)

## The bear case (what breaks the supercycle)

- **Memory-compression / quantisation** (FP4 inference, KV-cache + weight compression) cutting HBM-bytes-per-token and bending the demand curve. Directional, not yet quantified; contested vs the Jevons view that cheaper effective memory just expands usage.
- **AI-capex concentration:** demand underwritten by a handful of hyperscaler + Nvidia plans; any unwind hits HBM first (highest-beta line).
- **Supply catches up by 2027:** all three ramp HBM4 through 2026; TechInsights forecasts a 2027 downturn. Contested vs Samsung/SK Hynix "shortage through 2027+" guidance.
- **Watchable signals:** HBM-bytes-per-token trend; hyperscaler capex revisions (leading indicator); booking-coverage ratios rolling off 100%; DRAM contract ASP sequentials turning negative; CoWoS lead-time compression; Samsung 1c/SF4 yield disclosures. The KB's formal trigger: a >25% peak-to-trough DRAM ASP correction in any 4-quarter window through 2027 = supercycle thesis broken.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
