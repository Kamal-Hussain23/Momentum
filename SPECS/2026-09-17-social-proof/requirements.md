# Feature: Social Proof / Credibility Section

Date: 2026-09-17
Project: Momentum

## Scope

Add the second landing-page section — Social Proof / Credibility — directly
after the existing Hero section (`build-lab/SPECS/2026-09-17-hero-section/`).
This section builds trust with the target audience by showing that Momentum
understands them. It appears in `build-lab/index.html` and is styled in
`build-lab/style.css`.

## Context

A startup without customers cannot invent testimonials or stats. The honest
form of social proof on a waitlist landing page is relatability: statements the
target persona recognises as true about themselves. This matches the brand
personality words (approachable, trustworthy).

## In Scope

- One new `<section>` named for social proof, placed inside `<main>` after the
  Hero section.
- The two copy lines from `build-lab/MISSION.md` Section 3, item 2:
  1. "Built for people who work full-time and study on the side."
  2. "You've tried the lists and the calendars. Momentum is different — because
     there's only ever one thing to do."
- Simple centered layout using design tokens only.
- A subtle divider separating this section from the Hero.

## Out of Scope

- Fictional testimonials with names, jobs, or photos.
- Number/stat strips (waitlist counts, percentages).
- Scroll animations or any JavaScript — **no motion** for this feature
  (founder decision: keep the site's single scroll effect unused for now).
- Any change to the Hero/Navbar feature or its acceptance checks.

## Design Source

All visual decisions come from `build-lab/MISSION.md` Section 2. No new CSS
tokens or hardcoded hex values are created.

- Background: page `--color-background` (the section sits on the page bg)
- Text: `--color-text-muted` for the statements
- Emphasis ("Momentum is different"): `--color-primary`
- Divider: `1px` solid `--color-text-muted`
- Spacing: `--space-6` between sections, `--space-4` between lines
- Max content width: `640px` to match the Hero text column

## Decisions

- Relatability statements (option A) chosen over testimonials and stat strips.
- No motion (founder decision, question set on 2026-09-17).
- Git branching skipped — workspace is not yet a git repository.
- Backward compatibility with the Hero feature is REQUIRED: this feature must
  not modify the Hero markup, its styles, or break `check_hero.py`.

## Engineering Constraints (from SPECS/TECH.md)

- Plain HTML5 + CSS3, no frameworks, no npm packages.
- Semantic tags: `<section>` for the new block.
- All colors/fonts/radii via CSS custom properties — no hardcoded hex codes.
- Motion budget respected: this feature adds zero animations.
- Keep it simple and readable for beginners.

## Logging / Storage Note

This is a static frontend landing page. There is no business logic and no
backend, so logging decorators and SQLite persistence do not apply to this
feature. Email collection goes live in a later backend phase, out of scope
here.