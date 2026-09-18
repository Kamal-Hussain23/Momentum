# Founder Notebook

Welcome to your Founder Notebook. This is the single source of truth for your startup project. As founder and lead decision-maker, use this file to define your concept, guide OpenCode, and track every important decision.

---

## 1. Vision & Problem Discovery

*The foundation: Knowledge → Problem → Solution → Value → Product*

- **Domain / Industry:** Productivity / personal development

- ** Pitch:** Momentum helps busy professionals who are also studying on
  the side finish what matters by focusing them on one small committed task at a
  time — not another to-do list, just the one thing that moves the needle.

- **Target Audience (Who is this for?):** A full-time professional in their 20s–30s
  who studies or learns on the side (a certification, a course, a promotion-lane
  skill), wants to earn more, and feels "busy but stuck." They have calendars and
  to-do lists but still don't follow through on the most important task.

- **The Core Problem (What pain point are you solving?):** "I have a plan, but I
  don't do it." Procrastinating specific tasks leads to guilt, then stress, then
  burnout — and that makes procrastination worse. The result is being busy all the
  time but never moving forward.

- **Proposed Solution:** Momentum — an app that closes the gap between planning and
  doing by narrowing each day to a single Most Important Task (MIT). It is not
  another calendar or to-do list. For this project we build the frontend landing
  page that names the problem, presents the solution, and collects waitlist emails.

- **Core Feature (the single most essential function):** Every day the app shows the
  user **one Most Important Task** — the single task that matters most that day. The
  user checks it off when done. That's it: one task, a check, a finished feeling.
  No lists of twenty items. One thing, done.

- **Value Proposition (Why choose this over existing alternatives?):** Existing
  apps help you plan; Momentum helps you finish. We help busy people who plan but
  don't follow through by turning small commitments into finished tasks, so they
  feel real progress instead of guilt. 

---

## 2. Visual Identity & Design System

*The exact design tokens: colors, fonts, buttons, and radius rules. If it's not
listed here, it doesn't appear on the site.*

- **Company / Product Name:** Momentum
- **Tagline:** *One thing done. Every day.*

- **Brand Personality / Tone of Voice:** Dark-mode focused, approachable, trustworthy. Friendly and encouraging, not bossy or guilt-tripping. Speaks like a good coach: short, warm, honest.

### Color Palette

| Token | Hex | Where to use it |
| :--- | :--- | :--- |
| Background | `#1C1917` | Page background (warm near-black, never pure black) |
| Surface / Card | `#292524` | Cards, inputs, containers, nav bar |
| Text Primary | `#FAF9F6` | Headings and body text |
| Text Muted | `#A8A29E` | Helper text, captions, labels |
| Primary | `#F0A868` | Buttons, links, active states |
| Secondary | `#F7C890` | Primary-button hover, softer highlights |
| Accent | `#FF7E67` | The "one task" highlight, badges — small doses only |

### Typography

- **Heading Font:** `Manrope` (weights 700–800) — friendly but confident
- **Body Font:** `Inter` (weights 400–500) — highly readable, trustworthy
- Headings and body in `#FAF9F6`; captions in `#A8A29E`

### Button Styles

- **Primary button:** Background `#F0A868`, text `#1C1917` (dark text on warm orange = strong contrast), pill shape.
  - Hover: background `#F7C890`
  - Active/pressed: darken slightly (`#E0915A`)
  - Focus: 2px outline `#FF7E67`
- **Secondary button:** Transparent background, 1px border `#F0A868`, text `#F0A868`.
  - Hover: subtle warm fill (10% `#F0A868` over `#1C1917`)

### Border Radius Rules

- Buttons & inputs: **pills**, `999px` — approachable, friendly
- Cards & containers: **`12px`** — soft but not childish
- Small elements (badges, chips, tags): **`6px`** 

---

## 3. Website Structure & Page Architecture

*Outline the narrative flow and layout of the public-facing website.*

