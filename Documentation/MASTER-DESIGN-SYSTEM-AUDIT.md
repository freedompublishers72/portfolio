# Master Design System & Portfolio Audit

## 1. Document Status

- **Date**: 2026 (post Stage-6 final QA)
- **Repository**: `/var/www/html/portfolio` — one-page portfolio (`index.html`) + subpages (`about.html`, `case-studies/*.html`, `404.html`) sharing `assets/css/site.css`
- **Purpose**: single authoritative reference for the standardized portfolio design system — what was found, decided, implemented, and what remains open
- **Status**: FINAL — all six stages complete; final QA passed
- **Authority**: this document supersedes the individual stage reports for *what the current state is*. The stage reports remain the detailed evidence trail.

**Six-stage sequence consolidated here:**

| # | Stage | Record |
|---|---|---|
| 0 | Standardization audit (initial, absorbed into Stages 1–2) | `standardization-audit-*.md` |
| 1 | Page Architecture & Visual Section-Division Audit | `section-architecture-audit-*.md` |
| 2 | Design System & Standardization Audit | `design-system-audit-*.md` |
| 3 | Whole-Page Standardization Remediation | `standardization-remediation-*.md` |
| 4 | Individual Section Remediation — Modular Feature Blobs | `section-remediation-*.md` |
| 5 | Cross-Section Consistency Audit & Remediation | `cross-section-audit-*.md` |
| 6 | Final Visual / Responsive QA & Cleanup | `final-qa-*.md` |

**Legend used throughout:** **[FINDING]** discovered in an audit · **[DECISION]** agreed direction · **[IMPLEMENTED]** confirmed live by Stages 3–6 · **[EXCEPTION]** deliberately non-conforming · **[OPEN]** unresolved.

---

## 2. Executive Summary

The portfolio looked coherent at 1440px but the stylesheet was **five stacked design passes** (~3,473 lines), with roughly 1,000 lines targeting selectors no longer present in the HTML. The page ran three competing gutter systems, two colour-token layers connected by a semantic-remap hack, six breakpoints (two dead), three button specs, and a heading scale where one semantic level (H2) rendered at four unrelated sizes (24/24/101/72px).

The transformation, in order:

1. **Architecture first** — Stage 1 established the zone model (steel chrome → steel slab → wash zone → ochre interstitial → navy terminal → canvas footer) and a boundary grammar (colour flip = boundary; same colour = quiet hairline; black reserved for chrome) before any token work.
2. **Tokens second** — Stage 2 produced the canonical token table (type scale, palette, measure/gutter, spacing, elevation, controls, breakpoints) split into global / surface-specific / intentional-exception groups.
3. **Global remediation** — Stage 3 rewrote `site.css` as one system (~1,770 lines), unified the container edge across all surfaces, tokenized typography, fixed contrast failures and the invisible focus ring, consolidated breakpoints to three, and removed all verified-dead CSS.
4. **Section pass** — Stage 4 converged the Blobs section's remaining one-off values onto tokens and fixed a real mobile overflow bug.
5. **Cross-section pass** — Stage 5 found and fixed four residual drifts (duplicate on-dark muted literal, nav tracking, H3 tracking split, triple lede line-heights).
6. **Final QA** — Stage 6 removed the temporary black audit-guide block (the permanent boundary grammar went live), verified all six widths, and confirmed zero remaining style defects.

**Headline result**: one typography system, one container/gutter system, one colour-token layer, one elevation system, one control spec, three breakpoints, deliberate section architecture. Approved hero artwork, palette, order, and visual character preserved.

---

## 3. Page Architecture

**Final sequence** (unchanged — the audits found the order logically sound):

```
Header & Navigation
→ Welcome Hero          (introduction)
→ Feature Project       (credibility — flagship work)
→ Modular Feature Blobs (technical evidence — six case-study accordions)
→ About                 (personal / working context)
→ CTA / Commercial      (commercial action)
→ Footer
```

- **[FINDING]** The progression intro → credibility → evidence → context → action is correct; no section was misplaced or detached.
- **[FINDING]** Visual-weight inversion in the original: "About" (101px) was louder than the CTA (72px) — resolved by the unified `--h2`; the CTA is now the second-loudest heading after the H1. **[IMPLEMENTED]**
- **[FINDING]** Travel Bonanza is not a peer section — it is accordion item 06 inside Blobs, expanding to a decorative `.technical-paper-mark` only. Its position as a footnote to the SRIA case study is intentional and retained. **[EXCEPTION]**
- **[FINDING]** Original imbalance: one ~1,400px steel slab held a single card while six evidence rows occupied ~460px collapsed. Layout structure retained; imbalance noted, not redesigned.

---

## 4. Section-Division System

