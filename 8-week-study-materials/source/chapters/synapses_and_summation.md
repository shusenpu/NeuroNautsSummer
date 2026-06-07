# Week C / Chapter 3. Graded Signals and Threshold

## Opening Question

How do many small synaptic inputs combine before a neuron fires?

## Learning Goals

- Define synapse, neurotransmitter, receptor, EPSP, IPSP, and graded potential.
- Distinguish graded potentials from action potentials.
- Explain temporal and spatial summation.
- Use simple arithmetic to reason about threshold without pretending the neuron is that simple.

## Week Snapshot

| Field | Week C plan |
|---|---|
| Current minibook anchor | Synapses and threshold |
| Revised textbook-style chapter | Graded signals and threshold |
| Prerequisites | Weeks A-B |
| Learning objectives | Explain EPSPs, IPSPs, temporal/spatial summation, trigger zone |
| Basic calculations | Add simple EPSP values to estimate threshold approach |
| Estimated total time | 4.0-4.5 h |

## Weekly Lesson Spine

| Lesson component | Typical time | This chapter's job |
|---|---:|---|
| Visual opener | 15-20 min | Follow neurotransmitter from presynaptic terminal to postsynaptic channels. |
| Core concept lesson | 35-45 min | Define EPSPs, IPSPs, graded potentials, and summation. |
| Graph/diagram-reading block | 20-30 min | Read a summation diagram with baseline and threshold marked. |
| Worked example | 15-25 min | Add small excitatory and inhibitory voltage changes. |
| Basic calculation | 15-25 min | Compare final V_m to threshold. |
| Mini-lab or code | 20-40 min | Build a paper, spreadsheet, or notebook summation model. |
| Retrieval quiz and reflection | 10-15 min | Explain why graded potentials are not action potentials. |

## Independent Study Scaffold

| Learning outcome | Misconception to address directly | Formative check | Support if stuck | Extension if ready |
|---|---|---|---|---|
| Explain EPSP, IPSP, and summation. | Any single input automatically causes a spike. | Predict whether a short input sequence reaches threshold. | Use tactile tokens or number-line cards for summation. | Add inhibitory inputs and discuss location effects. |

> **How to use this scaffold:** Read the outcome before starting the chapter. After each section, answer the quick check before continuing. If the answer is shaky, use the support prompt immediately; if the answer is solid, try the extension prompt.


## Prerequisites and Recap

Prerequisites: membrane potential can move up or down, and opening channels pulls voltage toward ion reversal potentials. Recap: Chapter 2 explained why channel opening changes voltage. This chapter applies that idea to synaptic input.

## Required Vocabulary

Use this table for the chapter, and use the cumulative [Glossary](../glossary/glossary.md) when a term returns in a later week.

| Term | Student-facing definition |
|---|---|
| Synapse | Communication point between neurons or between a neuron and another cell. |
| Neurotransmitter | Chemical messenger released by a presynaptic cell. |
| Receptor | Postsynaptic protein that responds to neurotransmitter. |
| EPSP | Excitatory postsynaptic potential, usually toward threshold. |
| IPSP | Inhibitory postsynaptic potential, usually away from threshold or stabilizing. |
| Graded potential | Local voltage change that can vary in size. |
| Temporal summation | Inputs close together in time add up. |
| Spatial summation | Inputs from different locations add up. |

## Misconception Box

> **Use this misconception box actively:** When one of these ideas appears, do not just mark it wrong. Replace it with the correction in your own words and give one piece of evidence from a figure, graph, or calculation.

- "Every voltage change is an action potential." Synaptic potentials are usually local, graded changes before threshold.
- "Inhibition means the neuron is turned off." Inhibition can hyperpolarize, stabilize, or reduce the effect of excitation.
- "EPSPs add perfectly forever." Real graded potentials fade over time and distance.
- "Threshold is reached at every synapse." Threshold is usually evaluated near the trigger zone, not at every dendritic input.

## Visual Opener

A presynaptic terminal releases neurotransmitter into a narrow cleft. Receptors on the postsynaptic cell open channels. The local voltage nudges upward or downward. Many nudges can combine before the trigger zone reaches threshold.


