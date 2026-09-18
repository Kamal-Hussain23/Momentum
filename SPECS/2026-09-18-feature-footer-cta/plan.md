# Plan: Footer / Secondary CTAs (TDD)

Follow the Red/Green TDD cycle: define the failing check first, write the
simplest code to make it pass, then polish. Keep it beginner-friendly.

## Task Group 1 — Red: write the acceptance check (fails first)

1. Create `check_footer.py` next to the sibling checks, asserting:
   - A `<footer>` element exists after `</main>` (and before `</body>`).
   - Heading "Ready to finish something?" is present.
   - Brand line "Momentum — One thing done. Every day." is present.
   - CTA markup: `class="btn btn--secondary"` linking to `href="#waitlist"`.
   - `.btn--secondary` CSS uses design tokens (transparent background, 1px
     `var(--color-primary)` border, primary text) and `var(--color-primary-wash)`
     on hover.
   - Token `--color-primary-wash` is defined inside `:root`.
   - No hardcoded hex/rgba outside `:root`; still exactly one `<h1>`, one
     `<script>`, one `@keyframes`.
   - Backward compatibility: hero, social-proof, feature-highlights,
     how-it-works, pricing and FAQ sections all still present.
2. Run it — confirm the new footer checks FAIL (footer not built yet) while the
   backward-compat checks pass.

## Task Group 2 — HTML structure

3. Add the `<footer>` to `build-lab/index.html` after `</main>` and before the
   `<script>` tag:
   - `<footer class="footer">`
     - `<h2>` heading: "Ready to finish something?"
     - `<a class="btn btn--secondary" href="#waitlist">Join the Waitlist</a>`
     - `<p class="footer__brand">Momentum — One thing done. Every day.</p>`
4. Re-run `check_footer.py` — the new HTML/copy checks should now pass (the CSS
   checks still fail).

## Task Group 3 — CSS styling (tokens only)

5. Add `--color-primary-wash: rgba(240, 168, 104, 0.1);` to `:root` in
   `build-lab/style.css`.
6. Add footer + secondary-button styles:
   - `.btn--secondary`: transparent background, `1px solid var(--color-primary)`
     border, `var(--color-primary)` text (pill radius inherited from `.btn`);
     hover sets background to `var(--color-primary-wash)`.
   - `.footer`: `var(--color-background)`, centered `max-width: 640px`,
     `--space-6` padding, `text-align: center`, top divider
     `1px solid var(--color-text-muted)` (matches the Social Proof pattern).
   - `.footer__brand`: `color: var(--color-text-muted)`.
7. Re-run `check_footer.py` — all checks should now pass.

## Task Group 4 — Motion & JS budget review

8. Confirm no new `@keyframes`, still exactly one `<script>` tag, and still
   exactly one `<h1>`; the FAQ accordion remains the only microinteraction.
9. Re-run `check_hero.py` (guards the single `@keyframes` budget).

## Task Group 5 — Verify no regressions (Green)

10. Run every acceptance suite head to tail and fix any failures:
    `check_hero.py`, `check_social_proof.py`, `check_feature_highlights.py`,
    `check_how_it_works.py`, `check_pricing.py`, `check_faq.py`,
    `check_footer.py`.

## Task Group 6 — Lint, polish, validate

11. Read the final `index.html` and `style.css` top to bottom and simplify
    anything a beginner would struggle with.
12. Serve the site (bind `0.0.0.0`, public Codio URL) and check the footer at
    375 / 768 / 1200 px: no horizontal scrollbar, readable text, CTA visible and
    clickable (jumps to the waitlist form).
13. Surface any differences between implementation and this spec to the founder;
    update the spec only after founder approval.