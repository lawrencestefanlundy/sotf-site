---
type: concept
slug: gallium-nitride
aliases:
- GaN
- gallium nitride
- GaN-on-Si
- GaN-on-SiC
canonical_name: Gallium Nitride
parent_concepts:
- wide-bandgap-semiconductors
- power-electronics
related_concepts:
- wide-bandgap-semiconductors
- silicon-carbide
- aluminium-gallium-nitride
- indium-gallium-nitride
- power-electronics
- compound-semiconductors
- mocvd-mbe
sources:
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-02-12-how-to-invest-in-ai-sovereignty-sovereign]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-05-26-semianalysis-800vdc-revolution]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-09-02-vertical-power-delivery-thermal-limits]]'
frontier:
- Does the sputtered sub-nanometre silicide template on Si(111) survive to a complete vertical device with measured blocking voltage, leakage and switching loss, and at what wafer diameter 2026 05 04 an advanced epitaxial strategy enabling vertical gan devices?
- Can the 2000 Ω/square channel sheet resistance in N-polar AlN/GaN HEMTs be reduced without losing the abrupt heterostructure that delivered the 10,000 on/off ratio 2026 05 15 depletion mode n polar aln based high electron mobility tran?
- Does the 24.4% surrogate-model accuracy gain on 468 MIS-HEMTs generalise to other process flows and to yield prediction, or is it dataset-specific 2026 05 28 hybrid classical quantum neural networks for multi character?
- How does GaN compare with silicon carbide and silicon on cost per amp and per volt at equivalent reliability? No supplied source addresses this.
- Will GaN-on-Si reach 650V yield and reliability parity with GaN-on-SiC at 8-inch, or does substrate-induced defect density remain a ceiling?
- Can GaN power ICs (gate driver + FET monolithic) pull further system integration away from silicon ASIC + discrete topology?
- Does GaN capture any share above 650V (1200V class) once vertical GaN device architectures mature, challenging SiC's lock on EV traction?
last_updated: '2026-08-31'
tags:
- concept
descendants:
- aluminium-gallium-nitride
- indium-gallium-nitride
mention_count: 33
scorecard:
  viability: 4
  drivers: null
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 3
sources_30d: 4
recent_mentions:
- slug: 2026-09-02-vertical-power-delivery-thermal-limits
  title: 'Vertical power delivery: the thermal limit at the 48V-to-point-of-load stage'
  date: '2026-09-02'
  kind: web
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-22-sintered-metal-die-attach-landscape
  title: Sintered-silver / sintered-copper die-attach landscape — physics, incumbents, AI-migration question (web research synthesis)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-22-tim-approaches-full-sweep
  title: TIM approaches — exhaustive in-market + R&D sweep (vendors, classes, startups)
  date: '2026-06-22'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-05-26-semianalysis-800vdc-revolution
  title: Inside the 800VDC Revolution – Part 1
  date: '2026-05-26'
  kind: web
- slug: 2026-04-20-fixing-the-gan-problem
  title: Fixing the GaN Problem
  date: '2026-04-20'
  kind: web
neighbors:
- slug: wide-bandgap-semiconductors
  name: Wide-Bandgap Semiconductors
  path: /materials/substrates/wide-bandgap-semiconductors/
  macro: materials
- slug: silicon-carbide
  name: Silicon Carbide
  path: /materials/substrates/silicon-carbide/
  macro: materials
- slug: aluminium-gallium-nitride
  name: Aluminium Gallium Nitride
  path: /materials/functional-layers/aluminium-gallium-nitride/
  macro: materials
- slug: indium-gallium-nitride
  name: Indium Gallium Nitride
  path: /materials/functional-layers/indium-gallium-nitride/
  macro: materials
- slug: power-electronics
  name: Power Electronics
  path: /energy-power/power-electronics/power-electronics/
  macro: energy-power
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /materials/substrates/compound-semiconductors/
  macro: materials
- slug: mocvd-mbe
  name: MOCVD / MBE
  path: /manufacturing/equipment-processes/mocvd-mbe/
  macro: manufacturing
---
**Gallium nitride is a wide-bandgap semiconductor whose AlGaN/GaN heterostructures underpin high-efficiency RF amplifiers and power switches; the current research frontier is moving it from lateral devices on foreign substrates to vertical devices on cheap silicon wafers, where interface resistance is still the binding constraint.**

