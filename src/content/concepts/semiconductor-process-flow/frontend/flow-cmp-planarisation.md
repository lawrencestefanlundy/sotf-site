---
type: concept
slug: flow-cmp-planarisation
canonical_name: Chemical-mechanical planarisation (CMP) (process step)
seq: 30
phase: feol
related_concepts:
- cmp-chemical-mechanical-planarisation
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
- slug: cmp-chemical-mechanical-planarisation
  name: Chemical Mechanical Planarisation
  path: /manufacturing/equipment-processes/cmp-chemical-mechanical-planarisation/
  macro: manufacturing
---
> Step 30 of 56 in the semiconductor flow (FEOL). Prev: [PVD / sputtering (process step)](/semiconductor-process-flow/frontend/flow-pvd-sputtering/) · Next: [Transistor module (FinFET / GAA nanosheet) (process step)](/semiconductor-process-flow/frontend/flow-transistor-module-finfet-gaa/)

## What this step does
CMP grinds the wafer surface flat by pressing it against a rotating polymer pad while a chemically reactive abrasive slurry flows between the two. It combines chemistry (the slurry etches/softens the top film) and mechanics (the pad and abrasive shear it away), removing excess material and leaving a near-atomically flat surface so the next lithography layer can focus. Sub-processes inside one CMP module:
- **Polishing** — wafer on a carrier head, downforce against the pad, slurry feed; the actual planarisation.
- **Pad conditioning** — a diamond disc roughens the pad in-situ to keep removal rate stable as the pad glazes.
- **Endpoint detection** — optical/eddy-current/motor-current sensing to stop at the target thickness.
- **Post-CMP clean** — brush/megasonic scrub to strip slurry particles and metal residue before the next step.

## Where it sits and why it matters
CMP is run dozens of times across a leading-edge flow: after each oxide/dielectric fill (STI, ILD), after every metal layer (tungsten, copper, cobalt) in damascene interconnect, and increasingly for advanced packaging hybrid bonding where sub-nanometre flatness gates the bond. Without CMP there is no multi-layer interconnect and no GAA stacking. It is one of the highest consumables-intensity steps in the fab: the tool is a one-time capital purchase, but every wafer pass burns slurry and wears the pad, so the value pool is heavily recurring rather than equipment-led.

## Equipment market
Tool market ~$3.2B in 2024, with most syndicated forecasts at ~5-6% CAGR for the CMP-specific equipment line and the broader "CMP machine" segment quoted higher (~12% CAGR, treat as report-mill optimism) [1][7]. This is a near-duopoly:

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Applied Materials | US | ~70% | Reflexion / Reflexion LK platform; dominant at every leading-edge foundry and memory maker [3][6] |
| Ebara | Japan | ~25% | F-REX300 family; F-REX300XA (Oct 2024) targets hybrid-bonding HVM; strong in Japan/Korea [1][6] |
| Onto Innovation / HWatec / NAURA | US / Korea / China | ~5% combined | NAURA is the China-localisation play [6] |

Concentration note: AMAT + Ebara hold >90% of CMP tools, one of the most concentrated WFE niches outside litho. China localisation (NAURA, HWatec) is the only structural threat, and it is at trailing nodes.

## Materials & consumables
This is where the durable money sits. Each wafer pass consumes **slurry** (colloidal silica or ceria abrasive plus oxidisers/chelators, tuned per film: oxide, tungsten, copper, cobalt, barrier) and wears the **polishing pad** (cast polyurethane). Plus conditioner discs, brushes and post-CMP clean chemistries. Combined CMP slurry + pad consumables market ~$3.3-3.4B in 2025, ~4.5% CAGR [2], of which slurry alone is ~$2.9B in 2024 [4].

- **Slurry** — top five (Entegris/CMC Materials, Fujimi, DuPont, AGC, Resonac) hold ~65-70% of revenue; Fujimi alone est. ~18% [2][4]. Versum/Merck KGaA also present.
- **Pads** — DuPont (now spinning electronics into **Qnity**) held ~80% in 2021; top three ~82% [5]. Cabot/CMC, Thomas West, Fujibo, JSR fill the tail.

