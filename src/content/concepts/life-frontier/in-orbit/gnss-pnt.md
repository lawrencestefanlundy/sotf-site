---
type: concept
slug: gnss-pnt
canonical_name: GNSS / PNT
aliases:
- GNSS
- PNT
- positioning navigation timing
- Global Navigation Satellite System
parent_concepts:
- in-orbit
- life-frontier
related_concepts:
- leo-mega-constellations
- space-communications
- optical-inter-satellite-links
sources:
- '[[2026-01-06-delfts-qualinx-raises-20m-to-bring-ultra-low-power-gnss-chip]]'
- '[[2024-06-03-conexio-stratus-pro-a-battery-powered-nrf9161-development-ki]]'
frontier:
- Can LEO PNT constellations (e.g. Xona Space) achieve sub-10 cm accuracy globally without augmentation?
- What is the minimum viable constellation size for cislunar PNT at decimeter accuracy?
- How resilient is GPS-denied navigation based on LEO signal-of-opportunity (SoOP) approaches?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 12
scorecard:
  viability: null
  drivers: null
  novelty: null
  diffusion: null
  impact: null
  timing_band: Unclear
  verdict: ''
scorecard_status: draft
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-01-06-delfts-qualinx-raises-20m-to-bring-ultra-low-power-gnss-chip
  title: Delft’s Qualinx raises €20M to bring ultra-low-power GNSS chip to market - Bits&Chips
  date: '2026-01-06'
  kind: web
- slug: 2024-06-03-conexio-stratus-pro-a-battery-powered-nrf9161-development-ki
  title: Conexio Stratus Pro – A battery-powered nRF9161 development kit with LTE IoT, DECT NR+, GNSS connectivity (Crowdfunding) - CNX Software
  date: '2024-06-03'
  kind: web
neighbors:
- slug: leo-mega-constellations
  name: LEO Mega-Constellations
  path: /life-frontier/in-orbit/leo-mega-constellations/
  macro: life-frontier
- slug: space-communications
  name: Space Communications
  path: /life-frontier/in-orbit/space-communications/
  macro: life-frontier
- slug: optical-inter-satellite-links
  name: Optical Inter-Satellite Links
  path: /life-frontier/in-orbit/optical-inter-satellite-links/
  macro: life-frontier
---
**GNSS/PNT is the satellite positioning, navigation and timing layer that almost all modern infrastructure silently depends on, and the current research frontier is not better satellites but detecting, attributing and surviving deliberate jamming and spoofing of it.**

## Summary

Global navigation satellite systems (GPS, Galileo, GLONASS, BeiDou and their augmentations) deliver position and time by broadcasting extremely weak ranging signals from medium Earth orbit. A receiver correlates those signals, solves for its own position and clock offset, and in doing so becomes a source of both navigation and of precise time. Because the signals arrive at power levels near the thermal noise floor, they are trivially overpowered by a local transmitter (jamming) or replaced by a plausible counterfeit (spoofing). That physical asymmetry, rather than any deficiency in the space segment, is what defines the technology's present problem set.

The body of work now forming around GNSS/PNT is therefore mostly a resilience layer. It has four strands. First, detection and classification of interference at or near the receiver: compressing raw GNSS streams and classifying jamming or spoofing in real time on edge hardware such as a Google Edge TPU using variational autoencoders, or folding GNSS jamming classification into a multi-task RF recognition accelerator that reports 99.5% accuracy on a GNSS jamming dataset with 98 microsecond per-frame latency. Second, geolocation of emitters: reinforcement-learning agents that actively move a 2x2 patch antenna to disambiguate multipath-corrupted snapshots, and received-power plus time-difference-of-arrival methods applied to reference-station networks. Third, space-based monitoring: using GNSS reflectometry delay-Doppler maps from the CYGNSS constellation to spot terrestrial RFI, where constellation size drives detection latency and coverage. Fourth, architectural defences and alternative PNT, including anchor-rooted recovery for spoofed UAV swarms and terrestrial LPWAN time-difference-of-arrival positioning for cases where GNSS is ruled out by energy cost or indoor operation.

The parameters that decide outcomes are: how much interference power and geographic reach an adversary can field (a space-based interferer changes the scale entirely, and one has been identified as a constellation of Russian early warning satellites in Molniya orbits causing wide-area events over Europe, Greenland and Canada since 2019); how many sensors a monitoring network has, since gains from adding satellites are steepest between one and three; the power and cost budget for putting detection into receivers, which is why ultra-low-power GNSS silicon matters commercially <sup class="ref"><a href="https://news.google.com/rss/articles/CBMipgFBVV95cUxNQ1dzLW1jcGxyc3UxQXlWRVRXcFNXRGJEXzF2UWk3dzlSZ25fOTh5RXJmWU13Q2g3ZGlpS3REekFYTGgyWmZMdUUyWFRuSVB1WTB4UkhxU2RMbGxpaVFXTjUtSWRDOEJrbVQ0MVZxTUg2OWp6REJrQk9nMGVvNE9sT1lHVUlTc0N2VW14R2JqYWgtV2ZSdzZHZjZldnBzWFdNUUFlV3pR?oc=5" title="Delft’s Qualinx raises €20M to bring ultra-low-power GNSS chip to market - Bits&Chips" rel="noopener">ref</a></sup>; and whether a defence has access to an absolute positional reference rather than only relative geometry, which is provably insufficient against a rigid translation.

## Viability (unscored)

## Drivers (unscored)

## Novelty (unscored)

## Diffusion (unscored)

## Impact (unscored)

## Timing Unclear

---
*Assessment drafted 2026-08-31 from up to 11 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
