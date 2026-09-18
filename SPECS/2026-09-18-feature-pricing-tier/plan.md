# Plan: Pricing / Tiers

Follow the Red/Green TDD cycle: define the failing check first, write the simplest
code to make it pass, then polish. Keep it beginner-friendly.

> **Decision (founder-confirmed 2026-09-18):** the Pricing section carries no
> CTA button — only its heading and waitlist-only body copy. Task Group 2 below
> originally planned a "Waitlist CTA or benefit statement"; that step is
> superseded by this decision. The waitlist/early-access message is conveyed by
> the copy, with conversion driven by the navbar, hero, and footer CTAs.

## Task Group 1 — Define the Pricing / Tiers section

1. Write the acceptance check: a "Pricing / Tiers" section exists on the page with
   copy stating "Waitlist only — no pricing yet. Mention early access on the waitlist instead."
2. Add the Pricing / Tiers HTML + CSS using the design tokens (Surface bg, Text
   Primary, Text Muted, no pricing tables or price inputs).
3. Verify the check passes.

## Task Group 2 — Copy and content

3. Add the approved copy to `build-lab/index.html` in the Pricing / Tiers section:
   - Heading text and body paragraph matching MISSION.md Section 3
   - Waitlist CTA or benefit statement
4. Verify the copy matches exactly.

## Task Group 3 — Visual validation

5. Write the acceptance check: Pricing / Tiers section uses correct design tokens,
   no hardcoded hex colors, no pricing tables, correct border-radius and button styles
6. Add the section HTML and styling using CSS custom properties only.
7. Verify the check passes.

## Task Group 4 — Placement and flow

8. Write the acceptance check: Pricing / Tiers section appears in the correct
   position on the page (after Feature Highlights / Value Drivers, before FAQ /
   Objection Handling).
9. Review the full page narrative flow to ensure logical ordering.
10. Verify the check passes.

## Task Group 5 — Lint, review, validate

11. Run any available checks and fix issues from the QA audit in SPECS/ROADMAP.md
    Stage 5.
12. Read through the final files top to bottom and simplify anything that looks
    obscure to a beginner, especially ensuring no pricing-related elements were
    accidentally introduced.
13. Confirm the section communicates "waitlist only" and "early access" clearly.