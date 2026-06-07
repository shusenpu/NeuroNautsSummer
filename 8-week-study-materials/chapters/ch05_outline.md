# Chapter 5 Outline: Spike Trains, Firing Rate, ISI, and Timing as Information

## 1. Opening Question

- Question: If action potentials are mostly the same height, how can neurons send stronger or different messages?
- Target answer: neurons can change spike number, rate, timing, intervals, and population patterns.
- Current source: `minibook_v2/source/chapters/spike_trains_rate_and_variability.md`.

## 2. Why This Matters

- This chapter shifts from one spike to patterns of spikes.
- It prepares the student to discuss information and variability with simple measurements.
- Keep the core message: rate and timing are readable features.

## 3. Visual First

- Required visual: `fig_09_spike_raster_and_rate.svg`.
- Companion visual: `spike_train_dashboard.svg`.
- Student task: count spikes in weak, medium, and strong stimulus conditions.

## 4. Core Concepts And Terms To Define

- Subsection headings: Spike trains; Raster plots; Firing rate; Interspike interval; Timing regularity; Trial-to-trial comparison; Message strength without taller spikes.
- Exact terms to define: spike train, raster plot, trial, firing rate, Hz, interspike interval, ISI, mean ISI, timing code, rate code.
- Keep calculations to counting, division, and simple averaging.

## 5. Read The Graph

- Graph to read: `spike_train_dashboard.svg`.
- Student reads: raster panel, ISI histogram, summary rate labels.
- Skill: compare two trials with similar rates but different timing.

## 6. Worked Example And Try One Yourself

- Worked example: A neuron fires 8 spikes in 1 second. What is the firing rate?
- Expected solution: 8 spikes / 1 s = 8 Hz.
- Try one: Spike times are 10, 30, 55, and 80 ms. ISIs are 20, 25, and 25 ms; mean ISI is about 23.3 ms.

## 7. Mini Lab Or Simulation

- Mini-lab: spike-time dashboard.
- Materials: `source/code/chapter05_spike_trains_rate_and_variability.ipynb` and `source/datasets/synthetic_spike_times.csv`.
- Student output: raster plot, ISI list, firing-rate sentence.

## 8. Assessment And Teacher Note

- 5-question quiz:
  1. Define spike train.
  2. Read a raster and count spikes.
  3. Calculate firing rate from spike count and time.
  4. Calculate ISIs from a short spike-time list.
  5. Explain why spike height is not the main message variable here.
- Teacher note: likely misconceptions are that information is stored in spike height, that rate and timing are the same thing, and that a raster is a voltage trace rather than a plot of spike times across trials.
