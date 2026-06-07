# From neuron shape to noisy spike trains

This is the source version of the eight-chapter high-school textbook. It keeps the no-calculus promise and preserves the ions -> spikes -> noise story while making the course systematic.

The student should read the chapters in order. The core path is:

1. Week A: neurons are living signaling cells.
2. Week B: ions and gradients explain why rest is negative.
3. Week C: graded synaptic signals approach threshold.
4. Week D: action potentials begin and travel.
5. Week E: spike trains carry neural information through rate and timing.
6. Week F: circuit ideas give Hodgkin-Huxley intuition.
7. Week G: random single channels can affect spike-time variability.
8. Week H: a capstone project turns the course into evidence and communication.

![Learning roadmap](figures/generated/week_roadmap.svg)

## Week-By-Week Syllabus

This syllabus mirrors the biological and quantitative dependencies in the minibook while making the neuro-information layer explicit. The student should not skip ahead: each week supplies vocabulary, graph-reading habits, and small calculations needed later.

| Week | Current minibook anchor | Revised textbook-style chapter | Prerequisites | Learning objectives | Basic calculations | Estimated total time |
|---|---|---|---|---|---|---:|
| Week A | Neuron shape, parts, voltage language | Neurons as signaling cells | Basic cell biology, atoms/charge | Identify dendrites, soma, axon, terminals; explain input/decision/output; distinguish charge, potential, voltage | mV changes such as -70 to -55 mV | 4.0-4.5 h |
| Week B | Ions, diffusion, resting potential | Ions, gradients, and why rest is negative | Week A | Explain Na+, K+, Cl-, Ca2+ distributions; distinguish diffusion vs electrical force; explain selective permeability | Sign-only Nernst reasoning; simple concentration-ratio thinking | 4.5-5.0 h |
| Week C | Synapses and threshold | Graded signals and threshold | Weeks A-B | Explain EPSPs, IPSPs, temporal/spatial summation, trigger zone | Add simple EPSP values to estimate threshold approach | 4.0-4.5 h |
| Week D | Action potentials and propagation | How spikes begin and travel | Weeks A-C | Narrate depolarization, repolarization, refractory period, myelin, nodes | Read phase durations and threshold crossings from graphs | 4.5-5.0 h |
| Week E | Spike trains are present but compressed | Spike trains and neural information | Weeks A-D | Distinguish single-spike amplitude from firing rate/timing; interpret rasters and rate plots | Spike rate, ISI, mean ISI | 4.0-4.5 h |
| Week F | HH week | Circuits and Hodgkin-Huxley intuition | Weeks A-E | Read membrane-as-capacitor analogy; interpret conductance and reversal potential; explain clamp experiments | Use I = g(V_m - E) qualitatively and numerically in simple cases | 4.5-5.0 h |
| Week G | Random channels and variability | From single channels to timing variability | Weeks A-F | Explain stochastic gating, channel noise, finite-size fluctuations, CV of ISI, trial-to-trial jitter | ISI SD and CV; open-fraction fluctuations from repeated trials | 4.5-5.0 h |
| Week H | Mini-project and final talk | Evidence, explanation, and communication | All earlier weeks | Form a hypothesis, run a simple model, summarize evidence, state limitations, communicate clearly | Compare conditions, summarize means/CVs | 4.0-5.0 h |

OpenStax-style dependency order supports the early biology sequence: graded potentials and synapses should come before action potentials, and action potentials should come before spike trains. Later weeks use authentic modeling language from Allen Cell Types, NEURON, and NetPyNE-style ecosystems without requiring the student to master those tools yet.

## How To Study

Each chapter follows the same lesson rhythm. The order matters: look first, explain next, read one graph or diagram carefully, then calculate.

| Lesson component | Typical time | Purpose |
|---|---:|---|
| Visual opener | 15-20 min | Start from an image, trace, simulation, or animation still. |
| Core concept lesson | 35-45 min | Define vocabulary and tell the causal story in plain language. |
| Graph/diagram-reading block | 20-30 min | Read one key visual before doing formula work. |
| Worked example | 15-25 min | Solve one concrete example step by step. |
| Basic calculation | 15-25 min | Do one small numeric task, never more than two new steps. |
| Mini-lab or code | 20-40 min | Use a simulation, spreadsheet, notebook, drawing, or physical analogy. |
| Retrieval quiz and reflection | 10-15 min | Check memory, explain the idea aloud, and decide what needs review. |

Every week also names prerequisites, required vocabulary, target misconceptions, homework, answer keys, and assessment checkpoints. The student should use these sections actively: cover the answers, try the questions, then compare.

## Teaching Infrastructure

The book is designed to feel like a short textbook, not a packet of notes. Each chapter now uses the same support system.