**Final grammar** **[DECISION][IMPLEMENTED]**: a colour flip *is* the boundary; same-colour neighbours get a quiet hairline; whitespace carries the rest; black is reserved for chrome. No rule is placed where a surface change already does the work.

| Boundary | Surface relationship | Whitespace | Rule | Final treatment | Mobile |
|---|---|---|---|---|---|
| Header → Hero | steel → steel (same zone family) | none needed | ticker band | **Ticker is the boundary** — the former steel-line under it was redundant | unchanged |
| Hero → Feature | `--home-hero-bg` → `--home-hero-bg` (one continuous steel zone) | ~230px | 1px `--home-steel-line` | **Quiet structural hairline** — whispers the boundary inside a shared zone | same; mobile art band adds a natural full-stop |
| Feature → Blobs | steel → wash (full flip) | ~128px pad | none | **Colour alone** — cleanest transition on the page | same |
| Blobs → About | wash → wash (same light zone) | ~200px | 1px `--home-rule-strong` | **Quiet warm-grey hairline** — same-colour neighbours need the whisper, not black | same |
| About → CTA | wash → **canvas interstitial** → navy | 112px band | navy hairline inside the band | **Interstitial is the transition device** — strongest boundary, no extra rule | same |
| CTA → Footer | navy → canvas | — | 1px `--home-rule-strong` | Quiet hairline | same |

- **[FINDING][RESOLVED]** Hero→Feature was the weakest boundary — a 1,900px continuous steel slab. **[DECISION]** treated as one zone + quiet hairline (the "differentiate Feature's background" alternative remains an open design option, not a defect). **[OPEN — optional]**
- **[FINDING][RESOLVED]** About→CTA was over-marked (grey rule + interstitial + black rule + navy flip). Now: interstitial + flip only.
- **[FINDING]** `.pacman-wrap` (112px ochre band with navy hairline + red circle motif) is a genuine independent transition — belongs to neither section. Retained. **[EXCEPTION]**
- **Role of the 1px rule**: *primary* separation = surface/colour change; *secondary* = whitespace; *tertiary structural* = the quiet hairline for same-colour neighbours; *decorative* = interstitial motifs. The temporary black rules were audit guides, never the design. **[RESOLVED — removed in Stage 6]**

---

## 5. Colour Architecture

**Zone sequence** (top→bottom): steel chrome (header+ticker) → steel slab (hero+feature) → wash zone (systems+about) → ochre canvas interstitial → navy terminal CTA → canvas footer.

### Final home palette (`body:has(.home-main--simple)`)

| Token | Value | Purpose | Scope | Status |
|---|---|---|---|---|
| `--home-paper` | #f2ede3 | warm paper text on dark | hero/feature/contact text | implemented |
| `--home-canvas` | #a07c33 | page canvas / interstitial / footer field | body bg | implemented |
| `--home-steel` | #5a7180 | header chrome | header | implemented |
| `--home-steel-line` | #3f5563 | hairline on steel surfaces | header bottom, hero→feature | implemented |
| `--home-hero-bg` | #2e5e79 | hero artwork field + feature zone | hero, feature | implemented — **locked to artwork** |
| `--home-surface` | #faf7ef | card/elevated surface | cards, pre | implemented |
| `--home-ink` | #151719 | primary text | light surfaces, footer | implemented |
| `--home-navy` | #152b43 | terminal CTA surface, marks, body text on warm | contact, tech-mark, buttons | implemented |
| `--home-blue` | #4c6272 | secondary/muted text | all muted text | **darkened from #627b8b** — contrast fix |
| `--home-ochre` | #bd8d32 | accent bars, eyebrows, focus-on-dark | decor + focus | implemented |
| `--home-red` | #a34a42 | links, labels, CTA button, focus-on-light | links/labels/controls | implemented |
| `--home-blue-wash` | #e2e9e9 | light zone surface | systems, about | implemented |
| `--home-ochre-wash` | #eee4ca | (defined; decorative wash reserved) | — | retained |
| `--home-rule` / `--home-rule-strong` | #c8c0b3 / #8e877d | hairlines | component rules, section quiet rules | implemented |
| `--on-dark-muted` | #c8d2d2 | secondary text on navy/steel | hero lede, contact body, tech-mark meta | **added in Stage 5** — merged `#b9c4c7` near-duplicate |
| `--home-texture` | SVG dot data-URI | grain on canvas/wash/surface | body, sections, cards | implemented |
| ticker | #000 / #00ff41 / #0a3d1f | console chrome | offer ticker | **[EXCEPTION]** — intentional |

### Aliases and duplicates found

