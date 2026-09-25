---
type: concept
slug: photonic-compute
canonical_name: Photonic Compute
aliases:
- photonic processor
- optical computing
kind: technology
parent_concepts:
- photonic-systems
- photonic-compute
related_concepts: []
sources:
- '[[2025-03-12-project-mayhem-ai-inward-collapse]]'
- '[[2025-12-02-the-future-of-computing-is-glass]]'
- '[[2023-07-14-e08-optical-computing]]'
- '[[2023-07-23-analog-computing-the-once-and-future]]'
- '[[2026-07-07-the-asml-killer]]'
- '[[2025-04-30-has-the-time-come-to-take-mortal]]'
- '[[2025-04-16-the-state-of-photonic-computing]]'
- '[[2026-05-24-mose2-exciton-polariton-all-optical-switch]]'
- '[[2025-07-14-solving-compute-crisis-physics-based-asics]]'
- '[[2026-08-07-chip-industry-week-in-review-7-aug-2026]]'
- '[[2023-03-29-oxford-spinout-lumai-secures-11m-grant-to-power-optical-comp]]'
scorecard:
  viability: 3
  drivers: 4
  novelty: 3
  diffusion: 2
  impact: 3
  timing_band: Soon (2-5yr)
  verdict: Overrated
scorecard_status: draft
scorecard_origin: hand
mention_count: 118
descendants:
- diffractive-deep-neural-network
- diffractive-deep-neural-networks
- optical-neural-networks
- photonic-compute
- photonic-compute-memory
- photonic-tensor-cores
sources_7d: 6
sources_30d: 15
recent_mentions:
- slug: 2026-08-07-chip-industry-week-in-review-7-aug-2026
  title: Chip Industry Week in Review (7 Aug 2026)
  date: '2026-08-07'
  kind: web
- slug: 2026-07-31-inference-silicon-roster-sprint
  title: 'Inference-silicon roster verification sprint: 10 companies for the competitive-analysis capital map'
  date: '2026-07-31'
  kind: web
- slug: 2026-07-07-the-asml-killer
  title: The ASML Killer?
  date: '2026-07-07'
  kind: substack
- slug: 2026-05-24-mose2-exciton-polariton-all-optical-switch
  title: New light-based switch could cut chip energy use and speed future AI photonics
  date: '2026-05-24'
  kind: web
- slug: 2025-12-02-the-future-of-computing-is-glass
  title: The Future of Computing is Glass w/ Andrea Rocchetto of Ephos
  date: '2025-12-02'
  kind: substack
- slug: 2025-07-14-solving-compute-crisis-physics-based-asics
  title: Solving the compute crisis with physics-based ASICs
  date: '2025-07-14'
  kind: web
- slug: 2025-04-30-has-the-time-come-to-take-mortal
  title: Has the time come to take Mortal Computing seriously?
  date: '2025-04-30'
  kind: substack
- slug: 2025-04-16-the-state-of-photonic-computing
  title: 'Photonic Computing: A Primer'
  date: '2025-04-16'
  kind: substack
neighbors: []
---
**Optical computing does the maths with light instead of electrons, which on paper is faster, cooler and more parallel, but 3 years after I first scored it the industry has mostly taken the photons into networking instead, the money has come back for opto-electronic AI accelerators anyway, and the thing that decides whether any of it becomes a computer, optical memory, still isn't solved.**

## Context

Once you get into the details of new computing approaches like photonics, quantum, and analogue, you end up in a debate between science and manufacturing. Scientifically, non-conventional computers are better across critical dimensions like power consumption, bandwidth, and latency. But then the actual hard questions around adoption and timing relate to manufacturing. All the barriers are around the scale and complexity of the electronic CMOS semiconductor supply chain and the difficulties in fabricating anything that doesn't fit almost perfectly into the existing processes.

So we end up with digital neuromorphic chips and optoelectronic chips. Designs that take some of the benefits of new architectures and substrates but connect neatly to other electronic components and processes. We should think about the computing process in these terms. We're on a path from a unipolar computing world with electronics as the hegemon to a multipolar world with dominant electronic power but with rising photonic, quantum, and analogue powers. Photonics, analogue, and quantum will try to fit into the existing world by incorporating many electronic features and processes to smooth the transition. Quantum and photonics might even merge. The big question is, how big will these new powers get? How much electronic land will they capture? And will any of the new approaches become a new hegemon?

