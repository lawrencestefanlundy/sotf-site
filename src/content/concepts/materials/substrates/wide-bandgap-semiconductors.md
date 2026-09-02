---
type: concept
slug: wide-bandgap-semiconductors
canonical_name: Wide-Bandgap Semiconductors
aliases:
- WBG
- wide bandgap
- ultra-wide-bandgap
- UWBG
- WBG semiconductors
parent_concepts:
- compound-semiconductors
related_concepts:
- silicon-carbide
- gallium-nitride
- aluminium-gallium-nitride
- indium-gallium-nitride
- compound-semiconductors
- power-electronics
- silicon-carbide-photonics
sources:
- '[[2017-10-10-arpa-e-funds-projects-using-wide-bandgap-semiconductors-for-]]'
frontier:
- Can interfacial thermal boundary conductance in heterointegrated stacks such as Ga2O3 on SiC be raised enough, and verified experimentally rather than by simulation, to let UWBG devices run at the current densities their breakdown fields imply?
- Do the record UWBG device results survive translation from epitaxial regrowth and electron-beam lithography to production-compatible processes and larger areas?
- Is controllable doping, including any usable p-type route, achievable in AlN, Ga2O3 and diamond, given that even Fermi-level determination in diamond currently requires indirect photoluminescence analysis?
- Will physics-based radiation and reliability models arrive fast enough to replace per-mission empirical qualification, which is currently the cost barrier for space and defence adoption?
- Can ultra-wide-bandgap materials (AlN ~6.2 eV, Ga2O3 ~4.9 eV, diamond ~5.5 eV) move from lab to commercially manufacturable devices before 2030?
- Will WBG substrates (SiC, GaN boule) ever reach silicon-scale wafer economics, or will material cost permanently cap WBG to premium applications?
- Does WBG device integration into standard CMOS packaging (co-packaged power + logic) unlock a new architecture for AI compute racks beyond the current discrete power stage?
last_updated: '2026-08-31'
tags:
- concept
descendants:
- aluminium-gallium-nitride
- gallium-nitride
- indium-gallium-nitride
- silicon-carbide
mention_count: 18
scorecard:
  viability: 4
  drivers: 4
  novelty: 4
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 4
recent_mentions:
- slug: 2017-10-10-arpa-e-funds-projects-using-wide-bandgap-semiconductors-for-
  title: ARPA-E Funds Projects Using Wide Bandgap Semiconductors for Power Conversion - Electronic Design
  date: '2017-10-10'
  kind: web
neighbors:
- slug: silicon-carbide
  name: Silicon Carbide
  path: /materials/substrates/silicon-carbide/
  macro: materials
- slug: gallium-nitride
  name: Gallium Nitride
  path: /energy-power/power-electronics/gallium-nitride/
  macro: energy-power
- slug: aluminium-gallium-nitride
  name: Aluminium Gallium Nitride
  path: /materials/functional-layers/aluminium-gallium-nitride/
  macro: materials
- slug: indium-gallium-nitride
  name: Indium Gallium Nitride
  path: /materials/functional-layers/indium-gallium-nitride/
  macro: materials
- slug: compound-semiconductors
  name: Compound Semiconductors
  path: /materials/substrates/compound-semiconductors/
  macro: materials
- slug: power-electronics
  name: Power Electronics
  path: /energy-power/power-electronics/power-electronics/
  macro: energy-power
- slug: silicon-carbide-photonics
  name: Silicon Carbide Photonics
  path: /materials/substrates/silicon-carbide-photonics/
  macro: materials
---
**Wide-bandgap semiconductors are substrate materials such as SiC, GaN, AlGaN, AlN, Ga2O3 and diamond whose larger electronic bandgap allows power switches, UV detectors and photonic devices to operate at voltages, temperatures, radiation doses and optical wavelengths where silicon fails; the SiC/GaN layer is already in service while the ultra-wide-bandgap frontier is still fighting heat removal and process complexity in the lab.**

## Summary

