"""Turns the approved Privacy Notice (Word file MOD-010) into the two page bodies.

Run only when a new approved version of the Word file exists:
    python3 _build/extract_privacy.py /path/to/MOD-010-PRV-EN-IT_Privacy_Notice_vNN.docx
It writes _build/privacy_en.html and _build/privacy_it.html. The text is taken
from the Word file as it is; nothing is rewritten here. Needs pandoc.
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = sys.argv[1]
html = subprocess.run(["pandoc", "-t", "html", "--wrap=none", src],
                      check=True, capture_output=True, text=True).stdout

en, it = html.split("<p>INFORMATIVA PRIVACY</p>")
en = en.replace("<p>PRIVACY NOTICE</p>", "", 1)


def clean(part):
    # version table -> one line of meta text
    def meta(m):
        cells = re.findall(r"<t[hd]>(.*?)</t[hd]>", m.group(0), flags=re.S)
        cells = [re.sub(r"</?strong>", "", c).strip() for c in cells]
        pairs = [f"{cells[i]} {cells[i + 1]}" for i in range(0, len(cells), 2)]
        return '<p class="legal-meta">' + " · ".join(pairs) + "</p>"
    part = re.sub(r"<table>.*?</table>", meta, part, flags=re.S)
    part = re.sub(r"<p><strong>(\d+\. .*?)</strong></p>", r"<h2>\1</h2>", part)
    part = re.sub(r"<li><blockquote>\s*<p>(.*?)</p>\s*</blockquote></li>", r"<li>\1</li>", part, flags=re.S)
    part = part.replace("<ul>", '<ul class="bullets">')
    part = re.sub(r"<p><em>(.*?)</em></p>", r'<p class="legal-note">\1</p>', part)
    part = re.sub(r"(fgabriele@bevstrategist\.co\.uk)", r'<a href="mailto:\1">\1</a>', part)
    part = re.sub(r"(https://ico\.org\.uk/make-a-complaint/)", r'<a href="\1" rel="noopener">\1</a>', part)
    return part.strip() + "\n"


for name, part in (("privacy_en.html", en), ("privacy_it.html", it)):
    with open(os.path.join(HERE, name), "w", encoding="utf8") as f:
        f.write(clean(part))
    print("wrote", name)
