# Teacher Notes

These notes support one high-school student working through the minibook independently with mentor check-ins. The tone should stay curious and precise. The goal is not to rush through content; the goal is to build a causal story from neuron shape to noisy spike trains without calculus.

## Chapter-by-Chapter Misconceptions

| Chapter | Likely misconception | Repair move |
| --- | --- | --- |
| 1. Neurons as signaling cells | Every neuron looks like the same cartoon. | Start with real morphology, then use the cartoon as a map of input, trigger, and output. |
| 1. Neurons as signaling cells | Voltage is a substance moving down the axon. | Ask: "Voltage between which two places?" Return to inside compared with outside. |
| 2. Ions and resting potential | The Na+/K+ pump directly causes all resting voltage. | Separate maintaining gradients from setting V_m through selective permeability. |
| 2. Ions and resting potential | The whole cell interior is full of extra negative charge. | Emphasize tiny charge separation near the membrane and near-neutral bulk solution. |
| 3. Graded signals and threshold | One synaptic input automatically causes a spike. | Use EPSP/IPSP tokens and add them against a threshold line. |
| 3. Graded signals and threshold | Inhibition simply turns the neuron off. | Show that IPSPs shift probability and timing, not just on/off status. |
| 4. Action potentials | A stronger stimulus makes a taller spike. | Compare spike height with spike count and timing. Use all-or-none language. |
| 4. Action potentials | The spike jumps through empty space in myelinated axons. | Say the spike is regenerated at nodes of Ranvier. |
| 5. Spike trains | Information is only in spike height. | Use rasters with identical spike height but different rates and intervals. |
| 5. Spike trains | Firing rate tells the whole story. | Compare two trials with the same rate but different ISIs. |
| 6. HH intuition | Voltage and current are the same thing. | Translate voltage as difference and current as movement of charge. |
| 6. HH intuition | The circuit diagram is literal anatomy. | Label it as an analogy: capacitor for membrane, conductance for channels, batteries for reversal potentials. |
| 7. Channel noise | Randomness means there is no mechanism. | Use coin flips: each event is uncertain, but many events have measurable statistics. |
| 7. Channel noise | A larger CV means more spikes. | CV measures relative interval variability, not spike count. |
| 8. Project | A graph alone is a conclusion. | Require claim, evidence, reasoning, and limitation as separate sentences. |
| 8. Project | A model proves what all real neurons do. | Add the phrase "in this model output" and ask what biological evidence would be needed. |

## Suggested Pacing Adjustments

Use the 8-week plan as the default. The student should spend about 4 to 5 hours per week, split across short sessions. If time is short, compress by reducing optional extension work, not by skipping graph reading or worked examples.

| Situation | Adjustment |
| --- | --- |
| Student struggles with signs and units | Add a 15-minute warm-up before Chapters 2-4 using mV changes and axis reading. |
| Student struggles with graph reading | Pause new content. Use the graph annotation lab and require axis, unit, pattern, and meaning sentences. |
| Student understands biology but avoids math | Keep calculations one step at a time. Ask for a meaning sentence after each number. |
| Student enjoys coding | Let coding become an extension, but still require hand explanations of every figure. |
| Week must be shortened | Keep visual opener, core concept, graph reading, one worked example, and retrieval quiz. Skip only optional extension. |
| Student is preparing final talk | Spend less time adding content and more time rehearsing claim-evidence-reasoning aloud. |

## Support Strategies for Struggling Students

- Use color consistently: blue for inputs, green for voltage traces, orange for threshold, purple for inhibition, gray for model limits.
- Ask the student to redraw before rereading. Drawing reveals missing structure quickly.
- Use sentence frames: "The graph shows ___, so I think ___ because ___."
- Keep a one-page personal glossary. Each entry should have term, drawing, and one sentence.
- Turn calculations into three lines: formula, substitution with units, meaning sentence.
- Use physical tokens for summation before using voltage graphs.
- Read one figure at a time. Do not let the student explain mechanism until she has named axes and units.
- If frustration rises, switch to oral explanation with the figure visible, then return to writing.

## Extension Strategies for Advanced Students

- Compare Purkinje and pyramidal morphology and predict differences in input collection.
- Compare Nernst reasoning with a qualitative Goldman-style idea: mixed permeability shifts V_m.
- Add one inhibitory input to a threshold summation example and discuss timing.
- Compare unmyelinated and myelinated propagation with a sketch of nodes.
- Use the synthetic spike-time CSVs to make a raster and calculate CV by condition.
- Modify the integrate-and-fire script by changing threshold, reset, or noise level.
- Read one Allen Cell Types example page and identify morphology, firing trace, and model output.
- In the final project, add one next-step experiment that would test the model with biological data.

## Oral Questioning Prompts

Use these during weekly check-ins. The student should answer while pointing to a figure or graph when possible.

### Chapter 1

- "Where does input usually arrive, where can a spike begin, and where does output go?"
- "What is useful about the cartoon neuron, and what does it hide?"
- "If the membrane changes from -70 mV to -55 mV, what happened?"

### Chapter 2

- "Why does K+ matter so much for resting membrane potential?"
- "Which way does the concentration gradient push K+, and which way can electrical force pull it?"
- "Why is the Na+/K+ pump important but not the whole direct explanation for resting voltage?"

### Chapter 3

- "What is the difference between an EPSP and an IPSP?"
- "Why can several small inputs matter more than one input alone?"
- "Does reaching threshold happen everywhere in the neuron or at a trigger region?"

### Chapter 4

- "Point to depolarization, repolarization, and refractory period on the graph."
- "Why does a stronger stimulus usually make more spikes instead of a taller spike?"
- "How does myelin change propagation?"

### Chapter 5

- "What does each tick mark in a raster plot mean?"
- "How do you calculate firing rate from spike count and time?"
- "Can two spike trains have the same firing rate but different timing?"

### Chapter 6

- "Translate I = g(V_m - E) into words."
- "What does conductance mean biologically?"
- "In voltage clamp, what does the experimenter control and what is measured?"

### Chapter 7

- "What does stochastic mean without saying 'no cause'?"
- "How do you calculate CV, and why does it have no unit?"
- "Why can small channel fluctuations matter near threshold?"

### Chapter 8

- "What is your claim?"
- "What exact evidence supports it?"
- "What does your model not prove?"
- "How would real biological evidence differ from your simulation output?"

## Feedback Language

Use feedback that gives the student a next action.

| Instead of | Say |
| --- | --- |
| "Be clearer." | "Add the axis units, then say what pattern changes." |
| "Check your math." | "Redo the subtraction with signs, then write the unit mV." |
| "Explain more." | "Add one cause-and-effect link between channel opening and voltage." |
| "Good job." | "Your claim is specific. Now add the limitation sentence." |

## Readiness Rule

The student is ready to move on when she can do three things:

1. Explain the chapter's core figure aloud.
2. Solve a worked-example analog with correct units.
3. Repair the chapter's main misconception in one sentence.

Perfection is not required. Repeated confusion about the same misconception means pause for a repair activity before adding new vocabulary.
