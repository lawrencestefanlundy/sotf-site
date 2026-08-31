---
type: concept
slug: flow-cvd-pecvd
canonical_name: CVD / PECVD deposition (process step)
seq: 27
phase: feol
related_concepts:
- semiconductor-materials-equipment
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 7
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
- slug: semiconductor-materials-equipment
  name: Semiconductor Materials & Equipment
  path: /manufacturing/equipment-processes/semiconductor-materials-equipment/
  macro: manufacturing
---
> Step 27 of 56 in the semiconductor flow (FEOL). Prev: [Annealing / rapid thermal processing (process step)](/semiconductor-process-flow/frontend/flow-annealing-rtp/) · Next: [Atomic layer deposition (ALD) (process step)](/semiconductor-process-flow/frontend/flow-ald-atomic-layer-deposition/)

## What this step does
Chemical vapour deposition (CVD) grows a thin solid film on the wafer by flowing gas-phase precursors that react and deposit on the hot surface. Plasma-enhanced CVD (PECVD) uses an RF plasma to drive the reaction at lower temperature, which is what makes it usable over heat-sensitive layers in the back end. It is the workhorse that deposits most of the dielectric and many of the conductor films a chip is built from. Sub-processes inside this step:
- Thermal / LPCVD: silicon nitride, polysilicon, doped oxides (often batch furnaces, Kokusai/TEL territory).
- PECVD dielectrics: silane- and TEOS-based oxide, nitride, low-k and the SiCN/SiN barrier and capping layers between metal levels.
- Tungsten and metal CVD: WF6-based tungsten fill for contacts and vias, plus liner/barrier films.
- Hard-mask and patterning films: amorphous carbon, anti-reflective coatings used by litho/etch.

## Where it sits and why it matters
Deposition and removal (etch) are the two highest-frequency operations in the fab. A modern logic or 3D-NAND wafer passes through deposition dozens of times, and CVD/PECVD is the largest sub-family of deposition by spend. As devices move to gate-all-around transistors and ever-taller NAND stacks, the number of conformal and gap-fill film steps keeps rising, so deposition intensity grows faster than wafer count. This step feeds directly into [Atomic layer deposition (ALD) (process step)](/semiconductor-process-flow/frontend/flow-ald-atomic-layer-deposition/) (the angstrom-precise complement) and is interleaved with [Plasma / dry etch (process step)](/semiconductor-process-flow/frontend/flow-plasma-dry-etch/).

## Equipment market
Deposition is roughly 20-25% of the ~$140B 2024 wafer-fab-equipment market; Yole puts the deposition equipment segment at about $14B in 2024, growing toward ~$24.5B by 2035 (low-to-high single digit CAGR, call it ~6-7%) [1][3]. CVD is the largest slice of that deposition spend; standalone PECVD systems are estimated at $2.5-4.7B depending on the source and how PVD/ALD are carved out [2]. Treat the report-mill PECVD point estimates as rough; the segment boundary is fuzzy.

| Vendor | HQ | Est. share (deposition) | Notable |
|---|---|---|---|
| Applied Materials | US | ~40-43% (broad deposition leader) | Producer/Centura PECVD, tungsten/metal CVD; widest portfolio [4][6] |
| Lam Research | US | top-3 in CVD/dielectric & metal | Dielectric + tungsten/metal deposition, strong in NAND [4][7] |
| Tokyo Electron (TEL) | Japan | top-3 | Thermal/LPCVD, coater track-adjacent films [4] |
| Kokusai Electric (KSEC) | Japan | strong in batch CVD/furnaces | Vertical-furnace LPCVD/oxide-nitride; ALD-adjacent [1][4] |
| ASM International | NL | ALD-led, some CVD/epi | More ALD/epi than CVD but overlaps [4] |
| Others: AIXTRON, Oxford Instruments, SPTS (KLA), Veeco, NAURA | EU/US/CN | niche / specialty / China-domestic | MOCVD, R&D and specialty PECVD, fast-rising China tools [8] |

Concentration note: the front-end equipment market is an oligopoly. The "Big Five" (ASML, Applied, Lam, TEL, KLA) held nearly 70% of WFE in 2024 [3]. Within deposition, Applied Materials is the clear leader and the top three or four vendors capture the overwhelming majority of spend.

