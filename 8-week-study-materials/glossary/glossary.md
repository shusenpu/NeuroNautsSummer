# Cumulative Glossary

This glossary covers the technical vocabulary used across Chapters 1-8 of *From neuron shape to noisy spike trains*. It is written for a high-school reader, but each entry also includes a more formal definition for mentor use.

## How To Link Terms In Chapters

Use relative Markdown links to the stable anchors below, such as `[dendrite](../glossary/glossary.md#dendrite)`. Link the first real use of a term in each chapter body, not every repeated use. If a term appears in a heading, link the first use in the paragraph below the heading instead.

For each chapter, insert glossary links in this order:

- Chapter 1: link `neuron`, `membrane`, `dendrite`, `soma`, `axon hillock`, `axon`, `axon terminal`, `synapse`, `charge`, `voltage`, `membrane potential`, `mV`, `depolarization`, and `hyperpolarization`.
- Chapter 2: link `ion`, `Na+`, `K+`, `Cl-`, `Ca2+`, `concentration gradient`, `diffusion`, `electrical force`, `electrochemical gradient`, `selective permeability`, `permeability`, `leak channel`, `Na+/K+ pump`, `resting membrane potential`, `equilibrium potential`, `Nernst equation`, `log10`, and `concentration ratio`.
- Chapter 3: link `presynaptic terminal`, `neurotransmitter`, `synaptic cleft`, `receptor`, `postsynaptic cell`, `postsynaptic potential`, `graded potential`, `EPSP`, `IPSP`, `temporal summation`, `spatial summation`, `threshold`, and `trigger zone`.
- Chapter 4: link `action potential`, `spike`, `all-or-none`, `voltage-gated channel`, `depolarization`, `overshoot`, `repolarization`, `after-hyperpolarization`, `refractory period`, `myelin`, `node of Ranvier`, `propagation`, and `regeneration`.
- Chapter 5: link `spike train`, `raster plot`, `trial`, `firing rate`, `Hz`, `interspike interval`, `ISI`, `mean ISI`, `histogram`, `rate code`, and `timing code`.
- Chapter 6: link `Hodgkin-Huxley model`, `circuit model`, `capacitance`, `capacitor`, `C_m`, `conductance`, `g_Na`, `g_K`, `leak conductance`, `reversal potential`, `E_Na`, `E_K`, `E_leak`, `driving force`, `current`, `I_app`, `current clamp`, `voltage clamp`, and `clamp trace`.
- Chapter 7: link `patch clamp`, `single channel`, `open state`, `closed state`, `stochastic`, `noise`, `channel noise`, `trial-to-trial variability`, `jitter`, `open fraction`, `standard deviation`, `SD`, `coefficient of variation`, and `CV`.
- Chapter 8: link `claim`, `evidence`, `reasoning`, `model`, `simulation`, `biological evidence`, `limitation`, `metric`, `graph label`, `source note`, and `claim-evidence-reasoning`.

## Terms

<a id="action-potential"></a>
### Action potential
- Plain-language definition: A fast voltage spike that can travel along an axon.
- Formal definition: A regenerative, all-or-none change in membrane potential caused mainly by voltage-gated ion channel dynamics.
- Common confusion: Not every voltage bump is an action potential.
- Chapter first introduced: Chapter 4.

<a id="after-hyperpolarization"></a>
### After-hyperpolarization
- Plain-language definition: The brief dip when voltage becomes more negative than rest after a spike.
- Formal definition: A post-spike membrane potential undershoot often caused by continued K+ conductance.
- Common confusion: It is part of recovery, not a separate message by itself.
- Chapter first introduced: Chapter 4.

<a id="all-or-none"></a>
### All-or-none
- Plain-language definition: Once threshold is crossed, the spike usually has a standard size and shape.
- Formal definition: A response property in which a sufficient trigger produces a full action potential rather than a partly scaled spike.
- Common confusion: Stronger input usually makes more spikes, not taller spikes.
- Chapter first introduced: Chapter 4.

<a id="axon"></a>
### Axon
- Plain-language definition: The output branch that carries spikes away from the cell body.
- Formal definition: A neuronal process specialized for action-potential initiation or propagation toward synaptic terminals.
- Common confusion: It is not just a long dendrite; its channel placement and role differ.
- Chapter first introduced: Chapter 1.

<a id="axon-hillock"></a>
### Axon hillock
- Plain-language definition: The region near the start of the axon where spikes often begin.
- Formal definition: A transition region between soma and axon that contributes to spike initiation, often discussed with the initial segment.
- Common confusion: It is not a decision-making brain by itself; it is a trigger zone with special membrane properties.
- Chapter first introduced: Chapter 1.

<a id="axon-terminal"></a>
### Axon terminal
- Plain-language definition: The end region of an axon that communicates with another cell.
- Formal definition: A presynaptic specialization where an axon forms synaptic contacts and often releases neurotransmitter.
- Common confusion: A terminal is not the same as a dendrite, even though both can branch.
- Chapter first introduced: Chapter 1.

