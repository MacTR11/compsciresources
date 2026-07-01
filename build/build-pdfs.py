#!/usr/bin/env python3
"""
Build print-ready PDFs from the Markdown revision resources.

Converts Markdown -> styled HTML (python-markdown) -> PDF (headless Chromium).
Designed for the printable handouts: revision games, worksheets, knowledge
organisers, mini-papers and mock papers.

Usage:
    python3 revision-tools/build-pdfs.py                # build the default set
    python3 revision-tools/build-pdfs.py <srcdir> <outdir>   # build one folder

Requires: python-markdown (pip install markdown) and the Chromium binary
(path auto-detected under /opt/pw-browsers, or set the CHROME env var).
"""
import sys, os, subprocess, tempfile, glob, re, shutil

try:
    import markdown
except ImportError:
    sys.exit("python-markdown not installed. Run: pip install markdown")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_chrome():
    if os.environ.get("CHROME") and os.path.exists(os.environ["CHROME"]):
        return os.environ["CHROME"]
    for pat in (
        "/opt/pw-browsers/chromium-*/chrome-linux/chrome",
        "/opt/pw-browsers/chromium-*/chrome-linux/headless_shell",
    ):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    for name in ("chromium", "chromium-browser", "google-chrome"):
        p = shutil.which(name)
        if p:
            return p
    sys.exit("No Chromium/Chrome binary found. Set the CHROME env var.")


CHROME = find_chrome()

CSS = """
@page { size: A4; margin: 14mm 12mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Segoe UI", Arial, sans-serif; font-size: 11pt;
       line-height: 1.4; color: #111; }
h1 { font-size: 19pt; border-bottom: 3px solid #2b6cb0; padding-bottom: 4px; color: #1a365d; }
h2 { font-size: 15pt; color: #2b6cb0; border-bottom: 1px solid #cbd5e0; padding-bottom: 2px;
     margin-top: 16px; page-break-after: avoid; }
h3 { font-size: 12.5pt; color: #2c5282; margin-top: 12px; page-break-after: avoid; }
h4 { font-size: 11.5pt; margin-top: 10px; page-break-after: avoid; }
p, li { orphans: 2; widows: 2; }
ul, ol { margin: 4px 0 8px 0; }
li { margin: 2px 0; page-break-inside: avoid; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 10pt;
        page-break-inside: avoid; }
th, td { border: 1px solid #999; padding: 4px 6px; text-align: left; vertical-align: top; }
th { background: #ebf4ff; }
tr:nth-child(even) td { background: #f7fafc; }
code { font-family: "DejaVu Sans Mono", Consolas, monospace; font-size: 9.5pt;
       background: #f0f0f0; padding: 1px 3px; border-radius: 3px; }
pre { background: #f6f8fa; border: 1px solid #ddd; border-radius: 5px; padding: 8px 10px;
      overflow-x: auto; page-break-inside: avoid; }
pre code { background: none; padding: 0; font-size: 9pt; }
blockquote { border-left: 4px solid #f6ad55; background: #fffaf0; margin: 8px 0;
             padding: 4px 12px; page-break-inside: avoid; }
hr { border: none; border-top: 2px dashed #cbd5e0; margin: 14px 0; }
details { display: block; border: 1px solid #cbd5e0; border-radius: 5px; padding: 6px 10px;
          margin: 6px 0; page-break-inside: avoid; background: #f7fafc; }
details > summary { font-weight: bold; }
details > summary ~ * { display: revert; }
strong { color: #1a202c; }
.answer-space { margin: 3px 0 12px; page-break-inside: avoid; }
.answer-space .rl { border-bottom: 1px solid #aab4c0; height: 8mm; }
.sheet-note { color: #2b6cb0; font-style: italic; font-size: 10pt; margin: 2px 0 10px; }
"""


# Folders whose resources are split into a worksheet + a separate answer sheet.
QA_FOLDERS = {"subtopic-quizzes", "worksheets", "mini-papers", "mock-papers",
              "homework", "recap-checkpoints"}
ANSWER_HEADING = re.compile(r"^\s*#{2,3}\s+(answer key|answers|mark scheme)", re.I)
MARK_TAG = re.compile(r"\[(\d+)\]|\((\d+)\s*marks?\)")


def md_to_html(md_text, title):
    md_text = re.sub(r"<details(?!\s+open)", "<details open", md_text)
    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    )
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>"
    )


def split_qa(text):
    """Split markdown at the first Answer key / Mark scheme heading."""
    lines = text.split("\n")
    for i, l in enumerate(lines):
        if ANSWER_HEADING.match(l):
            return "\n".join(lines[:i]).rstrip(), "\n".join(lines[i:]).strip()
    return text, None


