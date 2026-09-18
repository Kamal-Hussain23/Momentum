# Feature: How It Works / Product Demo

Date: 2026-09-18
Project: Momentum

## Scope

Add the fourth landing-page section — How It Works / Product Demo — positioned
below the Feature Highlights / Value Drivers section. This section communicates the
core workflow of Momentum using three concise steps. It appears in
`build-lab/index.html` and is styled in `build-lab/style.css`.

## In Scope

- One new `<section>` named for how it works, placed inside `<main>` after the
  Feature Highlights `</section>`.
- Three workflow steps, each with:
  - A bold headline (the action verb, e.g. "Set it", "Do it", "Check it")
  - A short descriptive paragraph
- Design tokens only (no hardcoded hex values).
- Visual style consistent with the Warm Ember palette and token-based design system.
- Motion budget respected: this feature adds zero animations (consistent with the
  feature-highlights and social-proof decisions).

## Out of Scope

- Interactive step toggles or hover animations (no motion, consistent with the
  founder's decision across social-proof and feature-highlights).
- Integration with backend or user accounts.
- Pricing tier information (out of scope — waitlist only).
- Secondary CTA placement (handled in Feature 7 / Footer).

## Design Source

All visual decisions come from `build-lab/MISSION.md` Section 3 and the design
tokens established in the Feature Highlights section. No values are invented
outside those tokens.

- Background: `--color-background` (page bg)
- Card background: `--color-surface`
- Primary text: `--color-text` (`#FAF9F6`)
- Muted text: `--color-text-muted` (`#A8A29E`)
- Accent/emphasis: `--color-primary` (`#F0A868`) — used sparingly for step emphasis
- Border radius: `--radius-card` (`12px`)
- Spacing: `--space-4` between steps, `--space-6` below the section

## Copy (from MISSION.md Section 3)

1. **"Set it."** — "Each evening, name the one task that matters most tomorrow."
2. **"Do it."** — "Focus on just that one thing. Nothing else to distract you."
3. **"Check it."** — "One tap tells the whole day 'done.' Repeat tomorrow."

## Engineering Constraints (from SPECS/TECH.md)

- Plain HTML5 + CSS3, no frameworks, no npm packages.
- Semantic tags: `<section>` for the how-it-works block.
- All colors/fonts/radii via CSS custom properties — no hardcoded hex codes.
- Motion budget respected: this feature adds zero animations (consistent with the
  social-proof and feature-highlights decisions).
- Keep it simple and readable for beginners.

## Logging / Storage Note

This is a static frontend landing page. There is no business logic and no backend,
so logging decorators and SQLite persistence do not apply to this feature.

(End of file - total 62 lines)