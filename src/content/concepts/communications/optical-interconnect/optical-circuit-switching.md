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
- Does any standalone OCS company break the pattern in which no standalone OCS company has ever reached venture scale (they get acquired or stay small) by 2030, or do all outcomes stay strategic-acquisition?
- Does ns-class optical switching arrive, moving OCS from slow topology reconfiguration toward NVLink-class fabric contention?
- 'Which switching medium wins for scale-up AI fabrics: MEMS, LCOS, free-space diffractive, or soliton-microcomb?'
- Is the binding constraint the switch medium or transceiver re-synchronisation (after the switch changes path, the link must re-lock its timing before data can flow, which can take longer than the data burst itself)? And if it is the timing, does the fix need a photonic oscillator ([[lumisync]]) or does an electronic precision clock + algorithms suffice ([[oriole-networks]])? (Two-source corroboration that the re-locking delay is the constraint; Oriole vs LumiSync diverge on the fix.)
- 'The buffering crux for OPS: can all-optical packet switching ([[finchetto]]) actually run with NO buffering, or is packet switching fundamentally buffer-bound as Oriole/Zervas argue ([[2026-06-01-oriole-networks]])? Turns on output-contention handling and whether address-bus synchronisation reintroduces a re-locking delay.'
last_updated: '2026-06-14'
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

## The convergence trap and the enabling-layer wedge

The whole venture cohort is building the **same thing** — a reconfigurable optical switch fabric — and differentiating only on the **actuation medium** (3D-MEMS, silicon-photonic MEMS, Mach-Zehnder / micro-ring, active metasurface, LCOS, free-space diffraction). That is a sustaining-innovation arms race on one axis (ports × switching speed × power), and the zero-success record (no standalone OCS company has ever reached venture scale) says that race ends in strategic acquisition, not a standalone winner. The re-synchronisation reframe above sharpens it: if the binding constraint is timing rather than the switch medium, a better switch is the wrong thing to build.

So the orthogonal, earlier-stage bets are the layers the whole race needs **regardless of which switch medium or hyperscaler wins**:

**The robust version of the bet:** back the layer that wins regardless of which switch wins. #1 (source) is safest and already in-portfolio; #2 (sync) is the most contrarian and the clearest "sell to everyone." Weakest links held honestly: the wavelength-routing flip has been academically promising for 15+ years without displacing switches (so bet the source layer on "every fabric needs sources," with the flip as upside, not as the thesis); and the sync primitive risks being built in-house by hyperscalers (the merchant-vs-captive test).

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- The pattern where no standalone OCS company has ever reached venture scale (they get acquired or stay small): broken by 2030, or holds?
- ns-class switching: does it arrive, and from which medium?
- Medium winner for scale-up AI fabrics (MEMS / LCOS / free-space diffractive / soliton-microcomb)?
- Does the architecture flip to **wavelength routing** (passive AWGR + nanosecond-tunable lasers), moving value from the switch to the **light source**?
- Is the backable-early wedge the switch at all, or the enabling layer (tunable-laser/comb source; merchant burst-mode sync primitive) the whole cohort must buy?
