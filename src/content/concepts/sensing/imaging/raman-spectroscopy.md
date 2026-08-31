---
type: concept
slug: raman-spectroscopy
canonical_name: Raman Spectroscopy
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2026-07-21-interworld-slingshot-resource-surveys]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 42
frontier:
- Can learned forward models close the accuracy gap with density functional perturbation theory, given that only 42.5% of RamanGPT predictions currently exceed a cosine similarity of 0.354 2026 06 03 ramangpt bidirectional mapping between crystal structures an, and does inverse spectrum-to-structure inference generalise beyond the chemistries covered by the 5,099-material training set?
- In strong-coupling cavity geometries, how large is the cavity-induced excited-state population enhancement relative to metal-induced lineshape broadening and non-radiative loss, and does the net figure of merit beat conventional SERS substrates in measurement 2026 05 28 raman spectroscopy at metal interfaces a numerical study of ?
- Do the proposed pump-and-probe surface-enhanced configurations recover intramolecular vibrational redistribution rates experimentally at the single-molecule level, and with what time resolution 2026 05 05 addressing intramolecular vibrational redistribution in a si?
- Under resonant excitation, can effective phonon temperature be separated quantitatively from lattice temperature so that Stokes/anti-Stokes ratios remain a valid thermometer in 2D materials 2026 06 02 resonant raman scattering in bilayer 3r mos2?
- What limit of detection and cycle time does label-free Raman achieve for unlabelled substrates in autonomous microfluidic reaction optimisation, compared with fluorescence readout on the same platform 2026 06 07 biorxiv cascademap autonomous closed loop optimization?
sources_7d: 0
sources_30d: 13
recent_mentions:
- slug: 2026-07-21-interworld-slingshot-resource-surveys
  title: Interworld Slingshot Resource Surveys
  date: '2026-07-21'
  kind: web
neighbors: []
---
## Physics / mechanism

Raman spectroscopy measures the inelastic scattering of light by vibrational modes. A monochromatic beam illuminates a sample, and a small fraction of scattered photons shift in energy by the quantum of a phonon or molecular vibration, producing Stokes (photon loses energy) and anti-Stokes (photon gains energy) lines. The spectrum is a fingerprint of bonding, symmetry and lattice dynamics, and it is one of the most accessible vibrational probes in materials laboratories ramangpt bidirectional mapping between crystal structures an. Typical crystalline spectra of interest for inorganic materials fall in the 50-1000 cm⁻¹ window ramangpt bidirectional mapping between crystal structures an, while ultralow-frequency configurations reach the interlayer modes of van der Waals stacks in the terahertz range tuning terahertz optomechanics of mos2 bilayers with homogen.

Key experimental knobs are excitation wavelength, temperature, polarisation and sample orientation. Multi-wavelength (resonant) Raman tunes the laser onto excitonic transitions, which changes relative mode intensities and can bring finite-momentum phonons into play alongside zone-centre modes; in bilayer 3R-MoS₂ this produces pronounced quenching of the Stokes intensity at low temperature, the emergence of anti-Stokes scattering above 130 K, and an effective phonon temperature that deviates strongly from the lattice temperature resonant raman scattering in bilayer 3r mos2. Angle-resolved Raman exploits polarisation selection rules in low-symmetry crystals to fix crystallographic orientation, as done for GeS in a p-GeS/n-MoS₂ heterojunction in plane anisotropy driven directional charge transport in v. Peak positions shift with strain: in MoS₂ bilayers under homogeneous biaxial tensile strain, interlayer breathing modes harden, yielding an effective out-of-plane Poisson's ratio of about 0.19-0.24 and a Grüneisen parameter of about 14-20 tuning terahertz optomechanics of mos2 bilayers with homogen.

Sensitivity is normally the limiting factor, since spontaneous Raman cross sections are small. Plasmonic and cavity environments amplify the signal, the familiar surface-enhanced Raman scattering (SERS) effect, and surface-enhanced vibrational spectroscopies can reach single-molecule sensitivity for vibrational lines and populations addressing intramolecular vibrational redistribution in a si. Numerical work on molecules near a flat mirror or inside a two-mirror cavity shows that metal proximity does more than boost the local field: a cavity traps the field and increases the effective excited-state population, while the nearby metal opens a relaxation channel that broadens lineshapes, so in the strong-coupling regime the vibronic structure of the Raman signal itself is reshaped raman spectroscopy at metal interfaces a numerical study of .

In practice Raman functions as a structural and chemical assay across very different systems: confirming that isolated type-II silicon clathrate grains are largely free of amorphous silicon magnetotransport measurements on isolated polycrystalline gr, distinguishing α- and β-phase MnSe grown by chemical vapour deposition controllable growth and characterization of alpha  and beta , identifying the bonding network of a Ge-Te solid electrolyte electrolyte bonding engineering for highly uniform gete base, detecting coordination-induced perturbation of a triazene moiety on Cd(II) complexation coordination induced tuning of ligand centered red emission , and characterising sp-carbon products from electrochemical reduction of polyynes charge transfer induced reactivity in sp carbon atomic wires.

