# Validation — Footer / Secondary CTAs

Goal: prove the footer matches `build-lab/MISSION.md` Section 3 item 7 and the
constitution before merging/moving on.

## Visual Validation

- [ ] `<footer>` element exists as the last element on the page (after
      `</main>`, before `</body>`).
- [ ] Heading reads: "Ready to finish something?"
- [ ] CTA reads "Join the Waitlist", uses `class="btn btn--secondary"`, and
      links to `#waitlist`.
- [ ] Brand line reads: "Momentum — One thing done. Every day."
- [ ] Colors match design tokens exactly (spot-check with a color picker; no
      hardcoded hex/rgba outside `:root`).
- [ ] Footer centered at `640px`, `--space-6` padding, top divider matching the
      Social Proof pattern.
- [ ] Secondary button matches MISSION.md §2: transparent background, 1px
      `#F0A868` border, `#F0A868` text, warm wash on hover.

## Responsive Validation

- [ ] No horizontal scrollbar at 375 / 768 / 1200 px.
- [ ] Footer stays centered and readable at all three widths; heading, button and
      brand line wrap cleanly on mobile.

## Motion & JS Budget

- [ ] Still exactly one `@keyframes` on the site.
- [ ] Still exactly one `<script>` tag; no JavaScript added for the footer.
- [ ] No new animation or transition introduced.

## Accessibility

- [ ] CTA is a real link (keyboard-focusable, Enter activates); focus ring
      visible (`--color-accent`).
- [ ] Heading is an `<h2>`; still exactly one `<h1>` on the page.

## Backward Compatibility

- [ ] `check_footer.py` passes all checks.
- [ ] `check_hero.py` still passes (guards the single `@keyframes` budget).
- [ ] `check_social_proof.py` still passes.
- [ ] `check_feature_highlights.py` still passes.
- [ ] `check_how_it_works.py` still passes.
- [ ] `check_pricing.py` still passes.
- [ ] `check_faq.py` still passes.
- [ ] Still exactly one `<h1>` and one `<script>` on the page.

## Copy Validation

- [ ] No copy drifts from MISSION.md Section 3 item 7 without founder approval.

## Review & Approval

- [ ] Founder reviews the rendered page at the public URL and confirms the CTA
      jumps to the waitlist form.
- [ ] Differences between implementation and this spec are surfaced here; specs
      updated only after founder approval.