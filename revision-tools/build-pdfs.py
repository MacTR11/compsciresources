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
"""


def md_to_html(md_text, title):
    # Force any collapsible answer sections open so answers print.
    md_text = re.sub(r"<details(?!\s+open)", "<details open", md_text)
    body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
    )
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<title>{title}</title><style>{CSS}</style></head><body>{body}</body></html>"
    )


def convert(md_path, pdf_path):
    with open(md_path, encoding="utf-8") as f:
        text = f.read()
    html = md_to_html(text, os.path.splitext(os.path.basename(md_path))[0])
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


def build_folder(srcdir, outdir):
    os.makedirs(outdir, exist_ok=True)
    mds = sorted(f for f in glob.glob(os.path.join(srcdir, "*.md"))
                 if os.path.basename(f).lower() != "readme.md")
    made = 0
    for md in mds:
        pdf = os.path.join(outdir, os.path.splitext(os.path.basename(md))[0] + ".pdf")
        convert(md, pdf)
        print(f"  {os.path.basename(pdf)}")
        made += 1
    return made


# Default set: which Markdown folders to render, and where the PDFs go.
DEFAULT_JOBS = [
    ("revision-tools/subtopic-quizzes",    "revision-tools/printable-pdfs/subtopic-quizzes"),
    ("revision-tools/revision-games",      "revision-tools/printable-pdfs/revision-games"),
    ("revision-tools/worksheets",          "revision-tools/printable-pdfs/worksheets"),
    ("revision-tools/knowledge-organisers", "revision-tools/printable-pdfs/knowledge-organisers"),
    ("revision-tools/mini-papers",         "revision-tools/printable-pdfs/mini-papers"),
    ("revision-tools/mock-papers",         "revision-tools/printable-pdfs/mock-papers"),
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
