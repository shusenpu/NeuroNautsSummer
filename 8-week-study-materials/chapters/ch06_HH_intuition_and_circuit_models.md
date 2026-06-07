# Chapter 6. Hodgkin-Huxley Intuition and Circuit Models

## Opening Question

How can ion channels be described with circuit-like language without using calculus?

The beginner answer is that the membrane can be modeled as parts that store and move charge. The membrane itself can store separated charge, a little like a capacitor. Ion-channel pathways let current flow, a little like conductances. Each ion has a reversal potential, the voltage that pathway tends to pull the membrane toward. Hodgkin-Huxley models use these ideas to connect biology and electricity.

This chapter does not ask you to solve the full Hodgkin-Huxley equations. Instead, it teaches the meaning of the pieces. You will learn to read a circuit diagram, translate I = g(V_m - E) into words, and interpret simple current traces.

> **Key idea**
> A conductance pathway pulls V_m toward its reversal potential. More conductance means a stronger pull.

## Why This Matters

Models are useful when they clarify a mechanism. They become confusing when equations turn into symbols with no story. Here, every symbol must have a biological meaning. V_m is membrane potential. g_Na is sodium conductance. g_K is potassium conductance. E_Na and E_K are reversal potentials. I_app is applied current from an experiment or model input.

The circuit picture is not saying a neuron is built from metal wires and batteries. It is an analogy that helps organize charge storage and ion movement. The membrane separates charge. Channels create pathways. Reversal potentials represent ion gradients. Current depends on both how open a pathway is and how far V_m is from that pathway's reversal potential.

This prepares you to understand why changing conductance can change spike timing and why models can produce useful predictions without being perfect copies of biology.

## What You Already Need to Know

You need ions and equilibrium potentials from Chapter 2, action-potential phases from Chapter 4, and spike timing from Chapter 5. You also need basic subtraction and multiplication.

The expression I = g(V_m - E) can be read without calculus. V_m - E is the difference between the current membrane potential and the reversal potential. This difference is often called driving force. g is conductance, a measure of how available the pathway is. If g is zero, that pathway contributes no current. If V_m equals E, the driving force is zero.

The units in a real biophysics course can become detailed. Here, focus on direction and relative size.

## Visual First

![HH circuit](../source/figures/generated/fig_10_HH_circuit.svg)

Figure 6.1. The membrane behaves like a capacitor in parallel with Na, K, and leak pathways.

Start by labeling parts. C_m represents membrane capacitance, the membrane's ability to store separated charge. g_Na is sodium conductance. g_K is potassium conductance. Leak conductance represents other resting pathways. E_Na, E_K, and E_leak are reversal potentials.

This is a conceptual circuit. The "batteries" represent ion gradients, not literal batteries. The conductances represent channels, not metal resistors. The purpose is to show how several pathways can influence the same membrane voltage.

> **Try it**
> On Figure 6.1, circle every symbol that represents a pathway and underline every symbol that represents a voltage target.

## Core Concepts

**Conductance** means how easily current can flow through a pathway. In a neuron, conductance often changes when channels open or close. More open Na+ channels means larger g_Na. More open K+ channels means larger g_K.

**Reversal potential** is the voltage at which the net current through one ion pathway would reverse direction. If V_m is far from E_K, the K+ pathway has a strong driving force. If V_m is close to E_K, the driving force is weak.

**Driving force** is V_m - E in this simple expression. It tells you how far the membrane voltage is from the pathway's reversal potential. The current expression I = g(V_m - E) combines availability of the pathway with the voltage difference.

**Voltage clamp** is an experimental idea where the experimenter controls voltage and measures current. This helped scientists separate currents that would normally overlap during an action potential.

Exact terms to define: V_m, C_m, conductance, g_Na, g_K, leak conductance, reversal potential, E_Na, E_K, driving force, current, I_app, voltage clamp.

## Read the Graph

![Clamp diagram](../source/figures/generated/clamp.svg)

Figure 6.2. Voltage clamp controls voltage and measures current.

Read the command voltage first. That is the voltage the experimenter asks the membrane to hold. Then read the current trace. Current changes after the voltage step because channels respond. A current trace is not the same as a voltage trace. It shows movement of charge, not the membrane voltage itself.

Graph sentence: "When the command voltage changes, the measured current changes because channel pathways open, close, or change their driving force."

This graph pairs with the circuit diagram. The circuit gives you the parts. The clamp trace shows how scientists can probe those parts.

## Worked Example

Problem: If g = 2 units, V_m = -40 mV, and E = -80 mV, compute g(V_m - E).

Step 1: Find V_m - E. -40 - (-80) = +40 mV.

Step 2: Multiply by g. 2 x 40 = 80 in simplified current units.

Step 3: Interpret. The pathway has a strong driving force because V_m is far from E. The positive sign depends on the sign convention; for this chapter, focus on the size and the fact that current would push V_m toward E.

Answer: 80 simplified current units.

Practice: If g = 1, V_m = -70 mV, and E = -70 mV, then V_m - E = 0, so the current expression is 0.

## Mini Lab, Misconceptions, and Quiz

Mini-lab: Open `../source/code/week6_hh_intuition.ipynb`. Change conductance values one at a time. Sketch how increasing g_Na or g_K changes the model trace. Then write two predictions using the sentence: "Increasing ___ conductance pulls V_m toward ___."

> **Common mistake**
> Voltage and current are not the same thing. Voltage is a difference in electrical potential. Current is movement of charge.

Chapter summary: HH-style circuit models translate membrane biophysics into a language of capacitance, conductance, current, and reversal potential. You do not need calculus to understand the first story: open pathways pull V_m toward their reversal potentials.

Quiz check:
1. Define conductance.
2. Identify C_m, g_Na, g_K, E_Na, and E_K on a circuit diagram.
3. Explain "current pulls voltage toward reversal potential."
4. Calculate g(V_m - E) for g = 3, V_m = -50 mV, E = -70 mV. Answer: 60 simplified units.
5. State what voltage clamp controls and what it measures.

Teacher note: Watch for students who think the circuit is literal anatomy or that formulas replace mechanisms. Ask them to translate each symbol into a biological phrase.

