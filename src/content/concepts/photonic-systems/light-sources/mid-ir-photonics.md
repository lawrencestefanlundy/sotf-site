---
type: concept
slug: mid-ir-photonics
canonical_name: Mid-Infrared Photonics
aliases:
- mid-IR
- mid-infrared
- MIR photonics
- quantum cascade laser
parent_concepts:
- photonics
- photonic-integrated-circuits
related_concepts:
- quantum-cascade-lasers
- hgcdte
- sensing-imaging
- spectral-sensing
- free-space-photonics
- compound-semiconductors
- photonic-imaging
sources:
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-05-24-mose2-exciton-polariton-all-optical-switch]]'
- '[[2023-10-05-nynomic-nlir-investment]]'
- '[[2026-06-17-single-photon-detector-market-spad-snspd]]'
frontier:
- Can GaSb/InAs-based photonic ICs reach the integration density of silicon photonics, or does the heterogeneous-on-Si bonding approach remain the practical route to chip-scale mid-IR systems?
- What is the achievable limit-of-detection for breath-based VOC diagnostics using mid-IR absorption spectroscopy before interferent gases and humidity dominate?
- Will interband cascade lasers (ICLs) displace QCLs below 5 µm emission on power budget, or does QCL wall-plug efficiency close the gap at room temperature?
last_updated: 2026-06-02
tags:
- concept
mention_count: 102
sources_7d: 2
sources_30d: 17
recent_mentions:
- slug: 2026-06-17-single-photon-detector-market-spad-snspd
  title: Single-photon detector market aggregation — SPAD, SiPM, SNSPD (2024–2035)
  date: '2026-06-17'
  kind: web
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2023-10-05-nynomic-nlir-investment
  title: 'Nynomic AG: Expansion of technology portfolio / investment in NLIR ApS'
  date: '2023-10-05'
  kind: web
neighbors:
- slug: quantum-cascade-lasers
  name: Quantum Cascade Lasers
  path: /photonic-systems/light-sources/quantum-cascade-lasers/
  macro: photonic-systems
- slug: hgcdte
  name: Mercury Cadmium Telluride
  path: /photonic-systems/modulators-detectors/hgcdte/
  macro: photonic-systems
- slug: sensing-imaging
  name: Sensing & Imaging
  path: /sensing/imaging/sensing-imaging/
  macro: sensing
- slug: spectral-sensing
  name: Spectral Sensing
  path: /sensing/mems/spectral-sensing/
  macro: sensing
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /communications/fibre-and-free-space/free-space-photonics/
  macro: communications
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /materials/substrates/compound-semiconductors/
  macro: materials
- slug: photonic-imaging
  name: Photonic Imaging
  path: /sensing/imaging/photonic-imaging/
  macro: sensing
---
**Mid-infrared (mid-IR) photonics** covers the wavelength range of ~2–20 µm, encompassing the **molecular fingerprint region** (6–20 µm) and the atmospheric transmission windows (MWIR 3–5 µm, LWIR 8–12 µm). The fundamental importance of the mid-IR is that most small molecules (CO₂, CH₄, NH₃, NO, SO₂, benzene, acetone) have strong rotational-vibrational absorption lines here — orders of magnitude stronger than in the near-IR — enabling parts-per-billion concentration detection via laser absorption spectroscopy.

The dominant sources are **quantum cascade lasers (QCLs)**, which exploit intersubband transitions in a periodic InGaAs/AlInAs or GaAs/AlGaAs heterostructure to emit at designer wavelengths from ~3–25 µm without being bound by the material bandgap. Interband cascade lasers (ICLs) extend coverage below 4 µm with lower threshold current. Detectors are dominated by [Mercury Cadmium Telluride](/photonic-systems/modulators-detectors/hgcdte/) focal-plane arrays and thermoelectrically cooled HgCdTe single elements; uncooled microbolometers serve lower-sensitivity applications. Integration is the frontier: GaSb-on-Si heterogeneous bonding and quantum-dot-based mid-IR emitters on CMOS aim to replicate the scaling dynamic of [Silicon Photonics](/photonic-systems/pic-platforms/silicon-photonics/) in the mid-IR.

The active thesis **Mid Ir Photonic Sensing** maps the industrial gas-analysis and breath-diagnostics opportunity, tracking [Quantum Cascade Lasers](/photonic-systems/light-sources/quantum-cascade-lasers/) as the enabling source and chip-level integration as the cost lever that displaces NDIR and electrochemical incumbents.

## Frontier

- Can GaSb/InAs-based photonic ICs reach the integration density of silicon photonics, or does the heterogeneous-on-Si bonding approach remain the practical route to chip-scale mid-IR systems?
- What is the achievable limit-of-detection for breath-based VOC diagnostics using mid-IR absorption spectroscopy before interferent gases and humidity dominate?
- Will interband cascade lasers (ICLs) displace QCLs below 5 µm emission on power budget, or does QCL wall-plug efficiency close the gap at room temperature?