<a id="biological-evidence"></a>
### Biological evidence
- Plain-language definition: Evidence measured from real living tissue or cells.
- Formal definition: Empirical data from biological observations, recordings, images, or experiments.
- Common confusion: A model output can support a mechanism, but it is not the same as biological evidence.
- Chapter first introduced: Chapter 8.

<a id="c_m"></a>
### C_m
- Plain-language definition: A symbol for membrane capacitance.
- Formal definition: The capacitance of the cell membrane, representing its ability to store separated charge.
- Common confusion: It is not a channel; it represents charge storage across the membrane.
- Chapter first introduced: Chapter 6.

<a id="ca2"></a>
### Ca2+
- Plain-language definition: A calcium ion with two positive charges.
- Formal definition: A divalent cation important in signaling, transmitter release, and many cellular processes.
- Common confusion: Ca2+ is not just "stronger sodium"; its two charges and biology make it special.
- Chapter first introduced: Chapter 2.

<a id="capacitance"></a>
### Capacitance
- Plain-language definition: The ability to store separated charge.
- Formal definition: Charge stored per voltage difference, used in membrane models to represent charge separation across the membrane.
- Common confusion: Capacitance stores charge separation; it is not the same as current flow through a channel.
- Chapter first introduced: Chapter 6.

<a id="capacitor"></a>
### Capacitor
- Plain-language definition: A circuit part that stores separated charge.
- Formal definition: An electrical component with two conducting surfaces separated by an insulator, used as an analogy for the membrane.
- Common confusion: The membrane is not literally a metal capacitor, but the analogy helps explain charge storage.
- Chapter first introduced: Chapter 6.

<a id="charge"></a>
### Charge
- Plain-language definition: The positive or negative property that makes particles attract or repel.
- Formal definition: A physical property of matter that creates electric forces and is measured in coulombs in formal physics.
- Common confusion: Charge is not the same as voltage; voltage compares electrical potential between locations.
- Chapter first introduced: Chapter 1.

<a id="channel-noise"></a>
### Channel noise
- Plain-language definition: Variability caused by random opening and closing of ion channels.
- Formal definition: Fluctuations in membrane current or voltage arising from stochastic ion-channel gating.
- Common confusion: Noise does not mean there is no mechanism.
- Chapter first introduced: Chapter 7.

<a id="circuit-model"></a>
### Circuit model
- Plain-language definition: A drawing or equation system that treats membrane parts like circuit parts.
- Formal definition: A simplified representation of membrane capacitance, conductance pathways, currents, and reversal potentials.
- Common confusion: It is an analogy and model, not literal anatomy.
- Chapter first introduced: Chapter 6.

<a id="claim"></a>
### Claim
- Plain-language definition: A clear statement you are trying to support.
- Formal definition: A scientific assertion that can be evaluated using evidence and reasoning.
- Common confusion: A claim is not just a topic; it must say something specific.
- Chapter first introduced: Chapter 8.

<a id="claim-evidence-reasoning"></a>
### Claim-evidence-reasoning
- Plain-language definition: A way to explain science by saying what you think, what supports it, and why it makes sense.
- Formal definition: A structured explanation format connecting a claim to evidence through causal or mechanistic reasoning.
- Common confusion: Evidence alone is not reasoning; reasoning explains the connection.
- Chapter first introduced: Chapter 8.

<a id="cl"></a>
### Cl-
- Plain-language definition: A chloride ion with one negative charge.
- Formal definition: A monovalent anion that can influence inhibition and membrane potential depending on its distribution.
- Common confusion: Negative ions do not always simply "make the cell negative"; direction depends on gradients and permeability.
- Chapter first introduced: Chapter 2.

<a id="clamp-trace"></a>
### Clamp trace
- Plain-language definition: A graph recorded during a voltage-clamp or current-clamp experiment.
- Formal definition: A time series showing controlled voltage, applied current, or measured current under clamp conditions.
- Common confusion: A current trace and a voltage trace show different quantities.
- Chapter first introduced: Chapter 6.

<a id="closed-state"></a>
### Closed state
- Plain-language definition: The condition when a channel is not letting ions through.
- Formal definition: A channel conformation with negligible ion conductance through the pore.
- Common confusion: Closed does not mean destroyed; the channel can open later.
- Chapter first introduced: Chapter 7.

<a id="coefficient-of-variation"></a>
### Coefficient of variation
- Plain-language definition: A unit-free measure of variability compared with the mean.
- Formal definition: Standard deviation divided by mean, often used to compare relative spread across conditions.
- Common confusion: A larger CV means more relative variability, not necessarily more spikes.
- Chapter first introduced: Chapter 7.

<a id="concentration-gradient"></a>
### Concentration gradient
- Plain-language definition: A difference in how much of a substance is in two places.
- Formal definition: A spatial difference in concentration that can drive diffusion from high concentration toward low concentration.
- Common confusion: A gradient is not a wall; it is a difference that can push movement.
- Chapter first introduced: Chapter 2.

