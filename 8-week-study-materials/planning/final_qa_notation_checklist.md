# Final QA: Notation Consistency

## Checklist

- [x] Use `V_m` for membrane voltage in notation-focused appendices and new notebooks.
- [x] Use `E_Na` for sodium reversal potential.
- [x] Use `E_K` for potassium reversal potential.
- [x] Use `g_Na` for sodium conductance.
- [x] Use `g_K` for potassium conductance.
- [x] Use `I_app` for applied current.
- [x] Use `mV` for voltage, `ms` for time, `Hz` for firing rate, and `CV` for coefficient of variation.
- [x] Preserve no-calculus language: `dV/dt` appears only as an optional source-note idea meaning "how fast voltage changes."
- [x] Keep the story order: neuron shape -> ions/resting voltage -> synapses/graded potentials -> action potentials/propagation -> spike trains -> HH intuition -> channel noise -> capstone.

## Patch-Style Required Edits

```diff
- VNa, VK, gNa, gK, Iapp
+ E_Na, E_K, g_Na, g_K, I_app

- Use V generically when teaching membrane voltage.
+ Use V_m when notation matters; define it as membrane voltage.

- Treat synapses, propagation, and spike-train variability as compressed subtopics.
+ Give synapses/graded potentials, action potentials/propagation, and spike-train variability their own chapters.

- Place logs and graph reading only inside ion chapters.
+ Put mV, ms, Hz, scientific notation, sign changes, graph reading, and common logs in the front math appendix.
```
