# Week-By-Week Redesign Plan

Purpose: convert the current v2 manuscript into a more systematic high-school textbook for a grade 9-10 reader. Keep the no-calculus promise. Every week follows this required learning rhythm: **visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz**.

## 8-Week Version

### Week 1. Neurons as Signaling Cells

- Current source sections: `source/chapters/neurons_as_signaling_cells.md`; use Opening Question through Source Notes, plus `source/code/chapter01_neurons_as_signaling_cells.ipynb`.
- Revised title: Neuron Shape, Signal Direction, and the Input-Decision-Output Map.
- Prerequisites: basic cell parts, atoms, charge, and the idea that cells have membranes.
- Learning objectives: label dendrites, soma, axon hillock, axon, and terminals; explain input, decision, and output regions; distinguish charge, voltage, and a signal in plain language.
- Estimated lesson times: visual 20 min; concept 45 min; graph/diagram reading 25 min; worked example 20 min; basic calculation 20 min; mini-lab 30 min; retrieval quiz 15 min; reading/homework 60 min.
- Required figures: `fig_01_real_neuron_gallery.svg`, `fig_02_neuron_map.svg`, `morphology_comparison_page.svg`, `week_roadmap.svg`.
- Required exercises: label a real neuron image; redraw the neuron map from memory; explain why shape supports signal direction; calculate simple mV changes such as -70 mV to -55 mV.
- Required quiz: `source/quizzes/chapter01.json`.
- Required lab/code block: `source/code/chapter01_neurons_as_signaling_cells.ipynb`; optional morphology tracing with `toy_pyramidal_morphology.swc`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz. Implementation: morphology gallery, vocabulary, neuron-map reading, mV-change example, sign calculation, tracing lab, quiz.

### Week 2. Ions, Gradients, and Resting Voltage

- Current source sections: `source/chapters/ions_gradients_resting_voltage.md`; use Opening Question through Source Notes, plus the math appendix and Nernst notebook.
- Revised title: Ions, Selective Permeability, and Why Rest Is Negative.
- Prerequisites: Week 1 neuron map, charge signs, ratios, scientific notation, and log10 from `source/glossary/math_tools_for_membrane_voltage.md`.
- Learning objectives: define ion, concentration gradient, selective permeability, resting membrane potential, and equilibrium potential; explain why K+ is central at rest; compute and interpret a simple Nernst value.
- Estimated lesson times: visual 20 min; concept 50 min; graph reading 30 min; worked example 25 min; basic calculation 25 min; mini-lab 35 min; retrieval quiz 15 min; reading/homework 75 min.
- Required figures: `fig_03_ion_gradients_barplot.svg`, `fig_04_electrochemical_push.svg`, `fig_05_membrane_potential_measurement.svg`, `nernst_sign_plot.svg`, `resting_membrane_cartoon.svg`.
- Required exercises: sort Na+, K+, Cl-, and Ca2+ by inside/outside pattern; predict diffusion direction; explain electrical pull versus concentration push; calculate one Nernst example with units.
- Required quiz: `source/quizzes/chapter02.json`.
- Required lab/code block: `source/code/chapter02_ions_gradients_resting_voltage.ipynb` and `source/code/week2_nernst_explorer.ipynb`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz. Implementation: ion-gradient bars, gradients/permeability, Nernst sign plot, sign example, Nernst calculation, explorer lab, quiz.

### Week 3. Graded Signals and Threshold

