---
type: concept
slug: free-space-photonics
canonical_name: Free-Space Photonics
aliases:
- free-space optics
- free-space photonics
- FSO
parent_concepts:
- communications
- photonics
related_concepts:
- free-space-photonics
- lidar
- avalanche-photodiode
- photonic-imaging
- hgcdte
- co-packaged-optics
- optical-interconnect
- diffractive-deep-neural-network
- spatial-light-modulators
- mid-ir-photonics
sources:
- '[[2026-02-02-photonic-engines-for-data-centers]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-06-16-trapped-ion-landscape-2026]]'
frontier:
- What link availability and bit error rate do hybrid FSO/D-band transmitters achieve over real outdoor paths and across weather, as opposed to the laboratory misalignment sweeps reported at over 100 Gb/s 2026 06 03 hybrid free space optics and millimetre wave d band trans mi?
- Can inter-satellite free-space optical links hold the required pointing under machine-learning-based formation control at the 1 km, 81-satellite scale, and what is the demonstrated link budget rather than the assumed one 2026 06 18 towards a future space based highly scalable ai infrastructu?
- How much of the bandwidth limitation in free-space links can be recovered digitally before the equalisation power budget eats the advantage over intensity-based fibre links, given that coherent DSPs already cost three to five times more and consume three to four times more power 2026 02 02 photonic engines for data centers 2026 06 16 ml enabled deformable matched filters for band limit compens?
- Do integrated mode-shaping elements such as glass-encapsulated MPLCs reach telecom wavelengths, insertion loss and mode-count figures good enough to replace bulk free-space multiplexers, or do they remain visible-wavelength proof-of-concepts 2026 07 07 miniaturised transmissive multi plane light converters via l?
- Can atmospheric-turbulence adaptive-optics correction (AO-FSO) reach the latency and power budget needed for untethered ground-to-ground links above 10 km?
- Will inter-satellite optical links (ISOL) become commodity infrastructure, and does that commoditise the terminal or the steering/pointing sub-system?
- What is the sustainable data-rate ceiling for a diffractive free-space compute link (light through air as a multiply-accumulate layer)?
last_updated: '2026-08-31'
tags:
- concept
descendants:
- diffractive-deep-neural-network
mention_count: 20
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 0
sources_30d: 2
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
neighbors:
- slug: free-space-photonics
  name: Free-Space Photonics
  path: /communications/fibre-and-free-space/free-space-photonics/
  macro: communications
- slug: lidar
  name: LiDAR
  path: /sensing/ranging-detection/lidar/
  macro: sensing
- slug: avalanche-photodiode
  name: Avalanche Photodiode (APD / SPAD)
  path: /photonic-systems/modulators-detectors/avalanche-photodiode/
  macro: photonic-systems
- slug: photonic-imaging
  name: Photonic Imaging
  path: /sensing/imaging/photonic-imaging/
  macro: sensing
- slug: hgcdte
  name: Mercury Cadmium Telluride
  path: /photonic-systems/modulators-detectors/hgcdte/
  macro: photonic-systems
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: optical-interconnect
  name: Optical Interconnect
  path: /communications/optical-interconnect/optical-interconnect/
  macro: communications
- slug: diffractive-deep-neural-network
  name: Diffractive Deep Neural Network
  path: /photonic-systems/photonic-compute/diffractive-deep-neural-network/
  macro: photonic-systems
- slug: spatial-light-modulators
  name: Spatial Light Modulators (SLMs)
  path: /photonic-systems/modulators-detectors/spatial-light-modulators/
  macro: photonic-systems
- slug: mid-ir-photonics
  name: Mid-Infrared Photonics
  path: /photonic-systems/light-sources/mid-ir-photonics/
  macro: photonic-systems
---
**Free-space photonics is the use of light beams through air or vacuum, rather than fibre, as the communications channel, and the bulk-optical hardware that shapes those beams; 2026 work shows it moving in two directions at once, becoming the assumed interconnect for orbital compute clusters while being designed out of instruments wherever a chip can replace an optical bench.**

## Summary