A semiconductor's bandgap is the energy needed to lift an electron into conduction. Making it larger has three consequences that matter for devices. First, the material tolerates a much higher electric field before avalanche breakdown, so a power transistor blocking a given voltage can use a thinner, more heavily doped drift region and therefore has lower conduction loss. Second, intrinsic carrier generation stays negligible at high temperature and under ionising radiation, so devices keep working in engine bays, reactor halls and orbit. Third, the material is transparent further into the ultraviolet and does not absorb two near-infrared photons at once, which makes it useful for solar-blind detectors and for nonlinear photonics. The family runs from the commercial wide-bandgap (WBG) materials, silicon carbide and gallium nitride, to the ultra-wide-bandgap (UWBG) set: AlGaN and AlN, gallium oxide, diamond, and in photonics oxides such as tantalum pentoxide.

The sources here show that the WBG base layer is established. SiC polymorphs are described as widely employed nuclear materials, mechanical components and wide-bandgap semiconductors, and AlGaN/GaN HEMTs are described as essential to satellite communications, defence radar, GPS and deep-space missions. Public funding for wide-bandgap power conversion goes back at least to ARPA-E's 2017 awards <sup class="ref"><a href="https://news.google.com/rss/articles/CBMi9wFBVV95cUxPX3FzQjlSc3U3RnV6MXVuQTQxcWlZMUpNd3lITjRUdVpUWjZrczlVWUlLb1JfaWtTdmpFT0FvLXJKaTQ2ZlRhd1EwVjBadWFvUm1zWV92bWt1MUh3LUJTR1cxZDNtV0J3SGZHTkk1d3JZUlhocmJpSHZkYXA5REticW5QWkhWNmt6U0hLbDhwazBNejdEdkY3enhqLWhFcV9LRnB1a3Zhc2tZMDZ5QnBQcGktQWZRcTE1WkFZVUVOUUI4eV8tSmRjVGo4eFJSRl9ZWS1vbnV6N2JBcU96MC1zX3I5bnNOWXBncnBGUHBlUGk0S1VLQ0hV?oc=5" title="ARPA-E Funds Projects Using Wide Bandgap Semiconductors for Power Conversion - Electronic Design" rel="noopener">ref</a></sup>.

The live research frontier is UWBG, and the 2026 record here is device-level rather than product-level. An epitaxially regrown AlN gate interlayer on UWBG AlGaN polarisation-graded FETs produced an average breakdown field above 6.94 MV/cm with on-state current above 1 A/mm and a power-switching figure of merit above 1.87 GW/cm2 at a breakdown voltage above 1.45 kV. A vertical gallium oxide transistor was demonstrated without planarisation etch-back or mid-gap acceptor blocking layers, with 200 nm fins, a threshold voltage of 2 V and an on/off ratio above 1e7, and was presented as comparable to existing vertical transistors but more manufacturable. Outside power switching, sub-bandgap AlN Schottky photodetectors gave non-saturating linear response to blue light above 40 W/cm2 and undistorted response to at least 300 °C.

The parameters that decide the outcome are: breakdown field and figure of merit actually achieved in manufacturable geometries; heat extraction, since interfacial thermal boundary conductance at heterointegrated interfaces such as Ga2O3 on SiC is called a major heat-removal bottleneck; controllable doping, still hard enough in diamond that measuring the Fermi energy requires indirect photoluminescence methods; and process compatibility, since several of the best results depend on epitaxial regrowth or electron-beam lithography.

## Viability (4/5)

Viability is well supported at two levels. SiC is treated in the literature as an in-use wide-bandgap semiconductor alongside its nuclear and mechanical roles, and AlGaN/GaN HEMTs are described as already underpinning satellite communications, radar and GPS. At the UWBG frontier there are working devices with hard numbers rather than projections: 6.94 MV/cm average breakdown field, >1 A/mm on-current and >1.87 GW/cm2 switching figure of merit on AlGaN PolFETs, and an enhancement-mode vertical Ga2O3 FET with on/off above 1e7.

The deductions are physical, not speculative. Interfacial thermal boundary conductance is named as a major heat-removal bottleneck for Ga2O3/SiC heterointegration, and direct experimental access to intrinsic interfacial transport remains limited, which is why the work relies on a neural network potential rather than measurement. Doping control is similarly immature: in diamond the Fermi energy has to be inferred from NV charge-state populations because its relation to donor and acceptor concentrations is highly nonlinear. Radiation response of even the mature GaN devices is modelled by approximate, trial-and-error methods rather than physical understanding, forcing per-mission testing. So the answer is: it works, and the UWBG members work in single devices, with thermal and doping physics still the gating problems.

