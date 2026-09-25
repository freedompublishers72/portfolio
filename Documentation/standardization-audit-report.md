# Standardization Audit Report — One-Page Portfolio

Date: 2026-09-24
Scope: `index.html` (one-page portfolio) + `assets/css/site.css`
Method: full source review + rendered measurement in Chromium at
1440 / 1280 / 1024 / 768 / 390 / 375 px (computed styles, geometry,
contrast ratios measured live; screenshots taken).
Status: AUDIT ONLY — no site files were changed.

Companion artefact: `standardization-audit-prompt.md` (verbatim prompt).

----------------------------------------------------------------------
0. EXECUTIVE SUMMARY
----------------------------------------------------------------------

The page is not one design system — it is the residue of **five stacked
design passes** in a single 3,473-line stylesheet:

1. Base "restrained static portfolio" system (tokens `--ink`, `--paper`,
   `--accent`, `.hero`, `.project-panel`, `.system-grid`, …).
2. "Final homepage design pass" (`.hero-cover`, `.project-card`, boxed
   `.systems-section`, dark `.contact-section`, `--shadow-card`).
3. "Simple portfolio homepage" (`.title-section`, `.feature-project`,
   `.demo-grid`, `.contact-section--simple`).
4. "Modernist editorial system" (`body:has(.home-main--simple)` remap of
   every colour token to the `--home-*` palette, full-bleed sections).
5. "Phase 1 header/hero" + ticker + accordions + `.elevated` elevation
   system + TEMPORARY black audit-guide block.

Only layers 4–8 (modernist + phase-1 + ticker + accordions + elevation)
are live on the homepage. Roughly **1,000+ lines of CSS (~30% of the
file) target selectors that no longer exist in `index.html`** (`.hero`,
`.hero-cover`, `.project-panel`, `.project-card*`, `.system-grid`,
`.system-card`, `.demo-grid`, `.demo-card`, `.capability-*`,
`.code-index`, `.section-heading`, `.section-intro`, `.hero-*`,
`.pacman` SVG animation, `.portfolio-hero__geometry` blocks, …).

The result: the page *looks* coherent at 1440 px, but underneath it runs
**three gutter systems, two colour-token layers, five overlapping
breakpoints, three unrelated button styles, and heading scales that
differ by 4× for the same semantic level.**

----------------------------------------------------------------------
1. TYPOGRAPHY
----------------------------------------------------------------------

Fonts actually in use (no webfonts):

- Sans: `"Helvetica Neue", "Avenir Next", "Segoe UI", Arial, sans-serif`
  (set once on `body:has(.home-main--simple)`).
- Mono: `ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation
  Mono", monospace` — labels, meta, code, footer, ticker.
- One inconsistency already in the stacks: `.technical-paper-mark` and
  `.demo-meta` use a slightly different mono list (includes `Monaco`,
  drops `SFMono-Regular`/`"Liberation Mono"`).

Computed text styles at 1440 px (px = computed):

| Element | Size | Weight | Line-h | Letter-sp | Transform | Colour |
|---|---|---|---|---|---|---|
| Brand name | 16 | 700 | 16 | 0.32 | uppercase | paper #f2ede3 |
| Brand descriptor | 9.92 | 600 | 9.92 | 1.59 | uppercase | paper 72% |
| Nav link | 13 | 400 | 20.8 | 0.78 | uppercase | paper |
| Hero H1 | **64 fixed** | 650 | 73.6 | -2.56 | none | blue-wash #e2e9e9 |
| Hero lede | 18 | 400 | 27 | – | none | #c8d2d2 |
| Hero button | 13 | 700 | 15.6 | 0.39 | none | surface on navy |
| H2 Feature | 24 nowrap | 620 | 28.8 | -0.48 | none | paper on steel |
| H2 Systems | 24 nowrap | 620 | 21.1 | -1.8 | none | ink |
| H2 About | **100.96** | 620 | 88.8 | -7.57 | none | ink |
| H2 Contact | 72.1 | 700 | 64.9 | -2.88 | none | paper on navy |
| Systems intro | 20 | 400 | 32 | – | none | blue #627b8b |
| Project label | 11.68 | 700 | 18.7 | 1.64 | uppercase | red #a34a42 |
| Feature H3 | 24 | 620 | 27.6 | -0.48 | none | ink |
| Feature desc | 22.4 | 400 | 31.4 | – | none | navy |
| Project facts | 12 mono | 400 | 19.2 | – | none | navy |
| Text link | 16 | 700 | 25.6 | – | none | red |
| Case summary | 19.2 | 620 | 22.1 | -0.58 | none | ink |
| Case index | 11.52 mono | 700 | 13.2 | 1.38 | none | red |
| Case meta | 11.84 mono | 500 | 13.6 | 0.71 | none | blue |
| Case desc | 15.68 | 400 | 25.1 | – | none | blue |
| Code-examples title | 11.2 mono | 700 | 13.4 | 1.57 | uppercase | blue |
| Code-item summary | 16 | 620 | 20.8 | -0.16 | none | ink |
| Code-item lang | 10.56 mono | 620 | 13.7 | 1.06 | uppercase | blue |
| Code-item heading | 12.8 mono | 600 | 20.5 | 0.51 | none | blue |
| Code-item body | 14.4 | 400 | 23.0 | – | none | ink |
| Code `pre` | 12.16 mono | 400 | 18.8 | – | none | navy |
| Code-item file | 14.4 | 400 | 23.0 | – | none | blue |
| Code-item note | 13.12 | 400 | 21.0 | – | none | blue |
| Eyebrow (About/Contact) | 11.68 mono | 700 | 18.7 | 1.64 | uppercase | red / ochre |
| About lede | 43.3 | 400 | 48.5 | – | none | navy |
| About note | 14.72 | 400 | 23.6 | – | none | blue |
| About H3 | 36.1 | 620 | 36.1 | – | none | ink |
| About body | 15.68 | 400 | 25.1 | – | none | navy |
| Contact body | 16 | 400 | 25.6 | – | none | #c8d2d2 |
| Contact button | 16 | 700 | 19.2 | – | none | white on red |
| Footer | 12.16 mono | 400 | 19.5 | – | none | blue on canvas |
| Ticker | 11 mono | 400 | 11 | – | none | #00ff41 on #000 |
| Ticker action | 11 mono | 400 | 11 | 0.88 | uppercase | #00ff41 on #0a3d1f |

