---
type: concept
slug: flow-ald-atomic-layer-deposition
canonical_name: Atomic layer deposition (ALD) (process step)
seq: 28
phase: feol
related_concepts:
- ald-atomic-layer-deposition
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 9
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors:
- slug: ald-atomic-layer-deposition
  name: ALD (Atomic Layer Deposition)
  path: /manufacturing/equipment-processes/ald-atomic-layer-deposition/
  macro: manufacturing
---
> Step 28 of 56 in the semiconductor flow (FEOL). Prev: [CVD / PECVD deposition (process step)](/semiconductor-process-flow/frontend/flow-cvd-pecvd/) · Next: [PVD / sputtering (process step)](/semiconductor-process-flow/frontend/flow-pvd-sputtering/)

## What this step does
ALD builds ultra-thin films one atomic layer at a time. Unlike CVD, where precursors react continuously, ALD splits the reaction into self-limiting half-cycles separated by inert-gas purges, so each pulse deposits exactly one monolayer no matter the surface shape. That gives near-perfect thickness control (sub-nanometre) and conformality on the vertical, high-aspect-ratio structures that define modern logic and memory. Sub-processes inside the step:
- High-k gate dielectric deposition (hafnium oxide, zirconium oxide) for the gate stack.
- Conformal liners and barriers (TiN, TaN) and ALD tungsten/molybdenum nucleation.
- Spacer and patterning films for self-aligned multi-patterning (a key litho-saver).
- Batch ALD for memory (3D NAND, DRAM capacitors) where throughput matters; single-wafer ALD for leading-edge logic.

## Where it sits and why it matters
ALD is the fastest-growing deposition technique because the industry is going vertical. Gate-all-around (GAA) transistors at 2nm wrap the gate around stacked nanosheets, 3D DRAM and ever-taller 3D NAD multiply the number of conformal-film steps, and self-aligned patterning offloads cost from EUV onto deposition. Each of these raises "ALD intensity," the number of ALD layers per wafer. ASM estimates the GAA and FinFET-in-periphery transition alone adds US$400-450M to its served market [1]. ALD is the technique that scales with vertical complexity, which is why it outgrows CVD and PVD.

## Equipment market
The cleanest figure comes from ASM's 2025 Investor Day: the single-wafer ALD market grows from US$3.0B (2024) to US$5.1-6.1B by 2030, a 9-13% CAGR [1]. Adding batch ALD and broader definitions, third-party reports put total ALD equipment at roughly US$4-9B in 2024-2025 at 10-17% CAGR; that spread reflects inconsistent report-mill scoping, so treat the ASM single-wafer figure as the anchor [1][2].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| ASM International | Netherlands | mid-50s% single-wafer ALD [3] | Gold standard for logic high-k ALD; Pulsar / Synergos platforms |
| Kokusai Electric | Japan | ~70% batch ALD [4] | Batch furnaces for 3D NAND / DRAM; KKR-backed 2023-24 IPO |
| Tokyo Electron (TEL) | Japan | #2 batch, growing single-wafer [4] | Strong memory and patterning film position |
| Lam Research | US | ~34% ALD-dielectric memory penetration [3] | High-aspect-ratio gapfill / dielectric ALD |
| Applied Materials | US | minority, scaling [3] | Acquired Picosun (2022); GAA and 3D DRAM R&D push |

Concentration is high: the four WFE incumbents (AMAT, ASM, TEL, Lam) plus Kokusai hold roughly 72% of revenue [3], and the market splits cleanly by segment, ASM owning single-wafer logic, Kokusai owning batch memory.

