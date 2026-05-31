---
type: concept
slug: hbm-cowos-bottleneck
canonical_name: HBM / CoWoS Bottleneck
aliases:
- advanced packaging bottleneck
- HBM scarcity
- CoWoS allocation fight
kind: industry-structure
parent_concepts:
- compute-architecture
- semiconductor-industry-structure
related_concepts:
- mature-foundry-positioning
- chiplets
- backside-power-delivery
- ucie
sources: []
frontier:
- When does TSMC CoWoS-S capacity reach demand parity? Current estimates point to mid-2027 at earliest.
- Does SK Hynix HBM4 capacity ramp on schedule for late-2026 GA?
- Does Samsung Foundry close the CoWoS-S gap, or does Intel Foundry break through with its EMIB-X variant?
- Which physics-native compute companies most credibly bypass the bottleneck vs which are paper claims?
last_updated: '2026-05-27'
tags:
- concept
- industry-structure
- semiconductor
- packaging
- hbm
sources_7d: 0
sources_30d: 2
recent_mentions: []
neighbors:
- slug: mature-foundry-positioning
  name: Mature Foundry Positioning
  path: /sotf-site/compute/compute-architecture/mature-foundry-positioning/
  macro: compute
- slug: chiplets
  name: Chiplets
  path: /sotf-site/compute/compute-architecture/chiplets/
  macro: compute
- slug: backside-power-delivery
  name: Backside Power Delivery (BPD)
  path: /sotf-site/compute/compute-architecture/backside-power-delivery/
  macro: compute
- slug: ucie
  name: UCIe (Universal Chiplet Interconnect Express)
  path: /sotf-site/compute/compute-architecture/ucie/
  macro: compute
---
The two simultaneous supply-side constraints that define AI accelerator economics through 2027. **TSMC CoWoS-S advanced packaging** and **HBM3e high-bandwidth memory** are both running at full utilisation, both allocated almost entirely to Nvidia, AMD, Broadcom, and the hyperscaler custom-silicon programmes. Any new entrant requiring either is queueing.

The bottleneck is not just a cost / lead-time problem; it's a structural moat against new AI accelerator companies, which is why bypass-the-bottleneck approaches like [Physics-Native Compute](/sotf-site/compute/non-conventional/physics-native-compute/) and [Mature Foundry Positioning](/sotf-site/compute/compute-architecture/mature-foundry-positioning/) have a window.

## CoWoS allocation

TSMC's Chip-on-Wafer-on-Substrate advanced packaging family. Three variants:
- **CoWoS-S** (silicon interposer) — the workhorse for HBM-paired AI accelerators
- **CoWoS-L** (large interposer) — for >reticle-size designs (Cerebras WSE successors)
- **CoWoS-R** (RDL interposer) — lower-end, less constrained

Industry-tracked capacity numbers (verify with Yole or TrendForce before citing):
- CoWoS-S capacity: ~330K wafers/year baseline, ramp to ~700K wafers/year by end-2026
- Allocated through 2026: Nvidia ~60%, AMD ~10–15%, Broadcom + hyperscalers ~20%, remainder split among new entrants

New entrants typically wait 18–24 months for first allocation. Cerebras's WSE generation requires CoWoS-L specifically, smaller production runs.

## HBM allocation

HBM3e (8-stack, 24Gb-die) supply allocated:
- Samsung: ~50% of capacity to Nvidia, ~30% AMD/Broadcom, remainder smaller buyers
- SK Hynix: similar allocation pattern, lead supplier for Nvidia H200 / Blackwell
- Micron: ramping, currently smallest of the three

HBM4 (12-stack, 32Gb-die, base-die customisation) target H2 2026 general availability. Likely slip to early 2027 per industry tracking.

## Why this matters as a positioning thesis

Two responses available to a new AI hardware startup:

Bypass approaches have a window through 2027. Once CoWoS capacity catches demand and HBM4 ramps, the bottleneck eases and the bypass edge erodes. The window is what makes pre-seed deals in this category time-sensitive.

## Bypass approaches across the cohort

## DD signals

**Strong signal.** Founder names "no CoWoS" or "no HBM" as a positioning choice. Maps the bypass mechanism specifically (on-die SRAM, in-substrate weights, photonic interconnect). Acknowledges the 2027 bottleneck window honestly.

**Weak signal.** "We'll figure out packaging later." "HBM is just one option." No supply-chain awareness.

## Sources

<!-- dataview block stripped for public site -->
