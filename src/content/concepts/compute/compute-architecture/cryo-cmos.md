---
type: concept
slug: cryo-cmos
canonical_name: Cryo CMOS
aliases: []
kind: technology
parent_concepts:
- compute
- compute-architecture
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 2
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---
## Physics / mechanism

Cryo CMOS refers to standard CMOS logic and mixed-signal circuits operated at cryogenic temperatures, typically 4 K (liquid helium) or 77 K (liquid nitrogen), to control and read out quantum processors co-located in dilution refrigerators. At 4 K, carrier freeze-out, threshold voltage shifts (+100–200 mV), reduced mobility (partially offset by phonon scattering suppression), and altered subthreshold slope change device behavior materially. Key parameters: power dissipation per qubit control channel must stay below ~1 mW at 4 K to avoid heat budget violations in dilution units (budget: 1–2 W at 4 K stage). State of the art: Intel Horse Ridge II, imec/SiGe demonstrators, and academic designs in 22 nm FD-SOI and 40 nm bulk nodes achieve multi-channel qubit control with sub-mW/channel targets approaching viable scale.

## Competitive landscape

The primary alternative is room-temperature classical electronics with coaxial cables running into the fridge—simple but fundamentally unscalable past ~100 qubits due to wiring density and heat load. SiGe HBT bipolar processes offer better cryo noise performance but higher static power. III-V HEMTs (InP, GaAs) operate cleanly at 4 K with superior noise figures but lack integration density. FD-SOI (GlobalFoundries 22FDX, ST 28 nm) is a leading candidate: back-gate tunability partially compensates threshold voltage shift, and the partially-depleted body reduces kink effect.

| Approach | Temp range | Integration density | Power/channel |
|---|---|---|---|
| Cryo CMOS (bulk/FD-SOI) | 4–77 K | High | ~0.5–5 mW |
| SiGe HBT | 4–77 K | Medium | ~2–10 mW |
| InP HEMT | 4 K | Low | <0.1 mW |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
