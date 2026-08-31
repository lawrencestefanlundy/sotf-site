---
type: concept
slug: mmwave
canonical_name: mmWave (24-100 GHz)
aliases: []
kind: technology
parent_concepts:
- communications
- wireless
related_concepts: []
sources:
- '[[2023-06-08-three-overrated-technologies-from]]'
- '[[2026-07-27-optimal-compute-vega-investor-briefing]]'
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
- '[[2026-06-01-photonic-mmwave-generation-research]]'
frontier:
- Does the delay-phased array that decouples control and data beams reproduce its near-2x spectral efficiency gain when built at 28 GHz or above, rather than on the 4-7 GHz testbed where it was prototyped 2026 06 02 flexlink decoupling control and data beams for next generati?
- Is Doppler degradation at mmWave under high mobility severe enough in measured channels to justify abandoning OFDM for delay-Doppler or chirp waveforms, or do MIMO, coding and scheduling remedies remain sufficient 2026 05 04 arxiv the resurrection of spectrum spreading for 6g and beyond fro?
- Will privacy regulation permit the spatial sensing that ISAC's value case depends on, given that mmWave and sub-THz deployments can infer behavioural and physiological data about non-consenting bystanders 2026 05 28 isac privacy challenges and solutions for 6g?
- Can the combination of reduced-feedback precoding, closed-form analog precoding, LO-free receivers and learned channel estimation actually bring per-array cost and power down enough for dense deployment, or do the individual savings fail to compose?
last_updated: '2026-08-31'
tags:
- concept
- technology
mention_count: 37
last_reorg_date: '2026-05-13'
scorecard:
  viability: 4
  drivers: 3
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-07-27-optimal-compute-vega-investor-briefing
  title: Optimal Compute / VEGA — Investor Briefing, July 2026 (7-page DocSend)
  date: '2026-07-27'
  kind: web
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
- slug: 2026-06-01-photonic-mmwave-generation-research
  title: Photonic mmWave / microwave signal generation — research landscape (2024–2025)
  date: '2026-06-01'
  kind: web
- slug: 2023-06-08-three-overrated-technologies-from
  title: '💡E03: Three Overrated Technologies from the Future Fusion, Bitcoin & LEO Internet + Ultrasound for Hibernation; Wind Power; Skeletal Editing; Carbon Pricing; & Psychedelics++'
  date: '2023-06-08'
  kind: substack
neighbors: []
---
**mmWave is the 24-100 GHz radio band that buys huge bandwidth at the cost of severe path loss and blockage, forcing every system built on it to be a beamforming system, and the current research frontier is not whether it works but how much overhead the beamforming, channel estimation and hardware cost.**

## Summary

Millimetre-wave denotes carrier frequencies roughly between 24 and 100 GHz (the sources also reach upward into sub-THz work at 111 GHz and 300 GHz). The attraction is arithmetic: bandwidth scales with carrier frequency, so mmWave channels offer the data rates and low latency that 6G and industrial IoT programmes are specified around. The cost is equally arithmetic: free-space path loss rises with frequency, the channel becomes sparse and directional, and any hand, wall or body between transmitter and receiver removes the link. Consequently mmWave is not really a band, it is an architecture. Every practical system uses large antenna arrays with beamforming to recover the lost link budget and to exploit channel sparsity.

That architecture is where all the engineering difficulty sits, and the supplied literature is essentially a catalogue of its overheads. Fully digital arrays need one RF chain per antenna, which is impractical at scale on cost and power grounds, so systems use hybrid analog-digital precoding, which in turn needs iterative optimisation and channel state feedback that both scale badly with array size and subcarrier count. Local oscillators for coherent downconversion are themselves named as a major source of cost, power and complexity in mmWave and sub-THz receivers. As apertures grow, users fall inside the near field and the planar-wave assumption underlying conventional codebooks breaks, requiring distance-aware channel models and codebooks. Under high mobility the time-invariance assumption behind OFDM, the waveform of the 4G and 5G eras, also becomes hard to maintain at mmWave and sub-THz, with Doppler-induced degradation prompting a return to spread-spectrum and chirp-based waveforms.

