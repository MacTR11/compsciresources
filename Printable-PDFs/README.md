# Printable PDFs

Ready-to-print **PDF** versions of the printable resources — for handing out, printing, or studying offline without rendering Markdown.

## What's here
| Folder | Contents |
|--------|----------|
| [scheme-of-work/](scheme-of-work/) | Year 12 weekly homework & consolidation plan |
| [subtopic-quizzes/](subtopic-quizzes/) | A printable quiz (with answer key) for all 24 subtopics |
| [revision-games/](revision-games/) | The 8 revision-game packs (loop cards, Taboo, bingo, etc.) |
| [worksheets/](worksheets/) | The 8 printable worksheets (with answer keys) |
| [knowledge-organisers/](knowledge-organisers/) | The 8 one-page knowledge organisers |
| [mini-papers/](mini-papers/) | The 8 topic mini-papers (with mark schemes) |
| [mock-papers/](mock-papers/) | The 4 full 140-mark mock papers (with mark schemes) |

That's **36 PDFs** covering every printable resource.

> ✂️ **Tip for games:** the loop cards / Taboo cards are laid out to print and cut out. Print double-sided to save paper; card stock makes sturdier cards.

## Regenerating the PDFs
The PDFs are generated from the Markdown sources with [`build-pdfs.py`](../build/build-pdfs.py) (Markdown → HTML → PDF via headless Chromium). If you edit a source `.md`, rebuild:
```bash
python3 build/build-pdfs.py                       # rebuild the default set
python3 build/build-pdfs.py <src-folder> <out-folder>   # one folder
```
Requires `python-markdown` (`pip install markdown`) and a Chromium/Chrome binary (auto-detected, or set the `CHROME` env var).
