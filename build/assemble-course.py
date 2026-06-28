#!/usr/bin/env python3
"""
Assemble the flat build outputs (Word-Documents/, Printable-PDFs/,
Teacher-Toolkit/, Spreadsheets/) into a single teaching-organised tree:

    Course/Component N/<Topic>/00 Topic Resources/   (topic-wide resources)
    Course/Component N/<Topic>/<Subtopic>/           (lesson, worksheet, homework)
    Course/Recap Checkpoints/
    Teacher Toolkit/
    Reference/

Run the build-* scripts first, then this. The flat output folders are
regeneration staging (git-ignored); this organised tree is what's kept.
"""
import os, shutil, glob

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WD = os.path.join(REPO, "Word-Documents")
PDF = os.path.join(REPO, "Printable-PDFs")
TT = os.path.join(REPO, "Teacher-Toolkit")
XL = os.path.join(REPO, "Spreadsheets")
SRC = os.path.join(REPO, "source", "revision-tools")
COURSE = os.path.join(REPO, "Course")

missing = []


def cp(src, dst):
    if not os.path.exists(src):
        missing.append(os.path.relpath(src, REPO)); return
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)


# (Component folder, [ (Topic folder, topic-stem, [(Subtopic folder, sub-stem)...]) ])
STRUCTURE = [
 ("Component 1 - Computer Systems", [
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
 ("Component 2 - Algorithms and Programming", [
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

# component number by folder name
COMP_WD = {"Component 1 - Computer Systems": "01-Computer-Systems",
           "Component 2 - Algorithms and Programming": "02-Algorithms-and-Programming"}


def build():
    if os.path.isdir(COURSE):
        shutil.rmtree(COURSE)
    for comp, topics in STRUCTURE:
        for tname, tstem, subs in topics:
            tdir = os.path.join(COURSE, comp, tname)
            tr = os.path.join(tdir, "00 Topic Resources")
            # topic-wide
            cp(os.path.join(PDF, "knowledge-organisers", f"{tstem}.pdf"), os.path.join(tr, "Knowledge Organiser.pdf"))
            cp(os.path.join(WD, "Knowledge-Organisers", f"{tstem}.docx"), os.path.join(tr, "Knowledge Organiser.docx"))
            cp(os.path.join(WD, COMP_WD[comp], f"{tstem}.docx"), os.path.join(tr, "Revision Notes (full topic).docx"))
            cp(os.path.join(SRC, "flashcards", f"{tstem}.csv"), os.path.join(tr, "Flashcards.csv"))
            cp(os.path.join(PDF, "revision-games", f"{tstem}.pdf"), os.path.join(tr, "Revision Game (how to play).pdf"))
            cp(os.path.join(PDF, "revision-games-cards", f"{tstem}-cards.pdf"), os.path.join(tr, "Revision Game - Print and Cut Cards.pdf"))
            cp(os.path.join(PDF, "worksheets", f"{tstem}.pdf"), os.path.join(tr, "End-of-Topic Worksheet.pdf"))
            cp(os.path.join(PDF, "worksheets", f"{tstem}-ANSWERS.pdf"), os.path.join(tr, "End-of-Topic Worksheet - ANSWERS.pdf"))
            cp(os.path.join(WD, "Worksheets", f"{tstem}.docx"), os.path.join(tr, "End-of-Topic Worksheet (editable).docx"))
            cp(os.path.join(PDF, "mini-papers", f"{tstem}.pdf"), os.path.join(tr, "Topic Mini-Paper.pdf"))
            cp(os.path.join(PDF, "mini-papers", f"{tstem}-ANSWERS.pdf"), os.path.join(tr, "Topic Mini-Paper - ANSWERS.pdf"))
            # subtopics
            for sname, sstem in subs:
                sd = os.path.join(tdir, sname)
                cp(os.path.join(TT, "Lesson-PowerPoints", f"{sstem}.pptx"), os.path.join(sd, "Lesson (PowerPoint).pptx"))
                cp(os.path.join(PDF, "subtopic-quizzes", f"{sstem}.pdf"), os.path.join(sd, "Worksheet.pdf"))
                cp(os.path.join(PDF, "subtopic-quizzes", f"{sstem}-ANSWERS.pdf"), os.path.join(sd, "Worksheet - ANSWERS.pdf"))
                cp(os.path.join(WD, "Subtopic-Quizzes", f"{sstem}.docx"), os.path.join(sd, "Worksheet (editable).docx"))
                cp(os.path.join(PDF, "homework", f"{sstem}.pdf"), os.path.join(sd, "Homework.pdf"))
                cp(os.path.join(PDF, "homework", f"{sstem}-ANSWERS.pdf"), os.path.join(sd, "Homework - ANSWERS.pdf"))
                cp(os.path.join(WD, "Homework", f"{sstem}.docx"), os.path.join(sd, "Homework (editable).docx"))

    # Component 3
    c3 = os.path.join(COURSE, "Component 3 - Programming Project")
    cp(os.path.join(WD, "03-04-Programming-Project", "Programming-Project-NEA-Guide.docx"), os.path.join(c3, "NEA Guide.docx"))
    for f in glob.glob(os.path.join(WD, "Programming-Workbook", "*.docx")):
        nice = os.path.splitext(os.path.basename(f))[0].replace("-", " ").title() + ".docx"
        cp(f, os.path.join(c3, nice))

    # Recap checkpoints
    rc = os.path.join(COURSE, "Recap Checkpoints")
    for f in sorted(glob.glob(os.path.join(PDF, "recap-checkpoints", "*.pdf"))):
        cp(f, os.path.join(rc, os.path.basename(f)))

    # Teacher Toolkit
    tk = os.path.join(REPO, "Teacher Toolkit")
    if os.path.isdir(tk): shutil.rmtree(tk)
    cp(os.path.join(TT, "Markbook", "H446-Markbook.xlsx"), os.path.join(tk, "Markbook.xlsx"))
    cp(os.path.join(TT, "Planning", "medium-term-plan.docx"), os.path.join(tk, "Lesson Plan (medium-term plan).docx"))
    cp(os.path.join(XL, "Scheme-of-Work-Homework-and-Consolidation.xlsx"), os.path.join(tk, "Scheme of Work - Homework and Consolidation.xlsx"))
    cp(os.path.join(XL, "Self-Assessment-Tracker.xlsx"), os.path.join(tk, "Self-Assessment Tracker (RAG).xlsx"))
    cp(os.path.join(XL, "Flashcards.xlsx"), os.path.join(tk, "Flashcards (all topics).xlsx"))
    for f in sorted(glob.glob(os.path.join(WD, "A-Star-Pack", "*.docx"))):
        cp(f, os.path.join(tk, "A-Star Pack", os.path.basename(f)))

    # Reference (course-wide guides)
    ref = os.path.join(REPO, "Reference")
    if os.path.isdir(ref): shutil.rmtree(ref)
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

    print("Assembled Course/, Teacher Toolkit/, Reference/.")
    course_files = sum(len(fs) for _, _, fs in os.walk(COURSE))
    print(f"Course files: {course_files}")
    if missing:
        print(f"\n{len(missing)} expected source(s) missing (run all build-* scripts first):")
        for m in missing[:20]:
            print("  -", m)


if __name__ == "__main__":
    build()
