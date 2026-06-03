---
type: concept
slug: gnss-pnt
canonical_name: GNSS / PNT
aliases:
- GNSS
- PNT
- positioning navigation timing
- Global Navigation Satellite System
parent_concepts: []
related_concepts:
- leo-mega-constellations
- space-communications
- optical-inter-satellite-links
sources: []
frontier:
- Can LEO PNT constellations (e.g. Xona Space) achieve sub-10 cm accuracy globally without augmentation?
- What is the minimum viable constellation size for cislunar PNT at decimeter accuracy?
- How resilient is GPS-denied navigation based on LEO signal-of-opportunity (SoOP) approaches?
last_updated: 2026-06-02
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: leo-mega-constellations
  name: LEO Mega-Constellations
  path: /sotf-site/life-frontier/in-orbit/leo-mega-constellations/
  macro: life-frontier
- slug: space-communications
  name: Space Communications
  path: /sotf-site/life-frontier/in-orbit/space-communications/
  macro: life-frontier
- slug: optical-inter-satellite-links
  name: Optical Inter-Satellite Links
  path: /sotf-site/life-frontier/in-orbit/optical-inter-satellite-links/
  macro: life-frontier
---
Global Navigation Satellite System (GNSS) is the umbrella term for satellite constellations that broadcast precise timing signals allowing receivers to compute their position, navigation, and timing (PNT) via trilateration. GPS (US), GLONASS (Russia), Galileo (EU), and BeiDou (China) are the four operational global systems. Accuracy depends on the number of satellites in view, atmospheric delay modelling (ionospheric and tropospheric corrections), and receiver quality — standalone GPS delivers ~3 m CEP; differential/RTK corrections reduce this to centimetre-level.

The strategic problem: current GNSS constellations orbit at medium Earth orbit (MEO, ~20,200 km), which produces relatively weak received signals (~-130 dBm at ground), making receivers vulnerable to jamming and spoofing. This is a front-line issue in contested environments (Ukraine, GPS-denied urban canyons). New LEO PNT architectures exploit stronger signal geometry and shorter propagation time to improve both accuracy and anti-jam margin, but require larger constellations to maintain continuous coverage.

The lunar extension (**Lunar Pnt Infrastructure**) is an open engineering problem: no operational PNT service covers cislunar space or the lunar surface, forcing current missions to rely on Earth-based DSN ranging, which gives kilometre-level lunar accuracy and requires dedicated DSN time.

## Frontier

- Can LEO PNT constellations achieve sub-10 cm accuracy globally without augmentation?
- What is the minimum viable constellation size for cislunar PNT at decimeter accuracy?
- How resilient is GPS-denied navigation based on LEO signal-of-opportunity (SoOP)?
