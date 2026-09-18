#!/usr/bin/env python3
"""Build Momentum-Problem-Solution.pdf (6 pages) deterministically with ReportLab."""
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Momentum-Problem-Solution.pdf")

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
pdfmetrics.registerFont(TTFont("DVS", os.path.join(FONT_DIR, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("DVSB", os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))

INK = (0.11, 0.10, 0.09)
BODY = (0.29, 0.27, 0.25)
MUTED = (0.62, 0.60, 0.58)
EMBER = (0.94, 0.66, 0.41)
EMBER_D = (0.88, 0.48, 0.18)
PAPER = (0.98, 0.97, 0.95)
WHITE = (1, 1, 1)
RULE = (0.91, 0.88, 0.85)

PW, PH = A4
ML = MR = 16 * mm
MT = 14 * mm
MB = 16 * mm


def start_page(c, num, total=6):
    c.setFillColor(PAPER)
    c.rect(0, 0, PW, PH, stroke=0, fill=1)


def footer(c, num, label="Momentum · Problem & Solution", total=6):
    c.setFont("DVS", 7.5)
    c.setFillColor(MUTED)
    c.drawString(ML, 10 * mm, label)
    c.drawRightString(PW - MR, 10 * mm, f"Page {num} of {total}")


def chip(c, x, y, text):
    c.setFillColor(EMBER)
    c.circle(x, y, 4.5 * mm, stroke=0, fill=1)
    c.setFont("DVSB", 9)
    c.setFillColor(INK)
    c.drawCentredString(x, y - 1.6 * mm, text)


def section_title(c, x, y, num, title):
    chip(c, x + 3 * mm, y + 2.35 * mm, "")
    c.setFillColor(EMBER_D)
    c.setFont("DVSB", 8)
    c.drawString(x + 10 * mm, y + 3 * mm, f"SECTION {num}")
    c.setFont("DVSB", 14)
    c.setFillColor(INK)
    c.drawString(x, y - 3 * mm, title)


def body(c, x, y, text, width, leading=5 * mm, font="DVS"):
    c.setFont(font, 10)
    c.setFillColor(BODY)
    return c.drawRightString  # placeholder replaced below


c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Momentum — Problem & Solution")
c.setAuthor("Momentum")
c.setSubject("Problem Statement and Solution")

# ---------- PAGE 1 : COVER ----------
start_page(c, 1)
c.setFillColor(INK)
c.rect(0, 0, PW, PH, stroke=0, fill=1)
c.setFillColor(EMBER)
c.setFont("DVSB", 13)
c.drawString(ML, PH - 22 * mm, "MOMENTUM")
c.setFillColor(EMBER)
c.roundRect(20 * mm, PH - 44 * mm, 12 * mm, 1.6 * mm, 1 * mm, stroke=0, fill=1)
c.setFillColor(WHITE)
c.setFont("DVSB", 34)
c.drawString(ML, PH - 60 * mm, "Problem &")
c.drawString(ML, PH - 72 * mm, "Solution")
c.setFillColor(EMBER)
c.setFont("DVSB", 13)
c.drawString(ML, PH - 88 * mm, "One thing done. Every day.")
c.setFont("DVS", 10.5)
c.setFillColor((0.85, 0.83, 0.80))
intro = ("A short, plain-English report on the problem Momentum solves, "
         "the solution we are building, and why it is different from the "
         "tools you have already tried.")
c.drawString(ML, PH - 98 * mm, "")
tw = c.stringWidth(intro, "DVS", 10.5)
c.drawString(ML, PH - 98 * mm, "")


def wrap(c, x, y, w, text, font="DVS", size=10.5, leading=4.6 * mm, color=(0.85, 0.83, 0.80)):
    c.setFont(font, size)
    c.setFillColor(color)
    words = text.split()
    lines, cur = [], ""
    for wd in words:
        test = (cur + " " + wd).strip()
        if c.stringWidth(test, font, size) <= w:
            cur = test
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    for ln in lines:
        c.drawString(x, y, ln)
        y -= leading
    return y


y = wrap(c, ML, PH - 98 * mm, PW - ML - MR, intro)
c.setFillColor(EMBER_D)
c.rect(ML, ML, 10 * mm, 1 * mm, stroke=0, fill=1)
c.setFont("DVS", 8)
c.setFillColor((0.75, 0.73, 0.71))
c.drawString(ML + 14 * mm, PH - 120 * mm, "1 · Introduction   2 · The Problem   3 · The Solution")
c.setFont("DVSB", 20)
c.setFillColor(WHITE)
c.drawRightString(PW - MR, ML + 4 * mm, "MOMENTUM")
c.setFont("DVS", 7.5)
c.setFillColor((0.75, 0.73, 0.71))
c.drawRightString(PW - MR, ML, "Problem & Solution  ·  Page 1 of 6")
c.showPage()

# ---------- PAGE 2 : INTRO + PROBLEM ----------
start_page(c, 2)
footer(c, 2)
section_title(c, ML, PH - MT - 6 * mm, 1, "Introduction")
y = PH - MT - 16 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "Momentum is a simple daily-habit app for busy professionals who work "
         "full time and study on the side. Every day it narrows you down to a "
         "single Most Important Task — the one thing that matters most — so you "
         "finally finish something instead of staying busy-but-stuck.")
y -= 2 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "The short version: lots of busy people plan and plan, but never finish. "
         "We are building Momentum, a simple app that gives you one task to do "
         "each day — so you actually finish things.")
