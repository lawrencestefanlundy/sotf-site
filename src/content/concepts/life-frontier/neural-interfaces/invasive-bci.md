---
type: concept
slug: invasive-bci
canonical_name: Invasive BCI (Neuralink, Synchron, Paradromics)
aliases: []
kind: technology
parent_concepts:
- life-frontier
- neural-interfaces
related_concepts: []
sources:
- '[[2023-05-31-three-underrated-technologies-from]]'
- '[[2026-06-13-noninvasive-bci-modality-research]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 4
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 2
recent_mentions:
- slug: 2026-06-13-noninvasive-bci-modality-research
  title: 'Non-invasive BCI modality state-of-the-art: which reaches depth + coverage + size + weight (research synthesis)'
  date: '2026-06-13'
  kind: web
- slug: 2023-05-31-three-underrated-technologies-from
  title: '💡E02: Three Underrated Technologies from the Future: Brain Recording; Deep Geothermal; IVF + Updates BCI; Clean Meat; LEO Internet++'
  date: '2023-05-31'
  kind: substack
neighbors: []
---
## Physics / mechanism

Invasive BCI places electrodes in direct contact with neural tissue to record action potentials or local field potentials with sub-millisecond temporal resolution and single-neuron spatial resolution. Three main insertion paradigms: Utah array (96–1024 electrodes, 400 µm pitch, silicon substrate), Neuralink's "threads" (~1024 channels, flexible polyimide, robotic insertion to minimize gliosis), and Synchron's Stentrode (endovascular, ~16 electrodes, no craniotomy). Signal chain: electrode → impedance matching amplifier → ADC (typically 16-bit, 20–30 kSps per channel) → compression/spike-sorting → wireless telemetry. Bandwidth bottleneck is the transcutaneous wireless link; Neuralink's N1 chip targets ~1 Mbps. Chronic recording stability degrades over 6–24 months due to foreign body response and electrode impedance drift. Paradromics pursues high-channel-count cortical surface arrays targeting 1M+ electrodes long-term.

## Competitive landscape

Non-invasive EEG competes on safety and cost but delivers ~64–256 channels, poor spatial resolution (~cm vs. µm), and no single-unit access. ECoG sits between—subdural grid, ~1mm resolution, used clinically. fNIRS and fMRI are research tools, not real-time BCI substrates. MEG offers good temporal resolution but zero implantability.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
