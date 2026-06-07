# Resource Catalog

This catalog prioritizes resources that are official, widely used, or both. When reuse terms are resource-specific or not obvious from a stable landing page, the catalog says so instead of guessing. For this minibook, the safest default is to link to external resources, use locally generated teaching figures, and avoid redistributing third-party assets unless the license is clear.

| Resource | URL | Purpose in the minibook | License or access terms | HS suitability | Evidence |
|---|---|---|---|---|---|
| OpenStax Anatomy and Physiology 2e | <https://openstax.org/details/books/anatomy-and-physiology-2e> | Core textbook source for membrane potential, action potentials, graded potentials, and synapses. | OpenStax A&P 2e preface states CC BY-NC-SA 4.0 for the textbook pages. Use attribution and noncommercial/share-alike care for adapted material. | Excellent for core reading and adapted concept figures. | Official OpenStax book details page and action-potential chapter. |
| OpenStax Biology 2e, Section 35.2 | <https://openstax.org/books/biology-2e/pages/35-2-how-neurons-communicate> | Core conceptual support for neuron communication, synapses, EPSPs/IPSPs, and action potentials. | OpenStax open textbook; check the specific book page/license before adapting figures. | Excellent for core reading. | Official OpenStax Biology 2e section. |
| Neuroscience Online | <https://nba.uth.tmc.edu/neuroscience/> | Open-access background textbook for mentor curation and occasional student reading. | Open-access electronic resource; the landing page does not clearly state a Creative Commons license, so link rather than redistribute. | Good as mentor reference; selected excerpts only for student reading. | UTHealth/McGovern Medical School resource page. |
| HHMI BioInteractive | <https://www.biointeractive.org/> | Videos, animations, interactives, activities, and assessments for biology teaching. | HHMI resources are free for educational use, but redistribution/adaptation depends on the specific resource terms. Link to resources and check each page before embedding or modifying. | Strong for visuals and enrichment. | HHMI terms of use and BioInteractive educator guidance. |
| PhET Membrane Channels | <https://phet.colorado.edu/en/simulations/membrane-channels> | Interactive for diffusion, membrane transport, and channel intuition. | PhET licensing page says regular HTML simulation files are CC BY-NC 4.0; check the current simulation/license page before redistributing files or screenshots. | Very good for intuition-first lesson blocks. | Official PhET licensing page. |
| Allen Cell Types Database | <https://celltypes.brain-map.org/> | Real morphology, electrophysiology, downloadable models, and API access. | Allen terms emphasize noncommercial use of content unless otherwise stated or agreed in writing. Use links and small mentor-guided examples; check current terms before redistribution. | Excellent for "real neuron" and "real data" chapters. | Allen Cell Types overview, AllenSDK page, and Allen Institute terms. |
| NEURON Simulator | <https://www.neuronsimulator.org/> | Authoritative simulator for single neurons and networks; supports Python and GUI workflows. | Open-source project; official GitHub organization identifies NEURON-related repositories, with license details in repository/license files. | Best for mentor and advanced student; use lightly in the high-school core. | Official NEURON site/GitHub repository and documentation route. |
| NetPyNE | <https://www.netpyne.org/> | Higher-level Python framework on top of NEURON; useful for structured multiscale examples. | Official site describes NetPyNE as open source and links to GitHub. Check the repository license before redistributing code. | Better for mentor-facing authored examples than for first-time student use. | Official NetPyNE about and documentation pages. |
| ModelDB | <https://modeldb.science/> | Repository of neuroscience models by simulator, topic, cell type, current, and paper. | Site has terms of use; individual models may vary by source. Link to models and check terms before reuse. | Excellent mentor resource for vetted examples and authentic links. | ModelDB help and terms guidance. |
| Hodgkin and Huxley 1952 conductance model paper | <https://pubmed.ncbi.nlm.nih.gov/12991237/> | Mentor background for conductance, reversal potentials, voltage clamp, and why the HH circuit in Chapter 6 matters. | Classic journal article; link to the PubMed record or journal page rather than redistributing a scanned PDF. | Mentor only. Too mathematical for the required high-school path. | PubMed record with DOI and Journal of Physiology citation; also represented in ModelDB's HH squid axon example. |
| Hamill et al. 1981 patch-clamp paper | <https://doi.org/10.1007/BF00656997> | Mentor background for why single-channel recordings changed neuroscience and how patch clamp made random channel openings visible. | Springer journal article; use citation and link rather than redistributing the article. | Mentor only. Use its historical idea, not the full methods paper, with the student. | Springer record for the patch-clamp methods article. |
| Allen GLIF model documentation | <https://alleninstitute.github.io/AllenSDK/glif_models.html> | Mentor background for simplified point-neuron models that can reproduce spike timing from measured cells. | Official AllenSDK documentation; check repository license before reusing code. | Mentor and advanced extension only. | AllenSDK GLIF documentation and Allen GLIF model page. |
| Allen biophysical model documentation | <https://alleninstitute.github.io/AllenSDK/biophysical_models.html> | Mentor background for morphology-linked conductance models run in NEURON. | Official AllenSDK documentation; downloaded models and scripts should follow Allen terms and repository licenses. | Mentor only, unless reduced to one screenshot or story. | AllenSDK biophysical model documentation and Allen Cell Types overview. |
| ModelDB HH squid axon example | <https://modeldb.science/84649> | Mentor example connecting the classic HH paper to runnable model code. | ModelDB terms apply; model-specific code and linked repositories may have their own terms. | Mentor only; use the idea to improve Chapter 6 explanations. | ModelDB model page for Squid axon (Hodgkin, Huxley 1952). |
| ModelDB channel-noise example | <https://modeldb.science/127992> | Mentor example connecting stochastic channel noise to conductance-based neuron models. | ModelDB terms apply; model-specific code and linked repositories may have their own terms. | Mentor only; use to inform Chapter 7 and the capstone, not as required reading. | ModelDB model page for Linaro et al. channel-noise simulation. |
| DANDI Archive | <https://dandiarchive.org/> | Open neurophysiology datasets for optional advanced capstone paths. | Public BRAIN Initiative-supported archive; datasets may include their own metadata and terms. Link rather than bundling large datasets. | Too advanced for core high-school path; excellent for extensions. | DANDI and NWB archive descriptions. |
| Neurodata Without Borders | <https://nwb.org/> | Standard for neurophysiology and behavioral data; useful for an advanced appendix. | Open standard and software ecosystem for neurophysiology data. | Advanced extension only. | Official NWB overview and archive pages. |
| NeuroMorpho | <https://neuromorpho.org/> | Downloadable neuron reconstructions in SWC format for morphology labs. | NeuroMorpho terms state CC BY 4.0 and require citation of original papers, NeuroMorpho.Org, and the current repository citation. Programmatic access must follow their API/direct-link rules. | Very good for morphology-focused enrichment. | Official NeuroMorpho terms of use. |