Findings (CURRENT → STANDARD/TARGET → REASON):

T1. Section H2 is three unrelated styles.
CURRENT: Feature 24 px caps / Systems 24 px caps / About 101 px /
Contact 72 px.
TARGET: one section-title token (e.g. `--h2: clamp(1.75rem, 4vw, 3rem)`
or a single deliberate caps style) applied to all five section heads.
REASON: identical semantic level rendered 4× apart; the 24 px caps are
only capped because of two one-off override blocks
(`site.css:3152–3172`).

T2. H2 forced `white-space: nowrap`.
CURRENT: `.feature-section h2`, `.systems-section h2` nowrap; they fit
at 375 px by ~2 px margin only.
TARGET: allow wrapping (or size down under `38rem`).
REASON: one word longer and the title clips — fragile hack, not a
system.

T3. H1 is a fixed 64 px at every viewport.
CURRENT: `font-size: 4rem` flat (`site.css:2655–2664`); wraps into a
~5-line, 368 px-tall stack at 375 px; overflows its 465 px column by
~110 px at 1024 px and ~205 px at 768 px (spills onto the artwork).
TARGET: `clamp()` like every other display heading (e.g.
`clamp(2.5rem, 8vw, 4rem)`).
REASON: only un-clamped headline on the page; breakpoint-fragile.

T4. Non-standard font weights that cannot render.
CURRENT: 620 (h2/h3/summaries), 650 (h1), plus 400/500/600/700/800 in
dead rules.
TARGET: 400/600/700 only.
REASON: system font stacks have no 620/650 — browsers round them, so the
intended hierarchy is an illusion.

T5. Lead/body sizes drift per section.
CURRENT: lede class rendered at 18 (hero), 20 (systems intro), 22.4
(feature desc), 43.3 (about), 16 (contact). Body text 14.4–16 across
sections.
TARGET: one `--lede` (~1.125–1.25 rem) and one `--body` (1 rem); About
may keep a larger intro but should be a declared variant.
REASON: five "intro paragraph" sizes for the same role.

T6. Letter-spacing is bespoke everywhere.
CURRENT: ~16 distinct tracking values (-0.085 em … +0.16 em).
TARGET: three tokens: tight display (-0.04 em), normal (0), label mono
(+0.12 em).
REASON: arbitrary per-rule values.

T7. Mono small-text sizes are all slightly different.
CURRENT: 9.92 / 10.56 / 11 / 11.2 / 11.52 / 11.68 / 11.84 / 12 / 12.16 /
12.8 / 13.12 / 13 px across labels, meta, code, footer, ticker.
TARGET: two mono sizes: `--label` ~0.73 rem (11.7 px) and `--small`
~0.78 rem (12.5 px).
REASON: twelve near-identical micro-sizes.

T8. Uppercase applied two different ways.
CURRENT: nav/eyebrows use `text-transform: uppercase`; section H2s are
hard-typed caps ("FEATURE PROJECT").
TARGET: pick one (CSS transform on a shared label class).
REASON: inconsistent casing control; a11y/text reuse.

T9. Brand markup duplicated across pages.
CURRENT: index uses `.brand-name`/`.brand-descriptor`; subpages use
`.brand-prompt`/`.brand-tagline` — both styled.
TARGET: one brand partial.
REASON: same header, two markups.

----------------------------------------------------------------------
2. COLOUR SYSTEM
----------------------------------------------------------------------

