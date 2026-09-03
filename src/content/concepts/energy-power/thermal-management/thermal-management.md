---
type: concept
slug: thermal-management
canonical_name: Thermal Management
aliases: []
kind: technology
parent_concepts:
- energy-power
- ai-thermal-management
related_concepts:
- thermal-stack-map
- thermal-interface-materials
- liquid-cooling-datacentre
- diamond-heat-spreader
- vapor-chambers
- phase-change-materials
sources:
- '[[2025-11-25-carbon-nanotubes-in-the-datacentre]]'
- '[[2024-10-22-state-of-the-future-part-deux]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2023-09-08-e14-the-real-ai-bottleneck-high-bandwidth]]'
- '[[2026-03-08-diamonds-are-semiconductors-best-friend]]'
- '[[2026-04-28-thermal-stack-arms-race-global-diamond-heat-spreaders]]'
- '[[2026-04-24-thermal-stack-arms-race-global-thermal-management-market-to]]'
- '[[2026-04-10-thermal-stack-arms-race-liquid-cooling-for-ai-data-centers]]'
- '[[2024-yole-thermal-management-2024]]'
- '[[2026-07-26-humanoid-duty-cycle-thermal-constraint]]'
- '[[2026-04-01-ai-power-thermal-binding-market-projection-35-of-new-ai]]'
- '[[2025-08-19-thermal-stack-arms-race-thermal-interface-materials-market]]'
- '[[2026-09-02-vertical-power-delivery-thermal-limits]]'
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 102
descendants:
- ai-thermal-management
- cryogenic-cooling
- cryogenics
- diamond-heat-spreader
- dilution-refrigerators
- graphene-thermal-films
- heat-pipes
- immersion-cooling
- liquid-cooling
- liquid-cooling-datacentre
- microfluidic-cooling
- phase-change-materials
- radiative-cooling
- solid-state-cooling
- thermal
- thermal-interface-materials
- thermal-management
- thermal-stack-map
- thermoelectric
- tim-approach-map
- two-phase-cooling
- vapor-chambers
sources_7d: 5
sources_30d: 11
recent_mentions:
- slug: 2026-09-02-vertical-power-delivery-thermal-limits
  title: 'Vertical power delivery: the thermal limit at the 48V-to-point-of-load stage'
  date: '2026-09-02'
  kind: web
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-04-28-thermal-stack-arms-race-global-diamond-heat-spreaders
  title: Global Diamond Heat Spreaders Emerging for AI Chip Cooling
  date: '2026-04-28'
  kind: web
- slug: 2026-04-24-thermal-stack-arms-race-global-thermal-management-market-to
  title: Global Thermal Management Market to Reach £22bn by 2030, Driven by AI and Data Centres
  date: '2026-04-24'
  kind: web
- slug: 2026-04-10-thermal-stack-arms-race-liquid-cooling-for-ai-data-centers
  title: Liquid Cooling For AI Data Centers Market Growth Analysis - Size and Forecast 2026-2030
  date: '2026-04-10'
  kind: web
- slug: 2026-04-01-ai-power-thermal-binding-market-projection-35-of-new-ai
  title: 'Market projection: 35%+ of new AI datacenter capacity specifying liquid cooling by 2026'
  date: '2026-04-01'
  kind: web
- slug: 2026-03-08-diamonds-are-semiconductors-best-friend
  title: Diamonds are Semiconductors' Best Friend 2026
  date: '2026-03-08'
  kind: web
- slug: 2025-08-19-thermal-stack-arms-race-thermal-interface-materials-market
  title: 'Thermal Interface Materials Market Report 2026-2036: High-Performance TIMs for Data Centers, AI Servers, and 5G Infrastructure'
  date: '2025-08-19'
  kind: web
neighbors:
- slug: thermal-stack-map
  name: AI Thermal Stack Map (junction-to-ambient)
  path: /energy-power/thermal-management/thermal-stack-map/
  macro: energy-power
- slug: thermal-interface-materials
  name: Thermal Interface Materials (TIM)
  path: /energy-power/thermal-management/thermal-interface-materials/
  macro: energy-power
- slug: liquid-cooling-datacentre
  name: Liquid Cooling at Datacentre Scale
  path: /energy-power/thermal-management/liquid-cooling-datacentre/
  macro: energy-power
