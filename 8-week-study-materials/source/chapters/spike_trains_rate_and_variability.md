# Week E / Chapter 5. Spike Trains and Neural Information

## Opening Question

How can spike timing carry information if individual spikes are mostly all-or-none?

## Learning Goals

- Show that rate and timing are both features of spike trains.
- Define spike train, spike time, firing rate, ISI, standard deviation, and CV.
- Compute firing rate from spike count and time.
- Compute ISIs from spike times.
- Explain why variability is scientifically meaningful rather than just messy data.

## Week Snapshot

| Field | Week E plan |
|---|---|
| Weekly focus | Spike trains are present but compressed |
| Chapter | Spike trains and neural information |
| Prerequisites | Weeks A-D |
| Learning objectives | Distinguish single-spike amplitude from firing rate/timing; interpret rasters and rate plots |
| Basic calculations | Spike rate, ISI, mean ISI |
| Estimated total time | 4.0-4.5 h |

## Weekly Lesson Spine

| Lesson component | Typical time | This chapter's job |
|---|---:|---|
| Visual opener | 15-20 min | See spikes as time stamps instead of tall or short events. |
| Core concept lesson | 35-45 min | Define rate, ISI, raster, standard deviation, and CV. |
| Graph/diagram-reading block | 20-30 min | Read raster, ISI histogram, and summary metrics together. |
| Worked example | 15-25 min | Compute firing rate from spike count and time. |
| Basic calculation | 15-25 min | Compute ISIs and interpret regularity. |
| Mini-lab or code | 20-40 min | Build a spike-train dashboard from synthetic data. |
| Retrieval quiz and reflection | 10-15 min | Explain how same rate can hide different timing. |

## Independent Study Scaffold

| Learning outcome | Misconception to address directly | Formative check | Support if stuck | Extension if ready |
|---|---|---|---|---|
| Interpret spike rasters and ISIs. | Information is only in spike height. | Convert a raster into a firing-rate and timing description. | Hand-count spikes before using the rate formula. | Discuss timing codes and population coding qualitatively. |

> **How to use this scaffold:** Read the outcome before starting the chapter. After each section, answer the quick check before continuing. If the answer is shaky, use the support prompt immediately; if the answer is solid, try the extension prompt.


## Prerequisites and Recap

Prerequisites: one action potential has a stereotyped shape. Recap: Chapter 4 explained single spikes. This chapter studies sequences of spikes.

## Required Vocabulary

Use this table for the chapter, and use the cumulative [Glossary](../glossary/glossary.md) when a term returns in a later week.

| Term | Student-facing definition |
|---|---|
| Spike train | Sequence of action-potential times. |
| Spike time | Time when voltage crosses threshold upward. |
| Firing rate | Spikes per second, measured in Hz. |
| ISI | Interspike interval, the time between consecutive spikes. |
| Standard deviation | A measure of spread around the mean. |
| CV | Coefficient of variation: standard deviation divided by mean. |
| Raster plot | Plot of spike times across repeated trials. |

## Misconception Box

> **Use this misconception box actively:** When one of these ideas appears, do not just mark it wrong. Replace it with the correction in your own words and give one piece of evidence from a figure, graph, or calculation.

- "Spike height is the main code." Individual spikes are mostly stereotyped, so timing, rate, and population activity matter.
- "Same firing rate means same spike train." Two spike trains can have the same count but different intervals.
- "Variability is just bad data." Variability can be measured and can reveal mechanisms or coding strategies.
- "Hz and ms are interchangeable." Hz is events per second; ms is time between events.

## Visual Opener

Draw spikes as vertical tick marks. Weak input may produce a few ticks. Stronger input may produce more ticks. Repeated trials may produce ticks at slightly different times. The dashboard figure makes the key point: two trials can have the same number of spikes in the same time window, so their average rate looks similar, while their gaps between spikes reveal different timing regularity.


### Concept Figure A: Raster And Rate

![Raster plots and rate annotations showing more frequent spikes in stronger conditions.](../figures/generated/fig_09_spike_raster_and_rate.svg)

*A stronger message is often more spikes, not taller spikes. Information can be carried by firing rate and timing, not by action-potential amplitude.*

> **What this figure is:** A teaching raster that separates spike count and timing from spike height.
>
> **What this figure is not:** It is not a claim that firing rate is the only neural code.
>
> **Source note:** Generated locally from synthetic teaching spike trains.

### Reality Figure B: Spike-Train Dashboard

![A dashboard with a raster plot, an interspike-interval histogram, and a summary metric panel.](../figures/generated/spike_train_dashboard.svg)

*Rate, interval, and variability can be read directly from spike trains.*

> **What this figure is:** A synthetic data dashboard for reading rate, ISI, and variability together.
>
> **What this figure is not:** It is not an Allen recording; it is clean teaching data designed to make the graph skills visible.
>
> **Source note:** Generated locally from synthetic spike-time data.

![Voltage trace with interspike intervals labeled.](../figures/generated/isi_measurement.svg)

*ISI is measured between consecutive threshold crossings.*

![Raster-like plot with jittered spike times across trials.](../figures/generated/random_trials.svg)

*Repeated trials can show spike-time variability.*


> **Quick Check: Visual opener**  
> **Question:** In a raster, what does one tick mark represent?  
> **Answer:** One spike time.


## Core Concept Lesson

A single spike is mostly all-or-none, so information often appears in rate, timing, and which neurons fire. ISIs turn spike timing into numbers. Mean ISI gives the average gap. Standard deviation gives spread. CV gives spread relative to average. Larger CV means more irregular timing.