<a id="concentration-ratio"></a>
### Concentration ratio
- Plain-language definition: One concentration divided by another concentration.
- Formal definition: A dimensionless comparison such as outside concentration divided by inside concentration.
- Common confusion: A ratio below 1 is not negative; its log10 can be negative.
- Chapter first introduced: Chapter 2.

<a id="conductance"></a>
### Conductance
- Plain-language definition: How easily current can flow through a pathway.
- Formal definition: The reciprocal of resistance, often representing ion-channel availability in membrane models.
- Common confusion: Conductance is not voltage; it controls how strongly a pathway can influence voltage.
- Chapter first introduced: Chapter 6.

<a id="current"></a>
### Current
- Plain-language definition: Movement of electric charge.
- Formal definition: Charge flow per unit time, often carried by ions in neurons.
- Common confusion: Current is not the same as voltage; current moves charge, voltage is a difference in potential.
- Chapter first introduced: Chapter 6.

<a id="current-clamp"></a>
### Current clamp
- Plain-language definition: An experiment where the researcher injects current and watches voltage change.
- Formal definition: An electrophysiological recording mode that controls applied current while measuring membrane voltage.
- Common confusion: Current clamp is the opposite control logic from voltage clamp.
- Chapter first introduced: Chapter 6.

<a id="cv"></a>
### CV
- Plain-language definition: Short for coefficient of variation, a variability number with no unit.
- Formal definition: CV = standard deviation / mean, often applied to interspike intervals.
- Common confusion: CV is not measured in ms, even when it is calculated from ISIs in ms.
- Chapter first introduced: Chapter 7.

<a id="dendrite"></a>
### Dendrite
- Plain-language definition: A branched receiving region of a neuron.
- Formal definition: A neuronal process specialized for receiving synaptic input and carrying graded signals toward integration regions.
- Common confusion: Dendrites are not just decorative branches; they are input structures.
- Chapter first introduced: Chapter 1.

<a id="depolarization"></a>
### Depolarization
- Plain-language definition: A voltage change where the inside becomes less negative.
- Formal definition: A positive shift in membrane potential toward 0 mV or above.
- Common confusion: Depolarization does not always mean the inside becomes positive; it may only become less negative.
- Chapter first introduced: Chapter 1.

<a id="diffusion"></a>
### Diffusion
- Plain-language definition: Spreading from where there is more to where there is less.
- Formal definition: Net movement down a concentration gradient due to random molecular motion.
- Common confusion: Diffusion is not the only force on ions because electrical force also matters.
- Chapter first introduced: Chapter 2.

<a id="driving-force"></a>
### Driving force
- Plain-language definition: How far V_m is from the voltage an ion pathway pulls toward.
- Formal definition: The voltage difference V_m - E for an ion pathway, which contributes to current size and direction.
- Common confusion: Driving force is not the same as conductance; current depends on both.
- Chapter first introduced: Chapter 6.

<a id="e_k"></a>
### E_K
- Plain-language definition: The reversal or equilibrium potential for potassium.
- Formal definition: The voltage at which net K+ current through a K+ pathway would be zero under specified conditions.
- Common confusion: E_K is not always equal to the resting membrane potential, though it strongly influences it.
- Chapter first introduced: Chapter 6.

<a id="e_leak"></a>
### E_leak
- Plain-language definition: The voltage target for leak pathways in a simple model.
- Formal definition: The reversal potential assigned to the combined leak conductance in a membrane model.
- Common confusion: Leak does not mean damage; it means resting pathway activity in the model.
- Chapter first introduced: Chapter 6.

<a id="e_na"></a>
### E_Na
- Plain-language definition: The reversal or equilibrium potential for sodium.
- Formal definition: The voltage at which net Na+ current through a Na+ pathway would be zero under specified conditions.
- Common confusion: E_Na is a voltage target, not the sodium concentration itself.
- Chapter first introduced: Chapter 6.

<a id="electrical-force"></a>
### Electrical force
- Plain-language definition: Push or pull caused by electric charge.
- Formal definition: The force on charged particles due to an electric field or voltage difference.
- Common confusion: Electrical force can oppose diffusion; the two do not always point the same way.
- Chapter first introduced: Chapter 2.

<a id="electrochemical-gradient"></a>
### Electrochemical gradient
- Plain-language definition: The combined push from concentration difference and electrical attraction or repulsion.
- Formal definition: The net driving influence on an ion from both chemical concentration gradient and electrical potential difference.
- Common confusion: It is not only a concentration gradient; charge matters too.
- Chapter first introduced: Chapter 2.

<a id="equilibrium-potential"></a>
### Equilibrium potential
- Plain-language definition: The voltage where one ion's chemical push and electrical pull balance.
- Formal definition: The membrane potential at which net movement of a specific ion is zero for a given concentration gradient and permeability pathway.
- Common confusion: It is for one ion at a time, not automatically the whole cell's voltage.
- Chapter first introduced: Chapter 2.