**TLDR: The WBG layer is in service and UWBG devices now hit quantified figures of merit, but heat removal and doping remain unsolved.**

## Drivers (4/5)

Supply side: wide-bandgap materials are explicitly named as one of the "More than Moore" domains where positions are still forming and where Europe's defensible strategy lies, in an analysis of roughly 1,550 semiconductor startups, with a proposed Chips Act 2.0 in June 2026 adding demand-side measures for the first time. US public funding is long-running and continuing, from ARPA-E awards for wide-bandgap power conversion in 2017 <sup class="ref"><a href="https://news.google.com/rss/articles/CBMi9wFBVV95cUxPX3FzQjlSc3U3RnV6MXVuQTQxcWlZMUpNd3lITjRUdVpUWjZrczlVWUlLb1JfaWtTdmpFT0FvLXJKaTQ2ZlRhd1EwVjBadWFvUm1zWV92bWt1MUh3LUJTR1cxZDNtV0J3SGZHTkk1d3JZUlhocmJpSHZkYXA5REticW5QWkhWNmt6U0hLbDhwazBNejdEdkY3enhqLWhFcV9LRnB1a3Zhc2tZMDZ5QnBQcGktQWZRcTE1WkFZVUVOUUI4eV8tSmRjVGo4eFJSRl9ZWS1vbnV6N2JBcU96MC1zX3I5bnNOWXBncnBGUHBlUGk0S1VLQ0hV?oc=5" title="ARPA-E Funds Projects Using Wide Bandgap Semiconductors for Power Conversion - Electronic Design" rel="noopener">ref</a></sup> to a $450,000 NSF award dated 4 August 2026 for radiation-aware AlGaN/GaN HEMT transport modelling with Los Alamos. The wider macro backdrop is a claimed bits-to-atoms deep-tech supercycle driven by sovereignty, industrial policy and surging energy demand **2026 06 Drumbeat Deep Tech Report**.

**TLDR: Policy money and extreme-environment demand are both documented; the sources do not quantify the volume markets.**

## Novelty (4/5)

Against the nearest comparators named in the sources, the margins are specific. The AlN gate interlayer result is claimed as state of the art for lateral field effect transistors on breakdown field, at above 6.94 MV/cm, while holding on-current above 1 A/mm, a combination normally traded off. In photodetection the advance is a change of kind, not degree: conventional photodetectors are optimised for weak signals and saturate at low-to-moderate intensity, whereas the sub-bandgap AlN device stays linear above 40 W/cm2 and to at least 300 °C by using deep levels at a metal-AlN Schottky junction with a deliberately narrow space charge region. In photonics, tantalum pentoxide offers a 300-8000 nm transparency window and a nonlinear refractive index three times that of silicon nitride, with the wide bandgap suppressing two-photon absorption at short wavelengths, and gamma-phase GaS nanobelts give second-harmonic intensities comparable to GaSe while being integrable on SiN waveguides.

Two qualifications. First, the sources contain no numerical silicon baseline, so the headline claim of the field, that wide-bandgap devices beat silicon on loss and voltage, is assumed rather than evidenced here. Second, some novelty is process novelty rather than performance novelty: the vertical Ga2O3 ISEFET is presented as comparable to existing vertical transistors, its advantage being that it removes planarisation etch-back and mid-gap acceptor regions and is therefore suited to high-throughput prototyping and large-scale manufacturing. That is a real but different kind of contribution.

**TLDR: Documented gains over the stated alternatives in three separate device classes, though no quantified silicon baseline appears in the sources.**

## Diffusion (3/5)

Diffusion has effectively already happened for the older members of the family: SiC is a widely employed wide-bandgap semiconductor and GaN devices are embedded in fielded satellite and defence systems. For the UWBG materials the barriers in these sources are of four kinds. Heat: interfacial thermal boundary conductance is the named bottleneck for Ga2O3 heterointegration, and it degrades with transport length. Process: the best AlGaN result depends on epitaxially regrown interlayers, and the Ga2O3 vertical device used electron-beam lithography for 200 nm fins, with manufacturability an aspiration rather than a demonstration. Doping and metrology: the diamond Fermi-energy work shows how immature basic electrical characterisation still is in the widest-gap materials. Qualification: absent physics-based radiation models, every mission requires costly bespoke testing.

