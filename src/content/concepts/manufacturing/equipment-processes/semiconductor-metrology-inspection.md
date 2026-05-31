---
type: concept
slug: semiconductor-metrology-inspection
canonical_name: Semiconductor Metrology & Inspection
aliases:
- metrology
- wafer inspection
- CD-SEM
- overlay metrology
- process control
- APC
kind: technology
parent_concepts:
- metrology-testing
related_concepts:
- lithography
- etch-tools
- electron-scale-metrology
- ald-atomic-layer-deposition
sources: []
frontier:
- Can non-destructive in-line sidewall metrology of gate-all-around fins reach production throughput at sub-3nm, or is destructive cross-section TEM the permanent ceiling?
- What is the minimum viable data set for AI defect classification to outperform KLA's native classifier on a compound-semiconductor substrate where KLA has no training data?
- Will multibeam e-beam inspection (ASML HMI eScan 1100, 25 beams) reach the throughput required for 100% wafer coverage at 3nm volume production, or does it remain a sampling tool?
- Can NV-diamond quantum sensing reach a cycle time below 5 minutes per package for TSV/microbump current-path inspection, making it production-viable by 2030?
- Is wavefront phase imaging (Wooptix Phemet) sufficient for hybrid bonding bow/warpage tolerance at sub-50nm, or does the patterned-surface signal confound the measurement?
last_updated: '2026-05-30'
tags:
- concept
- technology
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: lithography
  name: Lithography
  path: /sotf-site/manufacturing/lithography/lithography/
  macro: manufacturing
- slug: etch-tools
  name: Etch Tools (ALE, plasma etch)
  path: /sotf-site/manufacturing/equipment-processes/etch-tools/
  macro: manufacturing
- slug: ald-atomic-layer-deposition
  name: ALD (Atomic Layer Deposition)
  path: /sotf-site/manufacturing/equipment-processes/ald-atomic-layer-deposition/
  macro: manufacturing
---
Metrology and inspection is the measurement layer that sits between every process step in a semiconductor fab. It answers two questions: did the previous step land where it was supposed to (metrology), and did it create defects that will kill yield (inspection). At advanced nodes, a single defective die at 3nm represents $500 to $2,000 in lost value. Without this layer, yield collapses and the economics of the entire process disintegrate.

---

## Physics / mechanism

**Overlay metrology.** Measures the registration accuracy of one lithographic layer over the previous one. At sub-5nm logic nodes, overlay tolerance is below 2nm. At High-NA EUV nodes (Intel 18A, TSMC N2P), tolerance shrinks to 0.5 to 1nm. The dominant modality is diffraction-based optical scatterometry (KLA Archer series, Onto Innovation OCD tools): broadband light illuminates a grating target and the diffraction spectrum encodes positional offset. The hard physics limit is the diffraction limit itself. Optical overlay tools operate at 0.3 to 0.5nm 3-sigma, which is at or beyond the practical ceiling for High-NA nodes. Every overlay tool in every leading-edge fab needs replacement or augmentation by 2027.

**CD-SEM (Critical Dimension Scanning Electron Microscopy).** The ruler of the fab. A focused electron beam scans a feature; secondary electron yield encodes local geometry. Measures linewidths and feature dimensions at nanometre scale. Hitachi High-Tech and Applied Materials VeritySEM hold a duopoly. Entry barriers are prohibitive: precision electron optics, ultrahigh vacuum, and calibration infrastructure cost $5 to $20M to develop to production standard. Startup opportunity in this sub-segment is effectively zero.

**Broadband plasma (BBP) / optical inspection.** Intense broadband light illuminates the wafer surface in bright-field or dark-field mode. Scattering signals from particles, scratches, and patterning failures are detected by photomultipliers or CCD arrays. KLA Surfscan series dominates. High throughput; limited to surface and near-surface features. Misses buried defects below the first few nm.