<a id="epsp"></a>
### EPSP
- Plain-language definition: A small excitatory voltage change that moves V_m toward threshold.
- Formal definition: Excitatory postsynaptic potential, a graded postsynaptic depolarization that increases spike likelihood.
- Common confusion: An EPSP makes a spike more likely but does not guarantee one.
- Chapter first introduced: Chapter 3.

<a id="evidence"></a>
### Evidence
- Plain-language definition: The graph, data, calculation, or observation that supports a claim.
- Formal definition: Information used to evaluate a scientific claim.
- Common confusion: Evidence must be interpreted; it does not explain itself.
- Chapter first introduced: Chapter 8.

<a id="firing-rate"></a>
### Firing rate
- Plain-language definition: How many spikes happen per second.
- Formal definition: Spike count divided by time, usually reported in hertz.
- Common confusion: Firing rate does not show exact spike timing.
- Chapter first introduced: Chapter 5.

<a id="g_k"></a>
### g_K
- Plain-language definition: Potassium conductance.
- Formal definition: The conductance assigned to K+ channel pathways in a membrane model.
- Common confusion: g_K is not the same as K+ concentration.
- Chapter first introduced: Chapter 6.

<a id="g_na"></a>
### g_Na
- Plain-language definition: Sodium conductance.
- Formal definition: The conductance assigned to Na+ channel pathways in a membrane model.
- Common confusion: g_Na is not sodium current by itself; current also depends on driving force.
- Chapter first introduced: Chapter 6.

<a id="graded-potential"></a>
### Graded potential
- Plain-language definition: A small voltage change whose size can vary.
- Formal definition: A local membrane potential change that can vary in amplitude and usually decays with distance or time.
- Common confusion: Graded potentials are not all-or-none spikes.
- Chapter first introduced: Chapter 3.

<a id="graph-label"></a>
### Graph label
- Plain-language definition: Text on a graph that tells what an axis, line, or condition means.
- Formal definition: A visual annotation that identifies variables, units, conditions, or plotted quantities.
- Common confusion: A graph without labels may look scientific but cannot be interpreted reliably.
- Chapter first introduced: Chapter 8.

<a id="histogram"></a>
### Histogram
- Plain-language definition: A graph that counts how often values fall into ranges.
- Formal definition: A distribution plot using bins to summarize frequency of numerical values.
- Common confusion: A histogram is not the same as a time trace.
- Chapter first introduced: Chapter 5.

<a id="hodgkin-huxley-model"></a>
### Hodgkin-Huxley model
- Plain-language definition: A famous model that describes spikes using membrane voltage and ion conductances.
- Formal definition: A conductance-based mathematical model of action-potential generation using voltage-dependent Na+, K+, and leak currents.
- Common confusion: The beginner goal is to understand the pieces, not derive the full equations.
- Chapter first introduced: Chapter 6.

<a id="hyperpolarization"></a>
### Hyperpolarization
- Plain-language definition: A voltage change where the inside becomes more negative.
- Formal definition: A negative shift in membrane potential away from 0 mV.
- Common confusion: Hyperpolarization is not the same as repolarization; repolarization means returning after depolarization.
- Chapter first introduced: Chapter 1.

<a id="hz"></a>
### Hz
- Plain-language definition: A unit meaning "per second."
- Formal definition: Hertz, cycles or events per second; in spike trains, spikes per second.
- Common confusion: Hz is a rate unit, not a voltage unit.
- Chapter first introduced: Chapter 5.

<a id="i_app"></a>
### I_app
- Plain-language definition: Applied current put into a model or experiment.
- Formal definition: An externally imposed input current term in electrophysiology or membrane modeling.
- Common confusion: I_app is input current, not the membrane voltage itself.
- Chapter first introduced: Chapter 6.

<a id="initial-segment"></a>
### Initial segment
- Plain-language definition: The early axon region where spikes often start.
- Formal definition: The axon initial segment, a specialized membrane region with high density of voltage-gated channels.
- Common confusion: It is closely related to the axon hillock but not identical in detailed anatomy.
- Chapter first introduced: Chapter 1.

<a id="interspike-interval"></a>
### Interspike interval
- Plain-language definition: The time between one spike and the next.
- Formal definition: The elapsed time between consecutive action potentials in a spike train.
- Common confusion: ISI is a time interval, not a spike count.
- Chapter first introduced: Chapter 5.

<a id="ion"></a>
### Ion
- Plain-language definition: An atom or molecule with an electric charge.
- Formal definition: A charged chemical species formed by gaining or losing electrons or by carrying charged groups.
- Common confusion: Ions are not electrons; common neural ions include Na+, K+, Cl-, and Ca2+.
- Chapter first introduced: Chapter 2.

<a id="ipsp"></a>
### IPSP
- Plain-language definition: A small inhibitory voltage change that makes threshold harder to reach.
- Formal definition: Inhibitory postsynaptic potential, a graded postsynaptic effect that decreases spike likelihood.
- Common confusion: Inhibition is not simply "turning off" the neuron.
- Chapter first introduced: Chapter 3.

