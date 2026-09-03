---
type: concept
slug: flow-ion-implantation
canonical_name: Ion implantation (doping) (process step)
seq: 25
phase: feol
related_concepts:
- ion-implantation
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
sources_7d: 1
sources_30d: 2
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
- slug: ion-implantation
  name: Ion Implantation
  path: /manufacturing/equipment-processes/ion-implantation/
  macro: manufacturing
---
> Step 25 of 56 in the semiconductor flow (FEOL). Prev: [Wet etch / chemical surface prep (process step)](/semiconductor-process-flow/frontend/flow-wet-etch-surface-prep/) · Next: [Annealing / rapid thermal processing (process step)](/semiconductor-process-flow/frontend/flow-annealing-rtp/)

## What this step does

Ion implantation is how the electrical character of silicon gets written. Dopant atoms (boron, phosphorus, arsenic, and others) are ionised, accelerated to a chosen energy, and fired into the wafer to create the n-type and p-type regions that make a transistor work. The energy sets how deep the dopant goes; the beam current and dose set how many atoms arrive. The implanted lattice is left damaged and the dopant sits in the wrong (interstitial) sites, which is why the very next step, [Annealing / rapid thermal processing (process step)](/semiconductor-process-flow/frontend/flow-annealing-rtp/), heals the crystal and activates the dopant. Sub-processes inside this step:

- Ion generation in a source from a dopant gas (BF3, PH3, AsH3 and similar)
- Mass analysis and beam-line selection of the wanted ion species
- Acceleration to the target energy (low / medium / high)
- Beam scanning and wafer handling to hit dose uniformity across 300mm
- Dose metrology and angle control (channeling avoidance)

## Where it sits and why it matters

This is a defining FEOL step: a modern logic flow runs dozens of separate implant steps (well, channel, source/drain extension, halo, threshold-voltage adjust), each a distinct masked recipe. It is one of the few "additive" doping routes that places a precise number of atoms at a precise depth, which is why it has no real alternative for source/drain and well formation. It also sits at the centre of the power-device build (SiC and IGBTs lean on implant far more heavily than logic), which is the fastest-growing demand pocket.

## Equipment market

The implanter equipment market is roughly **$3.5B in 2024** counting systems plus aftermarket services; the systems-only pool is closer to $2.5-3B. Report-mill estimates scatter widely ($1.5B to $4B+) because of scope (machine-only vs. with services) and timing of the 2024 memory/logic downturn, so treat any single TAM as soft. SkyQuest puts the implanter market at ~$3.51B in 2024 growing to ~$4.99B by 2032 at ~4.5% CAGR; other sources claim 7-10%. The honest read: a low-to-mid-single-digit base CAGR for the mature logic/memory base, with SiC power as the high-growth overlay.

| Vendor | HQ | Est. share (2024) | Notable |
|---|---|---|---|
| Applied Materials | US | ~60-63% | Dominant across all current segments; sold ~686 systems in 2024 (per QYResearch) |
| Axcelis Technologies | US | ~21% | Purion platform; pure-play implant (98% of revenue); SiC power leader |
| Sumitomo Heavy / Nissin Ion | Japan | ~12-15% | Strong Asia presence; ~90% of Japan SiC implanters, ~40% overseas |
| Advanced Ion Beam Tech (AIBT) | Taiwan | low single digit | Niche / regional; China-facing |
| Hitachi High-Tech | Japan | low single digit | Smaller line, specialty |

Concentration note: this is effectively an AMAT-led duopoly with AMAT plus Axcelis taking ~80-85% of systems, and the top three above 90%. High barriers (beam-line physics, contamination control, 20+ year installed-base service relationships) keep new entrants out. Shares cited are 2024 estimates and move with the cycle.

## Materials & consumables

Implant consumes specialty **dopant gases** (boron trifluoride BF3, phosphine PH3, arsine AsH3, plus diborane and germanium/carbon sources for advanced steps) and beam-line consumables (graphite/tungsten source parts, repellers, vacuum and abatement hardware). Dopant gases are a small, strategically vital slice of the ~$3B+ electronic specialty gas market; electronic-grade BF3 alone is roughly $200M in 2024 (mid-single-digit CAGR). Vendors:

| Vendor | HQ | Notable |
|---|---|---|
| Merck KGaA / EMD Electronics | Germany | ION-X sub-atmospheric MOF dopant delivery (BF3, PH3, AsH3) |
| Air Liquide | France | Diborane, phosphine, arsine; broad electronics gases |
| Air Products | US | Industrial + electronic specialty gases |
| Linde | UK/Germany | Electronic gases incl. dopants |
| SIAD | Italy | Dopant gas supplier |

