"""Build the website CV. Requires reportlab; run from any working directory."""
from pathlib import Path

import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "chenqi-meng-cv.pdf"
INK = colors.HexColor("#1e2b38")
BLUE = colors.HexColor("#285b78")
MUTED = colors.HexColor("#58636e")

# Embed the fonts distributed with ReportLab for consistent PDF rendering.
font_dir = Path(reportlab.__file__).parent / "fonts"
for name, filename in [("CVSans", "Vera.ttf"), ("CVSans-Bold", "VeraBd.ttf"),
                       ("CVSans-Italic", "VeraIt.ttf"), ("CVSans-BoldItalic", "VeraBI.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(font_dir / filename)))
pdfmetrics.registerFontFamily("CVSans", normal="CVSans", bold="CVSans-Bold",
                            italic="CVSans-Italic", boldItalic="CVSans-BoldItalic")

styles = {
    "name": ParagraphStyle("name", fontName="Times-Roman", fontSize=29, leading=33, textColor=INK, spaceAfter=5),
    "body": ParagraphStyle("body", fontName="CVSans", fontSize=8.6, leading=12.3, textColor=INK, spaceAfter=4),
    "small": ParagraphStyle("small", fontName="CVSans", fontSize=7.6, leading=11, textColor=MUTED, spaceAfter=4),
    "section": ParagraphStyle("section", fontName="CVSans-Bold", fontSize=8.5, leading=12, textColor=BLUE, spaceBefore=12, spaceAfter=7),
    "title": ParagraphStyle("title", fontName="CVSans-Bold", fontSize=8.6, leading=12.3, textColor=INK, spaceAfter=3),
}
story = []

def p(text, style="body"):
    return Paragraph(text, styles[style])

def add(text, style="body"):
    story.append(p(text, style))

def section(title):
    add(title.upper(), "section")

def link(url, label):
    return f'<link href="{url}" color="#285b78">{label}</link>'

def publication(title, authors, venue, links):
    story.append(KeepTogether([
        p(title, "title"),
        p(authors, "body"),
        p(venue + " | " + " · ".join(link(url, label) for url, label in links), "small"),
        Spacer(1, 6),
    ]))

add("Chenqi Meng", "name")
add("PhD student in Physics | The Chinese University of Hong Kong")
add(
    link("mailto:mcqgravity@gmail.com", "mcqgravity@gmail.com") + " &nbsp; | &nbsp; " +
    link("https://chenqitrg.github.io/", "chenqitrg.github.io") + " &nbsp; | &nbsp; " +
    link("https://scholar.google.com/citations?user=IQELJroAAAAJ", "Google Scholar") + " &nbsp; | &nbsp; " +
    link("https://github.com/Chenqitrg", "GitHub"),
    "small",
)
story.append(Spacer(1, 7))
story.append(HRFlowable(width="100%", thickness=.6, color=colors.HexColor("#c6d0d4")))

section("Research interests")
add("Generalized symmetries and classification of quantum phases; fusion categories and non-invertible SPT phases; tensor network renormalization and many-body simulation; algebraic formulations of conformal field theory and holographic duality.")
add("I favor a mathematical approach, starting from ideal models and fixed-point theories. My longer-term interests include higher-dimensional conformal field theories and extending insights from these settings towards more realistic physical systems.")

section("Education")
add("<b>The Chinese University of Hong Kong</b> | PhD in Physics, in progress", "body")
add("September 2021 - Present &nbsp; | &nbsp; Advisor: Zhengcheng Gu", "small")
story.append(Spacer(1, 3))
add("<b>University of Science and Technology of China</b> | BS in Physics", "body")
add("September 2017 - May 2021 &nbsp; | &nbsp; GPA: 3.69/4.3", "small")

section("Publications and preprints")
publication(
    "Algebraic Tensor Network Renormalization and Holographic duality",
    "<b>Chenqi Meng</b>, Tian Lan, Zhengcheng Gu.",
    "Preprint (2026)",
    [("https://arxiv.org/abs/2610.08787", "arXiv:2610.08787")],
)
publication(
    "A Practical Introduction to Tensor Network Renormalization with TNRKit.jl",
    "Victor Vanthilt, Adwait Naravane, <b>Chenqi Meng</b>, Atsushi Ueda.",
    "<i>SciPost Physics Codebases</i> 77 (2026)",
    [("https://doi.org/10.21468/SciPostPhysCodeb.77", "DOI"), ("https://arxiv.org/abs/2604.06922", "arXiv:2604.06922")],
)
publication(
    "Non-invertible SPTs: an on-site realization of (1+1)d anomaly-free fusion category symmetry",
    "<b>Chenqi Meng</b>, Xinping Yang, Tian Lan, Zhengcheng Gu.",
    "Preprint (2024; revised 2025)",
    [("https://arxiv.org/abs/2412.20546", "arXiv:2412.20546")],
)

section("Research software")
add("Contributor to " + link("https://github.com/QuantumKitHub/TNRKit.jl", "TNRKit.jl") + ", a collaborative Julia package for tensor network renormalization.")

section("Skills")
add("<b>Programming:</b> Julia, Python, C, Mathematica.<br/><b>Scientific computing:</b> Tensor network algorithms, Loop-TNR, DMRG, many-body simulation.<br/><b>Mathematics:</b> Category theory, representation theory, conformal field theory, algebra.")

section("Other project")
add("<b>Peerpedia:</b> A website for reading and reviewing research papers. " + link("https://peerpedia.dev/", "peerpedia.dev"))

section("Personal interests")
add("Hiking, cycling, and the art of M. C. Escher.")

def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#c6d0d4"))
    canvas.setLineWidth(.5)
    canvas.line(46, 38, A4[0] - 46, 38)
    canvas.setFont("CVSans", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(46, 26, "Chenqi Meng | Curriculum vitae")
    canvas.drawRightString(A4[0] - 46, 26, f"Updated 21 October 2026 | {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=A4, leftMargin=46, rightMargin=46, topMargin=37, bottomMargin=50,
    title="Chenqi Meng - Curriculum Vitae", author="Chenqi Meng",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
