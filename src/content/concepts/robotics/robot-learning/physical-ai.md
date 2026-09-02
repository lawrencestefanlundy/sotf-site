---
type: concept
slug: physical-ai
canonical_name: Physical AI (robotics cluster hub)
aliases:
- physical ai
- embodied ai
- embodied intelligence
kind: category
parent_concepts:
- robotics-autonomous-systems
related_concepts:
- humanoid-robots
- vision-language-action-models
- world-models
- sim-to-real-robot-data
- dexterous-manipulation
- tactile-sensing
- robot-actuators
- robot-data-collection
sources:
- '[[2025-04-23-what-if-ai-can-already-feel]]'
- '[[2025-03-26-on-educating-our-children-in-the]]'
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2025-10-21-ceva-launches-wi-fi-7-ip-for-smarter-ai-driven-iot-and-physi]]'
- '[[2025-10-21-ceva-introduces-wi-fi-7-1x1-client-ip-to-power-smarter-more-]]'
- '[[2026-robot-data-supply-funding-wave]]'
- '[[2026-04-20-robot-autonomy-destination-bessemer-venture-partners]]'
- '[[2026-08-06-the-year-ai-science-and-the-physical-ai-industry-came-alive]]'
- '[[2026-04-20-physical-ai-deploys-this-decade-bessemer-predicts-robotics]]'
- '[[2026-07-01-sensifai-memo-streaming-physical-ai]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-06-13-sovereign-electronics-manufacturing-reshoring-digest]]'
- '[[2026-04-27-physical-ai-that-moves-the-world-qasar-younis-peter-ludwig-a]]'
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 4
  timing_band: Soon (2-5yr)
  verdict: Fairly rated
scorecard_status: draft
mention_count: 81
descendants:
- dexterous-manipulation
- humanoid-robots
- robot-actuators
- robot-data-collection
- sim-to-real-robot-data
- tactile-sensing
- vision-language-action-models
- world-models
sources_7d: 5
sources_30d: 12
recent_mentions:
- slug: 2026-08-06-the-year-ai-science-and-the-physical-ai-industry-came-alive
  title: The Year AI Science and the Physical AI Industry Came Alive
  date: '2026-08-06'
  kind: web
- slug: 2026-07-26-humanoid-duty-cycle-thermal-constraint
  title: 'What actually limits a humanoid to minutes: the thermal cliff, not the battery'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-26-unitree-ipo-shipment-and-segment-data
  title: 'Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix'
  date: '2026-07-26'
  kind: web
- slug: 2026-07-01-sensifai-memo-streaming-physical-ai
  title: SensifAI — Purpose-Built Silicon for Streaming Physical AI (funding memo)
  date: '2026-07-01'
  kind: web
- slug: 2026-06-23-semidoped-daily-update
  title: Semi Doped — Daily Update, June 23rd 2026
  date: '2026-06-23'
  kind: web
- slug: 2026-06-15-gf-investor-day-2026
  title: GlobalFoundries Investor Day 2026 (presentation)
  date: '2026-06-15'
  kind: web
- slug: 2026-robot-data-supply-funding-wave
  title: 'Robot data-supply & sensor layer funding wave (2025-26): PitchBook, Encord, PaXini, DAIMON'
  date: '2026-06-13'
  kind: web
- slug: 2026-06-13-sovereign-electronics-manufacturing-reshoring-digest
  title: 'Western/European electronics manufacturing reshoring (PCB/PCBA): market + why-now digest'
  date: '2026-06-13'
  kind: web
neighbors:
- slug: humanoid-robots
  name: Humanoid Robots
  path: /robotics/embodiment/humanoid-robots/
  macro: robotics
- slug: vision-language-action-models
  name: Vision-Language-Action (VLA) Models
  path: /robotics/robot-learning/vision-language-action-models/
  macro: robotics
- slug: world-models
  name: World Models (for robotics & autonomy)
  path: /robotics/robot-learning/world-models/
  macro: robotics
- slug: sim-to-real-robot-data
  name: Sim-to-Real, Robot Simulation & Synthetic Data
  path: /robotics/robot-learning/sim-to-real-robot-data/
  macro: robotics
