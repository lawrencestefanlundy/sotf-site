---
type: concept
slug: space-communications
canonical_name: Space Communications
aliases:
- SATCOM
- satellite communications
- space-to-ground links
kind: category
parent_concepts:
- life-frontier
- in-orbit
related_concepts:
- optical-inter-satellite-links
- leo-mega-constellations
- direct-to-cell-leo
- gnss-pnt
sources: []
frontier:
- Can optical inter-satellite links (OISLs) achieve sufficient pointing stability on low-cost small-sat platforms without deformable mirrors?
- What is the practical data-rate ceiling for direct-to-device LEO broadband without licensed spectrum refarming?
- How does quantum key distribution (QKD) via satellite scale to a commercial service model?
last_updated: 2026-06-02
tags:
- concept
- category
mention_count: 0
descendants: []
last_reorg_date: '2026-05-14'
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-06-12-conversations-in-the-sky-galileos-intersatellite-links-teste
  title: 'Conversations in the sky: Galileo’s intersatellite links tested'
  date: '2026-06-12'
  kind: web
neighbors:
- slug: optical-inter-satellite-links
  name: Optical Inter-Satellite Links
  path: /sotf-site/life-frontier/in-orbit/optical-inter-satellite-links/
  macro: life-frontier
- slug: leo-mega-constellations
  name: LEO Mega-Constellations
  path: /sotf-site/life-frontier/in-orbit/leo-mega-constellations/
  macro: life-frontier
- slug: direct-to-cell-leo
  name: Direct-to-Cell / LEO SOS (Lynk, AST SpaceMobile)
  path: /sotf-site/life-frontier/in-orbit/direct-to-cell-leo/
  macro: life-frontier
- slug: gnss-pnt
  name: GNSS / PNT
  path: /sotf-site/life-frontier/in-orbit/gnss-pnt/
  macro: life-frontier
---
Space communications covers all transmission of data between spacecraft and ground stations (space-to-ground links), between satellites (inter-satellite links, ISL), and between satellites and end-user terminals (direct-to-device). It is the nervous system of the commercial space economy.

**RF links** dominate current infrastructure. Ka-band (26.5–40 GHz) and Ku-band (12–18 GHz) are the workhorses for broadband SATCOM. The Shannon limit constrains throughput for a given bandwidth; link budget engineering (EIRP, G/T, rain fade margin) determines system performance. LEO mega-constellations ([LEO Mega-Constellations](/sotf-site/life-frontier/in-orbit/leo-mega-constellations/)) — Starlink, OneWeb, Amazon Kuiper — exploit lower path loss and lower latency (~20 ms vs ~600 ms for GEO) to deliver broadband from low-cost phased-array terminals.

**Optical inter-satellite links (OISL)** use laser beams between satellites to carry high-throughput backbone traffic without going to ground. See [Optical Inter-Satellite Links](/sotf-site/life-frontier/in-orbit/optical-inter-satellite-links/). Starlink's Gen 2 OISL operates at ~100 Gbps per link. Key technical challenge: pointing, acquisition, and tracking (PAT) of a diffraction-limited beam across thousands of km while both platforms vibrate and thermally flex.

**Direct-to-cell** (see [Direct-to-Cell / LEO SOS (Lynk, AST SpaceMobile)](/sotf-site/life-frontier/in-orbit/direct-to-cell-leo/)) eliminates the need for specialised terminals; Starlink, AST SpaceMobile, and others use unmodified 4G/5G handsets as terminals. Regulatory co-ordination with terrestrial mobile networks is the primary constraint.

**Investment relevance:** ground-segment hardware (phased-array antennas, optical terminals, ground-station-as-a-service) and spectrum management are the fundable wedges. Pure satellite manufacturing and launch are dominated by vertically integrated players. Quantum-secured SATCOM (QKD via satellite) is an early-stage opportunity for sovereign-assured communications.

## Frontier

- Can OISLs achieve sufficient pointing stability on low-cost small-sat platforms without deformable mirrors?
- What is the practical data-rate ceiling for direct-to-device LEO broadband without licensed spectrum refarming?
- How does QKD via satellite scale to a commercial service model?

## Companies using

<!-- dataview block stripped for public site -->

## Connected ideas

<!-- dataview block stripped for public site -->

## Sources

<!-- dataview block stripped for public site -->