| Infrastructure | How the student uses it | How the mentor uses it |
|---|---|---|
| Concept Figure A | Study the clean diagram and explain the mechanism in words. | Ask what the diagram intentionally leaves out. |
| Reality Figure B | Compare the simplified idea with a real image, trace, dataset, or model output. | Ask what kind of evidence the figure is: real data, cartoon, simulation, or storyboard. |
| What this figure is / is not | Prevents mixing up mechanism, evidence, and idealization. | Use this box whenever the student over-interprets a cartoon. |
| Worked examples | Read the solution, cover it, then solve the same style of problem again. | Gradually remove hints by the middle of the course. |
| Graph-reading blocks | Read axes, units, and visual patterns before doing formulas. | Ask for a graph interpretation before asking for a mechanism name. |
| Mini-labs and code | Use simple drawings, coins, spreadsheets, or notebooks to make the idea active. | Keep the code tiny and ask for a sentence of interpretation. |
| Low-stakes checks | Treat quizzes as feedback, not grades. | Look for misconceptions, especially sign errors and graph-reading errors. |
| Cumulative glossary | Use glossary words as anchors across weeks. | Ask the student to define a new term and use it in a causal sentence. |

## Pedagogical Scaffolding Map

Every chapter now makes the learning target, likely misconception, formative check, support path, and extension path explicit. The student should treat these as study controls: know the goal, check understanding, repair one misconception, then move forward.

| Week | Learning outcome | Misconception to address directly | Formative check | Support for struggling student | Extension for advanced student |
|---|---|---|---|---|---|
| A | Draw and explain a neuron as an input/decision/output system. | "Every neuron looks like the same cartoon." | Label an unlabeled neuron image. | Use color-coded part cards and tracing overlays. | Compare Purkinje vs pyramidal morphology. |
| B | Explain why resting voltage is usually negative inside. | "The Na+/K+ pump directly causes all of resting potential." | One-paragraph explanation of K+ leak plus gradients. | Use one-ion-at-a-time reasoning before mixed-ion reasoning. | Compare Nernst vs Goldman qualitatively. |
| C | Explain EPSP/IPSP and summation. | "Any single input automatically causes a spike." | Predict whether a short input sequence reaches threshold. | Use tactile tokens for summation. | Add inhibitory inputs and discuss location effects. |
| D | Narrate action-potential phases and propagation. | "A stronger stimulus makes a taller spike." | Annotate a blank action-potential graph. | Provide phase cards with matching channel behavior. | Compare unmyelinated vs myelinated conduction. |
| E | Interpret spike rasters and ISIs. | "Information is only in spike height." | Convert raster to firing-rate description. | Start with hand-counting spikes before the rate formula. | Discuss timing codes and population coding qualitatively. |
| F | Read HH-like current statements in words. | "Voltage and current are the same thing." | Translate I = g(V_m - E) into plain English. | Use water-flow/circuit analogy and unit labels repeatedly. | Add RC time-constant intuition or simple clamp traces. |
| G | Explain why finite random channel populations can jitter spike timing. | "Randomness means there is no mechanism." | Compute ISI mean and CV from a short list. | Use coin-flip analogies and repeated-trial visuals. | Compare deterministic vs stochastic simulations. |
| H | Make and defend a claim with data. | "A graph alone is a conclusion." | CER paragraph: claim, evidence, reasoning. | Give sentence frames and interpretation prompts. | Add limitation analysis and next-step experimental design. |

### Feedback Routine

At the end of each section, the student should answer the local quick check before continuing. If she misses it, she should revise the sentence, redraw the key part of the figure, or redo the calculation immediately. The goal is not general praise; the goal is actionable feedback that tells her what to repair next.

## Assessment Architecture

Assessment has three layers, and only the final layer is summative. The point is to make feedback useful while the student can still act on it.

| Layer | When | What it includes | How to use it |
|---|---|---|---|
| Daily formative checks | Each study day | One prediction question, one graph-reading question, one plain-language explanation, and one quantitative item. | Low-stakes. Discuss immediately and revise one answer before moving on. |
| Weekly chapter checks | End of each chapter | Five to eight questions plus one short oral explanation. | Check readiness for the next week; aim for about 80% on core items plus a coherent oral explanation. |
| Summative mini-project | Week H | One evidence-based claim with a figure, timing metric, limitation, and short presentation. | Assess scientific explanation, not coding sophistication. |

The final project should be graded on conceptual accuracy, correct graph labeling, correct use of terms, at least one timing calculation, one limitation, and the ability to distinguish model output from biological evidence.

## Student Core And Mentor Background Reading

Keep the student's assigned reading narrow. The core learning path is this minibook, selected OpenStax sections, selected Neuroscience Online pages, one or two HHMI/PhET interactives, and the local figures/notebooks. The mentor background path is different: those sources should improve the explanations and examples, but they do not need to be assigned in full to a high-school learner.

