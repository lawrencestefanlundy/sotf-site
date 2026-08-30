---
type: concept
slug: non-invasive-neural-recording-modalities
canonical_name: Non-invasive neural recording modalities (BCI readout)
aliases:
- brain imaging modalities
- non-invasive BCI modalities
parent_concepts:
- bci-neural
related_concepts: []
frontier:
- Does any group image at depth (>3cm) through an intact adult skull non-invasively with fUS, or does depth still require a window/array implant?
- Can ML-based skull aberration correction close the transcranial fUS imaging gap this cycle?
sources:
- '[[2026-06-13-noninvasive-bci-modality-research]]'
last_updated: 2026-06-13
tags:
- concept
- bci
- brain-imaging
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
The readout side of non-invasive BCI. The investable question (Lawrence, non-invasive only): which modality reaches the depth, coverage, spatial resolution and wearable size/weight a real BCI needs, without surgery. The dividing line is depth. Electrical, magnetic and optical modalities are all capped at the cortical surface by the skull; only ultrasound has a physical path to deep structures.

## Scorecard (state of the art, Jun 2026)

**EEG** — depth: cortical surface only, skull-blurred · spatial: poor (~cm) · temporal: excellent (ms) · size: tiny, fully wearable · non-invasive: yes · mature/commodity. A ceiling effect is documented: EEG information content already exceeds what BCI control needs (~175 bit/min), so ML and EEG foundation models (CBraMod, KU Leuven) decode the existing signal better but cannot add depth or spatial resolution. Plays: Neurable, BrainCo, Emotiv, OpenBCI.

**fNIRS / HD-DOT** — depth: ~20-30mm (cortical) · spatial: HD-DOT reaches ~1/2 fMRI · temporal: slow (hemodynamic, seconds) · size: wearable · non-invasive: yes · maturing. Cannot reach deep structures. Plays: Kernel (Flow), Openwater (optical).

