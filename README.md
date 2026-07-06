# OCR A Level Computer Science (H446) — Year 12 Course Pack

A complete, week-first resource bank for teaching OCR H446, built around the Year 12
scheme of work. Word-editable everything; print PDFs only where you hand out a formal
paper. **Open the folder for the week you are teaching — everything you need is in it.**

| Folder | What's inside |
|---|---|
| **0 Planning** | The master SOW (Excel + editable Word), Markbook (KA/CAP tracking), Personal Learning Checklist, all-topics flashcards workbook |
| **1 Year 12 Weekly** | THE spine — one folder per SOW week: lesson deck(s), class retrieval quiz + answers, homework + answers, consolidation tasks, cumulative flashcard bank |
| **2 Topic Library** | Revision by spec topic: knowledge organiser, full notes, per-subtopic revision notes, end-of-topic worksheet, timed mini-paper, flashcards, revision game, lesson activities |
| **3 Assessments - TEACHER ONLY** | Week-1 diagnostic, the KA/CAP assessment map, recap checkpoints, mock papers (incl. the unseen Week-27 mock). Keep out of student shares. |
| **4 NEA and Programming** | NEA guide + project template, Programming Workbooks 1–2, PyGame Workbook (weeks 22–28), Mini-NEA Pack (weeks 29–36) |
| **5 Reference and Stretch** | Glossary, exam technique, pseudocode guide, diagram bank, past-papers guide, A* stretch pack |

`START HERE.docx` is the one-page guide for students. `INDEX.md` lists every file.

## How the week works

1. **Teach** from `1 Lesson <subtopic>.pptx`.
2. **Retrieve** with `2 Class Quiz` — always on *last* week's subtopic, sat closed book.
3. **Set** `3 Homework` (typeable Word; separate answers file for you).
4. **Consolidate** with `4 Consolidation` — instructions plus any scheduled recap
   checkpoint / mini-paper for that week, included in the folder.
5. `5 Flashcards (cumulative)` holds every card for everything taught so far.

Assessment points (Diagnostic, KA1–8, CAP1–5, EOY quiz, Week-27 mock) are defined in
`3 Assessments - TEACHER ONLY/0 Assessment Map`, pre-aligned with the Markbook.

## Rebuilding

Everything is generated from the Markdown/JSON sources in `zz_source/`. To change any
resource, edit its source and run:

```
python3 zz_source/build/build.py
```

One command: builds PDFs, Word, PowerPoints, game cards and spreadsheets to a hidden
staging area, assembles the six folders above atomically (the old tree is only replaced
if every file built), then runs a mechanical validation gate over every output.
The week-by-week plan lives in **one** place: `zz_source/sow/year12.json`.

## The qualification at a glance

**Paper 1** Computer Systems (2h30, 140 marks, 40%) · **Paper 2** Algorithms &
Programming (2h30, 140 marks, 40%) · **NEA** Programming Project (70 marks, 20%).
AO2/AO3 decide A vs A\* — the practice material is deliberately weighted that way.

> ⚠️ Original material mapped to the published H446 specification. Not a substitute for
> OCR's official specification, past papers and mark schemes — the **Past Papers Guide**
> in `5 Reference and Stretch/` indexes every published series.
