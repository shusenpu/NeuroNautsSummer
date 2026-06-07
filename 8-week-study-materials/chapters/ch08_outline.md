# Chapter 8 Outline: Building an Evidence-Based Explanation About Noisy Spike Timing

## 1. Opening Question

- Question: How can you use a model, a graph, and a calculation to explain how noise changes spike timing?
- Target answer: make a clear claim, support it with graph evidence and one timing metric, and state what the model can and cannot prove.
- Current source: `minibook_v2/source/chapters/capstone_project.md`.

## 2. Why This Matters

- This chapter converts learning into a short scientific presentation.
- The focus is scientific explanation, not coding sophistication.
- The student should be ready to teach the core story to peers.

## 3. Visual First

- Required visual: `project_workflow.svg`.
- Companion visuals: `project_dashboard.svg`, `fig_12_noise_to_jitter_panel.svg`.
- Student task: choose one final figure to label and explain.

## 4. Core Concepts And Terms To Define

- Subsection headings: Claim; Evidence; Reasoning; Timing metric; Model output; Biological evidence; Limitation; Clear presentation.
- Exact terms to define: claim, evidence, reasoning, model, simulation, biological evidence, limitation, firing rate, mean ISI, CV, graph label, source note.
- Keep the capstone aligned to explanation quality.

## 5. Read The Graph

- Graph to read: `project_dashboard.svg` or a student-generated noise dashboard.
- Student reads: condition labels, axes, units, raster or voltage traces, timing metric panel.
- Skill: state what the graph shows before naming the mechanism.

## 6. Worked Example And Try One Yourself

- Worked example: Given two conditions, low noise CV = 0.10 and high noise CV = 0.42. Write a claim-evidence-reasoning sentence.
- Expected solution: high noise produced more variable spike timing; CV increased from 0.10 to 0.42; near-threshold fluctuations can shift crossing times.
- Try one: compare two firing rates or mean ISIs and write one cautious claim.

## 7. Mini Lab Or Simulation

- Mini-lab: capstone notebook and presentation draft.
- Materials: `source/code/week8_capstone.ipynb`, `source/code/chapter08_capstone_project.ipynb`, `source/rubrics/capstone_rubric.md`.
- Student output: one figure, one timing calculation, one limitation, and a three-minute oral explanation.

## 8. Assessment And Teacher Note

- 5-question quiz:
  1. Define claim.
  2. Identify evidence in a graph.
  3. Calculate one timing metric: rate, mean ISI, or CV.
  4. State one limitation of a simple noisy model.
  5. Distinguish model output from biological evidence.
- Teacher note: likely misconceptions are that a graph alone is a conclusion, that more code means better science, and that a simulation result should be presented as direct evidence from living neurons.
