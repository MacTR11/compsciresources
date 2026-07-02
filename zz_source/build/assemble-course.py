#!/usr/bin/env python3
"""
Assemble the flat build outputs (Word-Documents/, Printable-PDFs/,
Teacher-Toolkit/, Spreadsheets/) into the two folders people actually use:

    Course/           everything for teaching & revision, numbered in
                      teach order (components -> topics -> subtopics),
                      plus Recap Checkpoints, Reference Guides and the
                      A-Star pack. Includes a generated INDEX.md map.
    Teacher Toolkit/  markbook, PLC, lesson plan, SOW, trackers.

Run the build-* scripts first, then this. The flat output folders are
regeneration staging (git-ignored); Course/ + Teacher Toolkit/ are kept.
"""
import os, shutil, glob
from urllib.parse import quote

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WD = os.path.join(REPO, "Word-Documents")
PDF = os.path.join(REPO, "Printable-PDFs")
TT = os.path.join(REPO, "Teacher-Toolkit")
XL = os.path.join(REPO, "Spreadsheets")
SRC = os.path.join(REPO, "zz_source", "revision-tools")
COURSE = os.path.join(REPO, "Course")

missing = []


def cp(src, dst):
    if not os.path.exists(src):
        missing.append(os.path.relpath(src, REPO)); return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


# (Component folder, [ (Topic folder, topic-stem, [(Subtopic folder, sub-stem)...]) ])
STRUCTURE = [
 ("1 Component 1 - Computer Systems", [
   ("1.1 Processors, Input, Output and Storage", "1.1-processors-input-output-storage", [
     ("1.1.1 Structure and Function of the Processor", "1.1.1-structure-and-function-of-the-processor"),
     ("1.1.2 Types of Processor", "1.1.2-types-of-processor"),
     ("1.1.3 Input, Output and Storage Devices", "1.1.3-input-output-and-storage-devices")]),
   ("1.2 Software and Software Development", "1.2-software-and-software-development", [
     ("1.2.1 Operating Systems", "1.2.1-operating-systems"),
     ("1.2.2 Applications Generation", "1.2.2-applications-generation"),
     ("1.2.3 Software Development", "1.2.3-software-development"),
     ("1.2.4 Types of Programming Language", "1.2.4-types-of-programming-language")]),
   ("1.3 Exchanging Data", "1.3-exchanging-data", [
     ("1.3.1 Compression, Encryption and Hashing", "1.3.1-compression-encryption-and-hashing"),
     ("1.3.2 Databases", "1.3.2-databases"),
     ("1.3.3 Networks", "1.3.3-networks"),
     ("1.3.4 Web Technologies", "1.3.4-web-technologies")]),
   ("1.4 Data Types, Data Structures and Boolean Algebra", "1.4-data-types-structures-boolean-algebra", [
     ("1.4.1 Data Types", "1.4.1-data-types"),
     ("1.4.2 Data Structures", "1.4.2-data-structures"),
     ("1.4.3 Boolean Algebra", "1.4.3-boolean-algebra")]),
   ("1.5 Legal, Moral, Cultural and Ethical Issues", "1.5-legal-moral-cultural-ethical", [
     ("1.5.1 Computing Related Legislation", "1.5.1-computing-related-legislation"),
     ("1.5.2 Moral and Ethical Issues", "1.5.2-moral-and-ethical-issues")]),
 ]),
 ("2 Component 2 - Algorithms and Programming", [
   ("2.1 Elements of Computational Thinking", "2.1-elements-of-computational-thinking", [
     ("2.1.1 Thinking Abstractly", "2.1.1-thinking-abstractly"),
     ("2.1.2 Thinking Ahead", "2.1.2-thinking-ahead"),
     ("2.1.3 Thinking Procedurally", "2.1.3-thinking-procedurally"),
     ("2.1.4 Thinking Logically", "2.1.4-thinking-logically"),
     ("2.1.5 Thinking Concurrently", "2.1.5-thinking-concurrently")]),
   ("2.2 Problem Solving and Programming", "2.2-problem-solving-and-programming", [
     ("2.2.1 Programming Techniques", "2.2.1-programming-techniques"),
     ("2.2.2 Computational Methods", "2.2.2-computational-methods")]),
   ("2.3 Algorithms", "2.3-algorithms", [
     ("2.3.1 Algorithms", "2.3.1-algorithms")]),
 ]),
]

COMP_WD = {"1 Component 1 - Computer Systems": "01-Computer-Systems",
           "2 Component 2 - Algorithms and Programming": "02-Algorithms-and-Programming"}

RECAP_NAMES = {
    "recap-1-after-component-1.1-1.2": "Recap 1 - after 1.1-1.2",
    "recap-2-after-1.3-exchanging-data": "Recap 2 - after 1.1-1.3",
    "recap-3-after-1.4-data-and-logic": "Recap 3 - after 1.1-1.4 (pre-mock)",
    "recap-4-after-1.5-and-2.1": "Recap 4 - Year 13 (adds 1.5, 2.1)",
    "recap-5-after-2.2-2.3": "Recap 5 - Year 13 (adds 2.2-2.3)",
    "recap-6-full-year-12-pre-mock": "Recap 6 - Year 13 full synoptic",
}