Recurring-revenue note: gases and source parts are a steady aftermarket consumable, and the OEM aftermarket (service, spares, upgrades) is itself sticky. Axcelis CS&I aftermarket was $235.3M, 23.1% of 2024 revenue. The implant aftermarket overlaps with the **Deposition Materials Process Market** specialty-materials pool but is a smaller, more concentrated gas niche.

## Volumes, revenue, profitability

Axcelis is the clean public proxy: **$1,017.9M revenue in 2024**, ~98% from implant, at **44.7% gross margin** and **20.7% operating margin** (down from 23.5% in 2023 on the downcycle). AMAT does not break out implant, but at ~3x Axcelis's share its implant line is plausibly ~$1.5-2B. So the system+service revenue pool sits around $3.5B. Power devices were 56% of Axcelis 2024 system-shipment value, and Asia was 81% of system revenue. The margin is earned by the equipment OEMs (high-40s gross, ~20% operating at trough, higher at peak) and by the gas majors on the consumable; the value capture is overwhelmingly at the tool layer.

## Competitive landscape & value capture

The moat is classic capital-equipment: beam physics know-how, a 20+ year qualified installed base, and service lock-in. Value accrues to two OEMs (AMAT, Axcelis) and a handful of specialty-gas majors. The interesting frontier is **SiC / wide-bandgap power**, which is implant-intensive (high-temperature, high-dose, high-energy recipes) and where Axcelis (Purion Power Series+) and Nissin lead. No credible EU or seed-stage tool challenger exists at the system level; barriers are too high. The European exposure is on the **materials** side (Merck/EMD, Air Liquide, Linde) and on the SiC device pull-through (EU automotive/power).

## Market drivers, constraints & trends

Net read: a cyclical trough now, with two structural pulls (advanced-logic implant-step growth, wide-bandgap power) setting up a faster recovery from ~2027 than the flat ~4.5% base CAGR implies.

- **Drivers**
 - Implant-step count keeps climbing: a modern CMOS IC with embedded memory now needs up to ~60 implants, and GAA nanosheet nodes add new recipes (super-steep retrograde wells, channel/halo tuning) on top of the FinFET set, so the per-wafer implant intensity rises even before wafer-starts grow [10][11].
 - Wide-bandgap power is the high-growth overlay: SiC device revenue is forecast toward ~$10B by 2030 (~19-27% CAGR), and SiC/GaN are far more implant-intensive (high-energy, high-dose, hot recipes) than logic [12].
 - Consolidation re-rates the tool layer: the Axcelis-Veeco all-stock merger (announced Oct 2025, ~$4.4B EV, close 2026) expands the combined served market to over $5B by pairing implant with laser anneal, IBD and GaN/SiC MOCVD epi, aimed squarely at AI-power and wide-bandgap [13][14].

- **Constraints**
 - Deep cyclicality is biting now: Axcelis FY25 revenue fell to ~$839M from ~$1.02B in 2024 as SiC and memory digested; SiC upstream utilisation sat near 50% with an overcapacity downturn running into 2027-2028 [12][14].
 - China is both a demand risk and a share threat: 2024 BIS export rules cut Axcelis revenue by ~$20-50M in FY25, and China's first domestic high-energy implanter (POWER-750H, Jan 2026) targets exactly the mature power/IGBT lane where Western OEMs sell most units [15][12].
 - Extreme incumbency caps any new-entrant TAM: an AMAT-led duopoly (~80-85% of systems) plus a few gas majors leaves no room at the tool layer.

- **Trends & inflections to watch**
 - GAA-to-CFET ramp adding implant steps. Tripwire: TSMC N2/A16 and Intel 18A volume ramp through 2026 disclosed as a step-up in implant tool buys per fab [10][11].
 - SiC cycle turn. Tripwire: SiC device-line utilisation back above ~80% and a fresh power-implanter order upcycle reported in 2027 [12].
 - Axcelis-Veeco close + China localisation. Tripwire: deal closes in 2026 with the >$5B combined TAM affirmed, against domestic Chinese power-implanter design-ins [13][15].

## Connections

Cluster: [Ion Implantation](/manufacturing/equipment-processes/ion-implantation/)
Adjacent steps: [Wet etch / chemical surface prep (process step)](/semiconductor-process-flow/frontend/flow-wet-etch-surface-prep/) · [Annealing / rapid thermal processing (process step)](/semiconductor-process-flow/frontend/flow-annealing-rtp/) · [Plasma / dry etch (process step)](/semiconductor-process-flow/frontend/flow-plasma-dry-etch/)
Theses: **Deposition Materials Process Market**

## Sources