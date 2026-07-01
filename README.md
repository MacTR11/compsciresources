# OCR A Level Computer Science (H446) — Teaching & Revision Resources

A complete, spec‑mapped resource bank for **OCR H446**, organised the way you teach it: **Component → Topic → Subtopic**, with every resource as a ready‑to‑use **PDF, Word, PowerPoint or Excel** file (no Markdown to wade through).

> ⚠️ Mapped to the published H446 specification and audited for off‑spec content. A study aid — always cross‑check the official OCR specification, past papers and mark schemes.

---

## 📂 What's here

### `Course/` — everything organised by Component → Topic → Subtopic
```
Course/
  Component 1 - Computer Systems/
    1.1 Processors, Input, Output and Storage/
      00 Topic Resources/        ← whole-topic resources:
          Knowledge Organiser (.pdf/.docx) · Revision Notes (.docx) · Flashcards (.csv)
          Revision Game + Print-and-Cut Cards (.pdf) · End-of-Topic Worksheet (+ANSWERS)
          Topic Mini-Paper (+ANSWERS)
      1.1.1 Structure and Function of the Processor/   ← per subtopic:
          Lesson (PowerPoint).pptx
          Revision Notes.pdf / .docx        ← one-page subtopic summary
          Worksheet.pdf  +  Worksheet - ANSWERS.pdf  +  Worksheet (editable).docx
          Homework.pdf   +  Homework - ANSWERS.pdf   +  Homework (editable).docx
      1.1.2 … / 1.1.3 … /
    1.2 … 1.5 …
  Component 2 - Algorithms and Programming/   (2.1–2.3)
  Component 3 - Programming Project/          (NEA guide + student NEA template + workbooks)
  Recap Checkpoints/   ← cumulative recap papers (+ANSWERS) for SOW review points
  00 START HERE …                             ← student guide to using it all
```
**Every worksheet, quiz, homework and paper comes as a worksheet (with ruled answer space) *and* a separate answer sheet.** Editable Word versions sit alongside the print‑ready PDFs.

### `Teacher Toolkit/`
- **Markbook.xlsx** — track KA1–8 + CAP1–5 → auto percentage, grade & class averages
- **Lesson Plan (medium‑term plan).docx** — week‑by‑week SOW → resources map
- **Scheme of Work – Homework and Consolidation.xlsx** — weekly homework + spaced‑retrieval plan
- **Self‑Assessment Tracker (RAG).xlsx** — dropdowns + auto‑colour + live counts
- **Personal Learning Checklist.xlsx** — every "I can…" objective (72) with RAG + progress counts
- **Flashcards (all topics).xlsx** · **A‑Star Pack/** (model answers, examiner insights, synoptic questions)

### `Reference/` — course‑wide guides (Word)
Glossary · Reference Sheet (number, Big O, logic, SQL) · Command Words & AOs · Exam Technique · Common Mistakes · Diagram Bank · OCR Pseudocode Guide · Study Plan.

### `source/` + `build/`
`source/` holds the editable Markdown/CSV/JSON the files are generated from; `build/` holds the scripts. You normally never need these.

---

## 📐 The qualification

| Component | Title | Exam | Marks | Weighting |
|-----------|-------|------|-------|-----------|
| **01** | Computer Systems | 2h 30m written | 140 | 40% |
| **02** | Algorithms & Programming | 2h 30m written | 140 | 40% |
| **03/04** | Programming Project (NEA) | coursework | 70 | 20% |

**AOs:** AO1 knowledge (~35%) · AO2 apply (~30%) · AO3 design/program/evaluate (~35%). AO2/AO3 decide A vs A\*, so the practice here is application‑heavy.

---

## 🧭 How a teacher uses it

- **Plan** with `Teacher Toolkit/Lesson Plan` + `Scheme of Work` (maps each SOW week to the exact files).
- **Teach** from the subtopic `Lesson (PowerPoint).pptx` (objectives, Do‑Now retrieval, content, worked example, task, exit ticket).
- **Set work** with each subtopic's `Worksheet` and `Homework` (hand out the worksheet, keep the answer sheet).
- **Recap** at SOW review points with `Course/Recap Checkpoints/` (cumulative, synoptic).
- **Assess & track** with `Teacher Toolkit/Markbook.xlsx` and the `Self‑Assessment Tracker`.
- **Stretch** with the `A‑Star Pack`; **reference** anything in `Reference/`.

---

## 🔧 Regenerating (optional)

Everything in `Course/`, `Teacher Toolkit/` and `Reference/` is generated from `source/`:
```bash
python3 build/build-docx.py          # Word
python3 build/build-pdfs.py          # PDFs (worksheet + answer sheet split)
python3 build/build-powerpoints.py   # lesson decks
python3 build/build-spreadsheets.py  # flashcards, tracker, SOW
python3 build/build-markbook.py      # markbook
python3 build/build-card-games.py    # print-and-cut cards
python3 build/assemble-course.py     # arrange all outputs into Course/ + Teacher Toolkit/ + Reference/
```
Requires `python-docx`, `python-pptx`, `openpyxl`, `markdown` and a Chromium/Chrome binary.
