# Flashcard Decks — Active Recall for Every Topic

Flashcards are the most efficient way to drill the **AO1 recall** (definitions, facts, processes) that underpins everything else — so you can spend exam time on the AO2/AO3 application that decides your grade. Each deck is a plain **CSV** you can import into **Anki**, **Quizlet**, or any flashcard app — or just read down the columns and self-test.

> Use [spaced repetition](../study-plan-and-how-to-use.md): review a deck, mark what you get wrong, and re-test it after 1 day → 1 week → 1 month. Recall beats re-reading.

---

## The decks

| Spec | Deck | Cards |
|------|------|-------|
| 1.1 | [Processors, input, output & storage](1.1-processors-input-output-storage.csv) | ~40 |
| 1.2 | [Software & software development](1.2-software-and-software-development.csv) | ~40 |
| 1.3 | [Exchanging data](1.3-exchanging-data.csv) | ~45 |
| 1.4 | [Data types, structures & Boolean](1.4-data-types-structures-boolean-algebra.csv) | ~45 |
| 1.5 | [Legal, moral & ethical](1.5-legal-moral-cultural-ethical.csv) | ~36 |
| 2.1 | [Computational thinking](2.1-elements-of-computational-thinking.csv) | ~34 |
| 2.2 | [Problem solving & programming](2.2-problem-solving-and-programming.csv) | ~42 |
| 2.3 | [Algorithms](2.3-algorithms.csv) | ~42 |

**Format:** each row is one card — `"front (question/term)","back (exam-precise answer)"`. There is **no header row**, so every line imports as a card. Fields are wrapped in double quotes and comma-separated.

---

## How to import

### Anki (free, best for spaced repetition)
1. **File → Import**, choose the `.csv`.
2. Set **Fields separated by: Comma**.
3. Tick **"Allow HTML in fields"** is optional; leave **"Fields separated by"** as Comma.
4. Map **Field 1 → Front**, **Field 2 → Back**. Choose/Create a deck (e.g. "H446 — 1.4").
5. Import. Then just do your daily reviews — Anki schedules the spacing for you.

### Quizlet
1. Create a new set → **Import**.
2. Paste the CSV contents (or upload).
3. Set the delimiter between term and definition to **Comma**, and between cards to **New line**.
4. If quotes show up around your text, switch the delimiter to **Tab** after opening the CSV in a spreadsheet and re-exporting, or remove the surrounding quotes — Quizlet sometimes keeps them; Anki does not.
5. Import and study.

### No app? Use a spreadsheet
Open the CSV in Excel/Google Sheets: column A = fronts, column B = backs. Cover column B and test yourself down the list.

---

## How to get the most from them

- **Produce, don't recognise.** Say/write the answer *before* flipping. Recognising the right answer is far weaker than recalling it.
- **Bury the easy ones, drill the hard ones.** In Anki, "Again/Hard" surfaces weak cards more often — be honest.
- **Two-way practice for definitions.** Cover the term and recall it from the definition too (great for exam wording).
- **Tie into your [RAG tracker](../self-assessment-tracker.md).** A deck you can recall cold = evidence to mark that sub-topic 🟢 Green.
- **Combine with the [mini-papers](../mini-papers/README.md).** Flashcards lock in the facts; mini-papers prove you can *apply* them under time.

---

### Want to extend a deck?
Just add lines in the same `"front","back"` format (no header). Keep each field on one line and double any internal quotes (`""`). Re-import to refresh.
