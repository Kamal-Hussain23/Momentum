#!/usr/bin/env python3
"""Acceptance checks for the How It Works / Product Demo feature.

Run:  python3 check_how_it_works.py
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


print("== Content: section & copy ==")
# Check section sits inside <main>, directly after the Feature Highlights </section>
main_start = HTML.find("<main>")
fh_start = HTML.find('class="feature-highlights"')
wh_start = HTML.find('class="how-it-works"')
fh_end = HTML.find('</section>', fh_start)
wh_end = HTML.find('</section>', wh_start)
main_end = HTML.find("</main>")

check("how-it-works <section> exists", 'class="how-it-works"' in HTML)
check("section sits inside <main>",
      main_start < wh_start and wh_start < main_end)
check("section is after Feature Highlights </section>",
      fh_end < wh_start)
check("Step 1 headline: Set it.",
      "Set it." in HTML)
check("Step 1 body: Each evening, name the one task that matters most tomorrow.",
      "Each evening, name the one task that matters most tomorrow." in HTML)
check("Step 2 headline: Do it.",
      "Do it." in HTML)
check("Step 2 body: Focus on just that one thing. Nothing else to distract you.",
      "Focus on just that one thing. Nothing else to distract you." in HTML)
check("Step 3 headline: Check it.",
      "Check it." in HTML)
check("Step 3 body: One tap tells the whole day 'done.' Repeat tomorrow.",
      "One tap tells the whole day 'done.' Repeat tomorrow." in HTML)

print("== Design tokens ==")
root_block = re.search(r":root\s*\{[^}]*\}", CSS, re.S)
component_css = CSS[root_block.end():] if root_block else CSS

check("no hardcoded hex outside :root",
      not re.search(r"#[0-9a-fA-F]{3,6}", component_css))
check(".how-it-works uses var(--color-background)",
      "var(--color-background)" in component_css)
check(".how-it-works uses var(--color-surface)",
      "var(--color-surface)" in component_css)
check(".how-it-works uses var(--color-text)",
      "var(--color-text)" in component_css)
check(".how-it-works uses var(--color-text-muted)",
      "var(--color-text-muted)" in component_css)
check(".how-it-works uses var(--color-primary)",
      "var(--color-primary)" in component_css)
check(".how-it-works uses var(--radius-card)",
      "--radius-card" in component_css)
check(".how-it-works uses var(--space-4)",
      "--space-4" in component_css)
check(".how-it-works uses var(--space-6)",
      "--space-6" in component_css)
check("headlines use var(--color-primary) for emphasis",
      ".how-it-works__headline" in CSS and "var(--color-primary)" in CSS)

print("== Motion & JS budget ==")
check("still exactly one @keyframes (no new animation)",
      CSS.count("@keyframes") == 1)
check("no new <script> tag added", HTML.count("<script") == 1)

print("== Backward compatibility ==")
check("exactly one <h1> still present", HTML.count("<h1") == 1)
check("feature-highlights section still present",
      'class="feature-highlights"' in HTML)
check("social-proof section still present",
      'class="social-proof"' in HTML)
check("hero headline still present",
      "Stop planning. Start finishing." in HTML)

print()
print(f"Passed: {passed}  Failed: {failed}")
sys.exit(1 if failed else 0)
