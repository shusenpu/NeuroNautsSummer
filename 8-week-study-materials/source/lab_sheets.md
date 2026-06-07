# Lab Sheets

These labs are designed for a high-school student with no calculus background. Each lab can be done with paper, common classroom materials, or a basic spreadsheet. The goal is to connect a visible action to a neuroscience idea.

## Lab 1. Coin-Flip Channel Noise Activity

### Concept

Single ion channels open and close with randomness, but a population of many channels can have a measurable average pattern.

### Connects To

Chapter 7: stochastic gating, channel noise, open fraction, trial-to-trial variability, and CV.

### Time

25 to 35 minutes.

### Materials

- 10 coins.
- Paper or spreadsheet.
- Pencil.
- Optional: 100-coin version using a spreadsheet random number function.

### Setup

Treat each coin as one ion channel. Heads means open. Tails means closed. One round of flipping represents one moment in time.

### Procedure

1. Label a table with columns: `round`, `open channels`, `total channels`, `open fraction`.
2. Flip 10 coins at once.
3. Count heads. Record the number as open channels.
4. Compute open fraction: `open channels / total channels`.
5. Repeat for 20 rounds.
6. Plot round number on the x-axis and open fraction on the y-axis.
7. Optional: repeat using 50 or 100 simulated channels in a spreadsheet.

### Data Table

| Round | Open channels | Total channels | Open fraction |
| ---: | ---: | ---: | ---: |
| 1 |  | 10 |  |
| 2 |  | 10 |  |
| 3 |  | 10 |  |
| 4 |  | 10 |  |
| 5 |  | 10 |  |
| 6 |  | 10 |  |
| 7 |  | 10 |  |
| 8 |  | 10 |  |
| 9 |  | 10 |  |
| 10 |  | 10 |  |

### Graph Checklist

- x-axis label: `Round`.
- y-axis label: `Open fraction`.
- y-axis range: 0 to 1.
- Title: `Random channel openings over time`.

### Analysis Questions

1. Did the open fraction stay exactly the same every round?
2. What was the highest open fraction?
3. What was the lowest open fraction?
4. If you used more channels, would you expect the open fraction trace to look smoother or noisier?
5. Why does random channel timing still have a measurable pattern?

### Mentor Check

Ask: "Does stochastic mean causeless?" Expected answer: No. It means individual events have uncertain timing, but the overall pattern can still be measured.

### Extension

Use a spreadsheet to simulate 100 channels for 20 rounds. Compare the 10-channel and 100-channel traces. Write one sentence explaining why larger populations look smoother.

## Lab 2. Threshold and Reset Spreadsheet Simulation

### Concept

A simple model neuron can add input toward threshold, fire a spike, and reset. This is not a full biological neuron. It is a teaching model for threshold logic.

### Connects To

Chapters 3, 4, 5, and 7: summation, threshold, action potentials, spike trains, and timing variability.

### Time

30 to 45 minutes.

### Materials

- Spreadsheet software.
- Paper for prediction and explanation.

### Spreadsheet Columns

Use these columns:

| Column | Header | Meaning |
| --- | --- | --- |
| A | `time_ms` | Time step in milliseconds. |
| B | `input_mV` | Input added at that time step. |
| C | `V_m_before_reset_mV` | Voltage after adding input. |
| D | `spike` | 1 if threshold is crossed, 0 otherwise. |
| E | `V_m_after_reset_mV` | Voltage after reset rule. |

### Constants

Use these example values:

- Resting voltage: `-70 mV`.
- Threshold: `-55 mV`.
- Reset voltage: `-70 mV`.
- Time step: `1 ms`.

### Procedure

1. Fill column A with times from 0 to 30 ms.
2. In column B, enter a few inputs such as `+3`, `+4`, `+5`, or `0`.
3. Start `V_m_after_reset_mV` at `-70 mV`.
4. For each next row, compute `V_m_before_reset_mV = previous V_m_after_reset_mV + input_mV`.
5. If `V_m_before_reset_mV >= -55`, record spike = 1.
6. If spike = 1, set `V_m_after_reset_mV = -70`.
7. If spike = 0, keep `V_m_after_reset_mV = V_m_before_reset_mV`.
8. Plot `time_ms` on the x-axis and `V_m_after_reset_mV` on the y-axis.

### Example Rows

| time_ms | input_mV | V_m_before_reset_mV | spike | V_m_after_reset_mV |
| ---: | ---: | ---: | ---: | ---: |
| 0 | 0 | -70 | 0 | -70 |
| 1 | 4 | -66 | 0 | -66 |
| 2 | 5 | -61 | 0 | -61 |
| 3 | 6 | -55 | 1 | -70 |

