#!/usr/bin/env python3
"""Build Momentum-Problem-Solution.pdf (6 pages) — plain white layout.

Simple, clean report: black text on a white background, no cards, no
colored design elements, just readable headings and body paragraphs.
"""
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Momentum-Problem-Solution.pdf")


def reg(name, path, alt):
    p = path if os.path.exists(path) else alt
    pdfmetrics.registerFont(TTFont(name, p))
    return p


FD = os.path.expanduser("~/.fonts")
DV = "/usr/share/fonts/truetype/dejavu"
reg("BOLD", os.path.join(FD, "Manrope-Bold.ttf"), os.path.join(DV, "DejaVuSans-Bold.ttf"))
reg("XB", os.path.join(FD, "Manrope-ExtraBold.ttf"), os.path.join(DV, "DejaVuSans-Bold.ttf"))
reg("BODY", os.path.join(FD, "Inter-Regular.ttf"), os.path.join(DV, "DejaVuSans.ttf"))
reg("SEMI", os.path.join(FD, "Inter-SemiBold.ttf"), os.path.join(DV, "DejaVuSans.ttf"))

INK = (0.10, 0.10, 0.10)
GRAY = (0.42, 0.42, 0.42)
LINE = (0.85, 0.85, 0.85)
WHITE = (1, 1, 1)

PW, PH = A4
ML = MR = 20 * mm
CW = PW - ML - MR
TOTAL = 6


def footer(c, num, label="Momentum — Problem & Solution"):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(ML, 13 * mm, PW - MR, 13 * mm)
    c.setFont("BODY", 8)
    c.setFillColor(GRAY)
    c.drawString(ML, 9.5 * mm, label)
    c.drawRightString(PW - MR, 9.5 * mm, "Page %d of %d" % (num, TOTAL))


def wrap(c, x, y, w, text, font="BODY", size=11, leading=5.6 * mm, color=INK):
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


def heading(c, x, y, num, title):
    c.setFont("XB", 15)
    c.setFillColor(INK)
    c.drawString(x, y, title)
    c.setFont("SEMI", 8.5)
    c.setFillColor(GRAY)
    c.drawString(x, y - 5 * mm, "SECTION %s" % num)
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(x, y - 7 * mm, PW - MR, y - 7 * mm)
    return y - 12 * mm


c = canvas.Canvas(OUT, pagesize=A4)
c.setTitle("Momentum — Problem & Solution")
c.setAuthor("Momentum")
c.setSubject("Problem Statement and Solution")

# ---------------- PAGE 1 : TITLE PAGE ----------------
c.setFillColor(WHITE)
c.rect(0, 0, PW, PH, stroke=0, fill=1)
c.setFillColor(GRAY)
c.setFont("SEMI", 11)
c.drawCentredString(PW / 2, PH - 70 * mm, "MOMENTUM")
c.setStrokeColor(LINE)
c.setLineWidth(0.7)
c.line(40 * mm, PH - 78 * mm, PW - 40 * mm, PH - 78 * mm)
c.setFillColor(INK)
c.setFont("XB", 36)
c.drawCentredString(PW / 2, PH - 100 * mm, "Problem & Solution")
c.setFont("SEMI", 12.5)
c.drawCentredString(PW / 2, PH - 112 * mm, "One thing done. Every day.")
intro = ("A short, plain-English report on the problem Momentum solves, the "
         "solution we are building, and why it is different from the tools "
         "you have already tried.")
c.setFont("BODY", 11)
c.setFillColor(GRAY)
wrap(c, 50 * mm, PH - 130 * mm, PW - 100 * mm, intro, font="BODY", size=11,
     leading=5.6 * mm, color=GRAY)

c.setFont("BODY", 9)
c.setFillColor(GRAY)
wrap(c, 50 * mm, PH - 150 * mm, PW - 100 * mm,
     "Prepared by the Momentum team as part of the build-lab "
     "deliverables.", font="BODY", size=9, leading=4.6 * mm, color=GRAY)
c.showPage()

# ---------------- PAGE 2 : INTRODUCTION + THE PROBLEM ----------------
footer(c, 2)
y = heading(c, ML, PH - 20 * mm, "1", "Introduction")
y = wrap(c, ML, y, CW,
         "Momentum is a simple daily-habit app for busy professionals who work "
         "full time and study on the side. Every day it narrows you down to a "
         "single Most Important Task — the one thing that matters most — so you "
         "finally finish something instead of staying busy-but-stuck.")
