# Week B / Chapter 2. Ions, Gradients, and Why Rest Is Negative

## Opening Question

How can salty water and a thin membrane make a measurable voltage?

## Learning Goals

- Explain why potassium is central to resting membrane potential.
- Compute and interpret a simple Nernst equilibrium potential.
- Distinguish concentration gradient from electrical force.

## Week Snapshot

| Field | Week B plan |
|---|---|
| Weekly focus | Ions, diffusion, resting potential |
| Chapter | Ions, gradients, and why rest is negative |
| Prerequisites | Week A |
| Learning objectives | Explain Na+, K+, Cl-, Ca2+ distributions; distinguish diffusion vs electrical force; explain selective permeability |
| Basic calculations | Sign-only Nernst reasoning; simple concentration-ratio thinking |
| Estimated total time | 4.5-5.0 h |

## Weekly Lesson Spine

| Lesson component | Typical time | This chapter's job |
|---|---:|---|
| Visual opener | 15-20 min | Start from ion concentration bars before discussing voltage. |
| Core concept lesson | 35-45 min | Build the chain: ion -> gradient -> selective permeability -> V_m. |
| Graph/diagram-reading block | 20-30 min | Read the Nernst sign plot before calculator work. |
| Worked example | 15-25 min | Interpret a sign-and-units voltage change. |
| Basic calculation | 15-25 min | Compute one simple Nernst estimate with log10. |
| Mini-lab or code | 20-40 min | Use the Nernst explorer or PhET-style membrane channel simulation. |
| Retrieval quiz and reflection | 10-15 min | Explain why K+ is central to resting voltage. |

## Independent Study Scaffold

| Learning outcome | Misconception to address directly | Formative check | Support if stuck | Extension if ready |
|---|---|---|---|---|
| Explain why resting voltage is usually negative inside. | The Na+/K+ pump directly causes all of resting potential. | Write one paragraph explaining K+ leak plus ion gradients. | Reason one ion at a time before mixing ions. | Compare Nernst and Goldman qualitatively. |

> **How to use this scaffold:** Read the outcome before starting the chapter. After each section, answer the quick check before continuing. If the answer is shaky, use the support prompt immediately; if the answer is solid, try the extension prompt.


## Prerequisites and Recap

Prerequisites: atoms can have charge, concentration means amount per volume, and Chapter 1 introduced the neuron as a living cell with a membrane. Recap: the bridge from the previous chapter is from neuron shape to membrane function. This chapter explains how charged ions and selective membrane permeability give that shape an electrical state.

## Required Vocabulary

Use this table for the chapter, and use the cumulative [Glossary](../glossary/glossary.md) when a term returns in a later week.

| Term | Student-facing definition |
|---|---|
| Ion | Charged atom or molecule. |
| Concentration gradient | A difference in concentration from one place to another, such as high K+ inside and low K+ outside. |
| Selective permeability | A membrane property where some ions can cross more easily than others because certain channels are open. |
| Resting membrane potential | The usual membrane voltage of a neuron when it is not firing; many neurons sit near -70 mV. |
| Equilibrium potential | The voltage where one ion's concentration gradient and electrical force balance, so that ion has no net tendency to move. |
| Cation | Positive ion, such as Na+ or K+. |
| Anion | Negative ion, such as Cl-. |
| Electrical force | The push or pull on a charged particle caused by voltage. |
| Driving force | How far V_m is from an ion's equilibrium potential. |

## Misconception Box

> **Use this misconception box actively:** When one of these ideas appears, do not just mark it wrong. Replace it with the correction in your own words and give one piece of evidence from a figure, graph, or calculation.

- "Voltage is a substance stored inside the neuron." Voltage is a difference in electrical potential between inside and outside.
- "A negative membrane potential means the whole cell is full of negative charge." The whole cell is nearly neutral; the important imbalance is tiny and near the membrane.
- "The Na+/K+ pump directly makes every millisecond of resting voltage." The pump maintains gradients over time; leak channels and gradients explain the immediate V_m.
- "The Nernst equation gives the actual resting V_m for the whole neuron." Nernst gives one ion's balance point; real V_m depends on several permeabilities.

