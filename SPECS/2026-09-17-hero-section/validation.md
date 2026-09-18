# Validation — Hero Section

Goal: prove the hero matches `build-lab/MISSION.md` and the constitution before
merging/moving on.

## Visual Validation

- [ ] Navbar brand shows "Momentum"; one pill button right side.
- [ ] Headline reads exactly: "Stop planning. Start finishing."
- [ ] Subheadline matches MISSION.md Section 3 copy.
- [ ] Button text reads exactly: "Join the Waitlist".
- [ ] Colors match tokens exactly (spot-check with a color picker against
      MISSION.md Section 2 — no hardcoded hex in CSS).
- [ ] Phone mockup shows: "Today's task: finish the course module on databases"
      with an ember checkmark; built with HTML/CSS, no `<img>`.

## Responsive Validation

- [ ] Mobile (375px): hero stacks vertically, no horizontal scrollbar, nav
      stays usable.
- [ ] Tablet (768px): content readable, no overlap.
- [ ] Desktop (1200px): text left, phone mockup right; nav brand left /
      link right.

## Accessibility & Semantic Validation

- [ ] Exactly one `<h1>` on the page (the hero headline).
- [ ] Navbar links and buttons are keyboard-focusable with a visible focus ring
      (2px `#FF7E67` outline).
- [ ] Email input uses `type="email"` with a visible `<label>`.
- [ ] Contrast: ember button on dark surface passes (dark text `#1C1917` on
      `#F0A868`).

## Motion Budget Validation

- [ ] Exactly one hero entrance animation; nothing else animates.

## Copy Validation

- [ ] No copy drifts from MISSION.md Section 3 without founder approval.

## Review & Approval

- [ ] Founder reviews the rendered page at the public URL.
- [ ] Differences between implementation and this spec are surfaced here;
      specs updated only after founder approval.