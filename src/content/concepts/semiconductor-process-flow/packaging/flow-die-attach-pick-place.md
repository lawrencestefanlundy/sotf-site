---
type: concept
slug: flow-die-attach-pick-place
canonical_name: Die attach / pick-and-place (process step)
seq: 43
phase: assembly
related_concepts:
- bonding-dicing-equipment
created: 2026-06-20
last_updated: 2026-06-20
tags:
- concept
- process-flow
- semiconductor
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2026-03-10-fungible-compute-mortal-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
mention_count: 10
parent_concepts:
- packaging
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-03-10-fungible-compute-mortal-computing
  title: Fungible Compute, Mortal Computing and Why the IoT won't use Silicon
  date: '2026-03-10'
  kind: substack
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-09-10-uk-opportunity-in-ai-compound-semiconductors
  title: 'UK Opportunity in AI: Compound Semiconductors'
  date: '2025-09-10'
  kind: substack
neighbors:
- slug: bonding-dicing-equipment
  name: Bonding & Dicing Equipment
  path: /manufacturing/equipment-processes/bonding-dicing-equipment/
  macro: manufacturing
---
> Step 43 of 56 in the semiconductor flow (Assembly). Prev: [Wafer dicing / singulation (process step)](/semiconductor-process-flow/packaging/flow-wafer-dicing-singulation/) · Next: [Wire bonding (process step)](/semiconductor-process-flow/packaging/flow-wire-bonding/)

## What this step does
After the wafer is singulated into individual dies, a die bonder picks each known-good die off the diced tape and places it onto a substrate, leadframe, or another die, then fixes it in place with an adhesive that is cured. This is the gateway from wafer-level work into package assembly, and it sets the placement accuracy budget for everything downstream. The sub-processes inside the step:
- Pick: a collet or ejector lifts the die off the dicing tape without cracking it (thinned dies are fragile).
- Align and place: machine vision registers the die and the bond site; the head places to a target accuracy (microns for standard work, sub-micron for advanced).
- Attach: apply die-attach paste or pre-applied die-attach film (DAF), then thermal or UV cure; high-end flows use thermo-compression bonding (TCB) or, at the frontier, hybrid bonding (no adhesive, direct copper-to-copper plus oxide).

## Equipment market
Core die-bonder equipment is roughly a USD 1.0-1.5B annual market, growing low-to-mid single digits in the mainstream tier but far faster (20%+ CAGR) in the TCB/hybrid-bonding frontier [1][6]. Treat the wide report-mill range ($0.98B to $4.8B for "die bonder equipment") as noise from inconsistent scope definitions; the conservative ~$1B figure for classic die bonders is the defensible anchor [1][6]. Hybrid-bonding equipment alone is ~$165M in 2025 heading toward ~$600M+ by 2030-2032 at >20% CAGR [4].

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| Besi (BE Semiconductor) | Netherlands | ~24-39% (scope-dependent) | Hybrid-bonding leader; 63% gross margin; AI/2.5D order surge [2][6] |
| ASMPT | Singapore / Hong Kong | ~20% | TCB + high-end die bonders; AP revenue $532M, +30% YoY [3] |
| Kulicke & Soffa | US / Singapore | mid-single % in die attach | Wire-bond leader pivoting into TCB for advanced packaging [3] |
| Shinkawa (Yamaha) | Japan | niche/high-precision | Acquired by Yamaha Motor; precision and flip-chip [6] |
| Fasford, Toray Eng., Panasonic | Japan | niche each | Mechanical robustness, automotive 20-yr tool life [6] |

Concentration note: a tight oligopoly. Besi and ASMPT capture the bulk of the value, with Besi dominant in the hybrid-bonding frontier and ASMPT leading TCB. European exposure is unusually strong here (Besi is Dutch), a rarity in back-end equipment.

## Materials & consumables
The step consumes die-attach paste (silver-filled epoxy or sinter paste for power/thermal), die-attach film (DAF), and increasingly dicing-die-attach film (DDF, a two-in-one tape that serves both singulation and bonding). The die-attach materials market is roughly $2.0-2.5B in 2025 at ~5.5-8% CAGR; the DDF film slice alone is ~$2.3B in 2025 heading to ~$4.4B by 2034 at ~7.3% CAGR [5][7][8]. Vendors: Henkel (Loctite, ~18-20% of die-attach materials) leads; Resonac (ex-Hitachi Chemical), Nitto Denko, Dexerials and Lintec together hold ~52-58% [5]. Recurring-revenue note: unlike the lumpy capex of die bonders, materials are a per-wafer consumable that scales with production volume, so this is the stickier, more annuity-like layer of the step.

## Volumes, revenue, profitability
Volumes scale with die count, not wafer count: a single advanced package can stack 8-12+ HBM dies, and chiplet packages place many dies per substrate, so die-placement operations run into the trillions per year industry-wide. The combined revenue pool for the step (equipment + materials) is roughly $3-4B/yr. Profitability splits sharply: Besi posted 2025 gross margin of 63.3% and operating margin of 29.3% on EUR 591M revenue, the kind of margin that signals a frontier-tool monopoly-ish position [2]. ASMPT, weighted toward mainstream plus TCB, runs leaner at ~38% gross margin [3]. Materials vendors (Henkel, Resonac) earn typical specialty-chemical margins, lower headline gross than frontier equipment but with the annuity quality. The margin accrues to the firm holding the accuracy frontier: hybrid bonding for Besi, TCB for ASMPT and K&S.

## Connections
[Bonding & Dicing Equipment](/manufacturing/equipment-processes/bonding-dicing-equipment/)

- Owning idea: **Legacy Assembly Commoditised** (commodity assembly (recorded pass)).