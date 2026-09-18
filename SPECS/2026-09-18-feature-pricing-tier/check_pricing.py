#!/usr/bin/env python3
"""Acceptance checks for the Pricing / Tiers feature.

Run:  python3 check_pricing.py
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


print("== Content: section, copy & placement ==")
main_start = HTML.find("<main>")
main_end = HTML.find("</main>")
fh_start = HTML.find('class="feature-highlights"')
fh_end = HTML.find("</section>", fh_start)
wh_start = HTML.find('class="how-it-works"')
wh_end = HTML.find("</section>", wh_start)
pricing_start = HTML.find('class="pricing"')

check("pricing <section> exists", 'class="pricing"' in HTML)
check("section sits inside <main>",
      main_start < pricing_start and pricing_start < main_end)
check("section is after Feature Highlights </section>",
      fh_end < pricing_start)
check("section is after How It Works </section>",
      wh_end < pricing_start)
check("heading reads: Pricing / Tiers",
      "Pricing / Tiers" in HTML)
check("body copy verbatim",
      "Waitlist only — no pricing yet. Mention early access on the waitlist instead." in HTML)
pricing_end = HTML.find("</section>", pricing_start)
pricing_section = HTML[pricing_start:pricing_end]
check("no CTA button in pricing section",
      "Join the Waitlist" not in pricing_section)

print("== No pricing table / payment elements ==")
check("no <table> tag on the page", "<table" not in HTML.lower())
check("no number-type input",
      not re.search(r"<input[^>]*type=[\"']number[\"']", HTML, re.I))
check("no dollar sign ($)", "$" not in HTML)
check("no 'subscribe' wording", "subscribe" not in HTML.lower())
check("no 'per month' wording", "per month" not in HTML.lower())
check("no 'billing' wording", "billing" not in HTML.lower())

print("== Design tokens ==")
root_block = re.search(r":root\s*\{[^}]*\}", CSS, re.S)
component_css = CSS[root_block.end():] if root_block else CSS

check("no hardcoded hex outside :root",
      not re.search(r"#[0-9a-fA-F]{3,6}", component_css))
check(".pricing uses var(--color-background)",
      "var(--color-background)" in component_css)
check(".pricing uses var(--color-text)",
      "var(--color-text)" in component_css)
check(".pricing uses var(--color-text-muted)",
      "var(--color-text-muted)" in component_css)
check(".pricing__heading uses var(--font-heading)",
      ".pricing__heading" in CSS and "var(--font-heading)" in CSS)
check(".pricing uses var(--space-4)",
      "--space-4" in component_css)
check(".pricing uses var(--space-6)",
      "--space-6" in component_css)

print("== Motion & JS budget ==")
check("still exactly one @keyframes (no new animation)",
      CSS.count("@keyframes") == 1)
check("no new <script> tag added", HTML.count("<script") == 1)

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

print()
print(f"Passed: {passed}  Failed: {failed}")
sys.exit(1 if failed else 0)