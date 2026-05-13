---
type: concept
slug: arvr
canonical_name: AR/VR
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- neural-interfaces
related_concepts: []
companies_using:
- apple
- bigscreen-beyond
- bytedance-pico
- campfire
- dispelix
- htc-vive
- inpixon-xr-division-cxapp
- lynx
- magic-leap
- meta-platforms-reality-labs
- microsoft-hololens
- mojo-vision
- nreal-xreal
- owl-ai-seereal-technologies
- prisme-formerly-strivr-offshoot
- qualcomm
- rokid
- scivista-formerly-imverse
- sightful
- snap-inc
- sony-playstation-vr
- ultraleap
- varjo
- viewtoo
- waveoptics-acquired-by-snap
ideas_referencing: []
sources:
- '[[2025-01-07-fund-frontier-expeditions-otherwise]]'
- '[[2023-05-25-interview-ben-mildenhall-co-inventor]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 8
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# AR/VR

*Kind: technology · Attio deal count: 4*

## Physics / mechanism

AR overlays digital content onto the physical world; VR replaces it entirely. Both pipelines share a common optics stack: display (micro-OLED, microLED, LCoS, or laser scanning), waveguide or lens combiner, and tracking (IMU + SLAM + eye-tracking). Key parameters: field of view (current AR ~50–60°, target >90°), exit pupil, see-through efficiency, and photon-to-photon latency (<20 ms threshold for comfort). Waveguides — diffractive (surface relief gratings, volume holograms) or reflective — are the critical bottleneck; coupling efficiency and rainbow artifact suppression remain unsolved at volume yield. MicroLED arrays (1–5 µm pitch) are the likely long-term display winner but fab yield at colour is <40% today.

## Competitive landscape


Meta Quest 3 dominates volumetric VR; Apple Vision Pro anchors premium passthrough AR at $3,499 — neither is a mass market device. Competing form factors: smart glasses (Ray-Ban Meta, no waveguide), laser-scanning retinal (Bosch, Dispelix), and holographic waveguide (WaveOptics/Snap, Lumus, Vuzix). Key substitutes are 2D mobile and large-format displays — incumbent inertia is enormous.

| Approach | FOV | Efficiency | Fab complexity |
|---|---|---|---|
| SRG diffractive waveguide | 50–60° | ~5–15% | High (nanoimprint/etch) |
| Reflective waveguide (Lumus) | 50–55° | ~70% | Medium |
| Retinal laser scan | ~70°+ | High | Medium (MEMS) |

## Cloudberry relevance
Cloudberry relevance is direct: waveguide fabrication is a photonics-fab problem solvable on modified semiconductor tooling — GlobalFoundries LP context is live here. Diffractive optic patterning, compound semiconductor microLED epitaxy (GaN, InGaN), and photonic integrated circuits for LiDAR-based tracking are all deal-flow angles. Sensor fusion ASICs and low-power edge inference chips for SLAM are adjacent semiconductor plays fitting the fund thesis.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
