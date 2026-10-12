---
type: concept
slug: flow-advanced-pkg-3d-hybrid-bonding
canonical_name: 'Advanced packaging: 3D stacking & hybrid bonding (process step)'
seq: 52
phase: assembly
related_concepts:
- hybrid-bonding
- tsv-through-silicon-via
- 3d-ic-stacking
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
parent_concepts:
- packaging
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
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: tsv-through-silicon-via
  name: TSV / Through-Silicon Via
  path: /manufacturing/packaging/tsv-through-silicon-via/
  macro: manufacturing
- slug: 3d-ic-stacking
  name: 3D IC Stacking
  path: /manufacturing/packaging/3d-ic-stacking/
  macro: manufacturing
---
> Step 52 of 56 in the semiconductor flow (Assembly). Prev: [Advanced packaging: fan-out (InFO / FOWLP / FOPLP) (process step)](/semiconductor-process-flow/packaging/flow-advanced-pkg-fanout/) · Next: [OSAT (outsourced assembly & test) services (process step)](/semiconductor-process-flow/packaging/flow-osat-assembly-test-services/)

## What this step does
This is the step that stacks die vertically and bonds them with direct copper-to-copper interfaces, replacing the solder microbumps used in 2.5D packaging. Where fanout and 2.5D place die side by side on an interposer, 3D stacking puts logic on logic (TSMC SoIC, Intel Foveros) or memory on memory (HBM) and connects the layers through the silicon itself. The unit sub-processes inside this step:
- Through-silicon via (TSV) etch, fill and reveal, the vertical wiring that carries signal through a die.
- Wafer thinning / backgrind to expose TSVs (overlaps with [Wafer backgrinding / thinning (process step)](/semiconductor-process-flow/packaging/flow-wafer-backgrind-thinning/)).
- Surface preparation: CMP planarisation of the bonding surface to sub-nanometre flatness, megasonic clean, then N2 plasma activation of the dielectric.
- Alignment and bonding: wafer-to-wafer (W2W) fusion at room temperature, or die-to-wafer (D2W) pick-and-place at sub-micron accuracy.
- Anneal to grow the copper-to-copper bonds, then stack the next layer.

## Equipment market
Yole sizes the dedicated hybrid-bonding tool market at about $152M in 2025, growing to roughly $397M by 2030 at a ~21% CAGR [1]. The adjacent thermocompression bonding (TCB) market is larger today, about $542M in 2025 to ~$936M by 2030 at ~12% [1], and the two together lead a back-end equipment expansion Yole frames as reaching ~$1.3B by 2030 [1]. Note the spread across sources: MarketsandMarkets puts the broader hybrid-bonding market (tools plus surface-prep plus metrology) at $164.7M in 2025 to $633.9M by 2032 at ~21% [2][6]. The tool-only Yole number is the cleaner figure for the bonder itself.

| Vendor | HQ | Est. share | Notable |
|---|---|---|---|
| EV Group (EVG) | Austria | ~26-32% W2W bonders | GEMINI fusion/hybrid platform; W2W leader; private |
| SUSS MicroTec | Germany | ~21% | XBC300 Gen2 D2W (May 2025); both W2W and D2W; listed (ETR:SMHN) |
| BE Semiconductor (BESI) | Netherlands | leader in D2W place/bond | pick-and-place precision; AMAT 9% stake Apr 2025; listed (AMS:BESI) |
| Applied Materials | US | front-end + integration | Kinex integrated D2W system (Nov 2025); co-dev with BESI; listed (NASDAQ:AMAT) |
| ASMPT / K&S / Hanmi / Shinkawa | Asia | high-end TCB + bonders | adjacent TCB and D2W bench |

Concentration is high: the top five (EVG, SUSS, BESI, AMAT, K&S) hold the high-end fully-automated segment [2]. The structure splits cleanly: EVG and SUSS own wafer-to-wafer; BESI plus AMAT own die-to-wafer, the segment that grows fastest because D2W is what AI logic and HBM stacking need.

## Materials & consumables
This step is more capital-intensive than consumable-intensive, but the recurring spend is real and pulls through other flow steps:
- Ultra-flat CMP slurries and pads for the bonding-surface planarisation (Cabot, DuPont, Fujimi; see [Chemical-mechanical planarisation (CMP) (process step)](/semiconductor-process-flow/frontend/flow-cmp-planarisation/)).
- Plasma-activation gases (N2 chemistry) and megasonic cleaning chemistries.
- Copper electroplating chemistry for TSV fill (overlaps [Copper electroplating (ECD) (process step)](/semiconductor-process-flow/frontend/flow-copper-electroplating-ecd/)); barrier/seed for TSV liners ([Barrier / liner / seed deposition (process step)](/semiconductor-process-flow/frontend/flow-barrier-liner-seed/)).
- Temporary bonding adhesives and carrier wafers for thinned-wafer handling.
The recurring-revenue note: the tools are big-ticket and lumpy, but every bonded wafer burns slurry, plating chemistry and clean media, so the consumables layer is an annuity that scales with wafer-starts rather than with the tool installed base.

