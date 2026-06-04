---
type: concept
slug: optical-packet-switching
canonical_name: Optical Packet Switching (OPS)
aliases:
- OPS
- all-optical packet switching
kind: technology
parent_concepts:
- communications
- optical-interconnect
related_concepts:
- optical-circuit-switching
- optical-interconnect
- non-linear-photonic-logic
sources: []
frontier:
- Can all-optical packet switching work without optical buffering/RAM — the blocker that has stalled OPS for two decades?
- Is OPS a venture-scale EXCEPTION to the OCS 0/N base rate, because it is harder and far less crowded?
- What is the actual switching speed and port count of the leading OPS approaches?
last_updated: '2026-05-30'
tags:
- concept
- technology
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: optical-circuit-switching
  name: Optical Circuit Switching (OCS)
  path: /sotf-site/communications/optical-interconnect/optical-circuit-switching/
  macro: communications
- slug: optical-interconnect
  name: Optical Interconnect
  path: /sotf-site/communications/optical-interconnect/optical-interconnect/
  macro: communications
---
*The frontier sibling of [Optical Circuit Switching (OCS)](/sotf-site/communications/optical-interconnect/optical-circuit-switching/) — switching at packet granularity rather than dedicated lightpaths.*

## Mechanism

OPS switches **individual packets** in the optical domain, rather than holding a dedicated lightpath (the [Optical Circuit Switching (OCS)](/sotf-site/communications/optical-interconnect/optical-circuit-switching/) approach). This is the harder, holy-grail end of optical switching: it needs fast all-optical logic and, historically, optical buffering — and the absence of practical optical RAM is the blocker that has stalled OPS for ~two decades. Because it is so much harder, the field is far less crowded than OCS, which is the bull-case framing for a startup that can make it work.

- Does **optical packet switching** (NOT circuit switching of the Google-OCS kind) for scale-out networking; claims ~1,000× lower latency and lower power than electro-optic conversion via a passive optical approach.
- Tech: [Lithium Niobate (TFLN)](/sotf-site/materials/functional-layers/lithium-niobate-tfln/) used for **frequency mixing** (the non-linearity), not modulation; poling is the hard step. First patent is an all-optical passive ALU (**Non Linear Photonic Logic**).
- GTM: a passive-switching PIC module / custom NIC IP block, partnering with NIC OEMs rather than competing on silicon.

The framing that matters: packet-vs-circuit is the differentiator. Anyone can do OCS; packet-granularity all-optical switching is the harder, less-crowded problem.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Practical all-optical packet switching without optical RAM/buffering?
- Venture-scale exception to the OCS 0/N base rate?
- Real switching speed + port count of leading approaches?
