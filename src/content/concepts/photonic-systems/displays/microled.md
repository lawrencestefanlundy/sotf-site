---
type: concept
slug: microled
canonical_name: MicroLED microdisplays
aliases:
- micro-LED
- µLED
- uLED
- microLED
- micro LED
- monolithic RGB microLED
parent_concepts:
- emissive-display
related_concepts:
- emissive-display
- waveguides
- gallium-nitride
sources:
- '[[2025-12-09-gallium-nitride-photonics-w-james]]'
- '[[2026-07-10-the-next-vc-meme-is]]'
- '[[2026-06-15-barry-silverstein-rochester-cxr]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2026-06-01-ai-glasses-display-timing-jbd-introduces-roadrunner-ii-full]]'
- '[[2026-04-07-ai-glasses-display-timing-two-key-breakthroughs-advance]]'
- '[[2026-05-15-ai-glasses-display-timing-jbd-leaps-into-12-inch-wafer]]'
scorecard:
  viability: 3
  drivers: 3
  novelty: null
  diffusion: 3
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 30
sources_7d: 0
sources_30d: 1
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-10-the-next-vc-meme-is
  title: The Next VC Meme Is...
  date: '2026-07-10'
  kind: substack
- slug: 2026-06-15-barry-silverstein-rochester-cxr
  title: University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality
  date: '2026-06-15'
  kind: web
- slug: 2026-06-01-ai-glasses-display-timing-jbd-introduces-roadrunner-ii-full
  title: JBD introduces Roadrunner II full-color microLED projector and AR glasses kit
  date: '2026-06-01'
  kind: web
- slug: 2026-05-15-ai-glasses-display-timing-jbd-leaps-into-12-inch-wafer
  title: JBD Leaps Into 12-Inch-Wafer MicroLED Manufacturing
  date: '2026-05-15'
  kind: web
- slug: 2026-04-07-ai-glasses-display-timing-two-key-breakthroughs-advance
  title: Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays
  date: '2026-04-07'
  kind: web
- slug: 2025-12-09-gallium-nitride-photonics-w-james
  title: Gallium Nitride + Photonics w/ James Lee of Wave Photonics
  date: '2025-12-09'
  kind: substack
neighbors:
- slug: emissive-display
  name: Emissive vs modulated display architectures
  path: /photonic-systems/displays/emissive-display/
  macro: photonic-systems
- slug: waveguides
  name: Waveguides
  path: /photonic-systems/pic-platforms/waveguides/
  macro: photonic-systems
- slug: gallium-nitride
  name: Gallium Nitride
  path: /energy-power/power-electronics/gallium-nitride/
  macro: energy-power
---
**MicroLED microdisplays are arrays of inorganic GaN light emitters at micron-scale pitch bonded to silicon drive circuits, and they are the leading candidate light engine for waveguide-based AR glasses, with full-colour versions forecast to reach mature commercialisation in 2027-2028 <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>.**

## Summary

A microLED microdisplay (often called LEDoS, LED-on-silicon) is a dense two-dimensional array of inorganic light-emitting diodes, typically grown in gallium nitride, driven by a silicon CMOS backplane. Unlike a liquid-crystal-on-silicon (LCoS) panel, which modulates light from a separate illuminator, each pixel emits its own light. That matters for augmented reality: in a glasses form factor the light engine has to push an image through a diffractive or holographic waveguide that throws away most of the photons, so the panel needs extreme brightness from a package measured in cubic millimetres. The competing engine families in this niche are LCoS and laser scanning, all three of which sat inside the same remit at Meta Reality Labs, described as "the world's smallest and most efficient visual imaging systems" <sup class="ref"><a href="https://www.rochester.edu/newscenter/barry-silverstein-leads-center-for-extended-reality-682222/" title="University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality" rel="noopener">ref</a></sup>.

