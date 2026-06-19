---
type: concept
slug: rram-reram
canonical_name: RRAM / ReRAM
aliases: []
kind: technology
parent_concepts:
- memory
- emerging-memory
related_concepts:
- in-memory-computing
- memcapacitor
- analog-computing
- edge-ai
- embedded-non-volatile-memory
- mram
- pcm-phase-change-memory
sources: []
frontier:
- 'Three forks, three readiness states: (1) ReRAM-as-embedded-NVM is in production at low density (TSMC 28nm, GF 22FDX); (2) analog multi-level ReRAM-CIM is NOT production-ready (variability/drift/endurance/ADC wall); (3) binary/digital ReRAM-CIM is the emerging 2026 workaround (AAIC, Laxnar).'
- Does the binary/digital path (saturated two-level cells + architectural precision) overtake analog multi-level conductance for edge inference by 2027?
- Is Fork-1 process maturity (the Intrinsic/GF signal) the bridge that de-risks the substrate for Fork-3, or does the profit stay stuck at IP-licensing economics (the Weebit model)?
- Can analog multi-level ReRAM-CIM (TetraMem, Sagence) ever clear the precision wall, or is Mythic's 2024 restructuring the category verdict?
last_updated: '2026-06-04'
tags:
- concept
- technology
mention_count: 0
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 3
recent_mentions: []
neighbors:
- slug: in-memory-computing
  name: In-Memory Computing
  path: /sotf-site/memory/emerging-memory/in-memory-computing/
  macro: memory
- slug: memcapacitor
  name: Memcapacitor
  path: /sotf-site/memory/emerging-memory/memcapacitor/
  macro: memory
- slug: analog-computing
  name: Analog Computing
  path: /sotf-site/compute/non-conventional/analog-computing/
  macro: compute
- slug: edge-ai
  name: Edge AI
  path: /sotf-site/compute/ai-edge/edge-ai/
  macro: compute
- slug: embedded-non-volatile-memory
  name: Embedded Non-Volatile Memory
  path: /sotf-site/memory/emerging-memory/embedded-non-volatile-memory/
  macro: memory
- slug: mram
  name: MRAM (STT/SOT-MRAM)
  path: /sotf-site/memory/mainstream-memory/mram/
  macro: memory
- slug: pcm-phase-change-memory
  name: Phase-Change Memory (PCM)
  path: /sotf-site/memory/emerging-memory/pcm-phase-change-memory/
  macro: memory
---
## Physics / mechanism

Resistive RAM stores data by switching a thin dielectric (typically HfO₂, TaO_x, or Al₂O₃) between high-resistance (HRS) and low-resistance (LRS) states via controlled filament formation and rupture. An applied voltage drives oxygen vacancy migration, forming or dissolving a conductive filament—SET operation ~1 V, RESET ~1–2 V, switching <10 ns, endurance 10⁶–10¹² cycles depending on material stack. Retention >10 years at 85 °C for mature nodes. Cell area as small as 4F². Multi-level cell (MLC) operation enables 2–3 bits/cell. Leading process nodes: TSMC 28 nm embedded RRAM in production; GlobalFoundries exploring integration at 22FDX. Key players: Weebit Nano, Crossbar, CXMT, Ememory, Panasonic.

## Competitive landscape

RRAM competes primarily with embedded Flash (eFlash), MRAM, and PCM for NVM applications.

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Production status: three forks (4 Jun 2026)

"Is ReRAM scalable" has three answers, because ReRAM is three bets (full synthesis: **2026 06 04 Reram Scalability What It Enables**):

## Frontier (open questions)

See frontmatter `frontier:` block. Key resolution markers:
- **2027:** does binary/digital ReRAM-CIM outnumber analog multi-level parts reaching silicon for edge inference? (tracked as a prediction on **Emerging Nvm**)
- **2027:** does a startup ReRAM process get publicly designed into a major foundry's embedded-NVM roadmap (Intrinsic/GF materialises)?
- **2028:** does any analog multi-level ReRAM-CIM vendor reach $100M cumulative product revenue, or is the analog fork a confirmed dead end?

## 2026 update: the digital-readout shift

*Source: **2026 06 16 Cim Landscape 2026**.*