The parameters that decide mmWave in practice are therefore: beam management latency and overhead; blockage probability and the mitigations available (reconfigurable surfaces, obstacle-bending beams, antenna placement); channel estimation pilot cost; RF chain and LO count per array; and mobility, which sets the Doppler regime. Proposed answers in the sources include radar-assisted narrowing of the candidate beam set for non-terrestrial links, delay-phased arrays that split control and data beams without losing per-beam gain, large reconfigurable surfaces to route around blockages, Airy beams that curve around obstacles, and transparent on-screen antenna arrays to escape the limited aperture and 'death grip' of edge-mounted phone antennas.

A second, quieter use of the same band is sensing. mmWave radar keeps working in fog, smoke, dust and low light, which makes it attractive for size-, weight- and power-constrained robots, drones and wearables. Because comms arrays and radar arrays are the same hardware, integrated sensing and communication (ISAC) is a headline 6G feature, with the side effect that networks may infer location, movement, activity and even breathing or heart-rate-related information about people and bystanders.

## Viability (4/5)

There is real hardware in the sources, not only simulation. A validated 60 GHz testbed built from a Xilinx Zynq UltraScale+ RFSoC and a Sivers beamforming front-end scanned 63 transmit directions to construct a full 63x63 beamspace across 350 measurement points on a 1.95 m x 3.60 m indoor grid. mmWave radar is being flown on agricultural UAVs with a mechanically rotating head to widen the field of view for terrain-following. On the signal generation side, dual-laser self-injection locking to a micro-Fabry-Perot reached about -148 dBc/Hz at 1 MHz offset on a 111 GHz carrier, and an integrated photonic mmWave radar chip was reported in November 2025 <sup class="ref"><a href="https://www.nature.com/articles/s41586-024-07057-0" title="Photonic mmWave / microwave signal generation — research landscape (2024–2025)" rel="noopener">ref</a></sup>.

What holds the score below 5 is that most of the systems work in this set is simulation-only, and the one prototype that demonstrates a genuinely new array architecture, FlexLink's delay-phased array, was built on a 4-7 GHz testbed rather than at mmWave itself, with mmWave named as the target regime rather than the demonstration regime. The recurring theme across the hybrid precoding papers is that near-optimal spectral efficiency is achievable but only via algorithms requiring several hundred iterations, or with feedback that scales linearly in subcarrier count, which is exactly the sort of gap between demonstrated and deployable that keeps a technology at 4.

**TLDR: Physics and hardware are demonstrated; the unresolved questions are overhead, cost and power, not feasibility.**

## Drivers (3/5)

On the supply side there is evidence of a maturing component base: commercial 60 GHz beamforming front-ends integrated with off-the-shelf RFSoC platforms, and a photonic generation route framed as smaller, lighter and more power-efficient than electronic multiplier chains for carriers above 40 GHz, where the source states plainly that the remaining open question is commercial rather than scientific <sup class="ref"><a href="https://www.nature.com/articles/s41586-024-07057-0" title="Photonic mmWave / microwave signal generation — research landscape (2024–2025)" rel="noopener">ref</a></sup>. Against this, no source in this set provides shipment volumes, operator capex, spectrum auction outcomes or subscriber data, so the strength of the pull cannot be verified from the supplied evidence. The score reflects clearly articulated technical demand without any commercial confirmation.

**TLDR: Demand is asserted from 6G and IIoT specifications and from robot perception; the sources contain no market or deployment data.**

## Novelty (3/5)

mmWave itself is incumbent technology in this literature, treated as the assumed platform rather than the innovation. The comparisons worth judging are therefore internal. Against edge-mounted phone antennas at the same carrier, a transparent on-screen planar array is simulated to raise uplink spectral efficiency by over 50% at 28 GHz and by more than 150% at 300 GHz, while resisting user-induced blockage. Against conventional phased arrays, a prototyped delay-phased array achieves nearly double the spectral efficiency by serving control and data beams simultaneously without splitting per-beam gain. Against per-subcarrier feedback, hierarchical interpolation cuts overhead from O(K) to O(K/M + log M). Against iterative alternating-minimisation analog precoding requiring several hundred iterations, a closed-form column-wise solution computes the analog precoder in one step. Radar-assisted beam selection suppresses an unintended user below -135 dBm while adding roughly 2 dB of beamforming gain for legitimate users.

