---
type: concept
slug: energy-harvesting
canonical_name: Energy Harvesting
aliases: []
kind: technology
parent_concepts:
- energy-power
- storage
related_concepts: []
sources:
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2025-2026-european-next-gen-pv-cohort]]'
frontier:
- Does the Sr0.19 pyroelectric composition retain its two-orders-of-magnitude leakage suppression and 5.5% efficiency over thousands of thermal cycles, or does the transitional-regime advantage degrade with cycling 2026 05 05 compositionally tuned phase transformations enhance pyroelec?
- Can the 12 dB RF harvesting gain be obtained without a coherent 8x8 distributed MIMO array, i.e. from infrastructure that a commercial deployment would plausibly already have 2026 06 04 integrated real time testbed for wideband rfid and wireless ?
- Do unified SWIPT receivers that share analogue hardware between rectification and demodulation actually beat separate receivers on end-to-end power budget, or only on component count 2026 07 27 nsf 2616563 cif unified swipt emerging models and de?
- Does chirality-controlled piezoelectricity in selenium nanowires translate from a piezoresponse-force-microscopy coefficient difference into measurable device power output 2026 07 07 chiropiezoelectric energy harvesting from lattice handedness?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 32
descendants: []
last_reorg_date: '2026-05-14'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 3
recent_mentions: []
neighbors: []
---
**Energy harvesting converts ambient light, heat, vibration or radio waves into microwatts-to-milliwatts of electricity to run sensors without batteries; indoor printed photovoltaics and RF/backscatter links are already at production or testbed stage, while thermal and piezoelectric routes remain low-efficiency laboratory physics.**

## Summary

Energy harvesting is the extraction of usable electrical power from energy already present in a device's environment: indoor or ambient light, small temperature differences, mechanical vibration, and radio-frequency fields. It is not a storage technology and not a grid technology. The target is the power budget of a wireless sensor node, typically microwatts averaged over time, and the commercial argument is the elimination of primary batteries and the maintenance and waste they imply. One NSF-funded project frames this directly for tyre-embedded sensors, where battery replacement across millions of vehicles with four tyres each generates substantial electronic waste.

The technology splits by transduction mechanism, and each has a different maturity. Photovoltaic harvesting from indoor light is the most industrial: printed organic PV makers have raised real money and are building roll-to-roll capacity, with one company extending a Series A to €30M in October 2025 and quadrupling capacity towards 600M cm²/yr **2025 2026 European Next Gen Pv Cohort**. Thermal routes are much earlier. A tuned Ba(1-x)Sr(x)TiO3 pyroelectric multilayer device delivered about 1.6 µA at 64 °C, an energy density of 1.6 mJ/cm³ per cycle and 5.5% conversion efficiency; a high-entropy Fe2VAl thermoelectric module reached an average figure of merit zT of only about 0.3 over 300-500 K; thermoradiative InAs diodes are still at the stage of characterising reverse saturation currents 200 times the radiative limit. RF harvesting sits between the two: an 8x8 distributed MIMO testbed at 2.45 GHz demonstrated effective harvesting gains up to 12 dB by exploiting channel state information.

The parameters that decide outcomes are unglamorous. On the source side: available flux (indoor lux, ΔT, vibration spectrum, incident RF power density) and the conversion coefficient of the material. On the load side: the quiescent current of the electronics that must survive on the harvest. A hardware-orchestrated power management architecture that power-gates the microcontroller and peripherals got total quiescent drain down to 452 nA, on the argument that in energy-scarce low-light conditions leakage, not conversion, is the dominant energy sink. That framing matters: for much of this field, progress in load power has done more than progress in transducers.

A large slice of current activity is materials search rather than device engineering: lead-free electromechanical oxides, chirality as a new degree of freedom in piezoelectric nanowires, magnet-free nonreciprocal thermal emitters, Nernst-type transverse heat-to-voltage conversion, and high-throughput screening for large shift-current photovoltaics. These are upstream of any product.

## Viability (3/5)

The sources contain end-to-end demonstrations, not just proposals. The pyroelectric multilayer produced a measured current and a measured 5.5% conversion efficiency from low-grade heat at 64 °C. A complete thermoelectric module was fabricated from scaled-up hot-pressed batches whose properties matched laboratory samples, which is a real manufacturability check even though zT_ave of about 0.3 is modest. RF harvesting gains of 12 dB were demonstrated on hardware with real-time channel estimation in under 2 ms of airtime. Indoor printed OPV is past the demonstration question entirely and into product iteration, with a module generation shown at CES 2026 claiming +30% performance **2025 2026 European Next Gen Pv Cohort**.