Two token layers exist; the `--home-*` layer wins on the homepage via
`body:has(.home-main--simple)` remapping the base names
(`site.css:1784–1821`).

Live values (computed):

| Role | Value | Token |
|---|---|---|
| Page canvas (behind pacman strip + footer) | #a07c33 ochre | `--home-canvas` |
| Header bar | #5a7180 steel | `--home-steel` |
| Header bottom border | #3f5563 | `--home-steel-line` |
| Ticker | #000 bg / #00ff41 text / #0a3d1f action | hardcoded |
| Hero bg | #2e5e79 (matches artwork field) | `--home-hero-bg` |
| Feature section bg | #2e5e79 (same as hero) | `--home-hero-bg` |
| Systems + About bg | #e2e9e9 | `--home-blue-wash` |
| Feature card / accordion surface | #faf7ef | `--home-surface` |
| Card texture | 18 px dot-grid data-URI | `--home-texture` |
| Navy surfaces (image bg, tech-mark, contact) | #152b43 | `--home-navy` |
| Primary text | #151719 | `--home-ink` |
| Secondary/muted text | #627b8b | `--home-blue` |
| Red accent (labels, links, CTA) | #a34a42 | `--home-red` |
| Ochre accent (bars, eyebrows, nav underline) | #bd8d32 | `--home-ochre` |
| Rules | #c8c0b3 / #8e877d | `--home-rule(-strong)` |
| Paper (on dark) | #f2ede3 | `--home-paper` |
| Elevation edge/shadow | rgba(21,43,67,…) | `--elev-*` |

Token aliasing hack: `--accent`→navy, `--accent-dark`→ink,
`--green`→ochre, `--purple`→red — so `a:visited { color: var(--purple)
}` actually renders red, and `:focus-visible` renders navy.

Findings:

C1. Same colour, two names / surprise remap.
CURRENT: `--accent` renders navy, `--purple` renders red, `--green`
renders ochre.
TARGET: rename tokens semantically; delete the base→home remap.
REASON: unmaintainable indirection; visited-link styling is accidental.

C2. Near-duplicate blues.
CURRENT: steel #5a7180, hero-bg #2e5e79, blue #627b8b, steel-line
#3f5563, blue-wash #e2e9e9, navy #152b43 — six blue-ish values, two of
them (steel, steel-line) used only in the header.
TARGET: consolidate to navy / hero-steel / muted / wash / rule.
REASON: header introduces a sixth blue used nowhere else.

C3. Feature reuses hero-bg.
CURRENT: `.feature-section` background = `--home-hero-bg` #2e5e79.
TARGET: either intentional (declare it) or give Feature its own band.
REASON: hero and feature read as one continuous 1,900 px slab; the only
separation is the temporary black audit line.

C4. Systems and About share identical bg.
CURRENT: both `--home-blue-wash` + texture, adjacent.
TARGET: intentional merge or differentiate.
REASON: boundary between "technical evidence" and "personal context" is
invisible except the temp line.

C5. Single-use colours.
CURRENT: #c8d2d2 (hero lede + contact p), #b9c4c7 (tech-mark caption),
rgba(242,237,227,.32/.45/.5/.7) hero/nav decorative alphas, #00ff41 +
#0a3d1f + #000 (ticker), #a07c33 canvas.
TARGET: fold into tokens or document as exceptions.
REASON: token table should cover every value.

C6. Contrast failures (WCAG, measured):
- Footer text `#627b8b` on canvas `#a07c33` → **1.15:1** (severe).
- Brand descriptor paper@72% on steel → **2.99:1**.
- Nav links paper on steel → **4.38:1** (< 4.5 for 13 px text).
- Mono meta/headings `#627b8b` on surface `#faf7ef` → **4.15:1**
  (< 4.5 at 11–13 px).
TARGET: darken muted to ~#4c6272 (≈4.6) or place footer on navy/paper.
REASON: real AA failures, not stylistic.

C7. Ticker palette is alien to the page.
CURRENT: black/terminal-green strip between a steel header and a steel
hero.
TARGET: restyle to palette (navy/ochre) or keep as a deliberate
console-easter-egg exception — decide, don't drift.
REASON: only pure-black element; visually competes with approved hero.

----------------------------------------------------------------------
3. SECTION SYSTEM
----------------------------------------------------------------------

Measured at 1440 px (all full-bleed, no outer page rail):

| Section | bg | height | pad-block | pad-inline | boundary |
|---|---|---|---|---|---|
| Header | #5a7180 | 106 (80+25 ticker) | – | wrap 75 rem | 1 px steel-line |
| Hero | #2e5e79 + art | 520 min | 0 (copy centred) | 121 (= (vw−75rem)/2) | temp black top on next |
| Feature | #2e5e79 | 1,404 | 130 / 159 | 101 (7 vw) | 1 px black (temp) top+bottom |
| Systems | #e2e9e9 | 902 (=100 vh min) | 56 / 56 | 101 | 1 px black (temp) bottom |
| About | #e2e9e9 | 1,558 | 144 / 144 | 101 | (none visible — same bg) |
| Pacman strip | transparent → canvas | 112 | – | – | hairline + ring decor |
| Contact | #152b43 | 542 | 115 / 115 | 101 | 1 px black (temp) top |
| Footer | transparent → canvas | 63 | 21.6 | wrap | 1 px rule-strong |