<a id="isi"></a>
### ISI
- Plain-language definition: Short for interspike interval.
- Formal definition: The interval between consecutive spikes, usually measured in ms.
- Common confusion: ISI and firing rate are related but not identical.
- Chapter first introduced: Chapter 5.

<a id="jitter"></a>
### Jitter
- Plain-language definition: Small variation in when spikes happen across trials.
- Formal definition: Trial-to-trial variability in event timing.
- Common confusion: Jitter can be measured; it is not just messy behavior.
- Chapter first introduced: Chapter 7.

<a id="k"></a>
### K+
- Plain-language definition: A potassium ion with one positive charge.
- Formal definition: A monovalent cation central to resting membrane potential and spike repolarization.
- Common confusion: K+ often moves outward by diffusion but can be pulled inward electrically.
- Chapter first introduced: Chapter 2.

<a id="leak-channel"></a>
### Leak channel
- Plain-language definition: A channel that is open at rest and lets some ions pass.
- Formal definition: A resting membrane channel contributing baseline permeability, especially important for K+ in many neurons.
- Common confusion: "Leak" does not mean the cell membrane is broken.
- Chapter first introduced: Chapter 2.

<a id="leak-conductance"></a>
### Leak conductance
- Plain-language definition: The conductance of resting leak pathways in a model.
- Formal definition: A model conductance representing channels active near rest, often grouped into a leak current.
- Common confusion: It is a simplified combined pathway, not always one exact channel type.
- Chapter first introduced: Chapter 6.

<a id="limitation"></a>
### Limitation
- Plain-language definition: What a model, graph, or explanation cannot prove.
- Formal definition: A boundary on interpretation caused by assumptions, missing data, measurement limits, or model simplification.
- Common confusion: Stating a limitation makes the science stronger, not weaker.
- Chapter first introduced: Chapter 8.

<a id="log10"></a>
### log10
- Plain-language definition: The power of 10 needed to make a number.
- Formal definition: The base-10 logarithm; for example, log10(100) = 2 because 10^2 = 100.
- Common confusion: log10 of a number below 1 is negative, even though the number itself is positive.
- Chapter first introduced: Chapter 2.

<a id="mean-isi"></a>
### Mean ISI
- Plain-language definition: The average time between neighboring spikes.
- Formal definition: The arithmetic mean of interspike intervals in a spike train.
- Common confusion: Mean ISI summarizes intervals but can hide irregular timing.
- Chapter first introduced: Chapter 5.

<a id="membrane"></a>
### Membrane
- Plain-language definition: The thin boundary around a cell.
- Formal definition: A lipid bilayer with embedded proteins that separates inside from outside and controls exchange.
- Common confusion: The membrane is not just plastic wrap; it contains channels, receptors, and pumps.
- Chapter first introduced: Chapter 1.

<a id="membrane-potential"></a>
### Membrane potential
- Plain-language definition: The voltage inside the cell compared with outside.
- Formal definition: The electrical potential difference across the cell membrane, usually written V_m.
- Common confusion: It does not mean the whole inside is full of extra negative charge.
- Chapter first introduced: Chapter 1.

<a id="metric"></a>
### Metric
- Plain-language definition: A number used to summarize something.
- Formal definition: A quantitative measure such as firing rate, mean ISI, or CV.
- Common confusion: A metric helps summarize evidence but does not replace looking at the graph.
- Chapter first introduced: Chapter 8.

<a id="model"></a>
### Model
- Plain-language definition: A simplified version of a system used to understand or test an idea.
- Formal definition: A conceptual, mathematical, or computational representation of selected parts of a real system.
- Common confusion: A model is not the same as the real neuron.
- Chapter first introduced: Chapter 8.

<a id="mv"></a>
### mV
- Plain-language definition: Millivolts, a small unit of voltage.
- Formal definition: One millivolt is one-thousandth of a volt.
- Common confusion: mV measures voltage, not time or spike count.
- Chapter first introduced: Chapter 1.

<a id="ms"></a>
### ms
- Plain-language definition: Milliseconds, thousandths of a second.
- Formal definition: One millisecond is 0.001 seconds.
- Common confusion: ms is a time unit, not a voltage unit.
- Chapter first introduced: Chapter 4.

<a id="myelin"></a>
### Myelin
- Plain-language definition: Insulating wrapping around some axons.
- Formal definition: A glial membrane sheath that increases conduction efficiency and supports saltatory propagation.
- Common confusion: Myelin does not create the message; it changes how efficiently spikes travel.
- Chapter first introduced: Chapter 4.

<a id="na"></a>
### Na+
- Plain-language definition: A sodium ion with one positive charge.
- Formal definition: A monovalent cation important for action-potential depolarization.
- Common confusion: Na+ concentration and Na+ conductance are different ideas.
- Chapter first introduced: Chapter 2.

