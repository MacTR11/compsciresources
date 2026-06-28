# OCR A Level Computer Science (H446) — Complete Revision Hub

A full, spec-mapped revision system for **OCR A Level Computer Science, specification H446** (first assessment 2017). Built to do two things: **get every student a secure pass**, and **push able students to A\*** by targeting the application (AO2) and evaluation (AO3) marks where top grades are decided.

> ⚠️ **Accuracy:** all content is mapped to the published H446 specification and has been audited to remove off-spec material. It is a study aid, **not** a substitute for the official OCR specification, past papers and mark schemes — always cross-check those.

---

## 📥 Download & use (editable Word, Excel & PDF)

**Everything is available as a real, downloadable, editable file** — you don't need to read the Markdown.

| Format | Where | Use it for |
|--------|-------|-----------|
| 📝 **Word (.docx)** | [`Word-Documents/`](Word-Documents/) | Every guide, organiser, worksheet, quiz, mini/mock paper, A\* pack, workbook & NEA guide — **open & edit in Word or Google Docs** (86 documents) |
| 📊 **Excel (.xlsx)** | [`Spreadsheets/`](Spreadsheets/) | **Flashcards** (8 tabs), an **interactive RAG tracker** (dropdowns + auto-colour + live counts) and the **scheme-of-work** plan |
| ✂️ **Print-and-cut cards (PDF)** | [`revision-tools/printable-pdfs/revision-games-cards/`](revision-tools/printable-pdfs/revision-games-cards/) | The revision games as **actual cards to print and cut out** (loop cards, Taboo, bingo, Top Trumps, card sorts) |
| 🖨️ **Printable PDFs** | [`revision-tools/printable-pdfs/`](revision-tools/printable-pdfs/) | Print-ready quizzes, worksheets, organisers, mini/mock papers |

> The `.md` files under `component-*/` and `revision-tools/` are just the **source** used to generate the files above — you can ignore them. To regenerate after editing a source file: `build-docx.py` (Word), `build-spreadsheets.py` (Excel), `build-pdfs.py` / `build-card-games.py` (PDF), all in `revision-tools/`.

---

## 🚀 Start here