**E-beam inspection.** Focused electron beams detect defects at sub-10nm resolution, above the diffraction limit for optical tools. Slower throughput than optical inspection but detects buried and sub-surface defects that optical tools cannot reach. KLA holds the majority of this segment. ASML's HMI eScan 1100 uses 25 parallel beams, achieving up to 15x throughput over single-beam systems, and targets 3nm production volumes. The hard constraint is throughput: single-beam e-beam is too slow for 100% wafer coverage at volume; multibeam arrays solve throughput but require precision column arrays expensive to manufacture and align.

**Scatterometry / OCD (Optical Critical Dimension).** Broadband light illuminates periodic grating structures. The reflected spectrum encodes CD, sidewall profile, overlay offset, and film thickness simultaneously. This is the process control workhorse across leading-edge logic and memory. KLA and Onto Innovation compete here. The active frontier is the inverse problem: fitting a measured spectrum to a geometry model. Physics-based rigorous coupled-wave analysis (RCWA) simulation is computationally expensive and increasingly replaced by ML surrogate models, which solve the same inverse problem 100 to 1,000x faster.

**AFM / scanning probe metrology (SPM).** Atomic force microscopy uses a nanometre-radius tip on a cantilever to physically trace surfaces at sub-angstrom vertical resolution. The only modality capable of imaging gate-all-around fin sidewalls, 3D NAND deep-trench profiles, and hybrid bonding surface roughness non-destructively. Legacy AFM is slow: one image per hour. Nearfield Instruments (Netherlands) solved throughput with the QUADRA platform for production-grade in-line use after eight years and $169M of development capital. Infinitesima (UK, Oxford) achieves throughput differently: rapid thermal-optical cantilever actuation combined with interferometric position detection gives optical-tool speed at AFM resolution. The capital requirement to build a production SPM tool is $15 to $50M.

**Quantum sensing (NV-diamond magnetometry).** Nitrogen-vacancy centres in diamond detect magnetic fields at micrometre precision via optically detected magnetic resonance. When current flows through a defective TSV, microbump, or interconnect in a 2.5D/3D chiplet package, the local magnetic field changes detectably. QuantumDiamonds (Munich) and EuQlid (US) both pursue this for non-destructive current-path mapping in advanced packaging. No production tool exists today. Timeline to volume production readiness: 3 to 5 years.

**Advanced Process Control (APC) software.** Sits above all hardware. Collects metrology data from every measurement step, feeds run-to-run (R2R) control loops, and adjusts equipment setpoints between wafer lots. Virtual metrology extends this further: ML models predict electrical outcomes from equipment sensor readings without waiting for physical measurement, reducing cycle time for process correction from hours to minutes. Canopus AI (Grenoble, acquired by Siemens EDA in January 2026) is the cleanest exit proof for this segment. PDF Solutions (Exensio) and KLA's own APC suite dominate the installed base.

**Node-specific unsolved problems:**

- Sub-3nm / GAA: Non-destructive sidewall measurement of gate-all-around fin profiles at production throughput is not solved. Only AFM at Nearfield/Infinitesima throughput levels can approach this.
- Hybrid bonding: Bow and warpage at sub-50nm tolerance across 300mm on patterned surfaces. Wavefront phase imaging is the emerging candidate; whether it handles patterned-surface signal artifacts at production accuracy is unproven at scale.
- 3D NAND (300+ layers): Deep-trench aspect ratio measurement beyond optical depth-of-field. AFM and X-ray tomography compete; neither is a production-validated answer.
- Advanced packaging / chiplets: Current-path integrity in TSVs and microbumps, non-destructive, at production throughput. Quantum sensing is the only candidate; it is not production-ready.
- Stochastic patterning (LER/LWR): Line-edge roughness driven by photon shot noise and resist chemistry at sub-7nm causes yield loss estimated in the billions annually. Fractilia (Austin, bootstrapped) is the only pure-play in stochastics metrology. It is in production at four of the five largest chipmakers.

