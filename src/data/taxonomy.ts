/**
 * Canonical descriptions for the 9 macros + 35 mesos.
 *
 * Macro and meso names are referenced by slug. Descriptions are 1-2 short
 * sentences — readable, opinionated, not promotional. Used by:
 *   - homepage macro cards
 *   - macro page header + meso card blurbs
 *   - meso page intro
 *
 * Phase 5 of the plan replaces ~12 of these with hand-written 150-250 word
 * syntheses; the rest stay as auto-stubs. For now everything is auto-stub.
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
  {
    slug: "compute",
    name: "Compute",
    blurb:
      "Logic, AI accelerators, alternative paradigms, edge inference, quantum. How instructions become physics — and the substrates competing to do it.",
  },
  {
    slug: "memory",
    name: "Memory",
    blurb:
      "DRAM, HBM, NAND — and the novel layer: MRAM, RRAM, PCM, photonic, memcapacitor. The memory wall is where AI scaling breaks; this is where it gets repaired.",
  },
  {
    slug: "sensing",
    name: "Sensing",
    blurb:
      "Imaging, ranging, MEMS, quantum sensing. How machines measure the world — image sensors, LiDAR, radar, gravimeters, biosensors.",
  },
  {
    slug: "communications",
    name: "Communications",
    blurb:
      "Wireless, wireline, optical interconnect, space comms. How things talk to each other — from 5G and DECT NR+ to fibre, CPO, and quantum key distribution.",
  },
  {
    slug: "energy-power",
    name: "Energy & Power",
    blurb:
      "Power electronics, batteries, fusion, storage, thermal. The substrate of everything else — getting electrons in and heat out at scale.",
  },
  {
    slug: "manufacturing",
    name: "Manufacturing",
    blurb:
      "Lithography, packaging, equipment, foundry, deposition. How chips are made — and where the binding constraints on every other layer live.",
  },
  {
    slug: "materials",
    name: "Materials",
    blurb:
      "Substrates, functional layers, advanced materials, coatings. What chips are made of — silicon and far beyond. The slowest-moving but most consequential layer.",
  },
  {
    slug: "photonic-systems",
    name: "Photonic Systems",
    blurb:
      "PIC platforms, light sources, modulators, metasurfaces, photonic compute. Light as the carrier — increasingly the cheapest way to move and process information.",
  },
  {
    slug: "life-frontier",
    name: "Life & Frontier",
    blurb:
      "Biotech, neural interfaces, diagnostics, space, AI infrastructure, trust. The edges of the stack where deep-tech reaches into bodies, orbits, and institutions.",
  },
];

export const MESOS: MesoEntry[] = [
  // Compute
  { macroSlug: "compute", slug: "logic-and-paradigms", name: "Logic & paradigms",
    blurb: "Conventional logic — CPUs, AI accelerators, RISC-V — alongside the alternative paradigms: analog, neuromorphic, Ising machines, probabilistic, thermodynamic, reversible. The contest isn't just transistor scaling; it's whether the von Neumann model holds against substrates that compute by other physics." },
  { macroSlug: "compute", slug: "compute-architecture", name: "Compute architecture",
    blurb: "Chiplets, UCIe, CFET, GAA nanosheet, FD-SOI, backside power delivery, cryo-CMOS. How transistors are arranged once you can't shrink them any further — the geometry layer between the physics and the system." },
  { macroSlug: "compute", slug: "ai-edge", name: "AI at the edge",
    blurb: "Edge AI infrastructure, on-device LLM inference, TinyML, IoT compute. AI that runs where the data is created — measured in milliwatts, not megawatts." },
  { macroSlug: "compute", slug: "quantum-computing", name: "Quantum computing",
    blurb: "All qubit platforms — silicon spin, trapped ion, superconducting, neutral atom, photonic, topological, bosonic cat. Plus quantum software, compilers, error correction, and the cryogenic control stack that makes any of it work." },

  // Memory
  { macroSlug: "memory", slug: "volatile", name: "Volatile",
    blurb: "DRAM, HBM, SRAM, in-memory computing. The high-bandwidth top of the memory hierarchy — HBM is the binding constraint on AI training right now." },
  { macroSlug: "memory", slug: "non-volatile-novel", name: "Non-volatile & novel",
    blurb: "NAND flash plus the novel layer: MRAM, RRAM, PCM, FeRAM, photonic memory, memcapacitor, storage-class memory. The next memory substrate that survives a power cut." },

  // Sensing
  { macroSlug: "sensing", slug: "imaging", name: "Imaging",
    blurb: "CMOS image sensors, event-based vision, hyperspectral, InGaAs SWIR, microbolometer thermal IR. Cameras as the dominant input modality — and what comes after the conventional sensor." },
  { macroSlug: "sensing", slug: "ranging-detection", name: "Ranging & detection",
    blurb: "LiDAR, mmWave radar, SPAD arrays, time-of-flight. Measuring distance and motion — the sensing layer under autonomy, robotics, and consumer AR." },
  { macroSlug: "sensing", slug: "mems", name: "MEMS",
    blurb: "Micro-electromechanical systems — sensing, switching, actuation. Small mechanical things integrated into silicon, from accelerometers to optical micromirrors." },
  { macroSlug: "sensing", slug: "quantum-sensing", name: "Quantum sensing",
    blurb: "Quantum gravimetry, magnetometry, NV diamond sensing, atomic clocks, quantum imaging. The most mature commercial application of quantum technology — already shipping for navigation, geophysics, and defence." },

  // Communications
  { macroSlug: "communications", slug: "wireless", name: "Wireless",
    blurb: "5G NR-Advanced, mmWave, DECT NR+, sub-THz / 6G, beamforming ICs, phased-array antennas, software-defined radio. RF physics meeting silicon — the layer that makes everything mobile." },
  { macroSlug: "communications", slug: "wireline", name: "Wireline",
    blurb: "Fibre optics, dark fibre and submarine cables, free-space optics, and the quantum-comms stack (QKD, repeaters, networks). The literal backbone of the internet." },
  { macroSlug: "communications", slug: "optical-interconnect", name: "Optical interconnect",
    blurb: "Linear pluggable optics (LPO), chip-level optical I/O, pluggable transceivers. Where light replaces copper inside the data centre — the layer under the CPO transition." },

  // Energy & Power
  { macroSlug: "energy-power", slug: "energy-generation", name: "Energy generation",
    blurb: "Fusion in every confinement geometry (magnetic, inertial, FRC, stellarator, z-pinch), geothermal, perovskite and tandem solar, electrolysers, carbon capture. How new electrons get made — net-zero, on the largest scales." },
  { macroSlug: "energy-power", slug: "energy-storage", name: "Energy storage",
    blurb: "Batteries across every chemistry — lithium-ion, lithium-sulphur, sodium-ion, solid-state, flow — plus compressed-air, gravity-thermal, and long-duration storage. How electrons sit still until they're needed." },
  { macroSlug: "energy-power", slug: "power-electronics", name: "Power electronics",
    blurb: "GaN-on-Si, power management ICs, wireless power transfer, GW-scale power delivery, solid-state circuit breakers. The semiconductors that move large currents — the bottleneck under AI datacentres, EVs, and the grid build-out." },
  { macroSlug: "energy-power", slug: "thermal-management", name: "Thermal management",
    blurb: "Heat pipes, vapor chambers, thermal interface materials, liquid cooling, diamond heat spreaders, graphene thermal films, phase-change materials. AI's power density already exceeds what air-cooling can dissipate — this is where the next several W/cm² come from." },

  // Manufacturing
  { macroSlug: "manufacturing", slug: "lithography", name: "Lithography",
    blurb: "EUV (including high-NA), DUV immersion, e-beam, maskless multi-beam, nanoimprint, photoresists, two-photon polymerisation, xolography. The patterning layer that gates every other layer of semiconductor scaling." },
  { macroSlug: "manufacturing", slug: "packaging", name: "Packaging",
    blurb: "3D-IC stacking, CoWoS, FOWLP, hybrid bonding, co-packaged optics, photonic wire bonding, TSV, glass interposers, substrates. Where Moore's Law has actually been alive for the last decade." },
  { macroSlug: "manufacturing", slug: "equipment-processes", name: "Equipment & processes",
    blurb: "ALD, MOCVD/MBE, PVD, CMP, iCVD, etch tools, metrology, wafer-handling, additive manufacturing, diamond-turning. The physical processes that turn substrates into devices." },
  { macroSlug: "manufacturing", slug: "foundry-design", name: "Foundry & design",
    blurb: "Foundry services, multi-project wafer (MPW), OSAT, PDKs, EDA tools, specialty foundries. The commercial machinery between a chip design and an actual wafer." },

  // Materials
  { macroSlug: "materials", slug: "substrates", name: "Substrates",
    blurb: "Silicon, SiC, GaN, GaAs, InP, Ge, diamond, sapphire. Plus 2D materials — graphene, hBN, TMDs — and the compound semiconductor family. What the device is built on." },
  { macroSlug: "materials", slug: "functional-layers", name: "Functional layers",
    blurb: "Barium titanate (BTO), thin-film lithium niobate (TFLN), scandium aluminium nitride, ferroelectric HfO₂, polymer waveguides, piezoelectric and topological materials. Engineered films that do real work — modulate light, store charge, transduce energy." },
  { macroSlug: "materials", slug: "advanced-materials", name: "Advanced materials",
    blurb: "Graphene and its 2D cousins, MXenes, carbon nanotubes, chalcogenide glasses, ceramics, novel thin films. The post-silicon material zoo — most of it not yet at production scale." },
  { macroSlug: "materials", slug: "coatings-interfaces", name: "Coatings & interfaces",
    blurb: "Anti-reflection, hydrophobic and oleophobic coatings, optical coatings, diffusion barriers. The thin films at the boundary between a device and its environment." },

  // Photonic Systems
  { macroSlug: "photonic-systems", slug: "pic-platforms", name: "PIC platforms",
    blurb: "Silicon photonics, InP, GaAs, polymer photonics, photonic ICs, heterogeneous integration. The substrates competing to be the equivalent of CMOS for light." },
  { macroSlug: "photonic-systems", slug: "light-sources", name: "Light sources",
    blurb: "DFB/DBR lasers, quantum cascade lasers, VCSELs, micro-LEDs, OLED, single-photon sources, frequency combs, holographic displays. How photons get created — across visible, IR, and increasingly mid-IR." },
  { macroSlug: "photonic-systems", slug: "modulators-detectors", name: "Modulators & detectors",
    blurb: "Mach-Zehnder modulators, electro-absorption modulators, Pockels modulators, ring resonators, spatial light modulators, avalanche and Ge/InGaAs photodiodes. How photons get manipulated and counted." },
  { macroSlug: "photonic-systems", slug: "photonic-compute", name: "Photonic compute",
    blurb: "Optical neural networks, diffractive deep neural networks, photonic tensor cores, photonic compute-memory. Doing the multiply-accumulate in light — if it scales, the AI accelerator wars get a new entrant." },
  { macroSlug: "photonic-systems", slug: "metasurfaces", name: "Metasurfaces",
    blurb: "Metalens, metasurfaces / flat optics, metamaterials, wafer-level optics. Sub-wavelength nanostructured surfaces that replace whole lens stacks with a single layer — the cheapest path to high-volume optics." },

  // Life & Frontier
  { macroSlug: "life-frontier", slug: "biotech", name: "Biotech",
    blurb: "Synthetic biology, CRISPR, DNA synthesis, single-cell sequencing, spatial transcriptomics, 3D bioprinting, biomaterials. Engineering at the cell scale — increasingly converging with the semiconductor stack." },
  { macroSlug: "life-frontier", slug: "neural-interfaces", name: "Neural interfaces",
    blurb: "Invasive BCI, non-invasive BCI, bioelectronic medicine, hearables / silent speech, AR/VR. The interface between brains and machines — both ends moving fast in 2026." },
  { macroSlug: "life-frontier", slug: "diagnostics-health", name: "Diagnostics & health",
    blurb: "Digital pathology, liquid biopsy, point-of-care diagnostics, health/fitness tracking. Measurement-first medicine — the part of healthcare most directly improved by sensing and AI." },
  { macroSlug: "life-frontier", slug: "space", name: "Space",
    blurb: "Propulsion (electric, in-space, nuclear thermal, reusable launch), LEO mega-constellations, optical inter-satellite links, earth observation, lunar surface power and ISRU. The full space-hardware stack — including the parts that have to survive the radiation environment." },
  { macroSlug: "life-frontier", slug: "ai-infrastructure", name: "AI infrastructure",
    blurb: "AI-grade datacentre real estate, GW-scale power delivery, datacentre cloud infrastructure, sovereign AI. The physical and political substrate under the AI scaling laws." },
  { macroSlug: "life-frontier", slug: "trust", name: "Trust",
    blurb: "Cybersecurity, federated learning, homomorphic encryption, MPC, zero-knowledge proofs, TEEs, differential privacy, data unions. The cryptographic and architectural layer that makes shared computation possible without shared visibility." },
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