def build():
    if os.path.isdir(COURSE):
        shutil.rmtree(COURSE)

    # ---- Components 1 & 2: topics and subtopics, numbered in teach order ----
    for comp, topics in STRUCTURE:
        for tname, tstem, subs in topics:
            tdir = os.path.join(COURSE, comp, tname)
            tr = os.path.join(tdir, "00 Topic Resources")
            cp(os.path.join(PDF, "knowledge-organisers", f"{tstem}.pdf"), os.path.join(tr, "1 Knowledge Organiser.pdf"))
            cp(os.path.join(WD, "Knowledge-Organisers", f"{tstem}.docx"), os.path.join(tr, "1 Knowledge Organiser (editable).docx"))
            cp(os.path.join(WD, COMP_WD[comp], f"{tstem}.docx"), os.path.join(tr, "2 Revision Notes (full topic).docx"))
            cp(os.path.join(SRC, "flashcards", f"{tstem}.csv"), os.path.join(tr, "3 Flashcards.csv"))
            cp(os.path.join(PDF, "lesson-activities", f"{tstem}.pdf"), os.path.join(tr, "4 Lesson Activities Pack (teacher).pdf"))
            cp(os.path.join(WD, "Lesson-Activities", f"{tstem}.docx"), os.path.join(tr, "4 Lesson Activities Pack (editable).docx"))
            cp(os.path.join(PDF, "revision-games", f"{tstem}.pdf"), os.path.join(tr, "5 Revision Game - How to Play.pdf"))
            cp(os.path.join(PDF, "revision-games-cards", f"{tstem}-cards.pdf"), os.path.join(tr, "5 Revision Game - Print and Cut Cards.pdf"))
            cp(os.path.join(PDF, "worksheets", f"{tstem}.pdf"), os.path.join(tr, "6 End-of-Topic Worksheet.pdf"))
            cp(os.path.join(PDF, "worksheets", f"{tstem}-ANSWERS.pdf"), os.path.join(tr, "6 End-of-Topic Worksheet - ANSWERS.pdf"))
            cp(os.path.join(WD, "Worksheets", f"{tstem}.docx"), os.path.join(tr, "6 End-of-Topic Worksheet (editable).docx"))
            cp(os.path.join(PDF, "mini-papers", f"{tstem}.pdf"), os.path.join(tr, "7 Topic Mini-Paper.pdf"))
            cp(os.path.join(PDF, "mini-papers", f"{tstem}-ANSWERS.pdf"), os.path.join(tr, "7 Topic Mini-Paper - ANSWERS.pdf"))
            for sname, sstem in subs:
                sd = os.path.join(tdir, sname)
                cp(os.path.join(TT, "Lesson-PowerPoints", f"{sstem}.pptx"), os.path.join(sd, "1 Lesson.pptx"))
                cp(os.path.join(PDF, "subtopic-revision", f"{sstem}.pdf"), os.path.join(sd, "2 Revision Notes.pdf"))
                cp(os.path.join(WD, "Subtopic-Revision", f"{sstem}.docx"), os.path.join(sd, "2 Revision Notes (editable).docx"))
                cp(os.path.join(PDF, "subtopic-quizzes", f"{sstem}.pdf"), os.path.join(sd, "3 Worksheet.pdf"))
                cp(os.path.join(PDF, "subtopic-quizzes", f"{sstem}-ANSWERS.pdf"), os.path.join(sd, "3 Worksheet - ANSWERS.pdf"))
                cp(os.path.join(WD, "Subtopic-Quizzes", f"{sstem}.docx"), os.path.join(sd, "3 Worksheet (editable).docx"))
                cp(os.path.join(PDF, "homework", f"{sstem}.pdf"), os.path.join(sd, "4 Homework.pdf"))
                cp(os.path.join(PDF, "homework", f"{sstem}-ANSWERS.pdf"), os.path.join(sd, "4 Homework - ANSWERS.pdf"))
                cp(os.path.join(WD, "Homework", f"{sstem}.docx"), os.path.join(sd, "4 Homework (editable).docx"))

    # ---- Start Here at Course root ----
    cp(os.path.join(PDF, "course-guide", "00-Start-Here.pdf"), os.path.join(COURSE, "00 START HERE - How to Use These Resources.pdf"))
    cp(os.path.join(WD, "Course-Guide", "00-Start-Here.docx"), os.path.join(COURSE, "00 START HERE - How to Use These Resources.docx"))

    # ---- Component 3 ----
    c3 = os.path.join(COURSE, "3 Component 3 - Programming Project")
    cp(os.path.join(WD, "03-04-Programming-Project", "Programming-Project-NEA-Guide.docx"), os.path.join(c3, "1 NEA Guide.docx"))
    cp(os.path.join(PDF, "nea-pack", "NEA-Project-Template.pdf"), os.path.join(c3, "2 NEA Project Template (student).pdf"))
    cp(os.path.join(WD, "NEA-Pack", "NEA-Project-Template.docx"), os.path.join(c3, "2 NEA Project Template (editable).docx"))
    cp(os.path.join(WD, "Programming-Workbook", "01-core-programming-skills.docx"),
       os.path.join(c3, "3 Programming Workbook 1 - Core Skills.docx"))
    cp(os.path.join(WD, "Programming-Workbook", "02-algorithms-and-data-structures.docx"),
       os.path.join(c3, "4 Programming Workbook 2 - Algorithms and Data Structures.docx"))

    # ---- Recap checkpoints ----
    rc = os.path.join(COURSE, "4 Recap Checkpoints")
    for f in sorted(glob.glob(os.path.join(PDF, "recap-checkpoints", "*.pdf"))):
        base = os.path.basename(f)[:-4]
        ans = base.endswith("-ANSWERS")
        stem = base[:-8] if ans else base
        nice = RECAP_NAMES.get(stem, stem) + (" - ANSWERS" if ans else "")
        cp(f, os.path.join(rc, nice + ".pdf"))

    # ---- Reference guides (inside Course so students find them) ----
    ref = os.path.join(COURSE, "5 Reference Guides")
    refmap = {
        "glossary.docx": "Glossary.docx",
        "reference-sheet.docx": "Reference Sheet (number, Big O, logic, SQL).docx",
        "command-words-and-assessment-objectives.docx": "Command Words and Assessment Objectives.docx",
        "exam-technique.docx": "Exam Technique.docx",
        "common-mistakes.docx": "Common Mistakes.docx",
        "diagram-bank.docx": "Diagram Bank.docx",
        "pseudocode-guide.docx": "OCR Pseudocode Guide.docx",
        "study-plan-and-how-to-use.docx": "Study Plan.docx",
    }
    for src_name, dst_name in refmap.items():
        cp(os.path.join(WD, "Guides", src_name), os.path.join(ref, dst_name))
    cp(os.path.join(WD, "Course-Guide", "past-papers-guide.docx"),
       os.path.join(ref, "Past Papers Guide (index and how to use).docx"))
    cp(os.path.join(PDF, "course-guide", "past-papers-guide.pdf"),
       os.path.join(ref, "Past Papers Guide (index and how to use).pdf"))

    # ---- A-Star stretch pack (inside Course) ----
    astar = os.path.join(COURSE, "6 A-Star Stretch Pack")
    for f in sorted(glob.glob(os.path.join(WD, "A-Star-Pack", "*.docx"))):
        cp(f, os.path.join(astar, os.path.basename(f)))

    # ---- Teacher Toolkit ----
    tk = os.path.join(REPO, "Teacher Toolkit")
    if os.path.isdir(tk): shutil.rmtree(tk)
    cp(os.path.join(TT, "Markbook", "H446-Markbook.xlsx"), os.path.join(tk, "Markbook (KA and CAP tracking).xlsx"))
    cp(os.path.join(TT, "PLC", "Personal-Learning-Checklist.xlsx"), os.path.join(tk, "Personal Learning Checklist.xlsx"))
    cp(os.path.join(TT, "Planning", "medium-term-plan.docx"), os.path.join(tk, "Lesson Plan (week by week).docx"))
    cp(os.path.join(XL, "Scheme-of-Work-Homework-and-Consolidation.xlsx"), os.path.join(tk, "Homework and Consolidation Plan (week by week).xlsx"))
    cp(os.path.join(PDF, "scheme-of-work", "year-12-homework-and-consolidation.pdf"), os.path.join(tk, "Homework and Consolidation Plan (printable).pdf"))
    cp(os.path.join(XL, "Self-Assessment-Tracker.xlsx"), os.path.join(tk, "Self-Assessment Tracker (RAG).xlsx"))
    cp(os.path.join(XL, "Flashcards.xlsx"), os.path.join(tk, "Flashcards (all topics).xlsx"))

    # ---- Generated INDEX.md: a clickable map of everything in Course/ ----
    lines = ["# Course Index — every file, one click away", "",
             "*Generated by the assembler — regenerate rather than editing by hand.*", ""]
    for dirpath, dirnames, filenames in os.walk(COURSE):
        dirnames.sort()
        rel = os.path.relpath(dirpath, COURSE)
        depth = 0 if rel == "." else rel.count(os.sep) + 1
        if rel != ".":
            lines.append(f"{'#' * min(depth + 1, 4)} {os.path.basename(dirpath)}" if depth <= 2
                         else f"**{os.path.basename(dirpath)}**")
            lines.append("")
        for fn in sorted(filenames):
            if fn == "INDEX.md":
                continue
            relf = fn if rel == "." else os.path.join(rel, fn)
            lines.append(f"- [{fn}]({quote(relf)})")
        lines.append("")
    with open(os.path.join(COURSE, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("Assembled Course/ (+INDEX.md) and Teacher Toolkit/.")
    course_files = sum(len(fs) for _, _, fs in os.walk(COURSE))
    print(f"Course files: {course_files}")
    if missing:
        print(f"\n{len(missing)} expected source(s) missing (run all build-* scripts first):")
        for m in missing[:20]:
            print("  -", m)


if __name__ == "__main__":
    build()