- Current source sections: `source/chapters/synapses_and_summation.md`; use Opening Question through Source Notes, plus the chapter notebook.
- Revised title: Synapses, EPSPs, IPSPs, and How Small Inputs Add Up.
- Prerequisites: Weeks 1-2; membrane voltage, resting voltage, threshold as a marked voltage level.
- Learning objectives: explain chemical synapses; distinguish EPSP and IPSP; compare temporal and spatial summation; predict whether combined inputs approach threshold.
- Estimated lesson times: visual 20 min; concept 45 min; graph reading 30 min; worked example 20 min; basic calculation 20 min; mini-lab 35 min; retrieval quiz 15 min; reading/homework 60 min.
- Required figures: `fig_06_synapse_and_psps.svg`, `fig_07_summation_graph.svg`, `synapse_summation_diagram.svg`, `threshold_feedback.svg`.
- Required exercises: annotate presynaptic terminal, cleft, receptor, and postsynaptic cell; identify EPSP versus IPSP traces; add small voltage changes; write a one-paragraph threshold prediction.
- Required quiz: `source/quizzes/chapter03.json`.
- Required lab/code block: `source/code/chapter03_synapses_and_summation.ipynb`; tactile token summation activity can be used before code.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz. Implementation: synapse visual, graded potentials, summation graph, EPSP/IPSP example, threshold arithmetic, summation lab, quiz.

### Week 4. How Spikes Begin and Travel

- Current source sections: `source/chapters/action_potentials_and_propagation.md`; use Opening Question through Source Notes, plus storyboard and chapter notebook.
- Revised title: Action Potentials, Refractory Periods, Myelin, and Propagation.
- Prerequisites: Weeks 1-3; threshold, Na+/K+ gradients, EPSP/IPSP language, graph axes.
- Learning objectives: narrate depolarization, overshoot, repolarization, after-hyperpolarization, and refractory period; explain all-or-none spike shape; compare myelinated and unmyelinated propagation.
- Estimated lesson times: visual 20 min; concept 50 min; graph reading 30 min; worked example 25 min; basic calculation 20 min; mini-lab 35 min; retrieval quiz 15 min; reading/homework 70 min.
- Required figures: `fig_08_action_potential_phases.svg`, `action_potential_phase_plot.svg`, `ap_phase_strip.svg`, `myelin.svg`, `gating_timeline.svg`.
- Required exercises: label a blank action-potential graph; match channel-state cards to phases; identify threshold crossings; explain why stronger input does not make a taller spike.
- Required quiz: `source/quizzes/chapter04.json`.
- Required lab/code block: `source/code/chapter04_action_potentials_and_propagation.ipynb` and `source/animations/anim_01_action_potential_storyboard.md`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz. Implementation: AP phase visual, channel timing, voltage-time graph, phase-label example, duration/threshold calculation, storyboard lab, quiz.

### Week 5. Spike Trains and Neural Information

- Current source sections: `source/chapters/spike_trains_rate_and_variability.md`; use Opening Question through Source Notes, plus chapter notebook and synthetic spike-time data.
- Revised title: Spike Trains, Firing Rate, ISI, and Timing as Information.
- Prerequisites: Weeks 1-4; action potentials are all-or-none events; graph reading with ms and Hz.
- Learning objectives: distinguish spike height from spike timing; interpret rasters; calculate firing rate and interspike intervals; explain why rate and timing can both carry information.
- Estimated lesson times: visual 20 min; concept 45 min; graph reading 35 min; worked example 20 min; basic calculation 25 min; mini-lab 35 min; retrieval quiz 15 min; reading/homework 60 min.
- Required figures: `fig_09_spike_raster_and_rate.svg`, `spike_train_dashboard.svg`, `isi_measurement.svg`, `spike_code.svg`.
- Required exercises: count spikes in a raster; calculate firing rate in Hz; compute ISIs from a short spike list; compare two trials with similar rate but different timing.
- Required quiz: `source/quizzes/chapter05.json`.
- Required lab/code block: `source/code/chapter05_spike_trains_rate_and_variability.ipynb` and `source/datasets/synthetic_spike_times.csv`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz. Implementation: raster visual, rate/timing, raster and ISI graphs, firing-rate example, ISI calculation, notebook lab, quiz.

### Week 6. Circuits and Hodgkin-Huxley Intuition