**What it is.** Free-space photonics covers two things that are easy to conflate. The first is the communications channel: modulated light propagating through atmosphere or vacuum between two apertures, competing with fibre (no right-of-way, no trenching) and with millimetre-wave radio (far more bandwidth, far tighter beams). The second is the physical apparatus of free-space optics: lenses, gratings, spatial light modulators and dispersive elements arranged on a bench, used to shape, split and multiplex beams. The link is a growth story. The bench is, in several of the 2026 papers here, explicitly the problem to be removed.

**How the link works.** A laser is modulated, collimated through a telescope, and captured by a receiver aperture that must stay pointed within a small angular tolerance. Everything hard follows from that: pointing and tracking, beam wander, and bandwidth limits in the transmit/receive electro-optics. One 2026 demonstration built a hybrid transmitter that drives both a free-space optical channel and a D-band (110-170 GHz) millimetre-wave channel from a single optically harmonically locked laser pair, giving low RF phase noise and narrow optical linewidth from the same source, and characterised the combined capacity against beam angle misalignment at over 100 Gb/s signalling. A separate strand attacks the receiver side with machine learning: a neural network learns a residual deformation of the analytically derived matched filter for carrier-less amplitude and phase modulation, using 16 time-, frequency- and memory-domain features, and beats fixed matched filtering under severe bandwidth constraints in a hardware-in-the-loop experiment.

**Why it matters now.** The demand pull is data movement. Copper reach shrinks as bandwidth rises, pushing optics from the data centre floor into the rack and onto the board <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. Above that, a space-based AI infrastructure design study proposes fleets of satellites carrying solar arrays and TPU accelerators, connected by inter-satellite free-space optical links, flown in close formation specifically to make those links high-bandwidth and low-latency; it illustrates the approach with an 81-satellite cluster of 1 km radius and reports that Trillium TPUs survived a total ionising dose equivalent to a five-year mission without permanent failures. Trapped-ion roadmaps similarly depend on networking many ion-trap chips over photonic links to get past ten thousand qubits <sup class="ref"><a href="https://thequantuminsider.com/2026/06/12/trapped-ion-quantum-computing-companies-technology-and-where-it-stands-in-2026/" title="Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)" rel="noopener">ref</a></sup>.

**The parameters that decide it.** Link budget and pointing tolerance (the misalignment sensitivity measured in the hybrid D-band work), available modulation bandwidth and how much of it can be recovered by digital or learned equalisation, and the size, weight, power and alignment stability of the optics. The last of these is where integration bites: high-speed flow imaging is being rebuilt entirely on-chip precisely because the free-space version relies on bulky optics, long dispersive elements and is prone to alignment instabilities, and orbital angular momentum switching is being pushed into a 46 nm van der Waals film for the same reason.

## Viability (3/5)

The channel physics is demonstrated, not speculative. A single phase-locked laser pair has been shown to feed both an FSO and a D-band millimetre-wave transmitter with over 100 Gb/s signalling, with combined capacity characterised against beam angle misalignment. Receiver-side band-limit compensation has been validated in a hardware-in-the-loop transmission system rather than in simulation only. Both are single-paper, laboratory-scale results; neither reports field range, availability under weather, or long-duration link stability.

The honest counterweight comes from inside the same literature. Two independent 2026 papers describe free-space optical assemblies as bulky and alignment-unstable and present integrated alternatives to remove them. That is a viability judgement about the hardware form factor, not the channel, but it constrains where free-space photonics is the right answer: between apertures that cannot be joined by fibre, and rarely inside a box. A 3 reflects credible, repeatedly demonstrated components with no deployment-grade evidence in the sources.

**TLDR: Links work in the laboratory at over 100 Gb/s; alignment and bandwidth limits are being managed rather than solved.**

## Drivers (4/5)

**Supply.** Enablers are real but early. Optically harmonically locked laser pairs give one source serving both optical and millimetre-wave chains, reducing component count. Multi-plane light converters, the deterministic mode-mapping element behind spatial multiplexing, have been miniaturised into a fused silica chip by single-step 3D direct laser writing, though only as proof-of-concept devices operating in the visible. Learned equalisation lets designers trade optical bandwidth for digital signal processing. The sources do not give supply-chain volumes, costs or capacity, so the supply half of this score rests on capability trajectory rather than industrial evidence.