- slug: diamond-heat-spreader
  name: Diamond Heat Spreader
  path: /energy-power/thermal-management/diamond-heat-spreader/
  macro: energy-power
- slug: vapor-chambers
  name: Vapor Chambers
  path: /energy-power/thermal-management/vapor-chambers/
  macro: energy-power
- slug: phase-change-materials
  name: Phase-Change Materials (Thermal)
  path: /energy-power/thermal-management/phase-change-materials/
  macro: energy-power
---
**Thermal management is the engineering of where heat goes in a device, and across chiplet stacks, co-packaged optics, quantum chips and nanophotonics it has moved from a packaging afterthought to the constraint that decides whether an architecture works at all.**

## Summary

Thermal management covers everything done to get heat out of, around, or deliberately not through a device: heat spreaders, interface materials, substrate choice, layout, and more recently engineered materials whose thermal conductivity or radiative emission can be designed or actively switched. The physics that matters is narrower than it sounds. At the length scales now in play, bulk Fourier conduction is a poor guide: heat is carried by phonons with mean free paths comparable to film thickness, most of the resistance can sit at interfaces rather than in the bulk, and conventional cooling strategies fail because there is no room for a heat path.

The supplied literature splits into three clusters. The first is metrology and materials characterisation: frequency-domain thermoreflectance and machine-learned atomistic simulation on stoichiometric lithium niobate, whose room-temperature conductivity is orders of magnitude below silicon; time-resolved X-ray diffraction on colloidal quantum dot films measuring conductivity as low as 0.55 W/m/K in close-packed solids; sub-kelvin measurements of substrate conductivity for cryogenic quantum integration; and reconciliation of a near-order-of-magnitude experimental spread in MXene out-of-plane conductivity via heterogeneous surface terminations. The second is active or engineered control of heat flow: hexagonal boron nitride flakes as nanoscale heat spreaders, electrically switchable interfacial thermal conductance at metal/topological-insulator junctions, magnet-free nonreciprocal thermal radiation in magnetic Weyl semimetals, epsilon-near-zero coatings for spectrally selective emission, and 2D thermal metamaterials in which coherent nonlinear excitations route energy. The third is system-level design: high-resolution non-uniform-power thermal analysis of 2.5D/3D chiplet packages, reinforcement-learning chiplet placement that treats wirelength and temperature as explicitly conflicting objectives, and the argument that co-packaged optics is an architectural commitment in which thermal co-design determines deployment.

The deciding parameters are consistent across those clusters. In-plane versus out-of-plane conductivity anisotropy; interfacial thermal conductance, which frequently dominates over bulk conductivity; film thickness relative to phonon mean free path, where topological surface phonons can contribute over 30% of in-plane conductivity below 10 nm; and, at system level, the spatial resolution at which power density is modelled, since uniform power maps substantially underestimate peak temperature.

## Viability (3/5)

The characterisation layer is credible and converging. Independent techniques give quantitative, cross-checked numbers: FDTR plus machine-learned potentials agree on lithium niobate conductivity, contact-free time-resolved X-ray diffraction resolves quantum dot heating and cooling on sub-nanosecond timescales, and cryogenic substrate conductivities are measured and then reproduced with a non-equilibrium Green's function ballistic model. Simulation-plus-experiment agreement of this kind is the normal precondition for design use.

The control layer is much earlier. Nanoscale heat spreading with hBN is demonstrated with simulation and nanothermometry on immobilised gold nanospheres, not in a device. Electrically tunable interfacial conductance is reported as direct experimental evidence at Au/Bi(1-x)Sb(x) junctions with control experiments confirming topological specificity, but the reported modulation is a laboratory measurement of a junction, not a working thermal switch. Nonreciprocal emitters and thermal metamaterials remain predictive or theoretical. The residual MXene conductivity spread of 0.14 to 0.8 W/m/K shows how sensitive these materials are to uncontrolled surface chemistry.

**TLDR: Measurement and system-level modelling are solid; active heat-flow control is a set of single-device demonstrations.**

## Drivers (4/5)

On demand, the sources name the pull directly. Nanosheet transistor advances have significantly increased power densities, worsening thermal problems in 2.5D/3D chiplet systems-in-package. AI and accelerator workloads are pushing optics into the package, where packaging and thermal management increasingly dominate performance and scalability. Large-scale quantum systems that co-integrate qubits with control and readout electronics make cryogenic thermal management a central architectural challenge. Emerging device platforms add their own: integrated electro-optic lithium niobate, quantum dot films used for optical gain, and heat-sensitive plasmonic biosensing.