## Summary

Gallium nitride (GaN) is a compound semiconductor with a wide bandgap and high electron velocity. Its most commercially important trick is the heterostructure: stacking a thin aluminium gallium nitride (AlGaN) or aluminium nitride (AlN) barrier on a GaN channel creates a two-dimensional electron gas at the interface without intentional doping, giving a high-electron-mobility transistor (HEMT) that switches faster and with lower loss than a comparable silicon device. This makes GaN attractive in two distinct markets: radio-frequency power amplifiers, and power conversion (chargers, inverters, data-centre supplies). The same material family also emits blue and ultraviolet light, which is why GaN epitaxy and micro-LED work sit alongside the transistor work.

The engineering problem is almost entirely about crystal growth on substrates that are not GaN. Bulk GaN wafers are scarce, so devices are grown epitaxially on silicon or sapphire, which have different lattice constants and thermal expansion. Today's mainstream devices are *lateral*: current flows sideways through the 2DEG, and the buffer layer that absorbs the lattice mismatch does not have to conduct. *Vertical* devices, which would carry current through the substrate and scale better to high voltage and to dense micro-LED arrays, are blocked precisely because those conventional buffer layers are electrically resistive. One 2026 approach forms a sub-nanometre silicide template on Si(111) by sputtering plus rapid thermal annealing, producing an amorphous-like interlayer that relaxes strain while remaining ohmic, and reported to work across 25 different metal species before MOCVD overgrowth. Related growth work is still at the level of controlling where GaN nucleates on patterned sapphire as a function of mask growth temperature.

The parameters that decide GaN device quality are visible in the device papers. For HEMTs: channel sheet resistance, threshold voltage and its stability, on/off current ratio, on-resistance and gate leakage. N-polar AlN-based HEMTs with a 5.2 nm GaN channel reached on/off ratios of 10,000 and saturation currents over 240 mA/mm, but on-resistance of about 20 Ω·mm and the high-frequency performance were all limited by a 2000 Ω/square channel sheet resistance. For circuits, the figure of merit is efficiency at back-off: GaN HEMT Doherty amplifier prototypes measured over 44.2 dBm saturated output with peak drain efficiency above 71.2% across 2.6-2.8 GHz, and 64% at 6 dB back-off with ACLR better than -51.3 dBc after digital predistortion.

A supporting theme in the 2026 literature is that GaN process development is data-limited, and machine learning is being used to compensate. A hybrid classical-quantum neural network trained on 468 fabricated recessed-gate AlGaN/GaN MIS-HEMTs across 17 process splits predicted six electrical targets from a 24-dimensional process vector, cutting normalised RMSE by 24.4% against a classical ANN baseline. Similar tooling appears in materials simulation (machine-learning-accelerated pathway calculations including GaN, up to 7-fold speedup) and in contact-free doping metrology by terahertz spectroscopy covering SiC, Si and GaN layer stacks.

## Viability (4/5)

The sources contain real hardware, not proposals. Two GaN HEMT Doherty amplifier prototypes were fabricated and measured at over 44.2 dBm saturated power, above 71.2% peak drain efficiency in 2.6-2.8 GHz and 64% efficiency at 6 dB back-off. A dataset of 468 fabricated recessed-gate AlGaN/GaN MIS-HEMTs across 17 process splits exists and is being mined for process models. Depletion-mode N-polar AlN/GaN HEMTs were built and characterised. Contact-free doping metrology for GaN layer stacks has been validated against measurements. That is a working technology, not a lab curiosity.

The caveats are specific and admitted. Vertical GaN-on-silicon deployment 'remains bottlenecked by the high electrical resistance of conventional epitaxial buffer layers', and the proposed sputtered silicide template is demonstrated at the level of epitaxial film quality and ohmic behaviour rather than a finished power device with blocking voltage and reliability data. In the N-polar HEMTs, every performance metric that matters (on-resistance, high-frequency response) is pinned by a 2000 Ω/square sheet resistance, which is an unsolved materials problem rather than a design choice. The score reflects demonstrated lateral RF devices; the vertical route on its own would score lower.

**TLDR: Fabricated, measured devices with credible numbers; the vertical-on-silicon variant is not there yet.**

## Drivers (unscored)

