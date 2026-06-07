# One-Day Brain Code Basics Tutorial Plan

This plan redesigns the one-day tutorial as a **friendly basics day**, closer in spirit to the original concept-based morning slides. The eight-week research project can stay deeper and more technical. This one-day version should build confidence, curiosity, and graph-reading habits.

The goal is not to compress the whole minibook. The goal is to give students a clean first pass through the beginner spine:

> brain activity can be represented as signals -> neurons receive input -> voltage can move toward threshold -> threshold produces spikes -> spike count and timing can be plotted -> simple models help us ask "what changed?" -> every model leaves something out.

## Scope

Use the minibook selectively:

| Minibook source | One-day role | Depth |
|---|---|---|
| Intro and math appendix | Units, graphs, and model mindset | Light |
| Chapter 1: Neurons as signaling cells | Neuron parts and input-output flow | Core |
| Chapter 2: Ions/resting voltage | Resting voltage and "more/less negative" language | Very light |
| Chapter 3: Synapses/summation | Small inputs can add toward threshold | Light |
| Chapter 4: Action potentials | Threshold creates an all-or-none spike | Core concept only |
| Chapter 5: Spike trains | Spike count, rate, timing, and raster plots | Core |
| Chapters 6-8 | Save for the eight-week research project | Not in this tutorial |

Do **not** include HH models, full Nernst calculations, channel-noise mechanisms, patch clamp, Allen/ModelDB research workflows, or a full capstone project. Those belong in the deeper project.

## Six-Hour Flow

Assume 3 hours morning, lunch outside the 6 hours, and 3 hours afternoon.

| Time | Block | Source | Core question | Student product |
|---:|---|---|---|---|
| 0:00-0:20 | Hook: your brain as signals | Original slides, minibook intro | What does the brain do all day? | One everyday brain signal |
| 0:20-0:50 | Colab warm-up | Morning notebook 00 | How do we run code and read a plot? | Edited plot and one sentence |
| 0:50-1:20 | Neurons as input-output cells | Minibook Ch. 1 | What is a neuron built to do? | Labeled neuron map |
| 1:20-1:30 | Break | - | - | - |
| 1:30-2:15 | Simple neuron model | Morning notebook 01, minibook Ch. 3-4 | How does input become spikes? | Prediction-run-explanation table |
| 2:15-2:45 | Spike count and timing | Minibook Ch. 5 | How do we read spike output? | Spike count/rate/ISI practice |
| 2:45-3:00 | Morning wrap | Morning slides | What did the model help and hide? | Exit ticket |
| 3:00-3:25 | Recap and concept map | Slides + minibook figures | How do the pieces connect? | Completed chain |
| 3:25-4:10 | Guided model experiments | Morning notebook 01 | What happens if we change one thing? | Small results table |
| 4:10-4:20 | Break | - | - | - |
| 4:20-5:05 | Simple decision model | Morning notebook 02 | How can noisy evidence lead to choices? | Trial outcome and explanation |
| 5:05-5:35 | Models can mislead | Morning slides | What does a simple model leave out? | Trust/limit/caution notes |
| 5:35-6:00 | Final mini-share | Full basics day | Can students explain one graph? | One graph, one claim, one limitation |

## Morning: Build Confidence And Read Simple Models

### 0:00-0:20 - Hook: Your Brain As Signals

Use the original concept-based slides. Start with recognizable brain jobs: recognizing a friend, remembering a number, moving a hand, learning from feedback, deciding between options.

Core message:

- The brain is not magic in this course; it is a system that changes over time.
- A signal is anything we can track over time.
- A graph is a way to make change visible.

Activity:

- Students choose one everyday brain story: attention, hunger, confidence, reaction time, remembering a number, choosing between snacks.
- They sketch a simple time plot by hand before opening code.

Teacher line:

> Today we are using code like a microscope for ideas. We change one thing, look at the plot, and explain what changed.

### 0:20-0:50 - Colab Warm-Up

Use `colab_notebooks/monday_morning/00_Brain_Code_Colab_Warmup.ipynb`.

Core skills:

- Open notebook.
- Make a copy.
- Run a cell.
- Change one safe value.
- Read a plot.
- Write one interpretation sentence.

Do not teach Python syntax as the main event. Point only to student-editable values.

Student sentence:

> When I changed ___, the plot changed by ___.

### 0:50-1:20 - Neurons As Input-Output Cells

Use minibook Chapter 1 lightly.

Core concept:

- A neuron is a living cell with a communication job.
- Dendrites receive input.
- Soma/axon initial segment combine input and trigger spikes.
- Axon and terminals send output.
- Real neurons vary, so the cartoon is a map, not a portrait.

Best figures:

1. `minibook_v2/figures/fig_01_real_neuron_gallery.svg`
2. `minibook_v2/figures/fig_02_neuron_map.svg`

Activity:

- Label input, trigger, conducting, and output zones.
- Write: "The cartoon helps me see ___, but it leaves out ___."

Skip:

- Detailed morphology comparisons.
- Authentic cell-type datasets.

### 1:30-2:15 - Simple Neuron Model

Use `colab_notebooks/monday_morning/01_Brain_Code_Simple_Neuron_LIF.ipynb`.

Core concept:

- Input nudges voltage upward.
- Leak pulls voltage back down.
- Threshold marks when the model records a spike.
- Reset means the model starts again after a spike.
- This is not a full action-potential model; it is a simple rule for threshold and spikes.