- Current source sections: `source/chapters/circuits_and_hh_intuition.md`; use Opening Question through Source Notes, plus chapter notebook and HH seed notebook.
- Revised title: Membranes as Circuits: Conductance, Reversal Potential, and Clamp Logic.
- Prerequisites: Weeks 1-5; ions, equilibrium potential, action-potential phases, basic multiplication and subtraction.
- Learning objectives: read a membrane-as-capacitor diagram; translate I = g(V_m - E) into words; explain conductance and reversal potential without calculus; interpret simple clamp traces.
- Estimated lesson times: visual 20 min; concept 50 min; graph reading 30 min; worked example 25 min; basic calculation 25 min; mini-lab 40 min; retrieval quiz 15 min; reading/homework 75 min.
- Required figures: `fig_10_HH_circuit.svg`, `hh_equivalent_circuit.svg`, `clamp.svg`, `driving_force.svg`, `hh_simulation.svg`.
- Required exercises: label C_m, g_Na, g_K, and E terms; translate one current statement into plain English; compare current direction for two V_m values; explain voltage clamp as a measurement tool.
- Required quiz: `source/quizzes/chapter06.json`.
- Required lab/code block: `source/code/chapter06_circuits_and_hh_intuition.ipynb` and `source/code/week6_hh_intuition.ipynb`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz. Implementation: HH circuit visual, conductance language, clamp/current graph, driving-force example, I = g(V_m - E) calculation, notebook lab, quiz.

### Week 7. From Single Channels to Timing Variability

- Current source sections: `source/chapters/single_channel_noise.md`; use Opening Question through Source Notes, plus chapter notebook and noise notebook.
- Revised title: Single-Channel Randomness, Noise, Jitter, and CV.
- Prerequisites: Weeks 1-6; spike trains, ISI, firing rate, conductance, and model-output language.
- Learning objectives: explain stochastic channel opening; distinguish random timing from lack of mechanism; calculate open fraction and CV; connect near-threshold noise to spike-time jitter.
- Estimated lesson times: visual 20 min; concept 50 min; graph reading 35 min; worked example 25 min; basic calculation 25 min; mini-lab 40 min; retrieval quiz 15 min; reading/homework 75 min.
- Required figures: `fig_11_patch_clamp_trace.svg`, `patch_clamp_single_channel_trace.svg`, `fig_12_noise_to_jitter_panel.svg`, `channel_noise_scaling.svg`, `random_trials.svg`.
- Required exercises: read a single-channel trace; compute open fraction; calculate mean ISI, SD, and CV from a short list; explain why model output is not direct biological evidence.
- Required quiz: `source/quizzes/chapter07.json`.
- Required lab/code block: `source/code/chapter07_single_channel_noise.ipynb` and `source/code/week7_noise_and_cv.ipynb`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz. Implementation: patch-clamp visual, stochastic channels, jitter/CV graph, open-fraction example, CV calculation, noisy threshold lab, quiz.

### Week 8. Evidence, Explanation, and Communication

- Current source sections: `source/chapters/capstone_project.md`; use Opening Question through Source Notes, plus rubrics, datasets, and capstone notebook.
- Revised title: Building an Evidence-Based Explanation About Noisy Spike Timing.
- Prerequisites: Weeks 1-7; all core vocabulary, graph reading, spike metrics, and model-versus-evidence distinction.
- Learning objectives: form a testable claim; choose evidence from a graph or simulation; calculate at least one timing metric; explain one limitation; present clearly to peers.
- Estimated lesson times: visual 15 min; concept 35 min; graph reading 30 min; worked example 25 min; basic calculation 25 min; mini-lab/project work 75 min; retrieval quiz/rehearsal 20 min; revision 60 min.
- Required figures: `project_workflow.svg`, `project_dashboard.svg`, `fig_12_noise_to_jitter_panel.svg`, final student-generated figure.
- Required exercises: write a claim-evidence-reasoning paragraph; label a project graph; calculate rate, mean ISI, or CV; identify one model limitation and one next experiment.
- Required quiz: `source/quizzes/chapter08.json`; use `source/rubrics/capstone_rubric.md` for final scoring.
- Required lab/code block: `source/code/chapter08_capstone_project.ipynb` and `source/code/week8_capstone.ipynb`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz. Implementation: project dashboard, scientific explanation, graph evidence, CER example, timing calculation, capstone lab, quiz and oral rehearsal.

## 7-Week Compressed Version

