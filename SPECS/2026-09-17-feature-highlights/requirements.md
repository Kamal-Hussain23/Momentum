# Feature: Feature Highlights / Value Drivers

Date: 2026-09-17
Project: Momentum

## Scope

Add the third landing-page section — Feature Highlights / Value Drivers — positioned
below the Social Proof section. This section communicates the core benefits of Momentum
using three concise, benefit-focused cards. It appears in `build-lab/index.html` and
is styled in `build-lab/style.css`.

## In Scope

- One new `<section>` named for feature highlights, placed inside `<main>` after the
  Social Proof section.
- Three value driver cards, each with:
  - A bold headline (the "one thing" benefit)
  - A short descriptive paragraph
- Design tokens only (no hardcoded hex values).
- Visual style consistent with the Warm Ember palette and token-based design system.

## Out of Scope

- Interactive card toggles or hover animations (no motion for this feature, consistent
  with the founder's social-proof decision).
- Integration with backend or user accounts.
- Secondary CTA placement (handled in Feature 7).

## Design Source

All visual decisions come from `build-lab/MISSION.md` Section 2 and the Social Proof
section. No values are invented outside those tokens.

- Background: `--color-background` (page bg)
- Card background: `--color-surface`
- Primary text: `--color-text` (`#FAF9F6`)
- Muted text: `--color-text-muted` (`#A8A29E`)
- Accent/emphasis: `--color-primary` (`#F0A868`) — used sparingly for the "one thing" focus
- Border radius: `--radius-card` (`12px`)
- Spacing: `--space-4` between card and `--space-6` below the section

## Copy (from MISSION.md Section 3)

1. **"One task, chosen for you."** — "No list of twenty items to feel guilty about.
   Just the single thing that moves you forward."
2. **"Check it. Done."** — "One tap gives you the feeling of a finished task — real
   progress instead of guilt."
3. **"No guilt trips."** — "No streaks, no shaming notifications. Small wins that
   quietly add up."

## Engineering Constraints (from SPECS/TECH.md)

- Plain HTML5 + CSS3, no frameworks, no npm packages.
- Semantic tags: `<section>` for the feature highlights block.
- All colors/fonts/radii via CSS custom properties — no hardcoded hex codes.
- Motion budget respected: this feature adds zero animations (consistent with the
  social-proof decision).
- Keep it simple and readable for beginners.

## Logging / Storage Note

This is a static frontend landing page. There is no business logic and no backend,
so logging decorators and SQLite persistence do not apply to this feature. Email
collection goes live in a later backend phase, out of scope here.