## Competitive landscape

Raman is rarely used alone. In the sources it is paired with X-ray photoelectron spectroscopy, atomic force microscopy and scanning electron microscopy for phase identification in MnSe films controllable growth and characterization of alpha  and beta , with ARPES and transport for anisotropic heterojunctions in plane anisotropy driven directional charge transport in v, and with photoluminescence plus density functional theory to disentangle excitonic resonance from lattice dynamics resonant raman scattering in bilayer 3r mos2. Against IR absorption, the two are complementary vibrational probes and were reported together for the cis-[Cd(Tz)₂(py)₂] complex, with the Raman channel carrying the clearer coordination-induced change in the triazene moiety coordination induced tuning of ligand centered red emission .

For reaction monitoring, Raman's selling point is label-free readout. In an autonomous microfluidic enzyme-cascade platform, fluorescence was used for a glycerol detection pathway while label-free Raman monitored a 1,2,3-trichloropropane degradation pathway, the two treated as orthogonal detection modalities biorxiv cascademap autonomous closed loop optimization. On the computational side, the alternative to measurement is prediction: the forward structure-to-spectrum problem is bottlenecked by the cost of density functional perturbation theory, and the inverse spectrum-to-structure problem usually relies on retrieval against curated reference libraries ramangpt bidirectional mapping between crystal structures an.

## Evidence base

- RamanGPT trains an Atomistic Line Graph Neural Network on the 5,099-material Computational Raman Database to predict 200-bin spectra over 50-1000 cm⁻¹, with 42.5% of predictions reaching cosine similarity of at least 0.354 ramangpt bidirectional mapping between crystal structures an (3 June 2026).
- Ultralow-frequency Raman on 2H- and 2R-stacked MoS₂ bilayers under biaxial tensile strain gives an effective out-of-plane Poisson's ratio of ≈0.19-0.24 and a Grüneisen parameter of ≈14-20, exceeding the value reported for phosphorene tuning terahertz optomechanics of mos2 bilayers with homogen (16 June 2026).
- Temperature-dependent resonant Raman on bilayer 3R-MoS₂ shows Stokes quenching at low temperature with saturation, anti-Stokes scattering appearing above 130 K, and an effective phonon temperature decoupled from the lattice temperature resonant raman scattering in bilayer 3r mos2 (2 June 2026).
- Raman spectroscopy attributes a roughly three-orders-of-magnitude suppression of stochastic resistance variation in Ge₃.₅Te₁ CBRAM electrolytes to a network dominated by asymmetric-stretching GeTe₄ tetrahedral units electrolyte bonding engineering for highly uniform gete base (4 June 2026).
- Angle-resolved Raman fixed the crystallographic orientation of GeS in a p-GeS/n-MoS₂ diode whose FETs show mobility anisotropy of ≈3.4 in plane anisotropy driven directional charge transport in v (16 June 2026).
- A quantum framework based on molecular optomechanics models pump-and-probe surface-enhanced vibrational spectroscopy configurations for characterising intramolecular vibrational redistribution at single-molecule sensitivity addressing intramolecular vibrational redistribution in a si (5 May 2026).
- Label-free Raman served as one of two orthogonal detection modalities in a closed-loop microfluidic enzyme-cascade optimiser, where Bayesian optimisation found optimal conditions three times faster than design of experiments across 11 GB of data biorxiv cascademap autonomous closed loop optimization (7 June 2026).

## Frontier (open questions)

- Can learned forward models close the accuracy gap with density functional perturbation theory, given that only 42.5% of RamanGPT predictions currently exceed a cosine similarity of 0.354 ramangpt bidirectional mapping between crystal structures an, and does inverse spectrum-to-structure inference generalise beyond the chemistries covered by the 5,099-material training set?
- In strong-coupling cavity geometries, how large is the cavity-induced excited-state population enhancement relative to metal-induced lineshape broadening and non-radiative loss, and does the net figure of merit beat conventional SERS substrates in measurement raman spectroscopy at metal interfaces a numerical study of ?
- Do the proposed pump-and-probe surface-enhanced configurations recover intramolecular vibrational redistribution rates experimentally at the single-molecule level, and with what time resolution addressing intramolecular vibrational redistribution in a si?
- Under resonant excitation, can effective phonon temperature be separated quantitatively from lattice temperature so that Stokes/anti-Stokes ratios remain a valid thermometer in 2D materials resonant raman scattering in bilayer 3r mos2?
- What limit of detection and cycle time does label-free Raman achieve for unlabelled substrates in autonomous microfluidic reaction optimisation, compared with fluorescence readout on the same platform biorxiv cascademap autonomous closed loop optimization?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