- **[FINDING][RESOLVED]** The `body:has()` bridge remaps shared base vars into the home palette (`--accent`→navy, `--accent-dark`→ink, `--purple`→red, `--green`→ochre, etc.). It was an accidental-alias hack — **retained deliberately** because shared component rules (buttons, links, nav) depend on it; it is now documented as the home-theme bridge, not a defect.
- **[FINDING][RESOLVED]** `a:visited` rendered red via the `--purple`→red alias — visually consistent with unvisited red links; harmless, kept.
- **[FINDING][RESOLVED]** `#b9c4c7` vs `#c8d2d2` on-dark muted duplicate → unified under `--on-dark-muted`.
- Subpage palette (`:root` blue/ink set + dark-scheme block) is **surface-specific to non-home pages** — untouched. **[EXCEPTION]**
- No colour conflicts with the approved hero palette; the ticker is the only palette-alien element and is intentional.

### Contrast fixes applied **[IMPLEMENTED]**

- Nav links + brand descriptor → `#fff` on steel (4.38→4.86, 2.99→~4.9)
- `--home-blue` #627b8b → `#4c6272` (metadata ~4.15 → ~5.4 on surface)
- Footer text → `--home-ink` on canvas (1.15 → ~4.6)
- Focus rings per-surface (see §10)

---

## 6. Typography System

### Final scale (home)

| Role | Family | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|---|---|---|---|---|---|---|---|
| H1 | sans | `clamp(2.5rem,8vw,4rem)` | 700 | 1.05 | −0.04em | — | hero only; second line `nowrap` ≥48rem |
| H2 | sans | `clamp(1.75rem,4.5vw,3rem)` | 600 | 1.05 | −0.04em | — | all section titles incl. About |
| CTA display | sans | `clamp(2.5rem,5vw,5.5rem)` | 700 | 0.9 | −0.04em | — | contact h2 — deliberate loudness #2 |
| H3 / item titles | sans | `1.375rem` | 600 | 1.15 | −0.04em | — | card title, about-grid, case-study rows |
| Label / eyebrow | mono | `0.73rem` | 700 | 1.4 | +0.12em | upper | project-label, code-titles, index, lang badge |
| Body | sans | `1rem` | 400 | 1.6 | normal | — | incl. accordion body |
| Lede | sans | `1.125rem` | 400 | 1.5 | normal | — | hero, systems intro, feature desc |
| Lede-large | sans | `1.5rem` | 400 | 1.3 | normal | — | About lede — declared variant |
| Small / meta | mono/sans | `0.78rem` | 400–600 | 1.6 | +0.06em mono | — | meta, notes, file links, footer |
| Code block | mono | `0.76rem` | 400 | 1.55 | normal | — | `pre`, `overflow-x:auto` |
| Nav | sans | `0.8125rem` | 400 | — | +0.12em | upper | shares label tracking |
| Buttons | sans | `1rem` | 700 | 1.2 | +0.01em | — | one spec |
| Brand | sans | `1rem` / `0.62rem` | 700/600 | 1 | +0.02em/+0.12em | upper | name / descriptor |

### What was wrong → final **[RESOLVED]**

- H2 at 24/24/101/72px for one semantic level → single `--h2`; CTA keeps its own display size.
- Weights 620/650 (unrenderable in system stacks) → 600/700.
- ~16 letter-spacing declarations → `--ls-tight` / `--ls-label` / normal (+0.06em mono cluster).
- Five lede sizes (18/20/22.4/43.3/16) → `--lede` + `--lede-lg`.
- Lede line-height drift (1.5/1.6/1.4) → `--lh-lede: 1.5` (Stage 5).
- `white-space:nowrap` hacks on section H2s → removed; desktop-only `nowrap` kept on H1 line 2 (intentional overlap). **[EXCEPTION]**
- `code-item__file` specificity bug (rendered 14.4px instead of ~12px) → fixed.
- H1 fixed 64px → clamp; mobile was a 5-line stack → now 40px/3 lines.

**Families**: `--font-sans` ("Helvetica Neue", "Avenir Next", "Segoe UI", Arial) on home; `--font-mono` (ui-monospace stack) for labels/meta/code. Subpages keep the base system-ui stack. **[EXCEPTION — surface-specific]**

---

## 7. Container / Grid System

**Final system** **[IMPLEMENTED]** — one formula everywhere on home:

- `--home-measure: 75rem` (global `--measure` also set to 75rem for site-wide consistency)
- `--gutter: clamp(1.25rem, 7vw, 9rem)` (20px floor at ≤38rem → effective 20px via `1.25rem` override… actually `--gutter` is overridden to `1.25rem` inside the ≤38rem block)
- `.wrap` (header/footer): `width: min(100% - 2·gutter, measure)`
- Sections: `padding-inline: max(gutter, (100% - measure)/2)`

**Measured content edges — identical at every width:**

| Width | Edge offset |
|---|---|
| 1440 | 112px |
| 1280 | 90px |
| 1024 | 72px |
| 768 | 54px |
| 390/375 | 20px |

