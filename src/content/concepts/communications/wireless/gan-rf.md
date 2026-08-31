---
type: concept
slug: gan-rf
canonical_name: Gan RF
aliases: []
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 3
frontier:
- What measured V_br·f_T and R_on^sp values do production GaN RF processes achieve, and how large is the gap to the derived geometry-free limits?
- What are the corresponding breakdown field, saturation velocity and specific on-resistance figures for GaAs and silicon RF platforms, so the three-way comparison can be quantified rather than asserted?
- Does the undoped polarization-induced 2DEG deliver a measurable noise-figure advantage in the LNA block, or is the GaN benefit confined to the PA and switch functions?
- Which substrate and thermal configurations allow GaN RF ICs to operate near the 3.3 MV/cm field limit without self-heating collapsing the saturation velocity?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
neighbors: []
---
## Physics / mechanism

Gallium nitride RF integrated circuits exploit a property absent from silicon and GaAs platforms: the hexagonal, non-centrosymmetric GaN lattice supports a macroscopic spontaneous polarization, and elastic strain acting through the piezoelectric tensor fixes a bound sheet charge at an AlGaN/GaN heterointerface physics to circuit analysis of gan rf integrated circuits ve. Solving Poisson's equation with triangular-well quantisation at that interface yields a degenerate quasi-two-dimensional electron channel of roughly 10^13 cm^-2 carriers with no intentional doping physics to circuit analysis of gan rf integrated circuits ve. Because the channel is polarization-induced rather than doped, ionised-impurity scattering in the conduction path is decoupled from carrier density.

Two material constants set the device envelope. Energy-momentum conservation for impact-ionisation pair creation fixes the critical breakdown field at 3.3 MV/cm, and phonon-limited energy relaxation fixes the saturation velocity at 2.5 x 10^7 cm/s physics to circuit analysis of gan rf integrated circuits ve. These combine into geometry-free figures of merit: the breakdown-voltage/transit-frequency product V_br·f_T = E_c·v_sat/(2π), and the specific on-resistance floor R_on^sp = 4V_br^2/(μεE_c^3) physics to circuit analysis of gan rf integrated circuits ve. Both are independent of gate length and layout, so they bound what any GaN process can achieve rather than describing one implementation.

The same analysis maps these limits onto the three functional blocks of a transmit/receive module: the low-noise amplifier, the power amplifier, and the switch/phase-shifter physics to circuit analysis of gan rf integrated circuits ve. The V_br·f_T product governs how much power a PA can deliver at a given operating frequency; R_on^sp governs insertion loss and die area in the switch and phase-shifter path.

## Competitive landscape

The source frames GaN as the third stage of a migration in RF integrated-circuit platforms, from silicon to GaAs and now to gallium nitride, with the comparison derived from first-principles material physics rather than benchmarked parts physics to circuit analysis of gan rf integrated circuits ve. The distinguishing physics is the undoped polarization-induced 2DEG plus the high breakdown field, which together shift the achievable power-frequency and on-resistance-area trade-offs relative to the earlier platforms. The available sources do not give quantitative silicon or GaAs values for the same figures of merit, so the size of the advantage in each T/R block is not established here.

## Evidence base

- A first-principles derivation published 31 July 2026 traces the RF IC platform migration from silicon to GaAs to GaN and grounds it in lattice polarization physics physics to circuit analysis of gan rf integrated circuits ve.
- Poisson's equation with triangular-well quantisation at the AlGaN/GaN interface gives a degenerate quasi-2D channel of ~10^13 cm^-2 without doping physics to circuit analysis of gan rf integrated circuits ve.
- GaN breakdown field is given as 3.3 MV/cm and saturation velocity as 2.5 x 10^7 cm/s, derived from pair-creation energy-momentum conservation and phonon-limited energy relaxation respectively physics to circuit analysis of gan rf integrated circuits ve.
- The geometry-free limits are stated as V_br·f_T = E_c·v_sat/(2π) and R_on^sp = 4V_br^2/(μεE_c^3) physics to circuit analysis of gan rf integrated circuits ve.
- These limits are mapped onto LNA, PA and switch/phase-shifter functions within a transmit/receive chain physics to circuit analysis of gan rf integrated circuits ve.
- Q2 2026 semiconductor startup funding totalled over $6.0B across 80 companies, with the quarter's themes reported as AI hardware, edge silicon, quantum and datacentre infrastructure; RF GaN is not listed among the funded categories semiengineering startup funding q2 2026.

## Frontier (open questions)

- What measured V_br·f_T and R_on^sp values do production GaN RF processes achieve, and how large is the gap to the derived geometry-free limits?
- What are the corresponding breakdown field, saturation velocity and specific on-resistance figures for GaAs and silicon RF platforms, so the three-way comparison can be quantified rather than asserted?
- Does the undoped polarization-induced 2DEG deliver a measurable noise-figure advantage in the LNA block, or is the GaN benefit confined to the PA and switch functions?
- Which substrate and thermal configurations allow GaN RF ICs to operate near the 3.3 MV/cm field limit without self-heating collapsing the saturation velocity?

*Synthesised 2026-08-31 from 2 KB sources by the resynth pipeline; citations are KB source slugs.*