### Week 1. Neurons as Signaling Cells

- Current source sections: `source/chapters/neurons_as_signaling_cells.md`; preserve core sections and shorten homework to four required items.
- Revised title: Neuron Shape and Signal Direction.
- Prerequisites: basic cell biology, atoms, charge, and membrane vocabulary.
- Learning objectives: identify neuron parts; explain input-decision-output; distinguish charge, voltage, and signal.
- Estimated lesson times: visual 20 min; concept 40 min; graph/diagram reading 20 min; worked example 15 min; basic calculation 15 min; mini-lab 25 min; retrieval quiz 10 min; homework 45 min.
- Required figures: `fig_01_real_neuron_gallery.svg`, `fig_02_neuron_map.svg`, `morphology_comparison_page.svg`.
- Required exercises: label, redraw, explain direction of flow, calculate mV change.
- Required quiz: selected core items from `source/quizzes/chapter01.json`.
- Required lab/code block: `source/code/chapter01_neurons_as_signaling_cells.ipynb`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz. Implementation: diagram reading counts as the Week 1 graph-reading block.

### Week 2. Ions, Gradients, and Resting Voltage

- Current source sections: `source/chapters/ions_gradients_resting_voltage.md`; keep Nernst sign reasoning but limit algebra to one worked calculation.
- Revised title: Ions and Why Rest Is Negative.
- Prerequisites: Week 1, charge signs, ratios, log10 support from the math appendix.
- Learning objectives: explain ion gradients; distinguish diffusion from electrical force; compute and interpret one simple Nernst value.
- Estimated lesson times: visual 20 min; concept 45 min; graph reading 25 min; worked example 20 min; basic calculation 20 min; mini-lab 30 min; retrieval quiz 10 min; homework 60 min.
- Required figures: `fig_03_ion_gradients_barplot.svg`, `fig_04_electrochemical_push.svg`, `fig_05_membrane_potential_measurement.svg`, `nernst_sign_plot.svg`.
- Required exercises: predict ion movement, interpret sign, explain K+ leak, solve one Nernst problem.
- Required quiz: selected core items from `source/quizzes/chapter02.json`.
- Required lab/code block: `source/code/week2_nernst_explorer.ipynb`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz.

### Week 3. Synapses, Graded Signals, and Threshold

- Current source sections: `source/chapters/synapses_and_summation.md`; keep EPSP/IPSP and summation, defer advanced location effects to stretch.
- Revised title: Small Inputs Add Up Before a Spike.
- Prerequisites: Weeks 1-2, resting voltage, threshold.
- Learning objectives: explain synaptic transmission; distinguish EPSP and IPSP; predict threshold approach from simple summed inputs.
- Estimated lesson times: visual 20 min; concept 40 min; graph reading 25 min; worked example 20 min; basic calculation 20 min; mini-lab 30 min; retrieval quiz 10 min; homework 50 min.
- Required figures: `fig_06_synapse_and_psps.svg`, `fig_07_summation_graph.svg`, `threshold_feedback.svg`.
- Required exercises: label synapse, identify EPSP/IPSP, add inputs, explain why one input may not spike.
- Required quiz: selected core items from `source/quizzes/chapter03.json`.
- Required lab/code block: `source/code/chapter03_synapses_and_summation.ipynb`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz.

### Week 4. Action Potentials and Propagation

- Current source sections: `source/chapters/action_potentials_and_propagation.md`; keep myelin and refractory period, compress channel-state detail.
- Revised title: How Spikes Start, Reset, and Travel.
- Prerequisites: Weeks 1-3, ion gradients, threshold, EPSP/IPSP.
- Learning objectives: narrate spike phases; read threshold crossings; explain all-or-none spikes, refractory period, and myelin.
- Estimated lesson times: visual 20 min; concept 45 min; graph reading 30 min; worked example 20 min; basic calculation 15 min; mini-lab 30 min; retrieval quiz 10 min; homework 60 min.
- Required figures: `fig_08_action_potential_phases.svg`, `ap_phase_strip.svg`, `myelin.svg`, `gating_timeline.svg`.
- Required exercises: label AP trace, match phases to channel states, identify threshold, explain why stronger does not mean taller.
- Required quiz: selected core items from `source/quizzes/chapter04.json`.
- Required lab/code block: `source/code/chapter04_action_potentials_and_propagation.ipynb` and action-potential storyboard.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz.

