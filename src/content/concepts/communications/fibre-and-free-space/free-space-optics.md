---
type: concept
slug: free-space-optics
canonical_name: Free-Space Optics
aliases: []
kind: technology
parent_concepts:
- communications
- fibre-and-free-space
related_concepts: []
sources:
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-06-16-trapped-ion-landscape-2026]]'
frontier:
- What link distance, availability and bit error rate do the demonstrated >100 Gb/s hybrid FSO/D-band transmitters achieve over a real outdoor path, as opposed to a bench with controlled misalignment?
- In the hybrid architecture, how much capacity does the millimetre-wave path retain when the optical path drops out, and does that hand-off meet carrier availability requirements?
- What pointing accuracy and station-keeping precision does a close-formation compute constellation actually require, and does the ML-based constellation control approach hold at 81 satellites and beyond?
- Can FSO terminals reach the required capacity without coherent detection, given its 3-4x power and 3-5x cost penalty, or does high-capacity FSO inherit that penalty permanently?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 21
last_reorg_date: '2026-05-14'
scorecard:
  viability: 3
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Later (5-10yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 1
sources_30d: 3
recent_mentions:
- slug: 2026-06-16-trapped-ion-landscape-2026
  title: Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)
  date: '2026-06-16'
  kind: web
- slug: 2026-02-02-photonic-engines-for-data-centers
  title: Photonic "Engines" for Data Centers
  date: '2026-02-02'
  kind: substack
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
neighbors: []
---
**Free-space optics sends data as modulated light through air or vacuum instead of fibre, and the current evidence base is laboratory-scale: >100 Gb/s hybrid optical/millimetre-wave transmitters, machine-learning receivers to fight bandwidth limits, and design studies that make inter-satellite laser links the backbone of proposed orbital AI compute clusters.**

## Summary

Free-space optics (FSO) is optical communication without a waveguide. A laser is modulated with data, the beam crosses air or vacuum, and a receiver aperture collects it. The physics is the same as fibre transmission, so the same modulation formats, coherent detection tricks and DSP apply; what changes is the channel. Instead of a controlled glass core you have a path with atmospheric loss, turbulence, and, above all, a pointing problem: the transmitter and receiver must stay aligned to within a fraction of the beam divergence. The recent literature treats misalignment as the first-order design variable, studying combined link capacity as a function of beam angle misalignment in a hybrid FSO plus D-band (110-170 GHz) millimetre-wave transmitter driven by a single phase-locked laser pair, at >100 Gb/s signalling.

Two distinct engineering programmes sit under the same phrase, and they pull in opposite directions. The first is FSO as a link technology: laser beams as an alternative to fibre or radio. The second is "free-space optics" as the traditional bulk-optical bench, and here the whole thrust of current work is to eliminate it. On-chip high-speed imaging is presented explicitly as a replacement for approaches that "rely on bulky free-space optics, long dispersive elements, and are prone to alignment instabilities", and dynamic control of orbital angular momentum is described as still dependent on "bulky free-space optics or cascaded architectures", motivating an ultrathin 46 nm van der Waals alternative. Related work miniaturises multi-plane light converters into a fused silica chip by 3D direct laser writing. The lesson transfers: alignment stability is the recurring failure mode of anything that propagates light through free space, and it is what determines whether FSO links are operationally practical rather than merely demonstrable.

The parameters that decide FSO are therefore: available link margin (transmit power, aperture, range, atmospheric or vacuum loss), pointing and tracking accuracy relative to beam divergence, the electrical bandwidth of the transceiver front end, and cost per bit against the incumbent. On bandwidth, a neural-network-assisted deformable matched filter has been shown experimentally, in a hardware-in-the-loop carrier-less amplitude and phase system, to outperform conventional fixed matched filtering under severe bandwidth constraints without decision feedback. On cost, the wider optical interconnect economics are unfavourable to the most capable formats: coherent systems need DSPs consuming 3-4x more power and costing 3-5x more than intensity-modulated ones <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. The largest single demand pull in these sources is orbital: a proposed space-based AI compute system uses fleets of satellites with solar arrays, Google TPUs and inter-satellite links using free-space optics, flown in close proximity to obtain high bandwidth and low latency, illustrated with an 81-satellite cluster of 1 km radius.

## Viability (3/5)

The core function is demonstrated. A hybrid FSO and D-band transmitter has been built and run at >100 Gb/s signalling from a single phase-locked laser pair, deliberately characterised against beam angle misalignment. Receiver-side impairment compensation is also past simulation: the deformable matched filter result is from a hardware-in-the-loop transmission system, trained end-to-end on an error vector magnitude loss, and beats fixed matched filtering under severe bandwidth limitation.

