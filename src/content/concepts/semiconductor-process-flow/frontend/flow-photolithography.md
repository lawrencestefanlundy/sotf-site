---
type: concept
slug: flow-photolithography
canonical_name: Photolithography (coat / expose / develop) (process step)
seq: 22
phase: feol
related_concepts:
- lithography
- duv-immersion-lithography
- high-na-euv-lithography
- euv-light-sources
- photoresists
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
- slug: lithography
  name: Lithography
  path: /manufacturing/lithography/lithography/
  macro: manufacturing
- slug: duv-immersion-lithography
  name: DUV / Immersion Lithography
  path: /manufacturing/lithography/duv-immersion-lithography/
  macro: manufacturing
- slug: high-na-euv-lithography
  name: High-NA EUV Lithography
  path: /manufacturing/lithography/high-na-euv-lithography/
  macro: manufacturing
- slug: euv-light-sources
  name: EUV Light Sources
  path: /manufacturing/lithography/euv-light-sources/
  macro: manufacturing
- slug: photoresists
  name: Photoresists (incl. EUV resists)
  path: /manufacturing/lithography/photoresists/
  macro: manufacturing
---
> Step 22 of 56 in the semiconductor flow (FEOL). Prev: [Thermal oxidation & gate dielectric (process step)](/semiconductor-process-flow/frontend/flow-thermal-oxidation-gate-dielectric/) · Next: [Plasma / dry etch (process step)](/semiconductor-process-flow/frontend/flow-plasma-dry-etch/)

## What this step does
Photolithography prints the circuit pattern from the mask onto the wafer. A light-sensitive polymer (photoresist) is spun onto the wafer, exposed to patterned light through the mask, and developed away to leave a resist stencil that protects some areas and exposes others for the etch or implant that follows. It is the single most-repeated and most-expensive step in the fab, run dozens of times per wafer, and it sets the minimum feature size of the whole chip. Sub-processes inside it:
- Coat: spin a uniform resist film (and anti-reflective and adhesion layers) onto the wafer on a track.
- Soft bake / dehydration: drive off solvent and stabilise the film.
- Expose: project the mask image onto the resist with a scanner (DUV, EUV, or i-line stepper).
- Post-exposure bake: drive the acid-catalysed chemistry that sharpens the latent image.
- Develop: dissolve the exposed (or unexposed) resist to reveal the pattern, then rinse and hard bake.
- Inspect / overlay metrology: confirm the printed pattern aligns to the layers beneath before committing to etch.

## Where it sits and why it matters
Litho is the heartbeat of the fab. Every patterned layer (transistor gates, contacts, all the metal levels) needs at least one litho pass, and a leading-edge logic chip may see 80 or more. Because it defines the smallest printable feature, litho is the gate on Moore's law: each node shrink is, at root, a litho-resolution problem. It is also the biggest single line in fab capex, which is why one supplier controlling the leading-edge tool is the most consequential chokepoint in the entire semiconductor economy. The previous step lays the gate dielectric down; this step decides where the gate actually goes; the next step ([Plasma / dry etch (process step)](/semiconductor-process-flow/frontend/flow-plasma-dry-etch/)) transfers the resist pattern into the film beneath.

## Equipment market
The lithography (scanner/stepper) equipment market is the largest single equipment pool in the fab, roughly US$25.8B in 2024 by one estimate and projected near US$46B in 2025 on the EUV ramp, growing ~8-9% CAGR through the early 2030s [1][2]. Treat the level estimates as directional (report-mill numbers diverge widely); the structure is firmer than the decimal. The defining fact is ASML's near-monopoly.

| Vendor | HQ | est. share | notable |
|---|---|---|---|
| ASML | NL | ~94% of litho equipment revenue [2] | sole EUV maker; recognised 44 EUV + 374 DUV systems in 2024; €28.3B group revenue, 51.3% gross margin [3] |
| Canon | JP | ~3-4% revenue; ~33% of units (2024) [2] | i-line/KrF steppers for mature nodes; nanoimprint (NIL) as an EUV-alternative bet |
| Nikon | JP | ~2.5% revenue; ~5% of units (2024) [2] | ArF/KrF DUV scanners; retreated from EUV; niche/mature only |
| SUSS MicroTec | DE | small | mask aligners, advanced-packaging litho, coaters |
| EV Group | AT | small | mask aligners, nanoimprint, wafer bonding for packaging |

Concentration note: this is the most concentrated layer in the whole flow. ASML holds ~94% of revenue and 100% of EUV; for DUV immersion (the tool that prints sub-40nm without EUV) ASML ships >85% of units [2]. Canon and Nikon survive only in cost-sensitive mature-node DUV and steppers, where Canon's unit share has actually risen (mature-node and China demand) even as its revenue share stays small. There is no second EUV supplier, and none is plausible this decade.

