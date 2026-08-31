---
type: concept
slug: vcsels
canonical_name: VCSELs
aliases:
- VCSEL
- vcsel
- Vertical-Cavity Surface-Emitting Laser
kind: technology
parent_concepts:
- photonic-systems
- light-sources
related_concepts:
- gallium-arsenide
- photonic-compute
- lasers
sources:
- '[[2026-05-30-intel-optoscribe-acquisition]]'
mention_count: 28
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-05-30-intel-optoscribe-acquisition
  title: Intel Acquires Optoscribe (3D glass photonics, Livingston, Scotland)
  date: '2022-01-27'
  kind: web
neighbors:
- slug: gallium-arsenide
  name: Gallium Arsenide (GaAs)
  path: /materials/substrates/gallium-arsenide/
  macro: materials
- slug: photonic-compute
  name: Photonic Compute
  path: /photonic-systems/photonic-compute/photonic-compute/
  macro: photonic-systems
- slug: lasers
  name: Lasers
  path: /photonic-systems/light-sources/lasers/
  macro: photonic-systems
---
5-technical-questions]]'
- ''
- ''
- '**Idea Evidence 2026 07 22**'
- '**Idea Evidence 2026 08 06**'
deal_count: 0
frontier:
- ''
last_updated: '2026-07-25'
tags:
- concept
- technology
mention_count: 28
last_reorg_date: '2026-05-13'
---

# VCSELs

*Kind: technology*

## Physics / mechanism

Vertical-Cavity Surface-Emitting Lasers emit light perpendicular to the wafer surface via a resonant cavity formed between two distributed Bragg reflector (DBR) mirror stacks sandwiching a quantum-well active region. Stimulated emission occurs along the growth axis; single-mode operation is achievable at small apertures (3–5 µm). Key parameters: threshold current (sub-1 mA for small aperture), wall-plug efficiency (up to ~60% for 850 nm GaAs devices), modulation bandwidth (>30 GHz for datacom VCSELs), and beam quality (circular, low-divergence). Wavelengths span 670 nm–1550 nm depending on material system. State-of-the-art 940 nm VCSELs (Apple Face ID era) achieve >50% PCE; 1550 nm InP VCSELs remain efficiency-constrained. High-volume fabs now run VCSEL wafers on 6-inch GaAs.

## Competitive landscape

Edge-emitting lasers (EELs/FP/DFB) offer higher power-per-emitter and longer coherence but require cleaved facets, are harder to test on-wafer, and don't array as easily. VCSELs dominate short-reach datacom, 3D sensing, and LiDAR illumination where array density and testability matter.

## VCSELs in COMPUTING (added 2026-07-11 — full map: **Optical Compute Landscape**)

## Array scaling: the industry solved dot-count with optics, not with emitters (25 Jul 2026)

*Source: René Kromhof, — sent "just for your KB" as a correction to a figure Lawrence had put in writing to GlobalFoundries.*

**The structural point matters more than the number.** Face ID is the highest-volume VCSEL array ever manufactured, and when its designers needed a dense dot field they did **not** scale emitter count on die — they kept the array small and added an optical element. That is the revealed cost-and-yield answer from the one application with the volume to justify brute-forcing array size. Two consequences for diligence:

1. **There is no production learning curve running toward very large addressable arrays.** Anyone proposing 10⁵–10⁸ independently-addressed emitters per die is not extrapolating an industry trend; they are proposing a discontinuity the industry deliberately routed around. Do not let "Face ID proves VCSEL arrays scale" pass unchallenged — it proves the opposite about *emitter count*, and only proves scale in *units shipped*.
2. **Distinguish emitter count from dot count, and both from independently-addressed elements.** Illuminator arrays do reach tens of thousands of emitters, but wired in parallel as a single block — one control element, not thousands. The scarce quantity is **independently functioning, individually addressed lasing elements**, and nobody has demonstrated that beyond a few thousand.
3. **Optical fanout does not rescue a logic architecture — pre-load this rebuttal.** The obvious founder counter is "we don't need N emitters, we can replicate optically like Face ID does." It fails on the mechanism: a DOE replicates a **fixed, identical, static pattern**, which is exactly why it works for structured-light illumination. Logic is the opposite requirement — every gate must hold its own bit and switch independently of its neighbours. You cannot fan out state. So the one manufacturing trick the VCSEL industry actually uses to reach large dot counts is **structurally unavailable** to any architecture where the emitters are the compute elements, and the demonstrated ceiling on independently-addressed elements is the binding number.

## Investment relevance (all routes)

| Parameter | VCSEL | Edge Emitter | VCSEL Array |
|---|---|---|---|
| Single-emitter power | <10 mW typ. | 100 mW–W | — |
| On-wafer testability | Yes | No | Yes |
| Beam quality | Circular | Astigmatic | Engineered |
| Wavelength range | 670–1550 nm | 400 nm–3 µm | Same as single |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