## Materials & consumables
This step consumes a continuous stream of precursors and process gases: silane and dichlorosilane (oxide/nitride), TEOS (oxide), WF6 (tungsten), ammonia, plus the carrier and clean gases (NF3 chamber clean). It also burns hardware kits, showerheads, heaters and quartz that are replaced on a cycle. Silicon-precursor supply alone is ~$3.2B in 2025 at ~7.5% CAGR; the broader CVD/ALD precursor and specialty-gas pool is larger and faster (some sources ~10%+ CAGR) [5]. Suppliers: Merck/Versum, Entegris, Air Liquide Electronics, Linde, SK Materials, DuPont, Taiyo Nippon Sanso. This is recurring revenue: precursors and gases ship every day a fab runs, decoupled from the lumpy tool capex cycle, which is exactly why the materials layer is structurally attractive even when equipment orders soften [5].

## Volumes, revenue, profitability
There is no clean "unit volume" for deposition; the meaningful unit is wafer starts times film steps per wafer, and that product is rising as nodes add layers. Revenue pool: ~$14B/yr equipment + a multi-billion precursor/gas stream tied to the same installed base [1][5]. Margins: Applied Materials ran ~47.5% GAAP gross and ~29% operating in FY2024, with its Semiconductor Systems segment at ~35% operating margin [4]. Lam Research sits in a similar band. The equipment vendors earn the highest margin (proprietary tools, switching cost, service attach); precursor/gas suppliers earn lower gross margins but durable, recurring volume. The fab operator captures the downstream value; the tool and materials suppliers capture the picks-and-shovels margin.

## Competitive landscape & value capture
The moat is process know-how and qualification lock-in: a deposition recipe is co-developed with the foundry over years and is painful to re-qualify, so incumbents hold position node over node. Value accrues to (1) the handful of tool OEMs, with Applied Materials dominant, and (2) the recurring precursor/gas oligopoly (Merck, Entegris, Air Liquide, Linde). Europe is present but not dominant: ASML is litho not deposition; relevant EU deposition names are AIXTRON (MOCVD, Germany), Oxford Instruments Plasma Technology (specialty PECVD/R&D, UK) and SPTS (KLA, UK). These are mostly listed or owned, not seed.

## Market drivers, constraints & trends
Net read: steady-to-accelerating served market, but the equipment half rides a memory-led capex cycle while the precursor/gas half is the smoother compounder.

- **Drivers**
 - Deposition intensity outgrows wafer count. The move to sub-5nm and gate-all-around adds roughly 30-50% more CVD/ALD process steps per wafer vs 7nm, so tool and precursor consumption rise even when output is flat [9]. TSMC put GAA into production at N2 in 2025; GAA plus backside power at A16 adds more conformal film steps again [10].
 - 3D NAND vertical scaling. Stacks now exceed 300 layers, with ~1,000 layers projected by 2030; every added layer is more conformal dielectric and metal deposition [10][11].
 - AI/memory capex. SEMI sees WFE up ~9% in 2026 and ~7% in 2027 to a record ~$156B in equipment sales by 2027, with NAND WFE +35% and DRAM/HBM +18% in 2026 pulling deposition-heavy memory spend [12].
 - Advanced packaging. Hybrid-bonding equipment is forecast at ~21% CAGR 2025-2030; the SiCN/oxide bonding dielectric and TSV passivation are PECVD/CVD steps, opening a packaging-side demand pool on top of front-end [13].

- **Constraints**
 - China digestion and localisation. China is the largest WFE buyer but stops expanding from 2026, and a domestic-tool mandate is sidelining foreign suppliers; Piotech (China thin-film deposition) roughly doubled nine-month 2025 revenue to ~$617M, eroding the served pool the incumbents can address [14].
 - Cyclicality and capex lumpiness. Equipment orders swing with the memory cycle (NAND WFE itself moved from deep cuts to +35%), so the tool line is volatile even as the secular trend rises [12].
 - Step-count erosion from new metals. Molybdenum replaces tungsten in NAND wordlines and needs no barrier/adhesion layer, removing process steps; lower step count per layer is a mild headwind to CVD intensity even as it triggers a tool refresh [13].