### Analysis Questions

1. Which time step first reached threshold?
2. What happened immediately after the spike?
3. Did a larger input make a taller spike in this model?
4. How could you make the model fire more often?
5. What does this model leave out about real neurons?

### Mentor Check

Ask: "What is the reset rule doing?" Expected answer: It represents the model returning to a baseline after a spike. It is not a full biological refractory period.

### Extension

Add a column called `noise_mV`. Use small random values such as -2, -1, 0, +1, or +2 mV. Add noise to the voltage update and observe whether spike timing changes.

## Lab 3. Graph Annotation Lab

### Concept

A graph should be read before it is interpreted. The student should identify axes, units, visible pattern, and evidence before naming the mechanism.

### Connects To

All chapters, especially Chapters 2, 4, 5, 7, and 8.

### Time

20 to 30 minutes.

### Materials

- One graph from the book.
- Colored pens or digital annotation tool.
- Annotation checklist.

### Choose One Graph

Use one of these:

- Nernst sign plot from Chapter 2.
- Action potential phase graph from Chapter 4.
- Spike raster from Chapter 5.
- Noise and jitter panel from Chapter 7 or 8.

### Annotation Steps

1. Circle the title.
2. Underline the x-axis label and unit.
3. Underline the y-axis label and unit.
4. Box each condition label or legend entry.
5. Mark the main visible pattern with an arrow.
6. Write one sentence beginning: "This graph shows..."
7. Write one sentence beginning: "This supports the idea that..."
8. Write one sentence beginning: "This graph does not show..."

### Annotation Checklist

| Item | Done? |
| --- | --- |
| Title identified |  |
| x-axis variable identified |  |
| x-axis unit identified |  |
| y-axis variable identified |  |
| y-axis unit identified |  |
| Conditions identified |  |
| Main pattern described |  |
| Evidence sentence written |  |
| Limitation sentence written |  |

### Analysis Questions

1. What is the independent variable or condition?
2. What is being measured?
3. What pattern can you see before explaining the mechanism?
4. What claim could this graph support?
5. What would you need to know before making a stronger claim?

### Mentor Check

Ask the student to cover the caption and explain the graph using only labels and visible patterns. If she cannot, repair labels before discussing biology.

### Extension

Give the student a graph with one missing label. Ask her to identify what is missing and why the graph is harder to interpret.

## Lab 4. Morphology Observation Lab

### Concept

Real neurons have different shapes, but their parts still support signaling roles: input, trigger, conduction, and output.

### Connects To

Chapter 1: neuron morphology and input-decision-output structure. Optional bridge to Chapters 5, 6, and 8.

### Time

30 to 45 minutes.

### Materials

- Morphology gallery figure from the minibook, or a mentor-selected real neuron image from Allen Cell Types or NeuroMorpho.Org.
- Colored pencils or digital annotation.
- Observation table.

### Source Reminder

If using Allen Cell Types or NeuroMorpho.Org images, do not redistribute downloaded third-party data unless reuse terms are checked. For class use, record the source name, page URL, access date, and specimen or morphology ID if available.

### Procedure

1. Choose one simple cartoon neuron and one real neuron image.
2. Label likely dendrites, soma, axon or axon-like process, and terminals if visible.
3. Use one color for input regions and another color for output path.
4. Identify one feature that the cartoon shows clearly.
5. Identify one feature that the real neuron shows better.
6. Write a two-sentence comparison.

### Observation Table

| Feature | Cartoon neuron | Real neuron |
| --- | --- | --- |
| Dendrites or input branches |  |  |
| Soma position |  |  |
| Axon or output path |  |  |
| Branching complexity |  |  |
| What is easy to understand? |  |  |
| What is hidden or simplified? |  |  |

### Analysis Questions

1. Which parts look like input regions?
2. Where might the trigger zone be, even if you cannot see it directly?
3. What does the real neuron show that the cartoon hides?
4. Why is the cartoon still useful?
5. How could different morphology affect signaling?

### Mentor Check

Ask: "What is the difference between a real image and a conceptual map?" Expected answer: A real image shows biological detail. A conceptual map removes detail to show the signaling path.

### Extension

Compare two real neuron types, such as a pyramidal neuron and a Purkinje cell. Predict which one might collect inputs over a larger branching region and explain your reasoning from shape.

## Lab Report Format

For any lab, the student should submit:

1. Lab title.
2. One-sentence purpose.
3. Completed table or graph.
4. Three analysis answers.
5. One misconception repaired.
6. One remaining question.

## Safety and Scope

These are dry labs and computer activities. They do not use live tissue, chemicals, or human data collection. The goal is conceptual understanding and graph-based explanation.
