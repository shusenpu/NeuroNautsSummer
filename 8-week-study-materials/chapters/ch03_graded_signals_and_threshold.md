# Chapter 3. Graded Signals and Threshold

## Opening Question

How can many small synaptic inputs push a neuron toward or away from firing?

A neuron does not usually fire because one tiny input arrives. Most of the time, inputs are smaller voltage changes that must be combined. Some inputs make the membrane potential less negative. These are excitatory postsynaptic potentials, or EPSPs. Other inputs make the membrane potential more negative or harder to bring to threshold. These are inhibitory postsynaptic potentials, or IPSPs.

The key word is **graded**. A graded signal can be small, medium, or large. It can fade with time and distance. This is different from an action potential, which is usually all-or-none. In this chapter, the neuron is like a decision system: many graded inputs arrive, and the trigger zone responds to their combined effect.

> **Key idea**
> A synaptic input is usually not the spike itself. It is a small voltage change that can combine with other inputs.

## Why This Matters

Chapter 2 explained why a resting neuron can sit near a negative voltage such as -70 mV. This chapter explains how that voltage can be nudged. A synapse is a communication point between cells. In a chemical synapse, the presynaptic terminal releases neurotransmitter. Neurotransmitter crosses a tiny gap called the synaptic cleft and binds receptors on the postsynaptic cell. Those receptors affect ion channels, and ion movement changes the postsynaptic membrane potential.

This is where biology becomes a decision story. A single EPSP might move the membrane from -70 mV to -66 mV. That is a change, but it may not be enough to reach threshold. Several EPSPs close together can add. An IPSP can cancel part of that effect. The final question is not "Did one input arrive?" The better question is "What is the combined effect at the trigger zone?"

## What You Already Need to Know

You need the neuron map from Chapter 1 and resting voltage from Chapter 2. Dendrites and soma are common input regions. The axon initial segment is often the trigger region. Membrane potential is measured in mV. A change from -70 mV to -60 mV is upward and less negative. A change from -70 mV to -75 mV is downward and more negative.

You also need the idea of membrane channels. Synapses often work by opening or closing channels. Which channels open determines whether the postsynaptic voltage is pushed toward or away from threshold.

The calculations here are simple addition. We will use rough numbers to learn the logic, not to pretend real neurons are this simple.

## Visual First

![Synapse and postsynaptic potentials](../source/figures/generated/fig_06_synapse_and_psps.svg)

Figure 3.1. Synapses change postsynaptic voltage.

Start by naming the parts. The presynaptic terminal contains vesicles with neurotransmitter. The synaptic cleft is the narrow space between cells. Receptors sit on the postsynaptic membrane. When transmitter binds receptors, channels can open. If the channel effect makes the inside less negative, the result is an EPSP. If it makes the cell more negative or harder to spike, the result is an IPSP.

This figure is a conceptual diagram. It does not show all molecular details. Its purpose is to connect a biological event, transmitter release, to a voltage effect, EPSP or IPSP.

> **Try it**
> On Figure 3.1, draw one arrow for chemical communication and one arrow for voltage change. They are related, but they are not the same thing.

## Core Concepts

An **EPSP** is an excitatory postsynaptic potential. It moves V_m toward threshold. It does not guarantee a spike. An **IPSP** is an inhibitory postsynaptic potential. It moves V_m away from threshold or makes threshold harder to reach. Inhibition is not simply "turning off" the neuron. It is part of the calculation.

**Temporal summation** means inputs add over time. If EPSPs arrive close together, the first one has not fully faded before the next one arrives. Their effects can combine. **Spatial summation** means inputs from different locations combine. A dendrite, soma, and nearby synapses can all contribute to the voltage that reaches the trigger zone.

The **threshold** is a voltage level where a spike becomes likely. In this simplified chapter, we might use -55 mV as an example threshold. Real thresholds vary, but the idea is stable: below threshold, inputs are graded; once threshold is crossed at the trigger zone, an action potential can begin.

Exact terms to define: synapse, neurotransmitter, receptor, synaptic cleft, postsynaptic cell, graded potential, EPSP, IPSP, temporal summation, spatial summation, threshold, trigger zone.

## Read the Graph

![Summation graph](../source/figures/generated/fig_07_summation_graph.svg)

Figure 3.2. Small inputs can combine before a spike begins.

Read the axes first. The x-axis is time. The y-axis is membrane potential in mV. The resting level might be near -70 mV. A threshold line might be drawn at -55 mV. Small upward bumps are EPSPs. Downward bumps or opposing effects are IPSPs.

The graph is asking a prediction question: does the combined voltage reach threshold? Do not look only at one input. Look at the total pattern. If EPSPs are close together, they may add. If an IPSP arrives at the same time, it may reduce the total depolarization.

Graph sentence: "The inputs combine to move V_m from ___ mV to ___ mV, which is above/below threshold, so a spike is likely/not likely in this simplified example."

## Worked Example

Problem: A neuron starts at -70 mV. Three inputs arrive: +5 mV, +7 mV, and -3 mV. The example threshold is -55 mV. Does the neuron reach threshold?

Step 1: Add the voltage changes. +5 + 7 - 3 = +9 mV.

Step 2: Add the total change to the starting voltage. -70 mV + 9 mV = -61 mV.

Step 3: Compare to threshold. -61 mV is still below -55 mV. The neuron does not reach threshold in this simplified calculation.

Answer: No. The combined inputs depolarize the neuron to about -61 mV, which is not enough to reach -55 mV.

Practice: Start at -70 mV. Inputs are +6, +5, and +4 mV. Total change is +15 mV, so V_m reaches -55 mV. In this simplified model, threshold is reached.

## Mini Lab, Misconceptions, and Quiz

Mini-lab: Use tokens for summation. Let blue tokens be +2 mV EPSPs and red tokens be -2 mV IPSPs. Start at -70 mV and set threshold at -55 mV. Draw five input sequences and calculate the final estimated voltage. Then run or inspect `../source/code/chapter03_synapses_and_summation.ipynb` to compare the same idea in a notebook.

> **Common mistake**
> Do not assume any single input automatically causes a spike. Many inputs are small graded changes, and inhibition can shape the final result.

Chapter summary: Synapses convert communication between cells into voltage changes in the postsynaptic neuron. EPSPs and IPSPs can combine in time and space. The trigger zone responds to the combined effect, not just to one input.

Quiz check:
1. Define EPSP.
2. Define IPSP.
3. Identify temporal versus spatial summation from a diagram.
4. Add +4, +5, and -2 mV from -70 mV. Answer: -63 mV.
5. Explain why an IPSP is not simply "turning the neuron off."

Teacher note: Watch for students who think "excitatory" means guaranteed spike or "inhibitory" means no activity. Push them toward quantitative comparison with threshold.

