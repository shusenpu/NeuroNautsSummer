# Chapter 5. Spike Trains and Neural Information

## Opening Question

If action potentials are mostly the same height, how can neurons send stronger or different messages?

The answer is that information can be carried by spike timing and spike patterns. A single action potential is important, but many nervous-system messages are easier to see when you look at a **spike train**, a sequence of spike times. A stronger stimulus may produce more spikes per second. A different stimulus may produce a different timing pattern. Two trials may have the same number of spikes but different spacing between them.

This chapter moves from one spike to many spikes. You will learn to read raster plots, calculate firing rate, measure interspike intervals, and explain why spike height is not the main message variable here.

> **Key idea**
> A stronger message is often more spikes, different timing, or activity in different neurons, not taller spikes.

## Why This Matters

In Chapter 4, you learned that an action potential is a stereotyped event. That raises a natural question: if spikes are mostly all-or-none, where is the information? One answer is in the pattern. A neuron can fire rarely, steadily, rapidly, irregularly, or in bursts. A group of neurons can also share information across a population, but this chapter focuses on one neuron at a time.

Spike trains are also practical. Neuroscientists often record spike times and analyze them with graphs. A raster plot can show repeated trials. An interspike interval plot can show spacing. A firing rate calculation can summarize spike count over time. None of these require calculus. They require careful counting, units, and interpretation.

The goal is not to claim that rate is the only code. The goal is to learn that rate and timing are both readable features of neural activity.

## What You Already Need to Know

You need the all-or-none action potential idea from Chapter 4. You should also know that time can be measured in milliseconds, abbreviated ms, or seconds, abbreviated s. Firing rate is usually measured in hertz, Hz, which means events per second.

You should be able to read a graph with time on the x-axis. A spike train graph may not show voltage height at all. It may show only tick marks at spike times. That can feel strange at first. The tick marks mean "a spike happened here." They do not show the whole voltage waveform.

The basic calculations are division and subtraction: spikes per second for firing rate, and differences between neighboring spike times for interspike intervals.

## Visual First

![Spike raster and rate](../source/figures/generated/fig_09_spike_raster_and_rate.svg)

Figure 5.1. A stronger message is often more spikes, not taller spikes.

Read the figure by counting events. In a weak stimulus condition, there may be fewer spike marks. In a stronger condition, there may be more spike marks in the same time window. The height of each spike mark is not the point. The pattern and count are the point.

A **raster plot** stacks trials or conditions in rows. Each tick mark is a spike time. If the x-axis is time in ms, a tick at 40 ms means a spike occurred 40 ms after the start of the trial. The raster lets you compare patterns quickly.

> **Try it**
> Pick one row in Figure 5.1. Count the spikes. Then say whether the spikes look evenly spaced or clustered.

## Core Concepts

A **spike train** is a sequence of spike times. If a neuron fires at 10 ms, 25 ms, and 60 ms, those times form a spike train. A **trial** is one repeated measurement or one repeated stimulus presentation. A raster plot can show many trials at once.

**Firing rate** is spike count divided by time. If a neuron fires 12 spikes in 1 second, the firing rate is 12 Hz. If it fires 6 spikes in 0.5 seconds, the firing rate is 12 Hz because 6 / 0.5 = 12. Always include the time window.

An **interspike interval**, or ISI, is the time between neighboring spikes. If spike times are 10 ms, 30 ms, and 55 ms, the ISIs are 20 ms and 25 ms. ISIs tell you about timing regularity. Two spike trains can have the same firing rate but different ISI patterns.

Exact terms to define: spike train, raster plot, trial, firing rate, Hz, interspike interval, ISI, mean ISI, timing code, rate code.

## Read the Graph

![Spike train dashboard](../source/figures/generated/spike_train_dashboard.svg)

Figure 5.2. Rate, interval, and variability can be read directly from spike trains.

Read the raster first. Count spikes in each trial. Next, look at the ISI histogram or interval panel. The histogram shows how often different interval lengths occur. If most intervals are similar, timing is regular. If intervals spread out, timing is more variable.

A summary panel may show firing rate and mean ISI. These are summaries, not replacements for the graph. A rate number tells you how many spikes occurred per second on average. It does not tell you exactly when those spikes happened.

Graph sentence: "Trial A and Trial B have similar firing rates, but Trial ___ has more regular timing because its ISIs are more similar."

## Worked Example

Problem: A neuron fires 8 spikes in 1 second. What is the firing rate?

Step 1: Write the rule. Firing rate = spike count / time in seconds.

Step 2: Substitute the values. 8 spikes / 1 second = 8 spikes per second.

Step 3: Use the unit. Spikes per second is Hz.

Answer: 8 Hz.

Practice: Spike times are 10, 30, 55, and 80 ms. The ISIs are 20 ms, 25 ms, and 25 ms. The mean ISI is (20 + 25 + 25) / 3 = 70 / 3, about 23.3 ms.

## Mini Lab, Misconceptions, and Quiz

Mini-lab: Use `../source/code/chapter05_spike_trains_rate_and_variability.ipynb` with `../source/datasets/synthetic_spike_times.csv`. Make or inspect a raster plot. Count spikes in two trials. Calculate firing rate for one trial and ISIs for another. Write one sentence comparing rate and timing.

> **Common mistake**
> A raster is not a voltage trace. It usually shows spike times, not the full shape of each action potential.

Chapter summary: Spike trains let neurons represent information through count, rate, timing, and spacing. Firing rate is a useful summary, but it does not capture everything. ISIs help describe timing directly.

Quiz check:
1. Define spike train.
2. Read a raster and count spikes.
3. Calculate firing rate for 5 spikes in 0.5 s. Answer: 10 Hz.
4. Calculate ISIs for 12, 22, and 50 ms. Answer: 10 ms and 28 ms.
5. Explain why spike height is not the main message variable here.

Teacher note: Watch for students who treat every spike plot as a voltage plot. Ask them what one mark means before asking what the whole graph means.

