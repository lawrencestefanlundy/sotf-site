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
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 41
last_reorg_date: '2026-05-14'
sources_7d: 3
sources_30d: 4
recent_mentions:
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

Photonic memory stores and retrieves data using light rather than electrons, exploiting phase-change materials (PCMs) or electro-optic effects in integrated photonic circuits. The dominant mechanism: GST (Ge₂Sb₂Te₅) or GSST thin films erase/write via laser pulses that toggle crystalline ↔ amorphous states, modulating optical transmission. Multi-level cell (MLC) operation demonstrated at 5+ levels per cell. On-chip read speeds reach sub-nanosecond; endurance typically 10⁵–10⁷ cycles before degradation. Retention >10 years projected for crystalline state. Leading academic demonstrations: Oxford, MIT, EPFL. Commercial activity nascent — Bodle Technologies (acquired), Lumenisity adjacent. Integration with silicon photonics waveguides is the active frontier; insertion loss and CMOS back-end compatibility remain unsolved at volume.

## Competitive landscape

Competing approaches: DRAM and SRAM remain dominant for compute-adjacent memory; their latency advantage shrinks as photonic interconnect bandwidth scales. MRAM and ReRAM offer non-volatility but stay electronic. In-memory computing via memristors (Mythic, Analog Devices) is the most direct architectural rival for inference workloads.

| Approach | Non-volatile | Optical I/O native | Maturity |
|---|---|---|---|
| PCM photonic | Yes | Yes | Lab/early proto |
| Electronic PCM (Intel Optane lineage) | Yes | No | EOL |
| ReRAM / memristor | Yes | No | Early commercial |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
