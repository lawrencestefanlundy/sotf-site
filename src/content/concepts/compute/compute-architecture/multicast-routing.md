---
type: concept
slug: multicast-routing
canonical_name: Multicast Routing
aliases: []
parent_concepts:
- compute-architecture
- compute
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 1
frontier:
- How does HyNoC encode a multicast tree in a source-routed header, and how does header length scale with the number of destinations?
- When one branch of a multicast transfer is blocked, does the router stall all branches or buffer per branch, and what is the measured throughput penalty?
- What is the FPGA area and maximum frequency cost of multicast replication logic relative to a unicast-only version of the same router?
- Does the fixed grant latency of the PRRA still yield a closed-form worst-case latency bound for multi-branch transfers, and has this been validated against measurement?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Multicast routing is the delivery of a single message from one source to several destinations inside an interconnect fabric, as opposed to unicast delivery of one copy per destination. In an on-chip network the practical question is where copies are made: at the sender (repeated unicast, which consumes source bandwidth linearly in the number of destinations) or inside routers, which fork a flit stream across multiple output ports and therefore need arbitration and path-encoding support for branching trees rather than single paths.

The available source places multicast in the context of a source-routed network-on-chip. HyNoC encodes the complete path through the network in the packet header, written either by the sender at run time or statically at compile time, which makes transfers deterministic and allows hotspot avoidance to be handled in software instead of in hardware. Source routing shifts the burden of multicast tree construction to the compiler or the sending core, since the header must describe every branch taken rather than a destination address to be resolved hop by hop.

HyNoC combines circuit-switch path establishment with wormhole data transfer, targeting distributed computing systems built around VLIW processor cores on FPGA. Circuit establishment before a wormhole burst matters for multicast because a reserved path removes mid-transfer contention on each branch, at the cost of holding resources for the duration of the transfer. Router-level parameters reported are a parallel round-robin arbiter (PRRA) with fixed grant latency and per-port independent clock domains; fixed grant latency is the property that makes end-to-end timing of a multi-branch transfer analysable at compile time.

The router feature list in the available excerpt is cut off mid-sentence, so the exact multicast mechanism (header encoding of branch sets, replication policy, flow control on blocked branches) is not established by the source.

## Competitive landscape

The source frames NoC design as a trade-off between latency, area and congestion management, and positions the hybrid circuit-switch/wormhole approach as a way to obtain deterministic low-latency transfers without the area overhead of virtual channels. That is the relevant comparison axis for multicast: virtual-channel routers are the conventional way to avoid deadlock and head-of-line blocking when a message occupies several output ports at once, so a virtual-channel-free design must recover that property some other way, here through pre-established paths and compile-time path selection. No quantitative comparison against other NoC architectures is available in the supplied material.

## Evidence base

- HyNoC is presented as an open-source NoC architecture combining circuit-switch path establishment with wormhole data transfer, targeting distributed VLIW cores on FPGA, published 7 July 2026.
- The design uses source routing, with the full path encoded in the packet header by the sender or statically at compile time.
- Stated aim of source routing: deterministic low-latency transfers plus software-level hotspot avoidance, without the area overhead of virtual channels.
- Router features reported include a parallel round-robin arbiter (PRRA) with fixed grant latency and per-port independent clock domains.

## Frontier (open questions)

- How does HyNoC encode a multicast tree in a source-routed header, and how does header length scale with the number of destinations?
- When one branch of a multicast transfer is blocked, does the router stall all branches or buffer per branch, and what is the measured throughput penalty?
- What is the FPGA area and maximum frequency cost of multicast replication logic relative to a unicast-only version of the same router?
- Does the fixed grant latency of the PRRA still yield a closed-form worst-case latency bound for multi-branch transfers, and has this been validated against measurement?

*Synthesised 2026-08-31 from 1 KB sources by the resynth pipeline; citations are KB source slugs.*