I'd keep all of that 3 years on, with one correction to the map, which is that the first electronic land photonics actually took was the wiring, not the maths. Lightmatter, Lightelligence and Celestial AI all started out with the optical computing vision and all ended up selling interconnect, because that's where customers were paying <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>, and co-packaged optics from Broadcom, Nvidia, Intel and TSMC is now the mainstream roadmap. So the photonic power is rising, just mostly in [Optical Interconnect](/communications/optical-interconnect/optical-interconnect/) and [Co-Packaged Optics](/manufacturing/packaging/co-packaged-optics/), which have their own cards. This card is about the harder thing, doing the computation itself in light.

## Summary

Optical computing is a computing approach that uses light particles, or photons, instead of electrons to perform computations. Optoelectronic computing is a sub-field that involves the use of photons and electrons to perform computing tasks. It combines elements of both optical and electronic computing, aiming to leverage the advantages of both while mitigating their respective limitations. They are segments within the broader field of photonic computing encompassing optical computing and other technologies using light for information processing tasks. Photonics is the most expansive term involving the generation, manipulation, and detection of photons, which are light particles. Photonics applications range from fibre-optic communication to medical diagnostics and laser manufacturing.

Optical computing leverages the properties of light, including its speed and capacity to carry large amounts of data, to achieve higher processing speeds and energy efficiency compared to classical electronic computing. While classical computing relies on electric currents in circuits to perform calculations, optical computing uses light waves to transfer and process data. It involves components like optical transistors and optical fibres, which can handle multiple light signals at the same time.