There is also an ecosystem barrier on the commercial side. The European analysis frames wide-bandgap as a domain where positions are still forming and identifies funding velocity and exits as the binding gaps for converting semiconductor research into industrial leadership. The sources give no data on substrate supply, wafer diameter, yield or cost, which are the usual determinants of whether a new substrate diffuses, so a score above 3 cannot be justified from this evidence.

**TLDR: GaN and SiC have already diffused into RF and industrial use; the UWBG frontier faces thermal, doping and process barriers the sources name but do not resolve.**

## Impact (3/5)

The mechanism for large impact is clear. A switching figure of merit above 1.87 GW/cm2 at a breakdown voltage above 1.45 kV is the metric that determines converter loss and size, and the macro thesis in the analyst material treats surging energy demand and power as a binding constraint **2026 06 Drumbeat Deep Tech Report**, which is exactly where efficiency gains in power conversion compound. Beyond power, the same material property opens instrumentation that currently does not exist: linear optical measurement in bright, hot environments for industrial process control, thermal and nuclear power generation and spaceflight, solar-blind UV-C detection with radiation hardness and spectral selectivity across a broad application range, and ultraviolet-to-mid-infrared frequency combs on chip using wide-bandgap oxides.

The honest limit is that none of the supplied sources attaches a number to any of this: no market size, no efficiency delta against silicon systems, no energy saved, no cost per watt. The strategic framing that wide-bandgap materials are a domain where industrial positions are still forming supports the claim that the prize is worth contesting, but not its size. A 3 reflects a well-founded direction with unquantified magnitude.

**TLDR: Plausibly large across power conversion, extreme-environment sensing and UV photonics, but no source here quantifies the value.**

## Timing Now (0-2yr)

The category as a whole matters now. SiC is described as widely employed, GaN RF devices are in fielded space and defence systems, and public funding for wide-bandgap power conversion dates back to at least 2017 <sup class="ref"><a href="https://news.google.com/rss/articles/CBMi9wFBVV95cUxPX3FzQjlSc3U3RnV6MXVuQTQxcWlZMUpNd3lITjRUdVpUWjZrczlVWUlLb1JfaWtTdmpFT0FvLXJKaTQ2ZlRhd1EwVjBadWFvUm1zWV92bWt1MUh3LUJTR1cxZDNtV0J3SGZHTkk1d3JZUlhocmJpSHZkYXA5REticW5QWkhWNmt6U0hLbDhwazBNejdEdkY3enhqLWhFcV9LRnB1a3Zhc2tZMDZ5QnBQcGktQWZRcTE1WkFZVUVOUUI4eV8tSmRjVGo4eFJSRl9ZWS1vbnV6N2JBcU96MC1zX3I5bnNOWXBncnBGUHBlUGk0S1VLQ0hV?oc=5" title="ARPA-E Funds Projects Using Wide Bandgap Semiconductors for Power Conversion - Electronic Design" rel="noopener">ref</a></sup>. Anyone treating wide-bandgap as a future technology is a decade behind.

The frontier described in the 2026 sources runs on a different clock. Single-device demonstrations of UWBG AlGaN and Ga2O3 transistors appeared in mid-2026, while the interfacial heat-removal problem is still being attacked with simulation because direct experimental access is limited and radiation-response modelling for the mature GaN case is only now being funded. That sequence, from first device to thermal packaging solution to reliability qualification, does not compress into two years. Investors should read the band as two-speed: revenue now in SiC and GaN, optionality later in UWBG.

**TLDR: The SiC and GaN layer is already deployed; the UWBG members in these sources are 5-10 years from qualified products.**

## Overrated or underrated? Fairly rated