y -= 4 * mm
section_title(c, ML, y, 2, "The Problem")
y -= 12 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "Who this is for — Someone in their 20s or 30s who works full time and "
         "studies on the side — a certification, a course, or a skill that could "
         "earn them more. They have calendars, notebooks, and to-do lists. They "
         "still feel stuck.", size=10, leading=4.4 * mm)
y -= 1.5 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "The feeling: “busy but stuck”. They always have a plan, but they don't "
         "do it. They postpone the one task that matters most — and then they "
         "feel guilty about it. Over time, that guilt turns into stress and "
         "burnout, which makes putting things off even worse.", size=10, leading=4.4 * mm)
y -= 2 * mm
step_w = 33 * mm
steps = ["PROCRASTINATE", "FEEL GUILTY", "STRESS", "BURNOUT", "PROCRASTINATE MORE"]
gap = (PW - ML - MR - 5 * step_w) / 4
x = ML
for i, s in enumerate(steps):
    c.setFillColor((0.99, 0.93, 0.84))
    c.roundRect(x, y, step_w, 9 * mm, 2.5 * mm, stroke=0, fill=1)
    c.setFillColor(EMBER_D)
    c.setFont("DVSB", 5.6)
    c.drawCentredString(x + step_w / 2, y + 3.2 * mm, s)
    if i < len(steps) - 1:
        c.setFillColor(EMBER_D)
        c.setFont("DVSB", 12)
        c.drawCentredString(x + step_w + gap / 2, y + 3 * mm, "→")
    x += step_w + gap
y -= 9 * mm + 3 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "Why existing tools don't help — To-do lists hand you everything at "
         "once — twenty items, no clear starting point. Overwhelmed, you pick "
         "nothing. Calendars only help you plan time; they don't commit you to "
         "the single task that actually moves you forward. The result: you are "
         "busy every day but never moving forward.", size=10, leading=4.4 * mm)
c.showPage()

# ---------- PAGE 3 : SOLUTION + HOW IT WORKS ----------
start_page(c, 3)
footer(c, 3)
section_title(c, ML, PH - MT - 6 * mm, 3, "The Solution")
y = PH - MT - 16 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "Momentum closes the gap between planning and doing. Each day it "
         "narrows you down to a single Most Important Task (MIT) — the one "
         "thing that matters most today. Not a list of twenty items. Just one "
         "thing.", size=10, leading=4.4 * mm)
y -= 1.5 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "You check that one thing off when it's done. That gives you a real "
         "feeling of progress instead of guilt. And because there is only ever "
         "one thing to do, it is small enough that you actually do it.", size=10, leading=4.4 * mm)
y -= 2 * mm
c.setFillColor(EMBER_D)
c.rect(ML, y, 2 * mm, 2 * mm, stroke=0, fill=1)
y = wrap(c, ML + 5 * mm, y, PW - ML - MR - 5 * mm,
         "In one line: To-do lists help you plan. Momentum helps you finish.",
         font="DVSB", size=10.5, leading=4.4 * mm, color=INK)
