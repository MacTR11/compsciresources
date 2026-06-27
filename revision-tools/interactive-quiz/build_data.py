#!/usr/bin/env python3
"""
Bundle the flashcard CSVs and quiz JSONs into a single data.js that the
offline interactive hub (index.html) loads via a <script> tag — so the hub
works by simply double-clicking index.html, with no server and no internet.

Run this whenever you add or edit a flashcard deck or quiz:
    python3 revision-tools/interactive-quiz/build_data.py
"""
import json, glob, csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
RT = os.path.dirname(HERE)  # revision-tools/


def key(fn):
    return os.path.splitext(os.path.basename(fn))[0]


def main():
    flashcards = {}
    for f in sorted(glob.glob(os.path.join(RT, "flashcards", "*.csv"))):
        rows = [r for r in csv.reader(open(f, newline="", encoding="utf-8"))
                if len(r) >= 2 and r[0].strip()]
        flashcards[key(f)] = rows

    quizzes = {}
    for f in sorted(glob.glob(os.path.join(RT, "quizzes", "*.json"))):
        try:
            quizzes[key(f)] = json.load(open(f, encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise SystemExit(f"Invalid JSON in {f}: {e}")

    payload = {"flashcards": flashcards, "quizzes": quizzes}
    out = "window.H446_DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n"
    with open(os.path.join(HERE, "data.js"), "w", encoding="utf-8") as f:
        f.write(out)
    print(f"wrote data.js: {len(flashcards)} flashcard decks, {len(quizzes)} quizzes")


if __name__ == "__main__":
    main()
