---
type: concept
slug: iot-connected-devices
canonical_name: IoT & Connected Devices
aliases: []
kind: market
parent_concepts:
- communications
- wireless
related_concepts: []
sources: []
scorecard:
  viability: 4
  drivers: 3
  novelty: 4
  diffusion: 3
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Underrated
scorecard_status: draft
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-08-27-opener-is-an-open-source-reference-implementation-of-the-dec
  title: Opener is an open-source reference implementation of the DECT NR+ massive IoT, low-latency standard - CNX Software
  date: '2026-08-27'
  kind: web
- slug: 2026-08-21-dect-nr-gateway-brings-deterministic-wireless-to-industrial-
  title: DECT NR+ gateway brings deterministic wireless to industrial automation - eeNews Europe
  date: '2026-08-21'
  kind: web
- slug: 2026-08-19-wi-fi-7-breaks-into-the-mcu-field-next-gen-wireless-connecti
  title: 'Wi-Fi 7 Breaks into the MCU Field: Next-Gen Wireless Connectivity for Microcontroller Applications - 36 Kr'
  date: '2026-08-19'
  kind: web
- slug: 2026-08-18-wi-fi-7-accelerates-into-the-mcu-space-as-infineon-and-synap
  title: Wi-Fi 7 Accelerates into the MCU Space as Infineon and Synaptics Move First - finance.biggo.com
  date: '2026-08-18'
  kind: web
- slug: 2026-08-03-quectel-adds-wi-fi-7-and-bluetooth-60-modules-for-consumer-a
  title: Quectel Adds Wi-Fi 7 and Bluetooth 6.0 Modules for Consumer and Edge Devices - IoT Business News
  date: '2026-08-03'
  kind: web
- slug: 2026-08-02-shipments-of-wireless-devices-in-industrial-automation-to-re
  title: Shipments of wireless devices in industrial automation to reach 8.5 million by 2030 - TyN Magazine
  date: '2026-08-02'
  kind: web
- slug: 2026-08-01-inje-university-partners-with-huawei-to-build-a-cutting-edge
  title: Inje University Partners with Huawei to Build a Cutting-Edge Wi-Fi 7 Smart Campus - Huawei Enterprise
  date: '2026-08-01'
  kind: web
- slug: 2026-07-09-non-cellular-5g-networks-simplified---hacksterio
  title: Non-Cellular 5G Networks Simplified - Hackster.io
  date: '2026-07-09'
  kind: web
neighbors: []
---
**IoT and connected devices is no longer a connectivity story but an edge-compute, energy-autonomy and sensing-reuse story, where the frontier work is squeezing learning onto microcontrollers at nanoamp idle currents and extracting radar-like sensing from radios and fibre that are already deployed.**

## Summary

"IoT and connected devices" covers the population of low-cost, power-constrained, network-attached endpoints: wireless sensor nodes, wearables, smart-building sensors, tags, and the gateways and edge servers behind them. The category is old in technology terms. One of the sources notes the Internet of Things was introduced almost two decades ago, and that the wearable market has grown continuously over that period. What is moving now is not the idea of connecting a sensor, but four specific engineering constraints that decide whether a deployment is economic.

The first is energy. A node that must be visited to change a battery is usually not worth deploying. Recent work attacks the quiescent current that dominates energy budgets in light-starved photovoltaic installations, using a hardware-orchestrated power manager that fully power-gates the microcontroller and peripherals and wakes it from an ultra-low-power PMIC, RTC and latch, reaching 452 nA idle drain. The second is on-device intelligence. Because backhaul and cloud inference cost power, bandwidth and privacy, the work is on fitting learning, not just inference, into milliwatt budgets: neural architecture search that runs on the embedded device itself under 512 MB of RAM to generate tiny CNNs for low-end MCUs, an accelerator supporting end-to-end on-chip few-shot and continual learning on sequential data at 0.5% area overhead over the inference logic, and a fabricated 65 nm hyperdimensional encoder that uses transistor process variation as its entropy source and reports 7.13 nJ per encoding with 93.2% accuracy on EMG and 96.1% on UCI-HAR.

