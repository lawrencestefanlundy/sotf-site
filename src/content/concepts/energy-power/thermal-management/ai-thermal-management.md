---
type: concept
slug: ai-thermal-management
canonical_name: Ai Thermal Management
aliases: []
related_concepts: []
sources: []
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 3
  impact: 4
  timing_band: Now (0-2yr)
  verdict: Underrated
scorecard_status: draft
mention_count: 3
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-09-in-die-microfluidic-cooling-sprint
  title: In-die microfluidic cooling — cluster research sprint
  date: '2026-07-09'
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
- slug: 2025-11-25-carbon-nanotubes-in-the-datacentre
  title: Carbon Nanotubes in the Datacentre
  date: '2025-11-25'
  kind: substack
neighbors: []
---
**Thermal management is the discipline of moving waste heat out of AI compute hardware and the nanoscale materials it is built from, and it is now shifting from a downstream packaging concern to an architectural constraint that decides whether 3D chiplet stacks and co-packaged optics can scale at all.**

## Summary

Every joule delivered into a processor leaves as heat. As AI accelerators move from single dies to 2.5D and 3D chiplet assemblies, and as optics migrate from the board edge into the package, the heat has to escape through thinner, more thermally resistive, more crowded structures. "AI thermal management" is the cluster of techniques addressing this: package- and system-level heat extraction, thermal-aware physical design, and the materials science of heat conduction at nanometre scales where classical Fourier-law intuitions break down.

The work splits into three layers. At the **system layer**, the argument is architectural: co-packaged optics should be treated not as a component swap but as a commitment that reshapes the boundary between photonics, electronics and packaging, with thermal-aware co-design, standardisation and serviceability deciding whether it reaches volume deployment. At the **design-methodology layer**, high-resolution simulation is exposing errors in current practice: modelling chiplet stacks with uniform power maps underestimates peak temperature and hides the differences between frontside and backside power delivery, and backside power delivery in 3D configurations carries a pronounced thermal penalty under realistic localised workloads because lateral heat spreading is limited. Machine learning is entering the same layer, with multi-agent reinforcement learning used to trade wirelength against thermal design power in chiplet placement, two objectives that conflict directly.

At the **materials layer**, the picture is that heat transport at the nanoscale is neither well characterised nor well controlled. Close-packed colloidal quantum dot films conduct at 0.55 W/m/K; stoichiometric lithium niobate, now central to integrated electro-optics, has conductivity orders of magnitude below silicon; and in semiconductor films below 10 nm, topological surface phonons contribute over 30% of in-plane thermal conductivity at 300 K, up to 82 W/m/K in absolute terms. Countermeasures under investigation include hexagonal boron nitride flakes as lateral heat spreaders, assessed by finite-element simulation and cross-grating wavefront nanothermometry, and electrically switchable interfacial thermal conductance in Au/Bi-Sb topological insulator junctions.

The parameters that decide the field are: power density per unit die area and its spatial non-uniformity; through-stack and interfacial thermal resistance rather than bulk conductivity; the temperature ceiling of the most heat-sensitive component in the package, which for co-packaged optics is the laser and modulator rather than the logic; and whether design tools can price thermal cost early enough in the flow to change floorplans instead of only sizing heatsinks afterwards.

## Viability (3/5)

Existing practice is proven: five generations of TPU supercomputers delivered a 100x increase in peak node performance and a 3600x increase in supercomputer performance over eight years alongside substantial gains in performance per watt, which is only possible if heat extraction kept pace. The question is whether it keeps working through 3D stacking and in-package optics. Here the evidence is thinner and more negative than positive: the backside power delivery result is a simulation study, and its headline finding is that a technique attractive on other grounds becomes thermally worse in 3D under realistic power maps.

At the materials layer, several of the proposed levers are real but small or unproven at device scale. The hBN heat-spreader study combines finite-element modelling with experimental nanothermometry, but on gold nanospheres in water rather than in a package. Electrically tunable interfacial conductance has direct experimental evidence with control experiments confirming the topological origin, which is a genuine result, but it is a junction-level demonstration with no throughput or reliability data. The 2D thermal metamaterials work is explicitly a theoretical framework with benchmark models, not a device. A 3 reflects a field where the incumbent approach works, the diagnosis of where it fails is credible, and the replacements are early.

**TLDR: Conventional thermal engineering demonstrably works at scale; the new nanoscale and design-automation tools are mostly simulation or single-device demonstrations.**

