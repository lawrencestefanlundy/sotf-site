---
type: concept
slug: radiative-cooling
canonical_name: Radiative Cooling
aliases: []
parent_concepts:
- thermal-management
- energy-power
related_concepts: []
sources:
- '[[2026-06-23-semianalysis-space-datacenters]]'
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 5
frontier:
- What net cooling power (W/m²) and sub-ambient temperature drop do silica microsphere photonic glass coatings sustain over multi-season outdoor exposure, and how much does soiling degrade them?
- Does the diameter-insensitivity result extend below 2 µm and above 8 µm, and what minimum optical thickness is required to enter the diffusive regime at each diameter?
- Can the eight-layer cool-window stack be deposited over architectural-scale glass at a cost per m² competitive with existing low-emissivity coatings, and does it survive standard glazing durability tests?
- What radiator area, mass and $/kW does a megawatt-class orbital data centre require, and does that figure close the 4.4x 2026 cost gap between space and terrestrial compute 2026 06 23 semianalysis space datacenters?
sources_7d: 0
sources_30d: 0
recent_mentions:
- slug: 2026-09-03-space-compute-cheap-launch-rebuild
  title: Space compute rebuilt around the cheap-launch case — what survives the premise
  date: '2026-09-03'
  kind: web
- slug: 2026-06-23-semianalysis-space-datacenters
  title: 'To Boldly Go: The Case for Space Datacenters'
  date: '2026-06-23'
  kind: web
neighbors: []
---
## Physics / mechanism

Radiative cooling exploits thermal emission to move heat from a surface to a cold sink without pumps, compressors or working fluids. Two distinct engineering problems appear in the sources. The first is passive daytime radiative cooling at the Earth's surface, where a coating must reject incoming solar energy while emitting its own thermal radiation to the sky. The second is heat rejection in vacuum, where radiation is the only available transport mechanism and the design variable is radiator area and mass.

For terrestrial coatings, one implementation is a disordered "photonic glass": an optically thick, randomly packed layer of silica microspheres that scatters solar wavelengths strongly while the silica itself provides infrared emission. Once the coating is thick enough to operate deep in the multiple-scattering (diffusive) regime, both the spectral response and the net cooling performance become insensitive to microsphere diameter across 2 to 8 µm, despite measurable differences in the microscopic scattering properties. This weakens the usual assumption that particle-size optimisation is the critical design parameter and shifts the emphasis to layer thickness, packing and surface functionalisation.

The related solar-rejection problem for glazing is spectral rather than diffusive. Because more than 70% of incident solar energy lies below 1000 nm, useful cooling requires abrupt transitions from transparent to reflecting at both edges of the visible band, which conventionally implies tens of dielectric layers. An eight-layer planar stack has been demonstrated with sharp reflectance changes near 390 and 680 nm, giving above 70% visible transmittance with above 80% near-infrared and above 60% ultraviolet rejection.

In vacuum the constraint inverts: emissivity is easy, area is expensive. The ISS radiator system rejects only about 70 kW using roughly 325 m² of hardware at a reported $340-500M, which sets the scale of the area, mass and cost burden for any megawatt-to-gigawatt orbital compute platform <sup class="ref"><a href="https://newsletter.semianalysis.com/p/to-boldly-go-the-case-for-space-datacenters" title="To Boldly Go: The Case for Space Datacenters" rel="noopener">ref</a></sup>. Separately, plasma physics uses "radiative cooling" for a different mechanism, in which radiation losses are dynamically significant enough to alter magnetic reconnection and particle acceleration; that regime is a research topic rather than a thermal-management technology.

## Competitive landscape

| Approach | Sink | Key metric in sources | Status |
|---|---|---|---|
| Silica microsphere paint | Sky | Cooling robust to 2-8 µm particle diameter in diffusive regime | Outdoor measurement, scalable disordered coating |
| Multilayer solar-rejecting glazing | Reduced heat gain rather than net emission | >70% visible, >80% NIR and >60% UV rejection in 8 layers | Lab-realised structure |
| Space radiators | Vacuum | ~70 kW per ~325 m², $340-500M for the ISS system <sup class="ref"><a href="https://newsletter.semianalysis.com/p/to-boldly-go-the-case-for-space-datacenters" title="To Boldly Go: The Case for Space Datacenters" rel="noopener">ref</a></sup> | Flight-proven but area- and cost-limited |

Paints and glazings are complementary parts of a building envelope, not direct substitutes: the coating provides net radiative heat rejection from opaque surfaces, while the window stack suppresses solar gain through the transparent aperture. The vacuum case is a separate market where radiative cooling has no alternative, and where the sources treat thermal as the largest structural constraint on orbital data centres <sup class="ref"><a href="https://newsletter.semianalysis.com/p/to-boldly-go-the-case-for-space-datacenters" title="To Boldly Go: The Case for Space Datacenters" rel="noopener">ref</a></sup>.

## Evidence base

- Disordered silica microsphere coatings of 2-8 µm diameter give spectral response and net cooling that are robust to particle diameter once operating deep in the diffusive regime; outdoor thermal measurements were used to establish this, 2 June 2026.
- An eight-layer planar stack achieved sharp reflectance transitions at ~390 and ~680 nm with >70% visible transmittance, >80% near-infrared and >60% ultraviolet rejection, 4 May 2026.
- More than 70% of incident solar energy lies at wavelengths shorter than 1000 nm, which is why abrupt multi-wavelength spectral transitions are required for cool windows.
- The ISS radiator system removes about 70 kW using roughly 325 m² at $340-500M, cited as evidence that thermal management is the dominant structural constraint on megawatt-to-gigawatt orbital compute, 23 June 2026 <sup class="ref"><a href="https://newsletter.semianalysis.com/p/to-boldly-go-the-case-for-space-datacenters" title="To Boldly Go: The Case for Space Datacenters" rel="noopener">ref</a></sup>.
- Orbital data centre proposals under active capital formation include a SpaceX FCC filing of 30 January 2026 for up to 1,000,000 satellites at 500-2,000 km sun-synchronous orbits, all of which require radiative heat rejection.
- NSF funded a $300,000 study of magnetic reconnection mediated by radiative cooling, starting 1 August 2026, addressing regimes where radiation losses are dynamically significant.

## Frontier (open questions)

- What net cooling power (W/m²) and sub-ambient temperature drop do silica microsphere photonic glass coatings sustain over multi-season outdoor exposure, and how much does soiling degrade them?
- Does the diameter-insensitivity result extend below 2 µm and above 8 µm, and what minimum optical thickness is required to enter the diffusive regime at each diameter?
- Can the eight-layer cool-window stack be deposited over architectural-scale glass at a cost per m² competitive with existing low-emissivity coatings, and does it survive standard glazing durability tests?
- What radiator area, mass and $/kW does a megawatt-class orbital data centre require, and does that figure close the 4.4x 2026 cost gap between space and terrestrial compute <sup class="ref"><a href="https://newsletter.semianalysis.com/p/to-boldly-go-the-case-for-space-datacenters" title="To Boldly Go: The Case for Space Datacenters" rel="noopener">ref</a></sup>?

*Synthesised 2026-08-31 from 6 KB sources by the resynth pipeline; citations are KB source slugs.*
