---
type: concept
slug: pluggable-transceivers
canonical_name: Pluggable Transceivers (QSFP-DD, OSFP, 800G, 1.6T)
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
recent_mentions: []
neighbors: []
---
## Physics / mechanism

Pluggable transceivers are self-contained optical I/O modules that convert electrical signals to optical and back, enabling high-bandwidth interconnects between switches, routers, and AI/ML accelerators. The dominant form factors are QSFP-DD (8 electrical lanes, dual-density) and OSFP (larger thermal envelope, preferred for high-power DSPs). Current state-of-the-art is 800G per module using 8×100G lanes with PAM4 modulation; 1.6T (8×200G or 16×100G) is sampling now, driven by 200G-per-lane EMLs or SiPh-based coherent-lite approaches. Key parameters: power envelope (OSFP supports ~15W vs QSFP-DD's ~12W), reach (SR4 to ZR/ZR+), and DSP power efficiency (mW/Gbps). Dominant IC suppliers: Marvell, Broadcom (Inphi), HiSilicon. Module vendors: Coherent, II-VI, InnoLight, Eoptolink.

## Competitive landscape

The principal alternative is co-packaged optics (CPO), which moves optical engines onto the switch package, eliminating pluggable mechanical interfaces and the copper SerDes loss that forces power-hungry DSPs. Near-term competition also comes from Linear Drive Pluggable (LPO/LPO-AI), which strips the DSP to cut power and latency. On-board optics (OBO) sits between pluggable and CPO. For the foreseeable 3–5 year horizon, pluggables retain dominance in installed base, supply chain maturity, and replaceability.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
