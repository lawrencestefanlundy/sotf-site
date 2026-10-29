---
type: concept
slug: flow-epitaxy
canonical_name: Epitaxial deposition (epi) (process step)
seq: 18
phase: wafer
related_concepts:
- mocvd-mbe
- silicon-germanium
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
- slug: mocvd-mbe
  name: MOCVD / MBE
  path: /manufacturing/equipment-processes/mocvd-mbe/
  macro: manufacturing
- slug: silicon-germanium
  name: Silicon Germanium
  path: /materials/substrates/silicon-germanium/
  macro: materials
---
> Step 18 of 56 in the semiconductor flow (Wafer). Prev: [Wafer slicing, lapping & polishing (process step)](/semiconductor-process-flow/wafer-materials/flow-wafer-slicing-polishing/) · Next: [Wafer foundry / fabrication services (process step)](/semiconductor-process-flow/frontend/flow-foundry-fabrication-services/)

## Where it sits and why it matters
Epi is the first place crystal quality becomes a device-yield problem rather than a wafer-supplier problem. A single dislocation or thickness error in the epi layer propagates straight into transistor leakage and breakdown. For advanced logic, SiGe source-drain epi is the lever that has kept Moore's law alive across FinFET and into gate-all-around, so the leading-edge epi tool is a node-enabling chokepoint. For power and RF, the epi layer essentially is the product: a GaN-on-Si or SiC epi wafer is sold as a value-added intermediate at a large multiple of the bare substrate.

## Equipment market
Silicon epi equipment is roughly US$1.5B in 2024, forecast to US$2.5-3.2B by 2030 at a 9-13% CAGR, driven by gate-all-around source-drain, DRAM and advanced packaging [3]. Compound epi splits into two pools: SiC epi equipment is ~US$1.25-1.32B in 2024 growing 15-18% CAGR [1], and MOCVD systems (GaN/GaAs/InP) are a few hundred million per year and cyclical with LED and power demand [2]. Treat the report-mill point estimates as directional; the SEMI/Gartner-style splits are firmer on direction than on the decimal.

| Vendor | HQ | est. share | notable |
|---|---|---|---|
| Applied Materials | US | leads Si epi (historically ~50%+; >50% of GAA epi equipment) | Centura / Epi Prime / Xtera selective epi; node-enabling for 2nm GAA [4][5] |
| ASM International | NL | targets >30% Si epi by 2025 | Intrepid ES/ESA single-wafer epi; acquired LPE (Italy) for SiC CVD [3][6] |
| Aixtron | DE | ~70-75% of MOCVD | compound-semi MOCVD (GaN/GaAs/InP); ~1/3 of SiC CVD; €630M FY24 revenue [2][6] |
| Veeco | US | co-leader MOCVD with Aixtron | Propel GaN-on-Si MOCVD, As/P and LED; ~$630M FY24 revenue [2] |
| Tokyo Electron / Nuflare | JP | minority | Si epi and SiC epi tools |
| AMEC / Naura / JSG | CN | rising in China | state-backed local-substitution challengers in MOCVD and SiC epi [6] |

Concentration note: silicon epi is effectively an Applied-plus-ASM duopoly at the leading edge; MOCVD is an Aixtron-Veeco duopoly (>90% pre-2017, now ~60% of MOCVD with the top three including Taiyo Nippon Sanso) being eroded by Chinese entrants [2][6].

## Materials & consumables
Epi consumes high-purity precursor gases and organometallics on every wafer pass, so this is a genuine recurring-revenue layer rather than a one-off tool sale. Silicon epi runs on chlorosilanes and silane (trichlorosilane TCS, dichlorosilane DCS, silane SiH4, plus dopant hydrides) [7]. Compound epi runs on organometallics (trimethylgallium TMGa, trimethylindium TMIn, trimethylaluminium TMAl) and hydride gases (arsine, phosphine, ammonia); merchant-grade TMGa transacts at ~US$2,500-4,500/kg and TMIn ~US$3,000-6,000/kg in 2026 [7]. Other consumables: SiC-coated graphite susceptors, quartzware, showerheads and filters. Supply concentrates in specialty-gas majors (Linde, Air Liquide, Air Products) as blenders/distributors plus producers like Wacker, Shin-Etsu, SK and Nippon Sanso [7]. The materials pool is smaller than the tool pool but stickier, qualified into each process recipe and switched only with painful requalification.

