#!/usr/bin/env python3
"""Acceptance checks for the Hero section feature.

Run:  python3 check_hero.py
Exits 0 when every check passes, 1 when any fails.
"""

import os
import re
import sys

# Repo root = two folders up from this script (SPECS/<feature>/check_hero.py)
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

HTML = open(os.path.join(REPO, "build-lab", "index.html"), encoding="utf-8").read()
CSS = open(os.path.join(REPO, "build-lab", "style.css"), encoding="utf-8").read()

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


print("== Copy & content ==")
check("title is 'Momentum'", "<title>Momentum</title>" in HTML)
check("headline: Stop planning. Start finishing.",
      "Stop planning. Start finishing." in HTML)
check("subheadline copy present",
      "One small thing done beats a perfect plan, every time." in HTML)
check("button text: Join the Waitlist", "Join the Waitlist" in HTML)
check("phone task text present",
      "Finish the course module on databases" in HTML)

print("== Structure & semantics ==")
check("exactly one <h1>", HTML.count("<h1") == 1)
check("sticky navbar present", "navbar" in HTML and "sticky" in CSS)
check("brand text 'Momentum' in navbar", "Momentum" in HTML)
check("email input uses type=\"email\"", 'type="email"' in HTML)
check("visible <label> with for attribute",
      re.search(r'<label[^>]*for="[^"]+"', HTML) is not None)
check("phone mockup element exists", "phone" in HTML)
check("task card ember checkmark element", "task-card__check" in HTML)
check("no <img> tags", "<img" not in HTML)
check("Google Fonts: Manrope + Inter",
      "Manrope" in HTML and "Inter" in HTML)

print("== CSS tokens & rules ==")
root_block = re.search(r":root\s*\{[^}]*\}", CSS, re.S)
root_hexes = set(re.findall(r"#[0-9a-fA-F]{3,6}", root_block.group(0))) if root_block else set()
component_css = CSS[root_block.end():] if root_block else CSS
check("all 7 palette tokens defined in :root",
      len(root_hexes & {"#1C1917", "#292524", "#F0A868", "#F7C890",
                        "#FF7E67", "#FAF9F6", "#A8A29E"}) == 7)
check("no hardcoded hex outside :root",
      not re.search(r"#[0-9a-fA-F]{3,6}", component_css))
check("button radius via pill token", "--radius-pill" in root_block.group(0))
check("card radius via 12px token", "--radius-card" in root_block.group(0))
check("media query for desktop (min-width 900px)",
      re.search(r"@media[^{]*\(min-width:\s*900px\)", CSS) is not None)

print("== Motion budget ==")
check("exactly one @keyframes", CSS.count("@keyframes") == 1)
check("hero entrance animation defined and applied",
      CSS.count("rise-in") >= 2)

print("== Focus & contrast ==")
check("focus ring uses accent (2px outline)",
      re.search(r"outline:\s*2px\s+[^;]*accent", CSS) is not None
      or ":focus-visible" in CSS and "--color-accent" in CSS)
check("primary button uses dark on-primary token",
      "--color-on-primary" in CSS)

print()
print(f"Passed: {passed}  Failed: {failed}")
sys.exit(1 if failed else 0)