# Design System & Standardization Audit — Report

Date: 2026-09-24
Scope: `index.html` + `assets/css/site.css` (one-page portfolio)
Method: rendered measurement in Chromium at 1440 / 1280 / 1024 / 768 /
390 / 375 px; full CSS source analysis. Builds on
`standardization-audit-report.md` and respects the zone map from
`section-architecture-audit-report.md` (steel chrome → steel zone →
light zone → ochre interstitial → navy CTA → footer).
Status: AUDIT ONLY — nothing implemented.

Companion artefact: `design-system-audit-prompt.md`.

----------------------------------------------------------------------
1. TYPOGRAPHY
----------------------------------------------------------------------

Fonts in use (no webfonts):

- Sans: `"Helvetica Neue", "Avenir Next", "Segoe UI", Arial, sans-serif`
- Mono: `ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation
  Mono", monospace` — plus two divergent mono stacks
  (`.technical-paper-mark`, `.demo-meta` use `Menlo, Monaco, Consolas`).

Complete live text-style inventory (computed at 1440 px):

| Role | Selector | Size | Wt | LH | LS | Xform | Colour | Max-w |
|---|---|---|---|---|---|---|---|---|
| H1 | `.portfolio-hero h1` | 64 fixed | 650 | 1.15 | -.04em | – | #e2e9e9 | – |
| H2 feature | `.feature-section h2` | 24 | 620 | 1.2 | -.02em | caps(src) | #f2ede3 | – |
| H2 systems | `.systems-section h2` | 24 | 620 | .88 | -.075em | caps(src) | #151719 | – |
| H2 about | `.about-section h2` | 101 | 620 | .88 | -.075em | – | #151719 | 14ch |
| H2 contact | `.contact-section h2` | 72 | 700 | .9 | -.04em | – | #f2ede3 | 16ch |
| H3 card | `.feature-project-copy h3` | 24 | 620 | 1.15 | -.02em | – | #151719 | – |
| H3 about | `.about-grid h3` | 36 | 620 | 1 | – | – | #151719 | – |
| H3 code title | `.code-examples__title` | 11.2 | 700 | 1.2 | .14em | caps | #627b8b | – |
| H4 code | `.code-item__heading` | 12.8 | 600 | 1.6 | .04em | – | #627b8b | – |
| Eyebrow | `.eyebrow`, `.project-label` | 11.68 | 700 | 1.6 | .14em | caps | #a34a42 / #bd8d32 | – |
| Lede | `.portfolio-hero__lede` | 18 | 400 | 1.5 | – | – | #c8d2d2 | 32.5rem |
| Lede | `.about-intro .lede` | 43 | 400 | 1.12 | – | – | #152b43 | 62rem |
| Intro | systems heading p | 20 | 400 | 1.6 | – | – | #627b8b | 45rem |
| Body | feature desc | 22.4 | 400 | 1.4 | – | – | #152b43 | 48rem |
| Body | about p/li | 15.68 | 400 | 1.6 | – | – | #152b43 | – |
| Body | code-item p/li | 14.4 | 400 | 1.6 | – | – | #151719 | 56rem |
| Body | contact p | 16 | 400 | 1.6 | – | – | #c8d2d2 | 42ch |
| Small | `.case-study__desc` | 15.68 | 400 | 1.6 | – | – | #627b8b | 44rem |
| Small | `.code-item__note` | 13.12 | 400 | 1.6 | – | – | #627b8b | – |
| Meta | `.case-study__meta` | 11.84 | 500 | 1.15 | .06em | – | #627b8b | – |
| Meta | `.case-study__index` | 11.52 | 700 | 1.15 | .12em | – | #a34a42 | – |
| Meta | `.project-facts` | 12 | 400 | 1.6 | – | – | #152b43 | 52rem |
| Meta | `.code-item__file` | 14.4 | 400 | 1.6 | – | – | #627b8b | – |
| Meta | `.code-item__lang` | 10.56 | 620 | 1.3 | .1em | caps | #627b8b | – |
| Nav | `.nav-list a` | 13 | 400 | 1.6 | .06em | caps | #f2ede3 | – |
| Brand | `.brand-name` | 16 | 700 | 1 | .02em | caps | #f2ede3 | – |
| Brand | `.brand-descriptor` | 9.92 | 600 | 1 | .16em | caps | paper@72% | – |
| Button | `.portfolio-hero__action` | 13 | 700 | 1.2 | .03em | – | #faf7ef | – |
| Button | `.contact-actions .button` | 16 | 700 | 1.2 | – | – | #fff | – |
| Link | `.text-link` | 16 | 700 | 1.6 | – | – | #a34a42 / paper | – |
| Code | `.code-item pre` | 12.16 | 400 | 1.55 | – | – | #152b43 | – |
| Ticker | `.offer-ticker` | 11 | 400 | 1 | – | – | #00ff41 | – |
| Ticker act | `.offer-ticker__action` | 11 | 400 | 1 | .08em | caps | #00ff41 | – |
| Footer | `.site-footer` | 12.16 | 400 | 1.6 | – | – | #627b8b | – |
| Accordion | `.case-study__summary` | 19.2 | 620 | 1.15 | -.03em | – | #151719 | – |
| Accordion | `.code-item__summary` | 16 | 620 | 1.3 | -.01em | – | #151719 | – |