**OPM-MEG** — depth: cortical (surface-biased) · spatial: better than EEG · temporal: excellent · size: light helmet, BUT needs a magnetically shielded room and often coils, so the *environment* is bulky · non-invasive: yes · clinically advancing (FieldLine wearable helmet, phase-2 epilepsy/Parkinson's 2024-25; Cerca 64-sensor; QuSpin). The best wearable surface modality, but shielding-bound and cortical.

**fUS (functional ultrasound imaging)** — depth: 5-8cm, reaches deep structures · spatial: ~100µm (mesoscopic) · temporal: ~1-10Hz · size: tiny transducer (≈11.5×8.6mm footprint) · non-invasive at depth in adults: NOT YET (current human depth fUSI replaces a skull fragment with the imaging array, i.e. semi-invasive; transcranial adult readout is blocked by skull attenuation and aberration) · research/early but heavily funded. The only modality with the physics for depth + resolution + tiny size; the whole bet is cracking the transcranial skull. Plays: Forest Neurotech (FRO), Merge Labs ($252M, OpenAI/Bain/Newell), Gestala ($21.6M), Openwater.

Note: focused-ultrasound *stimulation* (TUS, write/neuromodulation) does work transcranially, even to deep targets, because energy only has to go in. fUS *imaging* (readout) is harder, the echo has to come back out through the skull, which is why transcranial adult imaging lags stimulation.

## Verdict

On the depth / coverage / size / weight quartet, fUS is the only non-invasive-class modality that can in principle hit all four; the surface modalities (EEG, fNIRS, OPM-MEG) are structurally capped at the cortex. The gating risk is real and current: non-invasive transcranial adult fUS imaging at depth is unsolved, so today's deep fUS in humans is semi-invasive (window). The diligence binary for any fUS BCI deal is whether it images at depth through an intact adult skull or needs a window. The smart money (Merge, Forest, Gestala, Openwater) is concentrating on ultrasound precisely to solve this.

## How close is transcranial adult fUS (deeper read, 13 Jun 2026)

Three routes through the skull, ranked by invasiveness:
1. **Cranial window / acoustically-transparent skull replacement** — demonstrated in a living adult human (Caltech, Science Translational Medicine; a polymeric window placed during TBI skull reconstruction). Full depth, high resolution, works. Requires the window, so not non-invasive.
2. **Microbubble-contrast transcranial ULM/fUS** — images deep adult human brain vasculature through intact skull and scalp today, but needs an IV microbubble injection plus heavy aberration-correction compute. 4D functional shown in rats through intact skull at ~15µm. No surgery, but contrast-dependent, and whole-brain adult human functional is still preclinical.
3. **Acoustic-transparency (chelating agent) + pure aberration correction** — 2025 preprint: a chelating agent matches skull acoustic impedance for ~94% transmission, ~20µm, full depth, through mouse and human skulls. The cleanest path to truly non-invasive (no contrast, no surgery) if it can be delivered to a living skull safely. Earliest-stage, likely ex-vivo human skull, unproven in vivo.

Route-agnostic enabling layer: **skull-aberration-correction compute** (ML differentiable beamforming, complex-valued CNNs, SVD, ray-theory), needed by every route, working in rodents and non-human primates and improving fast. The durable wedge that pays off whichever physical route wins.

Revised timeline: a genuinely non-invasive (no-surgery) adult fUS readout at depth is plausibly 2-4 years out, gated by acoustic-transparency translating to living humans, or by contrast-ULM scaling to whole-brain functional.

## Who's on which route (Jun 2026)

The read/write axis explains the field. Transcranial **stimulation** (energy in) works non-invasively today; transcranial deep **readout** (echo back out) does not, so the serious readout money goes through a window.

- **Forest Neurotech / Merge Labs** (Sumner Norman; Forest = Eric Schmidt FRO, Merge = $252M OpenAI/Bain/Newell): fUS imaging readout (plus neuromodulation), but deliberately starting through a **skull window / craniectomy** because the adult skull is the obstacle (demonstrated across wide swaths of human brain in craniectomy patients, correlations meeting or exceeding fMRI). The best-resourced, most credible readout team, and they chose semi-invasive. That choice is itself the signal that non-invasive transcranial readout is not ready.
- **Gestala** (China, $21.6M, Guosheng/Dalton): **non-invasive** transcranial phased-array, but **stimulation-led** (write, modulating deep circuits), not deep readout. Three months old, prototype pending, building an "Ultrasound Brain Bank" decoding dataset.
- **Openwater** (Mary Lou Jepsen, ~$100M): non-invasive light + sound + EM imaging, a separate optical/acoustic hybrid.

The combination Lawrence wants, non-invasive + depth + readout, is the hardest corner and is currently unfunded at scale. The only way to back it now is the enabling layer (acoustic-transparency chemistry, aberration-correction compute), or to accept stimulation (Gestala-style) as the non-invasive write play.

Sources: [Emergence of fUS for non-invasive BCI (Research/Science)](https://spj.science.org/doi/10.34133/research.0200) · [Future of transcranial ultrasound as a precision brain interface (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11521279/) · [Miniaturized 4D fUS (medRxiv 2025)](https://www.medrxiv.org/content/10.1101/2025.08.19.25332261) · [OPM-MEG next-gen neuroimaging (Trends in Neurosciences)](https://www.cell.com/trends/neurosciences/fulltext/S0166-2236(22)00102-3) · [Merge Labs $252M ultrasound BCI](https://www.biopharmatrend.com/news/openai-backs-ultrasound-based-brain-computer-interface-startup-with-252m-seed-round-1470/) · [Gestala $21.6M (TechCrunch)](https://techcrunch.com/2026/03/11/bci-startup-gestala-raises-21-million-for-non-invasive-ultrasound-brain-tech/) · [HD-DOT depth/resolution (Sci Rep 2025)](https://www.nature.com/articles/s41598-025-85858-7) · [EEG foundation models / ceiling](https://arxiv.org/pdf/2506.01867)
