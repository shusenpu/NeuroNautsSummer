# QA Fix List

## Safe Fixes Applied

1. Standardized HH-style notation from `I = g(V - E)` to `I = g(V_m - E)` in the revised source and exports.
2. Corrected source chapter glossary links so assembled single-file exports point to the cumulative glossary anchor.
3. Added accessible SVG metadata to generated figures: `role="img"`, `<title>`, and `<desc>`.
4. Added missing graph units to `fig_06_synapse_and_psps.svg`: `Time (ms)` and `V_m (mV)`.
5. Clarified the clamp figure by labeling current traces as relative teaching units and voltage traces in `mV`.
6. Added a note in Chapter 6 explaining that the clamp sketch uses calibrated voltage units but relative current units.
7. Expanded the optional Chapter 6 capacitance worked example so unit conversion and multiplication steps are explicit.
8. Replaced the broken OpenStax A&P overview link with `https://openstax.org/details/books/anatomy-and-physiology-2e`.
9. Replaced `https://www.neuromorpho.org/` with `https://neuromorpho.org/` to avoid the certificate hostname mismatch.
10. Replaced the older Hodgkin-Huxley DOI link that produced access trouble with the stable PubMed record.
11. Regenerated the assembled manuscript and exports:
    - `minibook_v2/source/minibook_master.md`
    - `minibook_v2/exports/minibook_v2.md`
    - `minibook_v2/exports/minibook_v2.html`
    - `minibook_v2/exports/minibook_v2.pdf`
12. Aligned the legacy HTML export in `minibook_v2/exports/from_neuron_shape_to_noisy_spike_trains.html` with the same notation and URL fixes.

## Not Automatically Changed

1. HHMI BioInteractive still returns `403` to automated `curl`, but this appears to be request blocking rather than a bad public URL. The canonical link was kept.
2. The intro readability estimate is higher than some chapters because it contains tables and source names. It was not rewritten because the student-facing chapters meet the grade 9-10 target.
3. Repeated vocabulary boxes were kept. They are useful retrieval scaffolds, not accidental duplicate glossary entries.
4. Quiz wording was not broadly rewritten. Structural checks passed, and broad prose changes could accidentally alter intended answer keys.

## Final Verification Snapshot

- Missing local links: 0
- Empty Markdown image alt text: 0
- HTML images missing `alt`: 0
- Generated SVGs missing title/description metadata: 0
- Master image references: 39
- Missing master image files: 0
- Insert-map figures not in master manuscript: 0
- Quiz/key counts: 8 quiz items and 8 keyed answers for each chapter
- Exercise/solution counts: 9 prompts and 9 solutions for each chapter
- PDF: valid `%PDF-1.4`, EOF marker present, 4,145,475 bytes
