---
type: concept
slug: silicon-carbide-photonics
canonical_name: Silicon Carbide Photonics
aliases:
- 4H-SiC photonics
- SiC integrated photonics
kind: technology
parent_concepts:
- materials
- substrates
related_concepts:
- silicon-nitride
- diamond
- sic
- quantum-computing
- mid-ir-photonic-sensing
sources: []
frontier:
- Does any commercial photonic foundry add a 4H-SiC waveguide module by 2028?
- Can SiC color-centre quantum emitters reach the photonic-integration density needed for ≥100-qubit on-chip systems by 2030?
- Does the high thermal conductivity (490 W/m·K) of SiC unlock high-power photonic ICs that silicon can't host (e.g. >1W on-chip lasers)?
- Does a SiC power-electronics fab repurpose for photonics — or is the process incompatibility (different epi recipes) prohibitive?
- Mid-IR SiC waveguides — can SiC fill the 4-7 μm band where silicon absorption kicks in, competing with chalcogenide?
last_updated: 2026-05-07
tags:
- concept
- photonics
- silicon-carbide
- quantum
- mid-ir
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---
*Wide-bandgap waveguide platform with quantum + high-power + mid-IR potential*

## Physics / mechanism

4H-silicon-carbide (4H-SiC) has a wide bandgap (~3.2 eV) making it transparent from UV through near-IR with low absorption. Refractive index ~2.6 at 1550 nm gives reasonable mode confinement. Critically, SiC hosts color centres — silicon vacancies (V_Si), divacancies, and nitrogen-vacancy-like defects — that emit single photons at telecom wavelengths and can store quantum information for milliseconds at room temperature. SiC also has thermal conductivity ~490 W/m·K (vs silicon's 150 W/m·K), enabling high-power photonic ICs that silicon can't host without thermal failure.

The materials-processing path is unique among emerging photonic platforms: SiC has a mature CMOS-style fab ecosystem from power electronics (Wolfspeed, ST, onsemi, Infineon), but those fabs run different epi/etch recipes than would be needed for low-loss photonic waveguides. The repurposing question is real and unresolved.

## Competitive landscape

Lab demonstrators only as of 2026. Commercial production: zero foundries. Active research: Marko Lončar group (Harvard), HRL Labs (US), Princeton (Englund/Awschalom-derived programmes), Linköping University (Sweden, the SiC PIC pioneer). Best-demonstrated waveguide loss ~1–2 dB/cm for 4H-SiC-on-insulator; the trajectory is comparable to where TFLN was in 2018–2019.

Closest peers:
- [Diamond](/materials/substrates/diamond/) for quantum (NV centres) — even better quantum coherence but worse manufacturing path
- [Silicon Nitride](/materials/substrates/silicon-nitride/) for low-loss visible — much more mature but no native quantum emitters
- **Gallium Nitride** for wide-bandgap photonics — different application focus

## Frontier (open questions)

See frontmatter `frontier:` block.