## Reading Tiers For This Course

### Student Core

The student should not be asked to chase every source. Required reading stays narrow:

1. This minibook narrative, figures, worked examples, homework, and notebooks.
2. OpenStax membrane, action-potential, graded-potential, and synapse sections.
3. Selected Neuroscience Online pages only when the minibook calls for them: resting potential, ionic mechanisms, propagation, and synaptic transmission.
4. Selected HHMI or PhET interactives for intuition before equations.

### Mentor Background

Mentor background is different from student reading. These sources should shape the mentor's explanations, examples, and answers, but they should not be assigned in full:

| Source | Best mentor use | Do not assign in full because |
|---|---|---|
| Hodgkin and Huxley 1952 conductance model paper | Clarify why Chapter 6 uses conductance, reversal potential, and a membrane-circuit analogy. | It assumes advanced mathematics, experimental electrophysiology, and a long technical paper format. |
| Hamill et al. 1981 patch-clamp paper | Explain why patch clamp made single-channel all-or-none openings experimentally visible. | It is a methods paper, not a beginner teaching text. |
| Allen GLIF documentation and Teeter et al. 2018 | Connect simple threshold models to real electrophysiology data and spike-time prediction. | The model-fitting details exceed the no-calculus promise. |
| Allen biophysical model documentation | Show what a full morphology-linked conductance model looks like after the student understands the cartoon circuit. | It requires NEURON, model files, and advanced computational setup. |
| ModelDB examples | Choose one trusted runnable model when the mentor wants authenticity. | Open browsing can overwhelm the student and individual model quality/terms vary. |
| DANDI and NWB | Explain where modern neurophysiology datasets live and why data standards matter. | They are data infrastructure, not a beginner path through ions and spikes. |

The mentor's job is to translate these background sources into one clear figure, one causal sentence, or one small calculation at a time.

## Practical Reuse Rule For This Book

1. Link to external resources whenever possible.
2. Use locally generated diagrams for the minibook's core explanations.
3. Treat real datasets as mentor-guided examples, not open-ended student browsing.
4. Before copying a third-party figure, video still, model file, or interactive into the book, check the exact page-level license and attribution requirements.
5. Label every figure as real data, cartoon, simulation, storyboard, or conceptual diagram.