Findings:

S1. Four different vertical rhythms.
CURRENT: 130/159, 56, 144, 115 block padding across sections.
TARGET: one section-padding token (e.g. `clamp(4rem, 9vw, 8rem)`) for
all content sections; keep systems tighter only if intentional.
REASON: no shared section cadence.

S2. `min-height: 100vh` on Systems only.
CURRENT: systems is the lone vh-height section → ~150 px dead space
top/bottom at 1440×900, ~180 px at 390×844.
TARGET: drop or apply consistently.
REASON: arbitrary; creates a visible "air pocket".

S3. Hero↔Feature boundary ambiguity.
CURRENT: identical bg colour; separation relies on the temp black line.
TARGET: real boundary treatment in the final system.
REASON: two sections read as one.

S4. Systems content column narrower than siblings.
CURRENT: `.case-study-list` = `width: 80%` (979 px) inside a 1,225 px
content field.
TARGET: same content width as Feature card / About grid.
REASON: accordion stack visibly inset vs every other section.

S5. Footer unpainted.
CURRENT: transparent → ochre canvas; 12 px blue text at 1.15:1.
TARGET: footer on a real surface (navy or paper).
REASON: contrast fail + looks unfinished.

S6. Full-bleed vs contained inconsistency.
CURRENT: sections are full-bleed with inline padding; header/footer use
`.wrap` (75/78 rem); hero uses its own `(100vw − 75rem)/2` formula.
TARGET: one container rule (see §4).
REASON: three gutter systems → content edges never align.

----------------------------------------------------------------------
4. CONTAINER / GRID SYSTEM
----------------------------------------------------------------------

There is **no single container**. Left content edge measured:

| Viewport | Header | Hero | Sections | Case list |
|---|---|---|---|---|
| 1440 | 113.5 | 121.1 | 101 | 224 |
| 1280 | 40 | 41.1 | 89.8 | 199 |
| 1024 | 40 | 40 | 71.8 | 159 |
| 768 | 32 | 32 | 53.9 | 119 |
| 390 | 22 | 22 | 27.3 | 36 |

Rules producing this: `.wrap` = `min(100% − 3rem, 78rem)` redefined to
`min(100% − 5rem, 75rem)` for header; hero `padding: 0 max(2.5rem,
(100vw − 75rem)/2)`; sections `padding-inline: clamp(1.25rem, 7vw,
9rem)`; case list `80%/95%`.

Findings:

G1. Three gutter systems, zero alignment.
CURRENT: as table — hero, header, and section edges all differ.
TARGET: one `--gutter` (e.g. `clamp(1.5rem, 6vw, 8rem)`) + one
`--measure` (75 rem) used by header, hero, all sections, footer.
REASON: the ragged left edge is the single biggest "unsystematic"
signal on the page.

G2. Percent-width content column.
CURRENT: `.case-study-list { width: 80% }` (95% ≤38 rem).
TARGET: fixed token width / same as other content.
REASON: only %-derived content width on the page.

G3. Grids: hero `1fr 1fr` (second column hidden → artwork is actually
page background, geometry column `display:none`), feature card
single-column, about `1fr 1fr` → 1 col ≤38 rem, contact `1fr auto` →
1 col ≤54 rem.
TARGET: document one 12-col or simple half/half rule; the current grids
are fine once gutters unify.
REASON: hero's "2-col grid" is vestigial — the right cell is dead code.

----------------------------------------------------------------------
5. SPACING SYSTEM
----------------------------------------------------------------------

Live spacing values (px, rem at 16 px): 4, 8, 9.6, 12, 13.6, 14.4, 16,
17.6, 18.4, 20, 21.6, 22, 24, 25.6, 27.3, 30, 32, 35, 36, 40, 48, 51,
56, 64, 72, 80, 86, 90, 101, 102, 115, 128, 130, 144, 158, 240 …

Rough tiers in practice:
- micro (inside components): 8–24
- component padding: 24–48
- section padding: 56–159
- hero/structural: 240 bottom band, 400–520 min-heights

Findings:

SP1. No declared scale.
CURRENT: ~35 distinct values, many arbitrary (e.g. padding
`1.15rem 2rem 1.15rem 0`, `0.1rem 0 1.9rem`, `padding-block 21.6`).
TARGET: 8-pt-ish scale: 4/8/12/16/24/32/48/64/96/144 + section token.
REASON: everything is a one-off.

