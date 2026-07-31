---
type: concept
slug: osat
canonical_name: OSAT (Outsourced Semiconductor Assembly & Test)
aliases:
- OSAT
- outsourced assembly and test
- assembly and test
- back-end
kind: category
parent_concepts:
- packaging
- advanced-packaging
related_concepts:
- advanced-packaging
- pic-packaging-stack
- co-packaged-optics
- hybrid-bonding
- cowos
- fiber-to-chip-coupling
sources:
- '[[2023-10-19-e20-the-state-of-privacy-enhancing]]'
- '[[2022-12-15-unbundling-the-database]]'
- '[[2026-05-30-optical-interconnect-ma-ledger]]'
- '[[2026-06-22-sintered-metal-die-attach-landscape]]'
- '[[2026-06-22-thermal-stack-layer-landscape]]'
- '[[2026-06-16-advanced-packaging-market-tsmc-foundry-allocation-status-q1]]'
- '[[2026-05-30-osat-market-structure]]'
- '[[2025-09-25-corintis-microsoft-in-chip-microfluidic-cooling]]'
- '[[2026-06-22-liquid-metal-tim-landscape]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-07-11-neutral-pdk-heterogeneous-integration-landscape]]'
- '[[2026-04-10-advanced-packaging-market-advanced-packaging-market-monitor]]'
- '[[2026-07-26-ai-backend-network-optics-2026]]'
- '[[2026-07-27-cxmt-star-market-debut]]'
- '[[2026-05-30-intel-glass-substrates-program]]'
- '[[2025-07-03-datacentre-thermal-power-market-cooling-is-the-new]]'
- '[[2025-05-27-datacentre-thermal-power-market-intel-foundry-s-integrated]]'
- '[[2025-12-28-advanced-packaging-market-tsmc-cowos-capacity-scaling-up]]'
- '[[2025-05-03-datacentre-thermal-power-market-intel-foundry-thermal]]'
- '[[2025-08-05-taiwan-osat-gains-from-bis-whitelist-fall-short-as-us-grants]]'
frontier:
- Does a pure-play "photonic OSAT" emerge at scale, or do traditional OSATs (ASE/Amkor) + Fabrinet absorb the photonic-assembly value?
- Does TSMC's capture of the AI-accelerator advanced-packaging tier (CoWoS) permanently cap OSAT value, or do OSATs win the CPO-assembly tier?
last_updated: '2026-05-30'
tags:
- concept
- category
- packaging
- supply-chain
mention_count: 76
sources_7d: 5
sources_30d: 17
recent_mentions:
- slug: 2026-07-27-cxmt-star-market-debut
  title: CXMT's 466% STAR Market debut makes it China's most valuable mainland-listed company
  date: '2026-07-27'
  kind: web