Recurring-revenue note: slurry and pads are qualified per-film, per-customer and locked in for years (e.g. the 2025 Qnity-SK hynix long-term pad supply agreement [5]), so this is razor-and-blades attached to an installed tool base.

## Volumes, revenue, profitability
A leading-edge logic wafer sees ~15-30+ CMP steps; each consumes slurry and incrementally wears the pad, so consumables scale with wafer-passes, not just wafer-starts. Revenue pool split: ~$3.2B equipment (largely one-time, AMAT-captured) versus ~$3.3-3.4B annually recurring consumables. Margins: AMAT-class equipment runs ~47-48% gross / ~30%+ operating at the corporate level; consumables houses (Entegris, post-CMC) run roughly 40-45% gross with materials science as the moat. The durable, compounding margin is in qualified consumables, not the box.

## Competitive landscape & value capture
Moat is qualification lock-in on both axes: AMAT owns the tool, DuPont owns the pad, a five-firm club owns the slurry. Once a slurry/pad is qualified into a node it rarely changes, so incumbents compound. Value accrues to the consumables layer (recurring, high-switching-cost) and secondarily to AMAT (installed-base control). EU exposure is thin: Merck KGaA / Versum (Germany) in slurry chemistries and AGC's European footprint; no leading-edge EU tool or pad maker. Seed-stage angle is narrow but real on the materials side (ceria abrasive engineering, defect-reducing slurry chemistry, sub-nm hybrid-bonding CMP) where a novel particle or formulation can win a single high-value qualification.

## Market drivers, constraints & trends
Net read: this is one of the better structurally-growing consumables pools in WFE, because every architecture shift on the roadmap adds CMP steps rather than removing them. TECHCET/Semiconductor Digest put CMP consumables at ~$3.6B in 2025 (+6% YoY) on a ~9% CAGR through 2029, faster than the equipment line [8].

- **Drivers**
  - Step-count compounding is the core engine: sub-7nm logic now runs 30-40 CMP steps per wafer vs 15-20 at 28nm, with steps rising ~20-30% per node generation as metal layers and multi-patterning multiply [9][10].
  - Three roadmap shifts each bolt on net-new CMP: 3D NAND scaling toward >1,000 layers, GAA nanosheet release/isolation, and backside power delivery (which needs aggressive wafer thinning from >700um to 1-3um then fine CMP) [8][11].
  - Advanced packaging is the second leg: NVIDIA Blackwell interposers use ~14 CMP steps per package (2x the prior generation), and SK hynix is reportedly adding ~36 CMP tools by 2027 for HBM, with hybrid bonding demanding sub-1um co-planarity [7].

- **Constraints**
  - Cerium-oxide chokepoint: China controls ~70% of ceria extraction/refining; 2025 export quotas lifted ceria prices ~34% YoY, squeezing slurry-maker margins even after ~7% list-price rises [7]. Colloidal-silica substitution cuts oxide removal rates up to ~30%, so it is not a clean swap [7].
  - WFE cyclicality and capex pauses still gate the equipment leg; consumables are stickier but track wafer-passes, which fall in a memory downturn.
  - Qualification lock-in cuts both ways: hard for incumbents to lose, but also hard for a new abrasive/formulation to displace, capping how fast the materials pool re-prices.

- **Trends & inflections to watch**
  - Backside power going to HVM is the biggest single step-count event. Tripwire: TSMC A16 (GAA + backside power) reaching volume in H2 2026, Intel 18A/PowerVia already in production, Samsung 2027 [11].
  - Cerium-free / low-ceria chemistries. Tripwire: DuPont's ~$45M cerium-free program hitting its 2027 launch, or Entegris's $200M Kulim (Malaysia) slurry plant (Jan 2026, +35% regional capacity) re-localising supply [7].
  - Hybrid-bonding CMP as a distinct premium tier. Tripwire: Ebara F-REX300XA-class hybrid-bonding tools and packaging-tuned slurries (Fujifilm launched one Sep 2025) winning OSAT qualifications, the fastest-growing CMP sub-segment [7].