## Visual Opener

Start with ions before voltage. First compare the ion concentration bars: Na+ is mostly outside, K+ is mostly inside, Cl- is often higher outside, and Ca2+ is kept extremely low inside. Then look at the Nernst sign plot: when outside/inside is less than 1 for a positive ion like K+, the equilibrium potential is negative. Finally, use the resting membrane cartoon to see why selective K+ permeability can make the inside of the neuron negative relative to outside.


### Reality Figure B: Ion Gradient Barplot

![Bar chart comparing intracellular and extracellular concentrations of four major ions.](../figures/generated/fig_03_ion_gradients_barplot.svg)

*Different ions are unevenly distributed across the membrane. The pattern, not the exact number, is the key beginner lesson.*

> **What this figure is:** A quantitative comparison of typical inside/outside ion concentrations.
>
> **What this figure is not:** It is not a claim that every neuron has exactly these numbers at every moment.
>
> **Source note:** Generated locally from standard illustrative ion distributions used in introductory membrane-potential lessons.

### Concept Figure A: Electrochemical Push

![Diagram showing potassium pushed outward by concentration and inward by negative interior.](../figures/generated/fig_04_electrochemical_push.svg)

*Electrochemical force combines two pushes. Diffusion and electrical attraction can oppose each other, and the balance point defines a reversal potential.*

> **What this figure is:** A two-force diagram that separates concentration push from electrical pull.
>
> **What this figure is not:** It is not a full molecular simulation of every ion near the membrane.
>
> **Source note:** Generated locally from resting-potential and reversal-potential concepts.

### Measurement Figure: Membrane Potential

![Cell membrane with recording electrode inside and reference outside, meter reading negative voltage.](../figures/generated/fig_05_membrane_potential_measurement.svg)

*Membrane potential is a voltage difference. A neuron's inside is measured relative to the outside reference.*

> **What this figure is:** A measurement cartoon showing what -70 mV means operationally.
>
> **What this figure is not:** It is not saying the whole inside of the cell has become strongly negative.
>
> **Source note:** Generated locally from the standard membrane-potential measurement description used in introductory physiology.

![Semilog plot of equilibrium potential E versus outside divided by inside concentration ratio, crossing zero at ratio one.](../figures/generated/nernst_sign_plot.svg)

*Equilibrium potential changes sign when the outside/inside ratio crosses one.*

![Membrane diagram with K+ leak channels, high K+ inside, high Na+ outside, and negative inside voltage.](../figures/generated/resting_membrane_cartoon.svg)

*Resting membrane cartoon: selective K+ permeability lets K+ diffusion outward and electrical pull inward balance near a negative V_m.*

> **Quick Check: Visual opener**  
> **Question:** Which ion pattern is most important for explaining a negative resting V_m?  
> **Answer:** K+ is high inside, and resting membranes often have K+ leak permeability.


## Core Concept Lesson

Resting voltage comes from ion gradients plus selective permeability. The concentration gradient for K+ points outward because K+ is much more concentrated inside the neuron. The electrical force on K+ points inward once the inside becomes negative. The K+ equilibrium potential is the voltage where those two tendencies balance. Because resting membranes are often more permeable to K+ than to Na+, V_m at rest sits closer to E_K than to E_Na, though not exactly at E_K because other ions and channels also matter. The Na+/K+ pump maintains the Na+ and K+ gradients over time, but the immediate resting voltage is mainly explained by the existing gradients plus which leak channels are open. The next chapter uses this resting voltage as the starting point for synaptic inputs and graded potentials.

> **Quick Check: Core concept**  
> **Question:** What two ingredients create resting voltage?  
> **Answer:** Ion gradients plus selective permeability.


## Graph/Diagram-Reading Block