In practice almost everything that exists today is analogue matrix maths. You encode a vector onto light, send it through something whose transmission is the weight matrix (a mesh of interferometers on a chip, a lens system in free space, an array of modulators), and read the answer off photodetectors, so the multiply-accumulate itself costs almost no energy and happens in the time the light takes to cross the device. Everything around that, the weights, the nonlinear functions, the memory, is still electronic. The best public result is Lightmatter's processor in Nature in April 2025, 4 photonic tensor cores (128x128) stacked with 2 12nm digital chips in one package, running ResNet, BERT and DeepMind's Atari agent unmodified at close to 32-bit accuracy, at 65.5 trillion 16-bit operations a second on 78W of electrical power plus 1.6W optical ([Nature](https://www.nature.com/articles/s41586-025-08854-x)). It also only reaches 27.5% of standard performance on high-precision regression and can only hold models up to 268MB without splitting them across units <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>. The academic work is smaller again, MNIST-class classifiers and 49-dimensional vectors,.

## Viability (3/5)

In 2023 I said opto-electronic computing was 1-2 years from commercialisation. It wasn't, or at least nobody is shipping it in volume yet, so I was early. What has changed is that the hybrid demonstrably works on real models now rather than toy ones, which is the Lightmatter result above.

An optoelectronic chip, also known as a photonic integrated circuit (PIC), is a device that integrates multiple optical (light-based) and electronic functions onto a single chip. Such a chip aims to utilise the best of both worlds: optics' high-speed, high-bandwidth capabilities and mature, well-understood electronics technology. PICs take data as an electronic signal, convert it to an optical signal using a modulator, process the data as light, convert the signal back into an electronic signal using a photodetector, and the electronic signal is then output from the chip. The primary challenges are manufacturing and performance, especially the efficient conversion between optical and electrical signals, consuming roughly 30% of their energy converting electronic energy into photons and back.

Memory is the bit the 2023 card underplayed. Phase change materials, basically the same stuff as rewritable DVDs, are the best bet for optical memory, but they wear out after 10,000-100,000 write cycles against 10^16 plus for electronic memory, and the best lab results are around 10^8 <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>. So the weights live in electronics and you pay the conversion every time you go to memory, which the research literature now describes as the fundamental limitation on programmable photonic systems. Every opto-electronic chip I've looked at is finding clever ways to avoid going to memory, or running models small enough to fit in a few hundred MB.

All-optical computing with no electronic components is far less mature, still in the lab demonstration phase. The primary goal is still to build a scalable optical transistor to replace the electronic transistor. This would avoid the need for modulators and photodetectors entirely, simplifying the design and reducing power consumption. Numerous approaches include reflective mirrors, semiconductor nanocrystals, laser switching, and non-linear optical materials. All of which are still at the lab testing stage. The likelihood of a scalable all-optical computer in the next five years is low. I'd say the same in 2026. The 3 is for the opto-electronic hybrid, which you can nearly buy, all-optical on its own would be a 1.

**TLDR: Opto-electronic accelerators run real models now, all-optical is still in the lab, and memory is what's holding both back.**

## Drivers (4/5)

**Supply:** The market is driven by developments on the supply-side of the market: advancements in silicon photonics, photodetectors, and non-linear optical devices. Firstly, manufacturing advancements, particularly in silicon photonics, allow for cost-effective, high-volume production of optical components. Secondly, the efficiency of converting between optical and electrical signals is key to optical computing performance. Innovations like lightwave looping and more efficient photodetectors and modulators enhance this efficiency, increasing speed and reducing power consumption. Lastly, the ability to perform non-linear operations is crucial for computing. Advances in designing and manufacturing non-linear optical devices, such as optical logic gates and amplifiers, enable more complex and powerful optical computing systems. Since 2023 TSMC has come into silicon photonics with its COUPE co-packaged optics platform, which is what turns waveguide photonics into a normal fab product rather than a science project <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>, and research groups are deliberately designing inside standard foundry processes. And there's a packaging angle I didn't have in 2023, the photonics might end up inside the glass substrate the chiplets are mounted on rather than on a chip of its own <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-future-of-computing-is-glass" title="The Future of Computing is Glass w/ Andrea Rocchetto of Ephos" rel="noopener">ref</a></sup>.

**Demand:** Three major factors drive the optical computing market: AI growth, power consumption concerns, and quantum computing advancements. AI applications like machine learning require processing vast data at high speeds, a task where optical computing could excel due to its high-speed, parallel data processing capabilities. Notably, optical computing can quickly perform linear algebra operations and matrix multiplications, essential for AI algorithms. The power argument is stronger now than it was in 2023, AI basically turns electricity into intelligence and the bill grows with every agent call <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-compute-gradient" title="The Compute Gradient" rel="noopener">ref</a></sup>, and the money has followed: Arago's $26M seed in July 2025 ([DCD](https://www.datacenterdynamics.com/en/news/photonic-chip-startup-arago-closes-26m-seed-round/)), and Neurophos's $110M Series A in January 2026, led by Gates Frontier ([TechCrunch](https://techcrunch.com/2026/01/22/from-invisibility-cloaks-to-ai-chips-neurophos-raises-110m-to-build-tiny-optical-processors-for-inferencing)). That's investors coming back to optical compute after a couple of years of everyone running to interconnect. Quantum still helps on the side, quantum photonics and datacentre photonics both want the same ultra-low-loss components, so whoever builds for one is partly building for the other <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-future-of-computing-is-glass" title="The Future of Computing is Glass w/ Andrea Rocchetto of Ephos" rel="noopener">ref</a></sup>.

Why a 4 and not the 5 I gave it in 2023? The same forces pay for the alternatives. AI's power and bandwidth problem is exactly what's funding co-packaged optics and better digital accelerators, so the adoption forces are huge but they don't all point at optical compute.

**TLDR: AI's power problem and a lot of new money push hard, but the same forces fund interconnect and better digital chips.**

## Novelty (3/5)

Optical computers compete primarily with electronic computers to run computations. Computing with photons versus electrons theoretically offers superior speed and performance and lower power consumption. The trade-off versus electronic computing is that analogue will be less accurate, more complex to control signals due to the interaction of several signals, and bulky. Although, we should expect better control and miniaturisation as manufacturing capabilities develop. Optical computers are particularly well-suited to tasks involving large amounts of data and require high-speed data transfer, like high-performance computing and AI applications, especially LLMs based on matrix multiplication. A useful mental model is photonic computing at the core and [Neuromorphic Computing](/compute/non-conventional/neuromorphic-computing/) at the edge.

The 2026 version of this is that every company claims a big multiple, Arago 10x lower energy than GPUs at equivalent performance, Neurophos up to 100x on performance and efficiency, and I haven't seen any of them measured independently at system level. The one system measured in public, Lightmatter's, shows it can be accurate, and 65.5 trillion operations a second on roughly 80W all in is under 1 trillion operations a second per watt, which if I've done the maths right doesn't obviously beat a current GPU at 16-bit. Inside photonics the scaling arguments are real, one design needs 3N phase shifters where a standard interferometer mesh needs N^2, but both sides of that comparison are photonic.

**TLDR: Strong on matrix maths in principle, but the only measured system proves accuracy, and the 10-100x efficiency numbers are still company claims.**

## Diffusion (2/5)

Optical computing faces serious headwinds to adoption. Like any other non-electronic, non-CMOS computing architecture, it needs many components and manufacturing processes to change. Of the different configurations, optoelectronic computing faces the easiest path to adoption. A function of the ability to communicate directly with electronic memory and I/O, and existing software can be run. However, their design and fabrication are complex and require precise control over light properties, making development more challenging and costly than traditional electronic chips. Integrating existing electronic systems is another hurdle, requiring efficient conversion methods between optical and electronic signals. While decreasing, the cost of optoelectronic components can still be higher than equivalent electronic components. Material selection is also challenging, as the materials used need specific properties for efficient light generation, manipulation, and detection. Lack of established standards can hinder adoption, as can concerns about the reliability and lifespan of optoelectronic components, which can be sensitive to environmental conditions. For all-optical chips, the restraints are all noted for optoelectronic, plus an inability to use electronic fabrication processes and the need for new software and algorithms to be written.

The pivot is the best diffusion evidence we've got. When Lightmatter, Lightelligence and Celestial AI moved to interconnect, the market was telling you which photonics product it could actually absorb. The people I interviewed in 2025 added two barriers I'd underweighted, proving a photonic part runs for 3-5 years before anyone will design it into a product, and design tools that don't reflect real fab defects, so designs that work in simulation fail on the line <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>. And analogue versus digital is still open, analogue is where the physics advantage is, but noise and precision are hard enough that d-Matrix and Rain moved from analogue in-memory compute to digital <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>.

**TLDR: Opto-electronic is the easiest way in and still hard, and the move to interconnect shows where adoption actually is.**

## Impact (3/5)

The future computing landscape will be heterogeneous. The era of a single dominant computing approach is nearing its end. We already see specialisation in the electronic domain, with tasks offloaded to ASICs and FGPAs. Compute specialisation will continue from electronic computation to photonic, analogue and quantum in a 25-year timeframe. I wish I had a better mental model for how these tasks would break down. I am furiously scribbling crazy things on a 2x2 matrix, but I'm not there yet. Power consumption should be one of the axes, we can split the axis between edge and core, and performance could be another. But it's really not that easy because photons are faster than electrons, but controlling them is much more complex, so will the cost always be higher? Due to superposition and entanglement, Qubits are inherently more parallel (higher bandwidth) than electrons. However, controlling the qubits reliably is still not viable.

The right way to think about the impact of optical computing is to weigh the probability of manufacturing an all-optical chip at scale and reasonable cost. This involves solving the issues of logic-level restoration, cleaning up the signal to avoid error accumulation; scalability, connecting multiple logic gates in a sequence; higher fan-out, connecting multiple logic gates together; and input-output isolation, again, to avoid signal interference and errors. If these are solvable problems, then optical computing has the potential to perform a vast array of high-performance computing tasks, including a lot of AI training, most likely in the data centre. Suppose you think that the inherent non-linearity of photons will always mean electronic processing is cheaper and easier to manufacture. In that case, optical computing will mean optoelectronic computing and have a relatively limited impact.

I've got a bit further on the 2x2 since, and the variable I'd put on it now is memory. If someone makes optical memory with electronic-grade endurance, the conversion overhead goes away and most of the all-optical problems above get easier, and then this is a 5, a big chunk of AI inference and HPC in the datacentre. Without it optical computing means opto-electronic accelerators, 10-100x on specific operations like matrix multiplication and FFTs <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>, which is a valuable slice of inference but a slice. I'm scoring the version that exists.

**TLDR: A useful slice of AI inference if it stays opto-electronic, a much bigger deal if optical memory works.**

## Timing Soon (2-5yr)

Opto-electronic accelerators: I said 2025-2030 in 2023 and 3-5 years in April 2025 <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>, and I'd still say that, so real volumes late this decade, with specific jobs first, matrix multiplication for inference, FFTs, and oddities like defence, where immunity to electromagnetic interference matters <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>. The risk capital is already here, the revenue isn't.

All-optical: the timeline for a scalable all-optical computer is unknowable. Even a fabrication breakthrough in 2023 would still take 5+ years before significant volumes, and that ignored the need for optical memory and other SoC components. Still true, and it needs the memory breakthrough before it needs anything else.

**TLDR: Opto-electronic accelerators late this decade, all-optical whenever someone solves optical memory, which I can't date.**

## Overrated or underrated? Overrated

In 2023 I said correctly rated, boring I know, because the industry knew both the potential and how hard the manufacturing was. I'd move it to overrated now, mostly on the money. Arago and Neurophos alone raised $136M between July 2025 and January 2026 on 10-100x claims nobody has independently measured, while the thing everyone I interviewed named as the actual blocker, memory, gets a fraction of the attention <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>. Optical memory is the underrated bit. If I'm wrong about the accelerators it'll be because one of these companies publishes a system benchmark against a GPU on a model people actually run, which I'd love to see.

## Prediction

**2030 prediction, July 2023:** Optoelectronic processing chips will have a 30% market share in high-performance computing <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e08-optical-computing" title="🔮E08: Optical Computing" rel="noopener">ref</a></sup>.

Marking my own homework in September 2026, that's not happening. You'd need volume shipments by now to get anywhere near 30% by 2030, and nobody is shipping optical compute in volume.

**New prediction, September 2026:** By 31 December 2028, no photonic compute processor will have a published result in an MLPerf Inference round.

## Open questions

- Science versus manufacturing. Photonics is theoretically more performant than electronics, but we have yet to manufacture them. Is this a function of the inherent non-linearity of photons or just a money/processing challenge?
- Are electronic computers the result of path dependency, or are they the only computers we can reliably produce cheaply and at scale?
- Can optical transistors practically operate at extremely high frequencies? Electromagnetic waves must obey the transform limit, and therefore the rate at which an optical transistor can respond to a signal is still limited by its spectral bandwidth. For example, in fibre-optic communications, practical limits such as dispersion often constrain channels to bandwidths of tens of GHz, only slightly better than many silicon transistors.
- Does anyone get phase change or any other optical memory from around 10^8 write cycles to something near electronic endurance, on a silicon photonics line <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>?
- What's the measured energy per inference, lasers, converters and electronic memory included, for any of the new accelerators on a production-size model?

## Startups

**Doing the compute in light**

- [Neurophos](https://www.neurophos.com) (Austin): optical processing unit built from over 1M micron-scale metamaterial modulators, $110M Series A January 2026 ([HPCwire](https://www.hpcwire.com/off-the-wire/neurophos-secures-110m-series-a-to-launch-exaflop-scale-photonic-ai-chips/)).
- [Arago](https://www.arago.inc) (Paris): photonic AI accelerator, $26M seed July 2025.
- [Lumai](https://lumai.ai) (Oxford): free-space optics, the matrix maths done by beams of light in 3D space rather than in waveguides.
- [Optalysys](https://optalysys.com) (UK): optical Fourier transforms, now aimed at fully homomorphic encryption ([Optalysys](https://optalysys.com/fhe/)).
- [Luminous Computing](https://www.luminous.com): on the 2023 list, no public update in my sources since.

**Started in compute, moved to interconnect or switching**

- [Lightmatter](https://lightmatter.co), [Lightelligence](https://www.lightelligence.ai), [Celestial AI](https://www.celestial.ai) <sup class="ref"><a href="https://stateofthefuture.substack.com/p/the-state-of-photonic-computing" title="Photonic Computing: A Primer" rel="noopener">ref</a></sup>

**Enabler from the 2023 list**

- [LiGenTec](https://www.ligentec.com): silicon nitride photonics foundry.

---
*First published as a State of the Future card in July 2023 <sup class="ref"><a href="https://stateofthefuture.substack.com/p/e08-optical-computing" title="🔮E08: Optical Computing" rel="noopener">ref</a></sup>, updated 21 September 2026 from the April 2025 photonic computing primer and 2025-26 sources. Scores are a draft read pending review.*
