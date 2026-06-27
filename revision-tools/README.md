# Revision Tools — Catalogue

Everything here supports the [topic guides](../README.md#-the-specification-content). Tools are grouped by **what you'd use them for**. New here? Start with the [study plan](guides/study-plan-and-how-to-use.md) and the [self-assessment tracker](guides/self-assessment-tracker.md).

---

## 🧭 Plan & technique — [`guides/`](guides/)
| Tool | Use it to… |
|------|-----------|
| [Study plan & how to use this hub](guides/study-plan-and-how-to-use.md) | Build a spaced, active revision schedule |
| [Command words & assessment objectives](guides/command-words-and-assessment-objectives.md) | Decode what each question actually wants |
| [Exam technique](guides/exam-technique.md) | Pace the paper; nail extended-response questions |
| [Common mistakes](guides/common-mistakes.md) | Stop throwing away easy marks |
| [Self-assessment tracker (RAG)](guides/self-assessment-tracker.md) | Diagnose and prioritise weak topics |

## 📖 Reference — [`guides/`](guides/)
| Tool | Use it to… |
|------|-----------|
| [Glossary](guides/glossary.md) | Drill exam-ready definitions |
| [Reference sheet](guides/reference-sheet.md) | Look up number/Big O/logic/SQL facts |
| [Pseudocode guide](guides/pseudocode-guide.md) | Write OCR Exam Reference Language correctly |
| [Diagram bank](guides/diagram-bank.md) | Study/redraw key diagrams |

## 🧠 Condense & recall
| Tool | What it is |
|------|-----------|
| [Knowledge organisers](knowledge-organisers/README.md) | One-page summary per topic |
| [Flashcards](flashcards/README.md) | 374 cards, Anki/Quizlet-ready CSV |
| [Subtopic quizzes](subtopic-quizzes/README.md) | A printable quiz (with answer key) for **every** subtopic — also in [PDF](printable-pdfs/README.md) |

## ✍️ Practise
| Tool | What it is |
|------|-----------|
| [Worksheets](worksheets/README.md) | Hands-on practice + answer keys |
| [Revision games](revision-games/README.md) | Loop cards, Taboo, bingo, Top Trumps |
| [Programming workbook](programming-workbook/README.md) | Graded coding challenges + solutions |
| [Practice questions hub](practice-questions/README.md) | How to drill exam questions effectively |

## 📝 Exam practice
| Tool | What it is |
|------|-----------|
| [Mini-papers](mini-papers/README.md) | 8 short timed topic mocks + mark schemes |
| [Mock papers](mock-papers/README.md) | 4 full 140-mark synoptic mocks + mark schemes |

## 🎯 Stretch to A\*
| Tool | What it is |
|------|-----------|
| [A\* stretch pack](a-star-pack/README.md) | Model answers, examiner insights, synoptic questions, connections map |

## 🖨️ Print & build
| Item | What it is |
|------|-----------|
| [Printable PDFs](printable-pdfs/README.md) | 36 ready-to-print PDFs (games, worksheets, organisers, mini-papers, mocks) |
| [`build-pdfs.py`](build-pdfs.py) | Regenerate the PDFs from the Markdown sources |

---

### Regenerating generated assets
```bash
# Rebuild the printable PDFs (after editing any printable Markdown)
python3 revision-tools/build-pdfs.py
```
Requires `python-markdown` (`pip install markdown`) and a Chromium/Chrome binary for PDFs.