The hard parts are pixel pitch, full colour and yield. JBD's Roadrunner II, introduced in June 2026, is a full-colour microLED projector at 2.5 micron pixel pitch shipped with a monocular AR glasses development kit <sup class="ref"><a href="https://www.microled-info.com/jbd-starts-construct-second-phase-its-hefei-microled-microdisplay-fab" title="JBD introduces Roadrunner II full-color microLED projector and AR glasses kit" rel="noopener">ref</a></sup>. Full colour is the specific bottleneck the industry has been working through: TrendForce points to two enabling breakthroughs and forecasts full-colour LEDoS entering mature commercialisation between 2027 and 2028 <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>. On the manufacturing side, JBD completed an upgrade to a 12-inch reconstructed wafer platform in May 2026, framed as a step change in manufacturing efficiency and cost competitiveness for mass-production readiness <sup class="ref"><a href="https://www.prnewswire.com/news-releases/jbd-leaps-into-12-inch-wafer-microled-manufacturing-302773198.html" title="JBD Leaps Into 12-Inch-Wafer MicroLED Manufacturing" rel="noopener">ref</a></sup>.

The deciding parameters are therefore lumens per watt at the eye after waveguide losses, panel yield at micron pitch across a full wafer, and the cost of full-colour integration. A second, adjacent research thread treats micro-LEDs as communication emitters rather than display pixels: cubic GaN lacks the spontaneous internal polarisation of the conventional hexagonal phase and so promises higher modulation speed for short-range optical links, though c-GaN is metastable and its selective-area growth in silicon inverted pyramids is still being characterised at the TEM level.

For a reader meeting this for the first time: the physics is not in doubt, the devices exist and are being sampled, and the open question is entirely industrial economics plus whether laser-based engines leapfrog the category before it reaches volume.

## Viability (3/5)

There is a working full-colour part in the field: a 2.5 micron pitch projector plus a monocular AR development kit, characterised by the source as demonstrating commercial viability of a HUD-class display product <sup class="ref"><a href="https://www.microled-info.com/jbd-starts-construct-second-phase-its-hefei-microled-microdisplay-fab" title="JBD introduces Roadrunner II full-color microLED projector and AR glasses kit" rel="noopener">ref</a></sup>. That is a real device, not a lab curiosity. Manufacturing has also moved: a 12-inch reconstructed wafer platform completed in May 2026 is presented as delivering mass-production readiness <sup class="ref"><a href="https://www.prnewswire.com/news-releases/jbd-leaps-into-12-inch-wafer-microled-manufacturing-302773198.html" title="JBD Leaps Into 12-Inch-Wafer MicroLED Manufacturing" rel="noopener">ref</a></sup>.

What is missing from the sources is the number that decides the technology. No measured lumens-per-watt figure and no yield figure appear anywhere in the supplied material, even though that is the indicator these evidence items were gathered against. The forecast that full-colour LEDoS reaches mature commercialisation only in 2027-2028 is itself an admission that today's parts are not yet manufacturable at target cost and performance <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>. A 3 is the honest score: credible, demonstrated at device level, unproven at volume.

**TLDR: Full-colour devices exist and are sampling; mass-production readiness is asserted, not yet demonstrated in volume.**

## Drivers (3/5)

Demand: the stated driver is AR smart glasses. TrendForce couples its 2027-2028 full-colour commercialisation forecast to strong growth in AR smart glasses demand <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>, and the whole set of evidence items here was collected against a question of when AI glasses displays arrive, implying the display engine is the gating component rather than a nice-to-have. The shipment of a monocular AR glasses development kit alongside the projector is a supplier acting on expected OEM design-in activity <sup class="ref"><a href="https://www.microled-info.com/jbd-starts-construct-second-phase-its-hefei-microled-microdisplay-fab" title="JBD introduces Roadrunner II full-color microLED projector and AR glasses kit" rel="noopener">ref</a></sup>.

**TLDR: Demand pull from AR smart glasses is explicit; supply-side capacity investment is real but concentrated in few players.**

## Novelty (unscored)

The comparison set is identified: microLED, LCoS and laser scanning engines were all in scope for the same next-generation AR display remit <sup class="ref"><a href="https://www.rochester.edu/newscenter/barry-silverstein-leads-center-for-extended-reality-682222/" title="University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality" rel="noopener">ref</a></sup>. The sources do not provide a single side-by-side figure, no efficiency, brightness, contrast or volume comparison, so there is no basis here for judging how much better microLED is than LCoS or laser scanning, or in which parameter.

Worse for a confident score, the supplied material contains a credible dissent: the former Meta optics and display CTO's public position is that next-generation displays move to laser-based engines, and he is associated with a laser working group <sup class="ref"><a href="https://www.rochester.edu/newscenter/barry-silverstein-leads-center-for-extended-reality-682222/" title="University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality" rel="noopener">ref</a></sup>. There is a genuine architectural argument running against microLED from someone who ran the programme covering all three options. On the communication-emitter side, cubic GaN is said to promise increased speed over hexagonal GaN, but again with no quantified figure and with the material's metastability and contradictory prior growth reports acknowledged. Scoring novelty from this would be invention rather than assessment.

