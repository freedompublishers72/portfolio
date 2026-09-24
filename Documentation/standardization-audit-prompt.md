# Standardization Audit — Prompt Record

Date: 2026-09-24
Task type: Investigation / audit (no implementation)

The following is the exact prompt used for this task, preserved verbatim:

---

STANDARDIZATION AUDIT — ONE-PAGE PORTFOLIO

Perform a complete visual and structural standardization audit of the entire one-page portfolio.

Do NOT redesign anything yet.

The purpose of this audit is to identify every inconsistency, duplication, arbitrary value, spacing problem, typography mismatch, colour mismatch, sizing mismatch, and responsive inconsistency so the page can subsequently be standardized.

Audit the page as ONE SYSTEM, not as seven independent sections.

SECTIONS TO AUDIT

1. Header & Navigation
2. Welcome Hero
3. Feature Project
4. Modular Feature Blobs
5. Travel Bonanza
6. About
7. CTA / Commercial Section

Then perform a whole-page audit.

==================================================
1. TYPOGRAPHY
==================================================

Inventory every text style actually used.

For each, record:

- font family
- fallback fonts
- font size
- font weight
- line height
- letter spacing
- text transform
- colour
- maximum width
- alignment

Identify all:

- H1
- H2
- H3
- section labels / eyebrows
- body text
- lead text
- metadata
- navigation text
- buttons
- accordion titles
- code text
- captions
- small supporting text

Determine whether the same semantic level is consistently represented by the same typography.

Identify:
- unnecessary font-size variations
- duplicate heading styles
- headings that wrap unnecessarily
- inconsistent line heights
- arbitrary one-off sizes
- text that is too large/small relative to its role

Do not change the typography yet.

==================================================
2. COLOUR SYSTEM
==================================================

Inventory every colour used on the page.

Record the actual CSS value for:

- page background
- header background
- ticker background
- hero background
- section backgrounds
- card backgrounds
- elevated card surfaces
- borders
- dividers
- primary text
- secondary text
- muted text
- links
- buttons
- hover states
- geometric accents
- gold/ochre accents
- blue accents
- red accents
- black elements
- code blocks

Identify colours that are:
- duplicated under different variable names
- almost identical but unnecessarily different
- used only once
- inconsistent between sections
- insufficiently contrasted
- visually competing with the approved hero palette

Recommend a small standardized colour token system.

Do not implement changes yet.

==================================================
3. SECTION SYSTEM
==================================================

For every major section record:

- background colour
- minimum/actual height
- top padding
- bottom padding
- left/right padding
- content max-width
- alignment
- section boundary treatment
- relationship to adjacent sections

Determine whether sections follow a common layout rule.

Identify:
- excessive vertical whitespace
- inconsistent section padding
- arbitrary heights
- sections that feel disconnected
- sections that feel unnecessarily boxed
- inconsistent full-width vs contained treatment

The temporary 1px black section-boundary lines are audit guides only. Do not treat them as final design elements.

==================================================
4. CONTAINER / GRID SYSTEM
==================================================

Determine the actual layout system being used.

Record:

- maximum content width
- desktop side margins
- tablet side margins
- mobile side margins
- grid columns
- gaps
- card widths
- card heights
- image widths
- text column widths

Determine whether the page uses a consistent spacing/grid scale.

Identify arbitrary values that should become shared variables.

==================================================
5. SPACING SYSTEM
==================================================

Audit all significant:

- margins
- padding
- gaps
- section spacing
- heading-to-body spacing
- body-to-button spacing
- card padding
- accordion spacing
- image spacing
- navigation spacing

Group them into logical spacing tiers.

Identify values that should be standardized rather than individually defined.

==================================================
6. CARDS / ELEVATION
==================================================

Audit every elevated component.

Record:

- border
- border radius
- shadow layers
- shadow opacity
- shadow offsets
- hover elevation
- hover transform
- transition duration
- surface colour
- internal padding

Determine which elements should be:

- flat
- raised
- interactive/raised

Ensure the 3D language is consistent wherever elevation is used.

==================================================
7. BUTTONS / CONTROLS
==================================================

Audit all buttons and interactive controls.

Record:

- height
- width
- padding
- font
- font size
- weight
- border
- radius
- background
- text colour
- shadow
- hover state
- focus state
- transition

Determine whether all primary actions share a common control system.

==================================================
8. IMAGES / GRAPHICS
==================================================

Audit every image and graphic.

Record:

- intrinsic dimensions
- displayed dimensions
- aspect ratio
- object-fit
- object-position
- border treatment
- radius
- shadows
- cropping
- alignment

Pay particular attention to the approved hero artwork.

Do NOT alter the hero artwork itself.

Identify any image that is unnecessarily cropped, distorted, stretched, or inconsistently treated.

==================================================
9. ACCORDIONS
==================================================

Audit the Modular Feature Blobs accordion system.

Record:

- row height
- typography
- border/divider
- indentation
- icon
- hover state
- active state
- expanded spacing
- content width
- code presentation

Determine whether all accordion items behave and appear identically.

==================================================
10. RESPONSIVE SYSTEM
==================================================

Audit at:

1440px
1280px
1024px
768px
390px
375px

For each breakpoint inspect:

- typography
- container width
- side padding
- section height
- card width
- grid behaviour
- image behaviour
- navigation
- ticker
- accordion
- buttons
- line wrapping
- overflow
- hero artwork positioning

Identify breakpoint-specific hacks and arbitrary overrides.

==================================================
11. BORDER / DIVIDER SYSTEM
==================================================

Inventory:

- section boundaries
- card borders
- accordion borders
- button borders
- decorative lines
- image borders

Determine whether they form a coherent visual system.

The temporary black section lines should NOT be treated as the final solution.

==================================================
12. MOTION / INTERACTION
==================================================

Inventory:

- transitions
- hover transforms
- accordion animation
- ticker animation
- focus states
- reduced-motion handling

Identify inconsistent durations/easing.

==================================================
13. ACCESSIBILITY
==================================================

Audit:

- heading hierarchy
- landmarks
- labels
- button semantics
- keyboard navigation
- focus visibility
- colour contrast
- reduced motion
- image alt text
- accordion ARIA state
- navigation state

==================================================
14. CONTENT / STRUCTURAL DUPLICATION
==================================================

Identify:

- repeated section labels
- repeated titles
- redundant descriptions
- duplicated concepts
- unnecessary wrappers
- unnecessary visual elements
- content that belongs in another section

Do not rewrite content during this audit.

==================================================
15. PAGE ORDER
==================================================

Evaluate the current sequence:

Header & Navigation
→ Welcome Hero
→ Feature Project
→ Modular Feature Blobs
→ Travel Bonanza
→ About
→ CTA

Determine whether the sequence creates a logical progression from:

introduction
→ credibility
→ technical evidence
→ personal/working context
→ commercial action

Do not redesign the order yet. Report observations only.

==================================================
FINAL OUTPUT
==================================================

Produce a structured audit report.

For every inconsistency provide:

CURRENT
STANDARD / TARGET
REASON

Create a proposed global design-token table covering:

- font families
- H1 size
- H2 size
- H3 size
- section label size
- body size
- small text size
- line heights
- colours
- content max-width
- desktop padding
- tablet padding
- mobile padding
- spacing scale
- card radius
- card border
- card shadow
- hover elevation
- button dimensions
- standard transitions
- breakpoint rules

Also identify:

1. GLOBAL fixes
2. SECTION-specific fixes
3. One-off exceptions that should remain intentional
4. Temporary audit elements that should eventually be removed

IMPORTANT:

This is an AUDIT ONLY.

Do not modify files.
Do not redesign the page.
Do not change CSS.
Do not change HTML.
Do not generate new graphics.
Do not replace the approved hero artwork.

Return the findings first so the standardized design system can be agreed before implementation.
