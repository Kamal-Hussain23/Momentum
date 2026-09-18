# Feature: FAQ / Objection Handling

Date: 2026-09-18
Project: Momentum

## Scope

Build the FAQ / Objection Handling section — item **#6** of "Website Structure &
Page Architecture" in `MISSION.md` Section 3. It sits after Pricing / Tiers (#5,
already built) and before the Footer (#7, a later feature), so it becomes the
last section inside `<main>` for now.

## Decisions (founder-confirmed 2026-09-18)

- **Interaction:** a custom vanilla-JS accordion. Each question is a native
  `<button>`; clicking opens/closes its answer panel. Only one item is open at a
  time (exclusive accordion). All items start closed.
- **Heading:** **"Questions?"** — friendly, warm, matches the coach tone.
- **JavaScript:** added to the existing `build-lab/script.js`. This keeps a
  single `<script>` tag on the page so every existing acceptance check that
  asserts `HTML.count("<script") == 1` stays green.
- **Motion budget:** the accordion is the allowed "1 microinteraction" from
  `SPECS/TECH.md`. Panels open/close with CSS **transitions only — zero new
  `@keyframes`** — so the site still has exactly one `@keyframes` block (hero
  `rise-in`).
- **Copy:** all four Q&A pairs copied **verbatim** from `MISSION.md` Section 3,
  item 6. No invented questions or answers.
- **Backward compatibility:** yes — keep all existing acceptance suites passing
  (`check_hero.py`, `check_social_proof.py`, `check_feature_highlights.py`,
  `check_how_it_works.py`, `check_pricing.py`). This is why the accordion JS goes
  into `script.js` rather than a new file.

## In Scope

- FAQ section inside `<main>`, directly after the Pricing `</section>`.
- Heading `<h2>`: "Questions?"
- Four accordion items, each: a `<button>` (question) + a panel (answer), using
  `aria-expanded` / `aria-controls` / linked `id`s for accessibility.
- Vanilla JS accordion behaviour in `script.js` (toggle open/close, exclusive,
  updates `aria-expanded` and the panel class).
- CSS using only design tokens: Surface cards, Text Primary / Muted, `12px`
  radius (`--radius-card`), spacing scale. Visible `--color-accent` focus ring.
- A `check_faq.py` acceptance script (TDD) following the sibling-script pattern.

## Out of Scope

- Footer / Secondary CTAs (#7) — separate later feature.
- Scroll animations, `IntersectionObserver`, any other microinteractions.
- Backend, databases, forms, logging — **not applicable**: this is a static
  frontend landing page (`SPECS/MISSION.md` Out of Scope; `SPECS/TECH.md` files).
- New `<script>` tags, frameworks, libraries, npm packages.

## Copy (verbatim from MISSION.md Section 3, item 6)

- **Q:** Isn't this just another to-do list? → "To-do lists hand you everything at
  once. Momentum hands you one thing."
- **Q:** Why only one task? → "Busy people don't fail from lack of planning —
  they fail from too many options. One task is small enough to actually do."
- **Q:** What does it cost? → "It's in private beta. Joining the waitlist gets
  you early access and a launch-day email."
- **Q:** Does it sync with my calendar? → "Not yet. First we're making the
  one-task habit work perfectly on its own."

## Engineering Constraints (from SPECS/TECH.md)

- Plain HTML5 + CSS3 + vanilla JS. No frameworks, no npm packages.
- All colors / fonts / radii / spacing via CSS custom properties — no hardcoded
  hex values.
- Motion budget: maximum 1 hero effect + 1 scroll effect + 1 microinteraction.
  FAQ accordion counts as the microinteraction; keep exactly one `@keyframes`.
- Keep exactly one `<script>` tag and exactly one `<h1>`.
- Beginner-readable: obvious, small functions; short CSS; no clever tricks.

## Acceptance Criteria

- [ ] FAQ section exists inside `<main>`, directly after Pricing `</section>`.
- [ ] Heading reads: "Questions?"
- [ ] All four Q&A pairs present **verbatim** (see Copy above).
- [ ] Each question is a native `<button>` with `aria-expanded` and
      `aria-controls`; answer panels have matching `id`s.
- [ ] Accordion works: click opens an item, another click closes it; opening one
      closes the others; `aria-expanded` stays truthful.
- [ ] Only one `<script>` tag; accordion code lives in `script.js`.
- [ ] Still exactly one `@keyframes`; panel animation uses transitions only.
- [ ] No hardcoded hex outside `:root`; all FAQ CSS uses design tokens.
- [ ] No regressions: all five existing check suites still pass, and
      `check_faq.py` passes.