**TLDR: The sources name the alternatives but never quantify microLED's advantage over them.**

## Diffusion (3/5)

The route to adoption is visible. A projector plus reference glasses kit is the standard mechanism for pulling OEM designs in, and it exists now <sup class="ref"><a href="https://www.microled-info.com/jbd-starts-construct-second-phase-its-hefei-microled-microdisplay-fab" title="JBD introduces Roadrunner II full-color microLED projector and AR glasses kit" rel="noopener">ref</a></sup>. Moving to a 12-inch reconstructed wafer platform is the kind of change that shifts cost per die rather than merely improving specification, and it is explicitly framed as targeting cost competitiveness for mass production <sup class="ref"><a href="https://www.prnewswire.com/news-releases/jbd-leaps-into-12-inch-wafer-microled-manufacturing-302773198.html" title="JBD Leaps Into 12-Inch-Wafer MicroLED Manufacturing" rel="noopener">ref</a></sup>.

The barriers are three. First, full colour is not yet mature by the supplier ecosystem's own account, with maturity dated to 2027-2028 <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>. Second, the microdisplay is only one element of a system that also needs waveguides, whether volume holography, polarisation volume holograms or surface relief gratings, plus novel high-index lightweight materials <sup class="ref"><a href="https://www.rochester.edu/newscenter/barry-silverstein-leads-center-for-extended-reality-682222/" title="University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality" rel="noopener">ref</a></sup>; a good panel into a lossy waveguide still gives a poor product, so adoption is coupled to a second immature supply chain. Third, architectural risk: if OEMs believe the laser-engine thesis, microLED panel design-ins may not convert into volume programmes.

**TLDR: Development kits and 12-inch capacity lower the barrier, but adoption depends on a full-colour cost and yield curve nobody has published.**

## Impact (3/5)

If full-colour microLED microdisplays reach the required efficiency and yield, they unlock the display layer of AR smart glasses, a category the sources treat as demand-ready and awaiting the light engine <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>. The evidence trail assembled here exists precisely because display timing is the pacing item for AI glasses. A secondary impact channel is non-display: micro-LEDs as high-speed emitters for short-range optical communication, where cubic GaN's lack of spontaneous polarisation is expected to raise modulation speed. That gives the underlying device platform a second market if the display race is lost.

The score is capped at 3 because the sources contain no market sizing, no unit forecasts and no revenue figures. The judgement rests on position in the value chain, which is defensible, rather than on measured value, which is absent. Anyone modelling this should treat the impact number as a structural argument, not an estimate.

**TLDR: It is the gating component for consumer AR glasses, but the sources never size the prize.**

## Timing Soon (2-5yr)

Full-colour parts and AR development kits are available in 2026 <sup class="ref"><a href="https://www.microled-info.com/jbd-starts-construct-second-phase-its-hefei-microled-microdisplay-fab" title="JBD introduces Roadrunner II full-color microLED projector and AR glasses kit" rel="noopener">ref</a></sup>, and the manufacturing platform intended to support volume was completed in May 2026 <sup class="ref"><a href="https://www.prnewswire.com/news-releases/jbd-leaps-into-12-inch-wafer-microled-manufacturing-302773198.html" title="JBD Leaps Into 12-Inch-Wafer MicroLED Manufacturing" rel="noopener">ref</a></sup>. The industry's own date for mature full-colour LEDoS commercialisation is 2027-2028 <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>.

The reason to sit in the 2-5 year band rather than 0-2 is the gap between a supplier declaring mass-production readiness and a consumer OEM shipping volume with acceptable yield, cost and eye-brightness. Materials work that could reset the device stack, such as cubic GaN epitaxy, is still at the cross-sectional TEM stage with contradictory prior literature, so the higher-performance variants belong to a later window than the first commercial products.

**TLDR: HUD-class and development hardware now; full-colour maturity forecast 2027-2028, with volume consumer programmes plausibly after that.**

## Overrated or underrated? Fairly rated