y -= 8 * mm
section_title(c, ML, y, 4, "How It Works")
y -= 12 * mm
for h, bdy in [
    ("1 · Set it.", "Each evening, name the one task that matters most "
     "tomorrow. One task — not a list."),
    ("2 · Do it.", "Focus on just that one thing. Nothing else to distract you."),
    ("3 · Check it.", "One tap tells the whole day “done.” Repeat tomorrow."),
]:
    c.setFillColor(EMBER_D)
    c.setFont("DVSB", 10.5)
    c.drawString(ML, y, h)
    y -= 5.2 * mm
    y = wrap(c, ML + 6 * mm, y, PW - ML - MR - 6 * mm, bdy, size=10, leading=4.4 * mm)
    y -= 4 * mm
c.setFillColor((0.95, 0.95, 0.95))
c.roundRect(ML, y, PW - ML - MR, 10 * mm, 2 * mm, stroke=0, fill=1)
c.setFillColor(INK)
c.setFont("DVSB", 10)
c.drawString(ML + 4 * mm, y + 3.4 * mm, "SMALL ENOUGH TO DO → ACTUALLY DONE")
c.showPage()

# ---------- PAGE 4 : WHY DIFFERENT + WHAT EXISTS ----------
start_page(c, 4)
footer(c, 4)
section_title(c, ML, PH - MT - 6 * mm, 5, "Why It's Different")
y = PH - MT - 16 * mm
table = [
    ("Today's tools", "Momentum"),
    ("Hand you everything at once", "Hands you one thing"),
    ("Twenty items, no starting point", "One clear Most Important Task"),
    ("Leave you with guilt about what's left", "Give you a real feeling of done"),
    ("Help you plan", "Help you finish"),
]
col_x = ML
col_w = (PW - ML - MR) / 2
row_h = 10 * mm
for r_i, r_ in enumerate(table):
    c.setFillColor(WHITE if r_i % 2 else (0.985, 0.975, 0.955))
    c.rect(col_x, y - row_h + row_h, col_w, row_h, stroke=0, fill=1)
    x = col_x
    for ci in range(2):
        c.setFillColor(EMBER_D if (r_i == 0 and ci == 1) else INK)
        c.setFont("DVSB" if (r_i == 0 or ci == 1) else "DVS", 8.6)
        c.drawString(x + 3 * mm, y - 3.919 * mm, "")
        x += col_w
    break
row_y = y
for r_i, r_ in enumerate(table):
    c.setFillColor(WHITE if r_i % 2 == 0 else (0.985, 0.975, 0.955))
    c.rect(ML, row_y - row_h, col_w * 2, row_h, stroke=0, fill=1)
    c.setFillColor(RULE)
    c.rect(ML, row_y - row_h + row_h, col_w * 2, 0.3 * mm, stroke=0, fill=1)
    c.setFillColor(EMBER_D if r_i == 0 else INK)
    c.setFont("DVSB" if (r_i == 0 or 1) else "DVSB", 8.6)
    c.drawString(ML + 3 * mm, row_y - 3.7 * mm, r_[0])
    c.setFillColor(EMBER_D if r_i == 0 else (0.98, 0.66, 0.41))
    c.setFont("DVSB", 8.6)
    c.drawString(ML + col_w + 3 * mm, row_y - 3.7 * mm, r_[1])
    row_y -= row_h
y = row_y - 5 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "Momentum isn't a better to-do list. Too many lists are part of the "
         "problem — Momentum removes the list and keeps the one task that "
         "matters.", size=10, leading=4.4 * mm)
y -= 7 * mm
section_title(c, ML, y, 6, "What Exists Today")
y -= 12 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "The landing page is built and working. It starts with the problem, "
         "leads with the solution, explains how it works, and collects waitlist "
         "emails in one click.", size=10, leading=4.4 * mm)
y -= 1.5 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "Why a waitlist? Momentum is in private beta. Joining the waitlist "
         "gets you early access and a launch-day email. One signup, one click, "
         "no friction.", size=10, leading=4.4 * mm)
c.showPage()

