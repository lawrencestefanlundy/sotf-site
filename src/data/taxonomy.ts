/**
 * Canonical descriptions for the 12 macros + 53 mesos.
 *
 * Macro and meso names are referenced by slug. Descriptions are 1-2 short
 * sentences — readable, opinionated, not promotional.
 */

export type MacroEntry = {
  slug: string;
  name: string;
  blurb: string;
};

export type MesoEntry = {
  macroSlug: string;
  slug: string;
  name: string;
  blurb: string;
};

export const MACROS: MacroEntry[] = [
  { slug: "compute",          name: "Compute",          blurb: "Logic, alt paradigms, edge inference, quantum. How instructions become physics — and the substrates competing to do it." },
  { slug: "memory",           name: "Memory",           blurb: "DRAM, HBM, NAND — and the emerging layer: MRAM, RRAM, PCM, photonic, memcapacitor. The memory wall is where AI scaling breaks; this is where it gets repaired." },
  { slug: "sensing",          name: "Sensing",          blurb: "Imaging, ranging, MEMS, quantum sensing. How machines measure the world." },
  { slug: "communications",   name: "Communications",   blurb: "Wireless, fibre, optical interconnect, quantum. How things talk to each other — from 5G and DECT NR+ to fibre, CPO, and QKD." },
  { slug: "energy-power",     name: "Energy & Power",   blurb: "Generation, storage, carbon capture, power electronics, thermal. The substrate of everything else — getting electrons in and heat out at scale." },
  { slug: "manufacturing",    name: "Manufacturing",    blurb: "Lithography, packaging, equipment, foundry, deposition. How chips are made — and where the binding constraints on every other layer live." },
  { slug: "materials",        name: "Materials",        blurb: "Substrates, functional layers, advanced materials, coatings. What chips are made of — silicon and far beyond." },
  { slug: "photonic-systems", name: "Photonic Systems", blurb: "PIC platforms, light sources, displays, modulators, metasurfaces, photonic compute. Light as the carrier — increasingly the cheapest way to move and process information." },
  { slug: "life-frontier",    name: "Life & Frontier",  blurb: "Biotech, neural interfaces, space, AI infrastructure, trust. The edges of the stack where deep-tech reaches into bodies, orbits, and institutions." },
  { slug: "robotics",         name: "Robotics",         blurb: "Embodiment and robot learning. Physical AI — where models meet motors, and the data flywheel decides who wins." },
  { slug: "semiconductor-process-flow", name: "Process Flow", blurb: "The chip lifecycle step by step: design, wafer, frontend fab, test, packaging. A guided walk through how sand becomes silicon." },
  { slug: "ai-software",      name: "AI & Software",    blurb: "Agents, models, inference economics, vertical AI, AI security. The layer where compute's value actually gets captured." },
];

