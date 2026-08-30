---
type: concept
slug: flow-transistor-module-finfet-gaa
canonical_name: Transistor module (FinFET / GAA nanosheet) (process step)
seq: 31
phase: feol
related_concepts:
- high-k-dielectrics
- ru-w-co-metallisation
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
neighbors:
- slug: high-k-dielectrics
  name: High-K Dielectrics (HfO2, ZrO2)
  path: /materials/functional-layers/high-k-dielectrics/
  macro: materials
- slug: ru-w-co-metallisation
  name: Ru / W / Co Metallisation
  path: /manufacturing/equipment-processes/ru-w-co-metallisation/
  macro: manufacturing
---
> Step 31 of 56 in the semiconductor flow (FEOL). Prev: [Chemical-mechanical planarisation (CMP) (process step)](/semiconductor-process-flow/frontend/flow-cmp-planarisation/) · Next: [Contact & middle-of-line (silicide, contact fill) (process step)](/semiconductor-process-flow/frontend/flow-contact-mol-silicide/)

## What this step does
This is not a single tool. It is the integrated module that actually builds the switch: dozens of deposition, etch, epi and clean steps that shape the channel, wrap the gate around it, and form the source/drain. The architecture has marched from planar to FinFET (channel stands up as a fin, gate on three sides) to gate-all-around nanosheet (GAA, gate wraps the channel on all four sides), and next to CFET (n and p devices stacked vertically, ~2031). A single GAA transistor now takes more than 500 process steps [3][7]. The defining unit sub-processes:
- **Superlattice epi** — alternating Si / SiGe layers grown by selective epitaxy; the SiGe is the eventual sacrificial layer.
- **Fin / nanosheet patterning** — lithography plus plasma etch to define the stack.
- **Nanosheet release (channel-defining selective etch)** — atomic-layer etch removes the SiGe and leaves the Si sheets suspended like ladder rungs. Samsung's 3nm flow needs ~11 plasma steps to free the sheets versus ~6 for FinFET [9].
- **Inner-spacer + gate-stack ALD** — high-k dielectric and work-function metals deposited atom-layer by atom-layer into the gaps between sheets ([High-K Dielectrics (HfO2, ZrO2)](/materials/functional-layers/high-k-dielectrics/)).
- **Source/drain selective epi** — doped SiGe / Si grown only on exposed silicon to strain and contact the channel.

## Where it sits and why it matters
This module is the heart of FEOL and the single biggest reason advanced nodes cost what they do. It is where the actual electrical device is formed, so it gates performance, power and yield. Crucially for an investor, the FinFET-to-GAA-to-CFET march is the structural driver of equipment intensity: each transition does not just shrink, it adds new deposition, epi and selective-etch steps. That is why this step, more than lithography, is where deposition and etch vendors expand their served market node over node.

## Equipment market
There is no clean "GAA transistor tool" line; the value shows up inside the deposition, selective-etch and epitaxy segments of the ~$110B+ wafer-fab-equipment market [8]. The single-wafer ALD market alone runs ~$3.0B in 2024 heading to $5.1-6.1B by 2030 (9-13% CAGR) [2], and ASM has said first-gen GAA added ~$400M to its served available market versus 3nm FinFET, with the move to 1.4nm adding a further ~$450-500M, weighted to FEOL transistor steps [2][4]. AMAT frames the same inflection as roughly $1B of incremental tool revenue per 100,000 wafer starts of leading-edge GAA capacity, mostly deposition and etch [5].

| Vendor | HQ | Est. share of the GAA-relevant pool | Notable |
|---|---|---|---|
| Applied Materials | US | Leader in deposition + selective etch; ~1/3 of broad WFE | Selectra selective etch, Trillium/Xtera epi+ALD, IMS integration [5][6] |
| Lam Research | US | Co-leader in etch; ~42% of GAA-specific etch wins in 2025 | Selective-etch family (Argos, Prevos, Selis), ALE for sheet release [9][10] |
| Tokyo Electron (TEL) | JP | Major in etch + coat/develop; part of the ~75% etch trio | Strong in plasma etch and clean for the module [9] |
| ASM International | NL | ALD + epi leader at FEOL | Biggest single GAA content-gainer; SAM step-ups above [2][4] |

