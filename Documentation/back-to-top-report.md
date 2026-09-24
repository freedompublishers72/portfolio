# Back to Top — Implementation Report

## Implementation

New shared component + one sitewide script:

- `assets/js/site.js` — new file. Creates the `<button>` element itself and
  appends it to `body`, so no inert markup exists when JS is unavailable.
  Scroll/resize listeners are passive and rAF-throttled. Loaded with `defer`
  in the `<head>` of `index.html`, `about.html`, and `404.html` (404 uses the
  absolute `/portfolio/` path matching its stylesheet convention).
- `assets/css/site.css` — new `.back-to-top` shared block (after the footer
  section), a home-scoped focus override, and two rules added inside the
  existing `prefers-reduced-motion` block.

No accordion content, structure, section layout, typography, tokens, or other
components were modified.

## Trigger threshold

`window.scrollY > window.innerHeight` — the control appears after one full
viewport of scrolling and hides again above it. Threshold is recomputed on
`resize`.

## Positioning

`position: fixed; right: 1.25rem; bottom: 1.25rem; z-index: 30` — below the
sticky header (`z-index: 20`) and above all in-flow content. Rendered size
140 × 44 px at every verified width — comfortably tappable (≥ 44 px height).

## Behaviour

- Click calls `window.scrollTo(0, 0)` with no explicit `behavior`, so it
  defers to CSS `scroll-behavior` — `smooth` normally, `auto` under
  `prefers-reduced-motion`. Verified: `scrollY` returns to 0.
- Hidden state uses `visibility: hidden` + `opacity: 0`, which also removes
  the control from the tab order when not visible.
- Accordions are native `<details>` elements; verified a `<details>` left
  open stays `open` after scroll + click. The control never touches
  accordion state or any other element.

## Visual treatment

Reuses the design system rather than introducing a component style: bridged
tokens with fallbacks — `var(--surface)`, `var(--ink)`,
`var(--rule-strong)`, `var(--font-mono)`, `var(--label)`, `var(--ls-label)`,
`var(--elev-control)` / `--elev-control-hover`, `var(--motion)`,
`var(--lift-control)`. On the home palette it renders as a small warm-paper
mono-label pill (`↑ BACK TO TOP`); under the base palette the same rule
resolves to the blue-on-white scheme. No new accent colour. Hover uses the
existing control-lift pattern (`translate` property, kept separate from the
entrance `transform` so they compose).

## Accessibility

- Real `<button type="button">` with `aria-label="Back to top"` and visible
  text `↑ Back to top` — the purpose is not icon-only.
- Keyboard accessible (native button, in tab order only when visible).
- Focus: site `:focus-visible` ring (2 px outline, 3 px offset); under the
  home palette the outline is forced to `--home-ochre` so it stays legible
  over both light and dark surfaces. Verified computed outline
  `rgb(189, 141, 50)` = `--home-ochre`, 2 px.
- Contrast: `--ink` text on `--surface` background — high contrast on both
  palettes.

## Responsive verification (Chromium, live server)

| Width | Hidden at top | Visible after 1 vh scroll | Size | CTA overlap |
|---|---|---|---|---|
| 1440 | yes | yes | 140×44 | no |
| 1280 | yes | yes | 140×44 | no |
| 1024 | yes | yes | 140×44 | no |
| 768  | yes | yes | 140×44 | no |
| 390  | yes | yes | 140×44 | no |
| 375  | yes | yes | 140×44 | no |

- No overlap with the sticky header/ticker (button is bottom-anchored; the
  ticker is top-anchored).
- No overlap with the contact CTA at the page bottom (measured boxes do not
  intersect at 390/375/768).
- The control transiently overlays the right edge of body content (including
  the footer copyright line at the scroll end) — standard trade-off for a
  fixed viewport control; it blocks no interactive element.
- `about.html` loads the script with no console errors (page is 2181 px
  tall at 1280 px wide, so the control can appear there too).
- `404.html` loads via the absolute `/portfolio/` path used by that page;
  the control simply never appears if the page doesn't scroll.

## Commit-isolation note

The working tree contained a large uncommitted redesign (the Modular Code
Blobs editorial work). To keep this task's commit clean, the pending diff
was saved to a patch, the two tracked files were reverted to HEAD, this
feature was committed alone, and the pending work was reapplied via
`git apply --3way`. Two merge conflicts in `site.css` were resolved by hand
(their section-header rename + relocated reduced-motion block); the final
file was diff-verified to equal *pre-task content + back-to-top additions
only*. Their work is fully preserved in the working tree, uncommitted as
before.

## `git diff --check`

Clean — no whitespace errors, both when run against the isolated task
changes (pre-commit) and against the final working tree (pending work +
this feature).