export const MESOS: MesoEntry[] = [
  // ── COMPUTE ─────────────────────────────────────────────────────────
  { macroSlug: "compute", slug: "conventional-logic", name: "Conventional logic",
    blurb: "CPU/SoC, AI accelerators, RISC-V — von Neumann logic on silicon. Mature, mainstream, still the substrate under most production AI workloads." },
  { macroSlug: "compute", slug: "non-conventional", name: "Non-conventional computing",
    blurb: "Computing that isn't von Neumann — analog, neuromorphic, probabilistic, Ising machines, thermodynamic, reversible, nanomechanical, memristors. The substrates that compute by other physics, mostly pre-revenue." },
  { macroSlug: "compute", slug: "compute-architecture", name: "Compute architecture",
    blurb: "Chiplets, UCIe, CFET, GAA nanosheet, FD-SOI, backside power delivery, cryo-CMOS. How transistors are arranged once you can't shrink them any further." },
  { macroSlug: "compute", slug: "ai-edge", name: "AI at the edge",
    blurb: "Edge AI infrastructure, on-device LLM inference, TinyML, IoT compute. AI that runs where the data is created — milliwatts, not megawatts." },
  { macroSlug: "compute", slug: "quantum-computing", name: "Quantum computing",
    blurb: "All qubit platforms — silicon spin, trapped ion, superconducting, neutral atom, photonic, topological, bosonic cat. Plus quantum software, compilers, error correction, cryogenic control." },

  // ── MEMORY ──────────────────────────────────────────────────────────
  { macroSlug: "memory", slug: "mainstream-memory", name: "Mainstream memory",
    blurb: "DRAM, HBM, SRAM, NAND, MRAM, FeRAM. The memory a chip designer can actually pick today — including the increasingly-mature non-volatile options (MRAM, FeRAM) that have crossed into productisation." },
  { macroSlug: "memory", slug: "emerging-memory", name: "Emerging memory",
    blurb: "RRAM, PCM, memcapacitor, photonic memory, storage-class memory, in-memory computing. The watchlist — substrates and architectures still proving they can scale." },

  // ── SENSING ─────────────────────────────────────────────────────────
  { macroSlug: "sensing", slug: "imaging", name: "Imaging",
    blurb: "CMOS image sensors, event-based vision, hyperspectral, InGaAs SWIR, microbolometer thermal IR. Cameras as the dominant input modality — and what comes after the conventional sensor." },
  { macroSlug: "sensing", slug: "ranging-detection", name: "Ranging & detection",
    blurb: "LiDAR, mmWave radar, SPAD arrays, time-of-flight. Measuring distance and motion — the sensing layer under autonomy, robotics, and consumer AR." },
  { macroSlug: "sensing", slug: "mems", name: "MEMS",
    blurb: "Micro-electromechanical systems — sensing, switching, actuation, spectral analysis. Small mechanical things integrated into silicon." },
  { macroSlug: "sensing", slug: "quantum-sensing", name: "Quantum sensing",
    blurb: "Quantum gravimetry, magnetometry, NV diamond sensing, atomic clocks, quantum imaging. The most mature commercial application of quantum technology — already shipping for navigation, geophysics, and defence." },

  // ── COMMUNICATIONS ──────────────────────────────────────────────────
  { macroSlug: "communications", slug: "wireless", name: "Wireless",
    blurb: "5G NR-Advanced, mmWave, DECT NR+, sub-THz / 6G, beamforming ICs, phased-array antennas, software-defined radio. RF physics meeting silicon — the layer that makes everything mobile." },
  { macroSlug: "communications", slug: "fibre-and-free-space", name: "Fibre & free-space",
    blurb: "Long-haul fibre optics, dark fibre and submarine cables, free-space optical links. The literal backbone of the internet, plus its line-of-sight cousins." },
  { macroSlug: "communications", slug: "optical-interconnect", name: "Optical interconnect",
    blurb: "Linear pluggable optics (LPO), chip-level optical I/O, pluggable transceivers. Where light replaces copper inside the data centre — the layer under the CPO transition." },
  { macroSlug: "communications", slug: "quantum-comms", name: "Quantum communications",
    blurb: "Quantum key distribution (QKD), quantum networks, quantum repeaters. Information-theoretic security at the network layer — separate paradigm from classical comms." },

  // ── ENERGY & POWER ──────────────────────────────────────────────────
  { macroSlug: "energy-power", slug: "generation", name: "Generation",
    blurb: "Fusion in every confinement geometry (magnetic, inertial, FRC, stellarator, z-pinch), geothermal, solar (perovskite, photovoltaic, tandem), electrolysers, SOFCs, wave-tidal. How new electrons get made — net-zero, on the largest scales." },
  { macroSlug: "energy-power", slug: "carbon-capture", name: "Carbon capture",
    blurb: "BECCS, CCUS, direct air capture, mineralisation, ocean alkalinity. Removing CO₂ that's already been emitted — distinct from generation, often confused with it." },
  { macroSlug: "energy-power", slug: "storage", name: "Storage",
    blurb: "Batteries across every chemistry — lithium-ion, lithium-sulphur, sodium-ion, solid-state, flow — plus compressed-air, gravity-thermal, and long-duration storage. How electrons sit still until they're needed." },
  { macroSlug: "energy-power", slug: "power-electronics", name: "Power electronics",
    blurb: "GaN-on-Si, power management ICs, wireless power transfer, GW-scale power delivery, solid-state circuit breakers. The semiconductors that move large currents — the bottleneck under AI datacentres, EVs, and the grid build-out." },
  { macroSlug: "energy-power", slug: "thermal-management", name: "Thermal management",
    blurb: "Heat pipes, vapor chambers, thermal interface materials, liquid cooling, diamond heat spreaders, graphene thermal films, phase-change materials. AI's power density already exceeds what air-cooling can dissipate — this is where the next several W/cm² come from." },

  // ── MANUFACTURING ───────────────────────────────────────────────────
  { macroSlug: "manufacturing", slug: "lithography", name: "Lithography",
    blurb: "EUV (including high-NA), DUV immersion, e-beam, maskless multi-beam, nanoimprint, photoresists, two-photon polymerisation, xolography. The patterning layer that gates every other layer of semiconductor scaling." },
  { macroSlug: "manufacturing", slug: "packaging", name: "Packaging",
    blurb: "3D-IC stacking, CoWoS, FOWLP, hybrid bonding, co-packaged optics, photonic wire bonding, TSV, glass interposers, substrates. Where Moore's Law has actually been alive for the last decade." },
  { macroSlug: "manufacturing", slug: "equipment-processes", name: "Equipment & processes",
    blurb: "ALD, MOCVD/MBE, PVD, CMP, iCVD, etch tools, metrology, wafer-handling, additive manufacturing, diamond-turning. The physical processes that turn substrates into devices." },
  { macroSlug: "manufacturing", slug: "foundry-design", name: "Foundry & design",
    blurb: "Foundry services, multi-project wafer (MPW), OSAT, PDKs, EDA tools, specialty foundries. The commercial machinery between a chip design and an actual wafer." },

  // ── MATERIALS ───────────────────────────────────────────────────────
  { macroSlug: "materials", slug: "substrates", name: "Substrates",
    blurb: "Silicon, SiC, GaN, GaAs, InP, Ge, diamond, sapphire. Plus 2D materials — graphene, hBN, TMDs — and the compound semiconductor family. What the device is built on." },
  { macroSlug: "materials", slug: "functional-layers", name: "Functional layers",
    blurb: "Barium titanate (BTO), thin-film lithium niobate (TFLN), scandium aluminium nitride, ferroelectric HfO₂, polymer waveguides, piezoelectric and topological materials. Engineered films that do real work — modulate light, store charge, transduce energy." },
  { macroSlug: "materials", slug: "advanced-materials", name: "Advanced materials",
    blurb: "Graphene and its 2D cousins, MXenes, carbon nanotubes, chalcogenide glasses, ceramics, novel thin films. The post-silicon material zoo — most of it not yet at production scale." },
  { macroSlug: "materials", slug: "coatings-interfaces", name: "Coatings & interfaces",
    blurb: "Anti-reflection, hydrophobic and oleophobic coatings, optical coatings, diffusion barriers. The thin films at the boundary between a device and its environment." },

  // ── PHOTONIC SYSTEMS ────────────────────────────────────────────────
  { macroSlug: "photonic-systems", slug: "pic-platforms", name: "PIC platforms",
    blurb: "Silicon photonics, InP, GaAs, polymer photonics, photonic ICs, heterogeneous integration. The substrates competing to be the equivalent of CMOS for light." },
  { macroSlug: "photonic-systems", slug: "light-sources", name: "Light sources",
    blurb: "DFB/DBR lasers, quantum cascade lasers, VCSELs, single-photon sources, frequency combs. How photons get created — across visible, IR, and increasingly mid-IR." },
  { macroSlug: "photonic-systems", slug: "displays", name: "Displays",
    blurb: "Micro-LED, OLED, holographic and volumetric displays. Light emission as the output modality — the layer between digital state and the human eye." },
  { macroSlug: "photonic-systems", slug: "modulators-detectors", name: "Modulators & detectors",
    blurb: "Mach-Zehnder modulators, electro-absorption modulators, Pockels modulators, ring resonators, spatial light modulators, avalanche and Ge/InGaAs photodiodes. How photons get manipulated and counted." },
  { macroSlug: "photonic-systems", slug: "photonic-compute", name: "Photonic compute",
    blurb: "Optical neural networks, diffractive deep neural networks, photonic tensor cores, photonic compute-memory. Doing the multiply-accumulate in light — if it scales, the AI accelerator wars get a new entrant." },
  { macroSlug: "photonic-systems", slug: "metasurfaces", name: "Metasurfaces",
    blurb: "Metalens, metasurfaces / flat optics, metamaterials, wafer-level optics. Sub-wavelength nanostructured surfaces that replace whole lens stacks with a single layer — the cheapest path to high-volume optics." },

  // ── LIFE & FRONTIER ─────────────────────────────────────────────────
  { macroSlug: "life-frontier", slug: "biotech", name: "Biotech",
    blurb: "Synthetic biology, CRISPR, DNA synthesis, single-cell sequencing, spatial transcriptomics, 3D bioprinting, biomaterials. Engineering at the cell scale — increasingly converging with the semiconductor stack." },
  { macroSlug: "life-frontier", slug: "neural-interfaces", name: "Neural interfaces",
    blurb: "Invasive BCI, non-invasive BCI, bioelectronic medicine, hearables / silent speech, AR/VR. The interface between brains and machines — both ends moving fast in 2026." },
  { macroSlug: "life-frontier", slug: "diagnostics-health", name: "Diagnostics & health",
    blurb: "Digital pathology, liquid biopsy, point-of-care diagnostics, health/fitness tracking. Measurement-first medicine — the part of healthcare most directly improved by sensing and AI." },
  { macroSlug: "life-frontier", slug: "space-access", name: "Space access",
    blurb: "Propulsion (electric, in-space, nuclear thermal), reusable launch, space-grade FPGAs, rad-hard ICs, space hardware substrates. The platforms and the radiation-hardened silicon they need to survive." },
  { macroSlug: "life-frontier", slug: "in-orbit", name: "In orbit",
    blurb: "LEO mega-constellations, direct-to-cell, optical inter-satellite links, earth observation (atmospheric, hyperspectral, optical, SAR). Once you're in orbit, what you do there." },
  { macroSlug: "life-frontier", slug: "lunar", name: "Lunar",
    blurb: "Lunar landers, surface power, in-situ resource utilisation (ISRU), teleoperation. The next planetary surface — and the only one where commercial hardware will land this decade." },
  { macroSlug: "life-frontier", slug: "ai-infrastructure", name: "AI infrastructure",
    blurb: "AI-grade datacentre real estate, GW-scale power delivery, datacentre cloud infrastructure, sovereign AI. The physical and political substrate under the AI scaling laws." },
  { macroSlug: "life-frontier", slug: "trust", name: "Trust",
    blurb: "Cybersecurity, federated learning, homomorphic encryption, MPC, zero-knowledge proofs, TEEs, differential privacy, data unions. The cryptographic and architectural layer that makes shared computation possible without shared visibility." },

  // ── ROBOTICS ────────────────────────────────────────────────────────
  { macroSlug: "robotics", slug: "embodiment", name: "Embodiment",
    blurb: "Actuators, dexterous manipulation, tactile sensing, humanoid platforms, factory automation. The hardware half of physical AI — where torque, compliance and cost decide what's buildable." },
  { macroSlug: "robotics", slug: "robot-learning", name: "Robot learning",
    blurb: "Vision-language-action models, world models, sim-to-real transfer, robot data collection. The bet that robotics is now a data problem wearing a hardware costume." },

  // ── PROCESS FLOW ────────────────────────────────────────────────────
  { macroSlug: "semiconductor-process-flow", slug: "design", name: "Design",
    blurb: "RTL to tape-out: synthesis, place-and-route, timing signoff, verification, DFT, IP licensing, OPC. Where a chip exists only as software." },
  { macroSlug: "semiconductor-process-flow", slug: "wafer-materials", name: "Wafer materials",
    blurb: "Polysilicon, crystal growth, slicing and polishing. Sand to substrate." },
  { macroSlug: "semiconductor-process-flow", slug: "frontend", name: "Frontend",
    blurb: "Oxidation, lithography, etch, implant, deposition, CMP, the transistor module, damascene interconnect. The wafer's thousand-step gauntlet." },
  { macroSlug: "semiconductor-process-flow", slug: "test-metrology", name: "Test & metrology",
    blurb: "Defect inspection, CD/overlay metrology, wafer sort, parametric test, final test, burn-in. Where yield is measured and margins are made." },
  { macroSlug: "semiconductor-process-flow", slug: "packaging", name: "Packaging",
    blurb: "Backgrind, dicing, die attach, bonding, molding, substrates, bumping, 2.5D/3D/fan-out, OSAT. The back end that became the front line." },

  // ── AI & SOFTWARE ───────────────────────────────────────────────────
  { macroSlug: "ai-software", slug: "agents", name: "Agents",
    blurb: "AI agents, orchestration, agent identity and KYA, agentic payments, x402, stablecoin rails. Software that acts — and the trust and money plumbing it needs." },
  { macroSlug: "ai-software", slug: "models-inference", name: "Models & inference",
    blurb: "LLMs, open-weight models, post-training, RL, inference economics, KV cache, state-space models, the CUDA moat. What the models are and what they cost to run." },
  { macroSlug: "ai-software", slug: "ai-applications", name: "AI applications",
    blurb: "AI for EDA, diagnostics, materials discovery, simulation, physics, geospatial. Vertical AI where the domain is the moat." },
  { macroSlug: "ai-software", slug: "ai-security", name: "AI security",
    blurb: "Workload sandboxing, hypervisor isolation, microkernels, unikernels. Running untrusted intelligence safely." },
];

export function macroBySlug(slug: string): MacroEntry | undefined {
  return MACROS.find((m) => m.slug === slug);
}

export function mesosForMacro(macroSlug: string): MesoEntry[] {
  return MESOS.filter((m) => m.macroSlug === macroSlug);
}

export function mesoBySlug(macroSlug: string, mesoSlug: string): MesoEntry | undefined {
  return MESOS.find((m) => m.macroSlug === macroSlug && m.slug === mesoSlug);
}