**[FINDING][RESOLVED]** Previously three competing systems produced four different left edges (hero `max(2.5rem,(100vw−75rem)/2)`, `.wrap` `min(100%−5rem,75rem)`, sections `clamp(1.25,7vw,9rem)`, case-list `80%`).

- `.case-study-list` → `grid-template-columns: minmax(0,1fr)`, full content column (was 80%/95% — and the implicit `auto` track caused the ≤38rem overflow bug).
- Columns: hero 2-col (1.1fr/0.9fr ≤64rem, 1fr ≤48rem); about-grid 2-col (1fr ≤38rem); contact 1fr+auto (1fr ≤48rem); feature card 1-col always.
- Text measures: section headings 70rem cap; `h2` max 18ch; lede caps 45–62rem; code-item bodies 56/62rem progressive measure. **[EXCEPTION — deliberate reading measures]**

---

## 8. Spacing System

**Section block**: `--section-pad: clamp(4rem,9vw,8rem)` — symmetric top/bottom on feature, systems, about, contact (was 130/159, 56, 144, 115 asymmetric rhythms).

**Component spacing (final, on the converged scale):**

| Element | Value |
|---|---|
| Heading block → content | `clamp(2rem,4vw,3rem)` margin-bottom |
| Ochre bar → h2 | 1.5rem; bar width `clamp(3rem,7vw,7rem)` × 0.3rem |
| Case-study list gap | 1.5rem |
| Case-study padding | `0 1.5rem` (1rem ≤38rem) |
| Summary row padding | `1.15rem 2rem 1.15rem 0` |
| Card copy padding | `clamp(2.25rem,6vw,6rem)` / sides `clamp(1.25rem,6vw,7rem)` |
| Code-item row min-height | 3.75rem (3.5rem ≤38rem) |
| Interstitial height | 7rem fixed **[EXCEPTION]** |
| Header height | 5rem inner + 25px ticker |
| Footer padding | 1.35rem block |

**Intentional non-standard spacing retained**: the ~230px hero→feature breathing room inside the steel zone, the 112px interstitial, and `--min-height` presence sizing (hero 32.5rem, contact 25rem, mark 22rem). `.systems-section`'s `min-height:100vh` was **removed** (accidental dead air, not architectural). **[RESOLVED]**

---

## 9. Cards & Elevation

**Canonical system — `.elevated`** **[IMPLEMENTED]** (the only card elevation on the site):

| Property | Value |
|---|---|
| Border | `1px solid rgba(21,43,67,.24)` (`--elev-edge`) |
| Highlight | `inset 0 1px 0 rgba(255,255,255,.55)` |
| Shadow | `--elev-card`: `0 1px 2px /.16`, `0 5px 14px /.10`, `0 22px 44px /.13` |
| Hover shadow | `--elev-card-hover`: `0 2px 4px /.17`, `0 12px 28px /.14`, `0 36px 64px /.17` |
| Hover lift | `translateY(-5px)` (`--lift-card`), `200ms ease-out` |
| Radius | 0 (site-wide square) |
| Surfaces | `--home-surface` + dot texture |

**Controls** use `--elev-control` / `--elev-control-hover` with `translateY(-2px)` (`--lift-control`).

- **Raised**: `.feature-project`, six `.case-study` cards.
- **Flat**: `.code-item` rows (hairline separators inside cards), `.technical-paper-mark`, all text sections, hero, contact.
- **[FINDING][RESOLVED]** Three competing shadow recipes and eight radius values existed only in dead rules — purged.

---

## 10. Buttons & Controls

**One control spec** **[IMPLEMENTED]**, colour variants per surface:

| Property | Value |
|---|---|
| Height | 3rem min |
| Padding | 0.75rem / 1.25rem |
| Font | 1rem, weight 700, ls +0.01em |
| Border | 1px solid (surface-matched), radius 0 |
| Shadow | `--elev-control` |
| Hover | −2px lift + `--elev-control-hover`, `200ms` |
| Transition | transform + box-shadow + colours, `200ms ease-out` |

**Variants**: hero action = navy on steel (→ ink hover); contact button = red on navy (→ paper hover); `.text-link` = red (light) / paper (dark); ticker action = green-on-dark-green console **[EXCEPTION]**; nav links = white caps + ochre current underline.

**Focus** **[IMPLEMENTED]**: `outline:2px`, `offset:3px`; `--home-red` on light surfaces; `--home-ochre` on dark surfaces (header/hero/feature/contact/mark); green in ticker. **[FINDING][RESOLVED]** the ring was previously invisible navy-on-navy.

---

## 11. Responsive System