> **Quick Check: Core concept**  
> **Question:** Why can rate and timing both matter?  
> **Answer:** Rate counts spikes, while timing describes the gaps and patterns between spikes.


## Graph/Diagram-Reading Block

Read the spike-train dashboard from top to bottom. In the raster, each tick is one spike time and each row is a trial. Count spikes in a fixed time window to estimate rate. Then measure gaps between neighboring ticks to get ISIs. Finally read the ISI histogram: a narrow cluster means regular timing, while a broad spread means more variability. Do not call two trials identical just because they have the same number of spikes.

> **Quick Check: Graph/diagram reading**  
> **Question:** What does a broad ISI histogram suggest?  
> **Answer:** More variable or irregular spike timing.


## Worked Example Box A

> **Study move:** Cover the solution first, try the problem, then compare your reasoning with the worked solution.

**Problem:** A neuron fires 18 spikes in 3 seconds. What is the average firing rate?

**Solution:** 18 / 3 = 6 spikes per second = 6 Hz.

## Quick Check A With Answer

**Question:** What does Hz mean?

**Answer:** Events per second.

## Basic Calculation

**Task:** Spike times are 8, 29, 37, 58, and 66 ms. Compute the ISIs.

**Answer:** The ISIs are 21, 8, 21, and 8 ms. The alternating gaps show irregular timing even though the spike count is easy to count.

## Worked Example Box B

> **Study move:** Cover the solution first, try the problem, then compare your reasoning with the worked solution.

**Problem:** Spike times are 10, 24, 38, 53, and 67 ms. Compute ISIs and approximate firing rate from mean ISI.

**Solution:** ISIs are 14, 14, 15, 14 ms. Mean ISI is 14.25 ms = 0.01425 s. Rate is about 1/0.01425 = 70.2 Hz.

## Quick Check B With Answer

**Question:** What does a larger CV mean?

**Answer:** More irregular timing relative to the average interval.

## Mini-Lab or Code

Run `notebooks/chapter05_spike_trains_rate_and_variability.ipynb` or make a spreadsheet with two rows of spike times. For each row, compute ISIs and average rate. Then make one claim that uses both pieces of evidence, such as: "These trials have similar spike counts but different interval patterns."

> **Quick Check: Mini-lab**  
> **Question:** Why compare spike count and ISIs in the same claim?  
> **Answer:** The same count can hide different timing patterns.


## Interactive Exercise

Use `neuro_book/datasets/synthetic_spike_times.csv`. Pick one condition, make a raster by hand or in a spreadsheet, then compute the first three ISIs.

> **Quick Check: Interactive exercise**  
> **Question:** Before computing rate, what should you identify in the CSV or raster?  
> **Answer:** The time window and the spike times in that window.


## Retrieval Quiz and Reflection

1. Define spike train, firing rate, ISI, raster plot, and CV.
2. A train has 12 spikes in 2 seconds. What is the firing rate?
3. Why can two trials with the same rate still look different?
4. What does a larger CV suggest?

**Answers:** A spike train is a sequence of spike times; firing rate is spikes per second; ISI is the gap between spikes; a raster shows spike times across trials; CV is relative interval variability. 12 spikes/2 seconds = 6 Hz. Same rate can hide different timing because the gaps may differ. Larger CV suggests more irregular timing.

**Assessment checkpoint:** The student is ready to move on when she can read a raster and explain what the graph shows before naming a mechanism.

## Chapter Summary

Chapter 5 answers the opening question by connecting the visual story to a mechanism the student can explain without calculus. The key move is: A single spike is mostly all-or-none, so information often appears in rate, timing, and which neurons fire.

## Homework

### Questions

1. Compute ISIs for spike times 80, 125, 166, 210, and 260 ms.
2. Explain why two spike trains can have the same firing rate but different timing.
3. Graph-reading: in a raster, what does one tick mark mean and what does one row mean?
4. Quantitative: a neuron fires 24 spikes in 3 seconds. What is the firing rate?
5. Misconception check: explain why taller spikes are not the main code in this chapter.
6. Extension: use `synthetic_spike_times.csv` to choose one condition and compute two ISIs.

### Answer Key

1. ISIs are 45, 41, 44, and 50 ms.
2. They can contain the same number of spikes in the same time window but have different gaps between spikes.
3. One tick is one spike time; one row is usually one trial.
4. 24/3 = 8 Hz.
5. Individual spikes are mostly stereotyped; rate, timing, and which neurons fire can carry information.
6. Answers depend on condition. For low_noise trial 1, the first two ISIs are 103 ms and 104 ms.

## Stretch Box

> Find or sketch two spike trains with the same rate but different CV. Explain which one is more regular.

## Mentor Note

> Make the student calculate from spike times by hand before using a spreadsheet. The hand calculation makes CV meaningful.

## Glossary Additions

- Spike train
- Spike time
- Firing rate
- ISI
- CV
- Raster plot

## Source Notes

| Figure | Asset | Caption | Alt text | Source notes |
|---|---|---|---|---|
| 5.1 | `spike_code.svg` | Stimulus strength can be represented by spike timing and frequency. | Spike trains for weak, medium, and strong inputs. | Original generated course plot. |
| 5.2 | `isi_measurement.svg` | ISI is measured between consecutive threshold crossings. | Voltage trace with interspike intervals labeled. | Original generated course figure. |
| 5.3 | `random_trials.svg` | Repeated trials can show spike-time variability. | Raster-like plot with jittered spike times across trials. | Original generated course figure. |
| spike_train_dashboard | `spike_train_dashboard.svg` | Rate, interval, and variability can be read directly from spike trains. | A dashboard with a raster plot, an interspike-interval histogram, and a summary metric panel. | Generated locally from synthetic teaching data. |
