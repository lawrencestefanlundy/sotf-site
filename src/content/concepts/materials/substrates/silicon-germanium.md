---
type: concept
slug: silicon-germanium
canonical_name: Silicon Germanium
aliases:
- SiGe
- silicon germanium
- Si(1-x)Ge(x)
- SiGe BiCMOS
parent_concepts:
- compound-semiconductors
related_concepts:
- gallium-arsenide
- indium-phosphide
- ge-on-si-mid-ir
- topological-qubits
sources: []
frontier:
- Can SiGe HBT nodes keep pace with III-V GaN and InP in mmWave power amplifier performance beyond 100 GHz?
- Will Ge-channel PMOS transistors in SiGe stacks displace III-V channels in sub-3 nm CMOS nodes?
- Does SiGe quantum-well spin-qubit fidelity converge with silicon-only spin qubits, or does residual Ge nuclear spin decoherence remain a fundamental floor?
last_updated: '2026-06-02'
tags:
- concept
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: gallium-arsenide
  name: Gallium Arsenide (GaAs)
  path: /sotf-site/materials/substrates/gallium-arsenide/
  macro: materials
- slug: indium-phosphide
  name: Indium Phosphide (InP)
  path: /sotf-site/materials/substrates/indium-phosphide/
  macro: materials
- slug: ge-on-si-mid-ir
  name: Germanium-on-Silicon Mid-IR Photonics
  path: /sotf-site/materials/substrates/ge-on-si-mid-ir/
  macro: materials
- slug: topological-qubits
  name: Topological Qubits (Microsoft Majorana)
  path: /sotf-site/compute/quantum-computing/topological-qubits/
  macro: compute
---
Silicon germanium (Si₍₁₋ₓ₎Ge₍ₓ₎) is a group-IV alloy that is fully miscible across all compositions. Adding germanium to silicon reduces the bandgap (0.66 eV for pure Ge vs 1.12 eV for Si), increases carrier mobility — electron mobility in strained SiGe approaches ~2,000 cm²/V·s — and introduces a compressive biaxial strain when grown epitaxially on silicon substrates. The alloy is uniquely compatible with standard CMOS fabs, which distinguishes it from III-V materials and is the primary source of its commercial traction.

Three device classes dominate. First, SiGe heterojunction bipolar transistors (HBTs) are produced in high-volume BiCMOS processes (IBM, GlobalFoundries, TSMC) and are the standard technology for mmWave and RF front-end circuits: low-noise amplifiers, voltage-controlled oscillators, and phased-array beamformers from 5G sub-6 GHz through 100+ GHz automotive radar bands. **Rf Frontend Silicon** tracks the investment landscape here; **Sige Semiconductor Silanna** and **Sicoya** work in SiGe-based photonic and RF integration. Second, strained SiGe or pure Ge layers are used as the high-mobility channel in advanced CMOS nodes (Ge PMOS); this is a core enabler in sub-3 nm gate stacks. Third, Ge/SiGe quantum wells are a leading platform for silicon-compatible spin qubits, tracked under [Topological Qubits (Microsoft Majorana)](/sotf-site/compute/quantum-computing/topological-qubits/); **Hrl Laboratories** works on SiGe spin qubit architectures. The [Germanium-on-Silicon Mid-IR Photonics](/sotf-site/materials/substrates/ge-on-si-mid-ir/) concept covers the photonic use of Ge-on-Si for mid-IR waveguides.

The absence of a direct bandgap in Si and Ge limits SiGe to indirect-gap photonics and excludes it from efficient light emission, keeping emitter applications with III-V materials.

## Frontier
- Can SiGe HBT nodes keep pace with III-V GaN and InP in mmWave power amplifier performance beyond 100 GHz?
- Will Ge-channel PMOS transistors in SiGe stacks displace III-V channels in sub-3 nm CMOS nodes?
- Does SiGe quantum-well spin-qubit fidelity converge with silicon-only spin qubits, or does residual Ge nuclear spin decoherence remain a fundamental floor?
