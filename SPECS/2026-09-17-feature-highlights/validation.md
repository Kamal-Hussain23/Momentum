# Validation — Feature Highlights / Value Drivers

Goal: prove the section matches `build-lab/MISSION.md` Section 3 and the constitution
before merging/moving on.

## Content Validation

- [ ] Section sits inside `<main>`, directly after the Social Proof `</section>`.
- [ ] Card 1 headline reads exactly: "One task, chosen for you."
- [ ] Card 1 body reads: "No list of twenty items to feel guilty about. Just the single thing that moves you forward."
- [ ] Card 2 headline reads exactly: "Check it. Done."
- [ ] Card 2 body reads: "One tap gives you the feeling of a finished task — real progress instead of guilt."
- [ ] Card 3 headline reads exactly: "No guilt trips."
- [ ] Card 3 body reads: "No streaks, no shaming notifications. Small wins that quietly add up."
- [ ] No invented testimonials, stats, or fake names.

## Design Validation

- [ ] Uses only design tokens from MISSION.md Section 2 — no hardcoded hex in the
  new CSS.
- [ ] Section text is centered, max-width `640px`, on `--color-background`.
- [ ] Cards have `12px` radius (`--radius-card`), `--space-4` between cards,
  `--space-6` below the section.
- [ ] Headlines use `--color-primary` for emphasis.

## Motion & JS Validation

- [ ] Zero new `@keyframes` — site still has exactly 1.
- [ ] Zero new `<script>` tags and no JavaScript added for this feature.

## Backward Compatibility Validation

- [ ] `check_feature_highlights.py` still passes all checks.
- [ ] `check_social_proof.py` still passes all 16 checks.
- [ ] `check_hero.py` still passes all 23 checks (Hero, Social Proof untouched).
- [ ] Still exactly one `<h1>` on the page.

## Responsive Validation

- [ ] No horizontal scrollbar at 375 / 768 / 1200 px.
- [ ] Section remains centered and readable at all three widths.

## Copy Validation

- [ ] No copy drifts from MISSION.md Section 3 without founder approval.

## Review & Approval

- [ ] Founder reviews the rendered page at the public URL.
- [ ] Differences between implementation and this spec are surfaced here;
      specs updated only after founder approval.