Two items are more foundational. The first is the waveform question: if OFDM's time-invariance assumption really does fail in doubly dispersive mmWave and sub-THz channels, then delay-Doppler and chirp-based spreading is a break from the basis of 4G and 5G rather than an increment, though the source frames this as an emerging research direction rather than a settled result. The second is photonic generation, described as beating electronics on phase noise above 100 GHz <sup class="ref"><a href="https://www.nature.com/articles/s41586-024-07057-0" title="Photonic mmWave / microwave signal generation — research landscape (2024–2025)" rel="noopener">ref</a></sup>. Neither is yet demonstrated at system scale in these sources, so 3 rather than 4.

**TLDR: The band is not new; the credible novelty is in specific overhead reductions with quantified deltas of tens of percent to about 2x.**

## Diffusion (2/5)

The supplied literature reads as an inventory of adoption barriers. Phased arrays at mmWave are fundamentally constrained to a single beam or lose gain sharply when split, limiting simultaneous control and data support. Beam management overhead is called a critical requirement for practical deployment of non-terrestrial mmWave networks, implying it is not yet solved. Channel estimation is hard: pilot overhead is high in large-scale IRS deployments because surface elements are passive, and conventional far-field codebooks stop being valid as arrays grow. On the device side, user-induced blockage of edge-mounted antennas (the 'death grip') and poor aperture scalability are named as unsolved problems at mmWave and sub-THz. Hardware cost recurs: RF chains are expensive and power-hungry, and local oscillators are a major cost, power and complexity item in mmWave receivers.

There is also a non-technical barrier specific to this band. Because mmWave and sub-THz networks can collect or infer location and environment data, behavioural profiling such as movement and activity recognition, and in advanced cases physiological information including breathing frequency and heart-rate-related data about users and bystanders alike, sensing capabilities will have to be controlled to satisfy privacy requirements. That is a regulatory dependency on the ISAC value proposition. No source here reports deployed base stations, handset penetration or radar unit volumes, so a higher score would not be earned. The one area where diffusion looks easier is sensing on robots, where the components are already low-cost and being flown.

**TLDR: Blockage, beam management overhead, RF chain and LO cost, pilot overhead and ISAC privacy all remain open, and the sources show no adoption data.**

## Impact (3/5)

The breadth is real. The same beamforming hardware that carries data also supports simultaneous localisation and mapping, since a beamforming mmWave front-end provides all the specifications needed to build a SLAM system and to construct radio digital twins. In perception, dense LiDAR-like point clouds have been reconstructed from a single radar frame without motion or synthetic aperture, reaching state of the art on the RadarHD benchmark and generalising to new environments, which would extend usable perception into conditions where optical sensors fail. In non-terrestrial networks, radar-derived angle and distance information both cuts beam search overhead and provides a physical-layer security lever. The ISAC privacy analysis is, read the other way, a statement of how much information this band can extract from a physical environment.

What is missing is any measure of value. The sources report spectral efficiency gains, dBm suppression figures, feedback scaling and phase noise records; none reports revenue, cost saving, energy saving at network scale, or a counterfactual against staying in mid-band. Capacity gains in a network are also gated by the diffusion barriers above, so the realised impact is likely to be much smaller than the demonstrated per-link gains. A score of 3 records demonstrated technical consequence with unquantified economic consequence.

**TLDR: Broad capability across comms, localisation and perception, but the sources quantify performance rather than value.**

## Timing Soon (2-5yr)

The sensing side is already at the applied-engineering stage: radar is being mounted and rotated on agricultural UAVs for terrain-following flight, and single-frame densification is being tuned against an existing benchmark rather than proposed in the abstract. If the question is when mmWave hardware does useful work, the answer is now.

The communications side is explicitly framed as forward-looking. The waveform question is open, with the migration to mmWave and sub-THz described as a future condition under which OFDM's assumptions become difficult to maintain. Device antennas are proposed for 'future mobile devices', the new array architecture that removes the single-beam constraint exists as a 4-7 GHz prototype, and ISAC privacy controls are at the classification and requirements stage. Photonic generation above 40 GHz is described as scientifically settled with the commercial question open <sup class="ref"><a href="https://www.nature.com/articles/s41586-024-07057-0" title="Photonic mmWave / microwave signal generation — research landscape (2024–2025)" rel="noopener">ref</a></sup>. That combination of solved physics and unsolved integration, cost and standardisation puts the communications payoff in a 2-5 year band, contingent on 6G specification timelines the sources do not give.

