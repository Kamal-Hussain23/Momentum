# Feature: Hero Section (with Navbar + Waitlist CTA)

Date: 2026-09-17
Project: Momentum

## Scope

Build the first visible part of the landing page: a sticky navbar and a hero
section that names the problem, presents the solution, and collects waitlist
emails. This is Step 1 of Stage 5 in `SPECS/ROADMAP.md` (base shell + hero).

## In Scope

- Sticky navigation bar
- Hero section with:
  - Headline
  - Subheadline
  - Waitlist email form (email input + "Join the Waitlist" button)
  - CSS-only phone mockup showing the "one Most Important Task" card
- CSS design tokens (custom properties) in `style.css`
- One hero entrance animation (fits the motion budget)
- Responsive layout (mobile → desktop)

## Out of Scope (later features)

- Other page sections (Social Proof, Features, How It Works, FAQ, Footer)
- Real email storage / backend — the form visually captures a valid email only
- Scroll animations, other microinteractions, form submission handling
- Second CTA anywhere on the page

## Design Source

All visual decisions come from `build-lab/MISSION.md` Section 2 — Visual
Identity & Design System. No values are invented outside those tokens.

- Palette: Background `#1C1917`, Surface `#292524`, Primary `#F0A868`,
  Secondary `#F7C890`, Accent `#FF7E67`, Text `#FAF9F6`, Muted `#A8A29E`
- Fonts: Manrope (700–800 headings), Inter (400–500 body)
- Buttons: pill `999px`, primary = ember bg with dark text `#1C1917`
- Radius: cards `12px`, small elements `6px`

## Copy (from MISSION.md Section 3)

- Navbar brand: **Momentum**
- Headline: **"Stop planning. Start finishing."**
- Subheadline: "Momentum shows you your one Most Important Task each day. One
  small thing done beats a perfect plan, every time."
- CTA button: **"Join the Waitlist"**
- Phone mockup card text: "Today's task: finish the course module on databases"
  with an ember checkmark

## Engineering Constraints (from SPECS/TECH.md)

- Plain HTML5 + CSS3 + vanilla JS. No frameworks, no npm packages.
- Semantic tags: `<header>`, `<nav>`, `<section>`, `<main>`, etc.
- All colors/fonts/radii via CSS custom properties — no hardcoded hex codes.
- Motion budget: 1 hero effect max for this feature. Every animation has a
  purpose.
- Keep it simple and readable for beginners.

## Decisions

- Navbar is included in this feature, not a separate spec.
- The waitlist CTA in the hero includes an inline email input.
- The phone mockup is CSS-only, no image files required.