Read the Nernst sign plot in four passes. First find the x-axis: outside concentration divided by inside concentration. Second find the dashed ratio of 1, where outside and inside are equal. Third notice that the curve crosses 0 mV there. Fourth read the two sides: for a positive ion, ratios less than 1 give negative equilibrium potentials, while ratios greater than 1 give positive equilibrium potentials. This graph explains the sign before the calculator gives a number.

> **Quick Check: Graph/diagram reading**  
> **Question:** For a positive ion, what sign does E_ion have when outside/inside is less than 1?  
> **Answer:** Negative.


## Worked Example Box A

> **Study move:** Cover the solution first, try the problem, then compare your reasoning with the worked solution.

**Problem:** For a positive ion, the outside concentration is lower than the inside concentration. Before using a calculator, predict whether the Nernst equilibrium potential is positive, negative, or zero.

**Solution:** The outside/inside ratio is less than 1. For a positive ion, log10(outside/inside) is negative, so the equilibrium potential is negative. K+ is the main example: high K+ inside and lower K+ outside gives a negative E_K.

## Quick Check A With Answer

**Question:** Which is a concentration-gradient statement: 'K+ is high inside' or 'inside is negative'?

**Answer:** 'K+ is high inside' is the concentration-gradient statement. 'Inside is negative' is an electrical statement.

## Basic Calculation

**Task:** For a positive ion, outside = 10 mM and inside = 100 mM. Decide the sign of E_ion before calculating its value.

**Answer:** outside/inside = 10/100 = 0.1. log10(0.1) = -1, so E_ion is negative for z = +1. The biology sentence is: this ion would be balanced when the inside is negative relative to outside.

## Worked Example Box B

> **Study move:** Cover the solution first, try the problem, then compare your reasoning with the worked solution.

**Problem:** Use E_ion = (61 / z) log10(outside/inside) at room-temperature scale. For K+, z = +1, outside = 5 mM, and inside = 140 mM. Estimate E_K and interpret its sign.

**Solution:** Compute outside/inside = 5/140 = 0.0357. On a calculator, log10(0.0357) is about -1.40. E_K = 61 x -1.40 = about -85 mV. The negative sign means K+ would be balanced when the inside is substantially negative compared with outside.

## Quick Check B With Answer

**Question:** Why is potassium central to many resting membrane potentials?

**Answer:** K+ is high inside and many resting membranes have K+ leak permeability, so K+ strongly influences where V_m settles.

## Mini-Lab or Code

Run `notebooks/chapter02_ions_gradients_resting_voltage.ipynb` or the shorter Nernst explorer. Change only the outside/inside ratio at first. For each trial, write three things: the ratio, the sign of E_ion, and a sentence explaining what the sign means. After that, try changing z from +1 to -1 and notice why chloride needs special care.

> **Quick Check: Mini-lab**  
> **Question:** Why change only one ratio first in the Nernst explorer?  
> **Answer:** It lets the student see one cause-effect relation before combining variables.


## Interactive Exercise

Use PhET Membrane Channels or the local Nernst explorer. Open and close only one kind of channel at a time and write the causal sentence: "When this channel opens, V_m is pulled toward..."

> **Quick Check: Interactive exercise**  
> **Question:** Complete the sentence: when a channel opens, V_m is pulled toward...  
> **Answer:** That ion pathway's equilibrium or reversal potential.


## Retrieval Quiz and Reflection

1. Define ion, concentration gradient, and selective permeability.
2. Explain why K+ tends to diffuse outward at rest.
3. Explain why negative inside voltage pulls K+ inward.
4. State why V_m is near E_K but not exactly equal to E_K.

**Answers:** An ion is charged; a concentration gradient is a concentration difference; selective permeability means some ions cross more easily than others. K+ diffuses outward because it is high inside. Negative inside voltage attracts positive K+. V_m is near E_K because K+ permeability is important, but other ions also contribute.

**Assessment checkpoint:** The student is ready to move on when she can do a sign prediction from the Nernst graph and attach one biological interpretation sentence.

## Chapter Summary

