# Chapter 3 Outline: Synapses, EPSPs, IPSPs, and How Small Inputs Add Up

## 1. Opening Question

- Question: How can many small synaptic inputs push a neuron toward or away from firing?
- Target answer: synapses create graded voltage changes that can add across time and space before the trigger zone reaches threshold.
- Current source: `minibook_v2/source/chapters/synapses_and_summation.md`.

## 2. Why This Matters

- This chapter bridges resting voltage to spike initiation.
- The student learns that most inputs are not spikes yet; they are smaller graded changes.
- Emphasize decision-making by combination, not one automatic input.

## 3. Visual First

- Required visual: `fig_06_synapse_and_psps.svg`.
- Companion visual: `threshold_feedback.svg`.
- Student task: label presynaptic terminal, cleft, receptor, postsynaptic membrane, EPSP, and IPSP.

## 4. Core Concepts And Terms To Define

- Subsection headings: Synaptic transmission; Receptors and channels; EPSPs; IPSPs; Temporal summation; Spatial summation; Threshold at the trigger zone.
- Exact terms to define: synapse, neurotransmitter, receptor, synaptic cleft, postsynaptic cell, graded potential, EPSP, IPSP, temporal summation, spatial summation, threshold, trigger zone.
- Keep causal chain: transmitter -> receptor/channel -> ion movement -> voltage change.

## 5. Read The Graph

- Graph to read: `fig_07_summation_graph.svg`.
- Student reads: time on x-axis, membrane potential on y-axis, EPSPs/IPSPs as smaller changes, threshold line.
- Skill: predict whether combined inputs cross threshold.

## 6. Worked Example And Try One Yourself

- Worked example: Start at -70 mV. Inputs are +5 mV, +7 mV, and -3 mV. Is threshold -55 mV reached?
- Expected solution: final estimate -61 mV; threshold not reached.
- Try one: +6 mV, +5 mV, +4 mV from -70 mV; answer: -55 mV, threshold reached in this simplified model.

## 7. Mini Lab Or Simulation

- Mini-lab: token summation or notebook summation.
- Materials: colored tokens for EPSPs/IPSPs or `source/code/chapter03_synapses_and_summation.ipynb`.
- Student output: one table of inputs and final estimated voltage.

## 8. Assessment And Teacher Note

- 5-question quiz:
  1. Define EPSP.
  2. Define IPSP.
  3. Identify temporal versus spatial summation from a diagram.
  4. Add three small voltage changes and compare with threshold.
  5. Explain why one synaptic input may not cause a spike.
- Teacher note: likely misconceptions are that every synapse triggers a spike, that inhibition means “turning the neuron off,” and that threshold belongs everywhere equally instead of being especially important near the axon initial segment.
