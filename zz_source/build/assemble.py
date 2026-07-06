#!/usr/bin/env python3
"""
Assemble the staging outputs (zz_source/_staging/) into the teacher-facing
tree at the repo root:

    0 Planning/                  the master SOW, markbook, PLC
    1 Year 12 Weekly/            THE spine - one self-sufficient folder per SOW week
    2 Topic Library/             spec-order revision material per topic
    3 Assessments - TEACHER ONLY/  diagnostic, recaps, mocks (never set as homework)
    4 NEA and Programming/       NEA guide/template, workbooks, PyGame, Mini-NEA
    5 Reference and Stretch/     guides + A-Star pack
    INDEX.md                     generated map of every file

Non-destructive: builds into .assemble-tmp/, verifies every expected source
existed, then atomically swaps the six top-level folders. Exits non-zero and
leaves the old tree untouched if anything is missing.

Run the build-* scripts first (or just: python3 zz_source/build/build.py).
"""
import os, sys, csv, json, shutil, importlib.util
from urllib.parse import quote

from taxonomy import (REPO, SRC, STAGE_PDF, STAGE_WORD, STAGE_PPT, STAGE_XL,
                      STRUCTURE, SUB_STEM, SUB_TITLE, TOPIC_OF, TOPIC_STEM,
                      TOPIC_TITLE, YEAR13_SUBTOPICS, code_of)

STAGE_TT = os.path.join(REPO, "zz_source", "_staging", "tt")
STAGE_FC = os.path.join(REPO, "zz_source", "_staging", "flashcards")
TMP = os.path.join(REPO, ".assemble-tmp")
TOP = ["0 Planning", "1 Year 12 Weekly", "2 Topic Library",
       "3 Assessments - TEACHER ONLY", "4 NEA and Programming",
       "5 Reference and Stretch"]

missing = []


