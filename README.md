# Momentum

**One thing done. Every day.**

## The problem it solves

Busy professionals who study on the side (a certification, a course, a promotion-lane
skill) always have plans — but they don't do them. They feel **"busy but stuck."** The
guilt that follows sets off a loop: procrastinate → feel guilty → stress → burnout →
procrastinate more. They already have calendars and to-do lists; the lists just hand
them twenty things at once and none of them get finished.

## The solution

Momentum is an app that closes the gap between planning and doing by narrowing each day
down to a single **Most Important Task (MIT)**. It is not another calendar or to-do
list. There's only ever one thing to do, so that one thing is small enough to actually
get done.

This repository is the **frontend landing page** for Momentum. It names the problem,
presents the solution, and collects waitlist emails — one signup, one click, no friction.

## Key features

- **Hero section** — "Stop planning. Start finishing." with a waitlist form and a
  CSS-only phone mockup showing the daily task card.
- **Social proof** — built for people who work full-time and study on the side.
- **Feature highlights** — "One task, chosen for you", "Check it. Done.", "No guilt
  trips."
- **How it works** — a numbered 3-step path: **Set it → Do it → Check it**, with
  visible separators so each step reads as its own milestone.
- **FAQ accordion** — opens one answer at a time, accessible via ARIA state.
- **Waitlist form** — collects an email address with a single primary CTA.
- **Subtle motion** — a clean hero entrance animation, a smooth hover lift on the
  feature cards, and full `prefers-reduced-motion` support.

## Tech stack

Everything is vanilla — no frameworks, no build tools, no npm packages.

- **HTML5** — semantic markup, ARIA attribtes for the FAQ accordion
- **CSS3** — design tokens as CSS custom properties, Flexbox layouts, keyframe
  animations, and responsive breakpoints
- **JavaScript** — vanilla JS for the FAQ accordion (no libraries)
- **Fonts** — Manrope (headings) + Inter (body) via Google Fonts
- **Design system** — the color palette, typography, button styles, and radius rules
  are locked in `MISSION.md` and used everywhere via `:root` tokens
- **Local preview** — a simple Python HTTP server in the Codio box
  (`python3 -m http.server 3000 --bind 0.0.0.0`)

## Reflection

This project taught us that you don't need heavy tools to make something feel
professional — you need **consistency and restraint**.

The design tokens in `MISSION.md` were the biggest win. Because every color, radius, and
font lived in one place in CSS, the whole page stayed on-brand without thinking about
it. Adding new sections became a matter of reusing tokens, never reinventing them.

We also learned to respect motion. It's tempting to add a scroll-triggered animation to
every block, but visitors see the page once — so we kept a single hero entrance
animation and one hover effect, and made sure both respect `prefers-reduced-motion`.
The hover lift is animated with `transform` (not layout properties), so it stays smooth.

Along the way we learned the value of **verifying instead of assuming**. Every design
choice — the hover lift timing, the stagger of the hero entrance, the step separators —
was measured in a real headless browser to confirm it felt snappy, matched the tokens
exactly, and produced zero console errors.

The biggest surprise was how much the "one thing" constraint helped the design too. One
task, one CTA, one conversion goal — the same discipline that shapes the product shaped
the page.