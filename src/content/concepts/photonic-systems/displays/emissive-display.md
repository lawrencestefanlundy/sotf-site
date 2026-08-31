---
type: concept
slug: emissive-display
canonical_name: Emissive vs modulated display architectures
aliases:
- emissive display
- self-emissive
- additive display
- modulated display
- emissive vs modulated
related_concepts:
- microled
- laser-beam-scanning
- waveguides
sources: []
frontier:
- Does the volume-leading smart-glasses engine become emissive/additive by 2030, or does modulated LCoS persist because it is simply mature?
- Can any architecture delete the combiner entirely — the 1-5% throughput layer is the largest single efficiency sink in the stack.
last_updated: 2026-08-09
tags:
- concept
descendants:
- microled
parent_concepts:
- displays
- photonic-systems
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors:
- slug: microled
  name: MicroLED microdisplays
  path: /photonic-systems/displays/microled/
  macro: photonic-systems
- slug: laser-beam-scanning
  name: Laser Beam Scanning
  path: /photonic-systems/displays/laser-beam-scanning/
  macro: photonic-systems
- slug: waveguides
  name: Waveguides
  path: /photonic-systems/pic-platforms/waveguides/
  macro: photonic-systems
---
The distinction that decides whether a head-worn display can run **always-on**, and the
one most AR display comparisons skip. It is a power-architecture question, not an image-
quality one.

## The mechanism

- **Modulated** (LCoS, DLP): a separate illumination source runs, and a spatial modulator
 subtracts light to form the image. A black pixel is light that was generated and then
 thrown away. **Power is roughly independent of content.**
- **Emissive** ([MicroLED microdisplays](/photonic-systems/displays/microled/), microOLED) and **additive** (laser beam scanning — the
 lasers simply are not switched on for a dark pixel): only lit pixels consume power.
 **Power scales with content.**

AR content is overwhelmingly sparse — notifications, a few lines of text, a glyph on an
otherwise black field. So for an always-on device the gap between the two is not marginal;
it is the difference between a device you wear all day and one you charge at lunch.

## Why the current volume winner is not the endgame

LCoS leads today because it is **mature**, not because it is efficient: monolithic RGB
microLED is blocked on red EQE at small pitch (see [MicroLED microdisplays](/photonic-systems/displays/microled/)). That makes laser-LCoS a
strong candidate to win 2030 volume **and** to be replaced afterwards.

## The larger lever: deleting the combiner

**Caveat that keeps this honest:** microOLED is emissive but architecturally boxed into
birdbath/prism optics — it cannot reach the ~1-10M nits a waveguide needs, and its
Lambertian emission is étendue-inefficient for waveguide injection. Emissive is necessary,
not sufficient.