Use minibook Chapter 2 only for language:

- Resting voltage is often around -70 mV.
- Moving from -70 mV to -55 mV is less negative.
- Threshold is a comparison line.

Use minibook Chapters 3-4 only for the beginner story:

- Small inputs can add.
- Crossing threshold produces a spike.
- A stronger stimulus usually means more spikes or different timing, not one giant spike.

Teaching rhythm:

1. Predict before running.
2. Run the model.
3. Count spikes.
4. Compare the voltage plot to threshold.
5. Explain what changed.

Good student experiments:

- Increase input strength.
- Raise threshold.
- Change how long the input lasts.
- Add a refractory pause if the notebook exposes it clearly.

Avoid:

- Ion-channel mechanisms.
- Na+/K+ gating details.
- Advanced biophysical model comparisons.

### 2:15-2:45 - Spike Count And Timing

Use minibook Chapter 5 lightly.

Core concept:

- A spike is an event.
- A spike train is a sequence of spike times.
- Firing rate is spikes per second.
- ISI is the time between spikes.
- A raster plot shows spike times across trials.

Activity:

```text
Spike times: 8, 29, 37, 58, 66 ms
ISIs: 21, 8, 21, 8 ms
```

Ask:

- How many spikes?
- Are the gaps regular or irregular?
- What does spike count miss?

This is enough. Save CV and variability statistics for the longer project.

### 2:45-3:00 - Morning Exit Ticket

Prompt:

> The simple neuron model helped me understand ___, but it left out ___.

Strong examples:

- It helped me see how threshold turns input into spikes, but it left out real ion channels.
- It helped me see spike count, but it left out the full biology of an action potential.

## Afternoon: Practice, Decisions, And Model Limits

### 3:00-3:25 - Recap And Concept Map

Start afternoon by rebuilding the day chain:

```text
brain job -> signal -> neuron input -> voltage -> threshold -> spikes -> graph -> explanation
```

Students fill in one example:

```text
remembering a phone number -> working-memory signal -> neuron input -> threshold crossings -> spike count changes -> graph explanation
```

Keep this conversational. The afternoon should feel like practice and consolidation, not a new advanced lecture.

### 3:25-4:10 - Guided Model Experiments

Return to the simple neuron notebook.

Core idea:

- A good beginner experiment changes one thing at a time.

Student table:

| Experiment | What changed? | Prediction | What happened? | Explanation |
|---|---|---|---|---|
| A | Input strength | | | |
| B | Threshold | | | |
| C | Input duration | | | |

Discussion prompts:

- Which change made more spikes?
- Which change made no spike?
- What evidence did you use?
- What would make you trust the result more?

### 4:20-5:05 - Simple Decision Model

Use `colab_notebooks/monday_morning/02_Brain_Code_Simple_Decision_DDM.ipynb` only as a **plain-language decision model**.

Core concept:

- Evidence can accumulate over time.
- Noise can make the same situation produce different trials.
- A decision bound means "enough evidence to choose."
- Waiting for more evidence can change speed and accuracy.

This is acceptable for the one-day basics tutorial because it is already part of the morning session and stays at the "predict, run, explain" level. Do not connect it to advanced research models.

Teaching rhythm:

1. Predict: quick or careful?
2. Run one trial.
3. Read the path.
4. Record choice and reaction time.
5. Explain: "The model chose ___ because evidence reached ___."

Optional replacement:

- If you want the day to stay purely neuron-focused, replace this block with more spike-train graph reading from minibook Chapter 5.

### 5:05-5:35 - Models Can Mislead

Use the original slides on model limits.

Core concept:

- A simple model is useful because it is clear.
- A simple model can mislead if we forget what it leaves out.
- Code output is not the same thing as biological evidence.

Compare:

| Model | Helps us see | Leaves out |
|---|---|---|
| Everyday signal plot | Change over time | Real brain measurements |
| Simple neuron model | Input, threshold, spike count | Real ion-channel biology |
| Simple decision model | Evidence, noise, bound | Real human emotion, strategy, context |

Student prompt:

> I trust this model for ___, but not for ___.

### 5:35-6:00 - Final Mini-Share

This is not a capstone. It is a small confidence-building share.

Student deliverable:

1. Choose one plot from the day.
2. State what changed.
3. State what the graph shows.
4. State one thing the model leaves out.

Sentence frame:

> I changed ___. The graph shows ___. I think this means ___. One limitation is ___.

## What To Save For The Eight-Week Research Project

Save these for the deeper minibook/research arc:

- Full Nernst calculations.
- Detailed ion-channel gating.
- Hodgkin-Huxley/circuit models.
- Current clamp, voltage clamp, and patch clamp.
- Single-channel noise.
- CV and deeper variability statistics.
- Allen Cell Types, ModelDB, DANDI, NWB, and authentic data workflows.
- Formal capstone project with hypothesis, controls, and rubric.

You can mention that these exist as "what comes next," but do not teach them in the one-day basics tutorial.

## One-Day Success Criteria

By the end, students should be able to:

1. Run a Colab cell and change one safe value.
2. Explain that a graph shows something changing over time.
3. Label a neuron as input, trigger, conducting, and output zones.
4. Say that voltage can move toward or away from threshold.
5. Explain that threshold turns model voltage into spikes.
6. Count spikes and compute a simple firing rate or ISI.
7. Explain one simple decision-model trial in plain language.
8. State one useful thing and one limitation for a model.
