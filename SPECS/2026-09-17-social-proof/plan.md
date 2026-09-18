# Plan: Social Proof / Credibility Section (TDD)

Follow the Red/Green TDD cycle: write the acceptance check first (it must fail
against the current page), then implement the simplest code to make it pass,
then review. Keep it beginner-friendly.

## Task Group 1 — Acceptance check (RED)

1. Write `check_social_proof.py` in this feature folder. It checks:
   - a `<section>` for social proof exists inside `<main>`, after the Hero
   - both copy lines from `MISSION.md` Section 3 appear verbatim
   - no new `@keyframes` and no new `<script>` were added (motion budget)
   - no hardcoded hex appears outside `:root` in `style.css`
   - exactly one `<h1>` still exists (Hero untouched)
2. Run it against the current page. It must FAIL → confirms the feature is
   missing (Red).

## Task Group 2 — HTML section (GREEN start)

3. Add a `<section class="social-proof">` inside `<main>`, placed directly
   after the Hero `</section>` in `build-lab/index.html`.
4. Inside it, two paragraphs with the exact copy from `MISSION.md`:
   - `<p class="social-proof__line">Built for people who work full-time and
     study on the side.</p>`
   - `<p class="social-proof__line">You've tried the lists and the calendars.
     <span class="social-proof__emphasis">Momentum is different</span> —
     because there's only ever one thing to do.</p>`

## Task Group 3 — CSS (GREEN completion)

5. Add `.social-proof` styles in `build-lab/style.css`:
   - uses `--color-background`, `--color-text-muted`, `--color-primary`
   - max-width `640px`, centered, `text-align: center`
   - top divider: `1px solid var(--color-text-muted)`
   - section spacing via `--space-6`
6. Run `check_social_proof.py`. All checks must PASS (Green).

## Task Group 4 — Backward compatibility check

7. Re-run the Hero acceptance checks from
   `build-lab/SPECS/2026-09-17-hero-section/check_hero.py`. All 23 must still
   pass (the social-proof section must not break the Hero).
8. Verify the page still serves (HTTP 200) locally.

## Task Group 5 — Review & simplify

9. Read the final `index.html` and `style.css` top to bottom. Simplify anything
   that looks obscure to a beginner. Confirm no copy drift from `MISSION.md`
   Section 3.
10. Optionally page in a headless browser at 375 / 768 / 1200 px to confirm no
    horizontal scroll and that the section sits centered under the Hero.