Nothing in the supplied material quantifies supply or demand. The only demand-side statements are author motivations: vertical GaN-on-silicon architectures 'promise a transformative leap in cost-effective power electronics and high-resolution micro-LEDs', and the Doherty amplifier work is framed around efficiency at back-off, which is the operating condition of cellular base stations. Neither is evidence of volume, pricing or capacity.

One supply-side signal is indirect but real: experimental semiconductor datasets are described as costly, which is why a 468-device dataset is treated as a scarce asset worth building surrogate models around. That tells you process development is expensive. It does not tell you whether epitaxy capacity, substrate supply or gallium feedstock constrain the industry. Score withheld.

**TLDR: The sources carry no market, cost, capacity or demand data.**

## Novelty (3/5)

Where the sources make comparisons, they are internal to GaN and reasonably large. The N-polar AlN-based HEMTs report on/off ratios up to 10,000, described as 'much higher than previously reported N-polar AlN-based HEMTs', attributed to an abrupt AlN/GaN heterostructure with a dedicated AlN transition layer and reduced gate leakage. The epitaxial template work claims low vertical resistance and ohmic behaviour where conventional buffers are resistive, plus 'unprecedented versatility' across 25 metallic species. On the design-tooling side, the hybrid quantum-classical model beats a classical ANN by 24.4% in overall normalised RMSE, with target-wise gains that are modest in absolute terms (threshold voltage RMSE 0.297 V to 0.270 V).

What is missing is the comparison that decides commercial novelty: GaN against silicon and silicon carbide at equivalent voltage, current and cost. No source supplies it. The terahertz metrology paper places GaN alongside SiC and Si as materials to be characterised, but that is a measurement-scope statement, not a performance benchmark. Score 3 reflects genuine but incremental advances inside a mature material system, with the cross-material case unproven by these sources.

**TLDR: Clear improvements over prior GaN benchmarks; no comparison in the sources against silicon or silicon carbide.**

## Diffusion (2/5)

The sources are explicit about what blocks adoption of the frontier architectures. Vertical GaN-on-silicon is bottlenecked by buffer layer resistance. N-polar HEMT performance is capped by channel sheet resistance. Nucleation control on patterned sapphire is still being mapped as a function of mask growth temperature, with non-monotonic behaviour in the number of isolated GaN domains, which is the signature of a process not yet under control. Process-induced variability is described as something simulations cannot faithfully reproduce, forcing reliance on expensive experimental splits.

Two things would ease diffusion and both appear in the sources: contact-free doping metrology that works on realistic multi-layer GaN stacks, useful for inline process control, and inverse-design tooling that produced fabricated, working amplifier prototypes rather than simulations only. Note that the sources say nothing about qualification, reliability standards, packaging or customer uptake, so this score is about technical readiness of the newer variants only, not about the installed base of existing lateral GaN products.

**TLDR: The named barriers are all epitaxy and process control, and they are still open for the newer device architectures.**

## Impact (3/5)

The most tangible impact evidence is amplifier efficiency: above 71.2% peak drain efficiency and 64% at 6 dB back-off across 2.6-2.8 GHz, with ACLR better than -51.3 dBc after digital predistortion. Back-off efficiency is where transmitter energy is actually spent, so gains there translate directly into operating cost and thermal design, though the sources do not quantify that translation.

Beyond RF, impact rests on the vertical-on-silicon thesis: cost-effective power electronics and high-resolution micro-LEDs from cheap Si(111) substrates rather than bulk GaN or sapphire. If that holds, it changes the cost structure of a large device class. The sources give no cost figures, no yield data and no wafer-diameter demonstration, so the magnitude is unverified. A secondary, smaller impact channel appears in GaN as a photonic and terahertz material: an AlGaN/GaN plasmonic-crystal analyser reconstructing terahertz spectra without an interferometer, with reconstruction error reduced 3.6 times versus a Tikhonov baseline in FTIR mode, and a GaN hollow nanowire cavity generating orbital angular momentum light with |l| = 5.7, 97% mode purity and Q of about 250 in a sub-micron footprint. Both are early-stage instrument-level results.

## Timing Soon (2-5yr)

For RF power amplifiers, GaN HEMTs are already at the stage where the interesting research is circuit design methodology rather than the transistor, with fabricated prototypes hitting 44.2 dBm and above 71.2% peak drain efficiency. That part of the technology is 'Now' in everything but the sources' ability to prove market adoption.