## Connections
- [Chemical Mechanical Planarisation](/manufacturing/equipment-processes/cmp-chemical-mechanical-planarisation/) — the underlying process/technique concept page
- **Deposition Materials Process Market** — thesis on where value accrues across deposition + planarisation materials

## Sources
1. Technavio, CMP Equipment Market 2025-2029 ($757.3M growth, 5.4% CAGR; Ebara F-REX300XA Oct 2024) — https://newsroom.technavio.org/cmp-equipment-market-industry-analysis
2. Marketgrowthreports / WICZ, Global CMP Slurry and Pads Market (~$3.38B 2025, 4.5% CAGR; top players) — https://www.wicz.com/story/52144206/global-cmp-slurry-and-pads-market-size-20252032-applications-growth-opportunities-and-trend-analysis
3. SemiconductorX, WFE CMP (AMAT ~70%, Ebara ~25%, Reflexion / F-REX) — https://semiconductorx.com/wfe-cmp.php
4. Valuates / CMP Slurry market ($2,905M 2024; top-five ~65-70% incl. CMC/Entegris, Fujimi, DuPont, AGC, Resonac) — https://reports.valuates.com/market-reports/QYRE-Auto-32B8990/global-cmp-slurry
5. DuPont, Qnity-SK hynix CMP pad supply agreement (DuPont ~80% pads 2021; spinout to Qnity) — https://www.dupont.com/news/qnity-and-sk-kynix-sign-long-term-cmp-pad-supply-agreement.html
6. Cognitive Market Research, Semiconductor CMP Equipment (AMAT ~70%, Ebara ~25%, NAURA/HWatec tail) — https://www.cognitivemarketresearch.com/semiconductor-cmp-equipment-market-report
7. Market.us, Chemical Mechanical Planarization Market ($6.1B 2024 → $13.0B 2034, 7.9% CAGR; NVIDIA Blackwell ~14 CMP steps/package 2x prior gen; SK hynix ~36 CMP tools by 2027 for HBM; cerium ~70% China control + 2025 export quotas lifting ceria ~34% YoY; colloidal-silica substitution cuts removal ~30%; Entegris $200M Kulim Malaysia plant Jan 2026 +35% capacity; DuPont $45M cerium-free 2027 launch; Fujifilm packaging slurry Sep 2025; OSAT 9.45% CAGR) — https://market.us/report/chemical-mechanical-planarization-market/
8. Semiconductor Digest / TECHCET, The Future of CMP: More Process Steps, More Growth Ahead (CMP consumables ~$3.6B 2025 +6% YoY, ~9% CAGR 2024-2029; 3D NAND >1,000 layers, GAA, backside power adding steps; FOWLP/3D TSV/hybrid bonding) — https://www.semiconductor-digest.com/the-future-of-cmp-more-process-steps-more-growth-ahead/
9. IndexBox, CMP Abrasive Particle Market (sub-7nm logic 30-40 CMP steps/wafer vs 15-20 at 28nm) — https://www.indexbox.io/blog/cmp-abrasive-particle-market-forecast-points-higher-toward-2035-on-advanced-node-demand/
10. IndexBox, Slurry Additive Package Market (CMP steps/wafer rising ~20-30% per node generation; sub-10nm complexity) — https://www.indexbox.io/blog/slurry-additive-package-market-forecast-points-higher-toward-2035-driven-by-advanced-cmp-requirements-in-sub-10nm-nodes/
11. Semiconductor Engineering, Backside Power Delivery Gears Up For 2nm Devices (wafer thinned >700um to 1-3um then CMP; TSMC A16 GAA+backside power H2 2026, Intel 18A/PowerVia in production, Samsung 2027) — https://semiengineering.com/backside-power-delivery-gears-up-for-2nm-devices/