### Concept Figure A: Synapse And Postsynaptic Potentials

![Presynaptic terminal releasing transmitter onto postsynaptic membrane, with excitatory and inhibitory examples.](../figures/generated/fig_06_synapse_and_psps.svg)

*Synapses change postsynaptic voltage. The same neuron may be pushed toward or away from threshold depending on which channels open.*

> **What this figure is:** A conceptual synapse diagram paired with EPSP and IPSP voltage effects.
>
> **What this figure is not:** It is not a full chemical-reaction map of neurotransmitter release and receptor kinetics.
>
> **Source note:** Generated locally from OpenStax-style synapse and graded-potential concepts.

### Reality Figure B: Summation Graph

![Graph of multiple graded potentials summing toward a threshold line.](../figures/generated/fig_07_summation_graph.svg)

*Small inputs can combine before a spike begins. Threshold depends on the total membrane effect of multiple graded inputs.*

> **What this figure is:** A trace-reading exercise for temporal and spatial summation.
>
> **What this figure is not:** It is not a guarantee that real dendrites add inputs with simple arithmetic.
>
> **Source note:** Generated locally as a simplified summation graph using threshold as the reading anchor.

![Feedback diagram from depolarization to Na+ channel opening.](../figures/generated/threshold_feedback.svg)

*Threshold begins feedback, but synaptic inputs before threshold are graded.*

> **Quick Check: Visual opener**  
> **Question:** What changes on the postsynaptic cell after neurotransmitter binds?  
> **Answer:** Receptor-controlled channels open and create a graded voltage change.


## Core Concept Lesson

Synaptic potentials are local and graded. An EPSP often depolarizes the postsynaptic membrane. An IPSP often hyperpolarizes the membrane or makes it harder to depolarize. Because these voltage changes can overlap, the trigger zone receives a running total of recent inputs. If the total reaches threshold, the next chapter's action-potential machinery takes over.

> **Quick Check: Core concept**  
> **Question:** Why are synaptic potentials called graded?  
> **Answer:** Their size can vary; they are not all-or-none spikes.


## Graph/Diagram-Reading Block

Read the summation diagram before doing arithmetic. First locate the resting baseline, usually near -70 mV in these examples. Second locate threshold, here -55 mV. Third mark each EPSP as an upward nudge and each IPSP as a downward or stabilizing nudge. Fourth ask whether the combined trace crosses threshold. The key graph skill is comparing a changing V_m trace against a fixed threshold line.

> **Quick Check: Graph/diagram reading**  
> **Question:** What line should you compare the summed trace against?  
> **Answer:** The threshold line.


## Worked Example Box A

> **Study move:** Cover the solution first, try the problem, then compare your reasoning with the worked solution.

**Problem:** Start at -70 mV. Inputs are +4, +5, +6, and -3 mV. Threshold is -55 mV. Does the neuron reach threshold?

**Solution:** -70 + 4 + 5 + 6 - 3 = -58 mV. It does not reach -55 mV; it is 3 mV below threshold.

## Quick Check A With Answer

**Question:** Are graded potentials all-or-none?

**Answer:** No. They vary in size and can fade.

## Basic Calculation

**Task:** Start at -70 mV. Three EPSPs add +3 mV, +4 mV, and +5 mV. One IPSP adds -4 mV. What is the final V_m, and does it reach -55 mV threshold?

**Answer:** -70 + 3 + 4 + 5 - 4 = -62 mV. It does not reach threshold; it is 7 mV below -55 mV.

## Worked Example Box B

> **Study move:** Cover the solution first, try the problem, then compare your reasoning with the worked solution.

**Problem:** Two +6 mV EPSPs arrive far apart and fade before overlapping. A different pair arrives close together. Which pair is more likely to reach threshold?

**Solution:** The close-together pair is more likely to add because their voltage effects overlap in time.

## Quick Check B With Answer

**Question:** What is the difference between temporal and spatial summation?

**Answer:** Temporal summation adds inputs across time; spatial summation adds inputs from different locations.

## Mini-Lab or Code