The frontier that this page is really about sits later. The vertical-on-silicon epitaxy result is a film-quality and interface-resistance demonstration published in May 2026, and the N-polar HEMT work is still limited by a 2000 Ω/square channel. Moving from those to qualified devices requires wafer-scale uniformity, blocking-voltage and reliability data that no source provides. Two to five years is the reasonable band for first device-level validation of the vertical route; commercial volume could be later.

**TLDR: Lateral GaN RF devices are already producing measured circuit-level results; vertical GaN-on-silicon needs several years of epitaxy and device work.**

## Overrated or underrated? Fairly rated

The evidence base here describes a technology that already works in its mature form and has a specific, named obstacle in its ambitious form. That is the profile of something fairly rated rather than hyped or overlooked. Measured amplifier prototypes with 64% efficiency at 6 dB back-off and 468-device process datasets are the signatures of an industrialised material, not an emerging one. At the same time, the honest framing of vertical GaN-on-silicon as 'bottlenecked' by buffer resistance shows the field is not overselling the unsolved part.

The caveat for readers: this source set is thin in a specific way. It contains no market data, no cost comparison against silicon carbide, and no reliability or qualification results. Several apparent GaN references in adjacent literature are keyword collisions with generative adversarial networks or with author surnames, so the genuine GaN evidence here is roughly eight papers, all research-stage. Anyone underwriting a GaN investment thesis needs commercial evidence that these sources do not contain.

## Prediction

By 30 June 2028, peer-reviewed N-polar AlN/GaN HEMT results will report channel sheet resistance below 1000 Ω/square, at least halving the 2000 Ω/square value that limited on-resistance and high-frequency performance in the May 2026 devices.

## Evidence base

- 4 May 2026: vertical GaN-on-silicon is described as bottlenecked by high buffer-layer resistance; a sputtered 0.5 nm silicide template formed by rapid thermal annealing, demonstrated across 25 metallic species, yields low vertical resistance and ohmic behaviour with an amorphous-like interlayer accommodating lattice mismatch, and supports MOCVD overgrowth.
- 15 May 2026: depletion-mode N-polar AlN-based HEMTs with a 5.2 nm GaN channel show threshold voltage -2.4 to -3.0 V, saturation current over 240 mA/mm and on/off ratio up to 10,000, with on-resistance about 20 Ω·mm limited by 2000 Ω/square sheet resistance.
- 18 June 2026: two fabricated GaN HEMT Doherty PA prototypes with pixelated three-port combiners measured above 44.2 dBm saturated output and above 71.2% peak drain efficiency in 2.6-2.8 GHz, 64% drain efficiency at 6 dB back-off, and ACLR better than -51.3 dBc after digital predistortion.
- 28 May 2026: a hybrid classical-quantum neural network trained on 468 fabricated recessed-gate AlGaN/GaN MIS-HEMTs across 17 process splits reduced overall normalised RMSE by 24.4% versus a classical ANN, with threshold-voltage RMSE improving from 0.297 V to 0.270 V.
- 6 May 2026: an electrically tunable AlGaN/GaN plasmonic-crystal analyser with neural-network inversion reconstructed terahertz spectra with MSE 0.015 in FTIR mode and 0.038 in direct mode, reducing mean error 3.6 times versus a Tikhonov baseline.
- 16 June 2026: GaN nucleation inside SiO2 openings on patterned sapphire shifts from edge-biased to inward and sparse as boron-compound mask growth temperature rises above 700-750 °C, with non-monotonic domain counts, indicating incomplete process control at the nucleation stage.

## Open questions

- Does the sputtered sub-nanometre silicide template on Si(111) survive to a complete vertical device with measured blocking voltage, leakage and switching loss, and at what wafer diameter?
- Can the 2000 Ω/square channel sheet resistance in N-polar AlN/GaN HEMTs be reduced without losing the abrupt heterostructure that delivered the 10,000 on/off ratio?
- Does the 24.4% surrogate-model accuracy gain on 468 MIS-HEMTs generalise to other process flows and to yield prediction, or is it dataset-specific?
- How does GaN compare with silicon carbide and silicon on cost per amp and per volt at equivalent reliability? No supplied source addresses this.

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
