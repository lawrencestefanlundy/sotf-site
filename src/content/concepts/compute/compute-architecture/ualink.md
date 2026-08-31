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
sources:
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-04-02-scale-up-interconnect-the-nvidia-marvell-nvlink-fusion]]'
- '[[2026-06-14-rack-is-the-unit-of-compute-amd-mi400-helios-rack-scale]]'
- '[[2026-05-30-scale-up-interconnect-amd-helios-mi455x-rack-scale-platform]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-06-04-scale-up-interconnect-amd-helios-mi455x-rack-scale-platform]]'
- '[[2026-06-25-scale-up-interconnect-spheron-blog-ualink-vs-nvlink-open]]'
- '[[2026-07-02-scale-up-interconnect-upscale-ai-s-500m-bet-to-reinvent-ai]]'
- '[[2026-03-01-scale-up-interconnect-nvidia-nvlink-explained-a-guide-to]]'
frontier:
- Does a merchant UALink switch ship into a volume NVL72-class integrated rack before end-2027, or does it stay spec-ahead-of-silicon? (The scale up interconnect prediction 2.)
- Does the open scale-up camp consolidate, or stay fragmented three ways (UALink vs Broadcom SUE vs Meta ESUN)?
last_updated: '2026-06-22'
tags:
- concept
- standard
- interconnect
- compute
mention_count: 10
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-02-scale-up-interconnect-upscale-ai-s-500m-bet-to-reinvent-ai
  title: Upscale AI's $500M bet to reinvent AI networking
  date: '2026-07-02'
  kind: web
- slug: 2026-06-25-scale-up-interconnect-spheron-blog-ualink-vs-nvlink-open
  title: 'Spheron Blog: UALink vs NVLink: Open GPU Interconnect for AI Inference and Training (2026)'
  date: '2026-06-25'
  kind: web
- slug: 2026-06-14-rack-is-the-unit-of-compute-amd-mi400-helios-rack-scale
  title: AMD MI400 Helios Rack-Scale System and UALink Interconnect
  date: '2026-06-14'
  kind: web
- slug: 2026-06-04-scale-up-interconnect-amd-helios-mi455x-rack-scale-platform
  title: AMD Helios MI455X Rack-Scale Platform Surfaces with 72-GPU Design, UALink-over-Ethernet Interconnect
  date: '2026-06-04'
  kind: web
- slug: 2026-05-30-scale-up-interconnect-amd-helios-mi455x-rack-scale-platform
  title: AMD Helios MI455X Rack-Scale Platform Surfaces with 72-GPU Design, UALink-over-Ethernet Interconnect
  date: '2026-05-30'
  kind: web
- slug: 2026-04-02-scale-up-interconnect-the-nvidia-marvell-nvlink-fusion
  title: The NVIDIA Marvell NVLink Fusion partnership underscores the inevitable momentum of NVLink as the dominant fabric in AI data centers
  date: '2026-04-02'
  kind: web
- slug: 2026-03-01-scale-up-interconnect-nvidia-nvlink-explained-a-guide-to
  title: 'NVIDIA NVLink Explained: A Guide to the GPU Interconnect'
  date: '2026-03-01'
  kind: web
neighbors:
- slug: cuda-moat
  name: CUDA (the moat, and where it's eroding)
  path: /ai-software/models-inference/cuda-moat/
  macro: ai-software
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /manufacturing/packaging/co-packaged-optics/
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
