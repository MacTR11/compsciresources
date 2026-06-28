# OCR A Level Computer Science (H446) — Complete Revision Resources

A full, spec‑mapped set of revision resources for **OCR A Level Computer Science (H446)** — built to secure passes and push able students to A\*. **Everything is a real, downloadable, editable or printable file** (Word, Excel, PDF); the Markdown is tucked away in `source/` as regeneration material.

> ⚠️ **Accuracy:** all content is mapped to the published H446 specification and audited to remove off‑spec material. It's a study aid, **not** a substitute for the official OCR specification, past papers and mark schemes.

---

## 📥 Download & use

| Folder | Format | What's in it |
|--------|--------|--------------|
| 📝 **[`Word-Documents/`](Word-Documents/)** | `.docx` (edit in Word / Google Docs) | **86 documents** — topic guides, knowledge organisers, worksheets, revision games, the **24 subtopic quizzes**, mini‑papers, mock papers, A\* pack, programming workbook, NEA guide, scheme of work |
| 📊 **[`Spreadsheets/`](Spreadsheets/)** | `.xlsx` (interactive) | **Flashcards** (8 tabs), an **interactive RAG tracker** (dropdowns + auto‑colour + live counts), the **scheme‑of‑work** plan |
| 🖨️ **[`Printable-PDFs/`](Printable-PDFs/)** | `.pdf` (print) | Every quiz, worksheet and mini/mock paper as a **worksheet (with ruled answer space) + a separate answer sheet**; plus organisers and **✂️ print‑and‑cut game cards** in [`revision-games-cards/`](Printable-PDFs/revision-games-cards/) |
| 👩‍🏫 **[`Teacher-Toolkit/`](Teacher-Toolkit/)** | `.pptx` / `.xlsx` / `.docx` | **24 editable lesson PowerPoints**, an **interactive markbook** (KA1–8 + CAP1–5 → auto grade & class averages), and a **lesson-by-lesson plan** mapped to the SOW |

`source/` holds the editable Markdown/CSV/JSON sources and `build/` the scripts that regenerate the files above.

---

## 📐 How the qualification is assessed

Three components: 01, 02 and **either** 03 **or** 04.

| Component | Title | Format | Duration | Marks | Weighting |
|-----------|-------|--------|----------|-------|-----------|
| **H446/01** | Computer Systems | Written exam | 2h 30m | 140 | **40%** |
| **H446/02** | Algorithms & Programming | Written exam | 2h 30m | 140 | **40%** |
| **H446/03 or 04** | Programming Project (NEA) | Coursework | — | 70 | **20%** |

**Assessment Objectives:** **AO1** knowledge (~35%) · **AO2** apply (~30%) · **AO3** design/program/evaluate (~35%). AO1 alone caps you near a pass; **AO2/AO3 decide A vs A\***, so the practice here is deliberately application‑heavy.

---

## 📚 What's covered

**Component 01 — Computer Systems:** 1.1 Processors, input/output & storage · 1.2 Software & software development · 1.3 Exchanging data · 1.4 Data types, data structures & Boolean algebra · 1.5 Legal, moral, cultural & ethical issues.

**Component 02 — Algorithms & Programming:** 2.1 Elements of computational thinking · 2.2 Problem solving & programming · 2.3 Algorithms.

**Component 03/04 — Programming Project (NEA).**

Every section has a topic guide, knowledge organiser, worksheet, flashcards, revision game and mini‑paper; **all 24 subtopics** have their own quiz; and there are 4 full 140‑mark mock papers. (Open the matching file in `Word-Documents/` or `Printable-PDFs/`.)

---

## 🗂️ Repository structure

```
README.md
Word-Documents/     ← editable Word versions of every resource (.docx)
Spreadsheets/       ← flashcards, interactive RAG tracker, scheme of work (.xlsx)
Printable-PDFs/     ← print-ready PDFs, incl. revision-games-cards/ (print & cut)
build/              ← scripts that regenerate the above
source/             ← Markdown / CSV / JSON sources
  ├─ component-01-computer-systems/        (1.1–1.5 topic guides)
  ├─ component-02-algorithms-and-programming/ (2.1–2.3)
  ├─ component-03-04-programming-project/  (NEA guide)
  └─ revision-tools/   (guides, knowledge-organisers, worksheets, revision-games,
                        subtopic-quizzes, mini-papers, mock-papers, a-star-pack,
                        programming-workbook, flashcards, scheme-of-work, …)
```

---

## 🎯 Recommended route to A\*

1. **Diagnose** — fill in the **RAG tracker** (`Spreadsheets/Self-Assessment-Tracker.xlsx`).
2. **Learn** — read the topic guide (Word/PDF) for each weak area; rewrite key terms from memory.
3. **Condense & recall** — knowledge organiser + flashcards (`Spreadsheets/Flashcards.xlsx`).
4. **Practise** — worksheets, print‑and‑cut **games**, programming workbook, **subtopic quizzes**.
5. **Exam** — mini‑papers → full mocks → official past papers, timed & marked.
6. **Top band** — the **A‑Star‑Pack** (model answers, examiner insights, synoptic questions).
7. **Re‑RAG** and repeat on what's still weak.

Teachers: the **scheme‑of‑work** spreadsheet gives weekly homework + spaced‑retrieval consolidation tasks mapped to the Year 12 SOW.

---

## 🔧 Regenerating the files

After editing anything in `source/`:

```bash
python3 build/build-docx.py          # Word documents
python3 build/build-spreadsheets.py  # Excel spreadsheets (flashcards, tracker, SOW)
python3 build/build-pdfs.py          # printable PDFs
python3 build/build-card-games.py    # print-and-cut game cards
python3 build/build-powerpoints.py   # teacher lesson decks (.pptx)
python3 build/build-markbook.py      # teacher markbook (.xlsx)
```
Requires `python-docx`, `openpyxl`, `python-pptx`, `markdown` (`pip install …`) and a Chromium/Chrome binary for PDFs.