**TLDR: Demand is strong and specific (AI data movement, orbital compute, quantum networking); supply-side enablers are advancing but at proof-of-concept scale.**

## Novelty (3/5)

Against fibre, the advantage is structural rather than measured: no medium to install between the endpoints, which is the only reason the orbital case exists at all. Against millimetre-wave radio, the 2026 hybrid transmitter does not choose; it runs both from one locked laser pair and studies their combined capacity under misalignment, which is the more interesting claim because it implies FSO and D-band are complements with different failure modes. On the component side, the novelty claims are sharper: the first fully integrated on-chip system for spatio-temporal-encoded high-speed imaging, replacing free-space optics and long dispersive elements; MPLCs fully encapsulated in a glass chip via laser-written geometric phase holograms; monolithic sub-optical-cycle switching between vortex beams of opposite topological charge in a 46 nm film, where the incumbent is bulky free-space optics or cascaded architectures.

The missing quantity is the margin. Only the deformable matched filter work states a comparative result, and it is qualitative in the excerpt: significant improvement over fixed matched filtering under severe bandwidth constraints, without decision feedback or added receive complexity. A 3 is what the evidence earns: several credible firsts, no defensible multiple over the alternative.

**TLDR: Genuine architectural firsts, but the sources almost never quantify how much better than the incumbent.**

## Diffusion (2/5)

Every source here is a laboratory demonstration, a design study or a proof-of-concept device. Beam angle misalignment is treated as a first-order design variable rather than a solved engineering detail, and alignment instability is cited as a reason to abandon free-space configurations where an alternative exists. The orbital case adds a further dependency chain: high-precision machine-learning-based control of large constellations flown in close proximity, illustrated but not flown, on top of an 81-satellite cluster geometry.

The data-centre adoption path is also indirect. The cost pressure described there is on optical interconnect generally, with coherent systems penalised by digital signal processors consuming three to four times more power and costing three to five times more than intensity-based systems <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>. That pressure favours whichever optical link is cheapest per bit, which inside a building is fibre. Free-space photonics diffuses where fibre cannot go, which is a narrower set of deployments than the enthusiasm around photonics generally implies. The sources contain no market size, unit shipment or customer evidence, so this score reflects technical readiness and named barriers only.

**TLDR: No deployment evidence in the sources; pointing, misalignment and system integration remain the named obstacles.**

## Impact (4/5)

The qualification is that impact here is contingent on architectures that have not been built. Terrestrial FSO impact is more modest and not quantified anywhere in these sources. Mode multiplexing via MPLCs is described as having many future applications across optical communications, photonic computing and advanced imaging, which is breadth without magnitude. A 4 rests on the size of the dependent systems, not on demonstrated value delivered.

**TLDR: If orbital compute or multi-chip quantum networking depends on these links, the value at stake is very large; the dependency is asserted in the sources, not proven.**

## Timing Soon (2-5yr)

The link and receiver work is at the stage where laboratory results at over 100 Gb/s and hardware-in-the-loop equalisation exist and the remaining questions are engineering ones: pointing stability, weather availability, cost per aperture. Component integration is on a similar horizon, with MPLCs in glass and on-chip spatio-temporal encoding both at proof-of-concept in 2026.

The headline application is much further out. The orbital compute proposal is a system design paper that illustrates formation flight in simulation and reports radiation testing of the accelerators; it does not describe a flown cluster. Nothing in the sources dates a launch, a constellation or a commercial FSO product, so the band applies to the technology's readiness rather than to its deployment, and should be read as such.

**TLDR: Component and hybrid-link maturity is a 2-5 year story; orbital compute clusters that depend on these links are a decade-plus story.**

## Overrated or underrated? Underrated