**Final breakpoints** **[IMPLEMENTED]**: `≤64rem` (tablet), `≤48rem` (mobile stack), `≤38rem` (small) + one `min-width:48rem` rule (H1 nowrap) + a shared `≤54rem` chrome block for subpage header/footer stacking + `hover:hover` and `prefers-reduced-motion` queries.

- **[FINDING][RESOLVED]** Six breakpoints (70/68/64/54/48/38) collapsed to three; the 70/68rem rules were dead.
- `--header-h` token (7rem / 9.5rem at ≤48rem) drives `scroll-padding-top` + `scroll-margin-top` — replaced four drifted literals that overshot anchors by up to 76px.
- Mobile hero: 1-col, `auto 15rem` right-anchored art band, `overflow:hidden`, 4rem→3rem top pad.
- Cards: full content column; case-study padding 1rem; meta wraps to own line ≤38rem; `pre` scrolls horizontally.
- All six audited widths verified: zero horizontal overflow (incl. all accordions open), identical edges, no clipped text, no nav collision, ticker loops.

---

## 12. Image & Graphic System

| Asset | Treatment |
|---|---|
| `hero-artwork.webp` (approved master) | `background: var(--home-hero-bg) url(...) 55% center / cover`; mobile `auto 15rem` at `100% 100%` — **authoritative; must not be regenerated, redesigned, or approximated** (`hero-artwork-policy.md`) |
| `sria-homepage.jpg` 1600×760 | `width:100%; height:auto`; `filter: saturate(.82) contrast(1.04)` **[EXCEPTION]**; container `overflow:hidden`, navy bg; `min-height` removed (killed the navy-strip gap at 1024/768) |
| `.technical-paper-mark` | pure CSS navy block + paper circle + red slash; `min-height:22rem`; `aria-hidden` **[EXCEPTION]** |
| `.pacman-wrap` | CSS pseudo-elements only (navy hairline + red circle + ochre dot); 7rem **[EXCEPTION]** |
| `.contact-section::after` | paper-alpha circle outline, clipped by `overflow:hidden` |
| Ticker cars | 19px emoji/art + `scaleX(-1)` + hue-rotate accents **[EXCEPTION]** |

- **[FINDING][RESOLVED]** Dead decorative spans (`.portfolio-hero__geometry` + 4 shapes) and the hidden `.pacman` SVG removed from markup + CSS.

---

## 13. Modular Feature Blobs / Accordion System

**Anatomy** (final): `.case-study-list` grid `minmax(0,1fr)` gap 1.5rem → `.case-study` (`details`, `.elevated`, padding `0 1.5rem`) → `summary.case-study__summary` (index `--label` red mono · name `--h3` · meta `--small` mono right-aligned · "+/–" icon) → `.case-study__body` (desc `--body` muted · `.code-examples` hairline-topped · `.code-accordion` of flat hairline `.code-item` rows) → `.case-study__more` red text-link.

- Code items: summary 1rem/600 + `--label` lang badge; body sections h4 `--small` mono headings; `pre` `--code-size` with 0.3rem ochre left bar (unified from 0.2rem); inline `code` boxed; file links `--small`; notes `--small` hairline-topped.
- Hover: name/title → red (`200ms`); cards lift via `.elevated`; open = "–".
- Mobile: meta wraps `flex-basis:100%` ≤38rem; `minmax(0,1fr)` prevents intrinsic-width overflow.
- **[EXCEPTION]** Item 06 (Travel Bonanza): description + `.technical-paper-mark`, no code items — deliberately different anatomy.
- **[OPEN — content]** item 06's "more" link targets the same case study as item 05; the promised technical paper is unlinked.

---

## 14. Section-by-Section Remediation

### Header & Navigation
- **Found**: nav 4.38:1, descriptor 2.99:1 contrast; `aria-current="page"` on an anchor; nav tracking off-family; scroll-padding overshoot.
- **Done**: white text on steel; `aria-current="location"`; `--ls-label`; `--header-h` token; focus ochre.
- **Final**: sticky steel chrome, ticker boundary band. **Remaining**: none.

### Welcome Hero
- **Found**: H1 fixed 64px overflowed its column (+110px @1024, +205px @768) and stacked 5 lines at 375; dead geometry spans; 13px button off-spec.
- **Done**: `--h1` clamp; dead markup removed; action → shared control spec.
- **Final**: 64px desktop / 40px mobile, intentional nowrap-overlap ≥48rem, artwork untouched. **[EXCEPTION]** the desktop overlap is approved character. **Remaining**: none.

### Feature Project
- **Found**: H2 24px caps one-off; image container `min-height` outlived `height:auto` → 29–33px navy strip; copy desc a fifth lede size.
- **Done**: `--h2`; `min-height` removed; desc → `--lede`; h3 → token.
- **Final**: elevated card, label/h3/lede/facts/link/image anatomy. **Remaining**: none.

