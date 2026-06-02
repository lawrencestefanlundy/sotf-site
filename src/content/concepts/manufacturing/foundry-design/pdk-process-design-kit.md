---
type: concept
slug: pdk-process-design-kit
canonical_name: PDK / Process Design Kit
aliases: []
kind: technology
parent_concepts:
- manufacturing
- foundry-design
related_concepts:
- mpw-multi-project-wafer
- foundry
- eda-design-tools
sources: []
frontier:
- For a chip company turning foundry, how long from first internal PDK to a third-party-grade PDK external customers will design against?
- Which photonic foundries publish open vs NDA-gated PDKs, and does PDK openness predict adoption velocity?
last_updated: '2026-06-01'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: mpw-multi-project-wafer
  name: MPW / Multi-Project Wafer
  path: /sotf-site/manufacturing/foundry-design/mpw-multi-project-wafer/
  macro: manufacturing
- slug: foundry
  name: Semiconductor Foundries
  path: /sotf-site/manufacturing/foundry-design/foundry/
  macro: manufacturing
- slug: eda-design-tools
  name: EDA & Design Tools
  path: /sotf-site/manufacturing/foundry-design/eda-design-tools/
  macro: manufacturing
---
## Physics / mechanism

A PDK is the formal interface between a semiconductor fab's process and a designer's EDA toolchain. It packages design rules (DRC), layer definitions, SPICE models (BSIM, PSP, Verilog-A), parameterised cell libraries (pcells), and extraction decks (LVS/RCX) into a versioned artifact. When a designer draws a gate, the PDK defines minimum poly pitch, gate-oxide capacitance, threshold voltage corners (TT/FF/SS/SF/FS), and parasitic RC budgets. Modern advanced-node PDKs (TSMC N3, Intel 18A, GF 22FDX) contain millions of DRC rules; photonic PDKs (imec iSiPP50G, GF Fotonix, AIM Photonics) add waveguide loss coefficients, coupling gap tolerances, and S-parameter compact models. PDK maturity is a primary proxy for process maturity—tape-out yield tracks PDK revision count closely.

## Competitive landscape

Open-source PDKs (SkyWater SKY130, GF 180MCU, IHP SG13G2) have disrupted the traditional NDA-gated model, lowering university and startup entry costs. Competing abstraction layers include DTCO flows (design-technology co-optimisation, blurs PDK boundaries at 3 nm and below) and chiplet/UCIe interface specs that partially decouple die-level design rules from package integration. Cloud-native EDA (Cadence JedAI, Synopsys.ai) is pushing PDK consumption toward API-based rather than file-based delivery.

## PDK vs MPW, and what the customer actually does

A recurring confusion in foundry-layer deals: the PDK and the [MPW](/sotf-site/manufacturing/foundry-design/mpw-multi-project-wafer/) are orthogonal, not sequential stages of one thing.

- **A PDK is what you design *with*.** A software rulebook plus a characterised parts catalogue. It is the design-time interface.
- **An MPW is how you get a design *fabricated cheaply for the first time*.** A cost-sharing logistics model. It is the manufacturing-time service.

You design **with** the PDK, then fabricate **via** an MPW (prototype), and later via a dedicated wafer run (volume). The PDK does not change between MPW and dedicated; what changes is whether you share the wafer or own it. A foundry offering MPW access necessarily publishes a PDK first, because nothing can go on a shuttle that was not designed against the process rules.

| | PDK | MPW shuttle | Dedicated run |
|---|---|---|---|
| What it is | Design rulebook + parts library (software) | Shared-wafer prototype service | Own-wafer production service |
| Customer action | *Designs* a process-legal layout | *Submits* a finished layout to a slot | *Commits* to own masks + full wafers |
| Gets back | A GDS layout | A few–dozen prototype dies | Thousands of production dies |
| They are doing | Engineering / design | Validation / debug | Manufacturing |
| Cost | Licence (often free to qualified designers) | Per-area slot (~$50K–500K) | Full mask + wafers ($500K–5M+) |

## The chip-company → foundry transition (the load-bearing insight)

- Making your **own** chip work needs an **internal** PDK (your design team, your process).
- Letting **strangers** design on your process needs a **third-party-grade** PDK: documented, supported, with DRC decks, characterised components, MPW shuttle scheduling, and yield commitments.

The second is a multi-year, customer-facing engineering build that is categorically different from the first, and it serves a **different buyer**: the foundry-phase customer is a fabless photonics design team bringing their own designs, not the component buyer (e.g. a transceiver vendor) who purchases a finished chip. This is why Tower Semiconductor pulled the chip→foundry transition off (foundry DNA, productised PDK) while most photonic-chip peers stayed chip companies. "Our modulator works" does not imply "outsiders can design on our line." The external-PDK roadmap is both the moat and the most underestimated line item in the round.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