- slug: dexterous-manipulation
  name: Dexterous Manipulation & Robot Hands
  path: /robotics/embodiment/dexterous-manipulation/
  macro: robotics
- slug: tactile-sensing
  name: Tactile Sensing & Electronic Skin
  path: /robotics/embodiment/tactile-sensing/
  macro: robotics
- slug: robot-actuators
  name: Robot Actuators (the muscle layer)
  path: /robotics/embodiment/robot-actuators/
  macro: robotics
- slug: robot-data-collection
  name: Robot Data Collection (the data-supply stack)
  path: /robotics/robot-learning/robot-data-collection/
  macro: robotics
---
**Physical AI is the umbrella term for AI systems that perceive and act in the physical world through robots, vehicles and wearables, and it is now a real capital and silicon category, though the evidence that it clears production reliability and duty-cycle thresholds is still thin.**

## Summary

"Physical AI" names the stack that connects learned models to actuators: sensors that capture the world (cameras, event cameras, tactile skins, inertial and gaze signals), a learned policy that maps perception plus a language instruction to motor commands, and the compute that has to run that policy on a moving, battery-powered platform. The dominant policy architecture in the current literature is the vision-language-action (VLA) model, and within that the diffusion-based variants, which give the best motion quality and generalisation but must be evaluated at control frequencies of roughly 50-200 Hz, imposing hard latency and energy budgets at the edge. A parallel line of work replaces or augments the reactive policy with a world model: a learned predictive core that compresses observations into states and simulates action-conditioned futures for planning.

The research frontier is currently about the failure modes rather than the demonstrations. VLA perception is fragile at the sensing stage: under 20 lux, an image-only policy scored 0% on a pick-and-place task, rising to 60% when accumulated event-camera maps were simply overlaid on the RGB frames. Neuromorphic sensing is being pushed for the same reason on drones, cars and underwater vehicles, where motion blur and harsh light break frame-based imaging. On the compute side, the work is co-design: exploiting temporal similarity between consecutive control inputs to skip redundant bit-level operations, or, on AR glasses, using gaze, pose and inertial cues to keep only the informative parts of egocentric video for a 27.5x memory and 24.3x energy reduction versus a full-video baseline.

Three parameters decide the category. First, reliability: how much data, and of what kind, is needed to close the gap between lab performance and the roughly 99.9% reliability that production deployment demands, a question one investor thesis explicitly lists as unanswered <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Predicts: Robotics and physical AI" rel="noopener">ref</a></sup>. Second, duty cycle: a Unitree G1 carries a 421.2 Wh pack on a 35 kg body and manages 5 kg payload work for 10-15 minutes continuously, and eight hours at the implied sustained draw would need roughly 13.5 kWh, about 54 kg of cells at 250 Wh/kg <sup class="ref"><a href="https://airobotseidos.com/liquid-cooling-systems-for-humanoid-robots/" title="What actually limits a humanoid to minutes: the thermal cliff, not the battery" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>. Third, where value accrues: the open-source commoditisation of model architecture, with data and deployment layers remaining proprietary, and hardware cost compression pulling margin away from robot OEMs <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Venture Partners: Robotics and Physical AI - Data & Deployment as Defensible Value" rel="noopener">ref</a></sup>.

## Viability (3/5)

The subsystem evidence is real and quantified. Event augmentation lifts a manipulation task from 0% to 60% success at 20 lux; intent-driven perception filtering cuts memory 27.5x and energy 24.3x on glasses while preserving task accuracy; bit-sparsity and speculative inference are proposed specifically because diffusion VLA at 50-200 Hz does not fit edge budgets today. Commercially, hardware ships in volume: 5,215 humanoids and 23,000 quadrupeds in 2025 at roughly 60% gross margin <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>.