def _load(name):
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location(name, os.path.join(here, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cp(src, dst):
    if not os.path.exists(src):
        missing.append(os.path.relpath(src, REPO))
        return False
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    return True


def _h1(md_path, fallback):
    if os.path.exists(md_path):
        for l in open(md_path, encoding="utf-8"):
            if l.startswith("# "):
                return l[2:].strip()
    return fallback


def _fname(s):
    """Make a display title filesystem-safe."""
    s = s.replace("—", "-").replace("–", "-").replace("‘", "'").replace("’", "'")
    return "".join(c for c in s if c not in '\\/:*?"<>|').strip()


# ---------------------------------------------------------------- planning --
def build_planning(bdocx):
    d = os.path.join(TMP, "0 Planning")
    cp(os.path.join(STAGE_XL, "Year-12-SOW.xlsx"), os.path.join(d, "Year 12 Master SOW.xlsx"))
    cp(os.path.join(STAGE_TT, "Markbook", "H446-Markbook.xlsx"),
       os.path.join(d, "Markbook (KA and CAP tracking).xlsx"))
    cp(os.path.join(STAGE_TT, "PLC", "Personal-Learning-Checklist.xlsx"),
       os.path.join(d, "Personal Learning Checklist.xlsx"))
    cp(os.path.join(STAGE_XL, "Flashcards.xlsx"), os.path.join(d, "Flashcards (all topics).xlsx"))
    # editable Word render of the master SOW
    weeks = json.load(open(os.path.join(REPO, "zz_source", "sow", "year12.json"), encoding="utf-8"))
    md = ["# Year 12 Master Scheme of Work - OCR H446", "",
          "*One row per week. Everything named here is in the week's folder under "
          "'1 Year 12 Weekly', the Topic Library, or (for assessments) the teacher-only "
          "assessments folder.*", ""]
    for w in weeks:
        md.append(f"## {w['folder']}")
        md.append("")
        if w["taught"]:
            md.append(f"- **Taught:** {', '.join(w['taught'])}")
        if w["class_quiz"]:
            md.append(f"- **Class quiz (retrieval):** {', '.join(code_of(q) for q in w['class_quiz'])}")
        if w["assessment"]:
            md.append(f"- **Assessment:** {'; '.join(w['assessment'])}")
        if w["homework_note"]:
            md.append(f"- **Homework:** {w['homework_note']}")
        if w["consolidation_note"]:
            md.append(f"- **Consolidation:** {w['consolidation_note']}")
        if w["other_note"]:
            md.append(f"- {w['other_note']}")
        md.append("")
    bdocx.convert_text("\n".join(md), os.path.join(d, "Year 12 Master SOW (editable).docx"))


# ------------------------------------------------------------------ weekly --
def _qa_docx(bdocx, md_path, out_base, note=None):
    """Render one Q&A markdown into '<out_base>.docx' + '<out_base> - Answers.docx'."""
    if not os.path.exists(md_path):
        missing.append(os.path.relpath(md_path, REPO))
        return
    text = open(md_path, encoding="utf-8").read()
    q, a = bdocx.split_qa(text)
    if note:
        q = q.replace("\n", f"\n\n*{note}*\n", 1) if "\n" in q else q
    bdocx.convert_text(bdocx.inject_space(q), out_base + ".docx")
    if a:
        adoc = f"# {bdocx._h1(text)} - ANSWERS\n\n{a}"
        bdocx.convert_text(adoc, out_base + " - Answers.docx")


def _flashcard_doc(bdocx, dst, week_title, taught_codes, cards):
    if not taught_codes:
        return
    md = [f"# Flashcard Bank - {week_title}", "",
          f"*Everything taught so far ({len(taught_codes)} subtopic"
          f"{'s' if len(taught_codes) != 1 else ''}). Cover the answer column; "
          "quiz little and often.*", ""]
    for code in taught_codes:
        rows = [c for c in cards if c[0] == code]
        if not rows:
            continue
        md += [f"## {code} {SUB_TITLE.get(code, '').split(' ', 1)[-1]}", "",
               "| Question | Answer |", "|---|---|"]
        md += [f"| {q} | {a} |" for _, q, a in rows]
        md.append("")
    bdocx.convert_text("\n".join(md), dst)


def build_weekly(bdocx):
    root = os.path.join(TMP, "1 Year 12 Weekly")
    weeks = json.load(open(os.path.join(REPO, "zz_source", "sow", "year12.json"), encoding="utf-8"))
    clean = lambda s: " ".join(s.split()).replace("|", "/")
    cards = []
    with open(os.path.join(SRC, "flashcards", "by-subtopic.csv"), newline="", encoding="utf-8") as f:
        for r in list(csv.reader(f))[1:]:
            if len(r) >= 3:
                cards.append((r[0].strip(), clean(r[1]), clean(r[2])))
    taught = []
    for w in weeks:
        d = os.path.join(root, w["folder"])
        os.makedirs(d, exist_ok=True)
        for code in w["taught"]:
            cp(os.path.join(STAGE_TT, "Lesson-PowerPoints", f"{SUB_STEM[code]}.pptx"),
               os.path.join(d, f"1 Lesson {code}.pptx"))
            if code not in taught:
                taught.append(code)
        for stem in w["class_quiz"]:
            _qa_docx(bdocx, os.path.join(SRC, "subtopic-quizzes", f"{stem}.md"),
                     os.path.join(d, f"2 Class Quiz {code_of(stem)}"))
        # homework: one doc per week (merged if two subtopics are set)
        hw_note = w["homework_note"]
        if w["homework"]:
            qs, ans = [], []
            for stem in w["homework"]:
                p = os.path.join(SRC, "homework", f"{stem}.md")
                if not os.path.exists(p):
                    missing.append(os.path.relpath(p, REPO)); continue
                text = open(p, encoding="utf-8").read()
                q, a = bdocx.split_qa(text)
                qs.append(q)
                if a:
                    ans.append(f"# {bdocx._h1(text)} - ANSWERS\n\n{a}")
            doc = f"# {w['folder']} - Homework\n\n- {hw_note}\n\n---\n\n" + "\n\n---\n\n".join(qs)
            bdocx.convert_text(bdocx.inject_space(doc), os.path.join(d, "3 Homework.docx"))
            if ans:
                bdocx.convert_text("\n\n---\n\n".join(ans), os.path.join(d, "3 Homework - Answers.docx"))
        elif hw_note:
            bdocx.convert_text(f"# {w['folder']} - Homework\n\n- {hw_note}\n",
                               os.path.join(d, "3 Homework.docx"))
        # consolidation: instruction sheet + any scheduled paper as its own file
        cons_lines = [f"# {w['folder']} - Consolidation", ""]
        if w["consolidation_note"]:
            cons_lines.append(f"- {w['consolidation_note']}")
        if w["other_note"]:
            cons_lines.append(f"- {w['other_note']}")
        for stem in w["recap"]:
            title = _fname(_h1(os.path.join(SRC, "recap-checkpoints", f"{stem}.md"), stem)
                           .replace("Recap Checkpoint", "Recap"))
            _qa_docx(bdocx, os.path.join(SRC, "recap-checkpoints", f"{stem}.md"),
                     os.path.join(d, f"4a {title}"))
            cons_lines.append(f"- Sit **{title}** (in this folder) timed and closed book.")
        for stem in w["minipaper"]:
            _qa_docx(bdocx, os.path.join(SRC, "mini-papers", f"{stem}.md"),
                     os.path.join(d, f"4b Mini-Paper {code_of(stem)}"))
            cons_lines.append(f"- Sit **Mini-Paper {code_of(stem)}** (in this folder) timed.")
        for stem in w["worksheet"]:
            _qa_docx(bdocx, os.path.join(SRC, "worksheets", f"{stem}.md"),
                     os.path.join(d, f"4c End-of-Topic Worksheet {code_of(stem)}"))
            cons_lines.append(f"- Work through **End-of-Topic Worksheet {code_of(stem)}** (in this folder).")
        cons_lines += ["", "*Revision notes, knowledge organisers and flashcards for every topic "
                           "are in '2 Topic Library'.*"]
        if len(cons_lines) > 3:
            bdocx.convert_text("\n".join(cons_lines), os.path.join(d, "4 Consolidation.docx"))
        _flashcard_doc(bdocx, os.path.join(d, "5 Flashcards (cumulative).docx"),
                       w["folder"], list(taught), cards)


# ----------------------------------------------------------- topic library --
def build_library(bdocx):
    root = os.path.join(TMP, "2 Topic Library")
    comp_wd = {"Component 1 - Computer Systems": "01-Computer-Systems",
               "Component 2 - Algorithms and Programming": "02-Algorithms-and-Programming"}
    for comp, topics in STRUCTURE:
        for ttitle, tstem, subs in topics:
            td = os.path.join(root, comp, ttitle)
            cp(os.path.join(STAGE_WORD, "Knowledge-Organisers", f"{tstem}.docx"),
               os.path.join(td, "1 Knowledge Organiser.docx"))
            cp(os.path.join(STAGE_WORD, comp_wd[comp], f"{tstem}.docx"),
               os.path.join(td, "2 Topic Notes (complete).docx"))
            for stitle, sstem in subs:
                code = stitle.split()[0]
                cp(os.path.join(STAGE_WORD, "Subtopic-Revision", f"{sstem}.docx"),
                   os.path.join(td, f"3 Revision Notes {code}.docx"))
            cp(os.path.join(STAGE_WORD, "Worksheets", f"{tstem}.docx"),
               os.path.join(td, "4 End-of-Topic Worksheet.docx"))
            cp(os.path.join(STAGE_WORD, "Worksheets", f"{tstem}-ANSWERS.docx"),
               os.path.join(td, "4 End-of-Topic Worksheet - Answers.docx"))
            cp(os.path.join(STAGE_WORD, "Mini-Papers", f"{tstem}.docx"),
               os.path.join(td, "5 Mini-Paper (timed).docx"))
            cp(os.path.join(STAGE_WORD, "Mini-Papers", f"{tstem}-ANSWERS.docx"),
               os.path.join(td, "5 Mini-Paper (timed) - Answers.docx"))
            cp(os.path.join(STAGE_FC, f"{ttitle.split()[0]}.csv"),
               os.path.join(td, "6 Flashcards.csv"))
            cp(os.path.join(STAGE_WORD, "Revision-Games", f"{tstem}.docx"),
               os.path.join(td, "7 Revision Game.docx"))
            cp(os.path.join(STAGE_PDF, "revision-games-cards", f"{tstem}-cards.pdf"),
               os.path.join(td, "7 Revision Game - Cards (print and cut).pdf"))
            cp(os.path.join(STAGE_WORD, "Lesson-Activities", f"{tstem}.docx"),
               os.path.join(td, "8 Lesson Activities (teacher).docx"))
            # material for subtopics not taught until Year 13
            for stitle, sstem in subs:
                code = stitle.split()[0]
                if code not in YEAR13_SUBTOPICS:
                    continue
                y13 = os.path.join(td, f"Year 13 - {code} {stitle.split(' ', 1)[1]}")
                cp(os.path.join(STAGE_TT, "Lesson-PowerPoints", f"{sstem}.pptx"),
                   os.path.join(y13, "1 Lesson.pptx"))
                _qa_docx(bdocx, os.path.join(SRC, "subtopic-quizzes", f"{sstem}.md"),
                         os.path.join(y13, "2 Quiz"))
                _qa_docx(bdocx, os.path.join(SRC, "homework", f"{sstem}.md"),
                         os.path.join(y13, "3 Homework"))


# ------------------------------------------------------------- assessments --
def build_assessments(bdocx):
    root = os.path.join(TMP, "3 Assessments - TEACHER ONLY")
    amap = os.path.join(STAGE_WORD, "Assessments", "00-assessment-map.docx")
    cp(amap, os.path.join(root, "0 Assessment Map (KA-CAP-mock schedule).docx"))
    for stem, nice in [("01-diagnostic-week-1", "1 Diagnostic (Week 1)"),
                       ("02-mock-paper-1c", "2 Mock Paper 1C (Week 27, unseen)")]:
        cp(os.path.join(STAGE_WORD, "Assessments", f"{stem}.docx"),
           os.path.join(root, f"{nice}.docx"))
        cp(os.path.join(STAGE_WORD, "Assessments", f"{stem}-ANSWERS.docx"),
           os.path.join(root, f"{nice} - Answers.docx"))
        cp(os.path.join(STAGE_PDF, "assessments", f"{stem}.pdf"),
           os.path.join(root, f"{nice} (print).pdf"))
    mocks = os.path.join(root, "Mock Papers")
    for stem, nice in [("mock-paper-1-computer-systems", "Mock Paper 1"),
                       ("mock-paper-1b-computer-systems", "Mock Paper 1B"),
                       ("mock-paper-2-algorithms-and-programming", "Mock Paper 2 (Year 13)"),
                       ("mock-paper-2b-algorithms-and-programming", "Mock Paper 2B (Year 13)")]:
        cp(os.path.join(STAGE_WORD, "Mock-Papers", f"{stem}.docx"), os.path.join(mocks, f"{nice}.docx"))
        cp(os.path.join(STAGE_WORD, "Mock-Papers", f"{stem}-ANSWERS.docx"),
           os.path.join(mocks, f"{nice} - Answers.docx"))
        cp(os.path.join(STAGE_PDF, "mock-papers", f"{stem}.pdf"), os.path.join(mocks, f"{nice} (print).pdf"))
        cp(os.path.join(STAGE_PDF, "mock-papers", f"{stem}-ANSWERS.pdf"),
           os.path.join(mocks, f"{nice} - Answers (print).pdf"))
    recaps = os.path.join(root, "Recap Checkpoints")
    import glob as _glob
    for md in sorted(_glob.glob(os.path.join(SRC, "recap-checkpoints", "*.md"))):
        stem = os.path.splitext(os.path.basename(md))[0]
        if stem.lower() == "readme":
            continue
        title = _fname(_h1(md, stem).replace("Recap Checkpoint", "Recap"))
        y13 = stem in ("recap-4-after-1.5-and-2.1", "recap-5-after-2.2-2.3",
                       "recap-6-full-year-12-pre-mock")
        dstdir = os.path.join(recaps, "Year 13") if y13 else recaps
        cp(os.path.join(STAGE_WORD, "Recap-Checkpoints", f"{stem}.docx"),
           os.path.join(dstdir, f"{title}.docx"))
        cp(os.path.join(STAGE_WORD, "Recap-Checkpoints", f"{stem}-ANSWERS.docx"),
           os.path.join(dstdir, f"{title} - Answers.docx"))
        cp(os.path.join(STAGE_PDF, "recap-checkpoints", f"{stem}.pdf"),
           os.path.join(dstdir, f"{title} (print).pdf"))


# ---------------------------------------------------------------- nea etc. --
def build_nea():
    d = os.path.join(TMP, "4 NEA and Programming")
    W = lambda *p: os.path.join(STAGE_WORD, *p)
    cp(W("03-04-Programming-Project", "Programming-Project-NEA-Guide.docx"),
       os.path.join(d, "1 NEA Guide.docx"))
    cp(W("NEA-Pack", "NEA-Project-Template.docx"), os.path.join(d, "2 NEA Project Template.docx"))
    cp(W("Programming-Workbook", "01-core-programming-skills.docx"),
       os.path.join(d, "3 Programming Workbook 1 - Core Skills.docx"))
    cp(W("Programming-Workbook", "02-algorithms-and-data-structures.docx"),
       os.path.join(d, "4 Programming Workbook 2 - Algorithms and Data Structures.docx"))
    cp(W("03-04-Programming-Project", "pygame-workbook.docx"),
       os.path.join(d, "5 PyGame Workbook (weeks 22-28).docx"))
    cp(W("03-04-Programming-Project", "mini-nea-pack.docx"),
       os.path.join(d, "6 Mini-NEA Pack (weeks 29-36).docx"))


def build_reference():
    d = os.path.join(TMP, "5 Reference and Stretch")
    refmap = {
        "glossary.docx": "Glossary.docx",
        "reference-sheet.docx": "Reference Sheet (number, Big O, logic, SQL).docx",
        "command-words-and-assessment-objectives.docx": "Command Words and AOs.docx",
        "exam-technique.docx": "Exam Technique.docx",
        "common-mistakes.docx": "Common Mistakes.docx",
        "diagram-bank.docx": "Diagram Bank.docx",
        "pseudocode-guide.docx": "OCR Pseudocode Guide.docx",
        "study-plan-and-how-to-use.docx": "Study Plan.docx",
    }
    for s, t in refmap.items():
        cp(os.path.join(STAGE_WORD, "Guides", s), os.path.join(d, t))
    cp(os.path.join(STAGE_WORD, "Course-Guide", "past-papers-guide.docx"),
       os.path.join(d, "Past Papers Guide.docx"))
    import glob as _glob
    for f in sorted(_glob.glob(os.path.join(STAGE_WORD, "A-Star-Pack", "*.docx"))):
        base = os.path.splitext(os.path.basename(f))[0]
        nice = "A-Star " + base.split("-", 1)[0].lstrip("0") + " - " + \
               base.split("-", 1)[1].replace("-", " ").title()
        cp(f, os.path.join(d, nice + ".docx"))


def build_index():
    lines = ["# Index - every file, one click", "",
             "*Generated by the assembler; regenerate rather than edit.*", ""]
    for top in TOP:
        for dirpath, dirnames, filenames in os.walk(os.path.join(TMP, top)):
            dirnames.sort()
            rel = os.path.relpath(dirpath, TMP)
            depth = rel.count(os.sep)
            lines.append(f"{'#' * min(depth + 2, 4)} {os.path.basename(dirpath)}")
            lines.append("")
            for fn in sorted(filenames):
                lines.append(f"- [{fn}]({quote(os.path.join(rel, fn))})")
            lines.append("")
    with open(os.path.join(TMP, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    if os.path.isdir(TMP):
        shutil.rmtree(TMP)
    os.makedirs(TMP)
    bdocx = _load("build-docx")
    build_planning(bdocx)
    build_weekly(bdocx)
    build_library(bdocx)
    build_assessments(bdocx)
    build_nea()
    build_reference()
    cp(os.path.join(STAGE_WORD, "Course-Guide", "00-Start-Here.docx"),
       os.path.join(TMP, "START HERE.docx"))
    build_index()
    if missing:
        print(f"ABORT: {len(missing)} expected source file(s) missing - old tree left untouched:")
        for m in missing:
            print("  -", m)
        sys.exit(1)
    # atomic swap
    for top in TOP:
        dst = os.path.join(REPO, top)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.move(os.path.join(TMP, top), dst)
    shutil.move(os.path.join(TMP, "INDEX.md"), os.path.join(REPO, "INDEX.md"))
    if os.path.exists(os.path.join(REPO, "START HERE.docx")):
        os.remove(os.path.join(REPO, "START HERE.docx"))
    shutil.move(os.path.join(TMP, "START HERE.docx"), os.path.join(REPO, "START HERE.docx"))
    shutil.rmtree(TMP)
    total = sum(len(fs) for top in TOP for _, _, fs in os.walk(os.path.join(REPO, top)))
    print(f"Assembled {total} files across: {', '.join(TOP)}")


if __name__ == "__main__":
    main()
