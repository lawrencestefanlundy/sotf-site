---
type: concept
slug: neural-interfaces
canonical_name: Neural Interfaces
aliases: []
parent_concepts: []
related_concepts: []
sources:
- '[[2023-09-18-e15-in-conversation-with-wisear-on]]'
- '[[2026-03-26-sotf-interview-dorian-haci-mintneuro]]'
- '[[2023-05-31-three-underrated-technologies-from]]'
- '[[2026-06-23-inbrain-graphene-first-in-human]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
descendants:
- ar-glasses-stack
- ar-optical-combiners
- arvr
- bci-neural
- bioelectronic-medicine
- connectomics
- hearables-silent-speech
- invasive-bci
- non-invasive-bci
- non-invasive-neural-recording-modalities
mention_count: 11
frontier:
- Does the IGZO thin-film backplane retain in-pixel gain, noise floor and multiplexing fidelity over months of chronic implantation, and at what channel count does interconnect reduction stop being the limiting factor?
- Can the NEMO sensor's 110 µV limit of detection be reduced to resolve single-unit spikes in vivo, and what is the measured stimulation-artefact rejection compared with a matched electrode array?
- Do lysosome-directed interventions measurably reduce the reported ~50% one-year BCI failure rate in animal or human implants, and by how much?
- Will InBrain's 90-day follow-up and fuller 2026 results show whether graphene electrodes offer any chronic advantage, given that the completed study was intra-operative rather than chronic?
- Does ns-ZrOx's memristive behaviour produce a functional biohybrid computation advantage in neuron-glia networks, beyond demonstrated biocompatibility?
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-06-23-inbrain-graphene-first-in-human
  title: 'InBrain Neuroelectronics: world-first-in-human graphene neural interface study, $50M Series B, FDA Breakthrough Device, Merck KGaA partnership'
  date: '2026-06-23'
  kind: web
- slug: 2026-03-26-sotf-interview-dorian-haci-mintneuro
  title: 'Chips for the Brain: Modular Semiconductors for Neural Interfaces (MintNeuro / Dorian Haci)'
  date: '2026-03-26'
  kind: substack
- slug: 2023-09-18-e15-in-conversation-with-wisear-on
  title: '☎️ E15: In Conversation with Wisear on The State of Hearables, Brain Computer Interfaces and Augmented Reality 👂🎧🧠'
  date: '2023-09-18'
  kind: substack
- slug: 2023-05-31-three-underrated-technologies-from
  title: '💡E02: Three Underrated Technologies from the Future: Brain Recording; Deep Geothermal; IVF + Updates BCI; Clean Meat; LEO Internet++'
  date: '2023-05-31'
  kind: substack
neighbors: []
---
## Physics / mechanism

Neural interfaces are devices that transduce electrical activity in nervous tissue into signals a machine can read, and in the reverse direction deliver stimulation. The dominant approach places metal microelectrodes in or on the brain, where they capture extracellular potentials; clinical uses include treatment of Parkinson's disease, epilepsy and paralysis, and control of external effectors such as a robotic arm or a speech decoder nsf 2552758 lysosome directed strategies to improve . The core physical trade-off is between electrode size and signal quality: shrinking a site to improve spatial resolution raises its impedance and degrades signal-to-noise ratio, while stimulation on the same substrate leaves residual artefacts in the recording path nemo neural electro mechano optic sensors for multiplexed ne.

Channel count scaling has been driven by thin-film fabrication, lithography and connectorisation, taking passive arrays to thousands of channels, with credible routes to larger formats. Wiring density, not sensor density, becomes the binding constraint, so an alternative is to put active electronics at the sensing site. One implementation is a monolithic flexible thin-film integrated circuit built like an active-matrix display: dual-gate amorphous indium gallium zinc oxide transistors on polyimide provide in-pixel transconductance amplification plus row-column time-division multiplexing, reducing the interconnect count needed to address a large array biorxiv a thin film transistor backplane for scalable . A separate integration path is modular mixed-signal ASICs that split sensing, stimulation, processing, power, wireless and safety functions across function-specific chips, on the argument that amplification, filtering, ADC and stimulation need low power, low heat and small form factor rather than leading-edge process nodes sotf interview dorian haci mintneuro.

Optical and optomechanical readout sidesteps the impedance limit. The NEMO sensor uses a miniaturised nano-electromechanical electrostatic transducer to modulate a silicon photonic microdisk resonator, converting the local electrical signal into optical modulation for transmission out of tissue; the reported limit of detection is 110 microvolts, within range of neural signals nemo neural electro mechano optic sensors for multiplexed ne. Optical coherence tomography probes are a related enabling component: a fully fibre-integrated OCT probe whose distal interferometric architecture (beam expansion, side-view redirection) is defined by a single two-photon-polymerised element is aimed in part at neural interfaces and other confined structures fully fiber integrated endoscopic oct probes by single step .

