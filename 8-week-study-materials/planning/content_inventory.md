# Content Inventory

## Detected Source Files

Primary editable manuscript: `minibook_v2/source/intro.md`, `minibook_v2/source/_toc.yml`, and the eight files in `minibook_v2/source/chapters/`. The original mirrored source remains in `neuro_book/` and should be treated as a legacy duplicate unless a later diff proves otherwise. Supporting source includes `minibook_v2/source/glossary/`, `source/rubrics/`, `source/quizzes/`, `source/code/`, `source/datasets/`, `source/figures/`, and `source/animations/`. Exports are present in `minibook_v2/exports/` and `outputs/from-neuron-shape-to-noisy-spike-trains/`. Earlier HTML packets and slide decks exist under `outputs/student-neuro-biophysics-notes/`, `Brain_Code_*`, `website_publish/`, and `colab_notebooks/`. No `.qmd`, `.tex`, or docx-converted Markdown files were found inside this workspace.

## Current Chapter/Week Titles

1. Week A / Chapter 1. Neurons as Signaling Cells
2. Week B / Chapter 2. Ions, Gradients, and Why Rest Is Negative
3. Week C / Chapter 3. Graded Signals and Threshold
4. Week D / Chapter 4. How Spikes Begin and Travel
5. Week E / Chapter 5. Spike Trains and Neural Information
6. Week F / Chapter 6. Circuits and Hodgkin-Huxley Intuition
7. Week G / Chapter 7. From Single Channels to Timing Variability
8. Week H / Chapter 8. Evidence, Explanation, and Communication

## Repeated Elements Already Present

Each chapter already repeats a strong instructional pattern: opening question, learning goals, week snapshot, weekly lesson spine, independent study scaffold, prerequisites, vocabulary, misconception box, visual opener, core concept lesson, graph-reading block, worked examples, quick checks, calculation block, mini-lab or code, interactive exercise, retrieval quiz and reflection, summary, homework, answer key, stretch box, mentor note, glossary additions, and source notes. The book also has a cumulative glossary, math and notation appendices, figure specifications, generated figures, weekly quiz JSON, assessment rubrics, curated datasets, student notebooks, a final project chapter, and exported HTML/PDF versions.

## Missing Elements Needed For Textbook-Style Version

The next textbook pass should extract chapter-embedded exercises into standalone worksheets under `source/exercises/` and mentor answer keys under `source/solutions/`. Figure metadata should be normalized so every major figure has caption, alt text, source note, and “what this is / is not” guidance in one predictable location. The main manuscript needs stricter separation between student-facing prose and mentor-only notes. Several resources are present as files but not yet fully integrated into a print-ready textbook workflow: notebooks, quizzes, datasets, and animation storyboards need consistent cross-links from chapters. A lightweight editorial style sheet would also help enforce terminology, notation, and voice.

## Structural Diagnosis

The manuscript has matured beyond an outline: it is already a coherent eight-week, no-calculus textbook draft with recurring pedagogy and substantial visual support. The main structural weakness is not missing content volume, but source organization and reuse. Exercises, solutions, figure notes, notebook activities, and assessment materials exist, yet some are embedded inside chapter prose while others live as parallel JSON or notebook artifacts. The v2 folder is the right editorial move: it separates manuscript, assets, assessment, code, data, planning, and exports. The next revision should reduce duplication between `neuro_book/` and `minibook_v2/`, designate one canonical source, and make each chapter’s learning loop easier to audit.