What is not demonstrated is the whole loop under production conditions. The reliability gap between demonstration and the 99.9% threshold is named as an open question by an investor with money in the category <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Predicts: Robotics and physical AI" rel="noopener">ref</a></sup>. Duty cycle is arithmetically constrained rather than merely engineering-limited: the battery route to an eight-hour shift does not close at current or near-term cell energy density <sup class="ref"><a href="https://airobotseidos.com/liquid-cooling-systems-for-humanoid-robots/" title="What actually limits a humanoid to minutes: the thermal cliff, not the battery" rel="noopener">ref</a></sup>. And the reference industrial deployment of the volume leader's own embodied model is joint-motor assembly inside Unitree's own factory, a controlled environment reporting explicitly separates from real industrial conditions <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>. Credible, contested, not yet proven.

**TLDR: Components demonstrably work; the integrated system has not been shown to clear production reliability or shift-length duty cycles.**

## Drivers (4/5)

Demand is the thin half. The only disclosed end-customer breakdown in these sources shows over 70% of humanoids sold going to research and education and roughly 17% to commercial and consumer buyers, characterised as bought largely for show: retail promotion, tourist sites, performances <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>. Quadrupeds carry the genuine industrial base in power-grid, tunnel and pipeline inspection; humanoids do not yet. Q1 2026 revenue grew 68.5% year on year while net profit fell about 52%, which is consistent with a market being bought into rather than pulled <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>.

**TLDR: Supply-side push is strong and documented: record capital, collapsing sensor costs, foundry roadmaps rebuilt around the term; end demand is the weak side.**

## Novelty (3/5)

The comparison class is task-specific programmed automation and reactive control. VLA models are described as generalising to open-ended manipulation, and world models add planning beyond reactive control by simulating action-conditioned futures. That is a different kind of system, not an incremental one. Where the sources give magnitudes, they are large but narrow: 0% to 60% success on one task at one illumination level; 27.5x memory and 24.3x energy on egocentric video understanding against a full-video baseline; a 500-fold tactile sensor cost reduction **2026 Robot Data Supply Funding Wave**. Notably, the event-fusion win came from a parameter-free overlay, which suggests the current models leave easy robustness on the table rather than that the fusion method is deep.

Against that, the architecture itself is expected to stop being the differentiator: open source is predicted to commoditise model architecture, leaving data and deployment as the defensible layers, while hardware cost compression erodes OEM margin <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Venture Partners: Robotics and Physical AI - Data & Deployment as Defensible Value" rel="noopener">ref</a></sup>. On that view the novelty that persists is in datasets, evaluation and the sensing and compute components, not in the policy family.

**TLDR: Learned VLA and world-model policies are a genuine break from programmed automation, but the specific gains in the sources are point improvements and the architecture layer is commoditising.**

## Diffusion (2/5)

Reliability first: nobody in these sources claims to know how much more data, or which kinds, is required to move from lab performance to the 99.9% level production demands <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Predicts: Robotics and physical AI" rel="noopener">ref</a></sup>. Duty cycle second: 10-15 minutes of continuous 5 kg payload work is not a labour substitute, and the battery route to a shift is closed by mass arithmetic, pushing the problem onto thermal management and average power draw instead <sup class="ref"><a href="https://airobotseidos.com/liquid-cooling-systems-for-humanoid-robots/" title="What actually limits a humanoid to minutes: the thermal cliff, not the battery" rel="noopener">ref</a></sup>. Third, compute: diffusion VLA is compute-intensive at the control frequencies required, and the proposed fixes are custom accelerators with bit-serial datapaths, meaning deployment depends on silicon that is not yet in the field.

Fourth, and least discussed commercially, is security. Once a predictive layer sits between sensors and actuators, poisoning, backdoors, sensor spoofing, prompt injection and supply-chain attacks can propagate into physical action, and a compromised or over-trusted world model can generate what the survey calls predictive safety illusions while appearing to act as a safety shield. In regulated industrial and domestic settings that becomes a certification problem, not just an engineering one. The observed adoption pattern matches these barriers: inspection quadrupeds in the field, humanoids in labs and showrooms <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>.

**TLDR: Four independent barriers, each documented: reliability, duty cycle, edge inference budget and a new physical-action security surface.**

## Impact (4/5)

