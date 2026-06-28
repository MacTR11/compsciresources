# Printable PDFs

Ready-to-print **PDF** versions of every resource — for handing out, printing, or studying offline.

> 📄 **Every question resource comes as two files:** a **worksheet** (`<name>.pdf`) with the questions and **ruled space to write/type answers**, and a **separate answer sheet** (`<name>-ANSWERS.pdf`) with the mark scheme. Print the worksheet for students; keep the answer sheet for marking or self-assessment.

## What's here
| Folder | Contents |
|--------|----------|
| [subtopic-quizzes/](subtopic-quizzes/) | Quiz **+ answer sheet** for all 24 subtopics |
| [worksheets/](worksheets/) | 8 worksheets **+ answer sheets** |
| [mini-papers/](mini-papers/) | 8 topic mini-papers **+ answer sheets** |
| [mock-papers/](mock-papers/) | 4 full 140-mark mock papers **+ answer sheets** |
| [knowledge-organisers/](knowledge-organisers/) | 8 one-page organisers (reference — no answers) |
| [revision-games/](revision-games/) | 8 revision-game packs; see also [`revision-games-cards/`](revision-games-cards/) for print-and-cut cards |
| [revision-games-cards/](revision-games-cards/) | ✂️ print-and-cut card decks (loop cards, Taboo, bingo, Top Trumps) |
| [scheme-of-work/](scheme-of-work/) | Year 12 weekly homework & consolidation plan |

> ✂️ **Tip for games:** the loop cards / Taboo cards are laid out to print and cut out. Print double-sided to save paper; card stock makes sturdier cards.

## Regenerating the PDFs
The PDFs are generated from the Markdown sources with [`build-pdfs.py`](../build/build-pdfs.py) (Markdown → HTML → PDF via headless Chromium). If you edit a source `.md`, rebuild:
```bash
python3 build/build-pdfs.py                       # rebuild the default set
python3 build/build-pdfs.py <src-folder> <out-folder>   # one folder
```
Requires `python-markdown` (`pip install markdown`) and a Chromium/Chrome binary (auto-detected, or set the `CHROME` env var).