The third constraint is sensing cost, and this is where the most interesting shift sits. Rather than deploying new sensors, several lines of work reuse infrastructure that already exists. Passive bistatic integrated sensing and communication extracts Doppler-based, radar-like target separation from unmodified LoRa uplinks, validated with two USRP B210 software-defined radios and without interfering with the live network. Passive backscatter tags act as virtual anchors for non-line-of-sight indoor positioning, achieving an aggregated median error of 0.505 m in office-corridor measurements with four devices at 866 MHz. Installed fibre-optic plant is repurposed as a dense seismic array through distributed acoustic sensing, with a graph-theoretic analysis showing a percolation transition at 51.6% coverage above which a city is effectively fully covered for statistical traffic monitoring.

The fourth constraint is heterogeneity and operations. Edge fleets span low-power microcontrollers to accelerator-equipped nodes, which makes deploying AI pipelines across them a scheduling problem rather than a packaging problem, and drives orchestration frameworks that separate allocation decisions from execution. New device substrates carry their own operational tax: flexible IGZO thin-film electronics lack packaging and pins, making conventional automatic test equipment impractical and forcing built-in self-test with 93% single-defect coverage at 3% power overhead. The parameters that decide the field are therefore energy per inference, idle current, sensing accuracy achievable without new hardware, and the cost of managing a heterogeneous fleet.

## Viability (4/5)

The honest counterweight is that several papers name the residual gap themselves. DNN speech enhancement on an embedded FPGA meets the 10 ms clinical latency threshold for denoising at 9.7 ms but misses it for separation at 16.0 ms, with data movement rather than arithmetic identified as the bottleneck. Sub-THz presence detection at 134 to 146 GHz works, but detection depends strongly on target position and antenna beamwidth, and repeated empty-room measurements show that small environmental changes such as slight furniture movement produce channel variation of the same kind the detector relies on. That is a false-positive problem, not a sensitivity problem, and it is the harder of the two.

**TLDR: Component-level results are fabricated, measured and mostly reproducible, though several stop short of deployment thresholds.**

## Drivers (3/5)

On supply, the enablers stack up: silicon-level power gating that removes the dominant idle energy sink in energy-harvesting nodes; learning algorithms cheap enough to fit alongside inference logic at 0.5% area overhead; architecture search that no longer needs a server, so a gateway can retune a model on locally acquired data; and low-cost security primitives, where a hybrid oscillator arbiter PUF generates cryptographic keys at 2.7 uW against 25 uW for an arbiter PUF. Reuse of existing plant, LoRa networks and installed fibre, removes the capital cost that usually kills sensing deployments.

On demand, the sources assert rather than quantify. Growing wearable volumes and the resulting privacy exposure from constantly transmitted location and heart-rate data are given as the motivation for hardware security. Smart-city real-time applications and the need to cut latency and bandwidth are given as the motivation for edge orchestration. Low-altitude airspace planning is given as the motivation for aerial radio maps. These are plausible pulls, but there is no market sizing, procurement data or deployment count in the supplied material, so the score is capped.

**TLDR: Supply-side enablers are clearly documented; demand evidence in these sources is motivational rather than measured.**

## Novelty (4/5)

The comparisons are explicit and the multipliers are large. Against a full-video baseline on AR glasses, gaze- and pose-guided selective retention cuts memory footprint 27.5x and energy 24.3x while preserving egocentric video understanding accuracy. Against prior IGZO-TFT oscillator designs, the dual-purpose ring oscillator and VCO achieve 1100x area reduction and 5600x lower power. Against software-managed low-power states, hardware orchestration removes a persistent quiescent drain that the authors identify as the dominant energy sink in low light. The neuromorphic encoder is better than conventional item-memory schemes in that it does not store random basis vectors at all, using device variation as write-free entropy.

