---
type: concept
slug: lpo-linear-pluggable-optics
canonical_name: LPO (Linear Pluggable Optics)
aliases: []
kind: technology
parent_concepts:
- communications
- optical-interconnect
related_concepts: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---
## Physics / mechanism

LPO places the optical transceiver module directly on the switch ASIC package—or co-packaged on the same substrate—eliminating the pluggable cage, PCB trace runs, and retimer ICs that dominate power budgets in conventional architectures. The optical engine sits within ~5 mm of the SerDes I/O pads, cutting the electrical interface from 112 Gbps PAM4 over lossy FR4 to a short reach die-to-die or package-to-package link. This removes 1–2 W per port of retimer power and cuts insertion loss by 3–5 dB. Current SoA targets 800G per module (8×100G lanes), with 1.6T (8×200G, 200G-LR1) in qualification at leading hyperscalers. Lane rates are moving to 200 Gbps NRZ or PAM4; EML and silicon photonics are both candidate TX technologies. Thermal envelope per optical engine is constrained to ~5 W at the package edge.

## Competitive landscape

The primary competitor is CPO (co-packaged optics), which integrates the photonic die monolithically inside the switch package. CPO offers lower loss still, but demands tighter co-design between photonic foundry and ASIC vendor, creating supply chain risk. QSFP-DD and OSFP pluggables remain the incumbent—they lose on power per bit above 800G but preserve vendor flexibility. OSFP-XD and 1.6T pluggables extend the conventional form factor's life by 1–2 generations.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
