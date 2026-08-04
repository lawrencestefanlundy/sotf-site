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
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
mention_count: 229
sources_7d: 10
sources_30d: 24
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-17-sjtu-ge-si-photodetector-110ghz-fowlp
  title: Shanghai Jiao Tong University creates reconfigurable Ge-Si photodetector for high-speed datacoms
  date: '2026-06-17'
  kind: web
- slug: 2026-06-16-trapped-ion-landscape-2026
  title: Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)
  date: '2026-06-16'
  kind: web
- slug: 2026-06-13-next-gen-geothermal-research
  title: Next-gen geothermal (EGS / closed-loop / superhot mm-wave) — research sweep (Jun 2026)
  date: '2026-06-13'
  kind: web
- slug: 2026-06-04-q-memory-site
  title: Q-Memory — company website (q-memory.tech)
  date: '2026-06-04'
  kind: web
- slug: 2026-05-25-ai-glasses-display-timing-waveguide-display-technology
  title: Waveguide Display Technology Trends and Outlook 2026
  date: '2026-05-25'
  kind: web
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
- slug: 2025-10-30-ai-glasses-display-timing-meta-ray-ban-display-part-1-lumus
  title: Meta Ray-Ban Display Part 1 (Lumus Waveguide, OmniVision LCOS, and Goertek Projection Engine) – KGOnTech
  date: '2025-10-30'
  kind: web
neighbors:
- slug: laser-display-light-engines
  name: Laser-Based Display Light Engines
  path: /photonic-systems/displays/laser-display-light-engines/
  macro: photonic-systems
- slug: metasurfaces-flat-optics
  name: Metasurfaces & Flat Optics
  path: /photonic-systems/metasurfaces/metasurfaces-flat-optics/
  macro: photonic-systems
- slug: ar-glasses-stack
  name: 'AR glasses: the component stack and competing technologies (primer)'
  path: /photonic-systems/displays/ar-glasses-stack/
  macro: photonic-systems
- slug: displays
  name: Displays
  path: /photonic-systems/displays/displays/
  macro: photonic-systems
---
> The combiner is component 2 of the [AR glasses: the component stack and competing technologies (primer)](/photonic-systems/displays/ar-glasses-stack/): it takes the image from the light engine and overlays it on the real world. This is where most of the cost, the "eye glow," the flat-vs-curved problem, and the photolithography bottleneck live. It is also the layer the **Ar Display Optics** thesis bets *against* in its standalone form (we back fusion instead). Note: this is the **free-space near-eye combiner**, a different thing from the on-chip PIC waveguides covered by **Photonics Material Class War**, despite the shared word.

## The competing approaches

## The two structural problems

1. **Photolithography.** Diffractive waveguides are etched in silicon/SiC foundries. Jason Hartlove (Meta) put a number on the wall: ~6 TSMCs of photolith capacity to make the 100M diffractive pairs the market wants. The combiner is the photolith-bound part of the stack, so any photolith-free path (fusion, certain metasurface/replication routes) is a manufacturing-cost wedge.
2. **Flat vs curved.** Almost every waveguide approach is flat (foundry-made), but wrap-around curved lenses are what early adopters (cyclists, military, fashion) actually want, and what prescription grinding needs. Flatness is a form-factor dead end for the consumer market.

## Value capture (why the standalone combiner is a hard bet)

## See also

**Ar Display Optics** (the thesis) · [AR glasses: the component stack and competing technologies (primer)](/photonic-systems/displays/ar-glasses-stack/) (the full device) · [Laser-Based Display Light Engines](/photonic-systems/displays/laser-display-light-engines/) (the engine that feeds the combiner) · **Metalenses** (the metasurface platform) · **Photonics Material Class War** (the *other* kind of waveguide: on-chip PIC, not AR)