Captions: none live on the page (`.hero-visual figcaption`,
`.project-visual figcaption` are dead rules).

Findings:

T1. Same-level headings, four different sizes — H2 renders at 24 / 24 /
101 / 72 px; H3 at 24 / 36 / 11.2 / 12.8 px. Duplicate semantic styles.
T2. `font-weight: 620` is the most-used display weight (8 rules) and
cannot render in system stacks — collapses to ~600/700. 650 ×2, 800 ×1
also unreal. → standardize 400/600/700.
T3. 25 distinct letter-spacing declarations (-.085em … +.16em).
T4. Font-size sprawl: ~33 distinct computed sizes; mono micro-type alone
has 9 sizes in the 9.9–13 px band.
T5. `white-space: nowrap` on two section H2s — fits at 375 px by ~2 px;
pure hack.
T6. H1 fixed 4 rem at all widths → 5-line stack at 375 px; overflows
column +110 px @1024 / +205 px @768.
T7. Line heights scattered .88–1.9 with no scale; same "body" role at
14.4/15.68/16 px.
T8. Caps applied by `text-transform` (nav, eyebrows, lang chips) but
hand-typed in H2 source text — two casing mechanisms.
T9. Three lede scales (18/20/22.4/43 px) for one role.
T10. `.code-item__file` (14.4 px) is bigger than `.code-item__note`
(13.1) and body code text — inverted supporting hierarchy.

----------------------------------------------------------------------
2. COLOUR SYSTEM
----------------------------------------------------------------------

Complete live colour inventory:

| Colour | Role |
|---|---|
| #a07c33 ochre-dark | body canvas (pacman strip + footer field) |
| #5a7180 steel | header bar |
| #3f5563 | header border |
| #000 | ticker bg |
| #00ff41 | ticker text/action |
| #0a3d1f | ticker action bg |
| #2e5e79 | hero bg + feature bg (= artwork field; locked) |
| #e2e9e9 | systems + about bg; hero H1 text |
| #faf7ef | card/accordion surface; hero action text |
| #f2ede3 | nav/brand/contact text; paper |
| #152b43 | navy — image bg, tech-mark, contact, about text |
| #151719 | ink — primary text |
| #627b8b | muted blue — secondary text, rules-adjacent |
| #a34a42 | red — labels, links, CTA, accents |
| #bd8d32 | ochre — bars, eyebrows-on-dark, nav underline |
| #c8c0b3 | rule |
| #8e877d | rule-strong |
| #c8d2d2 | on-dark secondary text (hero lede, contact p) |
| #b9c4c7 | tech-mark caption (single use) |
| rgba(242,237,227,.32/.45/.5/.7/.72) | on-steel/navy decorative alphas |
| rgba(21,43,67,.10–.24) | elevation edge + shadows |
| dot-grid data-URI | texture on canvas/surface/wash |