What the sources do not contain is anything that would let you size an operational link: no link distances, no atmospheric attenuation or turbulence figures, no availability statistics, no bit error rate versus weather. The one system-level use case, orbital inter-satellite links, is a design study whose hardware evidence concerns the compute payload rather than the optics: Trillium TPUs survived a total ionising dose equivalent to a five-year mission without permanent failures. A 3 reflects credible physics with demonstrated transmitters and no demonstrated deployed link inside this evidence base.

**TLDR: Working laboratory links at >100 Gb/s and experimentally validated receiver compensation, but no range, availability or field data in the sources.**

## Drivers (3/5)

Demand: the explicit argument is that AI is a foundational general-purpose technology, so demand for compute and energy keeps growing, and the Sun is the largest energy source in the solar system, which makes orbital compute worth designing for; in that architecture inter-satellite free-space optical links are not optional, they are how the cluster becomes a machine rather than a set of isolated satellites. Terrestrially, the pressure is the same one driving optical interconnect generally: copper's reach shrinks as bandwidth rises, so links that once crossed the data centre floor now do not leave the rack <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. That pull mostly favours fibre; FSO inherits it only where fibre is impossible or too slow to install.

Supply: the enabling components appear in the sources as active research rather than commodity. Phase-locked laser pairs that deliver both low RF phase noise and narrow optical linewidth from one source are the enabling trick in the hybrid transmitter. Mode-shaping hardware relevant to spatial multiplexing is being miniaturised into glass chips at proof-of-concept stage in the visible. Against this, the highest-capacity format, coherent detection, carries a 3-4x power and 3-5x cost penalty in its DSP <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>, which constrains how cheaply high-capacity FSO terminals can be built.

**TLDR: Demand is real but concentrated in AI compute scaling and places fibre cannot reach; supply-side component maturity is only indirectly evidenced.**

## Novelty (3/5)

The interesting comparator in these sources is not fibre but radio. The hybrid transmitter's contribution is that one phase-locked laser pair simultaneously serves the optical path and generates a D-band (110-170 GHz) millimetre-wave carrier, giving low RF phase noise and narrow optical linewidth from shared hardware, with combined capacity studied under misalignment at >100 Gb/s. That is a real architectural advance: it turns FSO's misalignment fragility into a graceful-degradation problem by pairing it with a wider-beam RF path, and it removes duplicated frequency-reference hardware. The receiver-side novelty is similar in spirit: rather than replacing the analytically derived matched filter, a network learns a residual deformation of it from 16 physically motivated time, frequency and memory features.

The honest limit is that no source quantifies FSO against a like-for-like fibre or RF baseline in capacity per pound, availability or range. And the same body of work supplies the counter-case: across imaging, beam shaping and nonlinear optics, free-space propagation is the thing being engineered out because it is bulky and alignment-unstable. FSO is therefore novel as a link where guided optics is unavailable, not as a general improvement on guided optics.

**TLDR: Genuinely better than millimetre-wave alone on capacity and better than fibre where fibre cannot be laid, but the sources never quantify the margin.**

## Diffusion (2/5)

The adoption barrier is stated repeatedly and from two directions. Directly, the hybrid transmitter study treats beam angle misalignment as the variable that determines usable capacity. Indirectly, the wider photonics literature is migrating away from free-space benches precisely because they are prone to alignment instabilities, and prizes monolithic integration for being compact and robust. A technology whose central operational risk is the thing everyone else is designing out will diffuse only where there is no alternative.

The orbital case is the clearest such niche, and it is also the hardest: high-bandwidth low-latency inter-satellite links are obtained by flying satellites in close proximity, with formation flight illustrated for an 81-satellite cluster of 1 km radius and controlled by high-precision ML-based constellation models. That converts a communications problem into a station-keeping and control problem, adding failure modes rather than removing them. On cost, high-capacity coherent terminals carry the 3-4x power and 3-5x cost penalty of their DSPs <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>, which works against volume deployment. Nothing in the sources describes a fielded FSO network, a standard, or a terminal vendor, so 2 is as high as the evidence supports.

**TLDR: Alignment and pointing dominate, and the sources show no operational deployments, standards or volume terminal supply chain.**

## Impact (3/5)

If the orbital compute thesis holds, FSO is load-bearing rather than incremental: the value of a satellite fleet as an AI system depends entirely on whether the inter-satellite links deliver the bandwidth and latency that make many satellites behave as one cluster, and free-space optics is the only mechanism proposed for that. The framing behind that design study, that AI compute and energy demand keep growing and the Sun is the largest available energy source, is what makes the payoff large if it works.

