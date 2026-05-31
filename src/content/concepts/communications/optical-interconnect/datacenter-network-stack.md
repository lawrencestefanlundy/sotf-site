---
type: concept
slug: datacenter-network-stack
canonical_name: Datacenter Optical Networking — Plain-English Stack Primer
aliases:
- networking primer
- ocs context
- transceiver vs switch vs router
kind: framework
parent_concepts:
- communications
- optical-interconnect
related_concepts:
- optical-interconnect
- optical-circuit-switching
- optical-packet-switching
- co-packaged-optics
- lasers
last_updated: '2026-05-30'
tags:
- concept
- framework
- primer
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors:
- slug: optical-interconnect
  name: Optical Interconnect
  path: /sotf-site/communications/optical-interconnect/optical-interconnect/
  macro: communications
- slug: optical-circuit-switching
  name: Optical Circuit Switching (OCS)
  path: /sotf-site/communications/optical-interconnect/optical-circuit-switching/
  macro: communications
- slug: optical-packet-switching
  name: Optical Packet Switching (OPS)
  path: /sotf-site/communications/optical-interconnect/optical-packet-switching/
  macro: communications
- slug: co-packaged-optics
  name: Co-Packaged Optics
  path: /sotf-site/manufacturing/packaging/co-packaged-optics/
  macro: manufacturing
- slug: lasers
  name: Lasers
  path: /sotf-site/photonic-systems/light-sources/lasers/
  macro: photonic-systems
---
*A navigation aid for placing any optical-networking deal. Written 2026-05-30. The whole field solves one problem: moving bits between chips fast without burning too much power. Almost every component is a **converter** (electrons ↔ light), a **decider** (where does this bit go?), or the **road** between them.*

## The converter chain (one bit, GPU A → GPU B)

Data starts electrical on a chip; to send it far you put it on light and read it back.

- **Laser** — the light source. Steady blank carrier (flashlight held on).
- **Modulator** — impresses data onto the beam by flicking it billions of times/sec (the hand flicking the flashlight into Morse). The materials race (TFLN, BTO, silicon — [Lithium Niobate (TFLN)](/sotf-site/materials/functional-layers/lithium-niobate-tfln/)) is just ways to flick faster/cheaper/cooler.
- **Photodetector** — converts light back to electrical at the far end (reads the Morse).
- **Transceiver** — does both directions: TRANS-mitter (laser+modulator) + re-CEIVER (detector) + DSP. The translator at each fiber end. Each conversion (**O-E-O**, optical-electrical-optical) burns power — the villain of the whole story.
  - **Pluggable** — a transceiver as a removable faceplate module (a dongle). Most of the market.
  - **[Co-Packaged Optics](/sotf-site/manufacturing/packaging/co-packaged-optics/) (CPO)** — moves the transceiver next to the switch chip (mm not cm of electrical trace) to cut power. "CPO vs pluggables" = *where you put the converter*.
- **Fiber** — the road.

## The deciders (where OCS fits)

- **Switch (electronic packet switch)** — reads every packet's destination address and forwards it (postal sorting machine reading every label). Converts O-E-O at every hop = power cost. **Broadcom Tomahawk**, **NVIDIA**, **Arista**.
- **Router** — a switch one layer up: forwards *between* networks (datacenter ↔ internet) by IP. Switch = within a network; router = between networks. In an AI cluster you care about the switch.
- **[OCS](/sotf-site/communications/optical-interconnect/optical-circuit-switching/)** — does NOT read packets. Physically redirects the whole light beam fiber-to-fiber (tilting a mirror) to set a dedicated lane (railway turntable vs reading each parcel). Cheap, low-power, any-speed, but "dumb" and slow to reconfigure (ms). Sets the **topology**, not per-packet routing. Google's Apollo (**Google Ocs**).
- **[OPS](/sotf-site/communications/optical-interconnect/optical-packet-switching/)** — the holy grail: switch individual packets while still light, no conversion. Brutally hard (needs optical memory, which doesn't really exist). **Finchetto**'s bet.

## The hierarchy

chip → server → rack → pod → datacenter. (chip = desk, rack = office, pod = floor, datacenter = building; transceivers = phones on desks, switches = mailrooms on floors, OCS = the re-wireable riser.)
- **Chip/package:** electrical + emerging optical I/O (Ayar, Lightmatter).
- **Scale-up:** GPUs within a pod, fast/tight, mostly electrical (NVLink, copper). See **Optical Vs Electrical Scale Up**.
- **Scale-out:** pods across the building; top-of-rack → spine → core; where big packet switches live and where **OCS competes** as a reconfigurable patch panel.

## Where deals sit (the placement question)

AI broke the old model: thousands of GPUs in lockstep, so electronic switches hit power/bandwidth walls and every conversion hurts. Two layers, two responses:

**The one question that places any deal:** is it a *converter* (link layer) or a *decider* (switch layer), and at which rung of the hierarchy? That fixes who it competes with and which thesis it tests. For the switch-layer speed axis (why "MEMS is too slow"), see the spectrum table in [Optical Circuit Switching (OCS)](/sotf-site/communications/optical-interconnect/optical-circuit-switching/).
