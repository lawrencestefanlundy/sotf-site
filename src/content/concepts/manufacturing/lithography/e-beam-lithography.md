---
type: concept
slug: e-beam-lithography
canonical_name: E-Beam Lithography
aliases:
- e-beam lithography
- electron-beam lithography
- EBL
- EBL
kind: technology
parent_concepts:
- manufacturing
- lithography
related_concepts:
- maskless-lithography
- directed-self-assembly
- nanoimprint-lithography
- high-na-euv-lithography
- photoresists
sources: []
frontier:
- How much of the beam placement error that capped split-cavity Q at around 20,000 is fixable by better tooling versus intrinsic to serial writing 2026 08 04 a high q split cavity enabling independent electrical tuning?
- Can electrochemical AFM direct write scale beyond single sub-10 nm graphene devices to multi-layer, registered process flows, or does it remain a single-layer alternative 2026 05 14 direct write electrochemical nanofabrication of ultrasmall g?
- For which photonic geometries does chemo-mechanical etching or photolithography match EBL performance, given that Ta2O5 microrings reached intrinsic Q above 4e6 without it 2026 06 07 monolithic tantalum pentoxide microrings with intrinsic q fa?
- Do inverse-lithography and DRC-compliant design flows reduce the number of EBL fabrication iterations enough to change the cost calculus for photonics groups 2026 06 03 prism photonics informed inverse lithography for manufactura?
- Can multi-beam e-beam (IMS Nanofabrication, Multibeam Corporation) close the throughput gap to optical tools at 300 mm wafer scale by 2030?
- Does direct-write e-beam at single-wafer rates (ARM-on-photolithography research threads) reach a commercial pilot by 2030, or does High-NA EUV foreclose the market?
- What is the practical resolution floor for e-beam in production resists — does resist blur or forward/back-scatter dominate at sub-5 nm?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 8
descendants: []
last_reorg_date: '2026-05-13'
scorecard:
  viability: 5
  drivers: 3
  novelty: 2
  diffusion: 3
  impact: 3
  timing_band: Now (0-2yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2024-10-29-deploy-intelligence-too-cheap-to
  title: Deploy! Intelligence too cheap to meter @ $0.0001 per million tokens.
  date: '2024-10-29'
  kind: substack
- slug: 2023-07-27-e10-pushing-moores-law-to-the-limit
  title: '🔮E10: Pushing Moore''s Law to the Limit with High-NA EUV (aka Nanoscale Chip Printing)'
  date: '2023-07-27'
  kind: substack
- slug: 2023-05-31-three-underrated-technologies-from
  title: '💡E02: Three Underrated Technologies from the Future: Brain Recording; Deep Geothermal; IVF + Updates BCI; Clean Meat; LEO Internet++'
  date: '2023-05-31'
  kind: substack
neighbors:
- slug: maskless-lithography
  name: Maskless Lithography
  path: /manufacturing/lithography/maskless-lithography/
  macro: manufacturing
- slug: directed-self-assembly
  name: Directed Self-Assembly
  path: /manufacturing/lithography/directed-self-assembly/
  macro: manufacturing
- slug: nanoimprint-lithography
  name: Nanoimprint Lithography
  path: /manufacturing/lithography/nanoimprint-lithography/
  macro: manufacturing
- slug: high-na-euv-lithography
  name: High-NA EUV Lithography
  path: /manufacturing/lithography/high-na-euv-lithography/
  macro: manufacturing
- slug: photoresists
  name: Photoresists (incl. EUV resists)
  path: /manufacturing/lithography/photoresists/
  macro: manufacturing
---
**E-beam lithography writes nanoscale patterns directly with a focused electron beam instead of projecting light through a mask, and it remains the default way research groups fabricate sub-200 nm photonic, quantum and wide-bandgap prototype devices, while being too slow and costly to be a volume production route.**

## Summary

Electron-beam lithography (EBL) patterns a resist-coated wafer by scanning a focused electron beam across it point by point. Because the de Broglie wavelength of accelerated electrons is far below optical wavelengths, resolution is not set by diffraction in the way it is for projection optics, and no mask is required: the pattern is written directly from the layout file. That makes EBL a maskless, per-design tool rather than a per-wafer tool, which is exactly why it dominates prototyping and is largely absent from high-volume manufacturing, where the economics favour projecting one mask onto many wafers. The mainstream production counterpart is deep-ultraviolet and extreme-ultraviolet projection, where a 13.5 nm source and numerical apertures of 0.55 and above are used to keep shrinking logic features <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e10-pushing-moores-law-to-the-limit" title="🔮E10: Pushing Moore's Law to the Limit with High-NA EUV (aka Nanoscale Chip Printing)" rel="noopener">ref</a></sup>.

The parameters that decide EBL are resolution, beam placement accuracy, throughput and cost. Resolution is rarely the binding constraint in the 2026 literature; placement is. A GaAs photonic-crystal split cavity reported in August 2026 achieved average quality factors of 20,000 or more, enough for the strong-coupling regime, and the authors state explicitly that Q was limited primarily by the precision and accuracy of the e-beam lithography tool rather than by sidewall scattering. That is a useful marker: for high-Q nanophotonics, the writing tool itself is now the error budget.

What EBL buys is arbitrary geometry at nanometre scale without a mask set. Recent uses span deterministic ion placement for optical data storage, where EBL plus ion implantation gave controlled ion number and spatial distribution with multi-bit grayscale encoding across millimetre-scale areas; scaled 200 nm multi-fin channels in a vertical gallium oxide transistor with a threshold voltage of 2 V and on-off ratio above 1e7; and silicon photonic inverse design flows that treat EBL and photolithography as two distinct fabrication platforms with different design rules across the 1,500 to 1,600 nm band.

What EBL costs is money and time, and this is visible in the same literature as a push to avoid it. A graphene nanoribbon FET paper argues that high fabrication cost and complex processing hinder integration of GNR devices, and offers electrochemical AFM lithography with AC bias as a relatively low-cost direct-write route to sub-10 nm features explicitly positioned against photo- and e-beam lithography. A tantalum pentoxide microring paper reports loaded Q of 2.74e6 in the telecom band and intrinsic Q above 4e6 using photolithography-assisted chemo-mechanical etching, and states the result was obtained without employing expensive electron-beam lithography. EBL is therefore both the incumbent benchmark and the thing new nanofabrication methods advertise themselves against.

## Viability (5/5)

There is no open question about whether EBL works. In the supplied sources alone it produced a strong-coupling-capable photonic crystal cavity with average Q of 20,000 or more, 200 nm multi-fin channels in an enhancement-mode vertical gallium oxide transistor with on-off ratio above 1e7, and millimetre-scale deterministic ion patterning for multiplexed optical storage. These are independent groups, different material systems, same tool.

The honest qualifier is that EBL's own limits are now the limiting factor in the most demanding applications. Beam placement precision, not etch quality, capped cavity Q in the split-cavity work, and cost and process complexity are cited as reasons to look elsewhere for nanoribbon devices. Viability as a research and prototyping tool is settled; viability as a volume patterning route is not something these sources support, and the tier-7 commentary treats High-NA EUV, not EBL, as the production path for leading-edge chips <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e10-pushing-moores-law-to-the-limit" title="🔮E10: Pushing Moore's Law to the Limit with High-NA EUV (aka Nanoscale Chip Printing)" rel="noopener">ref</a></sup>.

**TLDR: Mature and working: multiple independent 2026 groups built functioning devices with it.**

## Drivers (3/5)

On the demand side, the pull is diffuse but consistent. Within a four-month window in 2026, EBL appears as the enabling patterning step in quantum photonics, gallium oxide power devices where the authors argue the architecture suits high-throughput prototyping and large-scale manufacturing, and high-density optical storage. Design-automation work reinforces this by codifying EBL as one of two named fabrication platforms with its own design rules for silicon photonic inverse design. Public funding continues to flow to programmes in the adjacent nanofabricated-device space, for example two NSF awards of $400,001 and $301,350 in June 2026 for terahertz reconfigurable reflectarrays.

On the supply side the sources say almost nothing directly: no tool vendors, no installed base, no throughput or cost figures. What they do reveal is a counter-driver, namely active substitution pressure. Two separate 2026 groups justify their method partly by avoiding EBL, one on cost and process complexity grounds, the other by reaching intrinsic Q above 4e6 without it. Demand for the capability is robust; demand for EBL specifically is contested at the margins.

**TLDR: Broad, steady research demand across photonics, quantum and wide-bandgap devices; no evidence of a volume-manufacturing pull.**

## Novelty (2/5)

EBL's advantage over optical projection is maskless arbitrary geometry at nanometre scale, which is why inverse-design flows generate separate device variants for EBL and photolithography platforms rather than treating them as interchangeable. That advantage is real but decades old, and in these sources EBL is consistently the reference point rather than the innovation. The graphene work frames photo- and e-beam lithography as the conventional techniques it seeks to improve on, claiming sub-10 nm graphene features by electrochemical AFM lithography without electrodes.

The comparative margins in the sources are mixed. For high-Q passive resonators, an alternative route beat EBL on cost while reaching loaded Q of 2.74e6 and intrinsic Q above 4e6 in a hard, brittle material, which suggests EBL is not uniquely necessary where geometry is simple and periodic. Where geometry must be arbitrary and registered to prior layers, such as electrically isolated split cavities or deterministic ion placement with wavelength-multiplexed readout, no alternative appears in these sources. The novelty score reflects the technology, not its usefulness.

**TLDR: Not novel: EBL is the incumbent benchmark that newer nanofabrication methods measure themselves against.**

## Diffusion (3/5)

Diffusion within its natural niche looks close to complete. EBL appears across unrelated groups and material systems as an assumed capability, and is now baked into design tooling as a named platform with its own design-rule set. That is what mature diffusion looks like: the tool is invisible infrastructure.

The barriers are to expansion, not to entry. Cost and process complexity are cited as blocking wider integration of EBL-defined devices into conventional transistor technology, and at least one group demonstrates that avoiding EBL is a selling point. Volume leading-edge patterning is described in these sources as the domain of EUV with numerical apertures of 0.55 and above <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e10-pushing-moores-law-to-the-limit" title="🔮E10: Pushing Moore's Law to the Limit with High-NA EUV (aka Nanoscale Chip Printing)" rel="noopener">ref</a></sup>. A second, subtler barrier is the prototype-to-foundry gap: photonics lacks a systematic mask optimisation flow, and fabrication deviations cause large optical response drift and compounding error in cascaded circuits, with model calibration requiring repeated fabrication cycles. Designs proven on an EBL platform do not transfer automatically to an optical one.

**TLDR: Already saturated in research and prototyping; structurally blocked from volume patterning by cost and serial writing.**

## Impact (3/5)

The impact evident in the sources is enablement of things that could not otherwise be built at all: an electrically split photonic crystal cavity that preserves independent tuning of two quantum dots while keeping Q at 20,000 or more, opening a path to strong-coupling-mediated interactions between two InAs quantum dots; deterministic control of ion number and position enabling multi-bit grayscale plus wavelength division multiplexed optical storage over millimetre areas; and a vertical gallium oxide transistor architecture that removes planarization etch-back and mid-gap acceptor steps. In each case EBL is the reason the experiment exists.

The ceiling is that value capture stays in the R&D layer. None of the supplied sources attribute production volume, revenue or market size to EBL, and the one source that quantifies lithography-linked economic value assigns roughly $200 billion of annual chip manufacturing to High-NA EUV rather than to direct-write methods <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e10-pushing-moores-law-to-the-limit" title="🔮E10: Pushing Moore's Law to the Limit with High-NA EUV (aka Nanoscale Chip Printing)" rel="noopener">ref</a></sup>. EBL's downstream impact is therefore mediated: it matters as much as the devices it de-risks, and the sources here show promising but pre-commercial devices.

**TLDR: High leverage per device as a prototyping enabler, but the sources do not support a claim of large-scale economic impact.**

## Timing Now (0-2yr)

EBL is a present-tense technology. Devices fabricated with it were reported repeatedly through 2026, from May to August, across photonics, storage and power electronics. Anyone deciding whether to build a nanoscale prototype today is already choosing between EBL and specific alternatives.

The timing question that remains open is when the substitution pressure bites. The competing methods in these sources are single-group demonstrations, one at sub-10 nm graphene features by AC-bias electrochemical AFM lithography and one at telecom-band microring Q of 2.74e6 by chemo-mechanical etching. Neither yet shows the layer-to-layer registration and arbitrary-geometry generality that EBL provides, so displacement on a two-year horizon is not supported by the evidence.

**TLDR: In routine use today; the near-term question is whether tool placement accuracy and cost improve, not whether the technique arrives.**

## Overrated or underrated? Fairly rated

EBL is understood correctly by the people who use it: the highest-flexibility, highest-resolution patterning tool available for one-off structures, priced and throughput-limited such that it never threatens volume manufacturing. The 2026 literature bears this out on both sides. It is the tool that made a strong-coupling-capable split cavity possible, and it is also the tool whose placement accuracy set the ceiling on that cavity's Q. It is the tool that enabled deterministic ion encoding for chip-scale optical storage, and the tool that two other groups went out of their way to avoid on cost and process-complexity grounds.

For investors the practical reading is that EBL is not itself the opportunity; it is the cost line in every nanophotonics, quantum photonics and wide-bandgap prototyping budget. The two adjacent opportunities the sources point to are cheaper direct-write substitutes for specific geometries, and the software layer that reduces how many EBL iterations a design needs, given that photonics currently lacks a systematic mask optimisation flow and calibration requires repeated fabrication cycles. Betting on EBL as a growth technology in its own right is not supported here.

## Prediction

By December 2028, e-beam lithography will still be the reported patterning method in the majority of newly published sub-200 nm photonic-crystal, quantum-dot-cavity and wide-bandgap prototype devices, and no leading-edge logic node will use it for critical-layer patterning in volume production.

## Evidence base

- 4 Aug 2026: GaAs photonic crystal split cavity reached average Q of 20,000 or more, with Q limited primarily by the precision and accuracy of the e-beam lithography tool rather than sidewall scattering.
- 14 Aug 2026: vertical gallium oxide ISEFET used EBL to define 200 nm multi-fin channels etched to ~1.2 um trench depth, giving enhancement-mode operation at 2 V threshold and on-off ratio above 1e7.
- 29 May 2026: EBL combined with ion implantation gave deterministic control of ion number and spatial distribution for multi-bit grayscale and wavelength division multiplexed optical storage over millimetre areas.
- 14 May 2026: graphene nanoribbon FET work cites high fabrication cost and complex processing of conventional photo- and e-beam lithography, offering AC-bias electrochemical AFM lithography for sub-10 nm features instead.
- 7 Jun 2026: monolithic Ta2O5 microrings reached loaded Q of 2.74e6 in the telecom band and intrinsic Q above 4e6 without employing expensive electron-beam lithography.
- 7 Jun 2026: DRC-compliant inverse design treated electron-beam lithography and photolithography as separate fabrication platforms for splitters, duplexers and mode converters across 1,500 to 1,600 nm, with over 5-fold lower computational cost than prior methods.
- 27 Jul 2023: mainstream leading-edge patterning is framed around 13.5 nm EUV light and numerical apertures of 0.55 and above, not direct-write methods <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e10-pushing-moores-law-to-the-limit" title="🔮E10: Pushing Moore's Law to the Limit with High-NA EUV (aka Nanoscale Chip Printing)" rel="noopener">ref</a></sup>.

## Open questions

- How much of the beam placement error that capped split-cavity Q at around 20,000 is fixable by better tooling versus intrinsic to serial writing?
- Can electrochemical AFM direct write scale beyond single sub-10 nm graphene devices to multi-layer, registered process flows, or does it remain a single-layer alternative?
- For which photonic geometries does chemo-mechanical etching or photolithography match EBL performance, given that Ta2O5 microrings reached intrinsic Q above 4e6 without it?
- Do inverse-lithography and DRC-compliant design flows reduce the number of EBL fabrication iterations enough to change the cost calculus for photonics groups?

---
*Assessment drafted 2026-08-31 from up to 15 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
