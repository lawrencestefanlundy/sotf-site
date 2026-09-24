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
- '[[2026-04-28-making-ai-inference-cheap-with-analog]]'
- '[[2026-06-23-semidoped-daily-update]]'
- '[[2025-10-21-ceva-launches-wi-fi-7-ip-for-smarter-ai-driven-iot-and-physi]]'
- '[[2025-10-21-ceva-introduces-wi-fi-7-1x1-client-ip-to-power-smarter-more-]]'
- '[[2026-robot-data-supply-funding-wave]]'
- '[[2025-10-28-ceva-wi-fi-7-client-ip-supports-ai-enabled-iot-devices-and-p]]'
- '[[2026-04-20-robot-autonomy-destination-bessemer-venture-partners]]'
- '[[2026-08-06-the-year-ai-science-and-the-physical-ai-industry-came-alive]]'
- '[[2026-09-01-chinas-ai-rally-is-real-most-global-investors-are-missing-it]]'
- '[[2026-04-20-physical-ai-deploys-this-decade-bessemer-predicts-robotics]]'
- '[[2026-07-01-sensifai-memo-streaming-physical-ai]]'
- '[[2026-06-15-gf-investor-day-2026]]'
- '[[2026-09-18-visions-of-ai-gpt-3-moment-for-physical-ai]]'
- '[[2026-09-07-microchip-acquires-hailo-jul-2026]]'
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
mention_count: 106
descendants:
- dexterous-manipulation
- humanoid-robots
- robot-actuators
- robot-data-collection
- sim-to-real-robot-data
- tactile-sensing
- vision-language-action-models
- world-models
sources_7d: 4
sources_30d: 20
recent_mentions:
- slug: 2026-09-18-visions-of-ai-gpt-3-moment-for-physical-ai
  title: 'Visions of AI: GPT-3 Moment for Physical AI'
  date: '2026-09-18'
  kind: web
- slug: 2026-09-07-microchip-acquires-hailo-jul-2026
  title: Microchip Technology signs definitive agreement to acquire Hailo (Microchip IR, 24 Jul 2026; CTech; Globes)
  date: '2026-09-07'
  kind: web
- slug: 2026-09-01-chinas-ai-rally-is-real-most-global-investors-are-missing-it
  title: China’s AI Rally Is Real. Most Global Investors Are Missing It.
  date: '2026-09-01'
  kind: web
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
## Summary

"Physical AI" names the stack that connects learned models to actuators: sensors that capture the world (cameras, event cameras, tactile skins, inertial and gaze signals), a learned policy that maps perception plus a language instruction to motor commands, and the compute that has to run that policy on a moving, battery-powered platform. The dominant policy architecture in the current literature is the vision-language-action (VLA) model, and within that the diffusion-based variants, which give the best motion quality and generalisation but must be evaluated at control frequencies of roughly 50-200 Hz, imposing hard latency and energy budgets at the edge. A parallel line of work replaces or augments the reactive policy with a world model: a learned predictive core that compresses observations into states and simulates action-conditioned futures for planning.

The research frontier is currently about the failure modes rather than the demonstrations. VLA perception is fragile at the sensing stage: under 20 lux, an image-only policy scored 0% on a pick-and-place task, rising to 60% when accumulated event-camera maps were simply overlaid on the RGB frames. Neuromorphic sensing is being pushed for the same reason on drones, cars and underwater vehicles, where motion blur and harsh light break frame-based imaging. On the compute side, the work is co-design: exploiting temporal similarity between consecutive control inputs to skip redundant bit-level operations, or, on AR glasses, using gaze, pose and inertial cues to keep only the informative parts of egocentric video for a 27.5x memory and 24.3x energy reduction versus a full-video baseline.

## Viability (3/5)

The subsystem evidence is real and quantified. Event augmentation lifts a manipulation task from 0% to 60% success at 20 lux; intent-driven perception filtering cuts memory 27.5x and energy 24.3x on glasses while preserving task accuracy; bit-sparsity and speculative inference are proposed specifically because diffusion VLA at 50-200 Hz does not fit edge budgets today. Commercially, hardware ships in volume: 5,215 humanoids and 23,000 quadrupeds in 2025 at roughly 60% gross margin <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>.

**TLDR: Components demonstrably work; the integrated system has not been shown to clear production reliability or shift-length duty cycles.**

## Drivers (4/5)

Demand is the thin half. The only disclosed end-customer breakdown in these sources shows over 70% of humanoids sold going to research and education and roughly 17% to commercial and consumer buyers, characterised as bought largely for show: retail promotion, tourist sites, performances <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>. Quadrupeds carry the genuine industrial base in power-grid, tunnel and pipeline inspection; humanoids do not yet. Q1 2026 revenue grew 68.5% year on year while net profit fell about 52%, which is consistent with a market being bought into rather than pulled <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>.

**TLDR: Supply-side push is strong and documented: record capital, collapsing sensor costs, foundry roadmaps rebuilt around the term; end demand is the weak side.**

## Novelty (3/5)

The comparison class is task-specific programmed automation and reactive control. VLA models are described as generalising to open-ended manipulation, and world models add planning beyond reactive control by simulating action-conditioned futures. That is a different kind of system, not an incremental one. Where the sources give magnitudes, they are large but narrow: 0% to 60% success on one task at one illumination level; 27.5x memory and 24.3x energy on egocentric video understanding against a full-video baseline; a 500-fold tactile sensor cost reduction **2026 Robot Data Supply Funding Wave**. Notably, the event-fusion win came from a parameter-free overlay, which suggests the current models leave easy robustness on the table rather than that the fusion method is deep.

