# Plan: Hero Section (TDD)

Follow the Red/Green TDD cycle: define the failing check first, write the
simplest code to make it pass, then polish. Keep it beginner-friendly.

## Task Group 1 — Design tokens & HTML shell (Foundation)

1. Add the Momentum design tokens (colors, fonts, radii, spacing) as CSS custom
   properties in `build-lab/style.css` (replace the placeholder tokens).
2. Replace the starter title in `build-lab/index.html` with "Momentum".
3. Create the semantic shell: `<header>` (navbar) and `<main>` with a hero
   `<section>` inside.
4. Wire the Google Fonts links for Manrope and Inter in `<head>`.

## Task Group 2 — Navbar (red check first)

5. Write the acceptance check: navbar renders "Momentum" brand left, one link
   to "Join the Waitlist" right, and stays visible when scrolling (sticky).
6. Add the navbar HTML + CSS using the design tokens (Surface bg, pill
   primary button for the link).
7. Verify the navbar check passes.

## Task Group 3 — Hero content & waitlist form

8. Write the acceptance check: hero shows headline, subheadline, email input,
   and "Join the Waitlist" button; the form uses a visible label and proper
   email input type.
9. Add the hero HTML + CSS (Background bg, Manrope headline, pill primary
   button). All values from tokens — no hardcoded hex.
10. Verify the check passes.

## Task Group 4 — CSS-only phone mockup

11. Write the acceptance check: an element styled like a phone shows the
    "Today's task" card, an ember checkmark, and no `<img>` tags.
12. Add the mockup with HTML + CSS cards (Surface card, `12px` radius,
    Accent checkmark).
13. Verify the check passes.

## Task Group 5 — Responsive layout

14. Write the acceptance check: on mobile the hero stacks vertically; on
    desktop (min-width ~900px) the text sits left and the phone mockup sits
    right, with the navbar brand left / link right.
15. Add media queries using the spacing tokens.
16. Verify at mobile (375px), tablet (768px), desktop (1200px) widths.

## Task Group 6 — One hero animation (motion budget)

17. Write the acceptance check: exactly one entrance animation — the hero text
    fades/slides in once on page load — and it doesn't block reading.
18. Add the animation with CSS `@keyframes` (no JS needed yet).
19. Verify the check passes.

## Task Group 7 — Lint, review, validate

20. Run any available HTML/CSS checks (e.g. a linter or validator if present)
    and fix Critical + Important issues from the QA audit in
    `SPECS/ROADMAP.md` Stage 5.
21. Read through the final files top to bottom and simplify anything that looks
    obscure to a beginner.