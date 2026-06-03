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
sources: []
frontier:
- Can GaSb/InAs-based photonic ICs reach the integration density of silicon photonics, or does the heterogeneous-on-Si bonding approach remain the practical route to chip-scale mid-IR systems?
- What is the achievable limit-of-detection for breath-based VOC diagnostics using mid-IR absorption spectroscopy before interferent gases and humidity dominate?
- Will interband cascade lasers (ICLs) displace QCLs below 5 µm emission on power budget, or does QCL wall-plug efficiency close the gap at room temperature?
last_updated: 2026-06-02
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: quantum-cascade-lasers
  name: Quantum Cascade Lasers
  path: /sotf-site/photonic-systems/light-sources/quantum-cascade-lasers/
  macro: photonic-systems
- slug: hgcdte
  name: Mercury Cadmium Telluride
  path: /sotf-site/photonic-systems/modulators-detectors/hgcdte/
  macro: photonic-systems
- slug: sensing-imaging
  name: Sensing & Imaging
  path: /sotf-site/sensing/imaging/sensing-imaging/
  macro: sensing
- slug: spectral-sensing
  name: Spectral Sensing
  path: /sotf-site/sensing/mems/spectral-sensing/
  macro: sensing
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /sotf-site/communications/fibre-and-free-space/free-space-photonics/
  macro: communications
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /sotf-site/materials/substrates/compound-semiconductors/
  macro: materials
- slug: photonic-imaging
  name: Photonic Imaging
  path: /sotf-site/sensing/imaging/photonic-imaging/
  macro: sensing
---
**Mid-infrared (mid-IR) photonics** covers the wavelength range of ~2–20 µm, encompassing the **molecular fingerprint region** (6–20 µm) and the atmospheric transmission windows (MWIR 3–5 µm, LWIR 8–12 µm). The fundamental importance of the mid-IR is that most small molecules (CO₂, CH₄, NH₃, NO, SO₂, benzene, acetone) have strong rotational-vibrational absorption lines here — orders of magnitude stronger than in the near-IR — enabling parts-per-billion concentration detection via laser absorption spectroscopy.

The dominant sources are **quantum cascade lasers (QCLs)**, which exploit intersubband transitions in a periodic InGaAs/AlInAs or GaAs/AlGaAs heterostructure to emit at designer wavelengths from ~3–25 µm without being bound by the material bandgap. Interband cascade lasers (ICLs) extend coverage below 4 µm with lower threshold current. Detectors are dominated by [Mercury Cadmium Telluride](/sotf-site/photonic-systems/modulators-detectors/hgcdte/) focal-plane arrays and thermoelectrically cooled HgCdTe single elements; uncooled microbolometers serve lower-sensitivity applications. Integration is the frontier: GaSb-on-Si heterogeneous bonding and quantum-dot-based mid-IR emitters on CMOS aim to replicate the scaling dynamic of [Silicon Photonics](/sotf-site/photonic-systems/pic-platforms/silicon-photonics/) in the mid-IR.

The active thesis **Mid Ir Photonic Sensing** maps the industrial gas-analysis and breath-diagnostics opportunity, tracking [Quantum Cascade Lasers](/sotf-site/photonic-systems/light-sources/quantum-cascade-lasers/) as the enabling source and chip-level integration as the cost lever that displaces NDIR and electrochemical incumbents.

## Frontier

- Can GaSb/InAs-based photonic ICs reach the integration density of silicon photonics, or does the heterogeneous-on-Si bonding approach remain the practical route to chip-scale mid-IR systems?
- What is the achievable limit-of-detection for breath-based VOC diagnostics using mid-IR absorption spectroscopy before interferent gases and humidity dominate?
- Will interband cascade lasers (ICLs) displace QCLs below 5 µm emission on power budget, or does QCL wall-plug efficiency close the gap at room temperature?