The interesting fact in this evidence base is that free-space photonics is being deleted and promoted simultaneously, and the two movements are consistent. Inside instruments, free-space optical benches are a liability and are being replaced by waveguides, glass-encapsulated holograms and van der Waals films because of bulk and alignment drift. Between apertures that cannot be joined by fibre, the free-space link is quietly becoming a load-bearing assumption in two of the most ambitious hardware programmes in circulation: orbital AI infrastructure and networked ion-trap quantum computers <sup class="ref"><a href="https://thequantuminsider.com/2026/06/12/trapped-ion-quantum-computing-companies-technology-and-where-it-stands-in-2026/" title="Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)" rel="noopener">ref</a></sup>.

The call is Underrated because attention in both programmes sits on the compute element, the radiation-tested TPU and the qubit count, while the interconnect is treated as available. It is not yet demonstrated at the scale, duration or reliability those architectures require, and the sources show misalignment sensitivity being actively characterised rather than closed out. That combination, critical-path dependency plus unresolved engineering, is where mispricing usually sits. The caveat is the thinness of this evidence base: a handful of 2026 preprints, no field deployments, no cost data. Anyone acting on this should treat the assessment as directional.

## Prediction

By 31 December 2029, no orbital compute cluster of the scale illustrated in the Google design study (order 80 satellites, kilometre-radius formation, TPU payloads linked by inter-satellite free-space optics) will be operating in orbit.

## Evidence base

- 3 June 2026: hybrid FSO and D-band (110-170 GHz) transmitter driven by a single optically harmonically locked laser pair, with combined capacity studied against beam angle misalignment using over 100 Gb/s signalling.
- 18 June 2026: space-based AI infrastructure design study proposing satellite fleets with solar arrays, TPU accelerators and inter-satellite free-space optical links, illustrated with an 81-satellite, 1 km radius cluster; Trillium TPUs survived a five-year-mission-equivalent total ionising dose without permanent failures.
- 16 June 2026: neural-network deformable matched filtering for CAP modulation, using 16 time, frequency and memory features, significantly outperformed fixed matched filtering under severe bandwidth constraints in a hardware-in-the-loop free-space optical system without decision feedback.
- 29 May 2026: first fully integrated on-chip spatio-temporal-encoding imaging platform, motivated explicitly by the bulk, long dispersive elements and alignment instability of free-space optics.
- 7 July 2026: multi-plane light converters fully encapsulated in a fused silica chip by single-step 3D direct laser writing of birefringent nanogratings, tested as proof-of-concept devices in the visible.
- 14 August 2026: monolithic all-optical switching between vortex second-harmonic beams of opposite topological charge in a 46 nm 3R-MoS2 film, presented as an alternative to bulky free-space optics for dynamic orbital angular momentum control.
- 16 June 2026: trapped-ion roadmap places photonic links between ion-trap chips on the path from 256 qubits at 99.99% to over 10,000 qubits <sup class="ref"><a href="https://thequantuminsider.com/2026/06/12/trapped-ion-quantum-computing-companies-technology-and-where-it-stands-in-2026/" title="Trapped-ion quantum computing landscape 2026 (vendors, scale, integrated photonics)" rel="noopener">ref</a></sup>.

## Open questions

- What link availability and bit error rate do hybrid FSO/D-band transmitters achieve over real outdoor paths and across weather, as opposed to the laboratory misalignment sweeps reported at over 100 Gb/s?
- Can inter-satellite free-space optical links hold the required pointing under machine-learning-based formation control at the 1 km, 81-satellite scale, and what is the demonstrated link budget rather than the assumed one?
- How much of the bandwidth limitation in free-space links can be recovered digitally before the equalisation power budget eats the advantage over intensity-based fibre links, given that coherent DSPs already cost three to five times more and consume three to four times more power <sup class="ref"><a href="https://stateofthefuture.substack.com/p/photonic-engines-for-data-centers" title="Photonic 'Engines' for Data Centers" rel="noopener">ref</a></sup>?
- Do integrated mode-shaping elements such as glass-encapsulated MPLCs reach telecom wavelengths, insertion loss and mode-count figures good enough to replace bulk free-space multiplexers, or do they remain visible-wavelength proof-of-concepts?

---
*Assessment drafted 2026-08-31 from up to 10 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
