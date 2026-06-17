---
type: concept
slug: ar-glasses-stack
canonical_name: 'AR glasses: the component stack and competing technologies (primer)'
aliases:
- smart glasses stack
- AR glasses architecture
- AR glasses components
kind: primer
parent_concepts:
- displays
- arvr
related_concepts:
- laser-display-light-engines
- displays
- micro-leds
- metasurfaces-flat-optics
- ar-optical-combiners
- arvr
last_updated: 2026-06-15
tags:
- concept
- primer
- ar-vr
- displays
- smart-glasses
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: laser-display-light-engines
  name: Laser-Based Display Light Engines
  path: /sotf-site/photonic-systems/displays/laser-display-light-engines/
  macro: photonic-systems
- slug: displays
  name: Displays
  path: /sotf-site/photonic-systems/displays/displays/
  macro: photonic-systems
- slug: micro-leds
  name: Micro-LEDs
  path: /sotf-site/photonic-systems/displays/micro-leds/
  macro: photonic-systems
- slug: metasurfaces-flat-optics
  name: Metasurfaces & Flat Optics
  path: /sotf-site/photonic-systems/metasurfaces/metasurfaces-flat-optics/
  macro: photonic-systems
- slug: ar-optical-combiners
  name: 'AR optical combiners (waveguides): getting the image to the eye'
  path: /sotf-site/photonic-systems/displays/ar-optical-combiners/
  macro: photonic-systems
- slug: arvr
  name: AR/VR
  path: /sotf-site/life-frontier/neural-interfaces/arvr/
  macro: life-frontier
---
> A plain-English primer on what is actually inside a pair of AR / smart glasses, and the competing technology for each part. Built 15 Jun 2026 to ground the **Ar Display Optics** thesis: it shows where our bet (the display optics) sits in the whole device, and why the rest of the stack is mostly someone else's problem.

## The one-line mental model

An AR glass has to do four things: (1) **make an image**, (2) **deliver it to your eye while you still see the world**, (3) **sit in a lens you can actually wear** (often a prescription), and (4) **run the software and sense the world** so it knows what to draw. The first three are the **optics**, and they are the hard, unsolved, value-bearing part. The fourth (compute, sensing, power, audio, connectivity) is increasingly **offloaded to your phone or watch, or commoditised onto Qualcomm / Apple silicon**. Lawrence's read from the Smith call: solve the display and you can largely get by with the compute and battery we already have, because most of it gets offloaded. So the bottleneck, and the value, is the optics.

## The whole stack at a glance

The pattern: **components 1-3 (the optics) are where the unsolved physics and the defensible IP live; 4-8 are increasingly offloaded or owned by incumbents.** That is the whole reason the thesis is an optics thesis.

## 1. Light engine (the image source)

Generates the red / green / blue light. The big efficiency lever is **étendue**: a tightly-collimated source couples far more light into a tiny waveguide than a diffuse one, which is the core argument for lasers over LEDs.

Full detail, R&D challenges, and a DD checklist: [Laser-Based Display Light Engines](/sotf-site/photonic-systems/displays/laser-display-light-engines/).

## 2. Combiner / waveguide (delivery to the eye)

Takes the engine's image and overlays it on the real world. This is where most of the cost, the "eye glow," and the photolithography bottleneck live.

| Tech | How | Strength | Weakness |
|---|---|---|---|
| Diffractive waveguide (SRG) | surface gratings steer light | thin, scalable design | eye glow, low efficiency, flat, photolith (**Dispelix**) |
| Reflective / geometric (Lumus) | embedded partial mirrors | bright, efficient | hard to manufacture |
| Holographic / volume-Bragg | recorded holograms | thin, wavelength-selective | colour uniformity (Digilens; Akonia bought by Apple) |
| Bonded glass (Schott / Lumileds) | stacked glass layers | shipping in Meta Ray-Ban Display | ~$800/unit, flat, still glows |
| Metasurface | nanostructured flat optics | flat, design freedom | value absorbed by incumbents (see **Metalenses**) |
| Birdbath | 45° beamsplitter | cheap, good image | bulky, looks odd |
| **Fused / waveguide-less** | image generated inside the lens | no separate combiner, no photolith | concentrates all the risk in one process (**the bet**) |

The thesis bets the last row beats the rest (see **Ar Display Optics**).

## 3. Prescription lens (the wearable substrate)

Over 60% of buyers need a prescription; ~80% of those are astigmatic (ground to order). A real, under-appreciated component.

## 4-8. The rest (mostly not our bet, and that is the point)

- **Compute / SoC:** Qualcomm Snapdragon AR/XR is the merchant platform (the reference designs are actually built by Goertek); everyone except Apple builds on it, and most heavy compute offloads to the phone or watch. Commoditised, not a wedge.
- **Sensing / perception:** RGB cameras, time-of-flight depth, eye-tracking (for foveated rendering and UI), IMU, contextual microphones. Sony dominates image sensors. Owned by majors.
- **Power / battery:** the binding wearable constraint (~1-2 W thermal budget on the temple). Distributed cells, offload to a puck or phone. A constraint, not a venture wedge.
- **Audio:** open-ear directional speakers, beamforming mic arrays. Mature.
- **Frame / materials / industrial design:** fashion is a genuine spec (Bernard Kress: people will not wear flat, bifocal-looking glasses); the military wants ballistic plastic, not glass. Curvature and weight are real constraints, which is exactly why curved-plastic optics (rows 2-3) matter.

## Where the thesis sits

## See also