Wide-bandgap semiconductors are correctly identified as a durable materials platform rather than a fashion, and the supplied evidence supports that: working commercial devices at the SiC and GaN end, credible new figures of merit at the UWBG end, and both US and European policy pointing at the sector <sup class="ref"><a href="https://news.google.com/rss/articles/CBMi9wFBVV95cUxPX3FzQjlSc3U3RnV6MXVuQTQxcWlZMUpNd3lITjRUdVpUWjZrczlVWUlLb1JfaWtTdmpFT0FvLXJKaTQ2ZlRhd1EwVjBadWFvUm1zWV92bWt1MUh3LUJTR1cxZDNtV0J3SGZHTkk1d3JZUlhocmJpSHZkYXA5REticW5QWkhWNmt6U0hLbDhwazBNejdEdkY3enhqLWhFcV9LRnB1a3Zhc2tZMDZ5QnBQcGktQWZRcTE1WkFZVUVOUUI4eV8tSmRjVGo4eFJSRl9ZWS1vbnV6N2JBcU96MC1zX3I5bnNOWXBncnBGUHBlUGk0S1VLQ0hV?oc=5" title="ARPA-E Funds Projects Using Wide Bandgap Semiconductors for Power Conversion - Electronic Design" rel="noopener">ref</a></sup>. There is no case here for calling the category overrated.

Where the market is likely to be wrong is inside the category. Headline UWBG figures of merit such as 6.94 MV/cm and 1.87 GW/cm2 measure the material and the small device, not the system, and the same source base states plainly that heat removal at heterointegrated interfaces is a major bottleneck and that basic doping metrology in the widest-gap materials is still under development. The underappreciated line in the evidence is process simplification rather than record-setting: removing planarisation and mid-gap acceptor steps from a vertical Ga2O3 flow is the kind of result that decides whether UWBG ever leaves the lab. Also underrated relative to power switching is the non-power use of these materials, where UWBG detectors do something silicon cannot do at all, such as staying linear above 40 W/cm2 and to 300 °C. Those niches are small but defensible and reachable sooner.

## Prediction

By 31 December 2028, published lateral UWBG AlGaN transistor results will exceed a 3 GW/cm2 power-switching figure of merit, while no Ga2O3 or AlGaN power transistor will have entered qualified volume production for automotive or grid applications.

## Evidence base

- 3 June 2026: UWBG AlGaN polarisation-graded FETs with regrown epitaxial AlN gate interlayers reached average breakdown fields above 6.94 MV/cm, on-current above 1 A/mm, and a power-switching figure of merit above 1.87 GW/cm2 at breakdown voltage above 1.45 kV.
- 14 August 2026: first vertical Ga2O3 transistor architecture without planarisation etch-back or mid-gap acceptor regions, using 200 nm fins and ~1.2 um trenches, showing enhancement-mode operation with 2 V threshold and on/off ratio above 1e7.
- 8 May 2026: interfacial thermal boundary conductance is identified as a major heat-removal bottleneck for Ga2O3/SiC ultra-wide-bandgap power electronics, with direct experimental access to intrinsic interfacial transport still limited.
- 15 June 2026: sub-bandgap AlN Schottky photodetectors gave non-saturating linear response to blue light above 40 W/cm2 and undistorted response at up to at least 300 °C, targeting industrial process control, thermal and nuclear power, aeronautics and spaceflight.
- 4 August 2026: NSF awarded $450,000 to Texas Tech with Los Alamos to replace approximate, trial-and-error radiation-damage models for AlGaN/GaN HEMTs, noting that current practice forces costly per-mission testing.
- July 2026: an analysis of ~1,550 semiconductor startups names wide-bandgap materials among the 'More than Moore' domains where positions are still forming and identifies funding velocity and exits as Europe's binding gaps.

## Open questions

- Can interfacial thermal boundary conductance in heterointegrated stacks such as Ga2O3 on SiC be raised enough, and verified experimentally rather than by simulation, to let UWBG devices run at the current densities their breakdown fields imply?
- Do the record UWBG device results survive translation from epitaxial regrowth and electron-beam lithography to production-compatible processes and larger areas?
- Is controllable doping, including any usable p-type route, achievable in AlN, Ga2O3 and diamond, given that even Fermi-level determination in diamond currently requires indirect photoluminescence analysis?
- Will physics-based radiation and reliability models arrive fast enough to replace per-mission empirical qualification, which is currently the cost barrier for space and defence adoption?

---
*Assessment drafted 2026-08-31 from up to 13 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