### Week 5. Spike Trains and Neural Information

- Current source sections: `source/chapters/spike_trains_rate_and_variability.md`; keep raster reading and rate/ISI calculations as the core.
- Revised title: Spike Timing, Rate, and Information.
- Prerequisites: Weeks 1-4, all-or-none action potentials, ms and Hz.
- Learning objectives: read rasters; calculate firing rate and ISI; explain why information is not mainly spike height.
- Estimated lesson times: visual 20 min; concept 40 min; graph reading 35 min; worked example 20 min; basic calculation 20 min; mini-lab 30 min; retrieval quiz 10 min; homework 50 min.
- Required figures: `fig_09_spike_raster_and_rate.svg`, `spike_train_dashboard.svg`, `isi_measurement.svg`.
- Required exercises: count spikes, calculate Hz, calculate ISI, compare timing across trials.
- Required quiz: selected core items from `source/quizzes/chapter05.json`.
- Required lab/code block: `source/code/chapter05_spike_trains_rate_and_variability.ipynb` with `synthetic_spike_times.csv`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz.

### Week 6. Conductance Models and Channel Noise

- Current source sections: merge essential parts of `source/chapters/circuits_and_hh_intuition.md` and `source/chapters/single_channel_noise.md`; keep only no-calculus HH intuition, patch clamp, and CV.
- Revised title: From Circuit Models to Noisy Spike Timing.
- Prerequisites: Weeks 1-5, ions, spikes, spike trains, basic multiplication, mean and standard deviation as descriptive summaries.
- Learning objectives: translate I = g(V_m - E) into words; read an HH-style circuit; explain stochastic channel opening; calculate open fraction or CV; distinguish model output from biological evidence.
- Estimated lesson times: visual 25 min; concept 55 min; graph reading 35 min; worked example 25 min; basic calculation 25 min; mini-lab 45 min; retrieval quiz 15 min; homework 75 min.
- Required figures: `fig_10_HH_circuit.svg`, `fig_11_patch_clamp_trace.svg`, `fig_12_noise_to_jitter_panel.svg`, `channel_noise_scaling.svg`.
- Required exercises: label circuit terms, translate current direction, read a single-channel trace, calculate CV from a short ISI list.
- Required quiz: selected core items from `source/quizzes/chapter06.json` and `source/quizzes/chapter07.json`.
- Required lab/code block: `source/code/week6_hh_intuition.ipynb` plus `source/code/week7_noise_and_cv.ipynb`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz.

### Week 7. Capstone Explanation and Presentation

- Current source sections: `source/chapters/capstone_project.md`; include only the final project pathway plus rapid review of Chapters 5-7.
- Revised title: Explain How Noise Changes Spike Timing.
- Prerequisites: Weeks 1-6 and all core graph-reading skills.
- Learning objectives: make an evidence-based claim; label and interpret a figure; calculate one timing metric; state one limitation; deliver a clear peer presentation.
- Estimated lesson times: visual 15 min; concept 30 min; graph reading 30 min; worked example 20 min; basic calculation 20 min; mini-lab/project 90 min; retrieval quiz/rehearsal 20 min; revision 60 min.
- Required figures: `project_workflow.svg`, `project_dashboard.svg`, `fig_12_noise_to_jitter_panel.svg`, student-generated final figure.
- Required exercises: claim-evidence-reasoning paragraph, graph-label audit, timing-metric calculation, limitation statement, oral rehearsal.
- Required quiz: selected items from `source/quizzes/chapter08.json`; score final work with `source/rubrics/capstone_rubric.md`.
- Required lab/code block: `source/code/week8_capstone.ipynb`.
- Required sequence: visual -> concept -> graph -> worked example -> basic calculation -> mini-lab -> retrieval quiz.
