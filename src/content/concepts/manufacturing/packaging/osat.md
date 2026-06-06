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
sources: []
frontier:
- Does a pure-play "photonic OSAT" emerge at scale, or do traditional OSATs (ASE/Amkor) + Fabrinet absorb the photonic-assembly value?
- Does TSMC's capture of the AI-accelerator advanced-packaging tier (CoWoS) permanently cap OSAT value, or do OSATs win the CPO-assembly tier?
last_updated: '2026-05-30'
tags:
- concept
- category
- packaging
- supply-chain
sources_7d: 0
sources_30d: 2
recent_mentions: []
neighbors:
- slug: advanced-packaging
  name: Advanced Packaging
  path: /sotf-site/manufacturing/packaging/advanced-packaging/
  macro: manufacturing
- slug: pic-packaging-stack
  name: PIC Packaging Stack
  path: /sotf-site/manufacturing/packaging/pic-packaging-stack/
  macro: manufacturing
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /sotf-site/manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: cowos
  name: CoWoS (TSMC)
  path: /sotf-site/manufacturing/packaging/cowos/
  macro: manufacturing
- slug: fiber-to-chip-coupling
  name: Fibre-to-Chip Coupling
  path: /sotf-site/manufacturing/packaging/fiber-to-chip-coupling/
  macro: manufacturing
---
*The **back-end** of the chip supply chain — the firms that take finished wafers and turn them into packaged, tested chips. Archetype #5 in **2026 05 30 Photonic Packaging Acquirer Map**; the assembly layer of the [PIC Packaging Stack](/sotf-site/manufacturing/packaging/pic-packaging-stack/).*

## What an OSAT is

A fab (TSMC, GF, Intel) makes the wafer — the **front-end**. An **OSAT** does everything after: dicing the wafer, **assembly** (putting die into/onto a package — wire-bond, flip-chip, fan-out, 2.5D/3D stacking), and **test**. They are contract manufacturers — the "foundry of the back-end." Historically commodity/low-margin, but the value is migrating here as Moore's-Law scaling stalls and performance comes from **[Advanced Packaging](/sotf-site/manufacturing/packaging/advanced-packaging/)** instead (chiplets, HBM stacks, CPO).

Two structural facts to hold:
1. **Geography:** Taiwan + China dominate. The big-3 (ASE, Amkor, JCET) hold ~55-60% of the merchant OSAT market; top-10 combined ≈ **$41.6B (2024)**, and Chinese OSATs (JCET, HT-Tech, TongFu) are gaining double-digit share.
2. **The IDM-foundry squeeze:** **TSMC captured the highest-value tier itself** — leading-edge 2.5D ([CoWoS (TSMC)](/sotf-site/manufacturing/packaging/cowos/)) and 3D (SoIC) for AI accelerators (Nvidia, AMD) is done in-house by TSMC, *not* outsourced to OSATs. So OSATs are pushed into fan-out, flip-chip, test, and TSMC-overflow capacity. This is the defining tension of the sector.

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

The bottleneck across all of them is **fibre-attach / active optical alignment** ([Fibre-to-Chip Coupling](/sotf-site/manufacturing/packaging/fiber-to-chip-coupling/)) — a different skill from electrical OSAT, done on ficonTEC machines. Because photonic packaging is **~25-50% of optical-module value**, the OSATs want in, but none has fully merged electrical-advanced-packaging + photonic-die-attach + fibre-coupling. That unmerged skill stack is the [PIC Packaging Stack](/sotf-site/manufacturing/packaging/pic-packaging-stack/) white space.

## Companies using

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Pure-play photonic OSAT at scale — emerges, or absorbed by ASE/Amkor/Fabrinet?
- Does TSMC's CoWoS capture permanently cap OSAT value, or do OSATs win the CPO-assembly tier?
- Western photonic-assembly capacity (PHIX/Tyndall scale-up) — sovereignty play as CPO volume arrives?
