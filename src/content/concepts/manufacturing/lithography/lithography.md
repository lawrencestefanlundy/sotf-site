---
type: concept
slug: lithography
canonical_name: Lithography
aliases: []
kind: technology
parent_concepts:
- manufacturing
- lithography
related_concepts: []
sources:
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-06-11-semianalysis-intel-should-raise-capital]]'
- '[[2026-05-02-euv-lithography-wikipedia]]'
- '[[2026-06-14-frontier-ai-value-capture]]'
- '[[2026-03-14-semianalysis-patel-bottlenecks]]'
- '[[2026-05-02-asml-euv-lithography-systems]]'
- '[[2026-05-30-intel-glass-substrates-program]]'
- '[[2026-01-08-semianalysis-apple-tsmc]]'
- '[[2026-01-13-semianalysis-interconnects-beyond-copper]]'
- '[[2023-12-06-euv-lithography-but-with-a-free-electron-laser]]'
- '[[2025-01-06-radiant-acquires-nilt]]'
- '[[2026-05-12-semianalysis-eda-rtl-to-silicon]]'
- '[[2026-06-14-semianalysis-smic-n3-vs-intel-18a]]'
- '[[2026-06-03-semianalysis-space-datacenters]]'
- '[[2026-05-02-two-photon-lithography-for-integrated-photonic-packaging-lig]]'
frontier:
- Lithography as three-way optimisation (throughput / feature size / feature complexity) — does any single tool win on all three, or does the market remain a portfolio of specialised tools each winning on two?
- Multi-material patterning at production volume — does a tool emerge that patterns dissimilar materials in the same step, or does multi-material foundry remain a retrofit (transfer printing, hybrid integration, post-processing)?
- ASML chokepoint resilience — TSMC's roadmap is gated on EUV ship rate. What's the bear case for ASML output bottleneck (geopolitics, Veldhoven workforce, parts supply chain) materially constraining global compute output 2027-2030?
- Photonic-specific lithography wedge — at what segment volume does dedicated photonics-lithography (Cnuic, SWHL, Eulitha) economics beat immersion-on-CMOS retrofit?
last_updated: '2026-05-08'
tags:
- concept
- technology
mention_count: 120
descendants:
- computational-lithography
- directed-self-assembly
- duv-immersion-lithography
- e-beam-lithography
- electron-beam-lithography
- euv-light-sources
- high-na-euv-lithography
- lithography
- lithography-tools
- mask-blank-manufacturing
- maskless-lithography
- nanoimprint-lithography
- photonic-manufacturing
- photoresists
- two-photon-polymerization
- x-ray-lithography
- xolography
last_reorg_date: '2026-05-13'
sources_7d: 4
sources_30d: 27
recent_mentions:
- slug: 2026-06-14-frontier-ai-value-capture
  title: 'Frontier AI value capture: where the $4T accrues (research synthesis)'
  date: '2026-06-14'
  kind: web
- slug: 2026-06-14-semianalysis-smic-n3-vs-intel-18a
  title: Is SMIC N+3's Metal Pitch Smaller than Intel 18A's?
  date: '2026-06-14'
  kind: web
- slug: 2026-06-11-semianalysis-intel-should-raise-capital
  title: Intel Should Raise Capital
  date: '2026-06-11'
  kind: web
- slug: 2026-06-03-semianalysis-space-datacenters
  title: 'To Boldly Go: The Case for Space Datacenters'
  date: '2026-06-03'
  kind: web
- slug: 2026-05-12-semianalysis-eda-rtl-to-silicon
  title: 'The EDA Primer: From RTL to Silicon'
  date: '2026-05-12'
  kind: web
- slug: 2026-05-02-euv-lithography-wikipedia
  title: EUV Lithography Wikipedia
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-asml-euv-lithography-systems
  title: ASML EUV lithography systems
  date: '2026-05-02'
  kind: web
- slug: 2026-05-02-two-photon-lithography-for-integrated-photonic-packaging-lig
  title: 'Two-photon lithography for integrated photonic packaging (Light: AM 2023)'
  date: '2026-05-02'
  kind: web
neighbors: []
---
## Physics / mechanism

Lithography is the patterning process that defines transistor features, interconnects, and devices on semiconductor wafers by projecting light (or particle beams) through a mask onto photoresist-coated substrates. Resolution is governed by the Rayleigh criterion: R = k₁λ/NA, where k₁ is a process-dependent factor, λ is wavelength, and NA is numerical aperture. EUV (13.5 nm wavelength) is current leading-edge, enabling sub-5 nm nodes at ~200 wafers/hour on ASML's NXE/EXE platforms. Deep-UV (193 nm immersion) remains dominant for mature nodes. Overlay accuracy, dose uniformity, and mask defectivity are the binding constraints at leading edge. High-NA EUV (0.55 NA) is entering HVM, pushing single-exposure resolution below 8 nm half-pitch.

## Competitive landscape

| Technique | Wavelength / Method | Node range | Key players |
|---|---|---|---|
| DUV (193i) | 193 nm immersion | 28 nm–65 nm | ASML, Nikon |
| EUV (Low-NA) | 13.5 nm, 0.33 NA | 5 nm–7 nm | ASML only |
| High-NA EUV | 13.5 nm, 0.55 NA | <2 nm | ASML only |
| Nanoimprint (NIL) | Contact mechanical | ~14 nm | Canon, EV Group |
| e-beam direct-write | Electron beam | Mask-making, R&D | IMS, Raith |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Lawrence's framing

Lithography is the most important machine you've probably never heard of. Every chip in every device you own was patterned by one. The principle: silicon wafer + photoresist + UV through a stencil (photomask) + dissolve/harden + etch. Stack 50-100 patterning steps and at the end you have a chip. *No lithography, no chips. No chips, no computing.*

The market for these machines is a Dutch monopoly. ASML's EUV scanners cost north of $300M each. TSMC, Samsung, and Intel buy almost all of them. **The entire global compute supply chain runs through one car park in Veldhoven.** Those machines are all optimised end-to-end for shrinking transistors. Photonics needs the opposite shape of problem: larger structures sized to the wavelength of light (hundreds of nanometres rather than tens), different materials beyond silicon, three-dimensional geometries. The whole optimisation surface flips. That's the gap that opens space for specialty-lithography startups (see [Maskless Lithography](/sotf-site/manufacturing/lithography/maskless-lithography/), [Two-Photon Polymerization](/sotf-site/manufacturing/lithography/two-photon-polymerization/), [Xolography](/sotf-site/manufacturing/lithography/xolography/)).

## Frontier (open questions)

See frontmatter `frontier:` block.
