#!/usr/bin/env python3
"""Acceptance checks for the Feature Highlights / Value Drivers feature.

Run:  python3 check_feature_highlights.py
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
# Check section sits inside <main>, directly after the Social Proof </section>
main_start = HTML.find("<main>")
social_proof_start = HTML.find('class="social-proof"')
hero_end = HTML.find('</section>', HTML.find('class="hero"'))
social_proof_end = HTML.find('</section>', social_proof_start)
main_end = HTML.find("</main>")

check("feature-highlights <section> exists", 'class="feature-highlights"' in HTML)
check("section sits inside <main>",
      main_start < HTML.find('class="feature-highlights"') and HTML.find('class="feature-highlights"') < main_end)
check("section is after Social Proof </section>",
      social_proof_end < HTML.find('class="feature-highlights"'))
check("Card 1 headline: One task, chosen for you.",
      "One task, chosen for you." in HTML)
check("Card 1 body: No list of twenty items to feel guilty about. Just the single thing that moves you forward.",
      "No list of twenty items to feel guilty about. Just the single thing that moves you forward." in HTML)
check("Card 2 headline: Check it. Done.",
      "Check it. Done." in HTML)
check("Card 2 body: One tap gives you the feeling of a finished task. Real progress instead of guilt.",
      "One tap gives you the feeling of a finished task — real progress instead of guilt." in HTML)
check("Card 3 headline: No guilt trips.",
      "No guilt trips." in HTML)
check("Card 3 body: No streaks, no shaming notifications. Small wins that quietly add up.",
      "No streaks, no shaming notifications. Small wins that quietly add up." in HTML)

print("== Design tokens ==")
root_block = re.search(r":root\s*\{[^}]*\}", CSS, re.S)
component_css = CSS[root_block.end():] if root_block else CSS

check("no hardcoded hex outside :root",
      not re.search(r"#[0-9a-fA-F]{3,6}", component_css))
check(".feature-highlights uses var(--color-background)",
      "var(--color-background)" in component_css)
check(".feature-highlights uses var(--color-surface)",
      "var(--color-surface)" in component_css)
check(".feature-highlights uses var(--color-text)",
      "var(--color-text)" in component_css)
check(".feature-highlights uses var(--color-text-muted)",
      "var(--color-text-muted)" in component_css)
check(".feature-highlights uses var(--color-primary)",
      "var(--color-primary)" in component_css)
check(".feature-highlights uses var(--radius-card)",
      "--radius-card" in component_css)
check(".feature-highlights uses var(--space-4)",
      "--space-4" in component_css)
check(".feature-highlights uses var(--space-6)",
      "--space-6" in component_css)
check("headlines use var(--color-primary) for emphasis",
      ".feature-highlight__headline" in CSS and "var(--color-primary)" in CSS)

print("== Motion & JS budget ==")
check("still exactly one @keyframes (no new animation)",
      CSS.count("@keyframes") == 1)
check("no new <script> tag added", HTML.count("<script") == 1)

print("== Backward compatibility ==")
check("exactly one <h1> still present", HTML.count("<h1") == 1)
check("hero headline still present",
      "Stop planning. Start finishing." in HTML)
check("social-proof section still present",
      'class="social-proof"' in HTML)

print()
print(f"Passed: {passed}  Failed: {failed}")
sys.exit(1 if failed else 0)