Chronic stability is a tissue-biology problem more than an electronics problem. Half of implanted brain-computer interfaces stop functioning within a year because the surrounding tissue fails to heal and remains inflamed; insertion leaves cellular debris including damaged cells, blood and myelin fragments, and the lysosomal clearance machinery of local cells is overwhelmed and cannot remove it nsf 2552758 lysosome directed strategies to improve . Material design responses include nanostructured cluster-assembled films chosen for biomimetic morphology, mechanotransductive properties and neuromorphic behaviour; nanostructured zirconium oxide (ns-ZrOx) has shown memristive and signal-processing behaviour compatible with biohybrid systems, and both nanostructured and flat zirconia substrates supported adhesion and survival of primary astrocytes and dorsal root ganglion neuron-glia co-cultures biorxiv nanostructured zirconia thin films as neurogli. Graphene is a second material route, taken to first-in-human use for intra-operative cortical mapping inbrain graphene first in human.

## Competitive landscape

| Route | Mechanism | Status in sources |
|---|---|---|
| Passive thin-film metal arrays | Direct extracellular recording, one interconnect per site | Thousands of channels demonstrated; interconnect-limited biorxiv a thin film transistor backplane for scalable  |
| Active flexible backplane | IGZO thin-film transistors on polyimide, in-pixel gain plus multiplexing | Platform demonstration biorxiv a thin film transistor backplane for scalable  |
| Modular implantable ASICs | Function-split mixed-signal chips on mature nodes | 40+ chips taped out over 15 years by the team behind the approach sotf interview dorian haci mintneuro |
| Electro-optomechanic sensing | NEMS transducer modulating a photonic microdisk | 110 µV limit of detection nemo neural electro mechano optic sensors for multiplexed ne |
| Graphene electrodes | Alternative electrode material | First-in-human intra-operative study completed inbrain graphene first in human |
| Nanostructured oxide / neurogliomorphic films | ns-ZrOx with memristive behaviour, biohybrid coupling | In-vitro cell studies biorxiv nanostructured zirconia thin films as neurogli |

These are complementary rather than strictly competing: electronics integration attacks channel count, optomechanics attacks the impedance/SNR and artefact limits, and materials plus lysosome-directed biology attack chronic failure. One view from within the industry is that miniaturisation rather than surgical access is the scaling barrier, drawing an analogy to a cardiac monitor that moved from roughly 100 implants per year to around 1 million per year as an injectable device sotf interview dorian haci mintneuro.

## Evidence base

- Roughly half of implanted BCIs stop functioning within a year owing to failed healing and persistent inflammation around the electrode, attributed in part to overwhelmed lysosomal clearance of insertion debris; NSF award 2552758, $550,000, dated 06/02/2026 nsf 2552758 lysosome directed strategies to improve .
- The NEMO electro-optomechanic sensor achieved a limit of detection of 110 microvolts, targeting the resolution/SNR trade-off from high-impedance small electrodes and stimulation artefacts; published 2026-04-20 nemo neural electro mechano optic sensors for multiplexed ne.
- A monolithic flexible thin-film IC using dual-gate amorphous IGZO transistors on polyimide implemented in-pixel transconductance amplification and row-column time-division multiplexing for high-channel-count chronic interfaces; preprint 2026-06-24 biorxiv a thin film transistor backplane for scalable .
- ns-ZrOx and flat zirconia substrates both supported adhesion and survival of primary astrocytes and DRG neuron-glia co-cultures, with ns-ZrOx previously shown to have memristive and signal-processing capability; preprint 2026-05-28 biorxiv nanostructured zirconia thin films as neurogli.
- InBrain completed enrolment of a first-in-human graphene neural interface study in April 2026, with 8 of 10 recruited patients implanted intra-operatively during brain-tumour resection at Manchester / Northern Care Alliance, reporting zero device failures and zero adverse events, 90-day follow-up underway; a $50M Series B closed in October 2024 led by imec.xpand inbrain graphene first in human.
- A single two-photon-polymerised element defined the complete distal interferometric architecture of a fully fibre-integrated endoscopic OCT probe, with neural interfaces named as a target application; published 2026-08-17 fully fiber integrated endoscopic oct probes by single step .

## Frontier (open questions)

- Does the IGZO thin-film backplane retain in-pixel gain, noise floor and multiplexing fidelity over months of chronic implantation, and at what channel count does interconnect reduction stop being the limiting factor?
- Can the NEMO sensor's 110 µV limit of detection be reduced to resolve single-unit spikes in vivo, and what is the measured stimulation-artefact rejection compared with a matched electrode array?
- Do lysosome-directed interventions measurably reduce the reported ~50% one-year BCI failure rate in animal or human implants, and by how much?
- Will InBrain's 90-day follow-up and fuller 2026 results show whether graphene electrodes offer any chronic advantage, given that the completed study was intra-operative rather than chronic?
- Does ns-ZrOx's memristive behaviour produce a functional biohybrid computation advantage in neuron-glia networks, beyond demonstrated biocompatibility?

*Synthesised 2026-08-31 from 9 KB sources by the resynth pipeline; citations are KB source slugs.*
