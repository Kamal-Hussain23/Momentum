#!/usr/bin/env python3
"""Acceptance checks for the Social Proof section feature.

Run:  python3 check_social_proof.py
Exits 0 when every check passes, 1 when any fails.
"""

import os
import re
import sys

# Repo root = three folders up from this script (build-lab/SPECS/<feature>/)
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
# Strip inner markup (e.g. the emphasis span) so "verbatim" means the visible text
plain_html = (HTML
              .replace('<span class="social-proof__emphasis">', "")
              .replace("</span>", ""))
check("social-proof <section> exists", 'class="social-proof"' in HTML)
check("section sits inside <main>",
      HTML.find("<main>") < HTML.find('class="social-proof"'))
check("section is after the hero section",
      HTML.find('class="hero"') < HTML.find('class="social-proof"'))
check("line 1 verbatim: Built for people...",
      "Built for people who work full-time and study on the side." in HTML)
check("line 2 verbatim: You've tried the lists...",
      "You've tried the lists and the calendars. Momentum is different"
      " — because there's only ever one thing to do." in plain_html)
check("emphasis span for 'Momentum is different'",
      'class="social-proof__emphasis"' in HTML)

print("== No invented proof ==")
check("no fake names/testimonials",
      not re.search(r'"[^"]+":\s*"[^"]+"', plain_html.replace(
          "You've tried the lists and the calendars. Momentum is different"
          " — because there's only ever one thing to do.", "")))
check("no stat numbers (waitlist counts / percentages)",
      not re.search(r'\b\d{2,3}\s*(on the waitlist|%|percent)\b', HTML))

print("== Motion & JS budget ==")
check("still exactly one @keyframes (no new animation)",
      CSS.count("@keyframes") == 1)
check("no new <script> tag added", HTML.count("<script") == 1)

print("== Design tokens ==")
root_block = re.search(r":root\s*\{[^}]*\}", CSS, re.S)
component_css = CSS[root_block.end():] if root_block else CSS
check("no hardcoded hex outside :root",
      not re.search(r"#[0-9a-fA-F]{3,6}", component_css))

social_proof_css = component_css[component_css.find(".social-proof"):]
check(".social-proof styles use only tokens",
      "var(--color-background)" in social_proof_css
      and "var(--color-text-muted)" in social_proof_css
      and "var(--color-primary)" in social_proof_css
      and not re.search(r"#[0-9a-fA-F]{3,6}", social_proof_css))
check("max-width 640px + centered text",
      "max-width: 640px" in social_proof_css
      and "text-align: center" in social_proof_css)
check("divider uses muted token",
      "1px solid var(--color-text-muted)" in social_proof_css)

print("== Hero untouched ==")
check("exactly one <h1> still present", HTML.count("<h1") == 1)
check("hero headline still present",
      "Stop planning. Start finishing." in HTML)

print()
print(f"Passed: {passed}  Failed: {failed}")
sys.exit(1 if failed else 0)