Alias problems: `--accent`→navy, `--accent-dark`→ink, `--green`→ochre,
`--purple`→red (visited links render red by accident); `:focus-visible`
outline renders navy — invisible on navy.

Findings:

C1. Accidental aliases via the base→home remap — replace with semantic
tokens.
C2. Near-duplicate blues: #5a7180/#2e5e79/#3f5563/#627b8b/#152b43 —
header introduces 2 blues used nowhere else.
C3. One-offs: #b9c4c7, rgba alphas ×5, ticker trio, #c8d2d2.
C4. Contrast fails (measured): footer 1.15, descriptor 2.99, nav 4.38,
mono-meta-on-cream 4.15 (all < 4.5 at their sizes).
C5. Palette conflicts with hero: only the ticker (pure black + terminal
green) genuinely conflicts; everything else derives from the artwork.
C6. Surface-specific colours that must NOT be flattened (per
architecture audit): `--home-hero-bg` #2e5e79 (artwork lock), canvas
#a07c33 (interstitial + footer field), navy CTA, ticker (pending its
keep/restyle decision).

----------------------------------------------------------------------
3. CONTAINER / GRID
----------------------------------------------------------------------

Three competing container systems (measured left edges):

| Viewport | header-inner | hero | sections | case-list |
|---|---|---|---|---|
| 1440 | 113.5 | 121 | 101 | 224 |
| 1280 | 40 | 41 | 90 | 199 |
| 768 | 32 | 32 | 54 | 119 |
| 390 | 22 | 22 | 27 | 36 |

Sources: `.wrap` (min(100%−5rem,75rem) — itself redefined 3×: 76/78/75
rem), hero `max(2.5rem,(100vw−75rem)/2)`, sections
`clamp(1.25rem,7vw,9rem)`, `.case-study-list` 80%/95%.

Grids: hero `1fr 1fr` (right cell is dead `display:none` code), feature
1-col, about `1fr 1fr`, contact `1fr auto`, case-list 1-col stack.

Arbitrary values to tokenize: `--measure 75rem`, one `--gutter`,
`--content-col` for the accordion stack, `--gap-grid 1.25rem`.

----------------------------------------------------------------------
4. SPACING
----------------------------------------------------------------------

Live spacing inventory (~35 values): section pads 56/64/72/80/115/128/
130/144/159; component pads 17.6/22/24/27/30/32/35/36/40/48/86; gaps
14.4/20/24/32/40/48/82/102/115; interstitial 112; min-heights
340/352/400/440/464/520.

Logical tiers present:
- micro (4–16) inside rows/labels
- component (16–48) card/accordion padding
- section (56–160) block padding
- structural (240 art band, 400–520 min-heights, 112 interstitial)

Intentional architectural whitespace to PRESERVE (from Prompt-1 audit):
the 112 px ochre interstitial, the generous About padding supporting
the light-zone breath, and section block-pads once unified.

Findings:
SP1. No declared scale → adopt 4/8/12/16/24/32/48/64/96/144 rem-based.
SP2. `min-height` staircases duplicate what padding+content could do.
SP3. Accordion rows use padding-only sizing; inner code rows use
min-height 60 — one row recipe needed.

----------------------------------------------------------------------
5. CARDS / ELEVATION
----------------------------------------------------------------------

`.elevated` (site.css:3394–3450) IS the canonical system:
edge `1px rgba(21,43,67,.24)` + `inset 0 1px 0 rgba(255,255,255,.55)`
+ 3-layer shadow + −5 px hover + 200 ms ease-out.
Controls: `--elev-control` 2-layer + −2 px.

Live elevated components: `.feature-project`, 6× `.case-study`.
Controls elevated: hero action, contact button.

