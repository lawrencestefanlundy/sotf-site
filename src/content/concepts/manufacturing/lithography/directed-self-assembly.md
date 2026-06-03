---
type: concept
slug: directed-self-assembly
canonical_name: Directed Self-Assembly
aliases:
- DSA
- directed self-assembly
parent_concepts:
- lithography
related_concepts:
- e-beam-lithography
- nanoimprint-lithography
- photoresists
- computational-lithography
- high-na-euv-lithography
sources: []
frontier:
- Does DSA survive the High-NA EUV ramp — is it still needed once 0.55 NA EUV delivers single-exposure 8 nm half-pitch?
- Can block-copolymer self-assembly periods reach sub-5 nm reliably in volume production, or does phase separation noise degrade CD uniformity beyond spec?
- Does Imec's DSA programme convert any proof-of-concept result into a semiconductor customer process-of-record before 2030?
last_updated: '2026-06-02'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: e-beam-lithography
  name: E-Beam Lithography
  path: /sotf-site/manufacturing/lithography/e-beam-lithography/
  macro: manufacturing
- slug: nanoimprint-lithography
  name: Nanoimprint Lithography
  path: /sotf-site/manufacturing/lithography/nanoimprint-lithography/
  macro: manufacturing
- slug: photoresists
  name: Photoresists (incl. EUV resists)
  path: /sotf-site/manufacturing/lithography/photoresists/
  macro: manufacturing
- slug: computational-lithography
  name: Computational Lithography
  path: /sotf-site/manufacturing/lithography/computational-lithography/
  macro: manufacturing
- slug: high-na-euv-lithography
  name: High-NA EUV Lithography
  path: /sotf-site/manufacturing/lithography/high-na-euv-lithography/
  macro: manufacturing
---
Directed self-assembly (DSA) is a lithographic patterning technique in which block copolymers (BCPs) — polymer chains with two chemically distinct, immiscible segments — spontaneously phase-separate into periodic nanoscale structures (lamellae, cylinders, spheres) when annealed on a pre-patterned or chemically functionalised substrate. The guiding pattern (produced by conventional optical lithography or e-beam) directs the BCP domains into the desired device geometry, effectively multiplying pattern frequency without additional mask exposures. Characteristic periods for leading BCP systems (PS-b-PMMA, PS-b-P2VP) reach 10–20 nm; high-chi BCPs (e.g., PS-b-PDMS) target sub-10 nm half-pitch.

The mechanism is thermodynamic rather than optical: resolution is set by the BCP molecular weight and Flory-Huggins interaction parameter (chi), not by wavelength or numerical aperture. This decouples feature size from light source energy — in principle enabling sub-5 nm patterning with 193 nm guiding optics.

In practice, DSA has been "five years from production" since approximately 2010. Yield-limiting defects (disclinations, dislocation density, BCP domain grain boundaries) remain unsolved at the CD uniformity required for leading-edge logic. Imec's DSA roadmap consistently publishes proof-of-concept patterns at sub-10 nm but flags unresolved yield at production scale. The **Beyond Euv Not In 2020S** thesis holds that DSA does not reach HVM as a leading-edge lithography step by 2030, reinforced by the fact that High-NA EUV already addresses the nodes DSA targets.

## Frontier

- Does DSA survive the High-NA EUV ramp — is it still needed once 0.55 NA EUV delivers single-exposure 8 nm half-pitch?
- Can block-copolymer self-assembly periods reach sub-5 nm reliably in volume production, or does phase separation noise degrade CD uniformity beyond spec?
- Does Imec's DSA programme convert any proof-of-concept result into a semiconductor customer process-of-record before 2030?
