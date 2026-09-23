---
type: concept
slug: hamr
canonical_name: Hamr
aliases: []
parent_concepts:
- mainstream-memory
- memory
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 2
frontier:
- What write energy, switching time and cycle endurance does Joule-heated HAMR in intercalated 2D magnets achieve relative to laser-plus-plasmonic-transducer HAMR in shipping drives?
- Can electrically heated HAMR bits be scaled to the areal densities and bit pitches required by hard-disk or embedded memory roadmaps, and at what thermal crosstalk penalty to neighbouring bits?
- Does the quantum diamond microscope imaging of patterned FeRh demonstrate reversible, addressable AFM-to-FM bit writing, or only static contrast between phases?
- How much lower, quantitatively, is the FeRh write temperature than incumbent HAMR media, and does that translate into a measured increase in head lifetime?
sources_7d: 0
sources_30d: 0
recent_mentions: []
neighbors: []
---
## Physics / mechanism

In the mainstream implementation, the heat is delivered optically: a laser and a plasmonic transducer concentrate energy into a sub-diffraction spot on the disk surface. This optical delivery chain is what confines HAMR largely to hard-disk drives and makes it difficult to integrate with on-chip or embedded memory architectures.

Two research directions attempt to change the heating and switching physics. The first replaces laser heating with Joule heating in an intercalated two-dimensional magnet, giving an electrically controlled variant of HAMR that does not require optics or a plasmonic near-field transducer. The second targets the medium itself: iron-rhodium (FeRh) has a first-order phase transition near room temperature between antiferromagnetic and ferromagnetic phases, which makes the write temperature lower and the transition sharper than in alternative materials.

The relevant design parameters follow from this: the write temperature and the sharpness of the thermal transition set the thermal engineering budget of the head and medium, and lower write temperatures are argued to extend write/read head lifetime.

## Competitive landscape

Within magnetic recording, HAMR is described as the leading solution to the trilemma relative to conventional bit-size scaling. The competition is therefore mostly internal to HAMR: optical/plasmonic heating, which is the deployed form but is tied to hard-disk drives, versus electrically driven Joule heating, which is being explored specifically to make heat-assisted writing compatible with on-chip and embedded memory. On the media side, FeRh competes with other high-anisotropy HAMR media on write temperature and transition sharpness rather than on areal density directly, but antiferromagnet-based magnetic memory using FeRh has not yet been realised despite considerable effort.

## Evidence base

## Frontier (open questions)

*Synthesised 2026-08-31 from 2 KB sources by the resynth pipeline; citations are KB source slugs.*
