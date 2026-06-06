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
- '[[2026-05-30-teramount-50m-molex-acquisition]]'
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
sources_7d: 0
sources_30d: 3
recent_mentions: []
neighbors:
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: photonic-wire-bonding
  name: Photonic Wire Bonding
  path: /sotf-site/manufacturing/packaging/photonic-wire-bonding/
  macro: manufacturing
- slug: glass-photonics
  name: Glass Photonics
  path: /sotf-site/photonic-systems/pic-platforms/glass-photonics/
  macro: photonic-systems
- slug: glass-interposers
  name: Glass Interposers
  path: /sotf-site/manufacturing/packaging/glass-interposers/
  macro: manufacturing
- slug: hybrid-bonding
  name: Hybrid Bonding (Cu-Cu)
  path: /sotf-site/manufacturing/packaging/hybrid-bonding/
  macro: manufacturing
- slug: heterogeneous-photonic-integration
  name: Heterogeneous Photonic Integration
  path: /sotf-site/photonic-systems/pic-platforms/heterogeneous-photonic-integration/
  macro: photonic-systems
- slug: silicon-photonics
  name: Silicon Photonics
  path: /sotf-site/photonic-systems/pic-platforms/silicon-photonics/
  macro: photonic-systems
- slug: inp-photonics
  name: InP Photonics
  path: /sotf-site/photonic-systems/pic-platforms/inp-photonics/
  macro: photonic-systems
- slug: fiber-to-chip-coupling
  name: Fibre-to-Chip Coupling
  path: /sotf-site/manufacturing/packaging/fiber-to-chip-coupling/
  macro: manufacturing
---
*The synthesis page for "how you package a photonic IC." Full decision brief: **2026 05 30 Pic Packaging Approaches Landscape**.*

## The core idea — two axes, not one

"Packaging a PIC" is constantly conflated with "which PIC platform wins." They are **different axes**:

1. **Platform axis** — what the PIC is *made of* (where light is generated/modulated/detected): [Silicon Photonics](/sotf-site/photonic-systems/pic-platforms/silicon-photonics/), [InP Photonics](/sotf-site/photonic-systems/pic-platforms/inp-photonics/), SiN, TFLN, polymer, glass. Covered by **Photonics Material Class War** / **2026 05 30 Pic Market Structure**.
2. **Packaging axis** — how you *connect* the PIC: a **4-layer stack**, each layer its own contest. This page.

**[Silicon Photonics](/sotf-site/photonic-systems/pic-platforms/silicon-photonics/) is the platform; [Glass Photonics](/sotf-site/photonic-systems/pic-platforms/glass-photonics/), [Photonic Wire Bonding](/sotf-site/manufacturing/packaging/photonic-wire-bonding/), [Hybrid Bonding (Cu-Cu)](/sotf-site/manufacturing/packaging/hybrid-bonding/) and [Co-Packaged Optics](/sotf-site/manufacturing/packaging/co-packaged-optics/) are competing answers to the packaging axis.** They are mostly complementary, not rival: a SiPh die does the electro-optics, and the packaging stack gets light + power on and off it.

## Why packaging is a sub-industry

Silicon's high index contrast makes the on-chip mode **~0.5 µm** vs a fibre's **~10 µm** — a ~20× mode mismatch that no glue can bridge. That, plus silicon's lack of a native laser and its two-photon absorption at high power, generates the whole stack below. Commercially this is where the value is: packaging is **~25% of a datacom pluggable's value, ~50% of early-CPO value**; Yole sizes photonics packaging at **$4.5B (2025) → $14.4B (2031), ~21.5% CAGR** (**2026 05 30 Pic Market Structure**).

## The four layers

| Layer | Problem | Competing approaches | Glass's role |
|---|---|---|---|
| **1. Fibre→chip coupling** | bridge the ~20× mode mismatch | edge/grating coupling · polymer [Photonic Wire Bonding](/sotf-site/manufacturing/packaging/photonic-wire-bonding/) · **glass waveguide** · fibre arrays (PROFA) | **competes directly** — the inorganic, reliability-winning option |
| **2. Laser / light-source attach** | silicon can't lase | external laser · flip-chip · [Heterogeneous Photonic Integration](/sotf-site/photonic-systems/pic-platforms/heterogeneous-photonic-integration/) · monolithic [InP Photonics](/sotf-site/photonic-systems/pic-platforms/inp-photonics/) · micro-LED | absent |
| **3. Die-to-die / die-to-substrate** | fine pitch, no optical misalignment | flip-chip bump · [Hybrid Bonding (Cu-Cu)](/sotf-site/manufacturing/packaging/hybrid-bonding/) · 2.5D interposer ([Glass Interposers](/sotf-site/manufacturing/packaging/glass-interposers/)) | glass-*core* substrate (primes' game) |
| **4. System co-packaging** | optics next to ASIC | [Co-Packaged Optics](/sotf-site/manufacturing/packaging/co-packaged-optics/) vs pluggable vs LPO/LRO | sets timing for all above |

Layer 1 is the contested, venture-relevant layer and the one the [Glass Photonics](/sotf-site/photonic-systems/pic-platforms/glass-photonics/) cohort lives in. See the cohort screen in **2026 05 30 Pic Packaging Approaches Landscape**.

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
