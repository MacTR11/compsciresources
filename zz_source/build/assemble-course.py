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

    build_weekly()

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




# ---------------------------------------------------------------------------
# Weekly plan folder: Course/7 Weekly Plan.../Week NN .../ with the actual
# homework + consolidation files for that week of the L6 SOW (v2 plan).
# ---------------------------------------------------------------------------
def _wk_sources():
    _c = lambda s: ".".join(s.split("-")[0].split(".")[:3])   # "1.3.1-compression..." -> "1.3.1"
    H  = lambda s: (os.path.join(PDF, "homework", f"{s}.pdf"), f"1 Homework {_c(s)}.pdf")
    HA = lambda s: (os.path.join(PDF, "homework", f"{s}-ANSWERS.pdf"), f"1 Homework {_c(s)} - ANSWERS.pdf")
    Q  = lambda s: (os.path.join(PDF, "subtopic-quizzes", f"{s}.pdf"), f"2 Consolidation - Quiz {_c(s)}.pdf")
    QA = lambda s: (os.path.join(PDF, "subtopic-quizzes", f"{s}-ANSWERS.pdf"), f"2 Consolidation - Quiz {_c(s)} - ANSWERS.pdf")
    RN = lambda s: (os.path.join(PDF, "subtopic-revision", f"{s}.pdf"), f"2 Consolidation - Revision Notes {_c(s)}.pdf")
    KO = lambda t, c: (os.path.join(PDF, "knowledge-organisers", f"{t}.pdf"), f"2 Consolidation - Knowledge Organiser {c}.pdf")
    MP = lambda t, c: (os.path.join(PDF, "mini-papers", f"{t}.pdf"), f"2 Consolidation - Mini-Paper {c}.pdf")
    MPA= lambda t, c: (os.path.join(PDF, "mini-papers", f"{t}-ANSWERS.pdf"), f"2 Consolidation - Mini-Paper {c} - ANSWERS.pdf")
    FC = lambda t, c: (os.path.join(SRC, "flashcards", f"{t}.csv"), f"2 Consolidation - Flashcards {c}.csv")
    RC = lambda s, n: (os.path.join(PDF, "recap-checkpoints", f"{s}.pdf"), f"2 Consolidation - {n}.pdf")
    RCA= lambda s, n: (os.path.join(PDF, "recap-checkpoints", f"{s}-ANSWERS.pdf"), f"2 Consolidation - {n} - ANSWERS.pdf")
    T11, T12, T13, T14 = ("1.1-processors-input-output-storage", "1.2-software-and-software-development",
                          "1.3-exchanging-data", "1.4-data-types-structures-boolean-algebra")
    s = {"1.1.1": "1.1.1-structure-and-function-of-the-processor", "1.1.2": "1.1.2-types-of-processor",
         "1.1.3": "1.1.3-input-output-and-storage-devices", "1.2.1": "1.2.1-operating-systems",
         "1.2.2": "1.2.2-applications-generation", "1.2.3": "1.2.3-software-development",
         "1.2.4": "1.2.4-types-of-programming-language", "1.3.1": "1.3.1-compression-encryption-and-hashing",
         "1.3.2": "1.3.2-databases", "1.3.3": "1.3.3-networks", "1.3.4": "1.3.4-web-technologies",
         "1.4.1": "1.4.1-data-types", "1.4.2": "1.4.2-data-structures", "1.4.3": "1.4.3-boolean-algebra",
         "2.1.1": "2.1.1-thinking-abstractly", "2.1.2": "2.1.2-thinking-ahead", "2.1.3": "2.1.3-thinking-procedurally",
         "2.1.4": "2.1.4-thinking-logically", "2.1.5": "2.1.5-thinking-concurrently",
         "2.2.1": "2.2.1-programming-techniques"}
    hw = lambda c: [H(s[c]), HA(s[c])]
    qz = lambda c: [Q(s[c]), QA(s[c])]
    R1, R2, R3 = "recap-1-after-component-1.1-1.2", "recap-2-after-1.3-exchanging-data", "recap-3-after-1.4-data-and-logic"
    M1  = (os.path.join(PDF, "mock-papers", "mock-paper-1-computer-systems.pdf"), "1 Mock Paper 1.pdf")
    M1A = (os.path.join(PDF, "mock-papers", "mock-paper-1-computer-systems-ANSWERS.pdf"), "1 Mock Paper 1 - ANSWERS.pdf")
    M1B = (os.path.join(PDF, "mock-papers", "mock-paper-1b-computer-systems.pdf"), "1 Mock Paper 1B (extra practice).pdf")
    M1BA= (os.path.join(PDF, "mock-papers", "mock-paper-1b-computer-systems-ANSWERS.pdf"), "1 Mock Paper 1B - ANSWERS.pdf")
    NEA = (os.path.join(PDF, "nea-pack", "NEA-Project-Template.pdf"), "1 NEA Project Template.pdf")

    return [
     ("Week 01 (31 Aug) - Induction and diagnostic",
      "HW: complete the diagnostic task; set up VS Code, Python, Classroom.\nConsolidation: read the START HERE guide; set up notes and folders.",
      [(os.path.join(PDF, "course-guide", "00-Start-Here.pdf"), "2 Consolidation - Start Here guide.pdf")]),
     ("Week 02 (07 Sep) - 1.1.1 CPU and FDE",
      "HW: Homework 1.1.1 (/20). Programming: Workbook 1 s1-2.\nConsolidation: Revision Notes 1.1.1 cover-and-recall; start Flashcards 1.1.",
      hw("1.1.1") + [RN(s["1.1.1"]), FC(T11, "1.1")]),
     ("Week 03 (14 Sep) - 1.1.2 Types of processor (KA1)",
      "HW: Homework 1.1.2; revise for KA1 with the 1.1 Knowledge Organiser.\nConsolidation: Quiz 1.1.1 closed-book; Flashcards 1.1.",
      hw("1.1.2") + qz("1.1.1") + [KO(T11, "1.1")]),
     ("Week 04 (21 Sep) - 1.1.3 IO and storage + 2.1.1 (KA1 feedback)",
      "HW: Homework 1.1.3 + Homework 2.1.1; act on KA1 feedback.\nConsolidation: Quizzes 1.1.2 and 2.1.1; Revision Notes 1.1.3.",
      hw("1.1.3") + hw("2.1.1") + qz("1.1.2") + qz("2.1.1") + [RN(s["1.1.3"])]),
     ("Week 05 (28 Sep) - 1.2.1 OS + 2.1.2 (CAP1-KA2)",
      "HW: Homework 1.2.1; prep CAP1/KA2.\nConsolidation: Quiz 1.1.3; Mini-Paper 1.1 Section A timed.",
      hw("1.2.1") + qz("1.1.3") + [MP(T11, "1.1"), MPA(T11, "1.1")]),
     ("Week 06 (05 Oct) - Review week - 1.2.1 BIOS, drivers, VMs",
      "HW: Homework 2.1.2; act on CAP1/KA2 feedback.\nConsolidation: file-check prep; Quiz 1.2.1; mixed Flashcards 1.1 + 1.2.",
      hw("2.1.2") + qz("1.2.1") + [FC(T12, "1.2")]),
     ("Week 07 (12 Oct) - 1.2.2 Translators (KA3, CAP1 due)",
      "HW: Homework 1.2.2; compilation-stages drill from End-of-Topic Worksheet 1.2.\nConsolidation: full Mini-Paper 1.1 timed; Quiz 2.1.2.",
      hw("1.2.2") + qz("2.1.2") + [MP(T11, "1.1"), MPA(T11, "1.1")]),
     ("Half Term 1 (19 Oct)",
      "Finish any outstanding sheet. 10 min per day of Flashcards 1.1-1.2.",
      [FC(T11, "1.1"), FC(T12, "1.2")]),
     ("Week 08 (02 Nov) - 1.2.3 Methodologies + 2.1.3 (KA3 feedback)",
      "HW: Homework 1.2.3 + Homework 2.1.3.\nConsolidation: Quiz 1.2.2; Revision Notes 1.2.3.",
      hw("1.2.3") + hw("2.1.3") + qz("1.2.2") + [RN(s["1.2.3"])]),
     ("Week 09 (09 Nov) - 1.2.4 Paradigms, assembly, OOP (CAP2-KA4)",
      "HW: Homework 1.2.4; prep CAP2/KA4 with the 1.2 Organiser.\nConsolidation: Quiz 1.2.3; Flashcards 1.2.",
      hw("1.2.4") + qz("1.2.3") + [KO(T12, "1.2"), FC(T12, "1.2")]),
     ("Week 10 (16 Nov) - 1.3.1 Compression and encryption (CAP2-KA4 fb)",
      "HW: Homework 1.3.1; act on CAP2 feedback.\nConsolidation: RECAP CHECKPOINT 1 (1.1-1.2) timed; Quiz 1.2.4.",
      hw("1.3.1") + qz("1.2.4") + [RC(R1, "Recap 1 (1.1-1.2)"), RCA(R1, "Recap 1 (1.1-1.2)")]),
     ("Week 11 (23 Nov) - 1.3.2 Normalisation and SQL",
      "HW: Homework 1.3.2; SQL practice from End-of-Topic Worksheet 1.3.\nConsolidation: Quiz 1.3.1; Revision Notes 1.3.2.",
      hw("1.3.2") + qz("1.3.1") + [RN(s["1.3.2"])]),
     ("Week 12 (30 Nov) - 1.3.3 Networks and TCP-IP",
      "HW: Homework 1.3.3; redraw the network diagrams (Diagram Bank in Reference Guides).\nConsolidation: Quiz 1.3.2; mixed Flashcards 1.1-1.3.",
      hw("1.3.3") + qz("1.3.2") + [FC(T13, "1.3")]),
     ("Week 13 (07 Dec) - 2.1.4 + 1.3.4 Web technologies (CAP2 due)",
      "HW: Homework 2.1.4 + Homework 1.3.4 Part A.\nConsolidation: Quiz 1.3.3; Revision Notes 1.3.4 and 2.1.4.",
      hw("2.1.4") + hw("1.3.4") + qz("1.3.3") + [RN(s["1.3.4"]), RN(s["2.1.4"])]),
     ("Week 14 (14 Dec) - 1.3.4 Server-client, PageRank - EOY quiz",
      "HW: finish Homework 1.3.4; prep the end-of-year quiz with Organisers 1.1-1.3.\nConsolidation: Quizzes 1.3.4 and 2.1.4; Mini-Paper 1.2 timed.",
      qz("1.3.4") + qz("2.1.4") + [MP(T12, "1.2"), MPA(T12, "1.2"), KO(T13, "1.3")]),
     ("Christmas Holidays",
      "RECAP CHECKPOINT 2 (1.1-1.3) over the break; 10 min per day flashcards.",
      [RC(R2, "Recap 2 (1.1-1.3)"), RCA(R2, "Recap 2 (1.1-1.3)")]),
     ("Week 15 (04 Jan) - 1.4.1 Binary, negatives, hex",
      "HW: Homework 1.4.1 Part A + conversion drills (End-of-Topic Worksheet 1.4).\nConsolidation: mark the holiday Recap 2; re-RAG the PLC.",
      hw("1.4.1") + [(os.path.join(PDF, "worksheets", T14 + ".pdf"), "1 End-of-Topic Worksheet 1.4 (drills).pdf"),
                     (os.path.join(PDF, "worksheets", T14 + "-ANSWERS.pdf"), "1 End-of-Topic Worksheet 1.4 - ANSWERS.pdf")]),
     ("Week 16 (11 Jan) - 1.4.1 Floating point (KA5)",
      "HW: floating-point drills from Worksheet 1.4; prep KA5 with the Reference Sheet.\nConsolidation: Quiz 1.4.1 Section A; Revision Notes 1.4.1.",
      qz("1.4.1") + [RN(s["1.4.1"])]),
     ("Week 17 (18 Jan) - 1.4.1 Character sets + 2.2.1 (KA5 feedback)",
      "HW: finish Homework 1.4.1; Homework 2.2.1 Part A; act on KA5 feedback.\nConsolidation: full Quiz 1.4.1; start Flashcards 1.4.",
      hw("2.2.1") + [FC(T14, "1.4")]),
     ("Week 18 (25 Jan) - 1.4.2 Arrays to stacks and queues (CAP3-KA6)",
      "HW: Homework 1.4.2; prep CAP3/KA6 with the 1.4 Organiser.\nConsolidation: Quiz 2.2.1; Workbook 2 stack and queue classes.",
      hw("1.4.2") + qz("2.2.1") + [KO(T14, "1.4")]),
     ("Week 19 (01 Feb) - Review week - implementing data structures",
      "HW: implement a linked list, stack and queue in Python (Workbook 2).\nConsolidation: Quiz 1.4.2; Mini-Paper 1.3 timed.",
      qz("1.4.2") + [MP(T13, "1.3"), MPA(T13, "1.3")]),
     ("Week 20 (08 Feb) - 1.4.2 Graphs, trees, hash tables (CAP3 due)",
      "HW: finish Homework 1.4.2 redos; BST + hash table in Python.\nConsolidation: Revision Notes 1.4.2.",
      [RN(s["1.4.2"])]),
     ("Half Term 2 (15 Feb)",
      "Finish any data-structure implementation. Flashcards 1.4 + one earlier Mini-Paper.",
      [FC(T14, "1.4")]),
     ("Week 21 (22 Feb) - 1.4.3 Boolean logic (KA7)",
      "HW: Homework 1.4.3 Part A; prep KA7.\nConsolidation: Quiz 1.4.3 Section A; truth-table drills from Worksheet 1.4.",
      hw("1.4.3") + qz("1.4.3")),
     ("Week 22 (01 Mar) - Component 3 PyGame (KA7 feedback)",
      "HW: PyGame tasks; act on KA7 feedback.\nConsolidation: full Quiz 1.4.3; Flashcards 1.4.",
      [FC(T14, "1.4")]),
     ("Week 23 (08 Mar) - 1.4.3 Karnaugh maps (SOW Recap 1.2 slot)",
      "HW: finish Homework 1.4.3; K-map and De Morgan drills from Worksheet 1.4.\nConsolidation: Mini-Paper 1.2 + Organiser 1.2 cover-recall.",
      [MP(T12, "1.2"), MPA(T12, "1.2"), KO(T12, "1.2")]),
     ("Week 24 (15 Mar) - Review week - CAP4-KA8 + 2.1.5 (SOW Recap 1.3 slot)",
      "HW: Homework 2.1.5; prep CAP4/KA8 (cumulative 1.1-1.4 + 2.1).\nConsolidation: RECAP CHECKPOINT 3 (1.1-1.4) timed; Mini-Paper 1.3.",
      hw("2.1.5") + [RC(R3, "Recap 3 (1.1-1.4)"), RCA(R3, "Recap 3 (1.1-1.4)"), MP(T13, "1.3"), MPA(T13, "1.3")]),
     ("Week 25 (22 Mar) - PyGame (SOW Recap 1.4 slot, CAP4 due)",
      "HW: PyGame workbook; act on CAP4/KA8 feedback.\nConsolidation: Mini-Paper 1.4 + Reference-Sheet drills.",
      [MP(T14, "1.4"), MPA(T14, "1.4")]),
     ("Easter Holidays",
      "Mock Paper 1 a section at a time, self-marked. Re-RAG the PLC.",
      [M1, M1A]),
     ("Week 26 (12 Apr) - Mock revision",
      "HW: sit remaining Mock Paper 1 sections timed; keep an error log.\nConsolidation: weakest PLC rows via their quizzes; Exam Technique + Command Words guides (Reference Guides).",
      [M1B, M1BA]),
     ("Week 27 (19 Apr) - MOCK WEEK (CAP5)",
      "Light week: skim the Glossary and Common Mistakes guides; rest before the mock.",
      []),
     ("Week 28 (26 Apr) - Mock feedback",
      "HW: re-attempt your two weakest mock questions in full.\nConsolidation: flashcards on the weakest topics; update the PLC from mock results.",
      []),
     ("Week 29 (03 May) - Mini-NEA Analysis (CAP5 due 7 May)",
      "HW: NEA Template section 1 - stakeholder, requirements, measurable success criteria.\nConsolidation: NEA Guide checklist; 10 min per day flashcards.",
      [NEA]),
     ("Week 30 (10 May) - Mini-NEA Analysis",
      "HW: complete the Analysis write-up.\nConsolidation: peer-review a partner's analysis against the NEA checklist.", []),
     ("Week 31 (17 May) - Mini-NEA Design",
      "HW: NEA Template section 2 - decomposition, algorithms, data structures, UI.\nConsolidation: check each design decision traces to a requirement.", []),
     ("Week 32 (24 May) - Mini-NEA Design",
      "HW: complete section 2 + the test plan (typical, boundary, erroneous).\nConsolidation: review against the Design checklist.", []),
     ("Half Term 3 (31 May)",
      "Finish the design so implementation starts clean. Light flashcard retrieval.", []),
     ("Week 33 (07 Jun) - Mini-NEA Implementation",
      "HW: NEA Template section 3 - iterative build, annotated evidence, tests per iteration.\nConsolidation: keep the development log as you go.", []),
     ("Week 34 (14 Jun) - Mini-NEA Implementation (review week)",
      "HW: continue section 3; add validation and robustness.\nConsolidation: file-check prep - all code evidence annotated.", []),
     ("Week 35 (21 Jun) - Mini-NEA Evaluation",
      "HW: NEA Template section 4 - test against every success criterion; stakeholder feedback.\nConsolidation: map every evaluation point back to the Analysis.", []),
     ("Week 36 (28 Jun) - Mini-NEA Evaluation",
      "HW: complete section 4 + justified improvements.\nConsolidation: final NEA checklist; set VESPA targets for Year 13.", []),
    ]


def build_weekly():
    wk_root = os.path.join(COURSE, "7 Weekly Plan - Homework and Consolidation (Year 12)")
    for folder, note, files in _wk_sources():
        d = os.path.join(wk_root, folder)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "0 This Week.txt"), "w", encoding="utf-8") as f:
            f.write(folder + "\n\n" + note.replace("\\n", "\n") + "\n")
        for src, dst in files:
            cp(src, os.path.join(d, dst))


if __name__ == "__main__":
    build()