On supply, the enabling change is computational and metrological rather than manufacturing. Machine-learned interatomic potentials now underpin conductivity prediction, phonon Boltzmann transport in thin films, fracture and strength prediction in candidate spreader materials and infrared dielectric response with dynamic charges. New probes such as cross-grating wavefront microscopy and time-resolved X-ray diffraction give in-situ temperature fields where contact thermometry cannot go.

**TLDR: Demand is unambiguous and comes from power density in 3D packaging, co-packaged optics and cryogenic integration; supply is being unlocked by machine-learned potentials and new nanothermometry.**

## Novelty (3/5)

The strongest novelty claims are quantified against a clear baseline. Topological surface phonons are shown to contribute over 30% of in-plane thermal conductivity in sub-10 nm Si, 4H-SiC and c-BN films, up to 82 W/m/K in absolute terms, which is a mechanism absent from conventional thin-film phonon models and tunable with temperature and biaxial strain. Magnetic Weyl semimetals such as Co3Sn2S2 are predicted to give stronger and broader nonreciprocal thermal radiation than the conventional semiconductor InAs while removing the external magnet entirely, which is an architectural simplification rather than an incremental gain. At system level, moving from uniform to 5 micrometre resolution non-uniform power maps reverses the ranking of backside versus frontside power delivery in 3D stacks, meaning the incumbent analysis method was giving the wrong answer, not merely a less precise one.

Elsewhere the improvement is over prior theory rather than over deployed practice. The MXene work brings simulation into quantitative agreement with experiment by invoking a stereochemical vacuum gap; the Bode-Fano analysis sets ultimate absorption-bandwidth bounds rather than beating any existing absorber; and theta-TaN is presented as combining metallic conductivity with high thermal conductivity, but the reported figures are anisotropic strength and modulus values from simulation, with over 73% of 300 K strength retained at 900 K, not a measured thermal comparison against copper or similar. The sources do not quantify how much better hBN spreading is than the alternatives in a real device.

**TLDR: Genuine departures from bulk Fourier practice, with quantified gains in a few places, but most comparisons are against prior models rather than incumbent hardware.**

## Diffusion (2/5)

The clearest statement of adoption barriers concerns co-packaged optics, where standardisation, serviceability and thermal-aware co-design are argued to be decisive in whether the technology moves from early deployment to widespread use, and where solving component-level problems is claimed to have stalled deployment because the real constraints are architectural. That framing generalises: thermal management is rarely blocked by a missing material, it is blocked by the fact that adopting it forces changes elsewhere in the stack.

The second barrier is objective conflict. Wirelength reduction and thermal management are inherently conflicting, and prior single-objective or weighted-sum placement methods were inadequate for practical deployment, which is why a multi-agent formulation with separate reward mechanisms was needed to produce an improved Pareto front. The third is reproducibility of the materials themselves: an order-of-magnitude experimental spread traced to minor deviations in surface termination is not yet a specifiable engineering material. For the cryogenic case, the practical consequence is a substrate selection decision, high-resistivity silicon at 5x10^-2 W/m/K against roughly 10^-3 for the alternatives at 300 mK, which is comparatively easy to adopt because it substitutes into an existing process. Nothing in the supplied sources reports a commercial product using any of the active control approaches.

**TLDR: No deployment evidence in the sources; the named barriers are standardisation, serviceability and the fact that thermal goals conflict with everything else designers optimise.**

## Impact (4/5)

The value is leverage rather than a standalone market. If localised heating sets peak temperature in 3D stacks, then thermal analysis fidelity directly determines which power delivery architecture is chosen, and backside power delivery networks that look beneficial under uniform assumptions carry pronounced penalties under realistic localised workloads because of limited lateral heat spreading. That is a decision affecting the roadmap of advanced logic packaging, not a marginal efficiency gain. Similarly, thermal co-design is presented as one of the factors deciding whether co-packaged optics reaches scale in AI datacentres, and cryogenic thermal budgets are a central challenge for integrating qubits with control electronics.

There is a second, smaller impact channel in device performance rather than system architecture. Quantum dot films providing optical gain conduct heat poorly at 0.55 W/m/K, which directly bounds duty cycle and lifetime in emissive and lasing devices; lithium niobate photonics faces conductivity orders of magnitude below silicon; and plasmonic heating degrades performance in biosensing, nanophotonics and microelectronics. Beyond electronics, the sources point to elastocaloric refrigeration, thermoelastic harvesting and latent heat storage using shape memory alloys, but give no market or performance figures to size that.

