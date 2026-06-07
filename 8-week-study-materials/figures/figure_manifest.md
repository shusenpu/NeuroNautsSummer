# Figure Manifest For Revised Minibook

This manifest is the production plan for the revised student-facing minibook. Each figure should support a specific learning task, not just decorate the page. Every final figure should include a caption, alt text, and a short note saying whether it is a cartoon, adapted open image, real data, or simulation output.

## Figure 1. Neuron Morphology Gallery

- File name: `fig_01_real_neuron_gallery.svg`
- Chapter placement: Chapter 1, Visual First.
- Figure purpose: show that real neurons have diverse shapes while still supporting input, decision, and output.
- Exact objects to draw: one pyramidal neuron, one Purkinje-like neuron, one multipolar motor neuron, one sensory/unipolar-like neuron; label dendritic region, soma, axon/output path where visible.
- Axis labels and units: not applicable.
- Draft caption: Different neuron shapes, same signaling job. Real neurons differ greatly in shape, but all still have receiving regions, a trigger zone, and an output path.
- Alt text: Gallery of several neuron morphologies showing diverse branching patterns and cell-body positions.
- Figure type: adapted open image or redraw from open morphology references.
- Source-credit placeholder: Adapted/redrawn from [OpenStax / Allen Cell Types / NeuroMorpho source to verify before final export].

## Figure 2. Simplified Neuron Map

- File name: `fig_02_neuron_map.svg`
- Chapter placement: Chapter 1, Visual First and Core Concepts.
- Figure purpose: give the student a stable functional map for input, decision, and output.
- Exact objects to draw: dendrites, soma, nucleus, axon hillock/initial segment, axon, optional myelin marks, axon terminals, arrow showing action-potential direction.
- Axis labels and units: not applicable.
- Draft caption: A simplified signaling map of a neuron. The cartoon removes detail so the reader can track where input arrives, where spikes begin, and where output goes.
- Alt text: Simplified neuron with labeled dendrites, soma, axon hillock, axon, terminals, and a direction arrow.
- Figure type: cartoon.

## Figure 3. Ion Gradient Comparison

- File name: `fig_03_ion_gradients_barplot.svg`
- Chapter placement: Chapter 2, Visual First.
- Figure purpose: make inside/outside ion distributions visible before equations.
- Exact objects to draw: grouped bars for Na+, K+, Cl-, and Ca2+; each ion has inside and outside bars; use consistent illustrative concentration values throughout the book.
- Axis labels and units: x-axis `Ion`; y-axis `Approximate concentration (mM)`; legend `Inside`, `Outside`.
- Draft caption: Different ions are unevenly distributed across the membrane. The pattern, not the exact number, is the key beginner lesson.
- Alt text: Bar chart comparing intracellular and extracellular concentrations of sodium, potassium, chloride, and calcium.
- Figure type: simulation output or locally generated teaching data.

## Figure 4. Electrochemical Gradient Diagram

- File name: `fig_04_electrochemical_push.svg`
- Chapter placement: Chapter 2, Core Concepts.
- Figure purpose: separate concentration push from electrical pull using K+ as the first example.
- Exact objects to draw: membrane cross-section, high K+ inside, low K+ outside, outward arrow labeled concentration push, inward arrow labeled electrical pull from negative inside, balance marker labeled equilibrium potential.
- Axis labels and units: not applicable.
- Draft caption: Electrochemical force combines two pushes. Diffusion and electrical attraction can oppose each other, and the balance point defines a reversal potential.
- Alt text: Diagram showing potassium pushed outward by concentration and pulled inward by negative charge inside the cell.
- Figure type: cartoon.

## Figure 5. Membrane Potential Measurement Diagram

- File name: `fig_05_membrane_potential_measurement.svg`
- Chapter placement: Chapter 2, Visual First or Read the Graph prelude.
- Figure purpose: show that membrane potential is inside voltage measured relative to outside.
- Exact objects to draw: cell membrane, intracellular electrode, extracellular reference electrode, voltmeter reading `-70 mV`, inside/outside labels, small charge separation near membrane.
- Axis labels and units: not applicable.
- Draft caption: Membrane potential is a voltage difference. A neuron's inside is measured relative to the outside reference.
- Alt text: Cell membrane with one electrode inside, one outside, and a meter reading negative seventy millivolts.
- Figure type: cartoon.