1. **New to the repo?** Read [how the qualification is assessed](#-how-the-qualification-is-assessed) below.
2. **Diagnose** your gaps with the [RAG self-assessment tracker](revision-tools/guides/self-assessment-tracker.md).
3. **Plan** your weeks with the [study plan](revision-tools/guides/study-plan-and-how-to-use.md).
4. Then follow the [recommended route to A\*](#-recommended-route-to-a) — learn → condense → recall → practise → exam.

**Just want to revise right now?** Grab a [Word document](Word-Documents/), open the [interactive tracker/flashcards](Spreadsheets/), or print a [card game](revision-tools/printable-pdfs/revision-games-cards/) / [PDF](revision-tools/printable-pdfs/).

---

## 📐 How the qualification is assessed

Take **three components**: 01, 02 and **either** 03 **or** 04.

| Component | Title | Format | Duration | Marks | Weighting |
|-----------|-------|--------|----------|-------|-----------|
| **H446/01** | Computer Systems | Written exam | 2h 30m | 140 | **40%** |
| **H446/02** | Algorithms & Programming | Written exam | 2h 30m | 140 | **40%** |
| **H446/03 or 04** | Programming Project (NEA) | Coursework | — | 70 | **20%** |

**Assessment Objectives:** **AO1** knowledge (~35%) · **AO2** apply (~30%) · **AO3** design/program/evaluate (~35%). AO1 alone caps you near a pass; **AO2/AO3 decide A vs A\*** — so most practice here is deliberately application-heavy. See [command words & AOs](revision-tools/guides/command-words-and-assessment-objectives.md).

---

## 📚 The specification content

### Component 01 — Computer Systems · [overview & checklist](component-01-computer-systems/README.md)
| Spec | Topic |
|------|-------|
| 1.1 | [Processors, input, output & storage](component-01-computer-systems/1.1-processors-input-output-storage.md) |
| 1.2 | [Software & software development](component-01-computer-systems/1.2-software-and-software-development.md) |
| 1.3 | [Exchanging data](component-01-computer-systems/1.3-exchanging-data.md) |
| 1.4 | [Data types, structures & Boolean algebra](component-01-computer-systems/1.4-data-types-structures-boolean-algebra.md) |
| 1.5 | [Legal, moral, cultural & ethical issues](component-01-computer-systems/1.5-legal-moral-cultural-ethical.md) |

### Component 02 — Algorithms & Programming · [overview & checklist](component-02-algorithms-and-programming/README.md)
| Spec | Topic |
|------|-------|
| 2.1 | [Elements of computational thinking](component-02-algorithms-and-programming/2.1-elements-of-computational-thinking.md) |
| 2.2 | [Problem solving & programming](component-02-algorithms-and-programming/2.2-problem-solving-and-programming.md) |
| 2.3 | [Algorithms](component-02-algorithms-and-programming/2.3-algorithms.md) |

### Component 03/04 — Programming Project (NEA)
- [How to score full marks on the project](component-03-04-programming-project/README.md)

---

## 🧰 The revision toolkit — by purpose

All tools live in [`revision-tools/`](revision-tools/README.md) (full catalogue there). Grouped by what you'd use them for:

### 🧭 Plan & technique — [`guides/`](revision-tools/guides/)
- [Study plan & how to use this hub](revision-tools/guides/study-plan-and-how-to-use.md)
- [Command words & assessment objectives](revision-tools/guides/command-words-and-assessment-objectives.md)
- [Exam technique (incl. extended-response)](revision-tools/guides/exam-technique.md)
- [Common mistakes to avoid](revision-tools/guides/common-mistakes.md)
- [RAG self-assessment tracker](revision-tools/guides/self-assessment-tracker.md)

### 📖 Reference — [`guides/`](revision-tools/guides/)
- [Glossary (exam-ready definitions)](revision-tools/guides/glossary.md)
- [Reference sheet (number, Big O, logic, SQL)](revision-tools/guides/reference-sheet.md)
- [OCR pseudocode (Exam Reference Language) guide](revision-tools/guides/pseudocode-guide.md)
- [Diagram bank (CPU, networks, logic, trees, ER)](revision-tools/guides/diagram-bank.md)

### 🧠 Condense & recall
- [Knowledge organisers](revision-tools/knowledge-organisers/README.md) — one page per topic
- [Flashcard decks](revision-tools/flashcards/README.md) — Anki/Quizlet CSV (374 cards)
- [**Subtopic quizzes**](revision-tools/subtopic-quizzes/README.md) — a printable PDF quiz (with answer key) for **every** subtopic

### ✍️ Practise
- [Worksheets](revision-tools/worksheets/README.md) — hands-on, with answer keys
- [Revision games](revision-tools/revision-games/README.md) — loop cards, Taboo, bingo, Top Trumps
- [Programming workbook](revision-tools/programming-workbook/README.md) — graded coding challenges + solutions
- [Practice questions hub](revision-tools/practice-questions/README.md) — how to drill exam questions

### 📝 Exam practice
- [Topic mini-papers](revision-tools/mini-papers/README.md) — bite-size timed mocks (with mark schemes)
- [Full mock papers](revision-tools/mock-papers/README.md) — four 140-mark synoptic mocks (with mark schemes)

### 🎯 Stretch to A\*
- [A\* stretch pack](revision-tools/a-star-pack/README.md) — model answers, examiner insights, synoptic questions, topic-connections map

### 👩‍🏫 For teachers
- [Scheme of work — homework & consolidation](revision-tools/scheme-of-work/README.md) — week-by-week homework + spaced-retrieval consolidation tasks mapped to the Year 12 SOW (PDF + CSV)

### 🖨️ Printables
- [Printable PDFs](revision-tools/printable-pdfs/README.md) — 36 ready-to-print PDFs of the games, worksheets, organisers, mini-papers and mock papers

---

## 🎯 Recommended route to A\*

1. **Diagnose** — fill in the [RAG tracker](revision-tools/guides/self-assessment-tracker.md) (green = "I could teach it").
2. **Learn** — read the topic file for each Red/Amber area; rewrite key terms from memory.
3. **Condense** — make the [organiser](revision-tools/knowledge-organisers/README.md) stick; drill [flashcards](revision-tools/flashcards/README.md) and a [subtopic quiz](revision-tools/subtopic-quizzes/README.md).
4. **Practise** — [worksheets](revision-tools/worksheets/README.md), [games](revision-tools/revision-games/README.md) and (for Paper 2) the [programming workbook](revision-tools/programming-workbook/README.md).
5. **Exam** — [mini-papers](revision-tools/mini-papers/README.md) → [full mocks](revision-tools/mock-papers/README.md) → official past papers, all timed and marked.
6. **Top band** — work the [A\* pack](revision-tools/a-star-pack/README.md): justify, compare, evaluate, connect topics.
7. **Re-RAG** and repeat on what's still weak.

---

## 🗺️ Directory map

```
README.md                          ← you are here (master index)
component-01-computer-systems/      ← 1.1–1.5 topic guides + overview
component-02-algorithms-and-programming/  ← 2.1–2.3 topic guides + overview
component-03-04-programming-project/      ← NEA project guide
revision-tools/                     ← all study tools (see its README)
├── guides/                ← strategy & reference (study plan, technique, glossary, pseudocode, diagrams…)
├── knowledge-organisers/  ← one-page topic summaries
├── flashcards/            ← CSV decks (Anki/Quizlet)
├── subtopic-quizzes/      ← a printable quiz for every subtopic (+ answer keys)
├── worksheets/            ← printable practice + answer keys
├── revision-games/        ← printable games
├── mini-papers/           ← short topic mocks + mark schemes
├── mock-papers/           ← full 140-mark mocks + mark schemes
├── programming-workbook/  ← coding challenges + solutions
├── a-star-pack/           ← top-grade technique & synoptic
├── practice-questions/    ← question-drilling guide
├── printable-pdfs/        ← 36 print-ready PDFs
└── build-pdfs.py          ← regenerate the PDFs
```

---

## ✅ What each topic guide contains
Spec checklist · clear recap notes · **💡 A\* extension** boxes · worked examples/traces · exam-ready definitions · common mistakes & examiner tips · **exam-style questions with full mark schemes** · a RAG grid.

Work actively — retrieve, don't re-read. Good luck. 🎓
