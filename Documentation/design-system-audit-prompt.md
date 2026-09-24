# Design System & Standardization Audit — Prompt Record

Date: 2026-09-24
Task type: Investigation / audit (no implementation)

The following is the exact prompt used for this task, preserved verbatim:

---

DESIGN SYSTEM & STANDARDIZATION AUDIT

Using the results of the preceding PAGE ARCHITECTURE & VISUAL SECTION-DIVISION AUDIT, perform the complete design-system standardization audit of the one-page portfolio.

Do NOT implement changes yet.

Treat the page as ONE SYSTEM.

The section architecture established by the previous audit must be respected.

==================================================
1. TYPOGRAPHY
==================================================

Inventory every actual text style.

Record:

- font family
- fallback
- size
- weight
- line-height
- letter-spacing
- transform
- colour
- maximum width
- alignment

Audit:

- H1
- H2
- H3
- labels / eyebrows
- body
- lead
- metadata
- navigation
- buttons
- accordion titles
- code
- captions
- small supporting text

Identify:

- duplicate semantic styles
- arbitrary one-off sizes
- unnecessary variations
- inconsistent weights
- inconsistent line heights
- unnecessary nowrap rules
- responsive typography hacks

==================================================
2. COLOUR SYSTEM
==================================================

Inventory all actual colours.

Include:

- page background
- header
- ticker
- hero
- sections
- cards
- elevated surfaces
- borders
- text
- muted text
- links
- buttons
- hover states
- geometric accents
- ochre/gold
- blue
- red
- black
- code blocks

Identify:

- duplicate colours under different variables
- near-duplicates
- accidental aliases
- one-off colours
- poor contrast
- colours that conflict with the approved hero palette

Do NOT flatten legitimate surface-specific colours identified by the architecture audit.

==================================================
3. CONTAINER / GRID
==================================================

Determine:

- global content max-width
- desktop gutter
- tablet gutter
- mobile gutter
- column widths
- gaps
- card widths
- image widths
- text widths

Identify competing container systems and arbitrary values.

==================================================
4. SPACING
==================================================

Inventory:

- section padding
- component padding
- margins
- gaps
- heading spacing
- body spacing
- button spacing
- accordion spacing
- image spacing

Group values into a logical spacing scale.

Do not eliminate intentional architectural whitespace identified in Prompt 1.

==================================================
5. CARDS / ELEVATION
==================================================

Audit:

- borders
- radius
- shadows
- shadow layers
- hover elevation
- transforms
- transitions
- surface colours
- internal padding

Determine the canonical elevation system.

Pay particular attention to `.elevated`.

Identify which components should remain flat versus raised.

==================================================
6. BUTTONS / CONTROLS
==================================================

Determine whether the current controls can share one control system with variants.

Audit:

- height
- padding
- typography
- border
- radius
- background
- text
- shadow
- hover
- focus
- transition

Ensure focus remains visible on every surface.

==================================================
7. RESPONSIVE SYSTEM
==================================================

Audit:

1440
1280
1024
768
390
375

Identify:

- breakpoint duplication
- breakpoint hacks
- arbitrary overrides
- typography failures
- gutter changes
- overflow
- wrapping problems
- image behaviour
- navigation behaviour

Propose a smaller coherent breakpoint system.

==================================================
8. ACCESSIBILITY
==================================================

Audit:

- heading hierarchy
- landmarks
- keyboard navigation
- focus visibility
- contrast
- reduced motion
- alt text
- accordion semantics
- navigation state

==================================================
9. FINAL TOKEN TABLE
==================================================

Produce a proposed canonical token system covering:

- font families
- H1
- H2
- H3
- label
- body
- small text
- line heights
- letter spacing
- colours
- content max-width
- gutters
- spacing scale
- card radius
- borders
- shadows
- elevation
- button dimensions
- transitions
- breakpoints

Separate:

GLOBAL TOKENS

from:

SURFACE-SPECIFIC TOKENS

from:

INTENTIONAL EXCEPTIONS

Do not implement.

Return the proposed system for use by subsequent remediation prompts.