# ---------- PAGE 5 : WHAT'S NEXT + ONE SENTENCE ----------
start_page(c, 5)
footer(c, 5)
section_title(c, ML, PH - MT - 6 * mm, 7, "What's Next")
y = PH - MT - 16 * mm
for h, bdy in [
    ("1 · Test with real people.", "Watch someone use the page for one minute "
     "and fix the three most confusing things."),
    ("2 · Deploy publicly.", "Put the site on the open web so anyone with the "
     "link can see it and join the waitlist."),
    ("3 · Connect a real signup form.", "Save the emails behind the landing "
     "page so the waitlist actually grows."),
]:
    c.setFillColor(EMBER_D)
    c.setFont("DVSB", 10.5)
    c.drawString(ML, y, h)
    y -= 5.2 * mm
    y = wrap(c, ML + 6 * mm, y, PW - ML - MR - 6 * mm, bdy, size=10, leading=4.4 * mm)
    y -= 4 * mm
y -= 4 * mm
section_title(c, ML, y, 8, "In One Sentence")
y -= 12 * mm
c.setFillColor(EMBER)
c.roundRect(ML, y, PW - ML - MR, 12 * mm, 2.5 * mm, stroke=0, fill=1)
c.setFillColor(INK)
c.setFont("DVSB", 13)
c.drawCentredString(ML + (PW - ML - MR) / 2, y + 4.2 * mm,
                    "Momentum — One thing done. Every day.")
y -= 12 * mm + 4 * mm
y = wrap(c, ML, y, PW - ML - MR,
         "Busy people don't fail from a lack of planning — they fail from too "
         "many options. Momentum sets that aside and hands you the one task "
         "that matters, so you can finally finish something.", size=10, leading=4.4 * mm)
c.showPage()

# ---------- PAGE 6 : DELIVERABLES ----------
start_page(c, 6)
footer(c, 6, label="Momentum · Deliverables")
section_title(c, ML, PH - MT - 6 * mm, "D", "Deliverables")
y = PH - MT - 16 * mm
rows = [
    ("1 · Startup Name", "Momentum"),
    ("2 · Value Proposition",
     "We help busy professionals who work full time and study on the side stop "
     "feeling “busy but stuck” and finally finish what matters — by narrowing "
     "every day down to a single Most Important Task."),
    ("3 · GitHub Repository URL",
     "https://github.com/Kamal-Hussain23/Momentum"),
    ("4 · Public Deployed URL",
     "https://kamal-hussain23.github.io/Momentum/"),
]
for head, val in rows:
    c.setFillColor(EMBER_D)
    c.setFont("DVSB", 10.5)
    c.drawString(ML, y, head)
    y -= 5.4 * mm
    c.setFillColor(EMBER)
    c.rect(ML, y, 2 * mm, 1.2 * mm, stroke=0, fill=1)
    is_url = val.startswith("http")
    y = wrap(c, ML + 5 * mm, y + 1.2 * mm, PW - ML - MR - 5 * mm, val,
             size=11, leading=5.4 * mm, color=(0.0, 0.4, 0.75) if is_url else INK)
    y -= 6 * mm
c.save()
print("wrote", OUT)

# ---------- verify ----------
try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader
r = PdfReader(OUT)
t = "\n".join((pg.extract_text() or "") for pg in r.pages)


def norm(s):
    return (s.replace("\ufb00", "ff").replace("\ufb01", "fi")
             .replace("\ufb02", "fl").replace("\ufb03", "ffi").replace("\ufb04", "ffl")
             .replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
             .replace("\u2013", "-").lower())


n = norm(t)
checks = [
    ("6 pages", len(r.pages) == 6),
    ("intro project para", "momentum is a simple daily-habit app for busy professionals" in n),
    ("no how-to-read meta", "this document explains a real problem" not in n),
    ("8 sections", all(s in n for s in ["introduction", "the problem", "the solution",
                                         "how it works", "why it's different",
                                         "what exists today", "what's next",
                                         "in one sentence"])),
    ("deliverables", "deliverables" in n),
    ("value prop", "we help busy professionals who work full time and study" in n),
    ("repo url", "github.com/kamal-hussain23/momentum" in n),
    ("deployed url", "kamal-hussain23.github.io/momentum/" in n),
    ("one-line tagline", "one thing done. every day." in n),
]
ok = True
for name, passed in checks:
    print(("OK  " if passed else "FAIL ") + name)
    ok = ok and passed
raise SystemExit(0 if ok else 1)
