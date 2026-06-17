---
type: concept
slug: ar-optical-combiners
canonical_name: 'AR optical combiners (waveguides): getting the image to the eye'
aliases:
- waveguide
- AR waveguide
- optical combiner
- near-eye combiner
kind: technology
parent_concepts:
- displays
- arvr
related_concepts:
- laser-display-light-engines
- metasurfaces-flat-optics
- ar-glasses-stack
- displays
last_updated: 2026-06-15
tags:
- concept
- technology
- ar-vr
- displays
- waveguides
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: laser-display-light-engines
  name: Laser-Based Display Light Engines
  path: /sotf-site/photonic-systems/displays/laser-display-light-engines/
  macro: photonic-systems
- slug: metasurfaces-flat-optics
  name: Metasurfaces & Flat Optics
  path: /sotf-site/photonic-systems/metasurfaces/metasurfaces-flat-optics/
  macro: photonic-systems
- slug: ar-glasses-stack
  name: 'AR glasses: the component stack and competing technologies (primer)'
  path: /sotf-site/photonic-systems/displays/ar-glasses-stack/
  macro: photonic-systems
- slug: displays
  name: Displays
  path: /sotf-site/photonic-systems/displays/displays/
  macro: photonic-systems
---
> The combiner is component 2 of the [AR glasses: the component stack and competing technologies (primer)](/sotf-site/photonic-systems/displays/ar-glasses-stack/): it takes the image from the light engine and overlays it on the real world. This is where most of the cost, the "eye glow," the flat-vs-curved problem, and the photolithography bottleneck live. It is also the layer the **Ar Display Optics** thesis bets *against* in its standalone form (we back fusion instead). Note: this is the **free-space near-eye combiner**, a different thing from the on-chip PIC waveguides covered by **Waveguide Platform By Segment 2030**, despite the shared word.

## The competing approaches

## The two structural problems

1. **Photolithography.** Diffractive waveguides are etched in silicon/SiC foundries. Jason Hartlove (Meta) put a number on the wall: ~6 TSMCs of photolith capacity to make the 100M diffractive pairs the market wants. The combiner is the photolith-bound part of the stack, so any photolith-free path (fusion, certain metasurface/replication routes) is a manufacturing-cost wedge.
2. **Flat vs curved.** Almost every waveguide approach is flat (foundry-made), but wrap-around curved lenses are what early adopters (cyclists, military, fashion) actually want, and what prescription grinding needs. Flatness is a form-factor dead end for the consumer market.

## Value capture (why the standalone combiner is a hard bet)

## See also

**Ar Display Optics** (the thesis) · [AR glasses: the component stack and competing technologies (primer)](/sotf-site/photonic-systems/displays/ar-glasses-stack/) (the full device) · [Laser-Based Display Light Engines](/sotf-site/photonic-systems/displays/laser-display-light-engines/) (the engine that feeds the combiner) · **Metalenses** (the metasurface platform) · **Waveguide Platform By Segment 2030** (the *other* kind of waveguide: on-chip PIC, not AR)
