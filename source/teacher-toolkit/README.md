# Teacher Toolkit

Ready-to-use teaching resources for OCR H446, on top of the student-facing revision materials. The usable outputs live in **`Teacher-Toolkit/`** at the repo root:

| Resource | Where | What it is |
|----------|-------|-----------|
| 🖥️ **Lesson PowerPoints** | `Teacher-Toolkit/Lesson-PowerPoints/` | **24 editable `.pptx` decks** — one per subtopic. Each has objectives, a Do-Now retrieval starter (with answers), key terms, content slides, a worked example, a task + stretch challenge, and an exit ticket (with answers). |
| 📒 **Markbook** | `Teacher-Toolkit/Markbook/H446-Markbook.xlsx` | Interactive markbook for **KA1–8 + CAP1–5**: enter max marks + raw marks → auto percentage, **grade** (editable boundaries) and **class averages**, with RAG colour. |
| 🗺️ **Medium-term plan** | `Teacher-Toolkit/Planning/` | Week-by-week map of the SOW → which lesson deck to teach, which practice resources, and the assessment points. |

Also useful for planning: the **Scheme-of-Work homework & consolidation** spreadsheet (`Spreadsheets/`) and the student resources in `Word-Documents/` and `Printable-PDFs/`.

## Regenerating
```bash
python3 build/build-powerpoints.py   # lesson decks (from source/teacher-toolkit/deck-data/*.json)
python3 build/build-markbook.py      # markbook xlsx
python3 build/build-docx.py source/teacher-toolkit Teacher-Toolkit/Planning   # the plan as DOCX
```