| Week | Student core reading and activity | Mentor background only |
|---|---|---|
| A | This minibook Chapter 1; HHMI BioInteractive neuron background; OpenStax Biology 2e 35.2 only for the broad neuron-communication picture. | Allen Cell Types morphology views; NeuroMorpho examples if a real morphology comparison would help. |
| B | This minibook Chapter 2; OpenStax Biology 2e 35.2 membrane-potential paragraphs; PhET Membrane Channels; optional Neuroscience Online Chapter 1 only through resting-potential intuition. | Neuroscience Online Membrane Potential Laboratory; NCBI Bookshelf resting-potential background; Goldman-Hodgkin-Katz context only if the student asks why the Nernst equation is not the whole story. |
| C | This minibook Chapter 3; OpenStax Anatomy and Physiology 2e 12.5 on communication between neurons; OpenStax Biology 2e 35.2 on synapses, EPSPs, and IPSPs. | Neuroscience Online Chapter 4 and Chapter 6 for mentor examples of chemical synapses and central synaptic transmission. |
| D | This minibook Chapter 4; OpenStax Anatomy and Physiology 2e 12.4 action-potential figure and text; Neuroscience Online Chapter 2 only for Na+ and K+ channel timing. | Hodgkin and Huxley's 1952 conductance model paper; ModelDB squid axon HH example. |
| E | This minibook Chapter 5; local spike raster, rate, ISI, and CV exercises; no extra paper reading required. | Allen electrophysiology traces for authentic firing patterns; spike-train interpretation examples chosen by the mentor. |
| F | This minibook Chapter 6; local HH circuit and HH-intuition notebook. | Allen GLIF model documentation and Teeter et al. 2018; Allen biophysical model documentation; NEURON and NetPyNE pages as tool context. |
| G | This minibook Chapter 7; patch-clamp cartoon, single-channel trace, and coin-flip channel-noise activity. | Hamill et al. 1981 patch-clamp methods paper; ModelDB channel-noise example; selected patch-clamp history background. |
| H | This minibook Chapter 8; capstone notebook, rubric, and final talk template. | Allen Cell Types, DANDI, NWB, and ModelDB as authentic data/model pathways for mentor-guided extensions only. |

The rule is simple: the student reads only what helps her complete the week's chapter tasks. The mentor may read deeper sources to answer questions accurately, choose better examples, and avoid oversimplifying the biology.

Key student-facing anchors include [OpenStax Biology 2e 35.2](https://openstax.org/books/biology-2e/pages/35-2-how-neurons-communicate), [OpenStax Anatomy and Physiology 2e 12.4](https://openstax.org/books/anatomy-and-physiology-2e/pages/12-4-the-action-potential), [OpenStax Anatomy and Physiology 2e 12.5](https://openstax.org/books/anatomy-and-physiology-2e/pages/12-5-communication-between-neurons), [Neuroscience Online Section 1](https://nba.uth.tmc.edu/neuroscience/m/s1/index.htm), [HHMI BioInteractive](https://www.biointeractive.org/), and [PhET Membrane Channels](https://phet.colorado.edu/en/simulations/membrane-channels).

Key mentor-facing anchors include [Hodgkin and Huxley 1952](https://pubmed.ncbi.nlm.nih.gov/12991237/), [Hamill et al. 1981](https://doi.org/10.1007/BF00656997), [Allen GLIF models](https://brain-map.org/our-research/computational-modeling/glif-single-neuron-models), [AllenSDK GLIF documentation](https://alleninstitute.github.io/AllenSDK/glif_models.html), [AllenSDK biophysical model documentation](https://alleninstitute.github.io/AllenSDK/biophysical_models.html), [NEURON](https://www.neuronsimulator.org/), [NetPyNE](https://www.netpyne.org/), [ModelDB HH squid axon example](https://modeldb.science/84649), [ModelDB channel-noise example](https://modeldb.science/127992), [DANDI](https://about.dandiarchive.org/), and [Neurodata Without Borders](https://nwb.org/).

## Curated Data Assets

The student should use curated examples, not open-ended data hunting.

| Asset | File or route | Use |
|---|---|---|
| Synthetic spike-time CSV | `neuro_book/datasets/synthetic_spike_times.csv` | Practice raster, ISI, mean ISI, rate, and CV. |
| Toy SWC morphology file | `neuro_book/datasets/toy_pyramidal_morphology.swc` | See how morphology can be stored as points and branches. |
| Allen example route | `neuro_book/datasets/allen_cell_types_example.md` | Mentor-guided path to a real morphology/ephys example. |
| Action-potential storyboard | `neuro_book/figures/generated/anim_01_action_potential_storyboard.md` | Build or rehearse an animation without producing video. |

The target final presentation is a short scientific explanation for other high-school students: how neuron shape, ions, membranes, channels, and random channel behavior can affect spike timing.
