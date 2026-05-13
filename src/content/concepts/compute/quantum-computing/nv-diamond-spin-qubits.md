---
type: concept
slug: nv-diamond-spin-qubits
canonical_name: NV Diamond / Spin Qubits
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- compute
- quantum-computing
related_concepts: []
companies_using:
- abacusai-quantum-coldquanta-infleqtion
- diraq
- element-six-de-beers-group
- equal1
- hrl-laboratories-boeinggm-jv
- intel-quantum-computing-division
- magnetiq-medical
- nvision-imaging-technologies
- photonic-inc
- qilimanjaro-quantum-tech
- qnami
- quantrolox
- quantum-brilliance
- quantum-diamond-technologies-qdti
- quantum-motion
- quobly
- qutech-tu-delft-tno
- qzabre
- scalinq
- silicon-quantum-computing-sqc
- sparrow-quantum
- spin-memory-now-integrated-silicon-solution
- spin-q-technology
- turing-formerly-quantum-computing-inc-diamond-division
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 2
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# NV Diamond / Spin Qubits

*Kind: technology · Attio deal count: 2*

## Physics / mechanism

Nitrogen-vacancy (NV) centres are point defects in diamond where a nitrogen atom substitutes for carbon adjacent to a lattice vacancy, creating an S=1 spin system with a ground-state zero-field splitting of ~2.87 GHz. The spin state is initialised and read out optically (637 nm zero-phonon line), making it operable at room temperature — the key differentiator versus superconducting or trapped-ion qubits. Coherence times (T₂) reach ~1 ms in isotopically purified ¹²C diamond; T₂* (inhomogeneous) is typically 1–100 µs. Current best qubit counts are small (single to tens of NV centres), but ensemble magnetometry already achieves sub-pT/√Hz sensitivity. Silicon-vacancy (SiV) and tin-vacancy (SnV) centres offer superior optical coherence for quantum networking. Leading groups: Element Six (CVD diamond), QDiamond, Bosch, Q.ANT, Fraunhofer IAF.

## Competitive landscape


Superconducting qubits (IBM, Google) dominate gate-based computation but require dilution refrigeration (~15 mK). Trapped ions (IonQ, Quantinuum) offer high fidelity but slow gate rates. Photonic qubits (PsiQuantum, QuiX) target fault-tolerance via photon loss tolerance. NV centres compete primarily in quantum sensing and quantum networking repeater nodes rather than gate-model computation. Silicon spin qubits (Intel, imec) are the closest room-temperature-compatible rival for integration with CMOS fabs.

| Platform | Temp | T₂ | Fab integration |
|---|---|---|---|
| NV Diamond | 300 K | ~1 ms | Hard, bespoke CVD |
| Si Spin Qubit | ~1 K | ~10 ms | CMOS-compatible |
| Superconducting | 15 mK | ~100 µs | Wafer-scale Al/Nb |

## Cloudberry relevance
Cloudberry's angle is material and fabrication infrastructure: CVD diamond synthesis, ion implantation for NV placement, and photonic integration (diamond waveguides, SiN coupling layers) all sit inside the advanced-materials and photonics thesis. GlobalFoundries LP context matters because GF's photonics and compound-semi process know-how is adjacent to heterogeneous integration of diamond dies. Near-term deal-flow: quantum sensing companies (magnetometry, gyroscopes) monetising before fault-tolerant QC arrives, and CVD diamond substrate suppliers entering the semiconductor supply chain.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