The breadth is visible in the sources rather than asserted: mining rigs, drones, trucks and warships in one operator's account of the category <sup class="ref"><a href="https://www.latent.space/p/appliedintuition" title="Physical AI that Moves the World — Qasar Younis & Peter Ludwig, Applied Intuition" rel="noopener">ref</a></sup>, household service robotics as a funded research programme, AR glasses as an embodied-intelligence platform in its own right, and inspection work already running on quadrupeds in power grids, tunnels and pipelines <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>. A specialty foundry has reorganised its public strategy around the sense / think / act / communicate stack and attaches a 39bn-plus connected-device figure by 2030 to the edge memory requirement alone <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>.

The qualifier is distribution rather than size. The same analysis that expects large value expects it to land in data, evaluation and world-model flywheels plus the component layer, not in robot OEMs facing hardware cost compression or in standalone foundation models commoditised by open releases <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Venture Partners: Robotics and Physical AI - Data & Deployment as Defensible Value" rel="noopener">ref</a></sup>. So the value at stake is high; the identity of the beneficiaries is contested, and the sources support a real risk that today's most visible players capture little of it.

**TLDR: If reliability and duty cycle are solved, the addressable surface spans manufacturing, logistics, vehicles, defence and the home, and the semiconductor layer is already sizing it.**

## Timing Soon (2-5yr)

Two clocks run at different speeds. The component and narrow-application clock is already at zero: quadrupeds are sold into industrial inspection at scale <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>, tactile sensing costs have collapsed **2026 Robot Data Supply Funding Wave**, and edge silicon roadmaps for always-on sensing are being marketed today <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://news.google.com/rss/articles/CBMijwJBVV95cUxOZkl3MHJ4d3lzSVpHalRDMGRNM3dEdUZ4RHlBZ1d5NkpOM2paUzYyOUtHRHhIUFNsaDh0Z0xYbWg3ckd6TGw0NVQ0Um9HVkJROWVleG1VV1E0bEE1YXJYMEM5VlB2S0ZNaVFpQXRMc2RhaVBYVEIxaUVCakpjRFhWVHhKbnBjZTl0UWhSd3lkOTREWi1VSmVfcGxsd1UtUnVMVWZmX0hmR1hMYy11ZzRWWllzQmV3YUhhSVc5OGVjZldzMnRPcklZNjYwSVVUaVFyczl0Y19YSndISTdENVVFMlRKbElFQnlRU25HRUZBY1oxQXZqWGh6djVSdnZXcnFpbWptdGtTTG5xd1NsTnZR?oc=5" title="Ceva Introduces Wi-Fi 7 1x1 Client IP to Power Smarter, More Responsive AI-Enabled IoT Devices and Emerging Physical AI " rel="noopener">ref</a></sup>. Expect steady, unglamorous revenue there over the next two years.

The general-purpose clock is slower and its length is genuinely unknown, because the data required to reach production reliability has not been quantified by anyone in these sources <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Predicts: Robotics and physical AI" rel="noopener">ref</a></sup>. Unitree plans roughly 20,000 humanoid units in 2026, about four times 2025 <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>, which will produce a large fleet and therefore a large amount of real-world data, but at present the mix is research, education and display rather than production work. The thermal and duty-cycle constraint sets a floor on how quickly humanoids can substitute for a shift of labour regardless of policy quality <sup class="ref"><a href="https://airobotseidos.com/liquid-cooling-systems-for-humanoid-robots/" title="What actually limits a humanoid to minutes: the thermal cliff, not the battery" rel="noopener">ref</a></sup>. Two to five years for the first credible non-demonstration industrial deployments at volume; longer for the household case.

**TLDR: Narrow deployments (inspection quadrupeds, egocentric wearables, edge sensing silicon) are live now; general manipulation labour substitution is gated by unresolved reliability and duty-cycle limits.**

## Overrated or underrated? Fairly rated

