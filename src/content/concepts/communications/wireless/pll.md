---
type: concept
slug: pll
canonical_name: Phase-Locked Loop
aliases:
- PLL
- phase locked loop
- phase-locked loops
- phase locked loops
parent_concepts: []
related_concepts: []
sources: []
auto_stub: true
last_updated: '2026-08-31'
tags:
- concept
- auto-stub
mention_count: 4
frontier:
- What measured SINR gain does joint channel and phase noise estimation deliver over CPE-only compensation in OTFS, and how does that gain differ between continuous-time and discrete-time PLL references 2026 05 15 joint phase noise and channel estimation for otfs?
- What absolute power consumption and jitter does the a-IGZO TFT PLL achieve, and what fraction of a flexible AMS system's power budget does it occupy compared with the up-to-90% figure cited for alternative clock sources 2026 08 03 low power pll based clock stabilization for flexible igzo am?
- By what factor does hybrid-loop demodulation exceed conventional PLL bandwidth as a function of sensor resonant frequency, and does it introduce additional noise at that bandwidth 2026 06 04 high temperature and high speed atomic force microscopy usin?
- Has the proposed 1596 nm multi-wavelength arm-length stabilisation scheme been demonstrated experimentally on an AlGaAs/GaAs-coated cavity, and does it reach the residual velocity required for lock acquisition 2026 06 24 a novel arm length stabilization scheme for gravitational wa?
sources_7d: 0
sources_30d: 1
recent_mentions: []
neighbors: []
---
## Physics / mechanism

A phase-locked loop is a feedback system that forces the phase of a locally generated oscillator to track that of a reference signal. The loop compares reference and output phase, filters the resulting error, and uses it to steer the oscillator, so the output inherits the long-term stability of the reference while retaining the oscillator's short-term properties. The consequence for communications hardware is a bounded phase noise spectrum: within the loop bandwidth, oscillator drift is suppressed by the feedback; outside it, the free-running oscillator noise dominates. PLLs are commonly analysed in either continuous-time or discrete-time form, and the two give different phase noise power spectral densities and hence different link-level penalties joint phase noise and channel estimation for otfs.

The key design parameter is loop bandwidth, which sets the trade-off between tracking speed and noise rejection. This appears directly in measurement applications: in frequency-modulation atomic force microscopy, the PLL demodulator's bandwidth limits how quickly a shift in the cantilever resonance frequency can be recovered, and this limit becomes binding for low-resonant-frequency sensors. A hybrid-loop frequency demodulation technique was reported to provide wider bandwidth than a conventional PLL for such low-$f_0$ sensors, enabling high-speed imaging with a qPlus sensor high temperature and high speed atomic force microscopy usin.

In receivers, residual PLL phase noise sets a floor on achievable SINR. Analysis of orthogonal time frequency space (OTFS) modulation derives SINR expressions for free-running oscillators, continuous-time PLLs and discrete-time PLLs, and shows that phase noise in the delay-Doppler domain produces inter-Doppler interference (IDI) in addition to a common phase error (CPE). Estimation schemes that correct only the CPE cannot suppress the IDI term, so the oscillator model, and by extension the PLL architecture, propagates directly into achievable data rate joint phase noise and channel estimation for otfs.

The same locking principle appears in optical and precision-metrology control loops, where auxiliary laser beams are phase-locked to bring long optical cavities into resonance. A proposed multi-wavelength arm-length stabilisation scheme for gravitational-wave detectors with AlGaAs/GaAs coatings uses frequency-doubled and frequency-tripled beams, with a 1596 nm auxiliary locking beam chosen to avoid the excessive absorption of a 532 nm beam by those coatings a novel arm length stabilization scheme for gravitational wa.

## Competitive landscape

The direct alternative to a PLL for on-chip clock generation is a free-running oscillator, which is simpler and lower power but suffers unbounded process, voltage and temperature (PVT) drift that degrades signal integrity; other clock sources can consume up to 90% of a flexible electronics system's power budget, which rules them out for that platform low power pll based clock stabilization for flexible igzo am. In frequency demodulation, hybrid-loop schemes compete with conventional PLLs on bandwidth for low-resonant-frequency sensors high temperature and high speed atomic force microscopy usin.

| Approach | Reported position |
|---|---|
| Free-running oscillator | Lowest complexity; unbounded PVT drift low power pll based clock stabilization for flexible igzo am; worst phase noise case in OTFS SINR analysis joint phase noise and channel estimation for otfs |
| Continuous-time PLL | Distinct phase noise model and SINR expression joint phase noise and channel estimation for otfs |
| Discrete-time PLL | Distinct phase noise model and SINR expression joint phase noise and channel estimation for otfs |
| Hybrid-loop demodulator | Wider bandwidth than conventional PLL for low-$f_0$ sensors high temperature and high speed atomic force microscopy usin |

## Evidence base

- 15 May 2026: SINR expressions derived for OTFS under three oscillator types, free-running, continuous-time PLL and discrete-time PLL, with the analysis showing OTFS is sensitive to phase noise and requires estimation and compensation joint phase noise and channel estimation for otfs.
- 15 May 2026: phase-noise-imposed inter-Doppler interference is reported as severe, and CPE-only estimation techniques cannot compensate it effectively; existing OTFS phase noise work assumes a known single-tap channel, motivating a joint channel and phase noise estimator joint phase noise and channel estimation for otfs.
- 4 June 2026: a hybrid-loop frequency demodulation technique for low-$f_0$ sensors was established with wider bandwidth than a conventional PLL, used in an AFM achieving atomic-resolution imaging of molten metal/solid interfaces above 200 °C with a 2.3 g qPlus sensor load on a Quadpod scanner (7.05 kHz lateral / 29.7 kHz vertical unloaded resonances) high temperature and high speed atomic force microscopy usin.
- 24 June 2026: a multi-wavelength arm-length stabilisation scheme was proposed for future gravitational-wave detector upgrades incorporating AlGaAs/GaAs coatings, using a 1596 nm auxiliary locking beam because the existing frequency-doubled 532 nm approach is excessively absorbed by those coatings a novel arm length stabilization scheme for gravitational wa.
- 3 August 2026: the first PLL architecture for n-type-only amorphous IGZO thin-film transistor technology was presented, targeting flexible electronics where alternative clock sources can consume up to 90% of total system power low power pll based clock stabilization for flexible igzo am.

## Frontier (open questions)

- What measured SINR gain does joint channel and phase noise estimation deliver over CPE-only compensation in OTFS, and how does that gain differ between continuous-time and discrete-time PLL references joint phase noise and channel estimation for otfs?
- What absolute power consumption and jitter does the a-IGZO TFT PLL achieve, and what fraction of a flexible AMS system's power budget does it occupy compared with the up-to-90% figure cited for alternative clock sources low power pll based clock stabilization for flexible igzo am?
- By what factor does hybrid-loop demodulation exceed conventional PLL bandwidth as a function of sensor resonant frequency, and does it introduce additional noise at that bandwidth high temperature and high speed atomic force microscopy usin?
- Has the proposed 1596 nm multi-wavelength arm-length stabilisation scheme been demonstrated experimentally on an AlGaAs/GaAs-coated cavity, and does it reach the residual velocity required for lock acquisition a novel arm length stabilization scheme for gravitational wa?

*Synthesised 2026-08-31 from 4 KB sources by the resynth pipeline; citations are KB source slugs.*