Against that: the thermoradiative branch is at the level of getting diode leakage under control, with reverse saturation current densities still 200 times the radiative limit and breakdown voltages just above 0.3 V. The near-field photon Nernst effect is a theoretical prediction bounded by Carnot, presented as a novel means of harvesting rather than a device. Chirality-controlled piezoelectricity is established so far by piezoresponse force microscopy on nanowires, not by a harvester output. Viability is therefore modality-dependent and the average is honestly middling.

**TLDR: Working devices exist in every modality, but measured efficiencies and currents are low outside indoor photovoltaics.**

## Drivers (3/5)

Supply is visible. Public funding is flowing to the specific sub-problems: $199,975 for bistable stochastic harvesting in self-powered tyres, $950,000 for unified simultaneous wireless information and power transfer receivers, $565,091 for circuit metamaterials with integrated sensing and harvesting, and $400,000 plus $1,200,000 across two collaborating institutions for lead-free electromechanical oxides. Private capital is concentrated in the indoor PV branch: €30M Series A extension in October 2025 including the EIC Fund and France 2030 instruments, and roughly $34M raised to date by a second printed-OPV firm **2025 2026 European Next Gen Pv Cohort**.

Demand is the weaker leg in the evidence. The pull is described qualitatively as IoT sensor deployment, wearables, soft robotics and structural or logistics monitoring, and as avoidance of battery replacement and e-waste. None of the sources gives shipment volumes, design-win counts or willingness-to-pay. One source is explicit that the closest historical analogue, far-field RF power transfer, has not found much commercial success despite decades of information-transmission progress. A regulatory driver towards lead-free piezoelectrics is implied by the framing of the DMREF projects but no rule or date is given.

**TLDR: Supply-side funding is documented and dated; demand is asserted in grant rationales rather than measured.**

## Novelty (3/5)

The clearest quantified advances: in the Ba(1-x)Sr(x)TiO3 system, tuning composition to Sr0.19 suppressed electrical leakage by over two orders of magnitude while retaining substantial polarisation, resolving the first-order-versus-second-order transformation trade-off that the authors say was previously unclear. High-entropy engineering of Fe2VAl produced one of the lowest lattice thermal conductivities reported for full-Heusler systems at about 2.3 W m⁻¹ K⁻¹. Magnetic Weyl semimetals such as Co3Sn2S2 are predicted to outperform conventional InAs for nonreciprocal thermal radiation while removing the requirement for an external magnetic field. Screening of over 154,000 entries yielded 32 materials with shift current above 100 µA/V², the strongest at 616 µA/V².

Two results are novel in kind rather than degree. Atomic chirality engineering is offered as a new mechanism for enhancing piezoelectricity, distinct from the composition, defect, strain and orientation strategies that preceded it, with right-handed selenium nanowires showing a higher effective coefficient than the left-handed enantiomer at identical composition. The in-plane anomalous Nernst observation removes the orthogonality constraint that had fundamentally limited Nernst device geometry. The caveat is that all of this is better than a weak incumbent: what these advances are improving upon are conversion efficiencies in the low single digits and figures of merit below one.

**TLDR: Several genuinely new mechanisms and one or two large quantified gains, but mostly improvements measured against low incumbent baselines.**

## Diffusion (2/5)

Indoor printed photovoltaics has an identifiable diffusion path: dedicated roll-to-roll factories, a stated capacity trajectory to 600M cm²/yr, a competitor with similar positioning, and equipment suppliers building lines for organic, perovskite and DSSC processes **2025 2026 European Next Gen Pv Cohort**. Adjacent flexible-perovskite scale-up gives dates (50 MW line, test production mid-2026, commercial output end-2027) which shows the manufacturing ecosystem is real even if the cells are aimed beyond indoor harvesting **2025 2026 European Next Gen Pv Cohort**.

Everywhere else the barriers are structural. Thermal harvesting must compete on cost, toxicity and scalability simultaneously, which is exactly why low-cost Fe2VAl is being pursued despite its modest zT. Piezoelectric incumbents contain lead, and the lead-free replacements are still at the design-space-exploration stage under a materials-informatics programme rather than qualified for products. RF harvesting requires either infrastructure (a distributed MIMO array with coherent channel estimation to get the 12 dB gain) or new unified receiver architectures that share analogue hardware between rectification and demodulation. And the whole category is gated on the load: without aggressive power gating, quiescent current dominates and autonomy collapses in low light, meaning adoption requires co-design of transducer, PMIC and firmware rather than a drop-in component.

