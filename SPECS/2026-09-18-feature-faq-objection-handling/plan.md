# Plan: FAQ / Objection Handling (TDD)

Follow the Red/Green TDD cycle: define the failing check first, write the
simplest code to make it pass, then polish. Keep it beginner-friendly.

## Task Group 1 — Red: write the acceptance check (fails first)

1. Create `check_faq.py` next to the sibling checks, asserting:
   - FAQ `<section>` exists inside `<main>`, directly after Pricing `</section>`.
   - Heading reads: "Questions?"
   - All four Q&A pairs present verbatim (exact strings from MISSION.md §3.6).
   - Each question is a `<button>` carrying `aria-expanded` and `aria-controls`;
     answer panels exist with matching `id`s.
   - Exactly one `<script>` tag and one `@keyframes` still hold.
   - No hardcoded hex outside `:root`; FAQ CSS uses design tokens.
   - Backward compatibility: hero, social-proof, feature-highlights,
     how-it-works and pricing sections all still present; exactly one `<h1>`.
2. Run it — confirm the new FAQ checks FAIL (section is not built yet) while the
   backward-compat checks pass.

## Task Group 2 — HTML structure

3. Add the FAQ section to `build-lab/index.html` after the Pricing `</section>`
   and before `</main>`:
   - `<section class="faq" aria-label="Frequently asked questions">`
   - `<h2>` heading "Questions?"
   - Four items: `<div class="faq__item">` containing a `<button>` (question,
     `aria-expanded="false"`, `aria-controls="faq-panel-N"`) and a panel
     `<div class="faq__panel" id="faq-panel-N" hidden>`. Use the exact FAQ copy.
4. Re-run `check_faq.py` — the new checks should now pass.

## Task Group 3 — CSS styling (tokens only)

5. Add FAQ styles to `build-lab/style.css`:
   - `.faq` matches the sibling section pattern: `--color-background`, centered,
     `max-width: 640px`, `--space-6` padding.
   - Items are Surface cards (`--color-surface`, `--radius-card`).
   - Question buttons: full-width, text-left, Text Primary, Manrope-ish weight
     via `--font-heading`, `--color-primary` hint text for the open state.
   - Panel: Text Muted answer text; open/close animated with a CSS **transition**
     (e.g. `max-height` or `opacity`), no new `@keyframes`.
   - Focus ring already handled globally (`--color-accent`).
6. Re-run `check_faq.py` plus `check_hero.py` (must stay at one `@keyframes`).

## Task Group 4 — Vanilla JS behaviour

7. Add a small accordion script to `build-lab/script.js`:
   - Select all FAQ `<button>`s.
   - On click: if the item is open, close it; otherwise close every item and open
     the clicked one (exclusive). Toggle the `hidden` attribute / open class and
     set `aria-expanded` truthfully.
   - Wrap in a feature check so it does nothing when the FAQ section is absent.
8. Re-run `check_faq.py`; manually confirm open/close and exclusivity in a
   browser.

## Task Group 5 — Verify no regressions (Green)

9. Run every acceptance suite head to tail and fix any failures:
   `check_hero.py`, `check_social_proof.py`, `check_feature_highlights.py`,
   `check_how_it_works.py`, `check_pricing.py`, `check_faq.py`.
10. Confirm `index.html` still has exactly one `<h1>` and one `<script>`.

## Task Group 6 — Lint, polish, validate

11. Read the final `index.html`, `style.css`, `script.js` top to bottom and
    simplify anything a beginner would struggle with.
12. Serve the site (bind `0.0.0.0`, public Codio URL) and click through the
    accordion at 375 / 768 / 1200 px: no horizontal scrollbar, readable text,
    focus ring visible.
13. Surface any differences between implementation and this spec to the founder;
    update the spec only after founder approval.