Against that, the architecture itself is expected to stop being the differentiator: open source is predicted to commoditise model architecture, leaving data and deployment as the defensible layers, while hardware cost compression erodes OEM margin <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Venture Partners: Robotics and Physical AI - Data & Deployment as Defensible Value" rel="noopener">ref</a></sup>. On that view the novelty that persists is in datasets, evaluation and the sensing and compute components, not in the policy family.

**TLDR: Learned VLA and world-model policies are a genuine break from programmed automation, but the specific gains in the sources are point improvements and the architecture layer is commoditising.**

## Diffusion (2/5)

Fourth, and least discussed commercially, is security. Once a predictive layer sits between sensors and actuators, poisoning, backdoors, sensor spoofing, prompt injection and supply-chain attacks can propagate into physical action, and a compromised or over-trusted world model can generate what the survey calls predictive safety illusions while appearing to act as a safety shield. In regulated industrial and domestic settings that becomes a certification problem, not just an engineering one. The observed adoption pattern matches these barriers: inspection quadrupeds in the field, humanoids in labs and showrooms <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>.

## Impact (4/5)

The breadth is visible in the sources rather than asserted: mining rigs, drones, trucks and warships in one operator's account of the category <sup class="ref"><a href="https://www.latent.space/p/appliedintuition" title="Physical AI that Moves the World — Qasar Younis & Peter Ludwig, Applied Intuition" rel="noopener">ref</a></sup>, household service robotics as a funded research programme, AR glasses as an embodied-intelligence platform in its own right, and inspection work already running on quadrupeds in power grids, tunnels and pipelines <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>. A specialty foundry has reorganised its public strategy around the sense / think / act / communicate stack and attaches a 39bn-plus connected-device figure by 2030 to the edge memory requirement alone <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup>.

The qualifier is distribution rather than size. The same analysis that expects large value expects it to land in data, evaluation and world-model flywheels plus the component layer, not in robot OEMs facing hardware cost compression or in standalone foundation models commoditised by open releases <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Venture Partners: Robotics and Physical AI - Data & Deployment as Defensible Value" rel="noopener">ref</a></sup>. So the value at stake is high; the identity of the beneficiaries is contested, and the sources support a real risk that today's most visible players capture little of it.

## Timing Soon (2-5yr)

Two clocks run at different speeds. The component and narrow-application clock is already at zero: quadrupeds are sold into industrial inspection at scale <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>, tactile sensing costs have collapsed **2026 Robot Data Supply Funding Wave**, and edge silicon roadmaps for always-on sensing are being marketed today <sup class="ref"><a href="https://investors.gf.com/static-files/d85029e8-6913-4ea1-919c-b8c4361f00b7" title="GlobalFoundries Investor Day 2026 (presentation)" rel="noopener">ref</a></sup> <sup class="ref"><a href="https://news.google.com/rss/articles/CBMijwJBVV95cUxOZkl3MHJ4d3lzSVpHalRDMGRNM3dEdUZ4RHlBZ1d5NkpOM2paUzYyOUtHRHhIUFNsaDh0Z0xYbWg3ckd6TGw0NVQ0Um9HVkJROWVleG1VV1E0bEE1YXJYMEM5VlB2S0ZNaVFpQXRMc2RhaVBYVEIxaUVCakpjRFhWVHhKbnBjZTl0UWhSd3lkOTREWi1VSmVfcGxsd1UtUnVMVWZmX0hmR1hMYy11ZzRWWllzQmV3YUhhSVc5OGVjZldzMnRPcklZNjYwSVVUaVFyczl0Y19YSndISTdENVVFMlRKbElFQnlRU25HRUZBY1oxQXZqWGh6djVSdnZXcnFpbWptdGtTTG5xd1NsTnZR?oc=5" title="Ceva Introduces Wi-Fi 7 1x1 Client IP to Power Smarter, More Responsive AI-Enabled IoT Devices and Emerging Physical AI " rel="noopener">ref</a></sup>. Expect steady, unglamorous revenue there over the next two years.

## Overrated or underrated? Fairly rated

So the honest position is that the aggregate label is fairly rated while the allocation within it is not. The thesis that data and deployment stay defensible and OEM margin compresses <sup class="ref"><a href="https://www.bvp.com/atlas/bessemer-predicts-robotics-and-physical-ai" title="Bessemer Venture Partners: Robotics and Physical AI - Data & Deployment as Defensible Value" rel="noopener">ref</a></sup> is the one to test, and Unitree's roughly 60% gross margin with falling net profit is an early datapoint on which side of it hardware sits <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>. Also underweighted relative to its severity: the security surface created by putting a learned predictive layer in the actuation path.

## Prediction

By the end of 2027, no disclosed customer-mix breakdown from a volume humanoid vendor will show a majority of units going to production industrial or commercial work rather than research, education, display or pilot use (2025 baseline: over 70% research and education, roughly 17% commercial and consumer, largely for show) <sup class="ref"><a href="https://www.scmp.com/business/banking-finance/article/3347365/chinas-unitree-robotics-rides-humanoid-tide-it-targets-us610m-ipo" title="Unitree STAR Market IPO prospectus: 2025 units, ASPs and customer mix" rel="noopener">ref</a></sup>.

## Evidence base

## Open questions

---
*Assessment drafted 2026-08-31 from up to 18 KB sources using the technology-scorecard framework; scores are a draft read pending review.*