The sensing side is better than the alternative mainly on cost of ownership rather than raw performance. Passive LoRa ISAC is not better than a purpose-built wideband radar at ranging; it is better than having no radar at all in a network you already own, and it distinguishes itself from earlier LoRa sensing work by needing no waveform modification, so it applies to deployed networks. Similarly, backscatter anchors avoid phase synchronisation and transmit-power calibration entirely, which is what makes sub-metre non-line-of-sight tracking cheap rather than accurate.

**TLDR: Large, quantified margins against the incumbent approach in each niche, chiefly by deleting hardware or deleting cloud round-trips.**

## Diffusion (3/5)

Two barriers dominate in these sources. The first is fleet heterogeneity: AI pipelines must span low-power microcontrollers through to accelerator-equipped systems, and existing edge platforms are described as focused on deployment automation while remaining inefficient at adaptive allocation under dynamic conditions. The same fragmentation appears one layer down, where static backend assignment on an edge platform cannot exploit shape-dependent performance differences, and naive per-operator selection introduces costly device and framework switches. The second is test and qualification. Flexible electronics cannot be tested with conventional ATE because of missing packaging, limited pins and high device variability, so self-test has to be designed in from the start.

Against that, the designs most likely to diffuse are the ones that demand nothing from the incumbent. Sensing on unmodified LoRa waveforms in a purely passive bistatic configuration can be added by an observer without touching network operation. Distributed acoustic sensing rides existing fibre, and the analysis is explicit that useful applications, earthquake early warning, groundwater monitoring and urban activity tracking, are available below 10% coverage with optimal design. Low incremental coverage requirements are the single best predictor of adoption here. The sources do not, however, say anything about standardisation, certification or procurement, which is where infrastructure sensing usually stalls.

**TLDR: The installed base is the strongest adoption asset and the biggest fragmentation problem at the same time.**

## Impact (4/5)

If the sensing-reuse thesis holds, the value is not incremental sensor revenue but a new data layer over existing assets. The DAS coverage analysis quantifies what that layer buys at each stage: below 10% coverage, earthquake early warning, groundwater monitoring, geological mapping and urban activity tracking; a percolation transition at 51.6% coverage above which the city is effectively fully covered and statistical traffic monitoring becomes possible; only near-complete coverage supports infrastructure monitoring and individual vehicle tracking, which is also why the authors argue privacy risk stays very low in practice. That is an unusually clean impact ladder for an infrastructure technology.

On the device side, the impact is in categories that were previously blocked by power or privacy. On-device few-shot and continual learning enables personalisation without sending raw data anywhere, with reduced maintenance cost as the stated commercial benefit, and the fabricated encoder supports in-situ decision-making, continual learning and federated learning for multi-user cold-start personalisation. Hearing aids are the clearest single high-value case, where the constraint is a hard 10 ms clinical latency threshold rather than a preference. The score is not 5 because none of the sources demonstrate value captured at scale; they demonstrate the enabling numbers.

**TLDR: Turns already-installed radios, fibre and wearables into a continuous sensing and inference layer with near-zero marginal capital cost.**

## Timing Soon (2-5yr)

The component layer is effectively available. Silicon has been fabricated and measured, MCU-class fusion and learning run on real boards under 100 mW, and hardware power management has demonstrated 452 nA idle. Products limited only by energy per inference should absorb these within a normal design cycle. The one named clinical gap, speech separation at 16.0 ms against a 10 ms threshold, is attributed to data movement and on-chip parameter caching rather than compute throughput, which is a tractable engineering target rather than a research one.

The sensing-reuse layer is slower. LoRa passive ISAC is at the feasibility stage, demonstrated with laboratory software-defined radios and focused on Doppler-based target separation. Sub-THz presence detection has an unresolved environmental-change confound. City-scale DAS depends on on-chip short-range DAS availability, which the analysis assumes rather than demonstrates. Aerial radio mapping is at the dataset-and-foundation-model stage. Two to five years is the reasonable band for these reaching operational service.