The consensus position, that microLED microdisplays are the front-runner light engine for AR glasses and are roughly two years from full-colour maturity, is what the sources actually support. There is a shipping full-colour part at 2.5 micron pitch, a 12-inch manufacturing platform, and a dated commercialisation forecast <sup class="ref"><a href="https://www.microled-info.com/jbd-starts-construct-second-phase-its-hefei-microled-microdisplay-fab" title="JBD introduces Roadrunner II full-color microLED projector and AR glasses kit" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.prnewswire.com/news-releases/jbd-leaps-into-12-inch-wafer-microled-manufacturing-302773198.html" title="JBD Leaps Into 12-Inch-Wafer MicroLED Manufacturing" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>. That is neither hype nor a neglected opportunity; it is a technology executing roughly on the schedule the market expects.

The one thing that could make it overrated is the laser thesis. The person who ran µLED, LCoS and laser scanning programmes at Meta Reality Labs for around seven years now publicly argues that next-generation displays move to laser-based engines <sup class="ref"><a href="https://www.rochester.edu/newscenter/barry-silverstein-leads-center-for-extended-reality-682222/" title="University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality" rel="noopener">ref</a></sup>. That is not decisive, but it is the strongest available signal against the category, and it is not reflected in the enthusiasm around LEDoS capacity announcements. Investors should treat microLED as the base case with a live architectural substitution risk, and should demand the two numbers the public record does not contain: measured lumens per watt at the eye, and panel yield at micron pitch.

## Prediction

By 31 December 2028, at least one volume consumer AR glasses product will ship with a full-colour microLED (LEDoS) light engine, consistent with the 2027-2028 mature-commercialisation forecast <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>.

## Evidence base

- 2026-04-07: TrendForce forecasts full-colour LEDoS devices entering mature commercialisation between 2027 and 2028, tied to strong growth in AR smart glasses demand <sup class="ref"><a href="https://www.trendforce.com/news/2026/04/07/news-two-key-breakthroughs-advance-full-color-micro-led-microdisplays/" title="Two Key Breakthroughs Advance Full-Color Micro LED Microdisplays" rel="noopener">ref</a></sup>.
- 2026-05-15: JBD completed an upgrade to a 12-inch reconstructed wafer platform, described as a step change in manufacturing efficiency and cost competitiveness for mass-production readiness <sup class="ref"><a href="https://www.prnewswire.com/news-releases/jbd-leaps-into-12-inch-wafer-microled-manufacturing-302773198.html" title="JBD Leaps Into 12-Inch-Wafer MicroLED Manufacturing" rel="noopener">ref</a></sup>.
- 2026-06-01: JBD introduced Roadrunner II, a 2.5 micron full-colour microLED projector, with a monocular AR glasses development kit <sup class="ref"><a href="https://www.microled-info.com/jbd-starts-construct-second-phase-its-hefei-microled-microdisplay-fab" title="JBD introduces Roadrunner II full-color microLED projector and AR glasses kit" rel="noopener">ref</a></sup>.
- 2026-06-15: Barry Silverstein, previously Senior Director and CTO of Optics and Display at Meta Reality Labs with a remit covering µLED, LCoS and laser scanning engines plus waveguide technologies, joined the University of Rochester in January 2026 to direct a new Center for Extended Reality; his public position is that next-generation displays move to laser-based engines <sup class="ref"><a href="https://www.rochester.edu/newscenter/barry-silverstein-leads-center-for-extended-reality-682222/" title="University of Rochester hires former Meta exec Barry Silverstein to direct Center for Extended Reality" rel="noopener">ref</a></sup>.
- 2026-07-01: Selective-area OMVPE growth study finds polarity is critical to cubic GaN growth in silicon inverted pyramids; c-GaN is metastable and prior reports contradictory, but its lack of spontaneous internal polarisation promises higher speed than hexagonal GaN for micro-LED short-range communication.

## Open questions

- What is the actual full-colour light-engine efficiency in lumens per watt at the eye after waveguide losses, and what is panel yield at 2.5 micron pitch on the 12-inch reconstructed wafer platform?
- Does the laser-engine argument advanced by the former Meta optics and display CTO win any major OEM design, and on what performance grounds?
- Beyond the single supplier visible in these sources, is there a credible second source for full-colour microLED microdisplays that a consumer OEM would accept?
- Can cubic GaN growth be made reproducible in inverted-pyramid templates at device scale, and does the predicted speed advantage over hexagonal GaN materialise in measured modulation bandwidth?

---
*Assessment drafted 2026-08-31 from up to 10 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
