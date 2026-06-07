# Chapter 7 Outline: Single-Channel Randomness, Noise, Jitter, and CV

## 1. Opening Question

- Question: Why are spike times not perfectly identical even when the input looks similar?
- Target answer: ion channels open and close probabilistically, and near threshold small random differences can shift spike timing.
- Current source: `minibook_v2/source/chapters/single_channel_noise.md`.

## 2. Why This Matters

- This chapter connects microscopic channel events to spike-train variability.
- It prepares the final capstone: make a claim about noise and timing using evidence.
- Keep randomness measurable, not mysterious.

## 3. Visual First

- Required visual: `fig_11_patch_clamp_trace.svg`.
- Companion visuals: `patch_clamp_single_channel_trace.svg`, `fig_12_noise_to_jitter_panel.svg`.
- Student task: mark open and closed channel intervals on a single-channel trace.

## 4. Core Concepts And Terms To Define

- Subsection headings: Single-channel openings; Stochastic gating; Channel noise; Open fraction; Spike-time jitter; ISI variability; Coefficient of variation.
- Exact terms to define: patch clamp, single channel, open state, closed state, stochastic, noise, trial-to-trial variability, jitter, open fraction, standard deviation, CV.
- Keep standard deviation as a descriptive spread measure; do not derive it.

## 5. Read The Graph

- Graph to read: `fig_12_noise_to_jitter_panel.svg`.
- Student reads: repeated voltage traces, raster, ISI histogram, CV bar.
- Skill: use graph evidence to compare low-noise and high-noise conditions.

## 6. Worked Example And Try One Yourself

- Worked example: A channel is open for 12 ms during a 60 ms recording. What is the open fraction?
- Expected solution: 12/60 = 0.20; the channel was open 20% of the time.
- Try one: ISIs are 20, 25, 30 ms with mean 25 ms and SD 5 ms; CV = 5/25 = 0.20.

## 7. Mini Lab Or Simulation

- Mini-lab: noisy threshold-spiking notebook.
- Materials: `source/code/week7_noise_and_cv.ipynb` and `source/code/chapter07_single_channel_noise.ipynb`.
- Student output: compare low-, medium-, and high-noise spike timing with rate and CV.

## 8. Assessment And Teacher Note

- 5-question quiz:
  1. Define stochastic gating.
  2. Identify open and closed states on a trace.
  3. Calculate open fraction.
  4. Calculate CV from given mean ISI and SD.
  5. Explain why random does not mean uncaused or unmeasurable.
- Teacher note: likely misconceptions are that randomness means no mechanism, that all variability is experimental error, and that a model output is direct proof about real neurons.
