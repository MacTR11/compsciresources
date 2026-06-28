#!/usr/bin/env python3
"""
Render the revision-game card data (revision-games/cards-data/*.json) into
PRINT-AND-CUT PDF card sheets: loop cards, Taboo cards, bingo grids + caller
list, quick-fire, and (per topic) card-sorts / apply-cards / Top Trumps.

Each card is a bordered box laid out on A4 so you can print and cut them out.

Usage:  python3 revision-tools/build-card-games.py
"""
import sys, os, glob, json, random, subprocess, tempfile, html

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(REPO, "revision-tools", "revision-games", "cards-data")
OUT = os.path.join(REPO, "revision-tools", "printable-pdfs", "revision-games-cards")


def find_chrome():
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium-*/chrome-linux/headless_shell"):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    import shutil
    for n in ("chromium", "chromium-browser", "google-chrome"):
        p = shutil.which(n)
        if p:
            return p
    sys.exit("No Chromium found.")


CHROME = find_chrome()

CSS = """
@page { size: A4; margin: 10mm; }
* { box-sizing: border-box; }
body { font-family: -apple-system, "Segoe UI", Arial, sans-serif; color:#111; }
h1 { font-size: 18pt; color:#1a365d; margin:0 0 2mm; }
h2 { font-size: 14pt; color:#2b6cb0; margin:6mm 0 1mm; page-break-before: always; }
h2.first { page-break-before: avoid; }
.intro { font-size:9.5pt; color:#444; margin-bottom:3mm; }
.grid { display:flex; flex-wrap:wrap; gap:4mm; }
.card { width:88mm; height:60mm; border:1.4px solid #333; border-radius:3px;
        padding:5mm; display:flex; flex-direction:column; page-break-inside:avoid;
        position:relative; overflow:hidden; }
.cnum { position:absolute; top:2mm; right:3mm; font-size:8pt; color:#999; }
.lbl { font-size:8.5pt; letter-spacing:.06em; text-transform:uppercase; color:#2b6cb0; font-weight:700; }
.have .big { font-size:17pt; font-weight:800; margin-top:1mm; line-height:1.1; }
.divider { border-top:1px dashed #bbb; margin:3mm 0; }
.whohas .clue { font-size:11.5pt; margin-top:1mm; }
.card.taboo .term { font-size:16pt; font-weight:800; text-align:center; border-bottom:2px solid #333; padding-bottom:2mm; margin-bottom:2mm; }
.card.taboo .dontsay { font-size:9pt; color:#c53030; font-weight:700; }
.card.taboo ul { margin:1mm 0 0; padding-left:6mm; font-size:12.5pt; }
.card.scn { height:46mm; }
.card.scn .scn-t { font-size:11.5pt; }
.card.cat { height:22mm; width:88mm; background:#ebf4ff; align-items:center; justify-content:center; }
.card.cat .term { font-size:14pt; font-weight:800; text-align:center; }
.card.trump .term { font-size:14pt; font-weight:800; text-align:center; border-bottom:2px solid #333; padding-bottom:1.5mm; margin-bottom:1.5mm; }
.card.trump table { width:100%; font-size:10.5pt; border-collapse:collapse; }
.card.trump td { padding:0.8mm 0; }
.card.trump td:first-child { color:#555; }
.card.trump td:last-child { text-align:right; font-weight:700; }
table.sheet { width:100%; border-collapse:collapse; font-size:10.5pt; margin-top:2mm; }
table.sheet th, table.sheet td { border:1px solid #999; padding:2mm 3mm; text-align:left; vertical-align:top; }
table.sheet th { background:#ebf4ff; }
.bingo { display:flex; flex-wrap:wrap; gap:6mm; }
.bcard { border:1.4px solid #333; padding:3mm; page-break-inside:avoid; }
.bcard .bt { text-align:center; font-weight:800; font-size:11pt; margin-bottom:2mm; }
.bcard table { border-collapse:collapse; }
.bcard td { border:1px solid #555; width:30mm; height:22mm; text-align:center;
            font-size:9.5pt; padding:1mm; vertical-align:middle; }
.note { font-size:9pt; color:#555; margin:2mm 0; }
.scissors { font-size:9pt; color:#888; }
"""


def esc(s):
    return html.escape(str(s))


def grid(cards):
    return '<div class="grid">' + "".join(cards) + "</div>"


