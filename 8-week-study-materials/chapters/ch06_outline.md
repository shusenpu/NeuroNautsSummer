# Chapter 6 Outline: Membranes as Circuits: Conductance, Reversal Potential, and Clamp Logic

## 1. Opening Question

- Question: How can ion channels be described with circuit-like language without using calculus?
- Target answer: the membrane stores charge like a capacitor, and channel pathways pull V_m toward their reversal potentials depending on conductance and driving force.
- Current source: `minibook_v2/source/chapters/circuits_and_hh_intuition.md`.

## 2. Why This Matters

- This chapter gives the student a careful bridge from biology to modeling.
- It explains what Hodgkin-Huxley-style language is trying to measure.
- Keep the goal qualitative plus simple arithmetic.

## 3. Visual First

- Required visual: `fig_10_HH_circuit.svg`.
- Companion visuals: `hh_equivalent_circuit.svg`, `clamp.svg`.
- Student task: label capacitor, Na+ pathway, K+ pathway, leak pathway, and reversal batteries.

## 4. Core Concepts And Terms To Define

- Subsection headings: Membrane as capacitor; Conductance; Reversal potential; Driving force; Current direction; Voltage clamp; HH as a model language.
- Exact terms to define: V_m, C_m, conductance, g_Na, g_K, leak conductance, reversal potential, E_Na, E_K, driving force, current, I_app, voltage clamp.
- Use I = g(V_m - E) as arithmetic and interpretation only.

## 5. Read The Graph

- Graph to read: `clamp.svg` or `hh_simulation.svg`.
- Student reads: command voltage, current trace, and timing of current changes.
- Skill: translate a current trace into “channels opened more or less.”

## 6. Worked Example And Try One Yourself

- Worked example: If g = 2 units, V_m = -40 mV, and E = -80 mV, compute g(V_m - E).
- Expected solution: V_m - E = 40 mV; current expression = 80 unit*mV; interpret as a strong driving force away from E.
- Try one: g = 1, V_m = -70 mV, E = -70 mV; answer: 0, no driving force.

## 7. Mini Lab Or Simulation

- Mini-lab: HH intuition notebook.
- Materials: `source/code/week6_hh_intuition.ipynb` and `source/code/chapter06_circuits_and_hh_intuition.ipynb`.
- Student output: one labeled circuit sketch and two current-direction predictions.

## 8. Assessment And Teacher Note

- 5-question quiz:
  1. Define conductance.
  2. Identify C_m, g_Na, g_K, E_Na, and E_K on a circuit diagram.
  3. Explain the phrase “current pulls voltage toward reversal potential.”
  4. Calculate g(V_m - E) for one simple case.
  5. State what voltage clamp controls and what it measures.
- Teacher note: likely misconceptions are that voltage and current are the same thing, that equations are the mechanism rather than a description, and that HH requires calculus for the beginner-level story.