**TLDR: Thermal limits gate 3D integration, in-package optics and cryogenic quantum scale-up, so getting this right or wrong changes what those architectures can be.**

## Timing Now (0-2yr)

The system-level layer is immediate. Power densities have already risen enough to worsen thermal problems in chiplet packages, the modelling tools to see it exist, and the design responses are placement algorithms and power delivery choices that fit inside current EDA and packaging flows. Co-packaged optics is described as already in early deployment with thermal co-design as a gate on wider adoption, which places that decision in the next few years.

Material substitutions with an existing process route, such as choosing high-resistivity silicon for sub-kelvin routing or inserting hBN flakes as spreaders, plausibly follow on a longer horizon. Active heat routing, thermal metamaterials and magnet-free nonreciprocal emitters have no engineering demonstration in these sources and should be treated as later or unclear.

**TLDR: The constraint is already binding in packaging and photonics; the exotic material and active-control routes are much further out.**

## Overrated or underrated? Underrated

The underrating is specific: thermal management is still treated as a downstream packaging task, and the sources show it is functioning as an architectural constraint that changes the answer to first-order design questions. The clearest single piece of evidence is that using uniform power maps flips the conclusion on backside versus frontside power delivery in 3D stacks, reinforced by the argument that component-level optimisation of co-packaged optics has stalled deployment because packaging and thermal effects dominate. Any roadmap for 3D logic, in-package optics or integrated cryogenic quantum systems that carries thermal as a late-stage check is likely mis-specified.

The caveat cuts the other way for the glamorous end of the field. Electrically tunable interfacial conductance, nonreciprocal thermal emitters, thermal metamaterials and topological surface phonon engineering are interesting physics with, in these sources, no device-level demonstration, no manufacturability evidence and in the MXene case not yet reproducible property values. Treating those as near-term solutions would be the mirror-image error. The value on a two-year view sits in metrology and thermal-aware co-design, not in new heat-routing materials.

## Prediction

By the end of 2028, thermal-aware design methods such as non-uniform power thermal analysis and multi-objective chiplet placement will be routine in published 2.5D/3D packaging work, while no commercially shipping product will use active heat-flow control based on tunable interfacial thermal conductance, thermal metamaterials or nonreciprocal thermal emitters.

## Evidence base

- 5 May 2026: time-resolved X-ray diffraction measures thermal conductivity as low as 0.55 W/m/K in close-packed CdSe/CdS quantum dot films that actively provide optical gain.
- 8 May 2026: sub-kelvin substrate measurements give high-resistivity silicon 5x10^-2 W/m/K at 300 mK against 8x10^-4 for low-resistivity silicon and 2x10^-3 for borosilicate and sapphire.
- 5 June 2026: thermal simulation at 5 micrometre resolution shows uniform power assumptions substantially underestimate peak temperatures and hide a pronounced thermal penalty for backside power delivery in 3D chiplet packages.
- 5 June 2026: topological surface phonons contribute over 30% of in-plane thermal conductivity in sub-10 nm Si, 4H-SiC and c-BN films at 300 K, up to 82 W/m/K.
- 16 June 2026: first-principles screening predicts magnet-free nonreciprocal infrared thermal radiation in magnetic Weyl semimetals such as Co3Sn2S2, outperforming conventional InAs.
- 22 July 2026: MXene out-of-plane thermal conductivity measurements span 0.14 to 0.8 W/m/K, a spread attributed to heterogeneous surface terminations creating a stereochemical vacuum gap.

## Open questions

- In a working device rather than a model system, how much peak temperature reduction does an hBN heat spreader deliver, and does interfacial thermal conductance rather than in-plane conductivity set the limit?
- Can MXene out-of-plane thermal conductivity be specified to better than a factor of two by controlling surface terminations, which is the precondition for using it as an engineering insulator?
- Does the reversible modulation of interfacial thermal conductance at Au/Bi(1-x)Sb(x) junctions give a switching ratio and speed sufficient for any useful thermal switch, and at what current cost?
- Do the thermal penalties found for backside power delivery under localised workloads survive in silicon measurements, or are they an artefact of the simulated power maps?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
