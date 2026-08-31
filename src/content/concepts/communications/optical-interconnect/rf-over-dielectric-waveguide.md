---
type: concept
slug: rf-over-dielectric-waveguide
canonical_name: RF-over-dielectric-waveguide interconnect
aliases:
- e-Tube
- THz radio over wire
- active RF cable
- sub-THz waveguide interconnect
- radio over plastic waveguide
parent_concepts:
- rack-scale-interconnect
related_concepts:
- optical-interconnect
- hbm
sources:
- '[[2026-07-13-semiengineering-startup-funding-q2-2026]]'
frontier:
- 'Reach and bandwidth-density ceiling vs linear-drive optics at 1.6T/3.2T lane classes: where exactly does the dielectric-waveguide window sit (rumoured 1-10m mid-range) and does it hold as lane rates double?'
- Loss per metre and connector story at sub-THz carriers in a production rack (bend radius, crosstalk, thermal drift) vs the copper DAC/AEC baseline?
- Does any hyperscaler or switch vendor standardise the medium (an OIF/IEEE lane), or does it stay proprietary point solutions absorbed as cable products?
- 'Watch item for optical displaces copper: if this medium takes the 1-10m mid-range socket, the optical transition skips a reach class and the CPO volume ramp thins.'
last_updated: 2026-07-16
tags:
- concept
mention_count: 1
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-07-13-semiengineering-startup-funding-q2-2026
  title: 'Startup Funding: Q2 2026'
  date: '2026-07-13'
  kind: web
neighbors:
- slug: optical-interconnect
  name: Optical Interconnect
  path: /communications/optical-interconnect/optical-interconnect/
  macro: communications
- slug: hbm
  name: HBM (High-Bandwidth Memory)
  path: /memory/mainstream-memory/hbm/
  macro: memory
---
Data transmission by modulating a millimetre-wave / sub-THz RF carrier onto a **plastic dielectric waveguide** instead of driving copper conductors or optical fibre. The transmitter and receiver are CMOS/SiGe RF SoCs; the channel is a low-loss dielectric "tube" or ribbon. The pitch: copper's reach collapses above 200G/lane while optics carries laser, photonic assembly, and reliability cost; a purely electrical RF front-end with a waveguide channel claims the **mid-range (roughly 1-10m, in-rack and adjacent-rack) socket** at optics-class bandwidth without optics-class complexity.

Two funded proponents as of Q2 2026 (see <sup class="ref"><a href="https://semiengineering.com/startup-funding-q2-2026/" title="Startup Funding: Q2 2026" rel="noopener">ref</a></sup>):

- ****Attotude**** (f. 2024, Menlo Park; $143M raised, $52M Series C with Keysight strategic): "THz radio over wire", ASIC signal generation + low-loss dielectric waveguides at 200G/400G/800G per lane, aimed at AI scale-up fabrics.
- ****Point2 Technology**** (f. 2016, San Jose; Series B extensions incl. Nvidia NVentures, UMC Capital): "Active RF Cable" mmWave transceiver SoCs and smart retimers through plastic dielectric waveguide, roadmap to 800G/1.6T/3.2T cable classes.

**Why this page exists.** The medium is a live counter-datapoint to the load-bearing assumption **Optical Displaces Copper**: it attacks the same reach class that co-packaged and near-packaged optics are supposed to take next, with a technology that keeps the electrical ecosystem (SerDes, retimers, cable vendors) intact. It does not need to beat optics everywhere to matter; it only needs the mid-range socket to delay the optical crossover by a reach class. Tracked so the radar and cross-pollination can tag papers, funding, and standards activity in this lane. Evidence lands on the assumption's `evidence_log` and on **Scale Up Interconnect**.