---

## Why now (2026)

**High-NA EUV is pushing overlay tolerance past current tool limits.** Intel 18A and TSMC N2P are both designed for High-NA EUV (ASML EXE:5200). First volume Intel High-NA wafers ran in 2025 to 2026. Overlay tolerance drops from roughly 2nm at prior-generation nodes to sub-1nm. KLA's Archer optical overlay tools operate at 0.3 to 0.5nm 3-sigma, the practical ceiling. The installed base of overlay tools in every leading-edge fab requires replacement or augmentation within two to three years. The incremental overlay metrology market created by this transition alone is $500M or more.

**AI chip architecture multiplies inspection steps per package.** KLA's January 2026 investor day: advanced packaging revenue grew from $500M (2024) to $850M (2025), 70% year on year. A CoWoS HBM package has 40 to 60% more inspection-relevant process steps than a monolithic die. More process complexity means more measurement steps, not just more wafers. This is a structural demand expansion that does not depend on wafer volume growth.

**Specialty fabs are scaling capacity faster than KLA is addressing them.** Photonics fabs (imec 300mm photonics line, GlobalFoundries BiCMOS), compound semiconductor fabs (IQE, Vishay Newport, Wolfspeed), and power device fabs (Infineon Dresden, STMicro Catania) are all expanding. These fabs run GaN-on-Si, SiC, InP, and SOI substrates at 150mm and 200mm, not 300mm silicon. KLA's tools are calibrated for 300mm silicon. The measurement accuracy gap on non-standard substrates is real: Surfscan laser scatter signals misread GaN optical properties, producing inaccurate defect maps. No incumbent is actively solving this.

**AI is collapsing the cost of defect classification software.** TSMC's deep-learning defect detection system deployed in July 2025 achieves 95% accuracy trained on billions of wafer images. NVIDIA Cosmos Reason VLM achieves 96%+ with few-shot fine-tuning. The marginal cost of building an AI classifier on top of existing inspection hardware is falling fast. This lowers the capital barrier for software-layer entrants but also accelerates incumbent replication.

**The Canopus AI exit validates the software acquisition thesis.** Siemens EDA acquired Canopus AI (Grenoble, five years old, computational metrology and AI-driven inspection) in January 2026. Terms undisclosed but the deal confirms that EDA vendors view AI metrology software as a strategic complement to their process simulation and verification toolchains. This is the exit path for European AI process control startups.

**European Chips Act capital is mobilising at scale.** QuantumDiamonds (Munich, founded 2022) announced a EUR 152M facility investment in December 2025, roughly 50% from German federal and Bavarian state government under the European Chips Act. A three-year-old company received infrastructure capital at that scale because the European Commission identified it as potentially the next ASML. The policy signal is clear: European metrology is a priority for public co-investment, which restructures the risk profile for VC.

---

## Competitive landscape

---

## Lawrence's framing

The pick-and-shovels framing for metrology is correct. Every architecture bet at advanced nodes, whether gate-all-around, high-NA EUV, hybrid bonding, or CoWoS, creates new measurement problems that the existing tool set cannot fully solve. The yield cost of getting those measurements wrong rises exponentially as feature dimensions shrink. KLA is not going away: it will hold 70%+ of the process control market because its tools work and its qualification relationships are structural moats. The opportunity is the 30% that KLA does not own, specifically the specialty substrates and the software layer above the hardware.

One thing I would not do: invest in AI defect classification software without a contractual data arrangement already in place at a specific specialty fab. The NVIDIA Cosmos Reason model at 96% accuracy with few-shot fine-tuning means the generic model is available to anyone. The only moat is the fab-specific defect image dataset for GaN-on-Si or InP or photonic waveguide processes, locked up in a development agreement before the seed closes. A team pitching AI inspection software without that agreement is pitching a generic CV product that KLA can replicate in one product cycle. Pass.

---

## Companies

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
