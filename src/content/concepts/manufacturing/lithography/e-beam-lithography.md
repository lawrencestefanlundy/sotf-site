---
type: concept
slug: e-beam-lithography
canonical_name: E-Beam Lithography
aliases:
- e-beam lithography
- electron-beam lithography
- EBL
- EBL (semiconductor)
kind: technology
parent_concepts:
- manufacturing
- lithography
related_concepts:
- maskless-lithography
- directed-self-assembly
- nanoimprint-lithography
- high-na-euv-lithography
- photoresists
sources:
- '[[2024-11-05-confidential-ai-the-dog-that-didnt]]'
- '[[2023-06-15-e04-no10-downing-street-and-vector]]'
- '[[2023-07-27-e10-pushing-moores-law-to-the-limit]]'
- '[[2023-10-06-e18-the-state-of-silent-speech-and]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-18-e11-in-conversation-with-lux-capital]]'
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2025-11-05-consensus-capital]]'
- '[[2025-01-27-ai-for-nuclear-fusion-feat-martin]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2024-10-29-deploy-intelligence-too-cheap-to]]'
- '[[2023-05-31-three-underrated-technologies-from]]'
- '[[2023-11-20-e21-can-we-make-enough-ai-chips]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2023-03-05-interview-dr-hyoduk-shin-professor]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-08-25-e12-nanomechanical-computing-gears]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2026-01-22-ai-chips-computeram-and-the-future]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
frontier:
- Can multi-beam e-beam (IMS Nanofabrication, Multibeam Corporation) close the throughput gap to optical tools at 300 mm wafer scale by 2030?
- Does direct-write e-beam at single-wafer rates (ARM-on-photolithography research threads) reach a commercial pilot by 2030, or does High-NA EUV foreclose the market?
- What is the practical resolution floor for e-beam in production resists — does resist blur or forward/back-scatter dominate at sub-5 nm?
last_updated: '2026-06-02'
tags:
- concept
- technology
mention_count: 1331
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 4
recent_mentions:
- slug: 2026-08-13-rochester-region-sees-semiconductor-growth-from-chips-act-in
  title: Rochester region sees semiconductor growth from CHIPS Act investments - Rochester Business Journal
  date: '2026-08-13'
  kind: web
- slug: 2026-08-12-chips-act-20-part-1-europes-second-semiconductor-push---eene
  title: 'Chips Act 2.0. Part 1: Europe’s second semiconductor push - eeNews Europe'
  date: '2026-08-12'
  kind: web
- slug: 2026-08-10-esd-cable-management-trays-market-to-reach-178-index-by-2035
  title: ESD Cable Management Trays Market to Reach 178 Index by 2035 on Semiconductor Fab Build-Out - IndexBox
  date: '2026-08-10'
  kind: web
- slug: 2026-08-10-chips-act-funding-opportunities-what-companies-in-the-semico
  title: 'CHIPS Act Funding Opportunities: What Companies in the Semiconductor Ecosystem Need to Know - Mayer Brown'
  date: '2026-08-10'
  kind: web
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-08-06-us-commits-874m-to-strengthen-semiconductor-supply-chain-thr
  title: US commits $874m to strengthen semiconductor supply chain through CHIPS Act - Innovation News Network
  date: '2026-08-06'
  kind: web
- slug: 2026-08-03-spad-single-photon-market-scan
  title: SPAD / single-photon detector market scan — incumbent structure and company cohort
  date: '2026-08-03'
  kind: web
- slug: 2026-08-03-uk-chip-firm-olix-valued-at-more-than-2bn-after-major-invest
  title: UK chip firm OLIX valued at more than £2bn after major investment - UKTN
  date: '2026-08-03'
  kind: web
neighbors:
- slug: maskless-lithography
  name: Maskless Lithography
  path: /manufacturing/lithography/maskless-lithography/
  macro: manufacturing
- slug: directed-self-assembly
  name: Directed Self-Assembly
  path: /manufacturing/lithography/directed-self-assembly/
  macro: manufacturing
- slug: nanoimprint-lithography
  name: Nanoimprint Lithography
  path: /manufacturing/lithography/nanoimprint-lithography/
  macro: manufacturing
- slug: high-na-euv-lithography
  name: High-NA EUV Lithography
  path: /manufacturing/lithography/high-na-euv-lithography/
  macro: manufacturing
- slug: photoresists
  name: Photoresists (incl. EUV resists)
  path: /manufacturing/lithography/photoresists/
  macro: manufacturing
---
## Physics / mechanism

Electron-beam lithography (EBL) fires a focused beam of electrons (typically 10–100 keV) across a resist-coated substrate in a rasterised or vector scan, exposing patterns without a physical mask. Resolution is limited by electron scattering in the resist rather than diffraction, enabling sub-10 nm half-pitch features; leading tools (JEOL JBX-9500, Raith EBPG) achieve ~2–4 nm resolution with ~1 nm placement accuracy. Throughput is the fundamental constraint: writing a full 300 mm wafer at high resolution takes hours vs. seconds for optical tools. EBL is the workhorse for mask/reticle fabrication, photonic IC prototyping, quantum device patterning, and research-scale compound semiconductor work.

## Competitive landscape

---

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Can multi-beam e-beam (IMS Nanofabrication, Multibeam Corporation) close the throughput gap to optical tools at 300 mm wafer scale by 2030?
- Does direct-write e-beam at single-wafer rates (ARM-on-photolithography research threads) reach a commercial pilot by 2030, or does High-NA EUV foreclose the market?
- What is the practical resolution floor for e-beam in production resists — does resist blur or forward/back-scatter dominate at sub-5 nm?