## Drivers (4/5)

On demand: nanosheet technologies have significantly increased power densities, which directly worsens the thermal problem in 2.5D and 3D systems-in-package, and the growth of AI and accelerator workloads is forcing optics into the package where packaging and thermal behaviour increasingly dominate performance and scalability. The TPU trajectory shows sustained scale increase over five generations with sustainability and performance-per-watt treated as first-order design goals. Cryogenic quantum systems provide a second, smaller demand pull, where close integration of qubits with control and readout electronics makes sub-kelvin thermal management a central architectural challenge.

On supply: characterisation is advancing on several independent fronts, including contact-free time-resolved X-ray diffraction for thermal response in device-like environments, frequency-domain thermoreflectance combined with machine-learned atomistic potentials, and structured illumination scanning thermography that removes the repeated temporal excitation and stitching artefacts of conventional photothermal imaging for large-area inspection. Machine-learned interatomic potentials are also now standard in predicting thermal and dielectric properties. What the sources do not show is a supply chain delivering new thermal materials into production packages.

**TLDR: Demand is unambiguous and rising with power density; the supply side of measurement and simulation tooling is improving fast, materials less so.**

## Novelty (3/5)

The clearest quantified novelty is in physical understanding. Topological surface phonons were previously not counted as a transport channel; they turn out to contribute over 30% of in-plane thermal conductivity in sub-10 nm Si, 4H-SiC and c-BN films at 300 K, with the largest absolute contribution reaching 82 W/m/K, and are tunable by temperature and biaxial strain. That changes what a thin-film thermal model should contain. Similarly, magnetic Weyl semimetals such as Co3Sn2S2 are predicted to give strong broadband nonreciprocal thermal radiation without an external magnetic field, outperforming the conventional semiconductor baseline InAs, with explicit design rules relating anomalous Hall response to optical loss. Bode-Fano-type bounds on broadband absorption by subwavelength particles set the ceiling that any such design can approach.

Against that, several results are novelty in the direction of lower conductivity, useful for thermoelectrics but a liability for cooling: a symbolic-regression framework selected GuaPbI3, synthesised with room-temperature conductivity of about 0.088 W/m/K. On the design side, the multi-agent reinforcement learning placer is reported to deliver a significantly improved Pareto front over state-of-the-art methods, but the sources give no magnitude, so the improvement cannot be sized. Novelty is genuine and broad but the improvement over incumbent heat-removal practice is not yet quantified anywhere in these sources.

**TLDR: Real advances against specific baselines, but the quantified improvements are mostly in measurement and understanding rather than in delivered heat flux.**

## Diffusion (3/5)

Two adoption paths run at very different speeds. Simulation and placement methodology is cheap to adopt: moving from uniform to non-uniform power maps at 5 micrometre resolution is a change of tooling and inputs, not of manufacturing, and thermal-aware placement is a software layer over existing flows. The friction is that adopting them may invalidate architectural choices already made, which is exactly what the backside power delivery finding implies.

The hardware path is slower and the sources name the obstacles directly: for co-packaged optics, standardisation, serviceability and thermal-aware co-design will be decisive in determining whether it moves from early deployment to widespread adoption, and device-centric analyses underappreciate the system trade-offs. A repairability problem is a diffusion problem, not a physics problem. For materials, conventional cooling strategies are said to fail at nanoscale because of limited heat transport and high interfacial thermal resistance, which means new spreaders must be integrated into the stack rather than bolted on, and none of the sources report integration into a manufacturable process. In cryogenic systems the material choice is already actionable, since high-resistivity silicon at 5e-2 W/m/K at 300 mK beats low-resistivity silicon, borosilicate and sapphire by one to two orders of magnitude.

**TLDR: Design-tool changes can propagate quickly; exotic materials and interfaces face packaging, standardisation and serviceability barriers that the sources call decisive.**

## Impact (4/5)

The sources position thermal behaviour as gating rather than incremental. Co-packaged optics is presented as an architectural commitment whose fate depends on thermal co-design. Backside power delivery, a technique adopted for electrical reasons, is shown to carry pronounced thermal penalties in 3D under localised workloads, meaning a thermal result can reverse a power-delivery roadmap decision. On the efficiency side, the TPU record ties performance per watt and carbon emissions per floating point operation directly to the viability of large-scale training systems.