- **Primary Goal / Conversion Action (e.g., Waitlist signup, Free trial, Contact demo):** Get the visitor to join the waitlist. CTA button text: **"Join the Waitlist."** The desired action is the visitor entering their email and clicking the button — one signup, one click, no friction. 
- **Page Sections:**
  1. **Hero Section:**
     - Headline: **"Stop planning. Start finishing."**
     - Subheadline: "Momentum shows you your one Most Important Task each day. One small thing done beats a perfect plan, every time."
     - Primary CTA: **"Join the Waitlist"** (primary pill button)
     - Hero visual: a phone mockup showing a card — *"Today's task: finish the course module on databases"* — with a warm ember checkmark
  2. **Social Proof / Credibility:**
     - "Built for people who work full-time and study on the side."
     - "You've tried the lists and the calendars. Momentum is different — because there's only ever one thing to do."
  3. **Feature Highlights / Value Drivers:**
     - **One task, chosen for you.** — "No list of twenty items to feel guilty about. Just the single thing that moves you forward."
     - **Check it. Done.** — "One tap gives you the feeling of a finished task — real progress instead of guilt."
     - **No guilt trips.** — "No streaks, no shaming notifications. Small wins that quietly add up."
  4. **How It Works / Product Demo:** (three steps)
     1. **Set it.** — "Each evening, name the one task that matters most tomorrow."
     2. **Do it.** — "Focus on just that one thing. Nothing else to distract you."
     3. **Check it.** — "One tap tells the whole day 'done.' Repeat tomorrow."
  5. **Pricing / Tiers (Optional):** Waitlist only — no pricing yet. Mention early access on the waitlist instead.
  6. **FAQ / Objection Handling:**
     - **"Isn't this just another to-do list?"** — "To-do lists hand you everything at once. Momentum hands you one thing."
     - **"Why only one task?"** — "Busy people don't fail from lack of planning — they fail from too many options. One task is small enough to actually do."
     - **"What does it cost?"** — "It's in private beta. Joining the waitlist gets you early access and a launch-day email."
     - **"Does it sync with my calendar?"** — "Not yet. First we're making the one-task habit work perfectly on its own."
  7. **Footer / Secondary CTAs:**
     - "Ready to finish something?"
     - **"Join the Waitlist"** (secondary outline button)
     - Brand line: "Momentum — One thing done. Every day."

---

## 4. Decision Log

*Follow the cycle: Think → Ask → Evaluate → Decide → Build*

| Date | Topic / Area | Options Considered | Final Decision & Rationale | Status |
| :--- | :--- | :--- | :--- | :--- |
| *2026-09-17* | *Startup direction* | *Several problem ideas from discovery interview (time management, earning more, stress/burnout)* | *Chosen: "Plan but don't do it" — the procrastination → guilt → stress → burnout cycle.* | *Done* |
| *2026-09-17* | *5-Point Filter check* | *User / Problem / Value / Feasibility / Clarity* | *User ✅ Problem ✅ Value ⚠️ (need differentiation from habit trackers) Feasibility ✅ Clarity ✅. Solid enough to lock in.* | *Done* |
| *2026-09-17* | *Idea challenge scoping* | *"Another to-do list" vs. single purpose* | *Scoped down: one Most Important Task (MIT) per day, one check-off, one goal — "Join the Waitlist." One feature, one persona, one CTA.* | *Done* |
| *2026-09-17* | *Brand identity* | *3 palette candidates (Midnight Blue, Deep Teal, Warm Ember)* | *Chosen: Warm Ember — most approachable. Typography: Manrope + Inter. Pills for buttons, 12px cards.* | *Done* |
| *2026-09-17* | *Design system* | *Generic placeholders vs. exact tokens* | *Locked exact design tokens (7-color palette, fonts, buttons, radius). Website copy + section 3 deferred to the building step.* | *Done* |
| *2026-09-18* | *CTA clutter* | *Repeat "Join the Waitlist" in 4 places vs. reduce* | *Removed the Pricing-section button; kept navbar, hero, and footer. One conversion action, fewer competing buttons — per the Non-Negotiables. Recorded in `SPECS/2026-09-18-feature-pricing-tier/`.* | *Done* |

---

## 5. Notes & Prompts for OpenCode

*Use this section to draft prompt briefs, review feedback, and keep track of pending tasks.*

- [x] Define core problem statement and audience
- [x] Select color palette and typography
- [x] Draft website copy for hero section
- [x] Build responsive hero and navigation components
- [x] Implement feature showcase sections
- [x] Add interactive elements and conversion forms
- [x] Final visual polish and responsive testing