Chapter 2 answers the opening question by connecting the visual story to a mechanism the student can explain without calculus. The key move is: Resting voltage comes from ion gradients plus selective permeability.

## Homework

### Questions

1. Make an ion table for Na+, K+, Cl-, and Ca2+ with charge, usual high side, and beginner role.
2. Write one sentence defining concentration gradient and one sentence defining electrical force.
3. For a positive ion, outside/inside = 10. Is log10(outside/inside) positive, negative, or zero? What does that imply for E_ion?
4. For K+, outside = 4 mM and inside = 120 mM. Use E_K = 61 log10(outside/inside). Round to the nearest mV.
5. Explain why opening K+ leak channels can make the inside of the neuron negative.
6. Bridge to Chapter 3: if a synapse opens channels after the neuron is resting near -70 mV, why can that synapse change V_m?
7. Graph-reading: in the Nernst sign plot, what happens when outside/inside crosses 1?
8. Extension: explain why Ca2+ can be a powerful signal even though its resting inside concentration is tiny.

### Answer Key

1. Na+ is +1 and high outside; K+ is +1 and high inside; Cl- is -1 and often higher outside; Ca2+ is +2 and extremely low inside. Na+ and K+ are central for voltage changes, Cl- often shapes inhibition, and Ca2+ is a powerful signaling ion.
2. A concentration gradient is a difference in concentration across space. Electrical force is the push or pull on an ion caused by voltage and charge.
3. It is positive because log10(10) = +1, so E_ion is positive for z = +1.
4. 4/120 = 0.0333. log10(0.0333) is about -1.48. E_K is about 61 x -1.48 = -90 mV.
5. K+ diffuses outward because it is high inside. Losing some positive charge leaves the inside relatively negative near the membrane, and that negative voltage then pulls K+ back inward.
6. Opening channels changes selective permeability. The newly open channels let ions pull V_m toward their own equilibrium potentials, creating a graded voltage change.
7. E_ion crosses 0 mV at outside/inside = 1 for z = +1. Ratios below 1 are negative; ratios above 1 are positive.
8. Because Ca2+ is kept extremely low inside, even a small influx can create a large relative change and trigger signaling pathways.

## Stretch Box

> The Nernst equation gives one ion's balance point, but a real resting neuron has several permeable ions. Explain why V_m is usually near E_K but not exactly equal to E_K. Use the phrase 'selective permeability' and mention at least one other ion.

## Mentor Note

> Keep the sequence strict: ions first, concentration gradients second, electrical force third, voltage fourth. If the student says 'voltage pushes K+ out,' pause and ask what the concentration gradient and electrical force are doing separately.

## Glossary Additions

- Ion
- Concentration gradient
- Selective permeability
- Resting membrane potential
- Equilibrium potential
- Electrical force
- Driving force

## Source Notes

| Figure | Asset | Caption | Alt text | Source notes |
|---|---|---|---|---|
| 2.1 | `ion_gradient_bars.svg` | Relative inside/outside ion concentrations create different electrochemical pulls. | Bar chart comparing clearly labeled illustrative inside and outside concentrations for Na+, K+, Cl-, and Ca2+. | Generated locally in Python using consistent illustrative values: Na+ 12/145 mM, K+ 140/5 mM, Cl- 10/110 mM, Ca2+ 0.0001/2 mM for inside/outside. |
| 2.2 | `nernst_sign_plot.svg` | Equilibrium potential changes sign when the outside/inside ratio crosses one. | Semilog plot of equilibrium potential E versus outside divided by inside concentration ratio, crossing zero at ratio one. | Generated locally in Python from E = 61 log10([out]/[in]) for z = +1. |
| 2.3 | `resting_membrane_cartoon.svg` | Resting membrane cartoon: selective K+ permeability lets K+ diffusion outward and electrical pull inward balance near a negative V_m. | Membrane diagram with K+ leak channels, high K+ inside, high Na+ outside, and negative inside voltage. | Original generated course figure; conceptually aligned with PhET Membrane Channels and NCBI Bookshelf ionic-basis explanations. |
