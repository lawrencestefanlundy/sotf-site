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
mention_count: 1377
descendants: []
last_reorg_date: '2026-05-13'
sources_7d: 1
sources_30d: 9
recent_mentions:
- slug: 2026-07-25-thoughts-on-ai-and-power
  title: Thoughts on AI and power
  date: '2026-07-25'
  kind: web
- slug: 2026-07-24-trust-stamp-selected-for-eu-advanced-semiconductor-technolog
  title: Trust Stamp selected for EU advanced semiconductor technology initiative - Proactive Investors
  date: '2026-07-24'
  kind: web
- slug: 2026-07-16-china-open-weight-strategy-loeber-teortaxes
  title: Why does China keep releasing open-weight models? — Loeber + Teortaxes threads (K3 week)
  date: '2026-07-16'
  kind: web
- slug: 2026-07-13-chips-act-20-targets-european-semiconductor-demand-as-eu-exp
  title: Chips Act 2.0 Targets European Semiconductor Demand as EU Expands AI Strategy - Astute Group
  date: '2026-07-13'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-13-sk-hynix-record-fall-hbm4-three-supplier
  title: SK Hynix record one-day fall as HBM4 goes three-supplier
  date: '2026-07-13'
  kind: web
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-07-09-munichs-quantumdiamonds-raises-91-million-to-scale-its-quant
  title: Munich’s QuantumDiamonds raises €91 million to scale its quantum-based semiconductor inspection technology - EU-Startups
  date: '2026-07-09'
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
