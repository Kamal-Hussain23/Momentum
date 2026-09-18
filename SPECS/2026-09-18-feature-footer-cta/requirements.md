# Feature: Footer / Secondary CTAs

Date: 2026-09-18
Project: Momentum

## Scope

Build the Footer / Secondary CTAs section — item **#7**, the last numbered
section of "Website Structure & Page Architecture" in `MISSION.md` Section 3. It
closes the page with a final nudge toward the waitlist and a brand sign-off. It
lives in `build-lab/index.html`, is styled in `build-lab/style.css`, and becomes
the last element on the page.

## Decisions (founder-confirmed 2026-09-18)

- **Placement:** a semantic `<footer>` element placed after `</main>`, before
  the `<script>` tag. The FAQ section stays the last section inside `<main>`.
- **CTA behaviour:** "Join the Waitlist" is a **secondary outline link** to the
  existing hero form (`href="#waitlist"`), matching how the Pricing section
  links. No duplicate email form in the footer.
- **Secondary button style:** this feature adds the `.btn--secondary` styles
  from `MISSION.md` Section 2 to `style.css` (transparent background, 1px
  `#F0A868` border, `#F0A868` text, warm wash on hover). The footer is its first
  use on the page.
- **Heading & hierarchy:** "Ready to finish something?" as an `<h2>`; the brand
  line "Momentum — One thing done. Every day." below it in muted text. This
  keeps exactly one `<h1>` (the hero headline) and valid H1 → H2 order.
- **New design token:** a `--color-primary-wash` token defined **inside `:root`**
  (`rgba(240, 168, 104, 0.1)`) for the secondary-button hover fill — a 10% warm
  wash over the page background, per `MISSION.md` Section 2.
- **Motion budget:** zero new animation. The footer is static; the FAQ accordion
  keeps the single microinteraction slot. Still exactly one `@keyframes`.
- **No JavaScript:** the footer needs none, so the page keeps exactly one
  `<script>` tag.
- **Backward compatibility:** yes — all prior sections and every existing
  acceptance suite stay green (`check_hero.py`, `check_social_proof.py`,
  `check_feature_highlights.py`, `check_how_it_works.py`, `check_pricing.py`,
  `check_faq.py`).

## In Scope

- `<footer>` element after `</main>`.
- Verbatim copy: heading, secondary CTA link, and brand line.
- `.btn--secondary` styles plus the `--color-primary-wash` token.
- Footer styling with design tokens only, centered at `640px` like sibling
  sections, `--color-background`, and a top divider matching the Social Proof
  pattern.
- A `check_footer.py` acceptance script (TDD) following the sibling-script
  pattern.

## Out of Scope

- Duplicate waitlist form or any backend interaction.
- New animations, keyframes, or scroll effects.
- New `<script>` tags, frameworks, libraries, npm packages.
- Social media links, legal pages, sitemaps, or multi-column footer grids — none
  of these appear in `MISSION.md`.

## Copy (verbatim from MISSION.md Section 3, item 7)

- **Heading:** "Ready to finish something?"
- **CTA:** "Join the Waitlist" (secondary outline button → `#waitlist`)
- **Brand line:** "Momentum — One thing done. Every day."

## Engineering Constraints (from SPECS/TECH.md)

- Plain HTML5 + CSS3 + vanilla JS; no frameworks, no npm packages.
- Use the real semantic `<footer>` element.
- All colors / fonts / radii / spacing via CSS custom properties; the only
  hex/rgba values live in `:root`.
- Motion budget: keep exactly one `@keyframes` (hero `rise-in`).
- Keep exactly one `<h1>` and exactly one `<script>` tag.
- Beginner-readable: reuse the existing `.btn` base and add a small
  `.btn--secondary` modifier. No clever tricks.

## Acceptance Criteria

- [ ] `<footer>` exists after `</main>`, before `</body>`.
- [ ] Copy verbatim: "Ready to finish something?", "Join the Waitlist",
      "Momentum — One thing done. Every day."
- [ ] CTA uses `class="btn btn--secondary"` and links to `#waitlist`.
- [ ] `.btn--secondary` matches MISSION.md §2 (transparent background, 1px
      primary border, primary text, warm wash hover via `--color-primary-wash`).
- [ ] `--color-primary-wash` is defined inside `:root` only.
- [ ] No hardcoded hex/rgba outside `:root`; footer CSS uses design tokens.
- [ ] Still exactly one `<h1>`, one `<script>`, one `@keyframes`.
- [ ] No regressions: all six existing check suites pass and `check_footer.py`
      passes.

## Logging / Storage Note

This is a static frontend landing page — no business logic, backend, or database,
so logging decorators and SQLite persistence do not apply (consistent with
`SPECS/MISSION.md` Out of Scope and every previous feature spec).