- **Trends & inflections to watch**
 - Tungsten-to-molybdenum metallisation. Lam's ALTUS Halo Mo-ALD (Feb 2025) and Applied's Selectra Mo etch mark the shift. Tripwire: Mo wordlines qualified into high-volume 1,000-layer NAND by ~2027-28 confirms a metal-deposition refresh cycle [13].
 - Packaging deposition as a second engine. Tripwire: hybrid-bonding lines reaching sub-1um pitch in HVM at a leading memory/foundry maker would re-rate the PECVD packaging pool [13].
 - China share crossover. Tripwire: a foreign deposition vendor reporting China revenue below ~25% of total (from ~35-40%) would confirm localisation is permanently shrinking the addressable pool [14].

## Connections
[Semiconductor Materials & Equipment](/manufacturing/equipment-processes/semiconductor-materials-equipment/) · **Deposition Materials Process Market** · [Annealing / rapid thermal processing (process step)](/semiconductor-process-flow/frontend/flow-annealing-rtp/) · [Atomic layer deposition (ALD) (process step)](/semiconductor-process-flow/frontend/flow-ald-atomic-layer-deposition/) · [Plasma / dry etch (process step)](/semiconductor-process-flow/frontend/flow-plasma-dry-etch/)

## Sources
1. Yole, Status of the WFE Industry / deposition segment (~$14B 2024 to ~$24.5B 2035): https://www.yolegroup.com/product/report/status-of-the-wafer-fab-equipment-industry-2024/
2. Verified Market Reports, PECVD Systems Market ($2.5B 2024) / Semiconductor PECVD ($4.7B 2023): https://www.verifiedmarketreports.com/product/plasma-enhanced-chemical-vapor-deposition-pecvd-systems-market/
3. Yole, WFE market to hit $184B by 2030; $140B 2024, Big Five ~70%: https://www.yolegroup.com/press-release/wafer-fab-equipment-wfe-market-to-hit-184-billion-by-2030-for-equipment-and-services-driven-by-specialized-segment-growth-and-global-manufacturing-shifts/
4. Yole, semiconductor equipment market-share reshuffle (vendor shares, deposition ~26-27% of WFE): https://www.yolegroup.com/strategy-insights/semiconductor-equipment-market-share-reshuffles-amid-memory-demand-decline/
5. Verified Market Reports, Semiconductor Silicon Precursor Market ($3.2B 2025, 7.5% CAGR; supplier oligopoly): https://www.verifiedmarketreports.com/product/semiconductor-silicon-precursor-market/
6. Applied Materials FY2024 results (47.5% GAAP GM, ~29% OM, Semi Systems ~35% OM): https://www.globenewswire.com/news-release/2024/11/14/2981573/0/en/Applied-Materials-Announces-Fourth-Quarter-and-Fiscal-Year-2024-Results.html
7. Lam Research FY2024 (system revenue incl. deposition/etch/clean): https://www.statista.com/statistics/1374835/lam-research-revenue-by-segment/
8. Oxford Instruments Plasma Technology / AIXTRON (EU specialty CVD/PECVD/MOCVD): https://plasma.oxinst.com/
9. OpenPR / Research Nester, CVD equipment market to ~$11.7B by 2036 (GAA + sub-5nm add 30-50% more CVD steps per wafer vs 7nm): https://www.openpr.com/news/4494410/semiconductor-chemical-vapor-deposition-cvd-equipment
10. SemiAnalysis, GAA + backside power at 2nm; imec 3D NAND >300 layers, ~1,000 by 2030 (deposition complexity): https://newsletter.semianalysis.com/p/clash-of-the-foundries
11. imec / Electronic Design, z-pitch scaling for next-gen 3D NAND (layer scaling, conformal deposition challenge): https://www.electronicdesign.com/technologies/embedded/article/55307984/imec-unlocking-z-pitch-scaling-for-next-generation-3d-nand-flash
12. SEMI, global equipment sales to record ~$156B by 2027; WFE +9% 2026 / +7.3% 2027; NAND WFE +35%, DRAM +18% 2026: https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports
13. Lam Research ALTUS Halo Mo-ALD (Feb 2025) + Mo-replaces-W removes barrier/adhesion steps; hybrid bonding ~21% CAGR 2025-30, SiCN/oxide via PECVD: https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition
14. Tom's Hardware, China domestic deposition localisation (Piotech ~doubles 9-mo 2025 rev to ~$617M; foreign suppliers sidelined; AMEC/Naura record revenue): https://www.tomshardware.com/tech-industry/semiconductors/smic-founder-and-amec-ceo-urge-chinese-fabs-to-test-domestic-chip-tools-on-production-lines
