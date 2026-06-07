# Chapter 2. Ions, Gradients, and Resting Potential

## Opening Question

Why does a neuron at rest usually have a negative voltage inside compared with outside?

The short answer is that ions are unevenly distributed across the membrane, and the membrane is selectively permeable. That means some ions can cross more easily than others. At rest, potassium ions, written K+, are especially important because many resting membranes allow K+ to leak through open channels. K+ tends to move out because it is more concentrated inside, but the inside becomes negative enough to pull K+ back. The balance between concentration push and electrical pull helps explain why resting membrane potential is often near a negative value.

This chapter adds the physical ingredients behind the voltage language from Chapter 1. A neuron has shape, but shape alone does not create electrical signals. Charged ions, concentration gradients, and membrane channels make voltage possible.

> **Key idea**
> Resting voltage is not caused by one thing. It comes from ion gradients plus selective permeability, with K+ leak playing a central role.

## Why This Matters

Every spike begins from a starting voltage. Every synaptic input changes voltage from a starting point. Every graph of membrane potential assumes that the inside and outside can be compared. If you understand resting membrane potential, later chapters will feel less mysterious.

The important beginner idea is not to memorize every exact ion concentration. The important idea is the pattern. Na+ is usually higher outside the neuron. K+ is usually higher inside. Ca2+ is much higher outside than inside. Cl- often has its own distribution depending on the cell type. These differences matter because ions carry charge.

![Ion gradient bar plot](../source/figures/generated/fig_03_ion_gradients_barplot.svg)

Figure 2.1. Different ions are unevenly distributed across the membrane.

This figure is a teaching comparison. It shows the pattern of inside and outside concentrations so you can reason about direction and sign.

## What You Already Need to Know

From Chapter 1, you need the idea of a membrane and a membrane potential. The membrane separates inside from outside. Membrane potential, V_m, means inside voltage compared with outside reference. You also need the idea that positive and negative charges can attract.

An **ion** is an atom or molecule with a net electric charge. Na+ and K+ are positive ions. Cl- is a negative ion. Ca2+ has two positive charges. A **concentration gradient** means there is more of a substance in one place than another. If K+ is high inside and low outside, K+ has a concentration gradient pointing outward.

No calculus is needed. You will use direction, sign, ratios, and one calculator-friendly rule.

## Visual First

Look at the electrochemical push diagram.

![Electrochemical push](../source/figures/generated/fig_04_electrochemical_push.svg)

Figure 2.2. Electrochemical force combines concentration push and electrical pull.

For K+, the concentration gradient often pushes outward because K+ is higher inside. But as K+ leaves, the inside loses positive charge and becomes more negative. That negative inside pulls K+ inward. At some voltage, the outward chemical push and inward electrical pull balance. That balance voltage for one ion is called an **equilibrium potential**.

Now look at the measurement cartoon.

![Membrane potential measurement](../source/figures/generated/fig_05_membrane_potential_measurement.svg)

Figure 2.3. Membrane potential is measured inside relative to outside.

This is not saying the whole cell is full of extra negative charge. Most of the cell remains nearly neutral. The important charge separation is tiny and concentrated near the membrane.

## Core Concepts

**Selective permeability** means the membrane lets some ions cross more easily than others. A plain lipid membrane blocks charged ions fairly well. Ion channels are proteins that provide controlled paths. If many K+ leak channels are open at rest, K+ has more influence on V_m than ions with fewer open paths.

**Diffusion** is movement from higher concentration toward lower concentration. If there is much more K+ inside than outside, diffusion tends to push K+ outward. **Electrical force** depends on charge. Since K+ is positive, a negative inside pulls K+ inward. For one ion, the balance point is the equilibrium potential.

The **Nernst equation** estimates that balance point for one ion. At body temperature, a beginner-friendly version for a positive ion with charge +1 is:

E = 61 log10(outside / inside)

This is not a new kind of magic. It says the sign and size of the equilibrium potential depend on the outside/inside concentration ratio. If outside/inside is less than 1, log10 is negative. If outside/inside is greater than 1, log10 is positive.

## Read the Graph

![Nernst sign plot](../source/figures/generated/nernst_sign_plot.svg)

Figure 2.4. Equilibrium potential changes sign when outside/inside crosses 1.

Read the x-axis first. It shows outside concentration divided by inside concentration. The scale is logarithmic, which means equal spacing marks equal multiplication, not equal addition. The y-axis shows equilibrium potential in mV. When the ratio is 1, outside and inside are equal, so the concentration gradient alone does not favor either side. The graph crosses 0 mV there.

When outside/inside is less than 1, the graph is below 0. That is the K+-like situation if K+ is high inside. When outside/inside is greater than 1, the graph is above 0. That is the Na+-like situation if Na+ is high outside.

Graph sentence: "When outside/inside is below 1, the equilibrium potential for a +1 ion is negative."

## Worked Example

Problem: Estimate E_K using outside K+ = 5 and inside K+ = 140. Use E = 61 log10(outside / inside).

Step 1: Form the ratio. outside / inside = 5 / 140 = 0.0357.

Step 2: Decide the sign before calculating. The ratio is less than 1, so log10(ratio) is negative. E_K should be negative.

Step 3: Use a calculator. log10(0.0357) is about -1.45. Multiply by 61. E_K is about -88 mV.

Step 4: Interpret. K+ is high inside, so chemical force tends to push K+ out. A negative inside pulls K+ back in. Around -88 mV, those two influences balance for K+ in this simplified calculation.

> **Try it**
> Estimate the sign of E_Na if outside Na+ = 145 and inside Na+ = 12. The ratio is greater than 1, so E_Na is positive. A calculator gives about +66 mV.

## Mini Lab, Misconceptions, and Quiz

Mini-lab: Open `../source/code/week2_nernst_explorer.ipynb`. Run the cells that plot equilibrium potential versus outside/inside ratio. Change the outside and inside values for K+ and Na+. Record whether each result is positive or negative, then write two sentences explaining why.

> **Common mistake**
> The Na+/K+ pump helps maintain gradients over time, but it is not the direct whole explanation for resting voltage. At rest, selective permeability, especially K+ leak, is the main beginner-level mechanism.

Chapter summary: Ions carry charge. Gradients create chemical push. Charge separation creates electrical pull. The resting membrane potential is negative mainly because the membrane at rest is much more permeable to K+ than to Na+, and K+ has a negative equilibrium potential.

Quiz check:
1. Define ion.
2. Predict diffusion direction for K+ if K+ is higher inside.
3. Explain how electrical pull can oppose diffusion.
4. If outside/inside = 0.1 for a +1 ion, is E positive or negative? Answer: negative.
5. Explain why the whole cell is still nearly neutral overall.

Teacher note: Watch for three linked misconceptions: voltage means the whole inside is packed with negative charge, the pump directly "makes" all resting voltage, and concentration force always wins over electrical force.