Concentration note: AMAT, Lam and TEL controlled ~75% of etch revenue in 2025 [9]; ALD/epi is effectively an ASM / AMAT / TEL contest. This is the most concentrated layer of the whole flow after lithography.

## Materials & consumables
The module consumes process gases and ultra-pure precursors rather than a branded consumable: high-k and work-function metal ALD precursors (hafnium, lanthanum, aluminium, the move toward molybdenum to replace tungsten/copper) [6], silicon and germanium epi source gases, and the etch chemistries for selective SiGe removal. These are sold by the specialty-gas / electronic-materials majors (Merck/EMD, Entegris, Air Liquide, Linde, Adeka, DNF). The recurring-revenue point: every wafer pass burns precursor and gas, and GAA's extra ALD and epi cycles raise per-wafer materials intensity, so the materials line grows faster than wafer volumes alone. Hard public share splits for these GAA-specific precursors are not cleanly disclosed; treat any single number as an estimate.

## Volumes, revenue, profitability
Volume is best read as leading-edge wafer starts: GAA capacity (TSMC N2, Samsung SF2, Intel 18A) is ramping through 2025-2027 on the order of low-hundreds-of-thousands of wafers per month industry-wide, each cohort of 100k starts pulling roughly $1B of incremental tools [5]. The revenue pool that this module specifically expands is the deposition + selective-etch + epi slice of WFE, plausibly $25-35B/yr today and the fastest-growing part of it. Who earns the margin: the equipment majors. AMAT ran ~47.5% gross / ~29% operating margin in FY2024 [11]; ASM ran ~50.5% gross / ~28% operating on €2.9B revenue [12]. Lam is in a similar band. These are durable hardware-plus-service margins, protected by the qualification lock-in described below.

## Market drivers, constraints & trends
Net read: this is one of the few steps where the served market is structurally accelerating, because every node transition adds deposition, epi and selective-etch steps faster than wafer volumes grow, and AI is now funding the leading-edge ramp.

- **Drivers**
  - AI is pulling the leading-edge ramp hard: TSMC put N2 (its first GAA node) into volume production in early 2026 with Apple, AMD, Nvidia and Qualcomm committed, and Nvidia's N2-based Rubin in production [14][18]. SEMI forecasts equipment sales hitting a record $156B in 2027, with the foundry/logic segment alone at $75.2B, driven explicitly by AI leading-edge logic [17].
  - Pricing power is in the supply chain: TSMC 2nm wafers are ~$30k versus ~$20k for 3nm, so each GAA wafer carries far more embedded tool and precursor value [18].
  - Two GAA-capable fabs ramping at once on strong customer pull, with N2P trial production from March 2026, compounds the deposition/epi/etch pull through 2026-2027 [14][18].
- **Constraints**
  - Capex intensity and cyclicality: this content sits on a handful of multi-billion-dollar leading-edge nodes, so a single customer push-out (Samsung SF2 meaningful volume has already slipped toward 2028) swings the served market [18].
  - China and export controls cap the addressable share: GAA tool sales are concentrated in TSMC/Samsung/Intel, while China WFE spend stays largely on mature and select advanced nodes [17].
  - Samsung undercutting 2nm to ~$20k pressures the pricing-power story if a share war breaks out [18].
- **Trends & inflections to watch**
  - Backside power delivery is the next content layer: Intel 18A (RibbonFET GAA + PowerVia) is in production ahead of TSMC's A16 Super Power Rail, expected end-2026; it adds high-aspect-ratio etch, fill and extreme wafer-thinning steps. Tripwire: A16 reaching volume production by Q4 2026 [15][16].
  - CFET (n/p stacked) is the larger step-up, targeted ~2031 (imec A7), needing HAR etch and wafer bonding. Tripwire: a foundry committing CFET to a named production node on a public roadmap [15].
  - ASM's disclosed SAM step-ups (+$400M first-gen GAA, +$450-500M at 1.4nm) are the cleanest gauge. Tripwire: ASM/AMAT raising per-node GAA content guidance at the next investor day [4][17].