**TLDR: Node-level energy and on-device learning results are ready now; infrastructure-scale sensing reuse needs coverage build-out and false-positive work.**

## Overrated or underrated? Underrated

IoT as a label is stale, and that staleness is causing the current substance to be underweighted. The interesting claim in this corpus is not that more devices will be connected; it is that already-deployed radios and fibre can be read as sensors without modification, and that learning now fits inside the node rather than in the cloud. Passive bistatic sensing on unmodified LoRa signals applies directly to networks already in operation, passive backscatter tags give sub-metre non-line-of-sight tracking without phase synchronisation or transmit-power calibration, and the DAS coverage analysis shows several monitoring applications are unlocked below 10% fibre coverage. Capabilities with near-zero marginal capital cost tend to be systematically undervalued because they generate no procurement event.

The qualifier is that the value accrues to whoever operates the infrastructure, not to a new device category. The bottleneck is unglamorous: idle current, data movement, defect coverage on untestable substrates, and orchestration across devices spanning several orders of magnitude in capability. Anyone expecting a unit-volume story should read this as fairly rated at best. Anyone underwriting sensing-as-a-service over existing plant is looking at an underpriced option.

## Prediction

By the end of 2028, at least one commercial LPWAN or building-systems operator will offer a motion or occupancy sensing service derived from unmodified LoRa uplinks in a live network, following the passive bistatic Doppler feasibility demonstrated in June 2026.

## Evidence base

- 15 June 2026: radar-like Doppler sensing shown feasible using unmodified LoRa signals in a purely passive bistatic configuration, validated with two USRP B210 software-defined radios and without interfering with network operation.
- 16 June 2026: hardware-orchestrated dynamic power management reaches 452 nA quiescent drain by fully power-gating the MCU and peripherals, targeting photovoltaic sensor nodes in low light.
- 16 June 2026: fabricated 65 nm privacy-preserving neuromorphic encoder measures 7.13 nJ per encoding, 76.44 nJ per prediction and 357.32 nJ per training update, with 93.2% EMG and 96.1% UCI-HAR accuracy and federated learning support.
- 16 June 2026: distributed acoustic sensing coverage analysis identifies useful monitoring applications below 10% fibre coverage and a percolation transition at 51.6% coverage above which a city is effectively fully covered.
- 17 June 2026: four passive backscatter devices at 866 MHz deliver 0.505 m aggregated median indoor non-line-of-sight positioning error in office-corridor measurements, without phase synchronisation or transmit-power calibration.
- 20 July 2026: fixed-point DNN denoising on an AMD-Xilinx Kria KV260 achieves 9.7 ms first-sample latency, meeting the 10 ms hearing-aid clinical threshold, while speech separation remains at 16.0 ms.
- 22 July 2026: built-in self-test for flexible IGZO-TFT mixed-signal circuits reports 1100x area reduction and 5600x lower power than prior designs, with 93% single-defect coverage at 3% power overhead, because conventional ATE is impractical for this substrate.

## Open questions

- Can passive LoRa ISAC hold Doppler-based target separation in a live multi-node network with uncontrolled traffic, rather than the controlled bistatic setup validated with two USRP B210 radios?
- Is the environmental-change false-positive problem in sub-THz presence detection, where slight furniture movement produces channel variation comparable to human presence, solvable by calibration or does it require a fundamentally different detection metric?
- Does on-chip DAS actually become available at the cost and range assumed by the coverage-threshold analysis, since the entire 51.6% percolation argument is conditional on that assumption?
- Can the data-movement bottleneck identified on embedded FPGA speech enhancement be closed enough to bring speech separation from 16.0 ms under the 10 ms clinical threshold, and does the same bottleneck cap other real-time edge inference workloads?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