## Figure 6. Synapse Schematic With EPSP/IPSP

- File name: `fig_06_synapse_and_psps.svg`
- Chapter placement: Chapter 3, Visual First.
- Figure purpose: connect synaptic anatomy to postsynaptic voltage effects.
- Exact objects to draw: presynaptic terminal, vesicles, neurotransmitter dots, synaptic cleft, postsynaptic receptors/channels, one EPSP trace moving toward threshold, one IPSP trace moving away from threshold.
- Axis labels and units: small inset traces with x-axis `Time (ms)` and y-axis `V_m (mV)`.
- Draft caption: Synapses change postsynaptic voltage. The same neuron may be pushed toward or away from threshold depending on which channels open.
- Alt text: Presynaptic terminal releasing transmitter onto a postsynaptic membrane with excitatory and inhibitory voltage examples.
- Figure type: cartoon with schematic graph insets.

## Figure 7. Summation Graph

- File name: `fig_07_summation_graph.svg`
- Chapter placement: Chapter 3, Read the Graph.
- Figure purpose: show temporal and spatial summation of small inputs relative to threshold.
- Exact objects to draw: baseline near `-70 mV`, threshold line near `-55 mV`, several EPSP bumps, one IPSP dip, combined trace approaching or missing threshold, labels for temporal and spatial summation.
- Axis labels and units: x-axis `Time (ms)`; y-axis `Membrane potential, V_m (mV)`.
- Draft caption: Small inputs can combine before a spike begins. Threshold depends on the total membrane effect of multiple graded inputs.
- Alt text: Graph of multiple graded potentials summing toward a horizontal threshold line.
- Figure type: simulation output or locally generated teaching graph.

## Figure 8. Action Potential Phase Graph

- File name: `fig_08_action_potential_phases.svg`
- Chapter placement: Chapter 4, Visual First and Read the Graph.
- Figure purpose: teach action-potential phases as a timed sequence of membrane states.
- Exact objects to draw: voltage trace with rest, threshold, depolarization, overshoot, repolarization, after-hyperpolarization, refractory period, and return to rest.
- Axis labels and units: x-axis `Time (ms)`; y-axis `Membrane potential, V_m (mV)`.
- Draft caption: The action potential is a stereotyped voltage event. Fast sodium entry drives the rise; delayed potassium effects help end the spike and reset the membrane.
- Alt text: Voltage trace with labeled phases and threshold line.
- Figure type: simulation output or locally generated teaching graph.

## Figure 9. Action Potential Animation Storyboard Frames

- File name: `anim_01_action_potential_storyboard.md` plus optional frame files `anim_01_frame_01.svg` through `anim_01_frame_08.svg`
- Chapter placement: Chapter 4, Mini Lab or Simulation.
- Figure purpose: pair channel states with matching regions of the action-potential trace.
- Exact objects to draw: 8 frames: resting state, graded depolarization, threshold, rising phase with Na+ channel opening, peak/Na+ inactivation, repolarization with K+ channel effect, after-hyperpolarization, refractory recovery.
- Axis labels and units: each frame includes a small trace inset with x-axis `Time (ms)` and y-axis `V_m (mV)`.
- Draft caption: Storyboard for an action-potential animation. Each frame pairs channel state with the matching segment of the voltage trace.
- Alt text: Text and frame sequence describing successive phases of an action potential animation.
- Figure type: cartoon storyboard with schematic graph insets.

## Figure 10. Spike Raster With Rate Comparison

- File name: `fig_09_spike_raster_and_rate.svg`
- Chapter placement: Chapter 5, Visual First.
- Figure purpose: show that stronger messages are often more spikes or different timing, not taller spikes.
- Exact objects to draw: three stimulus rows labeled weak, medium, strong; vertical spike ticks of equal height; increasing spike counts; optional rate labels such as `4 Hz`, `8 Hz`, `14 Hz`.
- Axis labels and units: x-axis `Time (ms)`; y-axis `Stimulus condition`.
- Draft caption: A stronger message is often more spikes, not taller spikes. Information can be carried by firing rate and timing, not by action-potential amplitude.
- Alt text: Raster plot showing more frequent spike ticks for stronger stimulus conditions.
- Figure type: simulation output or locally generated teaching data.

## Figure 11. HH Equivalent Circuit