## Competitive landscape & value capture
The moat is process know-how plus installed base plus an integrated recipe. Hybrid bonding yield is brutally sensitive to particle counts, surface flatness and sub-micron overlay, so a qualified tool with a working recipe at a leading foundry is extremely sticky. Value accrues in three pools: (1) the bonder itself (EVG/SUSS for W2W, BESI/AMAT for D2W); (2) the front-end prep that AMAT is bolting on (CMP, clean, activation, deposition) which is why AMAT took its BESI stake and launched Kinex; (3) the metrology pull-through, which is the underrated pool. Fine-pitch hybrid bonding needs IR void detection (voids hide under bonded silicon, invisible to optical), sub-micron overlay, and AFM-grade surface metrology, captured by KLA (irArcher overlay, PWG5 void detection), Onto Innovation (Dragonfly visible+IR), Camtek (3D/X-ray, strong at OSATs) and Bruker (AFM/white-light surface) [7][8]. Every pitch shrink raises the metrology intensity, so this is a structurally growing attach.

European angle: this step is unusually European-heavy at the tool layer. EVG (Austria, private) is the W2W leader and BESI (Netherlands, listed) and SUSS (Germany, listed) are top-five, so the picks-and-shovels here are largely EU-based.

## Market drivers, constraints & trends
Net read: the served market (bonders + surface-prep + metrology + consumables) is accelerating, but the curve is back-end-loaded. The logic-SoIC pull is here now; the big HBM volume wave slipped to ~2028-29.

- **Drivers**
 - AI logic stacking is the live driver: TSMC is building 10,000-15,000 SoIC wafers/month by 2026 (SoIC capacity CAGR >90% from 2022-27), with NVIDIA Rubin Ultra (2027) and Feynman (2028) the step-up where "SoIC usage rises significantly" [12][13]. SoIC capex is ~$6.8-7.0B per 10k wafers, so each unit of capacity is heavily bonder/prep-intensive [12].
 - First HBM mass-production hybrid-bonding order placed: SK Hynix ordered the AMAT+BESI inline system (~KRW 20B) in late March 2026 after completing 12-Hi hybrid-bonding validation, moving the platform from R&D to volume [14][15].
 - New volume pools beyond HBM/logic: hybrid bonding is being designed into 300-layer+ V10 NAND (SK Hynix targeting ~2027 mass production), widening the served wafer base [16].

- **Constraints**
 - HBM4/4E timing slip is the key near-term cap: JEDEC relaxed the HBM stack-height spec to ~900um, so HBM4/4E 12-16-Hi stays on TCB/microbumps and MR-MUF, postponing the large HBM hybrid-bonding step to HBM5 (~2028-29, 20+ layers) [17][18].
 - Capex intensity + cyclicality: tools are big-ticket and lumpy; BESI commentary flags FX/mix margin pressure and the uncertain pace at which dev tools convert to volume [15].
 - Yield brutality (particles, sub-micron overlay) keeps adoption gated to a few qualified foundry/memory lines, slowing the served-market ramp versus the demand narrative.

- **Trends & inflections to watch**
 - SoIC pitch shrink (6um in 2025 to 4.5um by 2029) raises bonder + metrology intensity per wafer [3]. Tripwire: TSMC confirming sub-4um or wafer-on-wafer SoIC in a 2027-28 symposium.
 - HBM hybrid-bonding inflection. Tripwire: a named DRAM maker placing volume (not pilot) hybrid-bonding HBM5 orders in 2027-28 [17].
 - NAND as a third part. Tripwire: SK Hynix or a peer confirming hybrid-bonded 300-layer NAND in mass production in 2027 [16].

## Connections
[Hybrid Bonding (Cu-Cu)](/manufacturing/packaging/hybrid-bonding/) · [TSV / Through-Silicon Via](/manufacturing/packaging/tsv-through-silicon-via/) · [3D IC Stacking](/manufacturing/packaging/3d-ic-stacking/) · theses: **Hybrid Bonding Interconnect** · **Advanced Packaging Market** · **Advanced Packaging Metrology**