y -= 2.5 * mm
y = wrap(c, ML, y, CW,
         "The short version: lots of busy people plan and plan, but never finish. "
         "We are building Momentum, a simple app that gives you one task to do "
         "each day — so you actually finish things.")
y -= 5 * mm
y = heading(c, ML, y, "2", "The Problem")
y = wrap(c, ML, y, CW,
         "Who this is for. Someone in their 20s or 30s who works full time and "
         "studies on the side — a certification, a course, or a skill that could "
         "earn them more. They have calendars, notebooks, and to-do lists. They "
         "still feel stuck.")
y -= 2.5 * mm
y = wrap(c, ML, y, CW,
         "The feeling: busy but stuck. They always have a plan, but they don't "
         "do it. They postpone the one task that matters most — and then they "
         "feel guilty about it. Over time, that guilt turns into stress and "
         "burnout, which makes putting things off even worse.")
y -= 2.5 * mm
c.setFont("SEMI", 11)
c.setFillColor(INK)
y = wrap(c, ML, y, CW,
         "PROCRASTINATE \u2192 FEEL GUILTY \u2192 STRESS \u2192 BURNOUT \u2192 REPEAT",
         font="SEMI", size=11, leading=5.6 * mm, color=INK)
y -= 2.5 * mm
y = wrap(c, ML, y, CW,
         "Why existing tools don't help. To-do lists hand you everything at "
         "once — twenty items, no clear starting point. Overwhelmed, you pick "
         "nothing. Calendars only help you plan time; they don't commit you to "
         "the single task that actually moves you forward. The result: you are "
         "busy every day but never moving forward.")
c.showPage()

# ---------------- PAGE 3 : THE SOLUTION + HOW IT WORKS ----------------
footer(c, 3)
y = heading(c, ML, PH - 20 * mm, "3", "The Solution")
y = wrap(c, ML, y, CW,
         "Momentum closes the gap between planning and doing. Each day it "
         "narrows you down to a single Most Important Task (MIT) — the one "
         "thing that matters most today. Not a list of twenty items. Just one "
         "thing.")
y -= 2.5 * mm
y = wrap(c, ML, y, CW,
         "You check that one thing off when it's done. That gives you a real "
         "feeling of progress instead of guilt. And because there is only ever "
         "one thing to do, it is small enough that you actually do it.")
y -= 2.5 * mm
c.setFont("SEMI", 11.5)
c.setFillColor(INK)
y = wrap(c, ML, y, CW,
         "In one line: To-do lists help you plan. Momentum helps you finish.",
         font="SEMI", size=11.5, leading=5.8 * mm, color=INK)
y -= 8 * mm
y = heading(c, ML, y, "4", "How It Works")
for head, body in [
    ("1. Set it.", "Each evening, name the one task that matters most "
     "tomorrow. One task — not a list."),
    ("2. Do it.", "Focus on just that one thing. Nothing else to distract you."),
    ("3. Check it.", "One tap tells the whole day \u201cdone.\u201d Repeat tomorrow."),
]:
    c.setFont("SEMI", 11.5)
    c.setFillColor(INK)
    c.drawString(ML, y, head)
    y -= 5.6 * mm
    y = wrap(c, ML + 12 * mm, y, CW - 12 * mm, body, font="BODY", size=11,
             leading=5.6 * mm, color=INK)
    y -= 3 * mm
c.setFont("SEMI", 11.5)
c.setFillColor(INK)
wrap(c, ML, y, CW,
     "SMALL ENOUGH TO DO \u2192 ACTUALLY DONE", font="SEMI", size=11.5,
     leading=5.8 * mm, color=INK)
c.showPage()

# ---------------- PAGE 4 : WHY IT'S DIFFERENT + WHAT EXISTS ----------------
footer(c, 4)
y = heading(c, ML, PH - 20 * mm, "5", "Why It's Different")
c.setFont("SEMI", 10.5)
c.setFillColor(INK)
c.drawString(ML, y, "Today's tools")
c.drawString(ML + 82 * mm, y, "Momentum")
y -= 6 * mm
c.setStrokeColor(LINE)
c.line(ML, y + 2.5 * mm, PW - MR, y + 2.5 * mm)
rows = [
    ("Hand you everything at once", "Hands you one thing"),
    ("Twenty items, no starting point", "One clear Most Important Task"),
    ("Leave you with guilt about what's left", "Give you a real feeling of done"),
    ("Help you plan", "Help you finish"),
]
left_w = 80 * mm
right_w = CW - left_w - 6 * mm
y -= 2 * mm
for i, (left, right) in enumerate(rows):
    c.setFont("BODY", 10)
    c.setFillColor(INK)
    y1 = wrap(c, ML, y, left_w, left, font="BODY", size=10, leading=5.2 * mm,
              color=INK)
    y2 = wrap(c, ML + left_w + 6 * mm, y, right_w, right, font="BODY", size=10,
              leading=5.2 * mm, color=INK)
    y = min(y1, y2)
    if i < len(rows) - 1:
        c.setStrokeColor(LINE)
        c.setLineWidth(0.4)
        c.line(ML, y, PW - MR, y)
    y -= 4 * mm
