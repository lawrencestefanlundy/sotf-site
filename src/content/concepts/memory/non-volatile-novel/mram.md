---
type: concept
slug: mram
canonical_name: MRAM (STT/SOT-MRAM)
aliases: []
kind: technology
domain:
- cloudberry
- sotf
parent_concepts:
- memory
- non-volatile-novel
related_concepts: []
companies_using:
- allegro-microsystems
- antaios
- applied-materials
- avalanche-technology
- cantor
- crocus-technology
- everspin-technologies
- globalfoundries
- headway-technologies
- imec
- infineon-technologies
- integrated-silicon-solution-inc-issi
- intel
- nxp-semiconductors
- qualcomm
- renesas-electronics
- samsung-electronics
- silicon-storage-technology-sst-microchip
- sindhu-spinout-from-eth-zurich
- spin-memory-now-part-of-applied-materials
- tdk-corporation
- tohoku-university-cies-spin-outs
- tsmc
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

# MRAM (STT/SOT-MRAM)

*Kind: technology*

## Physics / mechanism

Magnetic RAM stores bits via the magnetization orientation of a magnetic tunnel junction (MTJ): a fixed reference layer and a free layer separated by an MgO tunnel barrier. **STT-MRAM** (spin-transfer torque) switches the free layer by passing a spin-polarized current through the MTJ; switching current ~100 µA, write time ~10 ns, endurance >10¹² cycles. **SOT-MRAM** (spin-orbit torque) decouples read/write paths via a heavy-metal (W, Ta, Pt) spin Hall channel, cutting write current ~3× and improving endurance. Retention: ~10 years at 85 °C for embedded nodes. TSMC, GlobalFoundries, Samsung, and Everspin have qualified embedded STT-MRAM at 22–40 nm; SOT remains mostly pre-production.

## Competitive landscape

STT-MRAM competes directly with eFlash (dominant embedded NVM below 28 nm, but scaling-limited), SRAM (as last-level cache replacement), and FeRAM/FRAM (lower endurance, niche). SOT targets SRAM-class latency (<1 ns write claimed in research). PCM (Intel Optane, now discontinued) competed at storage-class tier. Emerging competition includes FeFET (TSMC, Globalfoundries roadmaps) which offers smaller cell size but inferior endurance data at scale.

## Cloudberry relevance

| Technology | Write energy | Endurance | Scalability |
|---|---|---|---|
| STT-MRAM | ~pJ/bit | >10¹² | Good to 14 nm |
| FeFET | ~fJ/bit | ~10⁸–10¹⁰ | Excellent |
| eFlash | ~nJ/bit | ~10⁵ | Poor <28 nm |


GlobalFoundries is a qualified STT-MRAM foundry (22FDX platform), making this directly deal-flow-relevant: startups building MCUs, edge-AI inference chips, or automotive SoCs on GF 22FDX need embedded NVM IP. Cloudberry angles include MTJ materials suppliers (MgO, CoFeB deposition), process IP licensors (Spin Memory, Avalanche), and fabless design teams targeting always-on IoT or rad-hard applications where MRAM's write-endurance and field-immunity beat all alternatives.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