### Modular Feature Blobs
- **Found**: 11 one-off values + a real ≤38rem overflow bug (implicit grid track + `flex-basis:100%` meta inflated past viewport).
- **Done**: all roles tokenized (see §13); `minmax(0,1fr)` fix; mobile size overrides removed.
- **Final**: verified all-open at all widths, zero overflow. **Remaining**: item-06 content link (content-level).

### About
- **Found**: duplicate eyebrow+h2 "About"; 101px display h2; 43px one-off lede; 2-col grid cramped on mobile.
- **Done**: eyebrow removed; `--h2`; `--lede-lg`; grid → 1fr ≤38rem.
- **Final**: quietest section per hierarchy order; hairline-topped intro; ochre-bar h3s. **Remaining**: none.

### CTA / Commercial
- **Found**: button off-spec (46px/red one-off); invisible navy focus ring; over-marked top boundary.
- **Done**: shared control spec (red variant); ochre focus on navy; boundary = interstitial+flip only.
- **Final**: navy terminal band, 72px display h2, paper text, red/paper controls. **Remaining**: none.

---

## 15. Accessibility

**RESOLVED:**
- Contrast: footer 1.15:1 → ~4.6 (ink on canvas); brand descriptor 2.99 → ~4.9; nav 4.38 → ~4.86; muted cluster ~4.15 → ~5.4.
- Focus: per-surface outline colours — visible on every surface including navy CTA and ticker.
- `aria-current="page"` → `"location"` on the same-page anchor.
- Duplicate "About" eyebrow removed (was eyebrow + identical h2).
- `code-item__file` specificity bug fixed (semantic size restored).
- Scroll anchoring: `--header-h`-driven `scroll-padding`/`scroll-margin` — no more 76px overshoot.

**Verified OK:** h1→h2→h3→h4 order; `aria-labelledby` all sections; nav `aria-label`; ticker labelled region + `aria-hidden` track; `aria-hidden` decor; native `details`/`summary` keyboard+state; feature `img` descriptive `alt`; skip link; consolidated `prefers-reduced-motion` (ticker static, transitions/lifts off, instant scroll).

**REMAINING (minor, content-level):** ticker `aria-label="Offers"` describes a decorative car strip — label/content mismatch from the original design; hero lede on hero-bg ~4.55:1 is a marginal pass.

---

## 16. Motion & Interaction

| Behaviour | Spec |
|---|---|
| Standard transition | `200ms ease-out` (`--motion`) |
| Card hover | −5px lift + shadow deepen |
| Control hover | −2px lift + shadow |
| Link/name hover | `color 200ms` (was instant snap) |
| Accordion | native `open` toggle; "+/–" icon swap |
| Ticker | 144s linear translate loop |
| Reduced motion | one consolidated block: ticker static+scrollable, lifts/transitions off, `scroll-behavior:auto` |

**[EXCEPTION]** ticker animation is the only perpetual motion on the page.

---

## 17. CSS / Structural Cleanup

**Confirmed removed (Stages 3+6):**
- ~1,700 lines total: all layer-1/2/3 remnants for selectors present in no HTML (`.hero*`, `.project-panel`, `.featured-project`, `.section-intro`, `.section-heading`, `.projects-stack`, `.project-card*`, `.system-grid`, `.system-card*`, `.demo-*`, `.capabilit*`, `.code-section`, `.code-index`, `.button-secondary`, `.card-link`, `.hero-cover`, `.project-mark-arrow`, `.tag-list`, `.card-number`, `.card-meta`)
- `.portfolio-hero__geometry` CSS + markup; `.pacman` SVG CSS + `@keyframes` + markup
- Dead 70rem/68rem media blocks; dead rules inside 54/38rem blocks
- Superseded tokens: `--shadow`, `--shadow-card`, `--panel-radius`, `--warm`
- **Stage 6**: temporary black audit-guide block
- `.systems-section` `min-height:100vh`; feature-image `min-height`s; `.project-facts` mobile `display:block` hack; `.code-section` group-membership leftovers

**HTML cleanup**: geometry spans, pacman SVG, About eyebrow — removed; `aria-current` corrected. Content/order untouched.

---

## 18. Temporary Audit Elements — Definitive List

| Element | Purpose | Final status |
|---|---|---|
| Black 1px boundary block (`site.css` tail, ~lines 3452–3473) | visualize section boundaries during audit | **REMOVED (Stage 6)** — replaced by the permanent quiet grammar beneath |
| `.pacman` hidden SVG | abandoned pacman animation concept | **REMOVED** — `.pacman-wrap` pseudo-decor remains as the interstitial |
| `.portfolio-hero__geometry` spans | abandoned decorative overlay | **REMOVED** |
| 10× duplicated ticker sequences | loop-safe track padding | **RETAINED** — harmless markup duplication |

