---
type: concept
slug: flow-physical-verification-drc-lvs
canonical_name: Physical verification (DRC/LVS/DFM) (process step)
seq: 12
phase: design
related_concepts:
- eda-design-tools
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
- flow-rtl-design
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
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
---
> Step 12 of 56 in the semiconductor flow (Design). Prev: [Timing signoff & parasitic extraction (process step)](/semiconductor-process-flow/design/flow-timing-signoff-extraction/) · Next: [Mask data prep & computational litho (OPC/ILT) (process step)](/semiconductor-process-flow/design/flow-mask-data-prep-opc/)

## What this step does
Physical verification is the final gate that checks the finished layout (the GDSII/OASIS polygon database) against the foundry's manufacturing and electrical rules before the design is handed to mask shops. It proves the geometry is buildable and that the drawn layout actually matches the intended circuit. The sub-processes inside it are:
- **DRC (design rule check)** — every polygon obeys the foundry's spacing, width, density and enclosure rules. At advanced nodes a rule deck can run to tens of thousands of rules.
- **LVS (layout versus schematic)** — the extracted netlist from the layout matches the source schematic/netlist device-for-device and net-for-net.
- **ERC / electrical checks** — antenna effects, latch-up, ESD and other reliability rules.
- **DFM (design for manufacturing)** — yield-oriented checks beyond pass/fail rules: lithography hotspot detection, critical-area/printability analysis, chemical-mechanical-polishing fill, and recommended-rule scoring.

## Where it sits and why it matters
This is the foundry's "you may not tape out until this is clean" checkpoint. Foundries publish their sign-off rule decks in the qualified vendor's format, and a chip cannot enter [Mask data prep & computational litho (OPC/ILT) (process step)](/semiconductor-process-flow/design/flow-mask-data-prep-opc/) until it returns zero violations against that deck. It is the single most captive, non-negotiable step in the whole design flow: there is no creative substitute, no in-house workaround, and the foundry, not the designer, dictates which tool is acceptable. That is what makes the value capture here unusually durable.

## Equipment market
Physical verification sits inside the larger IC physical design and verification segment, which is the biggest slice of EDA at roughly 35-38% of the ~$18B EDA+IP market in 2025 [1][2]. The standalone physical verification sub-segment is on the order of low-single-digit billions and growing high single digits to low teens, tracking overall EDA at ~8% CAGR with cloud-delivered verification growing faster (~16% CAGR) as multi-CPU sign-off moves off-prem [1][3]. Treat the exact split as an estimate; report-mill numbers for this sub-segment are thin and the big-three do not break it out.

| Vendor | HQ | Est. share (PV/sign-off) | Notable |
|---|---|---|---|
| Siemens EDA (Calibre) | Germany / US (Wilsonville OR) | ~70-85% | Golden DRC/LVS sign-off; foundries mandate "Calibre-clean" tape-out [4][5] |
| Synopsys (IC Validator) | US (Sunnyvale) | ~10-15% | In-design verification, tight fusion with its P&R/sign-off stack; growing [5] |
| Cadence (Pegasus / PVS) | US (San Jose) | ~5-10% | Cloud-native massively-parallel PV; second-source push [5] |
| Empyrean (Argus / Skipper) | China (Beijing) | <5% (global); largest China-domestic | China sign-off alternative under export curbs; state-controlled since 2024 [6][7] |

Concentration note: this is one of the most concentrated software markets on earth. Tool-level shares have been roughly stable for a decade, and physical verification is the extreme case. Calibre is the de-facto golden reference: TSMC, Samsung and Intel Foundry all specify Calibre-clean DRC/LVS for tape-out, which gives Siemens EDA structural relevance independent of how it does in other tool categories [4][5].

## Materials & consumables
Software has no physical consumables, but the economic equivalent is the **foundry rule deck and the recurring licence**. Two recurring streams:
- **Time-based licences (TBL).** EDA tools are leased, typically on multi-year subscriptions with pooled token licences, not sold perpetually. This is the recurring-revenue engine: Calibre seats renew annually/triennially and verification runs at advanced nodes consume large parallel token pools.
- **Foundry-encrypted PDK rule decks.** The DRC/LVS/DFM decks are written and maintained by foundries for the qualified tool. The deck is the lock-in: it is authored against Calibre's command language first, so the incumbent enjoys a self-reinforcing standard.

