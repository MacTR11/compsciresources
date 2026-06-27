# Interactive Revision Hub (offline)

A clickable, **offline** web app combining the flashcard decks and self-marking multiple-choice quizzes for every H446 topic — flip cards, take quizzes, and track your best score per topic. No install, no internet.

## How to use it
1. Download/clone this repo.
2. Open **`index.html`** in any web browser (double-click it).
3. Pick a topic from the dropdown, choose **🃏 Flashcards** or **✅ Quiz**, and go.

Best scores are saved in your browser (localStorage), so you can see yourself improve.

### Features
- **🎲 All topics (mixed)** — interleaves flashcards/quizzes from *every* topic (interleaving is the most effective way to revise). Mixed quizzes are a random 20-question set.
- **Self-marking quizzes** with instant feedback, explanations, and a live running score.
- **Keyboard control** — Flashcards: `Space` flip, `←/→` previous/next, `S` shuffle. Quiz: `1–4` to answer, `Space` for next.
- **Per-topic best scores** saved locally.

## Files
- `index.html` — the app (flashcards + quiz UI).
- `data.js` — bundled flashcards + quiz questions (generated; loaded by the app).
- `build_data.py` — regenerates `data.js` from the source decks/quizzes.

## Editing or adding questions
The app reads from `data.js`, which is built from:
- `../flashcards/*.csv` — the flashcard decks
- `../quizzes/*.json` — the quiz banks

After editing either, rebuild:
```bash
python3 revision-tools/interactive-quiz/build_data.py
```
Then refresh `index.html`.

> Why `data.js` and not direct file loading? Browsers block `fetch()` of local files from `file://`. Bundling the data into a `data.js` script means the hub works by simply opening the HTML file — no web server needed.
