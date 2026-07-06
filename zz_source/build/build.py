#!/usr/bin/env python3
"""
THE build command. Regenerates everything from zz_source/ in one run:

    python3 zz_source/build/build.py            # full build + assemble + validate
    python3 zz_source/build/build.py --fast     # skip PDFs/decks (docx-only iteration)

Order: PDFs -> Word -> PowerPoints -> game cards -> spreadsheets -> markbook
-> PLC -> assemble (atomic swap into the six top-level folders) -> validate.
Stops at the first failure; the assembled tree is only replaced if every
source built and every expected file was found.
"""
import os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = [
    ("build-pdfs.py", False),
    ("build-docx.py", True),
    ("build-powerpoints.py", False),
    ("build-card-games.py", False),
    ("build-spreadsheets.py", True),
    ("build-markbook.py", True),
    ("build-plc.py", True),
    ("assemble.py", True),
    ("validate.py", True),
]


def main():
    fast = "--fast" in sys.argv
    for script, always in STEPS:
        if fast and not always:
            print(f"== {script} (skipped, --fast)")
            continue
        print(f"== {script}")
        r = subprocess.run([sys.executable, os.path.join(HERE, script)])
        if r.returncode != 0:
            sys.exit(f"BUILD FAILED at {script} (exit {r.returncode})")
    print("\nBuild complete.")


if __name__ == "__main__":
    main()
