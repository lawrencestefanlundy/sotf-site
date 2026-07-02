---
type: concept
slug: photonic-memory
canonical_name: Photonic Memory
aliases:
- optical memory
- optical data storage
kind: technology
parent_concepts:
- memory
- emerging-memory
related_concepts: []
sources:
- '[[2023-07-14-e08-optical-computing]]'
- '[[2025-12-19-lfg-for-semiconductors]]'
- '[[2025-02-25-data-driven-vc-is-over]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-06-01-hbm-state-of-play]]'
frontier:
- Does any photonic / optical memory reach high-volume manufacturing this decade?
- Which pull comes first for photonic memory, compute buffering or interconnect?
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 58
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 4
recent_mentions:
- slug: 2026-06-01-hbm-state-of-play
  title: HBM state of play (mid-2026) — technology, supercycle, three-supplier standing
  date: '2026-06-01'
  kind: web
- slug: 2025-12-19-lfg-for-semiconductors
  title: LFG (for semiconductors)
  date: '2025-12-19'
  kind: substack
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
- slug: 2025-02-25-data-driven-vc-is-over
  title: data-driven VC is over
  date: '2025-02-25'
  kind: substack
- slug: 2023-07-14-e08-optical-computing
  title: '🔮E08: Optical Computing'
  date: '2023-07-14'
  kind: substack
neighbors: []
---
## Physics / mechanism

Photonic memory stores and retrieves data using light rather than electrons, exploiting phase-change materials (PCMs) or electro-optic effects in integrated photonic circuits. The dominant mechanism: GST (Ge₂Sb₂Te₅) or GSST thin films erase/write via laser pulses that toggle crystalline ↔ amorphous states, modulating optical transmission. Multi-level cell (MLC) operation demonstrated at 5+ levels per cell. On-chip read speeds reach sub-nanosecond. **But note: AIMA — the only memory-medium company in the space — does NOT use phase-change; it uses femtosecond all-optical magnetic switching (see landscape below).** Leading academic demonstrations: Oxford/Münster (Bhaskaran/Pernice, PCM-on-waveguide origin), MIT, EPFL, NTT (all-optical RAM). Commercial activity nascent. Integration with silicon-photonics waveguides is the active frontier; insertion loss and CMOS back-end compatibility remain unsolved at volume.

## Company landscape (2026)

Honest headline (landscape sweep, 2026-05-30): **very few pure-play "memory built from light" companies exist.** Most "photonic + memory" is actually interconnect, compute, or archival storage. The genuine memory-*medium* plays:

These three are the genuine memory-*medium* attempts (AIMA most advanced; the latter two found via a 2026-05-30 Granola search). The rest of the category is lab work (TU Eindhoven/Koopmans, Radboud/Kimel-Rasing, MIT/EPFL/NTT).

### Optical / holographic ARCHIVAL storage (separate market: cold-storage, not in-package AI memory)
Real, funded, EU-concentrated: **Cerabyte** (DE — ceramic-glass; WD / Pure / In-Q-Tel backed), **SPhotonix** (CH — 5D silica glass, $4.5M), **HoloMem** (UK — holographic tape), **Ewigbyte** (DE — glass ablation), **Optera Data** (SG). Defunct ref: **Akonia Holographics** (US) — acquired by **Apple (2018)** for AR waveguides.

### Research / lab context (not companies)
Microsoft **Project Silica** (5D glass archival), **IBM** (non-volatile optical memory in SiPh), **Oxford/Münster** (PCM-on-waveguide origin), **NTT** (all-optical RAM nanocavity), **Southampton** (Sb₂Se₃ low-loss PCM + the Kazansky 5D-glass lineage).

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- Does any photonic / optical memory reach high-volume manufacturing this decade?
- Which pull comes first for photonic memory, compute buffering or interconnect?
