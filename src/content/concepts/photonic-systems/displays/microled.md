---
type: concept
slug: microled
canonical_name: MicroLED microdisplays
aliases:
- micro-LED
- µLED
- uLED
- microLED
- micro LED
- monolithic RGB microLED
parent_concepts:
- emissive-display
related_concepts:
- emissive-display
- waveguides
- gallium-nitride
sources:
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-06-15-barry-silverstein-rochester-cxr]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-06-01-ai-glasses-display-timing-jbd-introduces-roadrunner-ii-full]]'
- '[[2026-04-07-ai-glasses-display-timing-two-key-breakthroughs-advance]]'
- '[[2026-05-15-ai-glasses-display-timing-jbd-leaps-into-12-inch-wafer]]'
frontier:
- Does red EQE at sub-5um pixel pitch become usable, and by when? This is the single gate on monolithic RGB.
- Does monolithic RGB beat 3-panel X-cube on cost and volume, or does X-cube stay good enough through 2030?
- Porotech's Dynamic Pixel Tuning (one pixel, any colour by current density) vs JBD's co-bonded stack — which reaches volume first?
last_updated: 2026-08-09
tags:
- concept
mention_count: 29
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-06-15-barry-silverstein-rochester-cxr
  title: University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality
  date: '2026-06-15'
  kind: web
- slug: 2026-06-01-ai-glasses-display-timing-jbd-introduces-roadrunner-ii-full
  title: JBD introduces Roadrunner II full-color microLED projector and AR glasses kit
  date: '2026-06-01'
  kind: web
- slug: 2026-05-15-ai-glasses-display-timing-jbd-leaps-into-12-inch-wafer
  title: JBD Leaps Into 12-Inch-Wafer MicroLED Manufacturing
  date: '2026-05-15'
  kind: web
- slug: 2026-04-07-ai-glasses-display-timing-two-key-breakthroughs-advance
  title: Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays
  date: '2026-04-07'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
neighbors:
- slug: emissive-display
  name: Emissive vs modulated display architectures
  path: /photonic-systems/displays/emissive-display/
  macro: photonic-systems
- slug: waveguides
  name: Waveguides
  path: /photonic-systems/pic-platforms/waveguides/
  macro: photonic-systems
- slug: gallium-nitride
  name: Gallium Nitride
  path: /energy-power/power-electronics/gallium-nitride/
  macro: energy-power
---
Self-emissive inorganic (GaN-family) LED arrays at micron pixel pitch, used as the light
engine in AR/smart glasses. The reason it matters for an always-on device is power:
microLED is **emissive**, so a dark pixel draws no current, and AR content is sparse
(text, a notification, a few glyphs on black). A modulated engine — LCoS or DLP — burns
full illumination power regardless of what is lit. See [Emissive vs modulated display architectures](/photonic-systems/displays/emissive-display/) for that
distinction, which is the load-bearing one.

## The binding constraint: red EQE at small pitch

Nothing about microLED for AR resolves until red does. Two materials routes, both hurting:

- **AlGaInP** (the conventional red) degrades catastrophically below ~10 µm pixel pitch —
  sidewall damage from the mesa etch dominates as the perimeter-to-area ratio rises.
- **GaN-based red** suffers high surface recombination at small pitch.

The consequence, verified 9 Aug 2026: **no monolithic RGB microLED is shipping in volume
anywhere.** Every shipping waveguide AR product uses either monochrome green
(**Jade Bird Display Jbd** in Vuzix Z100, INMO GO 2) or a 3-panel X-cube that optically
combines separate R, G and B arrays. Monolithic RGB exists as prototype only.

## Who is where (9 Aug 2026)

## The number discipline

Panel brightness is not the number. Waveguide throughput is 1-5%, so a 500,000-nit panel
may deliver 500-2,500 nits to the eye — barely adequate outdoors. **Always demand
system-level, post-waveguide nits-at-eye or lumens, never panel nits.** Most vendor claims
in this space are panel-level.