<a id="na-k-pump"></a>
### Na+/K+ pump
- Plain-language definition: A protein that helps maintain sodium and potassium gradients.
- Formal definition: The sodium-potassium ATPase that moves Na+ out and K+ in using ATP.
- Common confusion: The pump maintains gradients over time but is not the direct whole cause of resting voltage.
- Chapter first introduced: Chapter 2.

<a id="nernst-equation"></a>
### Nernst equation
- Plain-language definition: A formula that estimates the balance voltage for one ion.
- Formal definition: An equation relating an ion's equilibrium potential to its concentration ratio, charge, temperature, and constants.
- Common confusion: It applies to one ion at a time, not automatically to all ions mixed together.
- Chapter first introduced: Chapter 2.

<a id="neuron"></a>
### Neuron
- Plain-language definition: A cell specialized for receiving, processing, and sending signals.
- Formal definition: An excitable nervous-system cell that communicates through electrical and chemical signaling.
- Common confusion: A neuron is a living cell, not a copper wire.
- Chapter first introduced: Chapter 1.

<a id="neurotransmitter"></a>
### Neurotransmitter
- Plain-language definition: A chemical message released at a synapse.
- Formal definition: A signaling molecule released by a presynaptic cell that binds receptors on a target cell.
- Common confusion: Neurotransmitter does not become the voltage signal directly; it changes channel activity.
- Chapter first introduced: Chapter 3.

<a id="node-of-ranvier"></a>
### Node of Ranvier
- Plain-language definition: A gap between myelin segments where spikes are regenerated.
- Formal definition: An unmyelinated axonal region enriched in voltage-gated channels, supporting saltatory conduction.
- Common confusion: The spike does not literally teleport; it is regenerated at nodes.
- Chapter first introduced: Chapter 4.

<a id="noise"></a>
### Noise
- Plain-language definition: Random-looking variation in a signal or process.
- Formal definition: Fluctuation in measured or biological variables due to stochastic processes, background activity, or measurement limits.
- Common confusion: Noise can have causes and measurable patterns.
- Chapter first introduced: Chapter 7.

<a id="open-fraction"></a>
### Open fraction
- Plain-language definition: The fraction of time or channels that are open.
- Formal definition: Open time divided by total time, or number open divided by total number in a channel population.
- Common confusion: Open fraction is a ratio with no unit, not a current.
- Chapter first introduced: Chapter 7.

<a id="open-state"></a>
### Open state
- Plain-language definition: The condition when a channel lets ions pass.
- Formal definition: A channel conformation with nonzero conductance through the pore.
- Common confusion: Open state is all-or-none for one channel, but many channels together can create graded effects.
- Chapter first introduced: Chapter 7.

<a id="overshoot"></a>
### Overshoot
- Plain-language definition: The part of a spike when V_m rises above 0 mV.
- Formal definition: The positive-voltage phase of an action potential relative to the outside reference.
- Common confusion: Overshoot is not the same as threshold.
- Chapter first introduced: Chapter 4.

<a id="patch-clamp"></a>
### Patch clamp
- Plain-language definition: A method for recording tiny currents from a membrane patch or cell.
- Formal definition: An electrophysiological technique using a glass pipette to measure ion-channel or whole-cell currents.
- Common confusion: Patch clamp measures current or voltage depending on mode; it is not a microscope image.
- Chapter first introduced: Chapter 7.

<a id="permeability"></a>
### Permeability
- Plain-language definition: How easily something can cross a barrier.
- Formal definition: The ability of ions or molecules to pass through a membrane, often controlled by channels and transporters.
- Common confusion: Permeability is selective; membranes do not let every ion cross equally.
- Chapter first introduced: Chapter 2.

<a id="postsynaptic-cell"></a>
### Postsynaptic cell
- Plain-language definition: The cell receiving a synaptic signal.
- Formal definition: The target cell whose receptors respond to neurotransmitter released by a presynaptic cell.
- Common confusion: Postsynaptic does not always mean a neuron; muscles and glands can also receive signals.
- Chapter first introduced: Chapter 3.

<a id="postsynaptic-potential"></a>
### Postsynaptic potential
- Plain-language definition: A voltage change in the receiving cell after synaptic input.
- Formal definition: A graded membrane potential change caused by synaptic receptor activation.
- Common confusion: It is not automatically an action potential.
- Chapter first introduced: Chapter 3.

<a id="presynaptic-terminal"></a>
### Presynaptic terminal
- Plain-language definition: The sending side of a synapse, often at an axon terminal.
- Formal definition: A specialized neuronal ending that releases neurotransmitter onto a postsynaptic target.
- Common confusion: Presynaptic refers to the sending side, not the receiving dendrite.
- Chapter first introduced: Chapter 3.

<a id="propagation"></a>
### Propagation
- Plain-language definition: Travel of a spike along an axon.
- Formal definition: Sequential regeneration of an action potential along excitable membrane.
- Common confusion: Propagation is not passive sliding of one fixed voltage bump.
- Chapter first introduced: Chapter 4.