SP2. Heading→body gaps inconsistent.
CURRENT: heading margin-bottom 16–28 + decorative bar margin 24; about
h3 uses border-top + 16 pad.
TARGET: one `--gap-head` token.
REASON: visual rhythm differs per section.

SP3. Card padding varies by breakpoint via clamps — acceptable, but
three different clamp recipes (`2.25/6/6` vs `2/4/4` vs fixed 1.5 rem)
for the same card role.
TARGET: one `--pad-card`.

----------------------------------------------------------------------
6. CARDS / ELEVATION
----------------------------------------------------------------------

The `.elevated` system (`site.css:3394–3450`) is the newest and best:
1 px `rgba(21,43,67,.24)` edge + `inset 0 1px 0 rgba(255,255,255,.55)`
highlight + 3-layer shadow + `translateY(-5px)` hover + 200 ms ease-out.
Applied to: `.feature-project`, all six `.case-study` items.

Controls use `--elev-control` (2-layer shadow, −2 px lift): hero action,
contact button.

Findings:

E1. Three shadow recipes coexist.
CURRENT: `--elev-card` rgba(21,43,67) live; `0 22px 55px
rgba(20,32,51,.11)` on `.feature-project` base (overridden but still
declared); `--shadow`/`--shadow-card` rgba(25,55,92) / rgba(0,0,0,.2)
dead; `.demo-card` rgba(20,32,51) dead.
TARGET: keep `--elev-*` only; delete the rest.
REASON: four shadow colours for one page.

E2. Radius: everything live is square (`--panel-radius: 0`) — consistent.
But the stylesheet still carries 0.35/0.4/0.45/0.55/0.75 rem + 14/16/18
px radii in dead rules.
TARGET: `--radius: 0` token; purge dead radii.

E3. Accordions as elevated cards.
CURRENT: six `.case-study` items are floating raised cards (20 px gaps)
even though the CSS comment calls them a "thin-rule accordion"; inner
`.code-item`s are true hairline rows.
TARGET: decide — floating cards (current, fine) vs hairline accordion;
align comment + naming either way.
REASON: two different accordion languages nested.

E4. `min-height` on cards: system-card 24 rem (dead), feature img
440/340/0, tech-mark 352/288, contact 400, hero 520/464 — arbitrary
per-element heights.
TARGET: height by content + aspect ratios where possible.

----------------------------------------------------------------------
7. BUTTONS / CONTROLS
----------------------------------------------------------------------

| Control | h | pad | font | bg | text | border | radius | shadow | hover |
|---|---|---|---|---|---|---|---|---|---|
| Hero action | 48 min | 12/16 | 13 sans 700 | navy | surface | navy | 0 | elev-control | bg→ink, −2 px |
| Contact .button | 46.4 | 10.4/16 | 16 sans 700 | red | #fff | red | 0 | elev-control | bg→paper, text→navy, −2 px |
| Ticker action | 25 | 0/9.6–14.4 | 10–11 mono caps | #0a3d1f | #00ff41 | 1 px green-left | 0 | none | underline |
| Text link | – | – | 16 700 | – | red (paper on navy) | – | – | – | underline 2 px |
| Nav link | 35 | – | 13 caps | – | paper | ochre inset underline (current) | – | – | colour stays paper |

Findings:

B1. No common control system.
CURRENT: two "primary" buttons (navy hero / red contact) with different
sizes, plus a third control idiom in the ticker.
TARGET: one `.btn` token set (height 48, pad 0.75/1.25 rem, weight 700,
radius 0, elev-control, 200 ms) + colour variants (`--btn-bg`).
REASON: same role, unrelated specs.

B2. Hover transitions missing on buttons.
CURRENT: `.button`/nav/text-links snap instantly; only transform+shadow
transition (200 ms). Colour change is instant.
TARGET: add `background-color/color/border-color` to the 200 ms token.
REASON: mixed motion polish.

B3. Focus ring inconsistent.
CURRENT: global `:focus-visible` = 2 px `--accent` → renders **navy** —
invisible on the navy contact section and dark ticker; hero action
overrides to red.
TARGET: one visible focus colour per surface (e.g. ochre on dark, red on
light).
REASON: real a11y defect on dark sections.

----------------------------------------------------------------------
8. IMAGES / GRAPHICS
----------------------------------------------------------------------

| Asset | Intrinsic | Displayed (1440) | Fit | Notes |
|---|---|---|---|---|
| hero-artwork.jpg | 1549×471 | cover @ 55% centre in 1427×520 hero | cover | approved; steel bg merges seamlessly; ≤48 rem becomes `auto 15rem` bottom-right band — mostly cropped off-screen, only strands/sliver visible |
| sria-homepage.jpg | 1600×760 | 1224×581 | width 100%, height auto (cover inert) | `filter: saturate(.82) contrast(1.04)` — graded, undocumented |
| technical-paper-mark | CSS art | 929×352 | – | navy panel + ring + red slash; decorative, `aria-hidden` |
| pacman SVG | 540×40 | **display:none** | – | replaced by ::before/::after geometry; dead markup |
| hero geometry spans | – | **display:none** | – | ~200 lines of dead CSS + 4 dead HTML spans |

