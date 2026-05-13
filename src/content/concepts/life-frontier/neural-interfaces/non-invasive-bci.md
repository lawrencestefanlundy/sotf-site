---
type: concept
slug: non-invasive-bci
canonical_name: Non-Invasive BCI (EEG, in-ear, NIRS)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- life-frontier
- neural-interfaces
related_concepts: []
companies_using:
- arctop
- bitbrain
- brainaccess-neurotechnology
- cortrium
- earable-neuroscience
- emotiv
- haplox-formerly-brainco
- idun-technologies-acquired-by-logitech-sennheiser-spinout
- kernel
- mindo
- muse-interaxon
- neuphony
- neurable
- neuracle-technology
- neuroprofs-mentalab
- neuros-medical-exclude-invasive-use-holistic
- neurosity-already-listed-replace-with-flow-neuroscience
- neurosity
- nextmind-snap-inc
- nuro-neurowear-brand-use-nurokor-actually-use-versus
- openbci
- prophesee-relevant-nirs-adjacency-exclude-use-nirx-instead
- zeto
ideas_referencing: []
sources: []
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
---

# Non-Invasive BCI (EEG, in-ear, NIRS)

*Kind: technology*

## Physics / mechanism

Non-invasive BCI captures neural signals without penetrating the skull. EEG measures scalp electrical potentials (µV range, 0.1–100 Hz bandwidth) via electrode arrays; consumer-grade headsets run 8–32 channels at ~250 Hz sample rate, research-grade up to 256 channels. In-ear EEG embeds electrodes in the ear canal, sacrificing spatial resolution for wearability. NIRS (near-infrared spectroscopy, 650–950 nm) measures hemodynamic response (oxygenation proxy for neural activity) with ~1–2 cm spatial resolution, ~5 s temporal lag. Current SoA: EEG decodes motor imagery at ~80% accuracy in controlled settings; NIRS is used for prefrontal workload monitoring. Neither approach approaches invasive BCI (ECoG, Utah array) on signal fidelity.

## Competitive landscape

EEG competes directly with fNIRS and hybrid EEG-fNIRS systems. Invasive approaches (ECoG, Neuralink-style Utah arrays) dominate on bandwidth and signal quality but require surgery, defining a hard ceiling for non-invasive use cases.

## Cloudberry relevance

| Modality | Temporal res. | Spatial res. | Wearability |
|---|---|---|---|
| EEG | <10 ms | ~cm | High |
| fNIRS | ~5 s | ~1–2 cm | Medium |
| ECoG/Utah | <1 ms | ~µm | None |

Adjacent: EMG-based gesture control (Ctrl-Labs/Meta), eye-tracking, galvanic skin response. ML signal processing (transformer-based decoding) is increasingly the differentiator, not the sensor itself.


Relevance sits in the semiconductor and photonics stack beneath the application layer. Custom ASICs for low-noise analog front-ends (AFE), miniaturised VCSEL/photodetector pairs for wearable NIRS, and GaN/SiGe process nodes for ultra-low-power edge inference are the investable components. GlobalFoundries' 22FDX platform is credible for always-on AFE SoCs. Deal-flow angle: fabless chip startups targeting medical-grade or consumer-wearable signal acquisition, where process node and mixed-signal design are the moat, not the BCI software stack.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