y -= 3 * mm
y = wrap(c, ML, y, CW,
         "Momentum isn't a better to-do list. Too many lists are part of the "
         "problem — Momentum removes the list and keeps the one task that "
         "matters.")
y -= 7 * mm
y = heading(c, ML, y, "6", "What Exists Today")
y = wrap(c, ML, y, CW,
         "The landing page is built and working. It starts with the problem, "
         "leads with the solution, explains how it works, and collects waitlist "
         "emails in one click.")
y -= 2.5 * mm
y = wrap(c, ML, y, CW,
         "Why a waitlist? Momentum is in private beta. Joining the waitlist "
         "gets you early access and a launch-day email. One signup, one click, "
         "no friction.")
c.showPage()

# ---------------- PAGE 5 : WHAT'S NEXT + IN ONE SENTENCE ----------------
footer(c, 5)
y = heading(c, ML, PH - 20 * mm, "7", "What's Next")
for head, body in [
    ("1. Test with real people.", "Watch someone use the page for one minute "
     "and fix the three most confusing things."),
    ("2. Deploy publicly.", "Put the site on the open web so anyone with the "
     "link can see it and join the waitlist."),
    ("3. Connect a real signup form.", "Save the emails behind the landing "
     "page so the waitlist actually grows."),
]:
    c.setFont("SEMI", 11.5)
    c.setFillColor(INK)
    c.drawString(ML, y, head)
    y -= 5.6 * mm
    y = wrap(c, ML + 12 * mm, y, CW - 12 * mm, body, font="BODY", size=11,
             leading=5.6 * mm, color=INK)
    y -= 3 * mm
y -= 5 * mm
y = heading(c, ML, y, "8", "In One Sentence")
y -= 1 * mm
c.setFont("XB", 14)
c.setFillColor(INK)
wrap(c, ML, y, CW, "Momentum — One thing done. Every day.",
     font="XB", size=14, leading=6.2 * mm, color=INK)
y -= 6.5 * mm
y = wrap(c, ML, y, CW,
         "Busy people don't fail from a lack of planning — they fail from too "
         "many options. Momentum sets that aside and hands you the one task "
         "that matters, so you can finally finish something.")
c.showPage()

# ---------------- PAGE 6 : DELIVERABLES ----------------
footer(c, 6, label="Momentum — Deliverables")
y = heading(c, ML, PH - 20 * mm, "D", "Deliverables")
drows = [
    ("1.", "Startup Name", "Momentum"),
    ("2.", "Value Proposition",
     "We help busy professionals who work full time and study on the side stop "
     "feeling \u201cbusy but stuck\u201d and finally finish what matters — by narrowing "
     "every day down to a single Most Important Task."),
    ("3.", "GitHub Repository URL",
     "https://github.com/Kamal-Hussain23/Momentum"),
    ("4.", "Public Deployed URL",
     "https://kamal-hussain23.github.io/Momentum/"),
]
for num, head, val in drows:
    c.setFont("SEMI", 11)
    c.setFillColor(INK)
    c.drawString(ML, y, "%s %s" % (num, head))
    y -= 5.8 * mm
    c.setFont("BODY", 10.5)
    c.setFillColor(INK)
    y = wrap(c, ML + 10 * mm, y, CW - 10 * mm, val, font="BODY", size=10.5,
             leading=5.2 * mm, color=INK)
    y -= 8 * mm
c.setFont("BODY", 9.5)
c.setFillColor(GRAY)
wrap(c, ML, y, CW,
     "This document is part of the Momentum build-lab deliverables.",
     font="BODY", size=9.5, leading=5 * mm, color=GRAY)
c.showPage()

c.save()
print("wrote", OUT)

# ---------------- verify ----------------
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
