# Week G / Chapter 7. From Single Channels to Timing Variability

## Opening Question

Why are spike times not perfectly identical even when the input looks similar?

## Learning Goals

- Explain what a single-channel recording shows.
- Define stochastic, open probability, open fraction, and channel noise.
- Explain why larger channel populations average randomness better.
- Connect random channel openings to spike-time variability near threshold.

## Week Snapshot

| Field | Week G plan |
|---|---|
| Current minibook anchor | Random channels and variability |
| Revised textbook-style chapter | From single channels to timing variability |
| Prerequisites | Weeks A-F |
| Learning objectives | Explain stochastic gating, channel noise, finite-size fluctuations, CV of ISI, trial-to-trial jitter |
| Basic calculations | ISI SD and CV; open-fraction fluctuations from repeated trials |
| Estimated total time | 4.5-5.0 h |

## Weekly Lesson Spine

| Lesson component | Typical time | This chapter's job |
|---|---:|---|
| Visual opener | 15-20 min | Read single-channel current steps as open/closed events. |
| Core concept lesson | 35-45 min | Define stochastic behavior, open probability, open fraction, and channel noise. |
| Graph/diagram-reading block | 20-30 min | Compare patch-clamp steps, state diagrams, and noise-scaling histograms. |
| Worked example | 15-25 min | Compute open fraction from time open. |
| Basic calculation | 15-25 min | Compute open fraction from number of open channels. |
| Mini-lab or code | 20-40 min | Use coins or a noisy threshold notebook to connect randomness to CV. |
| Retrieval quiz and reflection | 10-15 min | Explain how molecular randomness can affect spike timing. |

## Independent Study Scaffold

| Learning outcome | Misconception to address directly | Formative check | Support if stuck | Extension if ready |
|---|---|---|---|---|
| Explain why finite random channel populations can jitter spike timing. | Randomness means there is no mechanism. | Compute ISI mean and CV from a short list. | Use coin-flip analogies and repeated-trial visuals. | Compare deterministic and stochastic simulations. |

> **How to use this scaffold:** Read the outcome before starting the chapter. After each section, answer the quick check before continuing. If the answer is shaky, use the support prompt immediately; if the answer is solid, try the extension prompt.


## Prerequisites and Recap

Prerequisites: HH variables describe average channel behavior. Recap: Chapter 6 used smooth conductances. This chapter asks what changes when channels are individual random molecules.

## Required Vocabulary

Use this table for the chapter, and use the cumulative [Glossary](../glossary/glossary.md) when a term returns in a later week.

| Term | Student-facing definition |
|---|---|
| Stochastic | Involving randomness. |
| Open probability | Chance that a channel is open. |
| Open fraction | Open channels divided by total channels. |
| Channel noise | Fluctuations from random channel openings and closings. |
| Markov state | Simplified channel condition such as closed, open, or inactivated. |
| Threshold jitter | Small shifts in spike time caused by voltage fluctuations near threshold. |

## Misconception Box

> **Use this misconception box actively:** When one of these ideas appears, do not just mark it wrong. Replace it with the correction in your own words and give one piece of evidence from a figure, graph, or calculation.

- "Random means unscientific." Random processes can have measurable probabilities and patterns.
- "A channel opens halfway when the current is half as large." In the beginner picture, one channel switches open or closed; averages can be fractional.
- "Noise disappears when many channels are present." Many channels reduce relative noise, but do not make molecular randomness vanish.
- "Variability only matters after spikes happen." Noise near threshold can help decide when spikes happen.

## Visual Opener

A patch-clamp trace looks like square steps. Closed means baseline. Open means current step. Many channels summed together look smoother, but the molecules underneath are still random.


### Concept Figure A: Patch Clamp And Single-Channel Trace

![Pipette attached to membrane and a current trace jumping between closed and open states.](../figures/generated/fig_11_patch_clamp_trace.svg)

*Single channels open all-or-none, but the timing of openings is random.*

> **What this figure is:** A conceptual patch-clamp setup paired with a square-step current trace.
>
> **What this figure is not:** It is not a raw trace from the student's own experiment.
>
> **Source note:** Conceptual redraw based on standard patch-clamp and single-channel recording teaching diagrams.

### Reality Figure B: Noise To Timing Jitter

![Voltage traces and spike-timing summaries comparing low-, medium-, and high-noise conditions.](../figures/generated/fig_12_noise_to_jitter_panel.svg)

*Small fluctuations can shift threshold crossing time. Near threshold, noise changes spike timing even when the average input is similar.*

> **What this figure is:** A model-data panel that links voltage fluctuations, spike timing, ISIs, and CV.
>
> **What this figure is not:** It is not proof that every biological variability source is channel noise.
>
> **Source note:** Generated locally from a simple threshold/noise modeling workflow compatible with the capstone arc.

![State diagram from closed states to conducting state.](../figures/generated/k_channel_states.svg)

*A simplified K+ channel state diagram prepares the student for stochastic channel models.*

![Histograms comparing open fraction spread for different channel counts.](../figures/generated/channel_noise_scaling.svg)

*Bigger channel populations have smaller relative fluctuations.*

![Voltage traces and ISI histograms for low and high noise.](../figures/generated/lif_noise.svg)

*A noisy threshold model shows how noise can change ISI variability.*

> **Quick Check: Visual opener**  
> **Question:** What does a square step in a single-channel trace usually mean?  
> **Answer:** A channel changed state, such as closed to open or open to closed.


## Core Concept Lesson

A single channel does not usually open halfway in the beginner picture. It switches between closed and open states. The time of switching is random. If the membrane has many channels, random openings partly average out. If the membrane has fewer channels or the neuron is near threshold, random fluctuations can change exactly when the next spike occurs.

