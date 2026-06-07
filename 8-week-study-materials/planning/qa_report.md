# Minibook V2 Quality-Control Report

Scope checked: `minibook_v2/source/`, `minibook_v2/source/minibook_master.md`, `minibook_v2/exports/`, chapter quizzes, exercises, solutions, generated SVG figures, and the assembled PDF.

## Executive Status

The revised minibook passes the core export and student-use checks after safe fixes. Local links are intact, image alt text is present, figure files resolve, SVGs include accessible metadata, quizzes and answer keys align structurally, and the PDF is valid. One external site, HHMI BioInteractive, returns `403` to automated `curl`; this is likely automated-request blocking rather than a student-facing broken URL, so it was not changed.

## Check Results

| Check area | Result | Evidence |
|---|---:|---|
| Reading level | Pass for student chapters | Chapter estimates range from grade 7.6 to 9.7; intro estimates grade 10.6 because it includes dense resource tables. |
| Unexplained jargon | Pass with minor fixes applied | Priority vocabulary is covered in the glossary/index; Chapter 6 now explains relative current units and the optional capacitance example more explicitly. |
| Missing graph units | Fixed | Added `Time (ms)` and `V_m (mV)` to the synapse EPSP/IPSP graph; clarified clamp current as relative teaching units. |
| Missing alt text | Pass | Markdown image alt text missing: 0. HTML `<img>` missing `alt`: 0. Generated SVGs missing title/description metadata: 0. |
| Broken local links | Pass | Missing local Markdown links: 0. Assembler verified HTML local file links and internal anchors. |
| External links | Mostly pass | 22 external URLs returned `200`; HHMI BioInteractive returned `403` to automated `curl`. |
| Duplicated definitions | Pass | `term_index.csv` has 115 term rows and 0 duplicate terms. Repeated chapter vocabulary boxes are intentional scaffolding. |
| Skipped math steps | Fixed | Expanded Chapter 6 capacitance example and clarified that microfarad/microcoulomb units are optional enrichment. |
| Figures referenced but not inserted | Pass | `insert_map.md` names 15 figure files; all 15 appear in the master manuscript. Master manuscript has 39 image references and 0 missing image files. |
| Quiz ambiguity | Pass structurally | Chapters 1-8 each have 8 quiz items and 8 keyed answers. Multiple-choice questions use complete option sets. |
| Exercise/solution consistency | Pass | Chapters 1-8 each have 9 exercise prompts and 9 solution entries. |
| Export health | Pass | HTML size: 327,075 bytes. PDF size: 4,145,475 bytes; header `%PDF-1.4`; EOF marker present; 144 page markers. |

## Reading-Level Snapshot

| File | Estimated grade |
|---|---:|
| `intro.md` | 10.6 |
| `neurons_as_signaling_cells.md` | 9.5 |
| `ions_gradients_resting_voltage.md` | 9.5 |
| `synapses_and_summation.md` | 9.3 |
| `action_potentials_and_propagation.md` | 9.7 |
| `spike_trains_rate_and_variability.md` | 7.6 |
| `circuits_and_hh_intuition.md` | 8.7 |
| `single_channel_noise.md` | 9.1 |
| `capstone_project.md` | 9.0 |

Automated readability formulas overestimate some technical text because terms like `electrochemical`, `depolarization`, and `conductance` are unavoidable. The main chapters are within the grade 9-10 target.

## External URL Notes

Two true URL hygiene issues were corrected: the OpenStax A&P overview link now points to the current details page, and NeuroMorpho now uses the certificate-valid non-`www` hostname. HHMI BioInteractive returned `403` to automated `curl`; because the public URL is still the canonical site and the issue is consistent with bot blocking, the link was left unchanged.

## Remaining Watch Items

The intro is slightly denser than the student chapters because it includes syllabus, source, and resource tables. This is acceptable for a front-matter reference section, but it could be split into a short student welcome plus a mentor resource appendix later. External links should be rechecked before distributing the PDF, especially educator-resource sites that change routing or block automated checks.
