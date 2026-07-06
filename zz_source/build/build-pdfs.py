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

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
td:empty { height: 8mm; }
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
.answer-space { margin: 4px 0 14px; }
.answer-space .rl { border-bottom: 1.2px dotted #666; height: 9mm; }
.sheet-note { color: #2b6cb0; font-style: italic; font-size: 10pt; margin: 2px 0 10px; }
"""


# Folders whose resources are split into a worksheet + a separate answer sheet.
QA_FOLDERS = {"subtopic-quizzes", "worksheets", "mini-papers", "mock-papers",
              "homework", "recap-checkpoints", "assessments"}
ANSWER_HEADING = re.compile(r"^\s*#{2,3}\s+(answer key|answers|mark scheme)", re.I)
MARK_TAG = re.compile(r"\[(\d+)\]|\((\d+)\s*marks?\)")


def normalise_md(md_text):
    """Work around python-markdown limitations that leak raw syntax:
    - fenced code blocks indented inside lists aren't recognised -> dedent
      every fence (and its contents) to column 0, with a blank line before;
    - a table block must be preceded by a blank line -> insert one."""
    lines = md_text.split("\n")
    out = []
    fence_indent = None            # indent string of the fence we're inside
    for i, line in enumerate(lines):
        stripped = line.lstrip()
        indent = line[:len(line) - len(stripped)]
        if fence_indent is None and stripped.startswith("```") and indent:
            fence_indent = indent
            if out and out[-1].strip():
                out.append("")
            out.append(stripped)
            continue
        if fence_indent is not None:
            # inside an indented fence: strip that indent from content
            content = line[len(fence_indent):] if line.startswith(fence_indent) else stripped
            out.append(content)
            if stripped.startswith("```"):
                fence_indent = None
            continue
        # blank line before a table block (header row followed by |---| separator)
        if (stripped.startswith("|") and out and out[-1].strip()
                and not out[-1].lstrip().startswith("|")
                and i + 1 < len(lines) and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", lines[i + 1])
                and "-" in lines[i + 1]):
            out.append("")
        out.append(line)
    return "\n".join(out)


def escape_blanks(md_text):
    """Answer blanks are runs of underscores; python-markdown would parse
    pairs of them as bold spans and swallow the blank. Escape runs of 3+
    underscores (outside code fences) as literal-underscore entities."""
    out, in_fence = [], False
    for line in md_text.split("\n"):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        elif not in_fence:
            line = re.sub(r"_{3,}", lambda m: "&#95;" * len(m.group(0)), line)
        out.append(line)
    return "\n".join(out)


def md_to_html(md_text, title):
    md_text = re.sub(r"<details(?!\s+open)", "<details open", md_text)
    md_text = escape_blanks(md_text)
    md_text = re.sub(
        r"^\s*@@SPACE:(\d+)@@\s*$",
        lambda m: _space_div(int(m.group(1))) if int(m.group(1)) else "",
        md_text, flags=re.M)
    md_text = normalise_md(md_text)
    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    )
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>"
    )


AO_TAG = re.compile(r"\s*\*\(AO[0-9x/, ]*\)\*")


def split_qa(text):
    """Split markdown at the first Answer key / Mark scheme heading.
    AO tags are stripped from the student-facing question section (real OCR
    papers do not print them); they stay in the mark scheme."""
    lines = text.split("\n")
    for i, l in enumerate(lines):
        if ANSWER_HEADING.match(l):
            return AO_TAG.sub("", "\n".join(lines[:i])).rstrip(), "\n".join(lines[i:]).strip()
    return AO_TAG.sub("", text), None


SPACE_SENTINEL = re.compile(r"^@@SPACE:(\d+)@@$")


def _space_div(n):
    return '<div class="answer-space">' + ('<div class="rl"></div>' * n) + "</div>"


def inject_answer_space(text):
    """After each question (a line carrying a [n] / (n marks) tag), add ruled
    writing space sized to the marks. The space is placed after any code fence
    or table that immediately follows the stem (the material the question
    refers to), never inside it. A manual @@SPACE:n@@ sentinel directly after
    the question block overrides the automatic space (n=0 means the answer is
    written in the table / code gaps themselves, so no lines are added)."""
    lines = text.split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        stripped = line.lstrip()
        if stripped.startswith("```"):
            out.append(line); i += 1
            while i < n:
                out.append(lines[i]); i += 1
                if lines[i - 1].lstrip().startswith("```"):
                    break
            continue
        out.append(line); i += 1
        if stripped.startswith("#") or stripped.startswith("|"):
            continue
        tags = MARK_TAG.findall(line)
        if not tags:
            continue
        # consume material attached to the stem: blank lines, fences, tables
        while i < n:
            s = lines[i].strip()
            if s == "":
                out.append(lines[i]); i += 1
            elif s.startswith("```"):
                out.append(lines[i]); i += 1
                while i < n:
                    out.append(lines[i]); i += 1
                    if lines[i - 1].lstrip().startswith("```"):
                        break
            elif s.startswith("|"):
                while i < n and lines[i].lstrip().startswith("|"):
                    out.append(lines[i]); i += 1
            else:
                break
        # a @@SPACE sentinel anywhere before the next question stem / heading
        # means the author controls this question's answer space
        j, manual = i, False
        while j < n:
            s2 = lines[j].strip()
            if s2.startswith("```"):
                j += 1
                while j < n and not lines[j].lstrip().startswith("```"):
                    j += 1
                j += 1
                continue
            if SPACE_SENTINEL.match(s2):
                manual = True
                break
            if s2.startswith("#") or (not s2.startswith("|") and MARK_TAG.search(s2)):
                break
            j += 1
        if manual:
            continue
        nums = [int(x) for pair in tags for x in pair if x]
        marks = max(nums) if nums else 2
        k = min(12, max(2, round(marks * 1.4)))
        out.append("")
        out.append(_space_div(k))
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
    ("zz_source/revision-tools/assessments",       "zz_source/_staging/pdf/assessments"),
    ("zz_source/revision-tools/recap-checkpoints", "zz_source/_staging/pdf/recap-checkpoints"),
    ("zz_source/revision-tools/mock-papers",       "zz_source/_staging/pdf/mock-papers"),
    ("zz_source/revision-tools/mini-papers",       "zz_source/_staging/pdf/mini-papers"),
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
