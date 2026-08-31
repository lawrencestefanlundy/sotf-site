---
type: concept
slug: ion-implantation
canonical_name: Ion Implantation
aliases:
- ion implant
- implanter
- doping
parent_concepts:
- semiconductor-equipment
related_concepts:
- deposition
- etch
- materials-process
sources:
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
frontier:
- What implanted Er3+ areal dose and anneal schedule maximise photoluminescence in Si3N4 before concentration quenching or residual implantation damage dominates, and how sharp is that optimum?
- Does implantation-induced damage in Si3N4 metasurfaces measurably degrade optical loss or resonance Q relative to undoped controls after annealing?
- Can contact-free terahertz time-domain spectroscopy resolve implanted, annealed dopant profiles in thin layers within the sensitivity bounds calculated for SiC, Si and GaN, or is it limited to bulk-like doping levels?
- For devices where implantation is not used, such as diamond 2D hole gas FETs, can the reported GIDL-like leakage be distinguished from implantation-style defect signatures by the same silicon MOS extraction toolkit?
last_updated: '2026-08-31'
tags:
- concept
mention_count: 121
sources_7d: 0
sources_30d: 15
recent_mentions:
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
neighbors:
- slug: deposition
  name: Deposition
  path: /manufacturing/equipment-processes/deposition/
  macro: manufacturing
- slug: etch
  name: Etch
  path: /manufacturing/equipment-processes/etch/
  macro: manufacturing
- slug: materials-process
  name: Materials & Process
  path: /materials/advanced-materials/materials-process/
  macro: materials
---
## Physics / mechanism

Ion implantation introduces a chosen species into a solid by ionising it, accelerating it to a defined energy and letting it come to rest at depth inside the target. The depth distribution is set by ion mass and energy, and the areal concentration by fluence, so the dopant profile is decoupled from the thermodynamics of the host: species and concentrations that would not be incorporated during growth can be placed in a film after it is made. The cost is lattice damage along the ion track, which normally has to be repaired by a subsequent thermal anneal that also moves implanted atoms onto sites where they are electrically or optically active.

The clearest use case in the current source set is rare-earth doping of a photonic host. Trivalent erbium was implanted into silicon nitride, which was then patterned into periodic nanocylinder arrays supporting Mie-type resonances; after thermal annealing the metasurfaces showed room-temperature photoluminescence at the telecommunication wavelength with an enhancement factor of about 18 at a nanocylinder radius of 390 nm, in agreement with simulation strong enhancement of er3 emission at room temperature in si. Time-resolved measurements showed a nearly ten-fold reduction in luminescence lifetime, attributed to the Purcell effect rather than to any change in the implanted emitter population strong enhancement of er3 emission at room temperature in si. Photoluminescence intensity depended strongly on the implanted Er3+ concentration, which is the standard implantation trade-off between more emitters and concentration quenching or residual damage strong enhancement of er3 emission at room temperature in si.

Two process variables therefore dominate outcomes: the implant dose, which fixes emitter or carrier density, and the anneal, which fixes activation and defect recovery. Because implantation is a post-growth step, it composes with lithographic patterning, allowing the same wafer to carry both the dopant profile and a resonant geometry designed to act on it strong enhancement of er3 emission at room temperature in si.

## Competitive landscape

The sources do not contain a head-to-head comparison of implantation against other doping routes, but they do show the alternatives in use. In-growth substitutional doping replaces host cations during synthesis, as with niobium substitution in Cr(1-x)Nb(x)Te2 across x = 0 to 0.2, which tuned ferromagnetic resonance from 40 GHz down to the few-GHz regime spin dynamics in the van der waals ferromagnet crte2 enginee, and trace metal addition to germanium anodes, where Yb doping extended anode lifetime by roughly a factor of three tailoring mechanical properties of germanium anodes via meta. Solution routes add dopants to the precursor, as with NaCl added to sol-gel ZnO films sol gel derived niozno thin films with single and heterostru. Implantation is distinguished by being applied after the host is formed, at the cost of damage and an anneal step.

On the metrology side, doping level is what has to be verified after any of these routes. Contact-free reflection terahertz time-domain spectroscopy has been assessed for its accessible doping ranges in SiC, Si and GaN using a simulation-based sensitivity metric that accounts for layer thickness, doping type and doping level accessibility of doping ranges of semiconductors by terahert, in contrast to contacting methods such as four-point probe and capacitance-voltage measurement accessibility of doping ranges of semiconductors by terahert.

## Evidence base

- Er3+ implanted into Si3N4 metasurfaces gave a room-temperature photoluminescence enhancement factor of about 18 at 390 nm nanocylinder radius after thermal annealing, matching simulation (2026-05-05) strong enhancement of er3 emission at room temperature in si.
- Time-resolved photoluminescence on the same implanted metasurfaces showed a nearly ten-fold lifetime reduction, assigned to the Purcell effect (2026-05-05) strong enhancement of er3 emission at room temperature in si.
- Photoluminescence intensity in the implanted Si3N4 films depended strongly on Er3+ ion concentration, indicating a dose optimum (2026-05-05) strong enhancement of er3 emission at room temperature in si.
- A sensitivity metric for reflection terahertz time-domain spectroscopy was defined and computed for SiC, Si and GaN to bound the doping ranges that contact-free measurement can access (2026-05-05) accessibility of doping ranges of semiconductors by terahert.
- Niobium substitution during growth of 1T-CrTe2 tuned the resonance frequency from 40 GHz to the few-GHz regime while Gilbert damping rose from about 0.066 to about 0.14, an example of dopant control achieved without implantation (2026-05-05) spin dynamics in the van der waals ferromagnet crte2 enginee.
- A GIDL-like leakage mechanism was reported in diamond 2D hole gas FETs despite the absence of intentional impurity doping, showing that unintentional defect states can mimic doping-related effects (2026-01-01) **Walker 2026 Diamond 2Dhg Conduction Mechanism**.

## Frontier (open questions)

- What implanted Er3+ areal dose and anneal schedule maximise photoluminescence in Si3N4 before concentration quenching or residual implantation damage dominates, and how sharp is that optimum?
- Does implantation-induced damage in Si3N4 metasurfaces measurably degrade optical loss or resonance Q relative to undoped controls after annealing?
- Can contact-free terahertz time-domain spectroscopy resolve implanted, annealed dopant profiles in thin layers within the sensitivity bounds calculated for SiC, Si and GaN, or is it limited to bulk-like doping levels?
- For devices where implantation is not used, such as diamond 2D hole gas FETs, can the reported GIDL-like leakage be distinguished from implantation-style defect signatures by the same silicon MOS extraction toolkit?

*Synthesised 2026-08-31 from 12 KB sources by the resynth pipeline; citations are KB source slugs.*
