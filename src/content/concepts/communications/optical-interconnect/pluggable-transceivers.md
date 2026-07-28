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
sources:
- '[[2026-04-07-optical-displaces-copper-all-ai-data-center-interconnects]]'
- '[[2026-04-10-optical-interconnect-cpo-transition-co-packaged-optics-cpo]]'
- '[[2026-06-15-pic-market-structure-2030-cpo-npo-market-expected-to-exceed]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 8
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 1
recent_mentions:
- slug: 2026-06-15-pic-market-structure-2030-cpo-npo-market-expected-to-exceed
  title: CPO/NPO Market Expected to Exceed US$39 Billion by 2030
  date: '2026-06-15'
  kind: web
- slug: 2026-04-10-optical-interconnect-cpo-transition-co-packaged-optics-cpo
  title: Co Packaged Optics (CPO) – Scaling with Light for the Next Wave of Interconnect
  date: '2026-04-10'
  kind: web
- slug: 2026-04-07-optical-displaces-copper-all-ai-data-center-interconnects
  title: All AI Data Center Interconnects Will Be Optical Within 5 Years
  date: '2026-04-07'
  kind: web
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