**TLDR: One branch is shipping; the rest faces integration, efficiency and system-design barriers the sources do not resolve.**

## Impact (3/5)

The upside claimed in the sources is systemic rather than per-unit: eliminating periodic battery replacement across very large installed bases of sensors, with the tyre case used as the illustration of scale and of the electronic-waste consequence. Enabling classes of deployment that are currently impractical, such as autonomous nodes in low-light indoor environments and battery-free backscatter tags that also serve for indoor positioning, is a genuine capability change rather than a cost saving.

What the sources do not support is a claim on energy or economic scale. Low-grade heat harvesting is described as promising, but at 1.6 mJ/cm³ per cycle and 5.5% efficiency this is a sensor-power technology, not a waste-heat recovery technology at plant scale, and no source claims otherwise. Secondary impact channels appear in the materials work, where the same compositions serve spintronics, hyperthermia, catalysis, infrared photodetection and sensing; that spreads the option value but also means harvesting may not be the application that pays for the research.

**TLDR: Large in aggregate if battery-free sensing becomes default; small per device, and the sources quantify no economic value.**

## Timing Soon (2-5yr)

The near-term clock is set by the photovoltaic branch, which already has product releases and factory expansion in train, with a comparable flexible-cell line targeting commercial output at end-2027 **2025 2026 European Next Gen Pv Cohort**. Power management hardware that makes those harvests usable exists at 452 nA quiescent drain today, and the RF testbed work is at the stage where standards-adjacent signals (5G NR reference signals) are being used for excitation, which suggests integration work rather than physics work remains.

The rest of the field is on a research clock measured by grant duration. NSF awards issued in mid-2026 for tyre harvesters, unified SWIPT receivers and lead-free oxides are foundational-research vehicles. Thermoradiative diodes need orders-of-magnitude leakage reduction before device-level efficiency is meaningful, and near-field photon Nernst harvesting has not yet been built. Treat those as ten-year items.

**TLDR: Indoor light and RF harvesting are commercialising now; thermal and piezoelectric routes are five years or more from product relevance.**

## Overrated or underrated? Fairly rated

Energy harvesting is neither vapour nor breakthrough. The evidence supports a specific and narrow reading: ambient-light printed photovoltaics plus ultra-low-quiescent power management is a working commercial proposition with capital behind it **2025 2026 European Next Gen Pv Cohort**, and RF/backscatter harvesting is at credible testbed maturity with demonstrated 12 dB gains from array processing. The thermal and mechanical modalities are interesting physics with numbers that do not yet justify product planning: 5.5% pyroelectric efficiency, zT_ave 0.3, diode leakage 200x the radiative limit.

The error to avoid is treating the label as one technology. Someone hearing '5.5% efficiency' and '600M cm²/yr factory' in the same conversation will misprice both. The defensible position is that harvesting wins where the load is small and the alternative is a technician replacing a coin cell, and that most of the recent progress worth paying for has come from reducing what the load needs rather than from raising what the transducer supplies. If there is an underrated element here, it is the power-management and system co-design layer, which attracts little attention relative to the materials work.

## Prediction

By 31 December 2027, printed indoor/ambient-light organic photovoltaics will remain the only energy-harvesting modality in this evidence base with a named production line above 100 million cm²/yr, and no pyroelectric low-grade-heat harvester will have been reported at above 10% conversion efficiency in a multilayer device.

## Evidence base

## Open questions

- Does the Sr0.19 pyroelectric composition retain its two-orders-of-magnitude leakage suppression and 5.5% efficiency over thousands of thermal cycles, or does the transitional-regime advantage degrade with cycling?
- Can the 12 dB RF harvesting gain be obtained without a coherent 8x8 distributed MIMO array, i.e. from infrastructure that a commercial deployment would plausibly already have?
- Do unified SWIPT receivers that share analogue hardware between rectification and demodulation actually beat separate receivers on end-to-end power budget, or only on component count?
- Does chirality-controlled piezoelectricity in selenium nanowires translate from a piezoresponse-force-microscopy coefficient difference into measurable device power output?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