Findings:

I1. Feature image navy gap.
CURRENT: container `min-height: 440 px` (>54 rem) / `340 px` (54–38 rem)
while `img` is `height: auto` → 29 px navy strip at 1024, 33 px at 768.
TARGET: remove container min-height or restore `object-fit: cover`
pairing (height 100%).
REASON: visible empty band inside the card.

I2. Undocumented image filter.
CURRENT: `saturate(0.82) contrast(1.04)` only on the SRIA screenshot.
TARGET: declare as token/policy or drop.
REASON: hidden, arbitrary grading.

I3. Mobile hero artwork nearly invisible.
CURRENT: `auto 15rem` band bottom-right → at 375 px the approved
composition reduces to a faint strand sliver.
TARGET: keep per policy or tune `background-position/size` so the
circle/fan survives (without altering the asset).
REASON: approved artwork effectively absent on phones.

I4. Dead graphics markup.
CURRENT: `.portfolio-hero__geometry` + 4 spans (display:none), pacman
SVG (display:none).
TARGET: delete markup + ~250 lines of CSS at implementation time.
REASON: pure weight.

----------------------------------------------------------------------
9. ACCORDIONS (Modular Feature Blobs)
----------------------------------------------------------------------

Measured (1440 px, open state):

- Row: summary 58.9 px tall, padding `18.4 32 18.4 0`, 19.2 px/620 ink
  title, mono red index (11.5), mono blue meta (11.8, right-aligned),
  "+" → "–" icon (mono blue, right).
- Item surface: cream `#faf7ef`, 24 px side padding, 1 px edge + elev
  shadow; hover lifts −5 px.
- Expanded body: max-width 62 rem, bottom pad 30.4; inner
  `code-accordion` hairline rows 60 px, "+"→"–" same icon idiom;
  code-item headings mono 12.8 blue; `pre` cream, 1 px rule + 3 px ochre
  left bar, 12.16 px mono.
- Width: 80% column (95% ≤38 rem) — see S4.
- Meta wraps under name ≤38 rem (`flex-basis:100%`) — consistent.
- All six rows behave identically; **item 06 (Travel Bonanza) breaks the
  anatomy**: no code examples, no links — only a decorative navy mark.
- Icon colour/position consistent; hover turns name red.
- `<details>`/`<summary>` native → keyboard + ARIA handled by browser.

Findings:

A1. Anatomy inconsistency.
CURRENT: 5 items = desc + code accordion + case-study link; item 06 =
desc + decorative block only.
TARGET: same internal structure for every item (or visually mark 06 as
different).
REASON: one accordion row expands to an ad.

A2. Row height not fixed; padding-driven (58.9). Fine — but note the
`min-height` only exists on code-item summaries (60), not case-study
summaries → two row recipes inside one accordion stack.
TARGET: unify row recipe.

----------------------------------------------------------------------
10. RESPONSIVE SYSTEM
----------------------------------------------------------------------

Media queries present: `70 rem` ×2, `68 rem` ×2, `64 rem`, `54 rem` ×3,
`48 rem` ×2, `38 rem` ×4 — six breakpoints; 70/68 rem rules all target
dead selectors.

Behaviour verified live:

- 1440: baseline above.
- 1280: same layout; hero gutter 41 vs sections 90 (worst edge
  mismatch); no overflow.
- 1024: H1 overflows copy column +110 px onto artwork (legible,
  unintended); feature image gap 29 px; still 2-col hero.
- 768: H1 overflow +205 px; feature image gap 33 px; about grid still 2
  cramped columns (292 px); contact → 1 col (54 rem rule).
- 390/375 (emulated): no h-scroll; H1 = 64 px → 5-line stack ~368 px;
  nowrap H2s fit by ~2 px; hero = copy over 240 px artwork band; accord
  list 95%; footer wraps; `pre` scrolls internally (contained).

Breakpoint hacks to fix:
- H1 fixed 64 px (no clamp) — worst offender.
- `scroll-padding-top`/`scroll-margin-top` magic numbers drifted from
  real header heights: 130 declared vs 106 actual (>54 rem); 182 vs ~106
  (54–48 rem) → 76 px overshoot; 150 vs ~139 (48–38 rem); 198 vs ~139
  (≤38 rem) → 59 px overshoot.
- `min-height` staircases (520/464/… ) duplicate what content+padding
  could do.
- Five breakpoints → consolidate to 3 (e.g. ≤64 rem, ≤48 rem, ≤38 rem).

----------------------------------------------------------------------
11. BORDER / DIVIDER SYSTEM
----------------------------------------------------------------------

