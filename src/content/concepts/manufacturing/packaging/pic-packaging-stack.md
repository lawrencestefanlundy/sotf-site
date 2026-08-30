---
type: concept
slug: pic-packaging-stack
canonical_name: PIC Packaging Stack
aliases:
- photonic packaging stack
- PIC packaging
- photonic packaging
kind: framework
parent_concepts:
- packaging
- photonic-integrated-circuits
related_concepts:
- co-packaged-optics
- photonic-wire-bonding
- glass-photonics
- glass-interposers
- hybrid-bonding
- heterogeneous-photonic-integration
- silicon-photonics
- inp-photonics
- fiber-to-chip-coupling
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2026-05-02-plug-and-play-sub-db-photonic-packaging-pubmed-2025]]'
- '[[2026-05-30-osat-market-structure]]'
- '[[2026-05-30-teramount-50m-molex-acquisition]]'
- '[[2026-05-21-doc-2bn-9-companies-quantum]]'
- '[[2026-05-02-two-photon-lithography-for-integrated-photonic-packaging-lig]]'
frontier:
- Which coupling approach wins volume CPO — edge, grating, glass, or PWB — and does it differ by platform (SiPh vs InP vs SiN)?
- Does the active-optical-alignment tooling gap (universal-unsolved per Ephos debrief) become a standalone equipment market?
- Do the fabless coupling specialists all get absorbed (Teramount→Molex pattern), leaving only captive + equipment plays?
last_updated: '2026-05-30'
tags:
- concept
- framework
- photonics
- packaging
descendants:
- fiber-to-chip-coupling
mention_count: 17
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-05-30-osat-market-structure
  title: OSAT market structure 2024-2025 — rankings, advanced-packaging split, photonic assembly
  date: '2026-05-30'
  kind: web
- slug: 2026-05-21-doc-2bn-9-companies-quantum
  title: Department of Commerce Announces Letters of Intent With 9 Companies for $2 Billion to Accelerate U.S. Leadership in Quantum Computing
  date: '2026-05-21'
  kind: web
- slug: 2026-05-30-teramount-50m-molex-acquisition
  title: Teramount — $50M raise (Jul 2025) then ~$430M Molex (Koch) acquisition (completed 7 May 2026)
  date: '2026-05-07'
  kind: web
- slug: 2026-05-02-plug-and-play-sub-db-photonic-packaging-pubmed-2025
  title: Plug-and-play sub-dB photonic packaging (PubMed 2025)
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-two-photon-lithography-for-integrated-photonic-packaging-lig
  title: 'Two-photon lithography for integrated photonic packaging (Light: AM 2023)'
  date: '2026-05-02'
  kind: web
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
neighbors:
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: photonic-wire-bonding
  name: Photonic Wire Bonding
  path: /manufacturing/packaging/photonic-wire-bonding/
  macro: manufacturing
- slug: glass-photonics
  name: Glass Photonics
  path: /photonic-systems/pic-platforms/glass-photonics/
  macro: photonic-systems
- slug: glass-interposers
  name: Glass Interposers
  path: /manufacturing/packaging/glass-interposers/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: heterogeneous-photonic-integration
  name: Heterogeneous Photonic Integration
  path: /photonic-systems/pic-platforms/heterogeneous-photonic-integration/
  macro: photonic-systems
- slug: silicon-photonics
  name: Silicon Photonics
  path: /photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
- slug: inp-photonics
  name: InP Photonics
  path: /photonic-systems/pic-platforms/inp-photonics/
  macro: photonic-systems
- slug: fiber-to-chip-coupling
  name: Fibre-to-Chip Coupling
  path: /manufacturing/packaging/fiber-to-chip-coupling/
  macro: manufacturing
---
*The synthesis page for "how you package a photonic IC." Full decision brief: pic packaging approaches landscape.*

## The core idea — two axes, not one

"Packaging a PIC" is constantly conflated with "which PIC platform wins." They are **different axes**:

1. **Platform axis** — what the PIC is *made of* (where light is generated/modulated/detected): [Silicon Photonics](/photonic-systems/pic-platforms/silicon-photonics/), [InP Photonics](/photonic-systems/pic-platforms/inp-photonics/), SiN, TFLN, polymer, glass. Covered by **Photonics Material Class War** / pic market structure.
2. **Packaging axis** — how you *connect* the PIC: a **4-layer stack**, each layer its own contest. This page.

**[Silicon Photonics](/photonic-systems/pic-platforms/silicon-photonics/) is the platform; [Glass Photonics](/photonic-systems/pic-platforms/glass-photonics/), [Photonic Wire Bonding](/manufacturing/packaging/photonic-wire-bonding/), [Hybrid Bonding (Cu-Cu)](/manufacturing/packaging/hybrid-bonding/) and [Co-Packaged Optics](/manufacturing/packaging/co-packaged-optics/) are competing answers to the packaging axis.** They are mostly complementary, not rival: a SiPh die does the electro-optics, and the packaging stack gets light + power on and off it.

## Why packaging is a sub-industry

Silicon's high index contrast makes the on-chip mode **~0.5 µm** vs a fibre's **~10 µm** — a ~20× mode mismatch that no glue can bridge. That, plus silicon's lack of a native laser and its two-photon absorption at high power, generates the whole stack below. Commercially this is where the value is: packaging is **~25% of a datacom pluggable's value, ~50% of early-CPO value**; Yole sizes photonics packaging at **$4.5B (2025) → $14.4B (2031), ~21.5% CAGR** (pic market structure).

## The four layers

| Layer | Problem | Competing approaches | Glass's role |
|---|---|---|---|
| **1. Fibre→chip coupling** | bridge the ~20× mode mismatch | edge/grating coupling · polymer [Photonic Wire Bonding](/manufacturing/packaging/photonic-wire-bonding/) · **glass waveguide** · fibre arrays (PROFA) | **competes directly** — the inorganic, reliability-winning option |
| **2. Laser / light-source attach** | silicon can't lase | external laser · flip-chip · [Heterogeneous Photonic Integration](/photonic-systems/pic-platforms/heterogeneous-photonic-integration/) · monolithic [InP Photonics](/photonic-systems/pic-platforms/inp-photonics/) · micro-LED | absent |
| **3. Die-to-die / die-to-substrate** | fine pitch, no optical misalignment | flip-chip bump · [Hybrid Bonding (Cu-Cu)](/manufacturing/packaging/hybrid-bonding/) · 2.5D interposer ([Glass Interposers](/manufacturing/packaging/glass-interposers/)) | glass-*core* substrate (primes' game) |
| **4. System co-packaging** | optics next to ASIC | [Co-Packaged Optics](/manufacturing/packaging/co-packaged-optics/) vs pluggable vs LPO/LRO | sets timing for all above |

Layer 1 is the contested, venture-relevant layer and the one the [Glass Photonics](/photonic-systems/pic-platforms/glass-photonics/) cohort lives in. See the cohort screen in pic packaging approaches landscape.

## The investable spine

## Companies / organisations using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Which coupling approach wins volume CPO, and does it differ by platform?
- Does the active-optical-alignment tooling gap become a standalone equipment market?
- Do all fabless coupling specialists get absorbed (Teramount→Molex pattern), leaving captive + equipment only?
