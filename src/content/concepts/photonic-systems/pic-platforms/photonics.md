---
type: concept
slug: photonics
canonical_name: Photonics
aliases:
- photonics-optics
- Photonics & Optics
kind: theme
parent_concepts:
- photonic-systems
- pic-platforms
related_concepts: []
sources:
- '[[2025-09-23-the-compute-gradient]]'
- '[[2025-04-23-what-if-ai-can-already-feel]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-08-31-e13-chiplets-how-chip-lego-is-driving]]'
- '[[2023-06-23-e05-the-future-of-edge-ai-brain-inspired]]'
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2024-12-16-willow-and-the-race-to-quantum-advantage]]'
- '[[2024-12-04-cubits-in-a-fridge-why-is-nobody]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2022-12-15-im-doing-research-in-venture-capital]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2026-07-17-the-once-and-future-kimi]]'
- '[[2025-02-12-wen-babelfish-feat-aron-of-semron]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
frontier:
- Photon-photon gates look fundamentally fidelity-limited under realistic imperfections while linear cluster states survive; does photonic quantum computing consolidate on measurement-based architectures, and what demonstrated gate fidelity would reverse that?
- Can a monolithic on-chip isolator close the gap from ~20 dB insertion loss to the ~1-3 dB a usable link budget needs, while keeping a mass-production-compatible process (local laser annealing or an alternative)?
- Does ML-driven inverse design (surrogate EM solvers, generative/diffusion design) become a standalone photonic EDA value pool with a foundry-endorsed flow, or stay an in-house tool at incumbents like STMicroelectronics?
- Telecom-band quantum-dot photon sources are now rack-integrated with >50% transmission; when does a fielded network pick them over SPDC sources, and is that component market venture-scale?
- Where does datacentre optics value settle between pluggables, co-packaged optics, and optical switching? Evidence this cycle is research-side only; needs market-side sources to update.
- Do 2D/TMD and diamond photonic materials get a credible high-volume manufacturing route by 2028, or stay lab platforms?
last_updated: '2026-07-26'
tags:
- concept
- theme
mention_count: 907
descendants:
- diffractive-deep-neural-network
- free-space-photonics
- microwave-photonics
- mid-ir-photonics
- optical-frequency-comb
- optical-frequency-division
- optoelectronic-oscillator
last_reorg_date: '2026-05-13'
sources_7d: 2
sources_30d: 10
recent_mentions:
- slug: 2026-07-22-photonics21-welcomes-chips-act-20-inclusion-of-photonics---o
  title: Photonics21 welcomes Chips Act 2.0 inclusion of photonics - Optics.org
  date: '2026-07-22'
  kind: web
- slug: 2026-07-21-niac-2026-selections
  title: NIAC 2026 Selections
  date: '2026-07-21'
  kind: web
- slug: 2026-07-17-the-once-and-future-kimi
  title: The Once and Future Kimi
  date: '2026-07-17'
  kind: substack
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-07-11-neutral-pdk-heterogeneous-integration-landscape
  title: Neutral PDK / EDA layer for heterogeneous photonic integration — landscape check (Scintil essay correction research)
  date: '2026-07-11'
  kind: web
- slug: 2026-07-02-pilot-photonics-awarded-104-mln-from-european-innovation-cou
  title: Pilot Photonics Awarded €10.4 Mln From European Innovation Council - TradingView
  date: '2026-07-02'
  kind: web
- slug: 2026-07-02-pilot-photonics-awarded-104-million-from-european-innovation
  title: PILOT PHOTONICS AWARDED €10.4 MILLION FROM EUROPEAN INNOVATION COUNCIL - PR Newswire
  date: '2026-07-02'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
neighbors: []
---
## Physics / mechanism

Photonics is the generation, manipulation, and detection of photons across UV, visible, near-IR, and mid-IR. Photons carry no charge and no rest mass, so optical signals move with low loss and no resistive heating; the cost is that photons barely interact with each other, so switching, gain, memory, and non-reciprocity all need an intermediating material. Nearly every platform battle in the field is a fight over which material stack best mediates light-matter interaction while staying manufacturable.

Sub-field map (this page is the orientation layer; depth belongs on child pages such as [Free-Space Photonics](/communications/fibre-and-free-space/free-space-photonics/), **Microwave Photonics**, [Mid-Infrared Photonics](/photonic-systems/light-sources/mid-ir-photonics/), **Optical Frequency Comb**):

## Competitive landscape

Silicon photonics competes with and complements III-V (InP, GaAs) and the emerging SiN and thin-film lithium niobate platforms. The trade is always among loss, nonlinearity, active gain, and CMOS-foundry compatibility: silicon is cheap and foundry-native but has no gain and no second-order nonlinearity; SiN is the low-loss passive; InP has monolithic lasers at higher cost; LNOI brings fast electro-optics but hybrid integration. No fresh source this cycle re-benchmarks the platform loss/bandwidth numbers, so specific dB/cm and GHz figures previously quoted here are dropped rather than restated (medium confidence they are still roughly right; re-cite before reuse).

A second battle is moving up the stack, from devices to design. Inverse design is becoming the bottleneck and the opportunity: FDTD-trained convolutional surrogates plus diffusion-model generative design now hit R^2 of about 0.97 on metasurfaces over 230x larger than the training apertures, in work affiliated with STMicroelectronics **2026 07 24 Design And Optimization Of Metasurfaces For Silicon Photonic**. That supports the view that a photonic design/EDA layer is forming (**Photonic Pdk Eda Layer**, **Electron Informed Materials Discovery**).

Where value is moving, on current evidence: (1) datacentre optical interconnect remains the volume driver (own synthesis, **2026 02 02 Photonic Engines For Data Centers**; this cycle's tier-1 flow is research-side, so the market read is medium confidence and not freshly re-verified); (2) quantum photonic components (sources, isolators, polarization control **2026 07 24 Compact Deterministic Liquid Crystal Polarization Controller**) are crossing from lab to deployable hardware, a component-vendor opportunity that exists whichever quantum modality wins; (3) design automation for photonics is separating into its own layer.

## Investment routing

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

## Merged from `photonics-optics` (archived 2026-05-07)

*Hyphenated variant. Photonics is the canonical concept; 'photonics-optics' was an Attio-tag-derived duplicate (kind: technology,  at merge). Its prose duplicated the sections above and was folded into the main body on re-synthesis 2026-07-26; the Dataview blocks below are kept because companies and sources still carry the legacy `photonics-optics` tag.*

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