<a id="raster-plot"></a>
### Raster plot
- Plain-language definition: A graph where each tick mark shows a spike time on a trial.
- Formal definition: A spike-time display with trials arranged on one axis and time on the other.
- Common confusion: A raster shows timing; it is not a voltage trace.
- Chapter first introduced: Chapter 5.

<a id="rate-code"></a>
### Rate code
- Plain-language definition: Information represented by how often spikes occur.
- Formal definition: A neural coding idea in which firing rate carries information about a stimulus or condition.
- Common confusion: Rate coding does not mean timing never matters.
- Chapter first introduced: Chapter 5.

<a id="reasoning"></a>
### Reasoning
- Plain-language definition: The explanation that connects evidence to a claim.
- Formal definition: The causal or logical bridge between data and conclusion.
- Common confusion: Repeating the evidence is not the same as explaining why it supports the claim.
- Chapter first introduced: Chapter 8.

<a id="receptor"></a>
### Receptor
- Plain-language definition: A protein that detects a signal such as a neurotransmitter.
- Formal definition: A molecule, often a membrane protein, that binds a ligand and changes cell activity.
- Common confusion: A receptor is not the same as a whole synapse.
- Chapter first introduced: Chapter 3.

<a id="refractory-period"></a>
### Refractory period
- Plain-language definition: A recovery time after a spike when firing again is harder.
- Formal definition: A period after an action potential when ion-channel states reduce excitability.
- Common confusion: It is not fatigue in the everyday sense; it comes from channel recovery and conductance changes.
- Chapter first introduced: Chapter 4.

<a id="regeneration"></a>
### Regeneration
- Plain-language definition: Restarting the spike at the next patch of membrane.
- Formal definition: Local reinitiation of an action potential as depolarization brings adjacent membrane to threshold.
- Common confusion: Regeneration is not the same as repairing damage.
- Chapter first introduced: Chapter 4.

<a id="repolarization"></a>
### Repolarization
- Plain-language definition: The falling phase when voltage moves back toward negative values after a spike.
- Formal definition: The return of membrane potential toward resting levels after depolarization, often involving K+ conductance.
- Common confusion: Repolarization is not the same as hyperpolarization, though hyperpolarization can follow it.
- Chapter first introduced: Chapter 4.

<a id="resting-membrane-potential"></a>
### Resting membrane potential
- Plain-language definition: The usual membrane voltage when a neuron is not firing.
- Formal definition: The steady membrane potential set by ion gradients and resting membrane permeabilities.
- Common confusion: It is not caused only by the Na+/K+ pump.
- Chapter first introduced: Chapter 2.

<a id="reversal-potential"></a>
### Reversal potential
- Plain-language definition: The voltage where current through a pathway changes direction.
- Formal definition: The membrane potential at which net ionic current through a specified pathway is zero and reverses sign across that voltage.
- Common confusion: Reversal potential and equilibrium potential are closely related, but reversal potential is often used for a channel pathway or current.
- Chapter first introduced: Chapter 6.

<a id="sd"></a>
### SD
- Plain-language definition: Short for standard deviation.
- Formal definition: A statistical measure of spread around a mean.
- Common confusion: SD has the same unit as the measured quantity, unlike CV.
- Chapter first introduced: Chapter 7.

<a id="selective-permeability"></a>
### Selective permeability
- Plain-language definition: The membrane lets some ions cross more easily than others.
- Formal definition: Differential membrane permeability to ions or molecules due to lipid properties and membrane proteins.
- Common confusion: Selective does not mean only one ion can ever cross.
- Chapter first introduced: Chapter 2.

<a id="simulation"></a>
### Simulation
- Plain-language definition: Running a model to see what it predicts.
- Formal definition: Computational execution of a model under chosen parameters or conditions.
- Common confusion: Simulation output is not automatically biological proof.
- Chapter first introduced: Chapter 8.

<a id="single-channel"></a>
### Single channel
- Plain-language definition: One ion-channel protein or channel pore.
- Formal definition: An individual channel whose open and closed states can produce discrete current steps.
- Common confusion: One channel opens all-or-none, but a whole membrane has many channels.
- Chapter first introduced: Chapter 7.

<a id="soma"></a>
### Soma
- Plain-language definition: The cell body of a neuron.
- Formal definition: The neuronal cell body containing the nucleus and much of the cell's metabolic machinery.
- Common confusion: The soma supports and integrates, but it is not the only input region.
- Chapter first introduced: Chapter 1.

<a id="source-note"></a>
### Source note
- Plain-language definition: A short note saying where a figure, data point, or idea came from.
- Formal definition: Attribution text identifying origin, evidence type, access information, and reuse context.
- Common confusion: A caption explains the figure; a source note documents provenance.
- Chapter first introduced: Chapter 8.

<a id="spatial-summation"></a>
### Spatial summation
- Plain-language definition: Adding inputs that arrive at different places on the neuron.
- Formal definition: Integration of postsynaptic potentials from multiple synaptic locations.
- Common confusion: Spatial summation is about location, not timing.
- Chapter first introduced: Chapter 3.

