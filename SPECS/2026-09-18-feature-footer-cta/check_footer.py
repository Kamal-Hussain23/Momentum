#!/usr/bin/env python3
"""Acceptance checks for the Footer / Secondary CTAs feature.

Run:  python3 check_footer.py
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


print("== Content: footer element, placement & verbatim copy ==")
footer_start = HTML.find("<footer")
main_end = HTML.find("</main>")
body_end = HTML.find("</body>")

check("<footer> element exists", "<footer" in HTML)
check("footer comes after </main>", main_end < footer_start)
check("footer comes before </body>", footer_start < body_end)
check("footer is the last element (nothing between footer and </body>)",
      "</body>" in HTML[footer_start:])
check("heading reads: Ready to finish something?",
      "Ready to finish something?" in HTML)
check("brand line verbatim: Momentum — One thing done. Every day.",
      "Momentum — One thing done. Every day." in HTML)

print("== CTA: secondary outline button linking to the waitlist ==")
footer_block = HTML[footer_start:HTML.find("</footer>", footer_start)]
check("CTA text 'Join the Waitlist' in footer",
      "Join the Waitlist" in footer_block)
check("CTA uses btn btn--secondary",
      'class="btn btn--secondary"' in footer_block)
check("CTA links to #waitlist", 'href="#waitlist"' in footer_block)
check("CTA is a real <a> element", "<a " in footer_block)

print("== Design tokens ==")
root_block = re.search(r":root\s*\{[^}]*\}", CSS, re.S)
root_css = root_block.group(0) if root_block else ""
component_css = CSS[root_block.end():] if root_block else CSS

check("--color-primary-wash token defined inside :root",
      "--color-primary-wash: rgba(240, 168, 104, 0.1)" in root_css)
check("no hardcoded hex outside :root",
      not re.search(r"#[0-9a-fA-F]{3,6}", component_css))
check("no hardcoded rgba outside :root",
      "rgba(" not in component_css)
check(".btn--secondary uses var(--color-primary)",
      ".btn--secondary" in CSS and "var(--color-primary)" in component_css)
check(".btn--secondary has transparent background",
      "background: transparent" in component_css or
      "background-color: transparent" in component_css)
check(".btn--secondary has 1px primary border",
      "1px solid var(--color-primary)" in component_css)
check(".btn--secondary hover uses warm wash",
      "var(--color-primary-wash)" in component_css)
check(".footer uses var(--color-background)",
      "var(--color-background)" in component_css)
check(".footer uses var(--color-text-muted)",
      "var(--color-text-muted)" in component_css)
check(".footer uses var(--space-6)",
      "--space-6" in component_css)

print("== Motion & JS budget ==")
check("still exactly one @keyframes (no new animation)",
      CSS.count("@keyframes") == 1)
check("still exactly one <script> tag", HTML.count("<script") == 1)

print("== Backward compatibility ==")
check("exactly one <h1> still present", HTML.count("<h1") == 1)
check("hero headline still present",
      "Stop planning. Start finishing." in HTML)
check("social-proof section still present",
      'class="social-proof"' in HTML)
check("feature-highlights section still present",
      'class="feature-highlights"' in HTML)
check("how-it-works section still present",
      'class="how-it-works"' in HTML)
check("pricing section still present",
      'class="pricing"' in HTML)
check("faq section still present",
      'class="faq"' in HTML)

print()
print(f"Passed: {passed}  Failed: {failed}")
sys.exit(1 if failed else 0)