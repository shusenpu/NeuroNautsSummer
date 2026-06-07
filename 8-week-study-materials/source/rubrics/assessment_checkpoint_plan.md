# Assessment Architecture

Use three layers of assessment. The first two are feedback tools, not grades. The final mini-project is summative, but it should still reward scientific explanation rather than coding sophistication.

## Layer 1: Daily Formative Checks

Each study day should end with four short checks. Discuss them immediately. If the student misses one, she should revise the answer, redraw the figure, or redo the calculation before moving on.

| Daily item | What it tests | Example prompt shape | What good feedback sounds like |
|---|---|---|---|
| Prediction question | Causal reasoning before seeing the answer | "If this channel opens, what should happen to V_m?" | "Name the cause first, then the predicted voltage direction." |
| Graph-reading question | Axes, units, patterns, and evidence | "What does each axis show, and where is threshold?" | "Read the graph before naming the mechanism." |
| Plain-language explanation | Conceptual clarity and vocabulary | "Explain this idea to another high-school student in three sentences." | "Use the term, define it, then connect it to the figure." |
| Quantitative item | Sign, units, arithmetic, and biological meaning | "Compute the change from -70 mV to -55 mV and interpret it." | "The number is not finished until it has units and a meaning sentence." |

### Daily Prompt Bank By Week

| Week | Prediction | Graph reading | Plain-language explanation | Quantitative item |
|---|---|---|---|---|
| A | Predict signal direction from dendrites to terminals. | Label soma, dendrites, axon, and terminals on a new neuron image. | Explain a neuron as input, decision, and output. | Compute a simple mV change such as -70 to -55 mV. |
| B | Predict whether K+ tends to diffuse inward or outward at rest. | Read the ion-gradient bars or Nernst sign plot. | Explain why K+ leak plus gradients can make inside negative. | Decide the sign of E_ion from outside/inside ratio. |
| C | Predict whether a short EPSP/IPSP sequence reaches threshold. | Read a summation trace against the threshold line. | Explain EPSP, IPSP, and graded potential. | Add simple voltage nudges and compare to -55 mV. |
| D | Predict what happens after threshold is crossed. | Annotate rest, threshold, peak, refractory period, and after-hyperpolarization. | Narrate the spike as Na+ and K+ channel timing. | Compute voltage change from rest to threshold or peak. |
| E | Predict which spike train has higher rate or more irregular timing. | Convert a raster into spike count, ISIs, and a rate sentence. | Explain why information is not mainly spike height. | Compute firing rate or ISIs from spike times. |
| F | Predict the direction of pull when V_m is far from E_Na or E_K. | Match HH-style panels to V_m, g_Na, and g_K. | Translate I = g(V_m - E) into words. | Compute V_m - E_ion with units. |
| G | Predict which channel population is less noisy. | Read a single-channel trace or open-fraction histogram. | Explain why random does not mean unmechanistic. | Compute open fraction or CV from a short list. |
| H | Predict which condition should have larger timing variability. | Read a project dashboard as evidence. | Explain claim, evidence, reasoning, and limitation. | Compare two CV values or one mean ISI. |

## Layer 2: Weekly Chapter Checks

At the end of each chapter, give a five- to eight-item check plus one short oral explanation. Use the chapter's retrieval quiz, quick checks, and homework to choose items. Keep the check short enough that it can be discussed immediately.

| Required weekly item type | Count | Purpose |
|---|---:|---|
| Concept and vocabulary | 1-2 | Can the student use the terms correctly? |
| Prediction or causal chain | 1 | Can the student connect cause to effect? |
| Graph or figure interpretation | 1-2 | Can the student use a visual as evidence? |
| Quantitative item | 1-2 | Can the student compute with correct sign, units, and interpretation? |
| Misconception repair | 1 | Can the student replace a common misconception with a better explanation? |
| Oral explanation | 1 | Can the student explain the week's core idea aloud in two to three minutes? |

### Weekly Readiness Rule

The student is ready to move on when she gets about 80% of core items correct and can give a coherent oral explanation. Do not require perfection. If she misses the same type of item twice, give a targeted repair task:

| Repeated issue | Repair task |
|---|---|
| Vocabulary without meaning | Write the term, define it, and use it in one causal sentence. |
| Graph-reading errors | Read axes, units, and pattern before explaining mechanism. |
| Sign or unit errors | Redo one worked example and add a biological meaning sentence. |
| Weak causal explanation | Use a chain with arrows, such as gradient -> permeability -> voltage. |
| Overclaiming from models | Add "what this figure is / is not" to the explanation. |

## Layer 3: Summative Mini-Project

The final mini-project asks the student to make one evidence-based claim about how noise changes spike timing or variability in a simple model. The project should not assess coding sophistication. It should assess scientific explanation.

### Required Project Artifacts

1. One research question and hypothesis.
2. One figure with correctly labeled axes and units.
3. One timing metric, such as firing rate, ISI, mean ISI, standard deviation, or CV.
4. One claim-evidence-reasoning paragraph.
5. One limitation sentence.
6. One sentence distinguishing model output from biological evidence.
7. A short oral presentation for other high-school students.

### Final Project Rubric Summary

Use the detailed [Final Project Rubric](capstone_rubric.md). The six required criteria are:

| Criterion | What to look for |
|---|---|
| Conceptual accuracy | The explanation correctly connects neurons, ions/channels, voltage, spikes, timing, and noise. |
| Correct graph labeling | Axes, units, conditions, and threshold or timing marks are clear. |
| Correct use of terms | Terms such as V_m, spike train, ISI, CV, model, and limitation are used accurately. |
| Timing metric calculation | At least one rate, ISI, mean ISI, SD, or CV calculation is correct and interpreted. |
| Limitation explanation | The student states what the model does not prove. |
| Model vs biological evidence | The student distinguishes simulation output from direct biological data. |

## Checkpoint Plan

Use this plan to decide when the student is ready to move on and where she needs support.

| Metric | When to measure | Target |
|---|---|---|
| Entry diagnostic on graph reading, signs, units, and basic neuron parts | Before week one | Identify support needs, not a grade. |
| Daily formative checks | Each study day | One prediction, one graph-reading, one explanation, and one quantitative item are discussed immediately. |
| Weekly chapter check | Weekly | About 80% on core items plus a clear oral explanation before moving on. |
| Worked-example independence | Weekly | By mid-course, the student should solve the second example in each chapter with only light prompting. |
| Trace/raster interpretation | Weeks D through H | Student can explain what a graph shows before naming mechanisms. |
| Quantitative accuracy | Weeks B, E, F, and G | Correct units, correct sign, and a sentence of interpretation. |
| Notebook independence | Weeks F through H | Notebook runs top-to-bottom; student can explain each figure. |
| Final capstone | Week H | Student makes one evidence-based claim about how noise changes spike timing or variability. |