## Materials & consumables
Every ALD cycle consumes metal-organic precursors: trimethylaluminium (TMA) for alumina, hafnium and zirconium amides for high-k, plus titanium, tantalum, molybdenum and tungsten precursors for liners and metal fill, alongside co-reactants (water, ozone, plasma). This is a recurring, per-wafer consumable pull-through that grows with ALD-layer count, so it tracks tool installed base rather than tool sales. The high-k and metal-precursor market is roughly US$0.6-1.2B (2024-2025) at high-single-digit CAGR; metal precursors specifically were about US$646M in 2024 [5]. Estimates vary widely by report, so the range is rough. Top suppliers: Merck KGaA (EMD), Entegris, Air Liquide, Adeka, Linde/Praxair and Hansol Chemical, the top five holding about 62% of the precursor market [5].

## Volumes, revenue, profitability
The revenue pool splits two ways. Tools are a lumpy ~US$5-6B equipment market that follows fab capex cycles; precursors are a smaller ~US$1B but stickier, recurring stream. The economics are excellent for the lead vendor: ASM posted FY2024 adjusted gross margin of 50.5% and adjusted operating margin of 28.0% on EUR2,933M revenue, and grew faster than WFE [6][1]. ASM's 2030 plan targets revenue above EUR5.7B at a 12%+ CAGR versus ~6% for the broader WFE market, explicitly an outperformance story driven by ALD intensity [1]. The margin accrues to the equipment vendor that owns the qualified process recipe at a given node, not to the fab or the precursor chemist; switching a qualified ALD recipe is slow and risky, which is the moat.

## Market drivers, constraints & trends
Net read: this is the structurally fastest-growing deposition step, set to outgrow WFE through the decade, but the served market still rides the memory and fab-capex cycle.

- **Drivers**
  - ALD intensity compounds with every vertical transition at once: GAA at 2nm/1.4nm, 3D DRAM, and taller 3D NAND each add conformal-film steps, and ASM guides to double-digit growth in application layers per node [7][9]. The single-wafer ALD market is put at US$4.2-5.0B by 2027 (10-14% CAGR) [9].
  - New metal chemistry expands the recipe pool: Lam's ALTUS Halo molybdenum ALD (Feb 2025) replaces tungsten, removes barrier/liner steps and is being adopted at 3D NAND fabs in Korea and Singapore [7].
  - Advanced DRAM/HBM is adopting logic-like ALD: ASM won new ALD dipole and work-function layer orders for DRAM/HBM ramping 2026-2027 [9].

- **Constraints**
  - The equipment pool is lumpy and cyclical, tracking memory and leading-edge fab capex rather than steady end-demand [9].
  - China is both a demand prop and a threat: domestic tool-makers now supply ~40% of China's deposition/etch market (2024-25), commoditising trailing-edge ALD even as export controls cap leading-edge sales [8].
  - Value stays locked to a few incumbents owning the qualified recipe; new entrants face years-long node qualification [11].

- **Trends & inflections to watch**
  - Area-selective deposition (ASD) is the late-2020s battleground, deleting litho steps via bottom-up growth; tripwire: first ASD/AS-ALD module qualified in HVM logic (watch ASM/AMAT/Lam 2026-2027 disclosures) [10].
  - Molybdenum displacing tungsten/copper; tripwire: SK Hynix 375-layer Mo-NAND reaching mass production by end-2026 [7].
  - Backside power delivery adds ALD layers; tripwire: BSPDN entering HVM at 2nm/A16 from 2026 [9].

## Connections
- Cluster concept: [ALD (Atomic Layer Deposition)](/manufacturing/equipment-processes/ald-atomic-layer-deposition/)
- Thesis: **Deposition Materials Process Market**
- Flow neighbours: [CVD / PECVD deposition (process step)](/semiconductor-process-flow/frontend/flow-cvd-pecvd/) · [PVD / sputtering (process step)](/semiconductor-process-flow/frontend/flow-pvd-sputtering/) · [Thermal oxidation & gate dielectric (process step)](/semiconductor-process-flow/frontend/flow-thermal-oxidation-gate-dielectric/) · [Epitaxial deposition (epi) (process step)](/semiconductor-process-flow/frontend/flow-epitaxy/)