# Minibook v2 Source Map

The v2 folder preserves the current book while reorganizing it for systematic revision.

| Current source | v2 destination | Purpose |
| --- | --- | --- |
| `neuro_book/intro.md` | `minibook_v2/source/intro.md` | Opening orientation and course overview |
| `neuro_book/chapters/` | `minibook_v2/source/chapters/` | Main eight-chapter textbook narrative |
| `neuro_book/figures/` | `minibook_v2/source/figures/` | Figure specs and generated visuals |
| `neuro_book/figures/generated/anim_01_action_potential_storyboard.md` | `minibook_v2/source/animations/` | Animation/storyboard seed |
| `neuro_book/quizzes/` | `minibook_v2/source/quizzes/` | Weekly quiz banks |
| `neuro_book/rubrics/` | `minibook_v2/source/rubrics/` | Assessment architecture and rubrics |
| `neuro_book/notebooks/` | `minibook_v2/source/code/` | Student notebooks and code activities |
| `neuro_book/datasets/` | `minibook_v2/source/datasets/` | Curated student datasets |
| `neuro_book/appendices/glossary.md` | `minibook_v2/source/glossary/glossary.md` | Cumulative glossary |
| `neuro_book/appendices/math_tools_for_membrane_voltage.md` | `minibook_v2/source/glossary/math_tools_for_membrane_voltage.md` | Front math appendix |
| `neuro_book/appendices/notation_and_units.md` | `minibook_v2/source/glossary/notation_and_units.md` | Notation and units reference |
| `neuro_book/appendices/resource_catalog.md` | `minibook_v2/source/glossary/resource_catalog.md` | Resource catalog |
| `neuro_book/appendices/tiny_code_snippets.md` | `minibook_v2/source/code/tiny_code_snippets.md` | Code appendix |
| `neuro_book/appendices/curated_data_assets.md` | `minibook_v2/source/datasets/curated_data_assets.md` | Data asset notes |
| `neuro_book/audits/` | `minibook_v2/planning/` | QA and planning records |
| `neuro_book/structured/` | `minibook_v2/planning/structured/` | Structured chapter JSON |

Exercises and solutions currently live inside chapter prose. The next revision pass should extract reusable worksheets into `source/exercises/` and the corresponding answer keys into `source/solutions/`.
