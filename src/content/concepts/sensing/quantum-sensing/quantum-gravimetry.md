---
type: concept
slug: quantum-gravimetry
canonical_name: Quantum Gravimetry
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- sensing
- quantum-sensing
related_concepts: []
companies_using:
- aosense
- applanix-trimble-subsidiary
- atomicorp-formerly-atomica
- birmingham-precision-gravity-group-gravlab-spinout-universit
- coldquanta-now-infleqtion
- csiro-silicon-quantum-computing-gravity-sensing-program
- exail-ixblue-photonetics-merger
- fraunhofer-iof-ipms-commercial-gravity-spinout
- gravitec-vector-atomics
- groningen-based-hivemind-quantum-sensing
- gwr-instruments
- leibniz-institut-humboldt-university-spin-off-atomin-gmbh
- m-squared-lasers
- microsemi-microsemi-vectron-now-part-of-microchip-technology
- muquans
- national-institute-of-metrology-nim-spinoff-zhejiang-lab-qua
- nearly-syrlinks-groupe-innovation
- nomad-atomics
- q-next-tiqker-honeywell-quantum-spinout-area
- qboson
- quantum-technology-laboratories-qtc-q-next-spinout
- sbg-systems
- scintrex
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Quantum Gravimetry

*Kind: technology*

## Physics / mechanism

Cold-atom interferometry exploits matter-wave phase shifts induced by gravitational acceleration. Atoms (typically Rb-87 or Cs-133) are laser-cooled to µK, launched in free-fall, and interrogated with three Raman or Bragg pulses in a Mach-Zehnder geometry. Phase shift Δφ = k_eff · g · T² encodes local gravity; longer interrogation time T and larger effective wavevector k_eff drive sensitivity. State-of-art lab systems reach <1 µGal (10⁻⁸ m/s²); fieldable units (AOSense, Muquans, Q-NEXT spinouts) are at ~10 µGal. Key engineering constraints: vibration isolation, magnetic shielding, laser coherence length, and vacuum lifetime. MEMS gravimeters (Scintrex, Sercel) hold the ruggedized baseline at ~5 µGal but lack the drift-free absolute accuracy cold-atom devices offer.

## Competitive landscape

Classical gravimetry: MEMS/spring-mass (Scintrex CG-6, iGrav SG) and superconducting gravimeters dominate deployed installations. Superconducting devices hit <0.1 µGal but require LHe, ruling out field use. Gravity gradiometry (full-tensor, e.g. ARKeX/Lumens) extracts gradient tensor for sharper subsurface contrast. GNSS-derived gravity is coarse (~mGal). Optical clocks offer an orthogonal relativistic gravimetry path (redshift = Δg·h/c²) at comparable sensitivity but with entirely different infrastructure requirements.

## Cloudberry relevance

| Approach | Sensitivity | Fieldable | Drift-free |
|---|---|---|---|
| Cold-atom (QGA) | ~1–10 µGal | Emerging | Yes |
| MEMS spring | ~5 µGal | Yes | No |
| Superconducting | <0.1 µGal | No | Yes |


Cloudberry relevance sits at the photonics and semiconductor intersection: cold-atom sensors consume narrow-linewidth laser modules, MEMS vacuum packages, and custom ASICs for control loops — all addressable by GF-process or photonic integration IP. Deal-flow angles: laser subsystem suppliers (DFB + MOPA stacks), MEMS foundry plays vacuum-packaging cold-atom cells, and ASIC teams doing real-time phase extraction. Lunar Ventures' hardware-first thesis and GF's PIC platform (SiPh) make this a plausible co-investment corridor as QGA moves from lab to OEM module form factor.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