- slug: 2026-07-26-ai-backend-network-optics-2026
  title: 'Dell''Oro: AI back-end switching past $100B by 2030, optical transport $16B in 2025'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-06-22-sintered-metal-die-attach-landscape
  title: Sintered-silver / sintered-copper die-attach landscape — physics, incumbents, AI-migration question (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-thermal-stack-layer-landscape
  title: AI datacentre thermal stack, junction-to-ambient — per-layer players, M&A, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-liquid-metal-tim-landscape
  title: Liquid-metal TIM landscape — players, physics, deployment, capture (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-16-advanced-packaging-market-tsmc-foundry-allocation-status-q1
  title: 'TSMC Foundry Allocation Status Q1 2026: CoWoS Sold Out, 2nm Booked, ~1M Wafer Demand'
  date: '2026-06-16'
  kind: web
neighbors:
- slug: advanced-packaging
  name: Advanced Packaging
  path: /manufacturing/packaging/advanced-packaging/
  macro: manufacturing
- slug: pic-packaging-stack
  name: PIC Packaging Stack
  path: /manufacturing/packaging/pic-packaging-stack/
  macro: manufacturing
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: cowos
  name: CoWoS (TSMC)
  path: /manufacturing/packaging/cowos/
  macro: manufacturing
- slug: fiber-to-chip-coupling
  name: Fibre-to-Chip Coupling
  path: /manufacturing/packaging/fiber-to-chip-coupling/
  macro: manufacturing
---
*The **back-end** of the chip supply chain — the firms that take finished wafers and turn them into packaged, tested chips. Archetype #5 in **2026 05 30 Photonic Packaging Acquirer Map**; the assembly layer of the [PIC Packaging Stack](/manufacturing/packaging/pic-packaging-stack/).*

## What an OSAT is

A fab (TSMC, GF, Intel) makes the wafer — the **front-end**. An **OSAT** does everything after: dicing the wafer, **assembly** (putting die into/onto a package — wire-bond, flip-chip, fan-out, 2.5D/3D stacking), and **test**. They are contract manufacturers — the "foundry of the back-end." Historically commodity/low-margin, but the value is migrating here as Moore's-Law scaling stalls and performance comes from **[Advanced Packaging](/manufacturing/packaging/advanced-packaging/)** instead (chiplets, HBM stacks, CPO).

Two structural facts to hold:
1. **Geography:** Taiwan + China dominate. The big-3 (ASE, Amkor, JCET) hold ~55-60% of the merchant OSAT market; top-10 combined ≈ **$41.6B (2024)**, and Chinese OSATs (JCET, HT-Tech, TongFu) are gaining double-digit share.
2. **The IDM-foundry squeeze:** **TSMC captured the highest-value tier itself** — leading-edge 2.5D ([CoWoS (TSMC)](/manufacturing/packaging/cowos/)) and 3D (SoIC) for AI accelerators (Nvidia, AMD) is done in-house by TSMC, *not* outsourced to OSATs. So OSATs are pushed into fan-out, flip-chip, test, and TSMC-overflow capacity. This is the defining tension of the sector.

## The roster (2024 revenue, rankings through 2025)

| Rank | OSAT | Country | ~Revenue | Niche / note | KB page |
|---|---|---|---|---|---|
| 1 | **ASE Technology** (incl. SPIL, USI) | 🇹🇼 | **$18.5B** (~45% of top-10) | Clear #1; VIPack adv-packaging + SiPh/CPO assembly | **ASE** |
| 2 | **Amkor** | 🇺🇸/🇰🇷 | **$6.3B** | Primary Western OSAT; $2B Arizona fab (near TSMC AZ) | **Amkor** |
| 3 | **JCET** | 🇨🇳 | **$5.0B** (+19% YoY) | Largest mainland-China OSAT | **JCET** |
| 4 | **TongFu (TFME)** | 🇨🇳 | **$3.3B** | Close AMD partner | **TongFu** |
| 5 | **Powertech (PTI)** | 🇹🇼 | **$2.3B** | Memory packaging specialist | **PTI** |
| – | **Tianshui Huatian** | 🇨🇳 | ~$2B | China OSAT, gaining share | — (no page) |
| – | **SPIL** | 🇹🇼 | (in ASE since 2018) | — | **SPIL** |
| – | **KYEC, ChipMOS, UTAC, Unisem** | 🇹🇼/SG/MY | smaller | test / display-driver / memory specialists | **KYEC**, **ChipMOS** |

**There is no pure-play "photonic OSAT" at ASE/Amkor scale.** Photonic packaging is fragmented across four kinds of player — and that fragmentation is itself the opportunity:

| Type | Who | Role |
|---|---|---|
| **Traditional OSATs adding photonic lines** | **ASE** (VIPack SiPh/CPO), **Amkor** (optical packaging) | scale + electrical packaging, *learning* optical alignment |
| **Volume optical contract mfr** | **Fabrinet** (🇹🇭, ~$910M/qtr) | the de-facto photonic OSAT *at scale* today |
| **Specialist photonic-assembly houses** | **PHIX** (🇳🇱), Tyndall, **Fraunhofer IZM**, Silitronics | Western pure-play photonic-assembly *foundries* |
| **Assembly/test equipment** | **ficonTEC** (active-alignment machines), Vanguard | the *tooling* the others run |

The bottleneck across all of them is **fibre-attach / active optical alignment** ([Fibre-to-Chip Coupling](/manufacturing/packaging/fiber-to-chip-coupling/)) — a different skill from electrical OSAT, done on ficonTEC machines. Because photonic packaging is **~25-50% of optical-module value**, the OSATs want in, but none has fully merged electrical-advanced-packaging + photonic-die-attach + fibre-coupling. That unmerged skill stack is the [PIC Packaging Stack](/manufacturing/packaging/pic-packaging-stack/) white space.

## Companies using

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Pure-play photonic OSAT at scale — emerges, or absorbed by ASE/Amkor/Fabrinet?
- Does TSMC's CoWoS capture permanently cap OSAT value, or do OSATs win the CPO-assembly tier?
- Western photonic-assembly capacity (PHIX/Tyndall scale-up) — sovereignty play as CPO volume arrives?