## Connections
- [High-K Dielectrics (HfO2, ZrO2)](/materials/functional-layers/high-k-dielectrics/) — the gate-stack ALD films deposited into the nanosheet gaps in this module.
- [Ru / W / Co Metallisation](/manufacturing/equipment-processes/ru-w-co-metallisation/) — adjacent metallisation chemistry; the gate-fill and contact metals tie in here.
- **Transistor Scaling Over** — thesis tested directly: GAA/CFET shows scaling is harder and costlier, not over; the value migrates from area-shrink to architecture.
- **Specialty Silicon Non Leading Edge** — the counter-position; most of the world's silicon never reaches this module, so the non-leading-edge thesis lives alongside it.

## Sources
1. Precedence Research, Gate-All-Around (GAA) Transistor Market — https://www.precedenceresearch.com/gate-all-around-transistor-market
2. Convequity / ASM ALD market sizing ($3.0B 2024 → $5.1-6.1B 2030) — https://convequity.substack.com/p/no-ald-no-ai-the-case-for-asm-international
3. Futurum Group, Applied Materials arms chipmakers for the GAA era (500+ steps) — https://futurumgroup.com/insights/applied-materials-arms-chipmakers-for-the-gaa-era-with-angstrom-class-tools/
4. ASM Investor Day 2025 (SAM step-ups: +$400M first-gen GAA, +$450-500M at 1.4nm) — https://www.globenewswire.com/news-release/2025/09/23/3154400/0/en/ASM-hosts-Investor-Day-provides-new-2030-targets-revises-H2-2025-outlook.html
5. Applied Materials GAA inflection page (~$1B per 100k wafer starts) — https://www.appliedmaterials.com/us/en/semiconductor/markets-and-inflections/advanced-logic/gaa.html
6. StockTitan, AMAT deposition + selective-etch systems for angstrom era — https://www.stocktitan.net/news/AMAT/applied-materials-introduces-deposition-systems-for-angstrom-era-7v0938tplllx.html
7. Applied Materials IR, transistor and wiring innovations — https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unveils-transistor-and-wiring-innovations
8. Verified Market Research, Wafer Fab Equipment market ($86.4B 2024) — https://www.verifiedmarketresearch.com/product/wafer-fab-equipment-market/
9. Mordor Intelligence, Semiconductor Etch Equipment market (75% trio, 42% Lam GAA wins, 11 vs 6 plasma steps) — https://www.mordorintelligence.com/industry-reports/semiconductor-etch-equipment-market
10. Lam Research, Selective Etch product family (Argos / Prevos / Selis) — https://www.lamresearch.com/product/selective-etch-product-family/
11. Applied Materials FY2024 Q4 results (47.5% gross, ~29% operating) — https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-fourth-quarter-and-fiscal-year-2024
12. ASM Q4 2024 results (€2.9B revenue, 50.5% gross, 28% operating) — https://www.globenewswire.com/news-release/2025/02/25/3032291/0/en/ASM-announces-fourth-quarter-2024-results.html
13. Yole Group, underappreciated EU semiconductor equipment suppliers — https://www.yolegroup.com/strategy-insights/underappreciated-eu-suppliers-lead-the-semiconductor-equipment-market/
14. Tom's Hardware, TSMC begins volume production of 2nm-class GAA chips — https://www.tomshardware.com/tech-industry/semiconductors/tsmc-begins-quietly-volume-production-of-2nm-class-chips-first-gaa-transistor-for-tsmc-claims-up-to-15-percent-improvement-at-iso-power
15. Semiconductor Engineering, Powering CFETs from the backside (HAR etch, thinning, ~2031 A7) — https://semiengineering.com/powering-cfets-from-the-backside/
16. Tom's Hardware, Intel 18A production starts before TSMC N2 (RibbonFET + PowerVia, A16 end-2026) — https://www.tomshardware.com/pc-components/cpus/intels-18a-production-starts-before-tsmcs-competing-n2-tech-heres-how-the-two-process-nodes-compare
17. SEMI, Global semiconductor equipment sales to reach record $156B in 2027 (foundry/logic $75.2B) — https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports
18. Phemex / Astute Group, TSMC 2nm wafer pricing ~$30k, customer demand, Samsung ~$20k undercut — https://www.astutegroup.com/news/industrial/tsmcs-2nm-wafer-price-hits-30000-amid-monopoly-concerns/