No temporary element remains in the CSS.

---

## 19. Intentional Exceptions (authoritative list)

Deliberately **not** conforming to the global system:

1. Approved hero artwork + `--home-hero-bg` — policy-locked.
2. Ticker palette/anatomy (black/green console) — chrome exception.
3. `.pacman-wrap` interstitial — independent transition device.
4. `.technical-paper-mark` — navy mark inside item 06.
5. CTA display heading `clamp(2.5rem,5vw,5.5rem)` — second-loudest by design.
6. `--lede-lg` 1.5rem About variant.
7. Progressive text measures (56/62rem) inside accordions.
8. `min-height` presence sizing: hero 32.5rem, contact 25rem, mark 22rem.
9. Paper-alpha decorative strokes at 0.32/0.45/0.7.
10. Non-caps mono cluster at 0.06em vs caps-label 0.12em.
11. Desktop `nowrap` on H1 line 2 (`min-width:48rem`) — produces the intentional overlap.
12. `saturate(.82) contrast(1.04)` on the feature screenshot.
13. Subpage palette/type stack (blue `--accent` system-ui family) — separate surface.
14. The shared-component variable bridge (`--accent`→navy etc.) — retained plumbing, documented.

---

## 20. Remaining Issues

| Issue | Location | Severity | Reason not resolved | Next action |
|---|---|---|---|---|
| Item 06 "more" link duplicates item 05's target | `.case-study` 06 | content | content decision, not style | point at the real technical-paper artifact when it exists |
| "Technical paper" referenced but unlinked | item 06 | content | asset doesn't exist yet | publish/link when written |
| Ticker `aria-label="Offers"` vs car-strip content | header ticker | minor a11y | label predates current content | relabel or re-skin in a content pass |
| Hero lede ~4.55:1 on hero-bg | hero | marginal | at the pass boundary; text role is large-ish | optionally brighten `--on-dark-muted` |
| Hero→Feature could still be differentiated further | zone seam | optional design | zone decision was "one steel zone + hairline" | revisit only if a new architecture audit reopens D1 |

---

## 21. Final Design Token Reference — *implemented* values

All tokens live on `body:has(.home-main--simple)` unless noted.

### Typography
`--font-sans` · `--font-mono` · `--h1 clamp(2.5rem,8vw,4rem)` · `--h2 clamp(1.75rem,4.5vw,3rem)` · `--h3 1.375rem` · `--label 0.73rem` · `--body 1rem` · `--lede 1.125rem` · `--lede-lg 1.5rem` · `--small 0.78rem` · `--code-size 0.76rem` · `--ls-tight -0.04em` · `--ls-label 0.12em` · `--lh-display 1.05` · `--lh-body 1.6` · `--lh-label 1.4` · `--lh-code 1.55` · `--lh-lede 1.5`

### Colours
`--home-paper #f2ede3` · `--home-canvas #a07c33` · `--home-steel #5a7180` · `--home-steel-line #3f5563` · `--home-hero-bg #2e5e79` · `--home-surface #faf7ef` · `--home-ink #151719` · `--home-navy #152b43` · `--home-blue #4c6272` · `--home-ochre #bd8d32` · `--home-red #a34a42` · `--home-blue-wash #e2e9e9` · `--home-ochre-wash #eee4ca` · `--home-rule #c8c0b3` · `--home-rule-strong #8e877d` · `--on-dark-muted #c8d2d2` · `--home-texture` (dot SVG)

### Layout
`--home-measure 75rem` · `--gutter clamp(1.25rem,7vw,9rem)` (→1.25rem ≤38rem) · container = `min(100% − 2·gutter, measure)` / `max(gutter, (100%−measure)/2)` · `--header-h 7rem` (→9.5rem ≤48rem) · `--section-pad clamp(4rem,9vw,8rem)`

### Borders
`--elev-edge rgba(21,43,67,.24)` · hairlines `--home-rule`/`--home-rule-strong`/`--home-steel-line` · accent bars 0.3rem ochre

### Elevation
`--elev-highlight` · `--elev-card` / `--elev-card-hover` (3-layer) · `--elev-control` / `--elev-control-hover` (2-layer) · `--lift-card -5px` · `--lift-control -2px` · radius 0

### Controls
3rem min-height · 0.75/1.25rem padding · 1rem/700/+0.01em · elev-control · focus: `--home-red` light / `--home-ochre` dark

### Motion
`--motion 200ms ease-out` · ticker 144s linear · reduced-motion kills all

### Breakpoints
`≤64rem` tablet · `≤48rem` mobile stack (+`min-width:48rem` nowrap) · `≤38rem` small · `≤54rem` shared chrome (subpages)

---

## 22. Final Page Blueprint

