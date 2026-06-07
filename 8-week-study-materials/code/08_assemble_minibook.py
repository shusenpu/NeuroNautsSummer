"""
Build the export-ready minibook manuscript.

This script combines the Jupyter Book source chapters and appendices into one
master Markdown manuscript, writes an export Markdown copy, renders a mobile-
readable HTML file, and checks local links before PDF printing.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote

import markdown
from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
EXPORTS = ROOT / "exports"


@dataclass(frozen=True)
class Section:
    title: str
    anchor: str
    path: Path | None = None
    body: str | None = None
    base_dir: Path | None = None
    demote: int = 0
    strip_first_heading: bool = False


CHAPTERS = [
    Section(
        "Chapter 1. Neurons as Signaling Cells",
        "chapter-1-neurons-as-signaling-cells",
        SOURCE / "chapters" / "neurons_as_signaling_cells.md",
    ),
    Section(
        "Chapter 2. Ions, Gradients, and Resting Voltage",
        "chapter-2-ions-gradients-and-resting-voltage",
        SOURCE / "chapters" / "ions_gradients_resting_voltage.md",
    ),
    Section(
        "Chapter 3. Synapses, Graded Signals, and Summation",
        "chapter-3-synapses-graded-signals-and-summation",
        SOURCE / "chapters" / "synapses_and_summation.md",
    ),
    Section(
        "Chapter 4. Action Potentials and Propagation",
        "chapter-4-action-potentials-and-propagation",
        SOURCE / "chapters" / "action_potentials_and_propagation.md",
    ),
    Section(
        "Chapter 5. Spike Trains, Rate, and Variability",
        "chapter-5-spike-trains-rate-and-variability",
        SOURCE / "chapters" / "spike_trains_rate_and_variability.md",
    ),
    Section(
        "Chapter 6. Circuits and Hodgkin-Huxley Intuition",
        "chapter-6-circuits-and-hodgkin-huxley-intuition",
        SOURCE / "chapters" / "circuits_and_hh_intuition.md",
    ),
    Section(
        "Chapter 7. Single-Channel Noise and Spike-Time Variability",
        "chapter-7-single-channel-noise-and-spike-time-variability",
        SOURCE / "chapters" / "single_channel_noise.md",
    ),
    Section(
        "Chapter 8. Capstone Project and Final Presentation",
        "chapter-8-capstone-project-and-final-presentation",
        SOURCE / "chapters" / "capstone_project.md",
    ),
]


LOCAL_LINK_PATTERN = re.compile(r"(!?)\[([^\]]+)\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^(#{1,6})(\s+)", re.MULTILINE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def strip_first_heading(text: str) -> str:
    lines = text.splitlines()
    if lines and lines[0].startswith("# "):
        return "\n".join(lines[1:]).lstrip() + "\n"
    return text


def demote_headings(text: str, levels: int) -> str:
    if levels <= 0:
        return text

    def repl(match: re.Match[str]) -> str:
        hashes = match.group(1)
        return "#" * min(6, len(hashes) + levels) + match.group(2)

    return HEADING_PATTERN.sub(repl, text)


def normalize_nested_choice_lists(text: str) -> str:
    """Indent multiple-choice options enough for Python-Markdown nested lists."""
    fixed_lines: list[str] = []
    for line in text.splitlines():
        if re.match(r"^ {3}- [A-D]\.", line):
            fixed_lines.append(" " + line)
        else:
            fixed_lines.append(line)
    return "\n".join(fixed_lines) + "\n"


def clean_glossary_for_book(text: str) -> str:
    """Remove editor-facing link-plan directions from the student export."""
    lines = text.splitlines()
    cleaned: list[str] = []
    skipping = False
    for line in lines:
        if line.strip() == "## How To Link Terms In Chapters":
            skipping = True
            continue
        if skipping and line.strip() == "## Terms":
            skipping = False
            continue
        if not skipping:
            cleaned.append(line)
    return "\n".join(cleaned).strip() + "\n"


def split_url_fragment(url: str) -> tuple[str, str]:
    if "#" in url:
        path, fragment = url.split("#", 1)
        return path, "#" + fragment
    return url, ""


def is_external(url: str) -> bool:
    lower = url.lower()
    return lower.startswith(("http://", "https://", "mailto:", "doi:", "tel:"))


def rewrite_links(text: str, base_dir: Path, target_dir: Path) -> str:
    text = text.replace("../appendices/glossary.md", "#cumulative-glossary")
    text = text.replace("../glossary/glossary.md", "#cumulative-glossary")

    def repl(match: re.Match[str]) -> str:
        bang, label, url = match.groups()
        url = url.strip()
        if is_external(url) or url.startswith("#"):
            return match.group(0)

        path_part, fragment = split_url_fragment(url)
        if not path_part:
            return f"{bang}[{label}]({fragment})"

        raw_path = unquote(path_part)
        absolute = (base_dir / raw_path).resolve()
        relative = os.path.relpath(absolute, target_dir)
        relative = relative.replace(os.sep, "/")
        return f"{bang}[{label}]({relative}{fragment})"

    return LOCAL_LINK_PATTERN.sub(repl, text)


def figure_md(alt: str, caption: str, source_path: Path, target_dir: Path) -> str:
    rel = os.path.relpath(source_path.resolve(), target_dir).replace(os.sep, "/")
    return f"\n![{alt}]({rel})\n\n*{caption}*\n"


def add_insert_map_supplements(text: str, section_path: Path, target_dir: Path) -> str:
    """Ensure the single-file manuscript includes every figure named by insert_map.md."""
    name = section_path.name
    if name == "action_potentials_and_propagation.md" and "anim_01_action_potential_storyboard.svg" not in text:
        supplement = figure_md(
            "Storyboard frames showing action-potential phases and matching channel states.",
            "Action-potential storyboard frames connect each phase of the voltage trace to Na+ and K+ channel behavior.",
            ROOT / "figures" / "anim_01_action_potential_storyboard.svg",
            target_dir,
        )
        text = text.replace(
            "[Action-potential storyboard]",
            supplement + "\n[Action-potential storyboard]",
            1,
        )

    if name == "spike_trains_rate_and_variability.md" and "isi_histogram_cv_panel.svg" not in text:
        supplement = figure_md(
            "ISI histogram and CV panel comparing interval variability.",
            "ISI histograms and CV summarize spike-timing regularity after the raster has been read.",
            ROOT / "figures" / "isi_histogram_cv_panel.svg",
            target_dir,
        )
        marker = "*ISI is measured between consecutive threshold crossings.*"
        text = text.replace(marker, supplement + "\n" + marker, 1)

    if name == "single_channel_noise.md" and "channel_state_diagram.svg" not in text:
        supplement = figure_md(
            "Channel state diagram showing transitions between closed and open states.",
            "A channel-state diagram is a compact map of possible closed and open states.",
            ROOT / "figures" / "channel_state_diagram.svg",
            target_dir,
        )
        marker = "*A simplified K+ channel state diagram prepares the student for stochastic channel models.*"
        text = text.replace(marker, supplement + "\n" + marker, 1)

    return text


def section_text(section: Section, target_dir: Path) -> str:
    if section.path is not None:
        text = read_text(section.path)
        base_dir = section.path.parent
    else:
        text = section.body or ""
        base_dir = section.base_dir or ROOT

    if section.strip_first_heading:
        text = strip_first_heading(text)
    text = demote_headings(text, section.demote)
    text = rewrite_links(text, base_dir, target_dir)
    if section.path is not None:
        text = add_insert_map_supplements(text, section.path, target_dir)
    return f'\n<a id="{section.anchor}"></a>\n\n{text.strip()}\n'


def build_quiz_appendix(target_dir: Path) -> str:
    chunks = ["# Quiz Appendix\n"]
    for idx in range(1, 9):
        quiz = read_text(ROOT / "quizzes" / f"ch{idx:02d}_quiz.md")
        key = read_text(ROOT / "quizzes" / f"ch{idx:02d}_quiz_key.md")
        chunks.append(normalize_nested_choice_lists(demote_headings(quiz, 1)))
        chunks.append("\n")
        chunks.append(demote_headings(key, 2))
        chunks.append("\n")
    return rewrite_links("\n".join(chunks), ROOT / "quizzes", target_dir)


def build_exercise_appendix(target_dir: Path) -> str:
    chunks = ["# Exercise Appendix\n"]
    for idx in range(1, 9):
        text = read_text(ROOT / "exercises" / f"ch{idx:02d}_exercises.md")
        chunks.append(demote_headings(text, 1))
        chunks.append("\n")
    return rewrite_links("\n".join(chunks), ROOT / "exercises", target_dir)


def build_solution_appendix(target_dir: Path) -> str:
    chunks = ["# Solution Appendix\n"]
    for idx in range(1, 9):
        text = read_text(ROOT / "solutions" / f"ch{idx:02d}_solutions.md")
        chunks.append(demote_headings(text, 1))
        chunks.append("\n")
    return rewrite_links("\n".join(chunks), ROOT / "solutions", target_dir)


def toc_for(sections: list[Section]) -> str:
    lines = ["# Table of Contents\n"]
    for section in sections:
        lines.append(f"- [{section.title}](#{section.anchor})")
    return "\n".join(lines) + "\n"


def all_sections(target_dir: Path) -> list[Section]:
    intro = Section(
        "Course Overview",
        "course-overview",
        SOURCE / "intro.md",
    )
    math = Section(
        "Front Appendix. Math Tools for Membrane Voltage",
        "math-tools-for-membrane-voltage",
        SOURCE / "glossary" / "math_tools_for_membrane_voltage.md",
    )
    notation = Section(
        "Front Appendix. Notation and Units",
        "notation-and-units",
        SOURCE / "glossary" / "notation_and_units.md",
    )
    lab_sheets = Section(
        "Lab Sheet Appendix",
        "lab-sheet-appendix",
        SOURCE / "lab_sheets.md",
    )
    final_rubric = Section(
        "Final Project Rubric",
        "final-project-rubric",
        ROOT / "rubrics" / "final_project_rubric.md",
    )
    quiz = Section(
        "Quiz Appendix",
        "quiz-appendix",
        body=build_quiz_appendix(target_dir),
        base_dir=target_dir,
    )
    exercises = Section(
        "Exercise Appendix",
        "exercise-appendix",
        body=build_exercise_appendix(target_dir),
        base_dir=target_dir,
    )
    solutions = Section(
        "Solution Appendix",
        "solution-appendix",
        body=build_solution_appendix(target_dir),
        base_dir=target_dir,
    )
    glossary = Section(
        "Cumulative Glossary",
        "cumulative-glossary",
        body=clean_glossary_for_book(read_text(ROOT / "glossary" / "glossary.md")),
        base_dir=ROOT / "glossary",
    )
    references = Section(
        "References and Source Notes",
        "references-and-source-notes",
        SOURCE / "glossary" / "resource_catalog.md",
    )
    return [
        intro,
        math,
        notation,
        *CHAPTERS,
        lab_sheets,
        final_rubric,
        quiz,
        exercises,
        solutions,
        glossary,
        references,
    ]


def build_markdown(target_dir: Path) -> str:
    sections = all_sections(target_dir)
    title = """# From Neuron Shape to Noisy Spike Trains

