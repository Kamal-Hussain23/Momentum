# Plan: How It Works / Product Demo (TDD)

Follow the Red/Green TDD cycle: define the failing check first, write the simplest
code to make it pass, then polish. Keep it beginner-friendly.

## Task Group 1 — Acceptance check (RED)

1. Write `check_how_it_works.py` in this feature folder. It checks:
   - a `<section>` for how it works exists inside `<main>`, after the Feature Highlights
     `</section>`
   - three workflow steps are present with the exact copy from MISSION.md
   - no new `@keyframes` and no new `<script>` were added (motion budget)
   - no hardcoded hex appears outside `:root` in `style.css`
   - the Hero, Social Proof, and Feature Highlights sections are untouched
2. Run it against the current page. It must FAIL → confirms the feature is missing (Red).

## Task Group 2 — HTML section (GREEN start)

3. Add a `<section class="how-it-works">` inside `<main>`, placed directly
   after the Feature Highlights `</section>` in `build-lab/index.html`.
4. Inside it, three workflow steps with `class="how-it-works__step"`:
   - Step 1: headline "Set it" + body copy
   - Step 2: headline "Do it" + body copy
   - Step 3: headline "Check it" + body copy
5. Each step wraps an `<h3>` for the headline and a `<p>` for the body copy.
6. Wire the Google Fonts links for Manrope and Inter in `<head>` (already present).

## Task Group 3 — CSS (GREEN completion)

7. Add `.how-it-works` and `.how-it-works__step` styles in
   `build-lab/style.css`:
   - uses `--color-background`, `--color-surface`, `--color-text`,
     `--color-text-muted`, `--color-primary`
   - max-width `640px`, centered, `text-align: center`
   - step `12px` radius (`--radius-card`), `--space-4` between steps,
     `--space-6` below the section
   - headline in `--color-primary` for emphasis
8. Run `check_how_it_works.py`. All checks must PASS (Green).

## Task Group 4 — Backward compatibility check

9. Re-run the Feature Highlights, Social Proof, and Hero acceptance checks from
   their respective spec folders and confirm all checks still pass (the new section
   must not break existing features).

## Task Group 5 — Review & simplify

10. Read the final `index.html` and `style.css` top to bottom. Simplify anything
    that looks obscure to a beginner. Confirm no copy drift from MISSION.md Section 3.
11. Optionally page in a headless browser at 375 / 768 / 1200 px to confirm no
    horizontal scroll and that the section sits centered below Feature Highlights.

## Task Group 6 — Mutation test (verify checks are non-vacuous)

12. Mutate a copy of `index.html` to remove the how it works section and
    verify `check_how_it_works.py` fails; then restore the original and
    mutate the copy to alter the copy text and verify the check fails again.