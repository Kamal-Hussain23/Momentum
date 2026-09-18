#!/usr/bin/env python3
"""Acceptance checks for the FAQ / Objection Handling feature.

Run:  python3 check_faq.py
Exits 0 when every check passes, 1 when any fails.
"""

import os
import re
import sys

# Repo root = three folders up from this script (SPECS/<feature>/)
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

with open(os.path.join(REPO, "build-lab", "index.html"), encoding="utf-8") as f:
    HTML = f.read()
with open(os.path.join(REPO, "build-lab", "style.css"), encoding="utf-8") as f:
    CSS = f.read()
with open(os.path.join(REPO, "build-lab", "script.js"), encoding="utf-8") as f:
    JS = f.read()

passed = 0
failed = 0


def check(name, condition):
    global passed, failed
    if condition:
        passed += 1
        print(f"  PASS  {name}")
    else:
        failed += 1
        print(f"  FAIL  {name}")


print("== Content: section, heading & verbatim copy ==")
main_start = HTML.find("<main>")
main_end = HTML.find("</main>")
pricing_start = HTML.find('class="pricing"')
pricing_end = HTML.find("</section>", pricing_start)
faq_start = HTML.find('class="faq"')
faq_open = HTML.rfind("<section", 0, faq_start)

check("faq <section> exists", 'class="faq"' in HTML)
check("section sits inside <main>",
      main_start < faq_start and faq_start < main_end)
check("section sits directly after Pricing </section>",
      pricing_end < faq_open and
      "<section" not in HTML[pricing_end:faq_open])
check("heading reads: Questions?",
      "<h2>Questions?</h2>" in HTML)
check("Q1 verbatim: 'Isn't this just another to-do list?'",
      "Isn't this just another to-do list?" in HTML)
check("A1 verbatim",
      "To-do lists hand you everything at once. Momentum hands you one thing." in HTML)
check("Q2 verbatim: 'Why only one task?'",
      "Why only one task?" in HTML)
check("A2 verbatim",
      "Busy people don't fail from lack of planning — they fail from too many options. One task is small enough to actually do." in HTML)
check("Q3 verbatim: 'What does it cost?'",
      "What does it cost?" in HTML)
check("A3 verbatim",
      "It's in private beta. Joining the waitlist gets you early access and a launch-day email." in HTML)
check("Q4 verbatim: 'Does it sync with my calendar?'",
      "Does it sync with my calendar?" in HTML)
check("A4 verbatim",
      "Not yet. First we're making the one-task habit work perfectly on its own." in HTML)

print("== Accessibility: buttons, aria, panels ==")
faq_block = HTML[faq_start:HTML.find("</section>", faq_start)]
button_tags = re.findall(r"<button[^>]*>", faq_block)
panel_ids = re.findall(r'id="(faq-panel-\d+)"', faq_block)
hidden_panels = re.findall(r'class="faq__panel[^"]*"[^>]*hidden|id="faq-panel-\d+"[^>]*hidden|hidden[^>]*id="faq-panel-\d+"', faq_block)

check("four question <button>s in FAQ section", len(button_tags) == 4)
check("every button has aria-expanded",
      all('aria-expanded="' in b for b in button_tags))
check("every button has aria-controls",
      all("aria-controls=" in b for b in button_tags))
check("four answer panels with faq-panel ids", len(panel_ids) == 4)
check("every aria-controls targets a real panel id",
      all(f'id="{ctrl}"' in HTML for ctrl in re.findall(r'aria-controls="([^"]+)"', faq_block)))
check("panels start hidden", len(hidden_panels) == 4)

print("== Design tokens ==")
root_block = re.search(r":root\s*\{[^}]*\}", CSS, re.S)
component_css = CSS[root_block.end():] if root_block else CSS

check("no hardcoded hex outside :root",
      not re.search(r"#[0-9a-fA-F]{3,6}", component_css))
check(".faq uses var(--color-background)",
      "var(--color-background)" in component_css)
check(".faq uses var(--color-surface)",
      "var(--color-surface)" in component_css)
check(".faq uses var(--color-text-muted)",
      "var(--color-text-muted)" in component_css)
check(".faq uses var(--font-heading)",
      "var(--font-heading)" in component_css)
check(".faq uses var(--radius-card)",
      "--radius-card" in component_css)

print("== Motion & JS budget ==")
check("still exactly one @keyframes (no new animation)",
      CSS.count("@keyframes") == 1)
check("still exactly one <script> tag", HTML.count("<script") == 1)
check("accordion JS lives in script.js",
      "faq" in JS and "querySelectorAll" in JS)

print("== Backward compatibility ==")
check("exactly one <h1> still present", HTML.count("<h1") == 1)
check("hero headline still present",
      "Stop planning. Start finishing." in HTML)
check("feature-highlights section still present",
      'class="feature-highlights"' in HTML)
check("social-proof section still present",
      'class="social-proof"' in HTML)
check("how-it-works section still present",
      'class="how-it-works"' in HTML)
check("pricing section still present",
      'class="pricing"' in HTML)

print()
print(f"Passed: {passed}  Failed: {failed}")
sys.exit(1 if failed else 0)