def render_topic(d):
    parts = []
    parts.append(f"<h1>Revision Game Cards — {esc(d['topic'])}</h1>")
    parts.append('<div class="intro">Print and cut along the borders. ✂️ '
                 'Loop cards: each player reads the bottom "Who has…?"; whoever holds the matching '
                 '"I have…" reads it out, then their own clue — the chain visits every card and loops back to the start.</div>')

    # Loop cards
    lc = d.get("loop_cards", [])
    if lc:
        cards = []
        for i, c in enumerate(lc):
            cards.append(
                f'<div class="card loop"><div class="cnum">{i+1} / {len(lc)}</div>'
                f'<div class="have"><span class="lbl">I have</span><div class="big">{esc(c["have"])}</div></div>'
                f'<div class="divider"></div>'
                f'<div class="whohas"><span class="lbl">Who has…</span><div class="clue">{esc(c["who_has"])}?</div></div></div>')
        parts.append('<h2 class="first">Loop cards (dominoes) — cut out & deal</h2>')
        parts.append(grid(cards))

    # Taboo cards
    tb = d.get("taboo", [])
    if tb:
        cards = []
        for c in tb:
            banned = "".join(f"<li>{esc(w)}</li>" for w in c["banned"])
            cards.append(f'<div class="card taboo"><div class="term">{esc(c["term"])}</div>'
                         f'<div class="dontsay">Don\'t say:</div><ul>{banned}</ul></div>')
        parts.append('<h2>Taboo cards — describe the term without the banned words</h2>')
        parts.append(grid(cards))

    # Top Trumps (2.3)
    tt = d.get("top_trumps", [])
    if tt:
        cards = []
        for c in tt:
            rows = "".join(f"<tr><td>{esc(k.replace('_',' ').title())}</td><td>{esc(c[k])}</td></tr>"
                           for k in ("best", "average", "worst", "space", "needs_sorted") if k in c)
            cards.append(f'<div class="card trump"><div class="term">{esc(c["name"])}</div>'
                         f'<table>{rows}</table></div>')
        parts.append('<h2>Top Trumps — sorting & searching (play higher/lower)</h2>')
        parts.append('<div class="note">Tip: for time complexity, "higher" = worse (slower). Compare the agreed stat; best card wins.</div>')
        parts.append(grid(cards))

    # Card sort (1.5)
    cs = d.get("card_sort")
    if cs:
        cats = "".join(f'<div class="card cat"><div class="term">{esc(c)}</div></div>' for c in cs["categories"])
        parts.append('<h2>Card sort — category headers</h2>')
        parts.append(grid([cats]) if isinstance(cats, str) else grid(cats))
        scn = "".join(f'<div class="card scn"><span class="lbl">Scenario</span>'
                      f'<div class="scn-t">{esc(it["scenario"])}</div></div>' for it in cs["items"])
        parts.append('<h2>Card sort — scenario cards (sort under the headers)</h2>')
        parts.append(grid([scn]))
        rows = "".join(f"<tr><td>{esc(it['scenario'])}</td><td>{esc(it['category'])}</td></tr>" for it in cs["items"])
        parts.append('<h2>Card sort — answer key (teacher)</h2>')
        parts.append(f'<table class="sheet"><tr><th>Scenario</th><th>Correct category</th></tr>{rows}</table>')

    # Apply cards (2.1)
    ap = d.get("apply_cards", [])
    if ap:
        scn = "".join(f'<div class="card scn"><span class="lbl">Apply: {esc(it["skill"])}</span>'
                      f'<div class="scn-t">{esc(it["scenario"])}</div></div>' for it in ap)
        parts.append('<h2>"Apply it" cards — give a valid application of the named skill</h2>')
        parts.append(grid([scn]))
        rows = "".join(f"<tr><td>{esc(it['scenario'])}</td><td>{esc(it['skill'])}</td><td>{esc(it.get('example',''))}</td></tr>" for it in ap)
        parts.append('<h2>"Apply it" — model answers (teacher)</h2>')
        parts.append(f'<table class="sheet"><tr><th>Scenario</th><th>Skill</th><th>Model application</th></tr>{rows}</table>')

    # Bingo
    bg = d.get("bingo")
    if bg and bg.get("terms"):
        terms = bg["terms"]
        parts.append('<h2>Bingo — word bank & ready-to-cut cards</h2>')
        parts.append('<div class="note"><b>Word bank</b> (students fill a blank 3×3 grid, or use the pre-filled cards below): '
                     + ", ".join(esc(t) for t in terms) + "</div>")
        bcards = []
        for k in range(6):
            rnd = random.Random(1000 + k)
            pick = rnd.sample(terms, min(9, len(terms)))
            tds = ""
            for r in range(3):
                tds += "<tr>" + "".join(f"<td>{esc(pick[r*3+c])}</td>" for c in range(3)) + "</tr>"
            bcards.append(f'<div class="bcard"><div class="bt">BINGO {k+1}</div><table>{tds}</table></div>')
        parts.append('<div class="bingo">' + "".join(bcards) + "</div>")
        rows = "".join(f"<tr><td>{i+1}</td><td>{esc(c['clue'])}</td><td>{esc(c['answer'])}</td></tr>"
                       for i, c in enumerate(bg.get("callers", [])))
        parts.append('<h2>Bingo — caller\'s list (teacher: read the clue, students cross off the term)</h2>')
        parts.append(f'<table class="sheet"><tr><th>#</th><th>Clue to read aloud</th><th>Answer</th></tr>{rows}</table>')

    # Quickfire
    qf = d.get("quickfire", [])
    if qf:
        rows = "".join(f"<tr><td>{i+1}</td><td>{esc(c['clue'])}</td><td>{esc(c['answer'])}</td></tr>"
                       for i, c in enumerate(qf))
        parts.append('<h2>Quick-fire — clue &amp; answer (self-test / quiz-quiz-trade)</h2>')
        parts.append(f'<table class="sheet"><tr><th>#</th><th>Clue</th><th>Answer</th></tr>{rows}</table>')

    return "<!DOCTYPE html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>" + "".join(parts) + "</body></html>"


def to_pdf(htmlstr, pdf_path):
    fd, hf = tempfile.mkstemp(suffix=".html")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(htmlstr)
    try:
        subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                        "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}", "file://" + hf],
                       check=True, capture_output=True)
    finally:
        os.unlink(hf)


def main():
    os.makedirs(OUT, exist_ok=True)
    files = sorted(glob.glob(os.path.join(DATA, "*.json")))
    if not files:
        sys.exit("No card-data JSON found — run the extractors first.")
    for jf in files:
        d = json.load(open(jf, encoding="utf-8"))
        name = os.path.splitext(os.path.basename(jf))[0]
        pdf = os.path.join(OUT, name + "-cards.pdf")
        to_pdf(render_topic(d), pdf)
        print(f"  {os.path.basename(pdf)}")
    print(f"\nDone. {len(files)} card-sheet PDF(s) in {os.path.relpath(OUT, REPO)}")


if __name__ == "__main__":
    main()