> **Quick Check: Core concept**  
> **Question:** How can one channel be all-or-none while a population average is fractional?  
> **Answer:** Each channel is open or closed, but the fraction open across many channels can be between 0 and 1.


## Graph/Diagram-Reading Block

Read the patch-clamp and noise figures in layers. In the single-channel trace, a flat baseline means closed and a step means open. In the state diagram, arrows mean possible transitions, not guaranteed schedules. In the open-fraction histogram, compare spread: more channels produce a tighter distribution. In the noisy threshold figure, connect voltage wobble to changed threshold-crossing times and wider ISI distributions.

> **Quick Check: Graph/diagram reading**  
> **Question:** What happens to relative fluctuation when the number of channels gets larger?  
> **Answer:** It usually becomes smaller because random openings average out better.


## Worked Example Box A

> **Study move:** Cover the solution first, try the problem, then compare your reasoning with the worked solution.

**Problem:** A channel is open for 6 ms in a 20 ms recording. What is the open fraction?

**Solution:** 6/20 = 0.30.

## Quick Check A With Answer

**Question:** Why does a single-channel trace look jumpy?

**Answer:** Because the channel switches between closed and open states.

## Basic Calculation

**Task:** At one instant, 18 out of 60 channels are open. What is the open fraction?

**Answer:** 18/60 = 0.30. This means 30% of the channels are open at that instant.

## Worked Example Box B

> **Study move:** Cover the solution first, try the problem, then compare your reasoning with the worked solution.

**Problem:** 30 out of 100 channels are open at one moment. What is the open fraction?

**Solution:** 30/100 = 0.30.

## Quick Check B With Answer

**Question:** Why do larger channel populations have smaller relative noise?

**Answer:** Random openings average out better when many channels are summed.

## Mini-Lab or Code

Do the coin mini-lab first: flip 20 coins ten times and write the fraction heads each time; then repeat with 100 coins or a spreadsheet random-number simulation. The larger group should fluctuate less in relative terms. Then run `notebooks/chapter07_single_channel_noise.ipynb` and explain how increasing noise changes spike count, rate, or CV in the simple threshold model.

> **Quick Check: Mini-lab**  
> **Question:** Why compare 20 coin flips with 100 coin flips?  
> **Answer:** To see that larger populations have less relative randomness.


## Interactive Exercise

Use the noisy threshold notebook as a slider exercise. Change only `noise_sd`, rerun, and record spike count, rate, and CV for three values.

> **Quick Check: Interactive exercise**  
> **Question:** When changing noise_sd, what variables should you record?  
> **Answer:** Spike count, firing rate, and CV or ISI spread.


## Retrieval Quiz and Reflection

1. Define stochastic, open probability, open fraction, and channel noise.
2. Why can an average open fraction be 0.30 even though one channel is either closed or open?
3. Why does noise matter more near threshold?
4. Give the causal chain from random channel opening to variable ISI.

**Answers:** Stochastic means random; open probability is chance of being open; open fraction is open channels divided by total channels; channel noise is fluctuation from random openings and closings. A population average can be fractional even when individual channels are all-or-none. Near threshold, small voltage fluctuations can change crossing time. Random opening -> current fluctuation -> voltage fluctuation -> threshold jitter -> ISI variability.

**Assessment checkpoint:** The student is ready for the capstone when she can explain why a random molecular event can produce a measurable change in a spike-train statistic.

## Chapter Summary

Chapter 7 answers the opening question by connecting the visual story to a mechanism the student can explain without calculus. The key move is: A single channel does not usually open halfway in the beginner picture.

## Homework

### Questions

1. Flip 20 coins ten times and record fraction heads. Then flip 100 coins ten times. Which set is less jumpy?
2. Write the chain from molecular event to spike-time variability.
3. Graph-reading: in the patch-clamp trace, what does a square step usually represent?
4. Quantitative: 12 channels out of 40 are open. What is the open fraction?
5. Misconception check: explain why "random" does not mean "not measurable."
6. Extension: explain why threshold makes small noise more important.

### Answer Key

1. The 100-coin fractions should usually be less jumpy because larger samples average randomness better.
2. Random channel openings -> noisy current -> voltage fluctuation -> threshold jitter -> variable ISIs.
3. A square step usually represents a channel opening or closing, changing current.
4. 12/40 = 0.30.
5. Random processes can still have probabilities, averages, distributions, and repeatable statistics.
6. Near threshold, a small voltage fluctuation can shift whether or when V_m crosses threshold.

## Stretch Box

> Explain why channel noise may matter more near threshold than far below threshold.

## Mentor Note

> This is the thesis bridge. Keep the claim qualitative: random molecular events can influence macroscopic spike timing. Do not require stochastic calculus.

## Glossary Additions

- Stochastic
- Open probability
- Open fraction
- Channel noise
- Threshold jitter

## Source Notes

| Figure | Asset | Caption | Alt text | Source notes |
|---|---|---|---|---|
| 7.1 | `patch_clamp_single_channel_trace.svg` | Single channels open all-or-none, but the timing of openings is random. | Conceptual patch-clamp cartoon paired with a step-like single-channel current trace. | Conceptual redraw based on standard Molecular Biology of the Cell patch-clamp teaching diagrams. |
| 7.2 | `k_channel_states.svg` | A simplified K+ channel state diagram prepares the student for stochastic channel models. | State diagram from closed states to conducting state. | Original generated course figure. |
| 7.3 | `channel_noise_scaling.svg` | Bigger channel populations have smaller relative fluctuations. | Histograms comparing open fraction spread for different channel counts. | Original generated course plot. |
| 7.4 | `lif_noise.svg` | A noisy threshold model shows how noise can change ISI variability. | Voltage traces and ISI histograms for low and high noise. | Original generated course plot. |
