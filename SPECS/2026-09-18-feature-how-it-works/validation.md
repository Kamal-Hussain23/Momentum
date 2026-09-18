# Validation — How It Works / Product Demo

Goal: prove the section matches `build-lab/MISSION.md` Section 3 and the constitution
before merging/moving on.

## Content Validation

- [ ] Section sits inside `<main>`, directly after the Feature Highlights `</section>`.
- [ ] Step 1 headline reads exactly: "Set it."
- [ ] Step 1 body reads: "Each evening, name the one task that matters most tomorrow."
- [ ] Step 2 headline reads exactly: "Do it."
- [ ] Step 2 body reads: "Focus on just that one thing. Nothing else to distract you."
- [ ] Step 3 headline reads exactly: "Check it."
- [ ] Step 3 body reads: "One tap tells the whole day 'done.' Repeat tomorrow."
- [ ] No invented testimonials, stats, or fake names.

## Design Validation

- [ ] Uses only design tokens from MISSION.md Section 2 — no hardcoded hex in the
  new CSS.
- [ ] Section text is centered, max-width `640px`, on `--color-background`.
- [ ] Steps have `12px` radius (`--radius-card`), `--space-4` between steps,
  `--space-6` below the section.
- [ ] Headlines use `--color-primary` for emphasis.

## Motion & JS Validation

- [ ] Zero new `@keyframes` — site still has exactly 1 (the rise-in from hero).
- [ ] Zero new `<script>` tags and no JavaScript added for this feature.

## Backward Compatibility Validation

- [ ] `check_how_it_works.py` still passes all checks.
- [ ] `check_feature_highlights.py` still passes all checks.
- [ ] `check_social_proof.py` still passes all 16 checks.
- [ ] `check_hero.py` still passes all 23 checks (Hero, Social Proof, Feature
  Highlights untouched).
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