"""
    parts = [title, toc_for(sections)]
    for section in sections:
        parts.append(section_text(section, target_dir))
    return "\n\n---\n\n".join(parts).strip() + "\n"


def render_html(markdown_text: str) -> str:
    body = markdown.markdown(
        markdown_text,
        extensions=["extra", "toc", "tables", "fenced_code", "attr_list", "sane_lists", "md_in_html"],
        output_format="html5",
    )
    soup = BeautifulSoup(body, "html.parser")
    for table in list(soup.find_all("table")):
        wrapper = soup.new_tag("div", attrs={"class": "table-wrap"})
        table.wrap(wrapper)
    for paragraph in soup.find_all("p"):
        if paragraph.find("img", recursive=False):
            paragraph["class"] = (paragraph.get("class", []) + ["figure-image"])

    h1s = soup.find_all("h1")
    if h1s:
        h1s[0]["class"] = (h1s[0].get("class", []) + ["book-title-heading"])
        next_node = h1s[0].find_next_sibling()
        if next_node and getattr(next_node, "name", None) == "hr":
            next_node["class"] = (next_node.get("class", []) + ["book-title-rule"])

    appendix_titles = {
        "Lab Sheet Appendix",
        "Final Project Rubric",
        "Quiz Appendix",
        "Exercise Appendix",
        "Solution Appendix",
        "Cumulative Glossary",
        "References and Source Notes",
    }
    for heading in h1s:
        text = heading.get_text(" ", strip=True)
        classes = heading.get("class", [])
        if text == "Table of Contents":
            classes.append("toc-heading")
        elif text == "Course Overview" or text.startswith("Front Appendix"):
            classes.append("front-heading")
        elif text.startswith("Week ") or text.startswith("Chapter "):
            classes.append("chapter-heading")
        elif text in appendix_titles:
            classes.append("appendix-heading")
        heading["class"] = classes

    css = """
    :root {
      color-scheme: light;
      --ink: #111827;
      --muted: #4b5563;
      --line: #d1d5db;
      --soft: #f8fafc;
      --accent: #0f766e;
      --callout: #fff7ed;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
      color: var(--ink);
      background: #eef2f7;
      line-height: 1.65;
      font-size: 16px;
    }
    main {
      width: min(100%, 980px);
      margin: 0 auto;
      background: white;
      padding: 44px 58px 72px;
      box-shadow: 0 12px 40px rgba(15, 23, 42, 0.14);
    }
    h1, h2, h3, h4 {
      line-height: 1.22;
      color: #0f172a;
      margin: 1.35em 0 0.45em;
      letter-spacing: 0;
    }
    h1 {
      font-size: 2.05rem;
      border-bottom: 3px solid var(--accent);
      padding-bottom: 0.35rem;
    }
    h2 { font-size: 1.45rem; }
    h3 { font-size: 1.15rem; }
    p, li { max-width: 78ch; }
    a { color: #0f766e; text-decoration-thickness: 0.08em; }
    img {
      display: block;
      max-width: 100%;
      height: auto;
      margin: 1rem auto;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: white;
    }
    em { color: #334155; }
    blockquote {
      margin: 1rem 0;
      padding: 0.85rem 1rem;
      border-left: 4px solid var(--accent);
      background: #ecfeff;
      border-radius: 0 6px 6px 0;
    }
    code {
      background: #f1f5f9;
      padding: 0.1rem 0.25rem;
      border-radius: 4px;
      font-size: 0.95em;
    }
    pre {
      overflow-x: auto;
      padding: 1rem;
      background: #0f172a;
      color: #e5e7eb;
      border-radius: 8px;
    }
    pre code { background: transparent; padding: 0; color: inherit; }
    .table-wrap {
      width: 100%;
      overflow-x: auto;
      margin: 1rem 0 1.25rem;
      border: 1px solid var(--line);
      border-radius: 8px;
    }
    table {
      border-collapse: collapse;
      width: 100%;
      min-width: 640px;
      font-size: 0.92rem;
    }
    th, td {
      border: 1px solid var(--line);
      padding: 0.55rem 0.65rem;
      vertical-align: top;
    }
    th { background: var(--soft); text-align: left; }
    hr { border: 0; border-top: 1px solid var(--line); margin: 2.3rem 0; }
    ul, ol { padding-left: 1.35rem; }
    .book-cover { display: none; }
    @media (max-width: 720px) {
      body { background: white; font-size: 16px; }
      main { padding: 22px 18px 44px; box-shadow: none; }
      h1 { font-size: 1.65rem; }
      h2 { font-size: 1.25rem; }
      table { min-width: 560px; }
    }
    @media print {
      @page {
        size: Letter;
        margin: 0.65in;
      }
      html, body { background: white; }
      body {
        color: #111827;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
        font-size: 10.6pt;
        line-height: 1.5;
      }
      main { width: 100%; padding: 0; box-shadow: none; }
      .book-cover {
        display: none !important;
      }
      .cover-kicker {
        color: #0f766e;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
        font-size: 11pt;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }
      .book-cover h1 {
        max-width: 8.5in;
        margin: 0.25in 0 0.18in;
        padding: 0;
        border: 0;
        color: #0f172a;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 34pt;
        line-height: 1.08;
      }
      .cover-subtitle {
        max-width: 6.4in;
        color: #334155;
        font-size: 14pt;
        line-height: 1.45;
      }
      .cover-line {
        width: 2.2in;
        height: 2pt;
        margin: 0.35in 0;
        background: #0f766e;
      }
      .cover-meta {
        color: #475569;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
        font-size: 10.5pt;
      }
      h1, h2, h3, h4 {
        color: #0f172a;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
        break-after: avoid;
        page-break-after: avoid;
      }
      h1 {
        margin: 0.28in 0 0.14in;
        padding: 0 0 0.08in;
        border-bottom: 1.5pt solid #0f766e;
        font-size: 21pt;
        line-height: 1.16;
      }
      .front-heading,
      .chapter-heading,
      .appendix-heading {
        page-break-before: auto;
        break-before: auto;
      }
      .toc-heading {
        page-break-before: avoid;
        break-before: avoid;
      }
      h2 {
        margin-top: 0.22in;
        font-size: 14.5pt;
      }
      h3 {
        margin-top: 0.16in;
        font-size: 12.2pt;
      }
      h4 {
        margin-top: 0.12in;
        font-size: 10.8pt;
      }
      p, li {
        max-width: none;
        orphans: 3;
        widows: 3;
      }
      p {
        margin: 0 0 0.08in;
      }
      ul, ol {
        margin-top: 0.04in;
        margin-bottom: 0.12in;
      }
      li > p:first-child {
        margin-bottom: 0.03in;
      }
      li > ul,
      li > ol {
        margin-top: 0.02in;
        margin-bottom: 0.08in;
      }
      ol > li,
      ul > li {
        margin-bottom: 0.035in;
      }
      a { color: black; text-decoration: none; }
      img {
        max-width: 100%;
        max-height: 6.45in;
        margin: 0.12in auto 0.1in;
        border: 0.75pt solid #cbd5e1;
        border-radius: 0;
        page-break-inside: avoid;
        break-inside: avoid;
      }
      .figure-image {
        margin: 0.08in 0 0.05in;
        page-break-inside: avoid;
        break-inside: avoid;
      }
      blockquote {
        margin: 0.12in 0;
        padding: 0.11in 0.14in;
        background: #f0fdfa;
        border-left: 3pt solid #0f766e;
        border-radius: 0;
        page-break-inside: avoid;
        break-inside: avoid;
      }
      pre {
        white-space: pre-wrap;
        page-break-inside: avoid;
        break-inside: avoid;
      }
      .table-wrap {
        overflow: visible;
        margin: 0.1in 0 0.16in;
        border: 0.75pt solid #cbd5e1;
        border-radius: 0;
        page-break-inside: auto;
        break-inside: auto;
      }
      table {
        min-width: 0;
        font-size: 8.8pt;
        line-height: 1.28;
        page-break-inside: auto;
        break-inside: auto;
      }
      thead {
        display: table-header-group;
      }
      tr {
        page-break-inside: avoid;
        break-inside: avoid;
      }
      th, td {
        padding: 0.055in 0.07in;
      }
      hr {
        margin: 0.2in 0;
        page-break-after: auto;
        break-after: auto;
      }
    }
    """
    cover = """
<section class="book-cover" aria-label="Book cover">
  <div class="cover-kicker">NeuroNauts Summer Study Materials</div>
  <h1>From Neuron Shape to Noisy Spike Trains</h1>
  <p class="cover-subtitle">An eight-week neuroscience study guide with chapters, figures, worked examples, labs, quizzes, code, and a final presentation project.</p>
  <div class="cover-line" aria-hidden="true"></div>
  <p class="cover-meta">Designed for a high-school student learning neuron biophysics from the beginning.</p>
</section>
"""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>From Neuron Shape to Noisy Spike Trains</title>
  <style>{css}</style>
</head>
<body>
{cover}
<main>
{soup}
</main>
</body>
</html>
"""


def verify_html_links(html_path: Path) -> tuple[list[str], list[str]]:
    soup = BeautifulSoup(read_text(html_path), "html.parser")
    ids = {tag.get("id") for tag in soup.find_all(attrs={"id": True})}
    ids.discard(None)
    missing_files: list[str] = []
    missing_anchors: list[str] = []

    for img in soup.find_all("img"):
        src = img.get("src", "")
        if src and not is_external(src):
            path_part, _ = split_url_fragment(src)
            if not (html_path.parent / unquote(path_part)).resolve().exists():
                missing_files.append(src)

    for link in soup.find_all("a"):
        href = link.get("href", "")
        if not href or is_external(href):
            continue
        path_part, fragment = split_url_fragment(href)
        if path_part:
            target = (html_path.parent / unquote(path_part)).resolve()
            if not target.exists():
                missing_files.append(href)
        if fragment and (not path_part or Path(path_part).name == html_path.name):
            anchor = fragment[1:]
            if anchor not in ids:
                missing_anchors.append(href)

    return sorted(set(missing_files)), sorted(set(missing_anchors))


def main() -> None:
    EXPORTS.mkdir(parents=True, exist_ok=True)

    master_md = build_markdown(SOURCE)
    export_md = build_markdown(EXPORTS)

    master_path = SOURCE / "minibook_master.md"
    export_md_path = EXPORTS / "minibook.md"
    html_path = EXPORTS / "minibook.html"

    master_path.write_text(master_md, encoding="utf-8")
    export_md_path.write_text(export_md, encoding="utf-8")
    html_path.write_text(render_html(export_md), encoding="utf-8")

    missing_files, missing_anchors = verify_html_links(html_path)
    if missing_files or missing_anchors:
        print("Link verification failed.")
        if missing_files:
            print("Missing files:")
            for item in missing_files:
                print(f"  - {item}")
        if missing_anchors:
            print("Missing anchors:")
            for item in missing_anchors:
                print(f"  - {item}")
        raise SystemExit(1)

    print(f"Wrote {master_path}")
    print(f"Wrote {export_md_path}")
    print(f"Wrote {html_path}")
    print("Verified HTML local file links and internal anchors.")


if __name__ == "__main__":
    main()
