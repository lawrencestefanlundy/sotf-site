---
type: concept
slug: power-electronics
canonical_name: Power Electronics
aliases: []
kind: technology
parent_concepts:
- energy-power
- power-electronics
related_concepts: []
sources:
- '[[2025-07-01-a-primer-carbon-nanotubes]]'
- '[[2025-09-10-uk-opportunity-in-ai-compound-semiconductors]]'
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2025-09-11-power-electronics-researchers-awarded-15m-to-advance-energy-]]'
- '[[2024-yole-power-gan-2024]]'
- '[[2024-omdia-power-electronics-forecast]]'
- '[[2026-02-19-the-rise-of-grid-power-electronics-with-drew-baglino---latit]]'
frontier:
- ''
last_updated: '2026-05-04'
tags:
- concept
- technology
mention_count: 26
last_reorg_date: '2026-05-13'
descendants:
- electric-motors-drives
- gan-on-si
- gw-scale-power-delivery
- power
- power-electronics
- power-management-ic
- solid-state-circuit-breakers
- wireless-power-transfer
sources_7d: 3
sources_30d: 4
---
## Physics / mechanism

Power electronics governs conversion, control, and conditioning of electrical power — switching, rectifying, and transforming voltage/current with minimal loss. Core components: MOSFETs, IGBTs, diodes, gate drivers, passive filters. Key figures of merit: switching frequency (kHz–MHz), on-resistance (RDS(on), mΩ range), breakdown voltage (V_BR, 10 V–10 kV+), and thermal resistance (°C/W). Silicon dominates legacy designs; wide-bandgap (WBG) materials — SiC (bandgap 3.26 eV) and GaN (3.4 eV) — enable higher switching frequencies, lower conduction losses, and operation above 150 °C. Leading SiC fabs: Wolfspeed, STMicro, onsemi. GaN leaders: Infineon (GaN Systems), EPC, Navitas. Inverter efficiency now routinely exceeds 99% in grid-tied applications.

## Competitive landscape

The primary competitive axis is material platform. Si IGBTs dominate cost-sensitive, lower-frequency applications (<50 kHz). SiC wins in EV traction inverters and industrial drives (600 V–1700 V). GaN dominates fast-charging and data-centre power (100–650 V, high-frequency). Gallium oxide (Ga₂O₃) and diamond are emerging for ultra-high-voltage (>3 kV) with theoretical advantages but remain pre-production.

| Platform | Voltage range | Switching freq | Maturity |
|----------|--------------|----------------|----------|
| Si IGBT | 600 V–6.5 kV | <50 kHz | Commodity |
| SiC MOSFET | 650 V–3.3 kV | 100 kHz–1 MHz | Scaling |
| GaN HEMT | 100–650 V | 1–10 MHz | Growth |

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->

## Frontier (open questions)

- *To be added.*