Findings:
E1. Canonical system = `.elevated` / `--elev-control`. Keep.
E2. Dead shadows to purge: `--shadow` rgba(25,55,92), `--shadow-card`
rgba(20,32,51/.12)+`rgba(0,0,0,.28)`, demo-card rgba(20,32,51),
feature-project base `rgba(20,32,51,.11)` (overridden but declared).
E3. Radius: everything live is square (`--panel-radius:0`). Eight dead
radii to purge.
E4. Flat vs raised assignment: raised = feature card, case-study rows,
primary buttons; flat = section fields, code-item rows, `pre` blocks,
tech-mark, ticker, header, footer. This is already correct — encode it.
E5. Accordions-as-cards vs "thin-rule" comment mismatch — decide naming;
behaviour is fine.

----------------------------------------------------------------------
6. BUTTONS / CONTROLS
----------------------------------------------------------------------

| Control | h | pad | font | bg→hover | text | shadow | lift |
|---|---|---|---|---|---|---|---|
| hero action | 48 | 12/16 | 13/700 | navy→ink | surface | ctrl | −2 |
| contact btn | 46.4 | 10/16 | 16/700 | red→paper | white→navy | ctrl | −2 |
| ticker action | 25 | 0/10–14 | 11 caps | #0a3d1f | #00ff41 | – | – |
| text-link | – | – | 16/700 | underline | red/paper | – | – |
| nav link | 35 | – | 13 caps | colour | paper | – | – |

Verdict: YES — one control system works: shared height 3 rem, pad
0.75/1.25 rem, weight 700, radius 0, elev-control, −2 px lift, 200 ms;
colour variants `navy` / `red` (+ `ghost`=text-link). Ticker action is a
chrome control — exception.

Focus visibility per surface (fix):
- light surfaces: current `--accent`→navy outline is fine on cream/wash.
- navy/steel/dark: use `--ochre` or `--paper` outline — hero action's
  red outline on steel is readable (5.4:1); keep red-on-dark or switch
  to ochre for consistency with CTA eyebrows.

----------------------------------------------------------------------
7. RESPONSIVE SYSTEM
----------------------------------------------------------------------

Media queries found: 70rem ×2, 68rem ×2, 64rem, 54rem ×3, 48rem,
min-48rem, 38rem ×7, hover, dark ×2, reduced-motion ×4.
Effective live breakpoints: 64/54/48/38. Dead: 70, 68.

Failures/hacks measured:
- H1 fixed 64 px → overflow @1024/+768, 5-line stack @375.
- nowrap H2s → ~2 px safety margin @375.
- feature image min-height gap 29 px @1024 / 33 px @768.
- scroll-padding magic numbers overshoot real header by up to 76 px.
- project-facts → `display:block` at ≤38 rem renders "/ PHP" lines.
- `.home-main--simple` padding-top 3.5rem/1.5rem dead (padding:0 wins).
- 7 separate `38rem` blocks — same breakpoint re-declared per pass.

Proposed coherent system: **3 breakpoints** —
`≤64rem` (tablet: hero/grid adjustments),
`≤48rem` (mobile: stacking, header column, art band),
`≤38rem` (small: fine-tuning).
Migrate 54 rem rules into 48 rem; delete 70/68 rem.

----------------------------------------------------------------------
8. ACCESSIBILITY
----------------------------------------------------------------------

- Landmarks/heading order OK; skip-link present.
- Fix: `aria-current="page"` on in-page anchor → `location` or remove.
- Fix: duplicated "About" eyebrow+h2; h3 same size as section h2
  (flattened hierarchy).
- Fix: focus ring invisible on navy (B3/C-alias above).
- Fix: contrast — footer 1.15, descriptor 2.99, nav 4.38, meta 4.15.
- OK: details/summary semantics, alt text, aria-hidden decor, reduced
  motion coverage, `pre` internal scroll.
- Minor: ticker `aria-label="Offers"` vs actual content; 10 duplicated
  sequences (2 suffice).

----------------------------------------------------------------------
9. FINAL TOKEN TABLE
----------------------------------------------------------------------

GLOBAL TOKENS