Live dividers: header-bottom steel-line; temp black section lines;
ochre 4.8 px bars (section-heading::before, about h3 top, pre left);
rules #c8c0b3 (code rows, facts, code-examples top) and #8e877d
(section bottoms, tech); elev-edge card borders; nav ochre underline;
ticker green hairline; pacman navy hairline + red ring.

Assessment: a coherent *hairline + ochre-bar* language exists inside the
cream surfaces; section boundaries are the weak point (relying on the
temp black lines). One-off borders: nav-external left divider
(paper@32%), ticker green left edge, pre ochre bar (0.2 rem vs 0.3 rem
bars elsewhere — mismatched weight).

----------------------------------------------------------------------
12. MOTION / INTERACTION
----------------------------------------------------------------------

- `.elevated` / controls: 200 ms ease-out transform+shadow. Good —
  adopt as the standard.
- Ticker: 144 s linear translate; reduced-motion → static scrollable.
- Pacman keyframes: dead on homepage.
- Accordions: native `<details>` — instant, no animation (consistent).
- Nav/link/button colour hovers: instant (no transition).
- `scroll-behavior: smooth` + reduced-motion override present.
- Inconsistency: hover colour changes snap while elevation animates;
  standardise `200 ms ease-out` for all interactive state changes.

----------------------------------------------------------------------
13. ACCESSIBILITY
----------------------------------------------------------------------

- Landmarks: header/nav/main/footer OK; skip-link present; `aria-label`s
  on nav ("Primary") and ticker ("Offers" — label mismatches content:
  it shows cars + one CTA).
- Heading order: h1 → h2s → h3s — but About renders `<p class=eyebrow>
  About` + `<h2>About</h2>` (duplicated) and feature h3 "siemreapinside"
  is styled same size as the section h2 (24 px) — visual hierarchy
  flattened.
- `aria-current="page"` on an in-page anchor — should be
  `aria-current="location"` or removed.
- Keyboard: details/summary native OK; links OK.
- Focus: navy outline invisible on navy/dark surfaces (see B3).
- Contrast: footer 1.15:1, descriptor 2.99:1, nav 4.38:1, mono meta
  4.15:1 (see C6).
- Reduced motion: handled (ticker, pacman, elevated, scroll).
- Alt text: SRIA image good; decorative SVG/spans aria-hidden; hero art
  is CSS bg (correctly non-semantic).
- Ticker: 10 duplicated sequences in markup (only 2 needed for the −50 %
  loop) — markup bloat, aria-hidden so harmless but noisy.

----------------------------------------------------------------------
14. CONTENT / STRUCTURAL DUPLICATION
----------------------------------------------------------------------

- "About" eyebrow + "About" h2 (triple label incl. ochre bar).
- "Start a conversation" button twice (hero + contact) — same label, two
  different styles.
- `.case-study__more` "Read the full case study →" ×5 + item 06 links
  to the same research-data-engine study as item 05.
- Travel Bonanza desc promises a "technical paper" that is never linked
  — dead-end content.
- Wrapper bloat: `.case-study-list` width-80% wrapper; duplicated ticker
  sequences ×10; dead `.portfolio-hero__geometry` markup; dead `.pacman`
  SVG.
- Footer claims "Plain HTML and CSS. No frameworks, no tracking." —
  accurate.

----------------------------------------------------------------------
15. PAGE ORDER
----------------------------------------------------------------------

Header → Hero → Feature (SRIA) → Blobs (01–06 incl. Travel Bonanza) →
About → CTA.

Assessment: intro → credibility → evidence → context → action is
logical and works. Observations only:
- Travel Bonanza is nested *inside* Blobs as item 06 — it is not a peer
  section; its "technical paper" content is absent, so the item reads as
  a stub.
- The Feature project's visual weight (1,404 px steel slab) dwarfs the
  six evidence rows (~460 px) — credibility dominates evidence.
- Pacman strip is the only canvas-coloured divider and sits between
  About and Contact — reads as decoration, not structure.

----------------------------------------------------------------------
PROPOSED GLOBAL DESIGN-TOKEN TABLE
----------------------------------------------------------------------

