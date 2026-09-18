# Validation — FAQ / Objection Handling

Goal: prove the FAQ section matches `build-lab/MISSION.md` Section 3 item 6 and
the constitution before merging/moving on.

## Visual Validation

- [ ] FAQ `<section>` exists inside `<main>`, directly after the Pricing
      `</section>`.
- [ ] Heading reads: "Questions?"
- [ ] All four Q&A pairs appear verbatim:
      - "Isn't this just another to-do list?" → "To-do lists hand you
        everything at once. Momentum hands you one thing."
      - "Why only one task?" → "Busy people don't fail from lack of planning —
        they fail from too many options. One task is small enough to actually do."
      - "What does it cost?" → "It's in private beta. Joining the waitlist gets
        you early access and a launch-day email."
      - "Does it sync with my calendar?" → "Not yet. First we're making the
        one-task habit work perfectly on its own."
- [ ] Colors match design tokens exactly (spot-check with a color picker against
      `SPECS/TECH.md` — no hardcoded hex in CSS).
- [ ] Cards use `--color-surface` with `12px` radius (`--radius-card`); spacing
      follows the scale (`--space-*`); FAQ section centered at `640px` like its
      siblings.

## Interaction & Accessibility Validation

- [ ] Each question is a native `<button>` (keyboard-focusable, Enter/Space work
      with no extra code).
- [ ] Buttons expose `aria-expanded` and `aria-controls`; panels have matching
      `id`s and start `hidden`.
- [ ] `aria-expanded` stays truthful (true when open, false when closed).
- [ ] Clicking an open item closes it; clicking a closed item opens it and closes
      the others (exclusive).
- [ ] Focus ring visible on the question buttons (`--color-accent`).

## Motion & JS Budget

- [ ] Still exactly one `@keyframes` on the site (no new animation).
- [ ] Still exactly one `<script>` tag; accordion code lives in `script.js`.
- [ ] Panel open/close uses CSS transitions, not keyframes.

## Responsive Validation

- [ ] No horizontal scrollbar at 375 / 768 / 1200 px.
- [ ] Section stays centered and readable at all three widths; buttons wrap
      cleanly on mobile.

## Backward Compatibility

- [ ] `check_faq.py` passes all checks.
- [ ] `check_hero.py` still passes (23 checks).
- [ ] `check_social_proof.py` still passes (16 checks).
- [ ] `check_feature_highlights.py` still passes (24 checks).
- [ ] `check_how_it_works.py` still passes (25 checks).
- [ ] `check_pricing.py` still passes (27 checks).
- [ ] Still exactly one `<h1>` on the page.

## Copy Validation

- [ ] No copy drifts from MISSION.md Section 3 item 6 without founder approval.

## Review & Approval

- [ ] Founder reviews the rendered page at the public URL and clicks through the
      accordion.
- [ ] Differences between implementation and this spec are surfaced here; specs
      updated only after founder approval.