## Volumes, revenue, profitability
Every advanced-logic and most power/RF wafers see at least one epi step, so unit throughput tracks total wafer starts (high tens of millions of wafers/year industry-wide). The revenue pool is the tool sale (silicon epi ~$1.5B, SiC epi ~$1.3B, MOCVD a few hundred million) plus a recurring precursor/parts annuity. Margins: the equipment makers earn the fattest cut. Applied Materials runs ~47-48% gross and ~29-30% operating margin company-wide; ASM ~50%+ gross; Aixtron historically 40-45% gross but highly cyclical (compound-epi demand swings hard with LED and power capex). Specialty-gas precursors are lower gross (commodity-ish chemistry, ~20-35%) but extremely durable. The margin sits with whoever owns the qualified recipe: the tool vendor at install, the gas major across the tool's life.

## Competitive landscape & value capture
Value capture is bimodal. At the leading edge, silicon/SiGe epi is a two-horse race (Applied, ASM) protected by a deep moat: the tool must hit angstrom-scale thickness and defect targets co-developed with the foundry over years, so switching is near-impossible mid-node. In compound epi, Aixtron and Veeco hold a structural MOCVD duopoly, but it is the most contestable of the deposition niches because Chinese local-substitution (AMEC, Naura, JSG) is funded to break it. The other place value accrues is merchant epi wafers: houses like IQE (Wales) sell finished GaN/GaAs/InP epi wafers, capturing the layer's value without owning a fab.

## Market drivers, constraints & trends
Net read is two engines on different clocks: the leading-edge silicon/SiGe epi pool is accelerating, while compound (SiC) epi is in a cyclical trough through ~2027-2028, so the blended served market grows but is lumpy.
- **Drivers** — GAA at 2nm makes epi step-intensive: the shift to gate-all-around at 2nm and below lifts demand for single-wafer Si epi and high-Ge SiGe selective source-drain, the lever keeping leading-edge logic moving [8][9]. HBM is a wafer-intensity multiplier: HBM consumes ~3x the wafer capacity per GB of DDR5 and reached ~23% of DRAM wafers in 2026, with HBM4 (16-die) volume in late 2026/2027, pulling more epi-bearing wafer starts [10]. Data-centre power: the GaN device market is forecast to grow ~35-42% CAGR to ~$2.5-2.9B by 2030 as AI power-supply demand hits the "power wall," all of it MOCVD epi-borne [11].
- **Constraints** — SiC epi is the drag: upstream SiC utilisation fell to ~50% in 2025 (devices ~70%), overcapacity persists to 2027-2028, and SiC equipment is forecast at roughly -7% to -11% CAGR through 2030 [12]. China local-substitution caps Western share: Chinese players held ~40% of SiC wafer/epiwafer capacity by 2024 and back local equipment buys, eroding the Aixtron-ASM-Veeco hold on compound epi [12]. Capex cyclicality: compound-epi (MOCVD) demand still swings hard with LED, EV and power capex.
- **Trends & inflections to watch** — 3D DRAM is the next epi bonanza: it needs 100+ Si/SiGe superlattice bilayers per stack (IMEC has shown up to ~120-300 layers on 300mm), but mass production is ~2032-2035, so the datable tripwire is a memory maker placing its first high-volume superlattice-epi tool order [13]. GaN-on-Si 200mm to 300mm transition (300mm projected >80% of GaN demand by 2030); tripwire = a second Propel300-class 300mm GaN MOCVD order from a power IDM after Veeco's Nov 2025 win [11][14]. SiC recovery tripwire = upstream utilisation back above ~80% plus 8-inch platform ramp signalling the 2027-2028 turn [12].

## Connections
- [MOCVD / MBE](/manufacturing/equipment-processes/mocvd-mbe/) - the compound-epi growth techniques (MOCVD, MBE) that this step uses for GaN/GaAs/InP/SiC.
- [Silicon Germanium](/materials/substrates/silicon-germanium/) - the SiGe / strained-Si epi that enables advanced-logic source-drain.
- **Gan On Si Substrate Epi** - thesis on GaN-on-Si epi wafers as the value-added intermediate for power.
- [Wafer slicing, lapping & polishing (process step)](/semiconductor-process-flow/wafer-materials/flow-wafer-slicing-polishing/) - prior step that delivers the polished substrate epi grows on.
- [Wafer foundry / fabrication services (process step)](/semiconductor-process-flow/frontend/flow-foundry-fabrication-services/) - next step, where the epi wafer enters device fabrication.