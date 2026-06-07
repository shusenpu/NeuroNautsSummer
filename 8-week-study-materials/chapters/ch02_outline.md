# Chapter 2 Outline: Ions, Selective Permeability, and Why Rest Is Negative

## 1. Opening Question

- Question: Why does a neuron at rest usually have a negative voltage inside compared with outside?
- Target answer: uneven ion concentrations plus selective permeability, especially K+ leak, create a stable negative resting membrane potential.
- Current source: `minibook_v2/source/chapters/ions_gradients_resting_voltage.md`.

## 2. Why This Matters

- This chapter turns cell anatomy into biophysics.
- The student learns that voltage comes from charged ions and membrane proteins.
- Keep the no-calculus path: use ratios, signs, and log10 only.

## 3. Visual First

- Required visual: `fig_03_ion_gradients_barplot.svg`.
- Companion visuals: `fig_04_electrochemical_push.svg`, `fig_05_membrane_potential_measurement.svg`.
- Student task: identify which ions are high inside versus outside.

## 4. Core Concepts And Terms To Define

- Subsection headings: What ions are; Concentration gradients; Diffusion push; Electrical pull; Selective permeability; K+ leak and rest; Equilibrium potential.
- Exact terms to define: ion, Na+, K+, Cl-, Ca2+, concentration gradient, diffusion, electrical force, selective permeability, leak channel, resting membrane potential, equilibrium potential, Nernst equation.
- Keep Na+/K+ pump as support, not the direct whole explanation for rest.

## 5. Read The Graph

- Graph to read: `nernst_sign_plot.svg`.
- Student reads: x-axis outside/inside concentration ratio on log scale; y-axis equilibrium potential in mV.
- Skill: explain why the sign changes when the ratio crosses 1.

## 6. Worked Example And Try One Yourself

- Worked example: Use approximate Nernst rule, E = 61 log10(outside/inside), for K+ with outside 5 and inside 140.
- Expected solution: E_K is negative because outside/inside is less than 1; calculator value about -88 mV.
- Try one: Na+ with outside 145 and inside 12; answer should be positive, about +66 mV.

## 7. Mini Lab Or Simulation

- Mini-lab: Nernst explorer.
- Materials: `source/code/week2_nernst_explorer.ipynb`.
- Student output: one plot screenshot or sketch plus two sentences explaining E_K and E_Na signs.

## 8. Assessment And Teacher Note

- 5-question quiz:
  1. Define ion.
  2. Predict diffusion direction for K+ if K+ is higher inside.
  3. Explain why electrical pull can oppose diffusion.
  4. Calculate whether outside/inside = 0.1 gives positive or negative equilibrium potential for z = +1.
  5. Explain why the pump is not the whole direct cause of resting voltage.
- Teacher note: likely misconceptions are that the whole cell is strongly negative, that voltage is caused only by the Na+/K+ pump, and that concentration force and electrical force always point the same way.
