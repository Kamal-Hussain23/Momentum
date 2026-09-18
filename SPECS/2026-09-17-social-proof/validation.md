# Validation — Social Proof / Credibility Section

Goal: prove the section matches `build-lab/MISSION.md` Section 3, item 2, and
the constitution, and that it does not break the Hero feature.

## Content Validation

- [ ] Section sits inside `<main>`, directly after the Hero `</section>`.
- [ ] Line 1 reads exactly:
      "Built for people who work full-time and study on the side."
- [ ] Line 2 reads exactly:
      "You've tried the lists and the calendars. Momentum is different — because
      there's only ever one thing to do."
- [ ] No invented numbers, testimonials, or fake names anywhere in the section.

## Design Validation

- [ ] Uses only design tokens from MISSION.md Section 2 — no hardcoded hex in
      the new CSS.
- [ ] Section text is centered, max-width `640px`, on `--color-background`.
- [ ] Divider is `1px solid var(--color-text-muted)`.

## Motion & JS Validation

- [ ] Zero new `@keyframes` in `style.css` (site still has exactly 1).
- [ ] Zero new `<script>` tags and no JavaScript added for this feature.

## Backward Compatibility Validation

- [ ] `check_hero.py` still passes all 23 checks (Hero untouched).
- [ ] Still exactly one `<h1>` on the page.
- [ ] Hero copy, buttons, and phone mockup unchanged.

## Responsive Validation

- [ ] No horizontal scrollbar at 375 / 768 / 1200 px.
- [ ] Section remains centered and readable at all three widths.

## Copy Validation

- [ ] No copy drifts from MISSION.md Section 3 without founder approval.

## Review & Approval

- [ ] Founder reviews the rendered page at the public URL.
- [ ] Differences between implementation and this spec are surfaced here;
      specs updated only after founder approval.