**TLDR: mmWave sensing is deployable now; mmWave as a mass communications layer is still gated by beam management, hardware cost and unsettled waveform choices.**

## Overrated or underrated? Fairly rated

Taken as a whole the band is priced about right, but the internal split is mispriced. The communications story is the loudly promoted one and it is the one carrying the most unresolved overhead: single-beam phased arrays, hundreds of iterations to compute an analog precoder, feedback scaling in subcarrier count, pilot overhead in reconfigurable-surface deployments, invalid far-field codebooks as arrays grow, and a waveform whose core assumption is being questioned for exactly these bands. That is a lot of load-bearing work still in progress.

The sensing story is quieter and closer to done. Robustness in fog, smoke, dust and low light on size-, weight- and power-constrained platforms is a differentiated capability with no obvious substitute at comparable cost, and it is being demonstrated on real flying hardware and real benchmarks. The main thing to watch is that the two converge: the case for ISAC rests on the arrays being shared, and the constraint on ISAC will be privacy regulation, since the same hardware can infer breathing frequency and heart-rate-related data about people who never consented. Anyone underwriting mmWave on comms capacity alone is buying the weaker half.

## Prediction

By June 2028, photonic mmWave generation will still have no volume deployment in commercial cellular base stations, remaining confined to instrumentation, radar and research demonstrators, notwithstanding phase-noise records already beating electronic multiplier chains above 100 GHz <sup class="ref"><a href="https://www.nature.com/articles/s41586-024-07057-0" title="Photonic mmWave / microwave signal generation — research landscape (2024–2025)" rel="noopener">ref</a></sup>.

## Evidence base

- A validated 60 GHz testbed pairing a Xilinx Zynq UltraScale+ RFSoC with a Sivers beamforming front-end scanned 63 transmit directions to build a full 63x63 beamspace across 350 points on a 1.95 m x 3.60 m indoor grid, published 8 May 2026.
- Transparent on-screen antenna arrays are simulated to raise uplink spectral efficiency by over 50% at 28 GHz and more than 150% at 300 GHz versus edge-mounted antennas, while resisting user-induced blockage, 3 June 2026.
- A prototyped delay-phased array at 4-7 GHz decoupled control and data beams for the first time, achieving nearly double the spectral efficiency of conventional phased arrays without extra power, 2 June 2026.
- Radar-assisted beam selection for mmWave non-terrestrial networks suppressed an unintended user's received power below -135 dBm while adding roughly 2 dB of beamforming gain for legitimate users, 2 June 2026.
- Dual-laser self-injection locking to a micro-Fabry-Perot reached about -148 dBc/Hz at 1 MHz offset on a 111 GHz carrier, and an integrated photonic mmWave radar chip was reported in November 2025; the source states the remaining question is commercial, not scientific <sup class="ref"><a href="https://www.nature.com/articles/s41586-024-07057-0" title="Photonic mmWave / microwave signal generation — research landscape (2024–2025)" rel="noopener">ref</a></sup>.
- ISAC in mmWave and sub-THz 6G deployments may collect or infer location and environment data, behavioural profiles such as movement and activity, and physiological data including breathing frequency and heart-rate-related information, from users and bystanders alike, 28 May 2026.

## Open questions

- Does the delay-phased array that decouples control and data beams reproduce its near-2x spectral efficiency gain when built at 28 GHz or above, rather than on the 4-7 GHz testbed where it was prototyped?
- Is Doppler degradation at mmWave under high mobility severe enough in measured channels to justify abandoning OFDM for delay-Doppler or chirp waveforms, or do MIMO, coding and scheduling remedies remain sufficient?
- Will privacy regulation permit the spatial sensing that ISAC's value case depends on, given that mmWave and sub-THz deployments can infer behavioural and physiological data about non-consenting bystanders?
- Can the combination of reduced-feedback precoding, closed-form analog precoding, LO-free receivers and learned channel estimation actually bring per-array cost and power down enough for dense deployment, or do the individual savings fail to compose?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