- File name: `fig_10_HH_circuit.svg`
- Chapter placement: Chapter 6, Visual First.
- Figure purpose: introduce conductance-based model language without calculus.
- Exact objects to draw: membrane capacitor `C_m`; sodium branch with `g_Na` and `E_Na`; potassium branch with `g_K` and `E_K`; leak branch with `g_L` and `E_L`; optional applied current arrow `I_app`; membrane voltage label `V_m`.
- Axis labels and units: not applicable.
- Draft caption: Hodgkin-Huxley turns membrane biophysics into a circuit language. The membrane stores charge, while ion-channel pathways pull voltage toward their reversal potentials.
- Alt text: Membrane represented by a capacitor in parallel with sodium, potassium, and leak conductance branches.
- Figure type: cartoon / conceptual circuit diagram.

## Figure 12. Patch-Clamp Single-Channel Trace

- File name: `fig_11_patch_clamp_trace.svg`
- Chapter placement: Chapter 7, Visual First.
- Figure purpose: show how single-channel openings appear as step-like current changes.
- Exact objects to draw: patch pipette sealed to membrane patch, one ion channel in the patch, amplifier/recording line, paired current trace jumping between closed and open levels.
- Axis labels and units: trace inset x-axis `Time (ms)`; y-axis `Current (pA)`.
- Draft caption: Single channels open all-or-none, but at variable times. Patch clamp made channel randomness experimentally visible.
- Alt text: Pipette attached to a membrane patch and a current trace jumping between closed and open channel states.
- Figure type: adapted open image or conceptual redraw.
- Source-credit placeholder: Conceptual redraw based on standard patch-clamp teaching diagrams; cite final source such as MBoC, Nobel Prize background, or original Hamill et al. reference if adapted.

## Figure 13. Channel-State Diagram

- File name: `channel_state_diagram.svg`
- Chapter placement: Chapter 7, Core Concepts.
- Figure purpose: distinguish closed, open, and inactivated channel states before discussing stochastic gating.
- Exact objects to draw: three membrane-channel cartoons labeled closed, open, inactivated; arrows showing possible transitions; ion dots passing only through open state; optional probability labels `more likely` and `less likely`.
- Axis labels and units: not applicable.
- Draft caption: Ion channels switch between states. The state changes follow rules, but the exact timing of a single channel opening can vary.
- Alt text: Three channel cartoons showing closed, open, and inactivated states with arrows between states.
- Figure type: cartoon.

## Figure 14. Repeated-Trial Spike Jitter Panel

- File name: `fig_12_noise_to_jitter_panel.svg`
- Chapter placement: Chapter 7 Read the Graph; Chapter 8 project bridge.
- Figure purpose: show how noise can shift threshold crossing times across repeated trials.
- Exact objects to draw: panel A with repeated voltage traces under low and high noise; threshold line; panel B with raster ticks from repeated trials; panel C with summary timing spread or jitter metric.
- Axis labels and units: voltage panel x-axis `Time (ms)`, y-axis `V_m (mV)`; raster x-axis `Time (ms)`, y-axis `Trial`; summary panel y-axis `Timing jitter (ms)` or `CV`.
- Draft caption: Small fluctuations can shift threshold crossing time. Near threshold, noise changes spike timing even when the average input is similar.
- Alt text: Voltage traces and spike-time summaries comparing low-noise and high-noise repeated trials.
- Figure type: simulation output.

## Figure 15. ISI Histogram And CV Panel

- File name: `isi_histogram_cv_panel.svg`
- Chapter placement: Chapter 5 Read the Graph; Chapter 7 calculation practice.
- Figure purpose: teach how intervals become a distribution and how CV summarizes relative timing variability.
- Exact objects to draw: top raster or spike-time strip; middle ISI histogram with bins; side or bottom summary panel listing mean ISI, SD of ISI, and CV = SD / mean.
- Axis labels and units: histogram x-axis `Interspike interval (ms)`; y-axis `Count`; summary panel units `ms` for mean and SD, no unit for CV.
- Draft caption: Interspike intervals describe timing between spikes. CV compares the spread of intervals with the mean interval.
- Alt text: Panel with spike times, an interspike-interval histogram, and a summary box showing mean ISI, standard deviation, and CV.
- Figure type: simulation output or locally generated teaching data.