Make four index cards labeled `+3 mV`, `+5 mV`, `-4 mV`, and `+6 mV`. Place them on a number line starting at -70 mV and move the marker as each card arrives. Repeat with the cards closer together and farther apart. If using the notebook, run `notebooks/chapter03_synapses_and_summation.ipynb` and explain why a trace may rise, fade, and fail to cross threshold.

> **Quick Check: Mini-lab**  
> **Question:** Why do index cards help in this chapter?  
> **Answer:** They make EPSPs and IPSPs visible as small additions or subtractions.


## Interactive Exercise

Use the summation graph like a slider exercise: change one EPSP from +3 mV to +6 mV and predict whether the combined trace reaches threshold before calculating.

> **Quick Check: Interactive exercise**  
> **Question:** What should you predict before recalculating a changed EPSP?  
> **Answer:** Whether the combined V_m reaches threshold.


## Retrieval Quiz and Reflection

1. Define EPSP, IPSP, and graded potential.
2. Explain temporal summation in one sentence.
3. Explain spatial summation in one sentence.
4. Why is threshold a transition point rather than just another small input?

**Answers:** EPSPs usually move V_m toward threshold; IPSPs usually oppose firing or stabilize V_m; graded potentials vary in size. Temporal summation is addition across time. Spatial summation is addition across locations. Threshold starts the self-amplifying action-potential process.

**Assessment checkpoint:** The student is ready to move on when she can read a summation trace and decide whether threshold is reached before using the word "spike."

## Chapter Summary

Chapter 3 answers the opening question by connecting the visual story to a mechanism the student can explain without calculus. The key move is: Synaptic potentials are local and graded.

## Homework

### Questions

1. Write a six-sentence mini-lesson explaining EPSP, IPSP, graded potential, and threshold.
2. Create and solve two threshold arithmetic problems, one that reaches threshold and one that does not.
3. Graph-reading: on the summation graph, mark the threshold line and the point where the combined input comes closest to it.
4. Quantitative: start at -70 mV. Add +5, +4, +3, and -2 mV. Does V_m reach -55 mV?
5. Misconception check: explain why an IPSP is not simply "turning the neuron off."
6. Extension: explain why two EPSPs close together in time can matter more than the same two EPSPs far apart.

### Answer Key

1. A complete answer says EPSPs tend to move toward threshold, IPSPs tend to oppose firing or stabilize voltage, graded potentials vary in size, and threshold is where spike feedback begins.
2. Answer key should show starting voltage, input changes, final voltage, threshold comparison, and conclusion.
3. The threshold line is the fixed comparison line; the closest point is the peak of the summed trace.
4. -70 + 5 + 4 + 3 - 2 = -60 mV, so it does not reach -55 mV.
5. Inhibition can hyperpolarize, stabilize V_m, or reduce the effect of excitation; it shapes probability of firing.
6. Close EPSPs overlap before fading, so their effects can add at the trigger zone.

## Stretch Box

> Explain why inhibition is not just 'turning the neuron off.' Include the idea that inhibition can stabilize voltage or reduce the effect of excitation.

## Mentor Note

> Keep saying 'graded is not spike.' This chapter exists so the student does not collapse every voltage change into an action potential.

## Glossary Additions

- Synapse
- EPSP
- IPSP
- Graded potential
- Temporal summation
- Spatial summation

## Source Notes

| Figure | Asset | Caption | Alt text | Source notes |
|---|---|---|---|---|
| 3.1 | `synapse.svg` | Chemical synapses change postsynaptic voltage by opening receptor-controlled channels. | Diagram of presynaptic terminal, cleft, and postsynaptic channels. | Original generated course figure. |
| 3.2 | `synapse_summation_diagram.svg` | Small excitatory and inhibitory inputs sum in time and space before threshold is reached. | Combined synapse and summation diagram using baseline -70 mV and threshold -55 mV. | Generated locally as a vector redraw from standard textbook synapse and summation concepts. |
| 3.3 | `threshold_feedback.svg` | Threshold begins feedback, but synaptic inputs before threshold are graded. | Feedback diagram from depolarization to Na+ channel opening. | Original generated course figure. |
