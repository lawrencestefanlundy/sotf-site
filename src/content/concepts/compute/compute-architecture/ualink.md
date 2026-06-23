---
type: concept
slug: ualink
canonical_name: UALink (Ultra Accelerator Link)
aliases:
- UALink
- Ultra Accelerator Link
kind: standard
parent_concepts:
- scale-up-interconnect
related_concepts:
- cuda-moat
- co-packaged-optics
sources: []
frontier:
- Does a merchant UALink switch ship into a volume NVL72-class integrated rack before end-2027, or does it stay spec-ahead-of-silicon? (The [[scale-up-interconnect]] prediction 2.)
- Does the open scale-up camp consolidate, or stay fragmented three ways (UALink vs Broadcom SUE vs Meta ESUN)?
last_updated: '2026-06-22'
tags:
- concept
- standard
- interconnect
- compute
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
---
> The open **scale-up** standard — the consortium answer to NVIDIA's proprietary NVLink/NVSwitch at the rack-scale GPU-to-GPU tier. The contested heart of the **Scale Up Interconnect** thesis: real spec, credible members, but **silicon is late** and the camp is fragmented. Distinct from scale-OUT standards (Ultra Ethernet / UEC).

## What it is

A memory-semantic load/store interconnect for connecting accelerators into one coherent pod, governed by the UALink Consortium. **Spec: UALink 200G 1.0 ratified 8 April 2025** — 200 Gbps/lane, 800 Gbps/port, up to **1,024 accelerators per pod**. (UALink 2.0 shipped before any 1.0 merchant silicon — spec-ahead-of-silicon while NVLink ships in volume.)

## Members + silicon

- **Board:** Alibaba, AMD, Apple, Astera Labs, AWS, Cisco, Google, HPE, Intel, Meta, Microsoft, Synopsys. **Note: Broadcom is a Contributor, not a board member — it has effectively stepped back, pushing its own Scale-Up Ethernet (SUE).**
- **First merchant silicon (the weak spot):** **Upscale Ai** ("SkyHammer," $200M Series A) samples late-2026 / volume 2027; **Marvell** (via the XConn acquisition) follows ~FY2027; **Astera Labs** Scorpio ships early 2026 but native-UALink support is unconfirmed (coverage conflates "scale-up switch" with "UALink silicon" — flag). No competitive merchant UALink switch in volume mid-2026.

## The honest read

Open standards historically win *eventually* on cost/ubiquity (Ethernet, PCIe), but only after the incumbent harvests the high-margin years — and every prior win had a cheap good-enough merchant chip *at the moment of decision*. UALink has the spec and the consortium but **not the silicon when buyers chose 2026 racks**, the "open" banner is split three ways, and NVIDIA's **NVLink Fusion** + its **$2B Marvell stake (Mar 2026)** were designed to drain UALink's urgency. Realistic 2-3yr outcome: **coexistence, not displacement** — NVLink keeps the integrated-rack crown; open scale-up takes a slice among custom-accelerator hyperscalers. Fade "UALink wins" (~30%).

## Sources

- [UALink Consortium — members + spec](https://ualinkconsortium.org/) — spec status, board roster. *Tier 7.*
- [HPCwire — UALink 1.0 ratified (Apr 2025)](https://www.hpcwire.com/) *Tier 5.*

*Built 2026-06-22 as part of the **Scale Up Interconnect** thesis.*
