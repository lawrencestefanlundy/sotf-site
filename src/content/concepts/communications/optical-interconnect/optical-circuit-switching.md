---
type: concept
slug: optical-circuit-switching
canonical_name: Optical Circuit Switching (OCS)
aliases:
- OCS
- optical-circuit-switch
- optical circuit switch
kind: technology
parent_concepts:
- communications
- optical-interconnect
related_concepts:
- optical-packet-switching
- optical-interconnect
- co-packaged-optics
sources: []
frontier:
- Does any standalone OCS company break the 0/N venture-scale base rate by 2030, or do all outcomes stay strategic-acquisition?
- Does ns-class optical switching arrive, moving OCS from slow topology reconfiguration toward NVLink-class fabric contention?
- 'Which switching medium wins for scale-up AI fabrics: MEMS, LCOS, free-space diffractive, or soliton-microcomb?'
last_updated: '2026-05-30'
tags:
- concept
- technology
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: optical-packet-switching
  name: Optical Packet Switching (OPS)
  path: /sotf-site/communications/optical-interconnect/optical-packet-switching/
  macro: communications
- slug: optical-interconnect
  name: Optical Interconnect
  path: /sotf-site/communications/optical-interconnect/optical-interconnect/
  macro: communications
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
---
*The "switch" layer, distinct from the "link" layer ([Optical Interconnect](/sotf-site/communications/optical-interconnect/optical-interconnect/), [Co-Packaged Optics](/sotf-site/manufacturing/packaging/co-packaged-optics/)).*

## Mechanism

OCS establishes a **dedicated lightpath** between input and output ports and holds it for the duration of a flow, reconfiguring the topology relatively slowly. It switches whole wavelengths/fibers, not individual packets. Reconfiguration time is set by the switching medium (MEMS tilt, LCOS phase, free-space diffraction) and is typically **µs-to-ms class** — fine for stable, long-lived flows and topology reconfiguration, too slow for per-packet routing. The complement, switching at packet granularity, is [Optical Packet Switching (OPS)](/sotf-site/communications/optical-interconnect/optical-packet-switching/).

**The discriminating spec for any optical switch is switching speed.** Per **Zigzag Networks**: ns-class competes with NVLink-class fabric; µs/ms competes only with incumbent OCS for slow topology reconfiguration.

## Where it sits (three distinct layers)

1. **Scale-up OCS / OPS** — the switch fabric (this page). Replaces electrical top-of-rack/spine with light for MoE all-to-all and collective ops.
2. **In-package optical I/O** — chip-to-chip (Ayar Labs, Lightmatter Passage, Celestial AI). *Not* switching.
3. **Fabric-replacement protocols** — NVLink, Broadcom Tomahawk. Electrical-native.

## Incumbent landscape

## Switching-speed spectrum (the discriminating axis)

The live competitive bet in OCS is **which medium delivers fast (sub-µs) switching at high radix and foundry-manufacturable cost** — where **Neye Ai**'s silicon-photonic MEMS currently looks strongest.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- 0/N base rate: broken by 2030, or holds?
- ns-class switching: does it arrive, and from which medium?
- Medium winner for scale-up AI fabrics (MEMS / LCOS / free-space diffractive / soliton-microcomb)?
