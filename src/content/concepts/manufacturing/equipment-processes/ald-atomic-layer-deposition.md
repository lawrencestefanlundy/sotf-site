---
type: concept
slug: ald-atomic-layer-deposition
canonical_name: ALD (Atomic Layer Deposition)
aliases:
- ALD
- atomic layer deposition
- PEALD
- spatial ALD
- AS-ALD
- area-selective ALD
kind: technology
parent_concepts:
- manufacturing
- equipment-processes
- deposition
related_concepts:
- chemical-vapor-deposition
- pvd-sputtering
- high-k-dielectrics
- low-k-dielectrics
- ru-w-co-metallisation
- epitaxy
- thin-films-coatings
- semiconductor-equipment
sources:
- '[[2026-02-22-deposition-materials-process-market-companies-that-master]]'
frontier:
- 'Area-selective deposition: inhibitor selectivity is ~1.5nm against a <5nm requirement, and killer-defect metrology is unestablished. Does the strong FSAV version (killing a litho layer) ever leave R&D? (Deposition-theme prediction #1, end-2030.)'
- 'The missing molecule: no material is simultaneously low-k (<6), etch-stop, and selectively depositable; FSAV is gated on it (imec/KU-Leuven, ACS 2023).'
- 'Molybdenum ALD/CVD fill (Lam ALTUS Halo, AMAT Centris Spectral) displacing tungsten: how fast does Mo spread beyond 3D-NAND word lines into logic contacts?'
- 'Throughput vs layer count: GAA and 3D-NAND multiply ALD passes per wafer. Does batch/spatial ALD keep the economics, and who wins the added intensity?'
- 'Does any venture-backed ALD/precursor/inhibitor pure-play raise a real Series A, or does all new chemistry keep exiting to Merck/Air Liquide/Entegris? (Predictions #2/#4/#6 on the theme; none found through Jun 2026.)'
last_updated: '2026-07-31'
tags:
- concept
- technology
mention_count: 7
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-02-22-deposition-materials-process-market-companies-that-master
  title: Companies that master AS-ALD today specifically ASM and AMAT are positioned to dominate the $15B deposition market of the late 2020s
  date: '2026-02-22'
  kind: web
neighbors:
- slug: pvd-sputtering
  name: PVD / Sputtering
  path: /manufacturing/equipment-processes/pvd-sputtering/
  macro: manufacturing
- slug: high-k-dielectrics
  name: High-K Dielectrics (HfO2, ZrO2)
  path: /materials/functional-layers/high-k-dielectrics/
  macro: materials
- slug: low-k-dielectrics
  name: Low-K Dielectrics
  path: /materials/functional-layers/low-k-dielectrics/
  macro: materials
- slug: ru-w-co-metallisation
  name: Ru / W / Co Metallisation
  path: /manufacturing/equipment-processes/ru-w-co-metallisation/
  macro: manufacturing
- slug: thin-films-coatings
  name: Thin Films & Coatings
  path: /materials/advanced-materials/thin-films-coatings/
  macro: materials
- slug: semiconductor-equipment
  name: Semiconductor Equipment
  path: /manufacturing/equipment-processes/semiconductor-equipment/
  macro: manufacturing
---
## Physics / mechanism

ALD deposits material one atomic monolayer at a time via sequential, self-limiting surface reactions. A precursor gas chemisorbs onto the substrate; excess is purged; a co-reactant (oxidant, plasma, or reducing agent) reacts with the chemisorbed layer; excess purged again. One cycle = ~0.1-2 Å growth. The self-limiting nature gives exceptional conformality (>99% step coverage in high-aspect-ratio structures) and sub-Ångström thickness control; the price is throughput (cycle times 0.5-5s), which is the permanent industrial constraint. Variants: thermal ALD, plasma-enhanced (PEALD, lower temperature), spatial ALD (substrate moves through zoned precursor curtains, the throughput answer), batch furnace ALD, and **area-selective ALD** (inhibitor chemistry blocks growth on chosen surfaces, so the film patterns itself). Key materials: Al2O3, HfO2, TiN, ZnO, Ru, and now Mo. Because ALD is CVD chemistry cut into self-limiting half-reactions, it inherits the same precursor constraint: the molecule defines what can be grown, and hydrogen rides in on most C and N precursors (**Chemical Vapor Deposition**).

## The forcing-function precedent (why ALD matters to every deposition thesis)

## Market structure

## Where value is capturable (routing)

The tool oligopoly and the ASD stack (tools + inhibitors + integration) are incumbent-owned: AMAT/Lam/ASM plus imec plus Merck/EMD. Primary route is public equity (ASM.AS is the pure ALD instrument; AMAT, LRCX, 8035.T; materials MRK.DE, AI.PA, ENTG). The only early-stage door any venture route has found is the novel precursor/inhibitor molecule out of an EU lab, as a chemistry-IP-and-exit play; through Jun 2026 repeated searches found no venture-backed ASD/precursor pure-play raising a Series A (theme predictions #2/#6 unfalsified).

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