Terrestrially the value is narrower. The general problem, copper running out of reach as bandwidth rises, is being solved by fibre and optical engines inside data centres <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>, and FSO is left with links where trenching is impossible or too slow. The hybrid FSO plus D-band architecture points at high-capacity fixed wireless and backhaul at >100 Gb/s class rates, which is valuable but bounded. The sources give no market sizing, so this score reflects breadth of technical consequence, not measured economic value.

**TLDR: Modest as a terrestrial fibre substitute; potentially large as the interconnect that makes orbital AI compute coherent, but that scenario is unproven.**

## Timing Later (5-10yr)

Everything in these sources dated 2026 is either a laboratory transmitter, a hardware-in-the-loop receiver experiment, or a system architecture paper. The hybrid FSO/D-band work is a demonstration with misalignment characterisation; the deformable matched filter is a receiver algorithm validated on a bench. Neither implies a product timetable.

The orbital use case sets the outer bound. Its compute payload has cleared a meaningful gate, with Trillium TPUs surviving a five-year-equivalent total ionising dose without permanent failures and being characterised for bit flips, but the constellation itself is presented through an illustrative 81-satellite, 1 km radius formation and an ML control approach for large constellations. Getting from radiation-tested chips and formation-flight modelling to an operating orbital cluster whose value depends on optical inter-satellite links is a multi-year hardware programme. Terrestrial niche links could plausibly land sooner, but the sources do not evidence that, so the honest band is 5-10 years for the impactful version.

**TLDR: Transmitters and receiver algorithms exist now in the lab; the deployments that would make FSO consequential are design studies.**

## Overrated or underrated? Fairly rated

FSO is neither hype nor a sleeper. The physics works, the transmitters exist at >100 Gb/s class rates, and the community is being sensible about the actual constraint by pairing optical with millimetre-wave paths and by studying misalignment head-on rather than assuming perfect pointing. Equally, the same literature that advances FSO is systematically removing free-space propagation from everything it can, because bulk optics is bulky and does not stay aligned. That is the correct prior: FSO wins where a waveguide cannot go, and loses everywhere else.

The position worth taking is that FSO's valuation should be read as a derivative of orbital compute, not of terrestrial telecoms. Inside a data centre, fibre and integrated optical engines are the answer and the economics of coherent DSP already bite hard <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. In orbit there is no fibre, and the entire case for satellite AI clusters rests on inter-satellite optical links working while satellites fly in close formation. If you are underwriting FSO, you are underwriting formation flight, pointing control and terminal cost, not laser modulation.

## Prediction

By 30 June 2028, no publicly documented flight demonstration will exist of an inter-satellite free-space optical network linking a close-formation cluster of the scale illustrated in the space-based AI infrastructure design study (order 81 satellites within a 1 km radius).

## Evidence base

- 3 June 2026: a hybrid FSO and D-band (110-170 GHz) millimetre-wave transmitter driven by a single phase-locked laser pair was demonstrated at >100 Gb/s signalling, with combined capacity studied against beam angle misalignment.
- 16 June 2026: a neural-network deformable matched filter, using 16 time, frequency and memory features and trained on an EVM loss, outperformed fixed matched filtering under severe bandwidth limits in a hardware-in-the-loop CAP system without decision feedback.
- 18 June 2026: a space-based AI compute architecture specifies inter-satellite links using free-space optics with satellites flown in close proximity, illustrated by an 81-satellite cluster of 1 km radius; Trillium TPUs survived a five-year-mission-equivalent total ionising dose without permanent failures.
- 29 May 2026: an on-chip high-speed imaging platform was introduced specifically to replace approaches that rely on bulky free-space optics and are prone to alignment instabilities.
- 14 August 2026: dynamic orbital-angular-momentum control was described as still dependent on bulky free-space optics, motivating an all-optical switch in a 46 nm 3R-MoS2 film.
- 2 February 2026: coherent optical systems are reported to require DSPs consuming 3-4x more power and costing 3-5x more than intensity-modulated systems, constraining high-capacity optical terminal economics <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>.

## Open questions

- What link distance, availability and bit error rate do the demonstrated >100 Gb/s hybrid FSO/D-band transmitters achieve over a real outdoor path, as opposed to a bench with controlled misalignment?
- In the hybrid architecture, how much capacity does the millimetre-wave path retain when the optical path drops out, and does that hand-off meet carrier availability requirements?
- What pointing accuracy and station-keeping precision does a close-formation compute constellation actually require, and does the ML-based constellation control approach hold at 81 satellites and beyond?
- Can FSO terminals reach the required capacity without coherent detection, given its 3-4x power and 3-5x cost penalty, or does high-capacity FSO inherit that penalty permanently?

---
*Assessment drafted 2026-08-31 from up to 10 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