def inject_answer_space(text):
    """After each question line (one carrying a [n] / (n marks) tag), add ruled
    writing space sized to the marks. Headings are skipped."""
    out = []
    for line in text.split("\n"):
        out.append(line)
        if line.lstrip().startswith("#"):
            continue
        tags = MARK_TAG.findall(line)
        if tags:
            nums = [int(x) for pair in tags for x in pair if x]
            marks = max(nums) if nums else 2
            n = min(12, max(2, round(marks * 1.4)))
            out.append("")
            out.append('<div class="answer-space">' + ('<div class="rl"></div>' * n) + "</div>")
            out.append("")
    return "\n".join(out)


def convert_text(md_text, title, pdf_path):
    html = md_to_html(md_text, title)
    fd, htmlfile = tempfile.mkstemp(suffix=".html")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(html)
    try:
        subprocess.run(
            [CHROME, "--headless", "--no-sandbox", "--disable-gpu",
             "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
             "file://" + htmlfile],
            check=True, capture_output=True,
        )
    finally:
        os.unlink(htmlfile)


def convert(md_path, pdf_path):
    with open(md_path, encoding="utf-8") as f:
        convert_text(f.read(), os.path.splitext(os.path.basename(md_path))[0], pdf_path)


def _h1(text):
    for l in text.split("\n"):
        if l.startswith("# "):
            return l[2:].strip()
    return "Worksheet"


def build_folder(srcdir, outdir):
    os.makedirs(outdir, exist_ok=True)
    folder = os.path.basename(srcdir.rstrip("/"))
    split = folder in QA_FOLDERS
    mds = sorted(f for f in glob.glob(os.path.join(srcdir, "*.md"))
                 if os.path.basename(f).lower() != "readme.md")
    made = 0
    for md in mds:
        base = os.path.splitext(os.path.basename(md))[0]
        with open(md, encoding="utf-8") as f:
            text = f.read()
        if split:
            questions, answers = split_qa(text)
            convert_text(inject_answer_space(questions), base,
                         os.path.join(outdir, base + ".pdf"))
            print(f"  {base}.pdf (worksheet)")
            made += 1
            if answers:
                title = _h1(text)
                a_doc = (f"# {title} — ANSWER SHEET\n\n"
                         f'<p class="sheet-note">Separate answer sheet / mark scheme — keep for marking.</p>\n\n'
                         + answers)
                convert_text(a_doc, base + "-ANSWERS",
                             os.path.join(outdir, base + "-ANSWERS.pdf"))
                print(f"  {base}-ANSWERS.pdf")
                made += 1
        else:
            convert(md, os.path.join(outdir, base + ".pdf"))
            print(f"  {base}.pdf")
            made += 1
    return made


# Default set: which Markdown folders to render, and where the PDFs go.
DEFAULT_JOBS = [
    ("source/revision-tools/scheme-of-work",      "Printable-PDFs/scheme-of-work"),
    ("source/revision-tools/subtopic-quizzes",    "Printable-PDFs/subtopic-quizzes"),
    ("source/revision-tools/revision-games",      "Printable-PDFs/revision-games"),
    ("source/revision-tools/worksheets",          "Printable-PDFs/worksheets"),
    ("source/revision-tools/knowledge-organisers", "Printable-PDFs/knowledge-organisers"),
    ("source/revision-tools/mini-papers",         "Printable-PDFs/mini-papers"),
    ("source/revision-tools/mock-papers",         "Printable-PDFs/mock-papers"),
    ("source/revision-tools/homework",            "Printable-PDFs/homework"),
    ("source/revision-tools/recap-checkpoints",   "Printable-PDFs/recap-checkpoints"),
    ("source/revision-tools/subtopic-revision",   "Printable-PDFs/subtopic-revision"),
    ("source/revision-tools/nea-pack",            "Printable-PDFs/nea-pack"),
    ("source/revision-tools/course-guide",        "Printable-PDFs/course-guide"),
]


def main():
    print(f"Using Chromium: {CHROME}")
    if len(sys.argv) == 3:
        jobs = [(sys.argv[1], sys.argv[2])]
    else:
        jobs = [(os.path.join(REPO, s), os.path.join(REPO, o)) for s, o in DEFAULT_JOBS]
    total = 0
    for src, out in jobs:
        if not os.path.isdir(src):
            print(f"skip (missing): {src}")
            continue
        print(f"\n{os.path.relpath(src, REPO)} -> {os.path.relpath(out, REPO)}")
        total += build_folder(src, out)
    print(f"\nDone. {total} PDF(s) generated.")


if __name__ == "__main__":
    main()