<a id="spike"></a>
### Spike
- Plain-language definition: A short name for an action potential.
- Formal definition: A rapid, transient action potential event in membrane voltage.
- Common confusion: A spike is not just any upward line on a graph.
- Chapter first introduced: Chapter 4.

<a id="spike-train"></a>
### Spike train
- Plain-language definition: A sequence of spike times.
- Formal definition: An ordered set of action potentials produced by a neuron over time.
- Common confusion: Spike trains carry information through timing and rate, not spike height alone.
- Chapter first introduced: Chapter 5.

<a id="standard-deviation"></a>
### Standard deviation
- Plain-language definition: A number that says how spread out values are.
- Formal definition: A statistic measuring typical distance of values from their mean.
- Common confusion: Standard deviation is not the range; it is a summary of spread around the mean.
- Chapter first introduced: Chapter 7.

<a id="stochastic"></a>
### Stochastic
- Plain-language definition: Involving randomness in timing or outcome.
- Formal definition: Describing a process whose individual events are probabilistic even if overall statistics are measurable.
- Common confusion: Stochastic does not mean causeless.
- Chapter first introduced: Chapter 7.

<a id="synapse"></a>
### Synapse
- Plain-language definition: A communication point between cells.
- Formal definition: A specialized junction where a presynaptic cell influences a postsynaptic cell through chemical or electrical signaling.
- Common confusion: A synapse is not just the gap; it includes sending and receiving machinery.
- Chapter first introduced: Chapter 1.

<a id="synaptic-cleft"></a>
### Synaptic cleft
- Plain-language definition: The tiny gap between the sending and receiving sides of a chemical synapse.
- Formal definition: The extracellular space across which neurotransmitter diffuses from presynaptic terminal to postsynaptic receptors.
- Common confusion: The cleft is only one part of the synapse.
- Chapter first introduced: Chapter 3.

<a id="temporal-summation"></a>
### Temporal summation
- Plain-language definition: Adding inputs that arrive close together in time.
- Formal definition: Integration of postsynaptic potentials across time when earlier signals have not fully faded.
- Common confusion: Temporal summation is about timing, not location.
- Chapter first introduced: Chapter 3.

<a id="threshold"></a>
### Threshold
- Plain-language definition: The voltage level where a spike becomes likely.
- Formal definition: A membrane potential at which positive feedback through voltage-gated channels can trigger an action potential.
- Common confusion: Threshold is not a fixed universal number for all neurons.
- Chapter first introduced: Chapter 3.

<a id="timing-code"></a>
### Timing code
- Plain-language definition: Information represented by exactly when spikes happen.
- Formal definition: A neural coding idea in which spike timing patterns carry information beyond average firing rate.
- Common confusion: Timing coding does not mean firing rate is irrelevant.
- Chapter first introduced: Chapter 5.

<a id="trial"></a>
### Trial
- Plain-language definition: One repeated run of the same stimulus or simulation.
- Formal definition: A single repetition of an experiment, recording, or model condition.
- Common confusion: A trial is not one spike; one trial can contain many spikes.
- Chapter first introduced: Chapter 5.

<a id="trial-to-trial-variability"></a>
### Trial-to-trial variability
- Plain-language definition: Differences between repeated runs of the same condition.
- Formal definition: Variation in measured responses across trials under similar stimulus or model conditions.
- Common confusion: Variability can be meaningful even when the average is unchanged.
- Chapter first introduced: Chapter 7.

<a id="trigger-zone"></a>
### Trigger zone
- Plain-language definition: The region where combined inputs can start a spike.
- Formal definition: A membrane region, often the axon initial segment, where voltage-gated channel density supports action-potential initiation.
- Common confusion: The trigger zone does not "think"; it responds to voltage and channel properties.
- Chapter first introduced: Chapter 3.

<a id="v_m"></a>
### V_m
- Plain-language definition: The symbol for membrane potential.
- Formal definition: Membrane voltage, usually inside potential relative to outside reference.
- Common confusion: V_m is a voltage, not a current.
- Chapter first introduced: Chapter 2.

<a id="voltage"></a>
### Voltage
- Plain-language definition: A difference in electrical potential between two places.
- Formal definition: Electric potential difference, measured in volts or millivolts.
- Common confusion: Voltage is not a substance moving down the axon.
- Chapter first introduced: Chapter 1.

<a id="voltage-clamp"></a>
### Voltage clamp
- Plain-language definition: An experiment where the researcher controls voltage and measures current.
- Formal definition: An electrophysiological recording mode that holds membrane potential at commanded values while measuring the current required.
- Common confusion: Voltage clamp records current responses; it does not simply watch natural voltage changes.
- Chapter first introduced: Chapter 6.

<a id="voltage-gated-channel"></a>
### Voltage-gated channel
- Plain-language definition: A channel that opens or closes depending on voltage.
- Formal definition: An ion channel whose gating state depends on membrane potential.
- Common confusion: Voltage-gated channels are not always open; their state depends on voltage and time.
- Chapter first introduced: Chapter 4.