## Materials & consumables
The recurring-revenue layer is photoresist plus the wet chemicals around it (developers, anti-reflective coatings, edge-bead removers, rinses), all consumed on every wafer pass. The photoresist market was ~US$5.1-5.5B in 2024; the EUV-resist sub-segment alone was ~US$1.5B and is the fastest-growing slice (~11% CAGR) [4][5]. This is a Japan-dominated oligopoly: JSR led with >22% share in 2024, and the top five (JSR, Tokyo Ohka Kogyo, Fujifilm, Shin-Etsu, Dongjin Semichem) held ~50% [4]. JSR and TOK in particular co-developed the EUV-resist chemistry and dominate that high-value tip [5]. The other big consumable is the coater/developer track that physically applies and develops the resist: a ~US$1.2B equipment market that Tokyo Electron owns at ~90-92% share, and effectively 100% for High-NA EUV tracks [6]. Resist and track are qualified into each process recipe, switched only with painful requalification, so the revenue is sticky annuity income rather than one-off.

## Volumes, revenue, profitability
Every patterned layer on every wafer is a litho pass, so unit throughput tracks total wafer starts multiplied by layer count (tens of millions of wafers/year, each seeing dozens of exposures). The revenue pool splits across three tiers, all profitable: the scanner (one EUV tool earns ASML ~US$180-220M; a High-NA EXE machine ~US$380M; ASML books ~€28B/yr at 51% gross margin and is guiding to 56-60% gross by 2030) [3][7]; the coater/developer track (~US$1.2B/yr, Tokyo Electron near-monopoly) [6]; and the resist/chemistry annuity (~US$5B/yr) [4]. The fattest margin sits with ASML: a hardware monopoly with a long service tail (~20% of revenue is service and field upgrades) and gross margins that rival software [3]. Tokyo Electron and the resist majors earn healthy but lower margins; ASML is the value sink of the step and arguably of the whole industry.

## Market drivers, constraints & trends
Net read: the served market is accelerating into the early 2030s, pulled by AI-driven EUV intensity, but with the cyclical, China-exposed DUV base softening underneath it.

- **Drivers**
 - EUV intensity per node keeps climbing: ~5-10 EUV layers at 7nm rising to 15-20 at 3nm and 25+ projected at 2nm, so each node shrink multiplies exposures even at flat wafer volume [9]. ASML raised 2026 guidance to EUR36-40B on AI demand and plans 60 low-NA EUV shipments in 2026 (25% more than 2025), 80 in 2027 [10].
 - EUV is moving into DRAM, not just logic: memory took 51% of ASML system sales, and SK Hynix and Micron are ramping EUV at the 1-delta/1c node on HBM-driven demand [11][12]. HBM grew ~130% in 2025 and is guided ~70% in 2026 [13].
 - Advanced-packaging litho is a second, faster pool: ~US$8.5B (2024) toward ~US$15.4B (2033), ~7.4% CAGR, with panel-level packaging on a ~38% decade CAGR off a small base [13].

- **Constraints**
 - China DUV is the soft underbelly: Chinese buyers were ~70% of DUV-immersion unit sales in 2024, and tighter US/MATCH-Act controls guide China to ~20% of 2026 sales, diluting gross margin toward 51-53% from the China-boom 55%+ [14][15].
 - High-NA adoption is slower than the EUR380M tool implies: only Intel has a commercial EXE in production; TSMC is bypassing High-NA for A14, capping near-term EXE volume [16][17].
 - The pool is capex-cyclical and single-supplier; a memory or AI-capex pause hits exposures directly.

- **Trends & inflections to watch**
 - Dry resist (Lam, ALD vapour-deposited) could displace Tokyo Electron's coater near-monopoly and the spin-on resist annuity. Tripwire: a foundry/DRAM maker qualifying dry resist into a production critical-layer recipe (Intel/Samsung/TSMC/SK Hynix engagements live) [18].
 - High-NA crossing into volume. Tripwire: a second commercial EXE node beyond Intel 14A entering HVM, or TSMC reversing its A14 bypass [16][17].
 - DRAM EUV step-up. Tripwire: Micron 1-gamma or SK Hynix moving multiple DRAM layers to High-NA EUV [11][12].

## Connections
- [Lithography](/manufacturing/lithography/lithography/) - the parent technique this step instantiates.
- [DUV / Immersion Lithography](/manufacturing/lithography/duv-immersion-lithography/) - the water-immersion DUV that prints sub-40nm and remains the workhorse below EUV.
- [High-NA EUV Lithography](/manufacturing/lithography/high-na-euv-lithography/) - the next-generation 0.55-NA EUV (ASML EXE) for sub-2nm.
- [EUV Light Sources](/manufacturing/lithography/euv-light-sources/) - the tin-plasma 13.5nm source (Cymer/ASML, Trumpf laser) that makes EUV possible.
- [Photoresists (incl. EUV resists)](/manufacturing/lithography/photoresists/) - the light-sensitive films this step coats, exposes and develops.
- **Lithography Patterning Market** - thesis on the patterning equipment + materials pool.
- **High Na Euv** - thesis on the High-NA EUV transition.
- **Litho Light Source Supply** - thesis on the EUV source / supply-chain chokepoint.
- [Thermal oxidation & gate dielectric (process step)](/semiconductor-process-flow/frontend/flow-thermal-oxidation-gate-dielectric/) - prior step, the gate dielectric this layer patterns over.
- [Plasma / dry etch (process step)](/semiconductor-process-flow/frontend/flow-plasma-dry-etch/) - next step, which transfers the resist pattern into the film.