Recurring-revenue note: PV revenue is almost entirely subscription/maintenance, which is why the value-capturing layer carries software-like, not equipment-like, economics (see below).

## Volumes, revenue, profitability
Unit volume is best read as tape-outs and active design seats rather than wafers: every one of the tens of thousands of annual IC tape-outs must pass PV, and every advanced-node tape-out consumes more compute and more licence tokens than the last (rule counts and run-times scale with node complexity). The revenue pool is the physical-verification + sign-off slice of EDA, low-single-digit billions and rising with design starts and node count. The margins are the headline: pure-play EDA runs at software gross margins of ~80-86% (Synopsys ~77-82%, Cadence ~86% gross) with operating margins in the ~25-34% range [8][9]. The margin is earned by the tool vendor (overwhelmingly Siemens EDA in this step), not by the fab or the fabless designer. PV is among the stickiest, highest-margin lines in that mix because the foundry mandate removes price competition at sign-off.

## Market drivers, constraints & trends
Net read: the served market grows steadily-to-accelerating, with rule-deck inflation and the AI-EDA layer the two things that could re-rate it above EDA's ~8% baseline.

- **Drivers**
 - **Rule-deck inflation per node.** Gate-all-around plus backside power plus multi-die produces roughly a 10x rise in DRC count versus 7nm, and each advanced tape-out consumes more compute and more licence tokens than the last, so revenue per design start compounds independent of unit volume [10].
 - **AI/datacentre capex pulls advanced-node design starts.** The AI-EDA layer (ML-driven verification, hotspot prediction, root-cause) is forecast to grow from ~$4.3B (2026) to ~$15.9B (2032), a ~24% CAGR, far above the verification base, and this is the layer that re-rates PV pricing [11].
 - **Advanced packaging is a net-new verification surface.** 2.5D/3D-IC needs inter-die DRC/LVS, alignment and 3D-aware ESD checks (Calibre 3DSTACK, 3DBlox standard) that did not exist on a flat die, adding a fresh foundry-mandated deck per stack [12].
- **Constraints**
 - **Capped by design starts, not wafer volume.** PV scales with tape-outs and seats; node economics ($30M+ mask sets at 2nm) concentrate design starts in a few large customers, which limits unit-count growth [13].
 - **Cloud parallelism is partly deflationary.** Elastic-CPU signoff cuts ~40% of compute and 2000+ core runs compress run-time, so some of the per-tape-out compute uplift is given back to customers rather than captured [14].
 - **China access is a policy yo-yo.** The May 2025 BIS halt on EDA sales to China was largely reversed by July 2025, so the domestic-substitution tailwind for the incumbents' served market is real but reversible at short notice [15].
- **Trends & inflections to watch**
 - **GAA/backside-power node ramp.** Tripwire: N2P volume ramp in early 2026 and A16 (backside Super Power Rail) parts by end-2026 lift per-tape-out deck size and signoff compute on the dominant tool [16].
 - **2nm-class GAA going mainstream.** Tripwire: TSMC A14 (1.4nm, 2nd-gen GAA) entering production in 2028 marks the next step-change in rule count and DFM scope [16].
 - **China domestic signoff share.** Tripwire: Empyrean H1-2025 revenue RMB 502M (~$70M, +13% YoY) with self-sufficiency past 10%; a full-process domestic DRC/LVS flow qualified by SMIC at an advanced node would confirm a real share-shift, not just a stub [17].

## Connections
[EDA & Design Tools](/manufacturing/foundry-design/eda-design-tools/) · [Timing signoff & parasitic extraction (process step)](/semiconductor-process-flow/design/flow-timing-signoff-extraction/) · [Mask data prep & computational litho (OPC/ILT) (process step)](/semiconductor-process-flow/design/flow-mask-data-prep-opc/)

- Owning idea: **Eda Chip Design** (EDA design-tool layer).