The cap on the score is that the sources quantify the problem far better than the payoff of any specific solution. No source gives a figure for how much extra performance, density or efficiency a particular thermal intervention buys in a real AI system. Impact is high because the constraint is binding, not because any of these techniques has been shown to relieve it by a measured amount.

**TLDR: Thermal limits sit directly on the critical path of 3D integration, in-package optics and datacentre energy efficiency, so the value at stake is the scaling of AI compute itself.**

## Timing Now (0-2yr)

The design-methodology findings are immediately actionable and immediately consequential. If uniform power maps materially understate peak temperature and mask the difference between frontside and backside power delivery in 3D stacks, then analyses already used to justify roadmap choices are wrong today. Co-packaged optics is described as being in early deployment with the transition to wide adoption still contested, which places the decision window inside the next few years.

The materials and active-control work sits on a different clock. Electrically tunable interfacial thermal conduction, topological-phonon engineering, nonreciprocal thermal emitters and 2D thermal metamaterials are at the single-junction, first-principles or theoretical-framework stage. Nothing in the sources suggests any of these reaches a shipping package inside five years.

**TLDR: The architectural decisions that thermal analysis should inform are being taken now; the exotic material solutions arrive much later, if at all.**

## Overrated or underrated? Underrated

Underrated as a system constraint, and specifically as a determinant of which packaging architectures survive. Two independent sources make the same argument from different directions: that treating thermal behaviour as a component-level or post-hoc concern produces wrong answers at the architecture level, whether in power delivery choice or in the boundary between photonics and compute. Investment attention in AI infrastructure concentrates on compute density and interconnect bandwidth; the sources suggest the binding variable is increasingly how much heat can be pulled laterally out of a stack whose lateral spreading has been designed away.

The nanoscale materials strand deserves a separate and cooler verdict. It is scientifically strong and produces quantified, surprising results, but nothing in these sources connects a novel spreader, metamaterial or tunable interface to a measured improvement in a real package. Anyone pricing hBN spreaders, topological phonon engineering or nonreciprocal emitters as near-term datacentre technology is ahead of the evidence. The near-term value is in measurement fidelity and thermal-aware design automation, both of which are unglamorous and cheap to deploy.

## Prediction

By 31 December 2028, thermal-aware objectives will be a standard input to commercial 2.5D chiplet placement flows, while no hexagonal boron nitride, topological-phonon or actively tunable-interface heat-spreading layer will have appeared in a volume-shipped AI accelerator package.

## Evidence base

- Thermal simulations at 5 micrometre resolution show uniform power maps substantially underestimate peak temperatures, and that backside power delivery in 3D exhibits pronounced thermal penalties under realistic localised workloads due to limited lateral heat spreading.
- Across five TPU generations over eight years, Google reports a 10x increase in HBM capacity and bandwidth per node, a 100x increase in peak node performance and a 3600x increase in supercomputer performance, with substantial improvements in performance per watt and carbon per floating point operation.
- In semiconductor thin films below 10 nm, topological surface phonons contribute over 30% of in-plane thermal conductivity at 300 K, reaching 82 W/m/K in absolute terms, and are modulated by temperature and biaxial strain.
- Sub-kelvin measurements give high-resistivity silicon 5e-2 W/m/K at 300 mK, against 8e-4 for low-resistivity silicon and 2e-3 for borosilicate and sapphire, a one to two order of magnitude substrate choice for cryogenic quantum integration.
- Interfacial thermal conductance across Au/Bi89Sb11 and Au/Bi87Sb13 junctions is reversibly modulated by electrical current injection, with control experiments on trivial semimetals and insulating interlayers confirming the topological origin.
- Co-packaged optics is argued to be an architectural commitment rather than a component optimisation, with standardisation, serviceability and thermal-aware co-design decisive for the transition from early deployment to widespread adoption.

## Open questions

- By how much do non-uniform power maps at 5 micrometre resolution change predicted peak temperature relative to uniform maps, and does that gap reverse the backside power delivery decision for any specific shipping 3D product?
- What is the actual Pareto improvement, in degrees and in wirelength, from multi-agent reinforcement learning placement against conventional weighted-sum optimisation on an industrial chiplet floorplan?
- Does the cooling benefit measured for hBN spreaders around gold nanoparticles in water survive translation to a dry, multilayer semiconductor stack where interfacial thermal conductance dominates?
- Which component sets the temperature ceiling in a co-packaged optics assembly, and can standardisation and serviceability requirements be met without giving back the energy-per-bit advantage that motivates moving optics into the package?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