The category is real, funded and already shipping in narrow forms, so dismissing it is wrong. But the internal pricing is skewed. The evidence that survives scrutiny sits in the unglamorous layers: sensing components with collapsing costs, data engines, edge inference silicon, and inspection-class platforms with genuine industrial customers **2026 Robot Data Supply Funding Wave** <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>. The evidence for the humanoid centrepiece that carries most of the narrative is weak on demand quality (over 70% of units to research and education, roughly 17% commercial and consumer bought largely for show) and hard-constrained on duty cycle <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://airobotseidos.com/liquid-cooling-systems-for-humanoid-robots/" title="What actually limits a humanoid to minutes: the thermal cliff, not the battery" rel="noopener">ref</a></sup>.

So the honest position is that the aggregate label is fairly rated while the allocation within it is not. The thesis that data and deployment stay defensible and OEM margin compresses <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Venture Partners: Robotics and Physical AI - Data & Deployment as Defensible Value" rel="noopener">ref</a></sup> is the one to test, and Unitree's roughly 60% gross margin with falling net profit is an early datapoint on which side of it hardware sits <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>. Also underweighted relative to its severity: the security surface created by putting a learned predictive layer in the actuation path.

## Prediction

By the end of 2027, no disclosed customer-mix breakdown from a volume humanoid vendor will show a majority of units going to production industrial or commercial work rather than research, education, display or pilot use (2025 baseline: over 70% research and education, roughly 17% commercial and consumer, largely for show) <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>.

## Evidence base

- 2025 robotics and physical-AI funding reached a record $27.6bn across roughly 1,009 deals, about twice 2024, per PitchBook; Encord raised $60M Series C at roughly $550M valuation and PaXini $145M at over $1.4bn having cut tactile sensor cost from ¥100,000 to ¥199 **2026 Robot Data Supply Funding Wave**
- Unitree's 2025 disclosures: RMB 1.71bn revenue, 5,215 humanoids at roughly $23,100 ASP and 23,000 quadrupeds, about 60% gross margin, but over 70% of humanoids to research and education and roughly 17% commercial or consumer bought largely for show; Q1 2026 revenue up 68.5% with net profit down about 52% <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>
- A G1 carries 421.2 Wh on a 35 kg body and does 5 kg payload work for 10-15 minutes continuously; eight hours at the implied draw needs roughly 13.5 kWh, about 54 kg of cells at 250 Wh/kg, closing the battery route to a full shift <sup class="ref"><a href="https://airobotseidos.com/liquid-cooling-systems-for-humanoid-robots/" title="What actually limits a humanoid to minutes: the thermal cliff, not the battery" rel="noopener">ref</a></sup>
- Event-camera augmentation raised pick-and-place success at 20 lux from 0% (image-only) to 60% using a parameter-free overlay of accumulated event maps, quantifying how fragile VLA perception is at the sensing stage 
- Diffusion-based VLA models must run at 50-200 Hz and do not fit edge latency and energy budgets without algorithm-hardware co-design such as temporal bit-sparsity and speculative inference 
- An investor thesis dated 20 April 2026 names two unanswered questions, how much more data and of what kinds are needed to close the lab-to-99.9%-reliability gap, while predicting open source commoditises model architecture and hardware cost compression shifts value away from OEMs <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Predicts: Robotics and physical AI" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Venture Partners: Robotics and Physical AI - Data & Deployment as Defensible Value" rel="noopener">ref</a></sup>
- GlobalFoundries structured its 2026 investor day around Physical AI (sense / think / act / communicate), citing 39bn-plus connected IoT devices by 2030 virtually all requiring embedded non-volatile memory <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>

## Open questions

- How many hours of what kind of data are actually needed to move a VLA policy from demonstration success to the 99.9% reliability production requires, and does that curve flatten or keep costing linearly?
- Does the duty-cycle problem yield to thermal management and lower average power draw, as the liquid-cooling argument implies, or does it hard-cap humanoid labour substitution regardless of policy quality?
- Do diffusion VLA accelerators exploiting temporal bit-sparsity reach commercial silicon, and at what power, given the 50-200 Hz control requirement?
- Does any pure robot OEM or standalone robot-foundation-model company sustain above 40% gross margin at scale without owning a proprietary data flywheel or component moat?

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