| Section | Surface | Container | Type hierarchy | Padding | Primary treatment | Boundary out | Special |
|---|---|---|---|---|---|---|---|
| Header + ticker | steel / black ticker | wrap | brand + label nav | 5rem/25px | sticky chrome | ticker band | aria region |
| Hero | `--home-hero-bg` + artwork | section gutter | h1 64 + lede 18 + btn | — | cover art 55% center | steel-line ↓ | nowrap overlap; mobile art band |
| Feature | `--home-hero-bg` (same zone) | section gutter | bar + h2 48 → elevated card | 128px | paper card + ochre bar + screenshot | colour flip ↓ | image `height:auto` |
| Blobs | `--home-blue-wash` + texture | section gutter | bar + h2 48 + lede → 6 elevated `details` | 128px | accordion cards, hairline code rows | rule-strong ↓ | item 06 mark |
| About | `--home-blue-wash` + texture | section gutter | bar + h2 48 + lede-lg → 2-col h3 grid | 128px | quiet text zone | interstitial ↓ | 1-col ≤38rem |
| Interstitial | `--home-canvas` | full-bleed | — | 7rem | navy hairline + red circle | — | `.pacman-wrap` |
| CTA | `--home-navy` + circle | section gutter | eyebrow + 72px display + p + controls | 128px | terminal band | rule-strong ↓ | red/paper controls |
| Footer | canvas | wrap | `--small` mono | 1.35rem | ink text, hairline top | — | — |

---

## 23. Implementation History

**Stage 0 — Standardization audit**: full inventory + rendered measurement at 6 widths; found the five-pass stylesheet, ~1,000 dead lines, 3 gutter systems, token aliasing, contrast failures, H1 overflow, nowrap hacks, dead breakpoints. Output: `standardization-audit-report.md`.

**Stage 1 — Architecture audit**: section order sound; zone map established; Hero→Feature identified as the weakest boundary; interstitial confirmed as an independent transition; boundary grammar proposed (flip/hairline/interstitial); 7 decisions queued for locking.

**Stage 2 — Design-system audit**: full type/colour/container/spacing/elevation/control/responsive/a11y inventories; proposed the canonical token table in global / surface / exception groups; identified `.elevated` as the canonical elevation and the shared-control spec.

**Stage 3 — Whole-page remediation**: rewrote `site.css` 3,473→~1,770 lines as one system; unified gutters (one edge at all widths); all type on tokens; contrast + focus fixed; breakpoints 6→3; dead CSS purged; 4 surgical HTML edits; verified all widths; subpages regression-checked. Temp block intentionally retained.

**Stage 4 — Section remediation (Blobs)**: 11 one-off values → tokens; **fixed a real mobile overflow** (implicit grid track + `flex-basis:100%`); mobile font overrides removed; verified all-accordions-open.

**Stage 5 — Cross-section audit**: verified consistency; fixed 4 drifts (`--on-dark-muted` merge, nav `--ls-label`, H3 `--ls-tight`, `--lh-lede`); re-verified all widths.

**Stage 6 — Final QA**: temp audit block removed; permanent boundary grammar live; boundaries verified at each seam; all six widths pass; a11y verified; zero remaining style defects.

**Git**: audit docs committed at `b8c63bd` (stage 0) and `2eee57b` (stage 2). Site changes + stage 1/3–6 docs were left uncommitted per per-stage instructions.

---

## 24. Authority & Future Development Rules

1. **This document is the authoritative record** of the standardized portfolio design system. The six stage reports are the evidence trail.
2. **Global tokens take precedence** over historical or section-specific CSS. Do not add one-off typography, spacing, or colour values without a documented reason recorded as an exception in §19.
3. **Never regenerate, redesign, or approximate the approved hero artwork** (`hero-artwork-policy.md`). CSS around it may change; the assets and `--home-hero-bg` may not.
4. **Do not add decorative elements to fill space.** Whitespace is architectural.
5. **Boundary grammar**: colour flip = boundary; same-colour neighbours = quiet hairline; black is chrome-only. Do not reintroduce prominent rules.
6. **Intentional exceptions must be documented** — add to §19, don't hide them in selectors.
7. **Test at the six established widths** (1440/1280/1024/768/390/375) with accordions both open and closed before declaring done.
8. **Do not reintroduce temporary audit elements** — the black-guide block is gone permanently.
9. **Preserve the information architecture** — section order, zone map, and the Travel-Bonanza-as-item-06 structure stand unless a new architecture audit reopens them.
10. **Shared stylesheet**: `site.css` also serves `about.html`, `case-studies/*`, `404.html` — home rules stay scoped under `body:has(.home-main--simple)`; don't break the subpage palette.
11. **Focus must remain visible on every surface** — use the red-light/ochre-dark pairing when adding controls.