| Token | Value |
|---|---|
| --font-sans | "Helvetica Neue","Avenir Next","Segoe UI",Arial,sans-serif |
| --font-mono | ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace |
| --h1 | clamp(2.5rem,8vw,4rem)/700/1.05/-.04em |
| --h2 | clamp(1.75rem,4.5vw,3rem)/700/1.05/-.04em |
| --h3 | 1.375rem/600/1.2/normal |
| --label | .73rem mono/700/1.4/.12em/uppercase |
| --body | 1rem/1.6 |
| --lede | 1.125rem/1.5 (about variant 1.5rem) |
| --small | .78rem/1.5 |
| --code-size | .76rem mono/1.55 |
| --ls-tight -.04em / --ls-label .12em / --ls-normal 0 | tracking scale |
| --paper #f2ede3 | light text on dark |
| --surface #faf7ef | card surface |
| --canvas #a07c33 | page field (interstitial) |
| --ink #151719 | primary text |
| --navy #152b43 | dark surface + strong text |
| --hero-bg #2e5e79 | LOCKED (artwork) |
| --muted #4c6272 | secondary text (fixed for AA) |
| --wash #e2e9e9 | light-zone field |
| --red #a34a42 | links/accents/CTA |
| --ochre #bd8d32 | bars/on-dark accents |
| --rule #c8c0b3 / --rule-strong #8e877d | hairlines |
| --measure 75rem | content max-width |
| --gutter clamp(1.5rem,6vw,8rem) | one gutter all sections |
| --space-1..6 .5/1/1.5/2/3/4rem | component spacing |
| --space-section clamp(4rem,9vw,8rem) | section block pad |
| --radius 0 | square system |
| --edge 1px rgba(21,43,67,.24) | elevated edge |
| --shadow-card / --shadow-card-hover | existing elev stacks |
| --shadow-control / -hover | existing |
| --lift-card -5px / --lift-control -2px | hover elevation |
| --motion 200ms ease-out | all interactive transitions |
| --btn-h 3rem / --btn-pad .75/1.25rem / --btn-w 700 | control spec |
| --focus-light var(--red) / --focus-dark var(--ochre) | per-surface ring |
| --bp-lg 64rem / --bp-md 48rem / --bp-sm 38rem | breakpoints |
| --header-h (measured, e.g. 6.625rem→var per bp) | scroll-margin source |

SURFACE-SPECIFIC TOKENS (per architecture zones — not flattenable):

| Token | Value | Zone |
|---|---|---|
| --chrome-bg #5a7180 / --chrome-text paper / --chrome-line #3f5563 | header |
| --ticker-bg #000 / --ticker-text #00ff41 / --ticker-action #0a3d1f | ticker |
| --hero-text #e2e9e9 / --hero-sub #c8d2d2 | hero copy on art |
| --wash-field --wash / --wash-text ink / --wash-muted muted | light zone |
| --terminal-bg navy / --terminal-text paper / --terminal-sub #c8d2d2 | CTA |
| --accent-on-dark --ochre | eyebrows/underline on steel/navy |

INTENTIONAL EXCEPTIONS (kept by design):

- Hero artwork treatment + `--hero-bg` (policy-locked asset).
- Pacman interstitial band (canvas + hairline + ring) — the About→CTA
  transition device.
- `.technical-paper-mark` decorative block (if item 06 survives).
- Ticker palette — chrome exception pending its keep/restyle decision.
- About lede's larger scale (declared variant of --lede).
- `text-wrap: balance` on headings.
- Dot-grid texture on canvas/surface/wash.

DEPRECATED (purge at implementation): --ink/--paper/--accent family
remap, --green, --purple, --warm, --shadow, --shadow-card(old),
--panel-radius, --measure 76rem, --prose, all dead-section rules
(~30 selector groups, ~1,000 lines), 620/650/800 weights, nowrap H2
hacks, 70/68 rem breakpoints, duplicated mono stacks, hero-geometry
markup+CSS, pacman SVG markup+keyframes.

----------------------------------------------------------------------
READINESS

This table is implementation-ready once the architecture decisions
D1–D7 (section-architecture-audit-report.md §7) are locked — in
particular D1 (hero/feature zone), D4 (footer surface) and D7 (ticker),
since they determine whether the surface-specific token list above is
final.