| Token | Proposed value | Replaces |
|---|---|---|
| `--font-sans` | "Helvetica Neue","Avenir Next","Segoe UI",Arial | both stacks |
| `--font-mono` | ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono" | 3 mono variants |
| `--h1` | clamp(2.5rem, 8vw, 4rem) / w700 / lh 1.05 / −0.04em | fixed 4rem, w650 |
| `--h2` | clamp(1.75rem, 4.5vw, 3rem) / w700 / lh 1.05 / −0.04em | 24px nowrap + 101px + 72px |
| `--h3` | 1.375rem / w600 / lh 1.2 | 19.2–36 px spread |
| `--label` | 0.73rem mono 700 caps +0.12em | 8 micro-sizes |
| `--body` | 1rem / 1.6 | 14.4–16 drift |
| `--lede` | 1.125rem / 1.5 (About variant 1.5rem) | 18–43 px |
| `--small` | 0.78rem / 1.5 | 9.9–13 px |
| `--code` | 0.76rem mono / 1.55 | 11.2–12.16 |
| `--paper` | #f2ede3 | — |
| `--surface` | #faf7ef | — |
| `--canvas` | #a07c33 | body bg |
| `--ink` | #151719 | — |
| `--navy` | #152b43 | + steel-line #3f5563 |
| `--hero-bg` | #2e5e79 | keep (artwork lock) |
| `--muted` | #4c6272 (darkened from #627b8b) | fixes 4.15–4.38:1 fails |
| `--wash` | #e2e9e9 | — |
| `--red` | #a34a42 | links, accents, CTA |
| `--ochre` | #bd8d32 | bars, on-dark accents |
| `--rule` / `--rule-strong` | #c8c0b3 / #8e877d | — |
| `--measure` | 75rem | 76/78/75 mix |
| `--gutter` | clamp(1.5rem, 6vw, 8rem) | 3 gutter systems |
| `--gutter-mobile` | 1.375rem | — |
| `--space-1…6` | 0.5/1/1.5/2/3/4rem + `--space-section` clamp(4rem,9vw,8rem) | ~35 values |
| `--radius` | 0 | 8 dead radii |
| `--edge` | 1px rgba(21,43,67,.24) | — |
| `--shadow-card` / `--shadow-card-hover` | existing elev stacks | 3 dead shadows |
| `--shadow-control(-hover)` | existing elev-control | — |
| `--lift-card` −5px / `--lift-control` −2px | existing | — |
| `--btn-h` 3rem / `--btn-pad` .75/1.25rem / `--btn-w` 700 | 3 button specs | |
| `--motion` | 200ms ease-out | .18s ease etc. |
| `--focus` | 2px ochre on dark / red on light | navy-invisible bug |
| breakpoints | ≤64rem, ≤48rem, ≤38rem | 70/68/64/54/48/38 |
| `scroll-margin` | `header-height + 1rem` via one var | 4 magic numbers |

----------------------------------------------------------------------
FIX LISTS
----------------------------------------------------------------------

GLOBAL (do first):
1. One gutter + measure for header/hero/sections/footer (G1).
2. One H2 token for all five sections (T1); drop nowrap (T2); clamp the
   H1 (T3).
3. Consolidate colours to the token table; fix muted blue → #4c6272;
   re-surface footer (C6/S5).
4. Standardise `.elevated` + `--elev-control` as the only 3-D system;
   purge dead shadow/radius tokens (E1/E2).
5. One button spec with colour variants; add colour to the 200 ms
   transition; fix dark-surface focus ring (B1–B3).
6. Consolidate breakpoints to 64/48/38 rem; recompute scroll-margins
   from a header-height var.
7. Delete dead CSS/markup (~1,000 lines): old hero/project/system/demo/
   capability/code-index layers, hero geometry spans, pacman SVG.

SECTION-SPECIFIC:
- Header: raise nav/descriptor contrast (brighter paper or darker
  steel); single brand markup.
- Hero: clamp H1; keep artwork per policy; consider whether mobile art
  band should preserve the circle (I3).
- Feature: decide its own bg vs sharing hero steel; fix image
  min-height gap (I1); declare or drop the image filter (I2).
- Blobs: align list width to the content column (S4); unify row anatomy
  for item 06 or mark it distinct (A1); fix "thin-rule" comment.
- Travel Bonanza: either link the technical paper or re-scope the item's
  promise.
- About: remove duplicate eyebrow/h2; keep the larger lede only as a
  declared variant.
- Contact: verify button focus ring on navy; keep as the page's single
  dark band.
- Footer: put on a real surface; unify with container system.

INTENTIONAL ONE-OFFS TO KEEP:
- Hero artwork treatment + `--home-hero-bg` (approved-asset policy).
- Ochre page canvas showing only at pacman strip + footer — keep only if
  deliberate; otherwise paint footer.
- `.technical-paper-mark` as a decorative device (if item 06 stays).
- Ticker — only if the console-easter-egg is deliberate; otherwise
  restyle to palette.
- `text-wrap: balance` on headings — fine.

TEMPORARY ELEMENTS TO REMOVE:
- `site.css:3452–3473` TEMPORARY AUDIT GUIDES block (1 px black lines on
  `.feature-section`, `.systems-section`, `.contact-section--simple`)
  — remove once the real boundary system lands.
- Any audit-only screenshots/scripts (none persisted).

----------------------------------------------------------------------
APPENDIX — evidence

- Measurements taken via Chrome DevTools MCP on
  `http://127.0.0.1:8099/index.html` at the six required widths.
- Screenshots: /tmp/audit-1440-full.png, /tmp/audit-1024-top.png,
  /tmp/audit-375-full.png (session-temporary).
- Contrast ratios computed per WCAG 2.x relative luminance.
