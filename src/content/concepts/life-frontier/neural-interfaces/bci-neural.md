---
type: concept
slug: bci-neural
canonical_name: BCI & Neural Interfaces
aliases:
- BCI
- brain-computer interface
- neural interface
kind: category
parent_concepts:
- life-frontier
- neural-interfaces
related_concepts:
- invasive-bci
- non-invasive-bci
- bioelectronic-medicine
- hearables-silent-speech
- arvr
- connectomics
sources: []
frontier:
- Can flexible, minimally invasive ECoG arrays achieve the channel count and longevity needed for high-bandwidth motor prosthetics without open-skull surgery?
- What is the signal fidelity ceiling for non-invasive EEG at scalp, and can dry electrode arrays close the gap with wet gel?
- How do regulatory pathways (FDA Breakthrough Device, CE MDR) shape the viable commercial BCI entry point — medical vs consumer first?
last_updated: 2026-06-02
tags:
- concept
- category
mention_count: 0
descendants:
- non-invasive-neural-recording-modalities
last_reorg_date: '2026-05-13'
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: invasive-bci
  name: Invasive BCI (Neuralink, Synchron, Paradromics)
  path: /sotf-site/life-frontier/neural-interfaces/invasive-bci/
  macro: life-frontier
- slug: non-invasive-bci
  name: Non-Invasive BCI (EEG, in-ear, NIRS)
  path: /sotf-site/life-frontier/neural-interfaces/non-invasive-bci/
  macro: life-frontier
- slug: bioelectronic-medicine
  name: Bioelectronic Medicine (vagus nerve, DBS)
  path: /sotf-site/life-frontier/neural-interfaces/bioelectronic-medicine/
  macro: life-frontier
- slug: hearables-silent-speech
  name: Hearables / Silent-Speech Interfaces
  path: /sotf-site/life-frontier/neural-interfaces/hearables-silent-speech/
  macro: life-frontier
- slug: arvr
  name: AR/VR
  path: /sotf-site/life-frontier/neural-interfaces/arvr/
  macro: life-frontier
- slug: connectomics
  name: Connectomics
  path: /sotf-site/life-frontier/neural-interfaces/connectomics/
  macro: life-frontier
---
A brain-computer interface (BCI) is a system that establishes a direct communication or control pathway between the brain and an external device, bypassing conventional motor or peripheral pathways. The field splits on two fundamental axes: **invasive vs non-invasive** recording, and **medical vs consumer** application.

**Invasive BCIs** — electrodes implanted into or on cortical tissue. Electrocorticography (ECoG) grids sit on the brain surface (subdural); microelectrode arrays (MEAs, e.g. Utah Array, Neuralink N1) penetrate cortex to record single-unit action potentials, giving the highest spatial resolution (~100 µm). Signal quality degrades over months to years due to glial scarring (the foreign-body response to implanted materials). See [Invasive BCI (Neuralink, Synchron, Paradromics)](/sotf-site/life-frontier/neural-interfaces/invasive-bci/).

**Non-invasive BCIs** — scalp EEG, fNIRS, MEG. Millimetre-to-centimetre spatial resolution; millisecond temporal resolution for EEG. EEG's ~20 µV signals are two to three orders of magnitude weaker than implanted recordings and are blurred by skull. See [Non-Invasive BCI (EEG, in-ear, NIRS)](/sotf-site/life-frontier/neural-interfaces/non-invasive-bci/).

The signal modalities determine application space: high-bandwidth motor prosthetics and direct speech decoding require implanted electrodes. Attention monitoring, emotion detection, and AR/VR interaction ([AR/VR](/sotf-site/life-frontier/neural-interfaces/arvr/)) are accessible with non-invasive approaches. Bioelectronic medicine ([Bioelectronic Medicine (vagus nerve, DBS)](/sotf-site/life-frontier/neural-interfaces/bioelectronic-medicine/)) closes-the-loop by using implanted electrodes to stimulate peripheral nerves (vagus, sciatic) for therapeutic effect in inflammatory disease, epilepsy, and pain.

**Investment relevance:** medical BCIs follow a long regulatory path (FDA PMA for implantables). Consumer-grade applications — hearables ([Hearables / Silent-Speech Interfaces](/sotf-site/life-frontier/neural-interfaces/hearables-silent-speech/)), AR/VR neural input, silent-speech interfaces — have shorter paths but harder monetisation. The semiconductor opportunity is in ultra-low-power analog front-ends (AFEs) capable of 1,000+ channel recording with on-chip spike sorting.

## Frontier

- Can flexible ECoG arrays achieve high channel-count, long-lifetime motor prosthetics without open-skull surgery?
- What is the signal-fidelity ceiling for non-invasive EEG at scalp, and can dry electrodes close the gap?
- How do FDA/CE regulatory pathways shape the viable BCI entry point — medical vs consumer first?

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
