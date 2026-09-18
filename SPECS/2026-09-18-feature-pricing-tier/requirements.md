# Feature: Pricing / Tiers

Date: 2026-09-18

Project: Momentum

## Scope

Define the Pricing / Tiers section for the public-facing website. This feature addresses section 3, point 5 of the Website Structure & Page Architecture in MISSION.md.

## Decisions (founder-confirmed 2026-09-18)

- **One clear CTA:** `SPECS/MISSION.md` Non-Negotiables require one CTA, so the
  Pricing section intentionally has **no** "Join the Waitlist" button. The
  section's own copy ("Waitlist only — no pricing yet. Mention early access on
  the waitlist instead.") communicates the waitlist status; conversion is driven
  by the navbar, hero, and footer CTAs.
- **Backward compatibility change:** the prior acceptance check that required a
  CTA inside the pricing section was replaced (see `validation.md`). This was an
  approved founder decision, so the earlier check was not preserved.

## In Scope

- **Pricing / Tiers page** reflecting the decision: "Waitlist only — no pricing yet. Mention early access on the waitlist instead."
- Copy clarifying that pricing is not yet available, but waitlist entrants get early access
- Placement in the page narrative flow (Section 5, after Social Proof / Credibility and before Credibility / Social Proof)
- Any related copy about waitlist benefits and early access

## Out of Scope

- Actual pricing tables or plans
- Payment processing or subscription forms
- User account management or dashboard
- Real billing system or payment gateway integration

## Copy (from MISSION.md Section 3)

- **Pricing / Tiers heading:** "Pricing / Tiers" (or appropriate heading)
- **Body copy:** "Waitlist only — no pricing yet. Mention early access on the waitlist instead."
- No CTA button inside this section (see Decisions above); waitlist status and early
  access are communicated by the body copy and the FAQ / footer instead

## Placement Constraints

- Must align with the overall site tone and voice from SPECS/TECH.md
- Must not introduce pricing tables, payment fields, or monetary inputs
- Must adhere to the established tone: professional, transparent, user-focused
- All copy must derive from or be consistent with SPECS/MISSION.md

## Acceptance Criteria

- [ ] Page or section exists and is labeled "Pricing / Tiers" (or equivalent)
- [ ] Copy reads exactly aligns with the approved wording from SPECS/MISSION.md
- No pricing tables, price inputs, or payment-related elements are present
- Copy clearly communicates "waitlist only" and "early access" status
- Design matches the established visual style (colors, typography, spacing) from the project's design system
- Placement on the page follows the prescribed order relative to other sections (Social Proof / Credibility, then Feature Highlights / Value Drivers, then this section)