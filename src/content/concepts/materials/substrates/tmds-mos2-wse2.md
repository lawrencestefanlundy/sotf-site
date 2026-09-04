---
type: concept
slug: tmds-mos2-wse2
canonical_name: TMDs (MoS2, WSe2)
aliases: []
kind: material
parent_concepts:
- materials
- substrates
related_concepts: []
sources: []
frontier:
- Do the ~42% on-current and ~16% subthreshold swing gains observed on narrowing MoS2 ribbons to 30-40 nm hold as median statistics across wafer-scale CVD material, rather than in champion devices on transferred flakes?
- Can the disorder and multi-domain kinetics that govern switching in CVD-grown 3R-WSe2 bilayers be suppressed enough for reproducible non-volatile ferroelectric operation?
- Do the calculated zero-field valley splittings (10.41 meV for V2O3/WSe2, 37.3 and 78.2 meV for Mo0.75V0.25Te2) survive experimental realisation at real interfaces, and at what temperature?
- Does periodic poling of TMDs raise SPDC conversion efficiency enough to compete with established phase-matched bulk crystals on brightness, not just on device thickness?
last_updated: '2026-08-31'
tags:
- concept
- material
mention_count: 28
last_reorg_date: '2026-05-13'
scorecard:
  viability: 3
  drivers: 3
  novelty: 4
  diffusion: 2
  impact: 4
  timing_band: Later (5-10yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 3
sources_30d: 5
recent_mentions: []
neighbors: []
---
**Transition metal dichalcogenides such as MoS2 and WSe2 are layered semiconductors that remain semiconducting at a single three-atom-thick layer, making them candidate channel materials for post-silicon transistors and a versatile substrate for stacked photonic, ferroelectric and spintronic devices; the electronics case now rests on real scaled devices, while most of the exotic quantum claims remain first-principles theory.**

## Summary

Transition metal dichalcogenides (TMDs) are compounds of the form MX2, where M is a transition metal (Mo, W, V-alloyed Mo) and X a chalcogen (S, Se, Te). They form covalently bonded triple layers held together by weak van der Waals forces, so single layers can be isolated or grown and then stacked without lattice matching. Monolayers have a direct band gap, strong spin-orbit coupling and inequivalent K/K' valleys, which is the origin of both the transistor interest and the valleytronics interest. The polytype matters as much as the chemistry: 2H is semiconducting, 1T' metallic, and 3R stacking breaks inversion symmetry and produces out-of-plane sliding ferroelectricity in bilayers.

Beyond logic, TMDs are being used as a substrate-like platform. Transfer printing without lattice mismatch motivates many-junction photovoltaics, although a conservative TMD gap window of 1.0 to 2.1 eV caps the detailed-balance efficiency near 63.4% at 50 junctions under full concentration, against 84.5% for an unconstrained ladder, with an experimentally plausible five-junction ladder identified. Subwavelength TMD films generate polarisation-entangled photon pairs by spontaneous parametric down-conversion without bulk phase matching, and periodic poling is being used to escape the coherence-length limit on efficiency. Proximity engineering supplies further knobs: a ferromagnetic V2O3 monolayer induces about 10.41 meV of zero-field valley splitting in WSe2, equivalent to roughly 10 T, with a Curie temperature of 500 K in calculation. The deciding parameters across all of this are the same three: growth uniformity and defect density, contact and doping control, and stacking or twist-angle fidelity.

## Viability (3/5)

The strongest evidence is device-level and recent. Monolayer MoS2 nanoribbon FETs at 30 to 40 nm width improved rather than degraded on scaling, reaching 995 microamps per micron in the best device, attributed to minimal edge-induced disorder and enhanced gate control. TMD flakes have been integrated on Si3N4 waveguides and characterised in situ using the waveguide's own defect photoluminescence as a source, which is the kind of prosaic result that indicates a platform is becoming workable rather than merely interesting. Entangled-photon generation from subwavelength van der Waals films is experimental, with periodic poling used to scale the interaction length.

**TLDR: Scaled MoS2 transistors and on-chip photonic integration are real; most valleytronic and orbitronic claims are still DFT.**

## Drivers (3/5)

Demand is well articulated on the electronics side. As silicon transistors scale, gate-all-around nanoribbon and complementary FET architectures require channel widths in the tens of nanometres to hit density targets, and that is precisely the regime where an atomically thin body offers electrostatic advantage. Secondary pulls exist in photovoltaics, where lattice-mismatch-free transfer printing removes the constraint that limits conventional multijunction stacks, and in quantum photonics, where a subwavelength source that bypasses phase matching removes bulk optics from the entangled-pair generation chain.

Supply is where the sources give little. CVD growth of specific polytypes is demonstrated for 3R-WSe2 bilayers and RF sputtering for MoTe2 films with a 1T' to 2H crossover near 4.5 nm thickness, but there is no wafer-scale yield, cost, precursor or fab-compatibility data in this evidence base. Nor is there any commercial or funding signal. The score reflects a strong demand pull with an unquantified supply chain.

**TLDR: Demand is a clear consequence of the silicon roadmap; supply-side evidence in these sources is thin.**

## Novelty (4/5)

In logic, the comparison is against silicon nanoribbons whose performance degrades as widths shrink; here narrowing the MoS2 channel improved both on-current density and subthreshold swing, a directional inversion of the usual scaling penalty, and it moved TMD FETs off the micrometre-width plateau that most reports occupy. In nonlinear optics, the incumbent is a macroscopic phase-matched crystal plus interferometers; a subwavelength TMD generates polarisation-entangled pairs natively from crystal symmetry, with periodic poling addressing the coherence-length ceiling. In nanophotonic patterning, anisotropic wet etching of multilayer 2H-WS2 yields crystallographically defined atomically sharp zigzag edges, eliminating the edge roughness that lithography and dry etching impose, and lithography-guided merging of etch fronts extends this beyond isolated triangles to long-range facets with 180-degree edge alignment.

**TLDR: The advantages over the incumbents are specific and, in several cases, quantified.**

## Diffusion (2/5)

The barriers named in the sources are all about reproducibility at scale rather than physics. CVD-grown 3R-WSe2 ferroelectric switching depends on intrinsic disorder, structural defects and multi-domain kinetics, which is exactly the failure mode that blocks a non-volatile memory from becoming a product. Most TMD FETs remain at micrometre widths, meaning the scaled results are still champion-device demonstrations rather than statistical distributions across a wafer. Twisted-stack devices depend on 3D atomic reconstruction that has until now had no experimental method for direct access; dark-field TEM is being extended to extract local displacements and interlayer distance, which shows the metrology gap is real and being closed only now.

There are cheaper diffusion paths. Integration of MoS2 and WS2 flakes onto Si3N4 photonic waveguides, characterised without an external source, is compatible with existing photonic foundry stacks and needs far less uniformity than logic does. Multijunction photovoltaics via transfer printing require the highest process throughput of any application here and, per the same analysis, radiative quality and optics dominate beyond five junctions, so incremental junction stacking buys little. A score of 2 reflects genuine early adoption routes against unresolved manufacturability.

**TLDR: Disorder, domain structure and stacking control are the gating problems, and metrology for them is only now arriving.**

## Impact (4/5)

The prize is a channel material that keeps improving where silicon stops, in the gate-all-around and CFET width regime that defines future density targets. Nothing else in this evidence base carries comparable economic weight. Secondary impacts are real but bounded: chip-scale entangled photon sources without bulk phase matching would simplify quantum photonic systems; zero-field valley splitting equivalent to roughly 10 T would remove magnets from valleytronic device concepts if it survives experiment; phase-selective orbital-charge conversion in 1T'-MoTe2 opens an orbitronic route for magnetic switching; and misfit layered compounds offer a bulk platform for Ising-protected superconductivity that would otherwise need exfoliated monolayers.

The photovoltaic case caps its own upside at 63.4% under full concentration for the TMD gap window, materially below the unconstrained 84.5%. Similarly, the exciton splittings that would underpin quantum information use are small, about 3 meV from a ferroelectric twisted bilayer hBN substrate, which places tight limits on operating temperature. Four is earned by the logic pathway alone, conditional on manufacturability.

**TLDR: A working sub-40 nm channel material would matter enormously; the non-logic applications are valuable but narrower.**

## Timing Later (5-10yr)

The logic case has only just cleared the width-scaling question, at 30 to 40 nm and single champion devices, and the sources contain no wafer-scale uniformity, contact resistance or yield data. Insertion into a production node therefore sits beyond the five-year horizon on this evidence. Photonic integration on Si3N4 and etched TMD nanophotonic structures could produce usable components sooner, since both are demonstrated and tolerate flake-scale material.

The valleytronic and orbitronic strands are earlier still. They are dominated by DFT predictions published in mid-2026 with no corresponding measurements in this set, and cold-atom quantum simulation of TMD-like excitons is being proposed as a way to study the physics at all. Treat those as ten-year-plus, if ever.

**TLDR: Photonic and metrology uses are near-term; a TMD logic channel is a next-decade decision.**

## Overrated or underrated? Fairly rated

TMDs are one of the few post-silicon channel candidates with a specific, quantified reason to believe: performance that improves rather than degrades as the ribbon narrows towards the widths that future architectures demand, with a champion device at 995 microamps per micron. That is a serious result and it justifies the attention the material class receives. It does not yet justify treating TMD logic as a solved materials problem, because the same body of work concedes that most devices remain at micrometre widths and because the one CVD-grown functional device here is limited by disorder and domain kinetics.

## Prediction

By 31 December 2028, a peer-reviewed or preprint report will demonstrate monolayer TMD FETs exceeding 1000 microamps per micron on-current density at channel widths at or below 40 nm, but no such device will be reported with statistical yield data across a full 300 mm wafer.

## Evidence base

- Monolayer MoS2 nanoribbon transistors narrowed from hundreds of nanometres to ~30-40 nm showed median on-current density up ~42% and subthreshold swing down ~16%, with a champion device at 995 microamps per micron at 1 V drain and 2.5 V overdrive 
- A conservative TMD bandgap window of 1.0-2.1 eV limits multijunction efficiency to ~63.4% under full concentration at N=50, versus 84.5% for unconstrained ladders, with radiative quality and optics dominating beyond five junctions 
- Ferroelectric switching in CVD-grown 3R-stacked WSe2 bilayers, probed via a graphene ferroelectric FET, is governed by intrinsic structural defects and multi-domain kinetics 
- Periodically poled TMDs were investigated to scale native polarisation-entangled photon generation beyond the material coherence length in subwavelength-thick films, without conventional phase matching 
- First-principles calculations predict ~10.41 meV spontaneous valley splitting in WSe2 from a kagome V2O3 monolayer, equivalent to ~10 T, with a Curie temperature of 500 K 
- RF-sputtered MoTe2 films show a structural crossover near 4.5 nm thickness, metallic 1T' below and semiconducting 2H above, with orbital-charge conversion detected only in the 1T' phase 
- MoS2 and WS2 flakes were characterised on Si3N4 waveguides using the waveguide's own broadband defect photoluminescence as an internal probe, with no external source 

## Open questions

- Do the ~42% on-current and ~16% subthreshold swing gains observed on narrowing MoS2 ribbons to 30-40 nm hold as median statistics across wafer-scale CVD material, rather than in champion devices on transferred flakes?
- Can the disorder and multi-domain kinetics that govern switching in CVD-grown 3R-WSe2 bilayers be suppressed enough for reproducible non-volatile ferroelectric operation?
- Do the calculated zero-field valley splittings (10.41 meV for V2O3/WSe2, 37.3 and 78.2 meV for Mo0.75V0.25Te2) survive experimental realisation at real interfaces, and at what temperature?
- Does periodic poling of TMDs raise SPDC conversion efficiency enough to compete with established phase-matched bulk crystals on brightness, not just on device thickness?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
