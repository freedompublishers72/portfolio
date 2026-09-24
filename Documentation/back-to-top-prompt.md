# Prompt — Sitewide Back to Top Button

Implement a Back to Top control for the portfolio.

## Behaviour

- The control should appear only after the user has scrolled a meaningful distance down the page.
- Clicking/tapping it returns the user to the top of the page.
- Use smooth scrolling where supported.
- It must work regardless of which accordion is open.
- It must not close an open accordion.
- It must not interfere with the existing accordion controls or links.

## Visual treatment

Keep it restrained and consistent with the existing portfolio design.
Use the established design system rather than introducing a new component style.
The control should be:

- small;
- unobtrusive;
- clearly identifiable;
- fixed to the viewport rather than embedded in a section;
- usable on both desktop and mobile.

Use the existing portfolio colour language. Do not introduce another accent colour.

## Accessibility

- Use an actual button/control with an accessible name such as `Back to top`.
- Keyboard accessible.
- Visible focus state.
- Sufficient contrast.
- Do not rely solely on an icon to communicate its purpose.

## Responsive

Verify at:

- 1440px
- 1280px
- 1024px
- 768px
- 390px
- 375px

Pay particular attention to:

- mobile viewport clearance;
- avoiding overlap with the fixed ticker/navigation;
- avoiding overlap with important CTA controls;
- ensuring the button remains comfortably tappable.

## Scope

This is an independent sitewide utility and can be implemented in parallel with the Modular Code Blobs editorial work.
Do not modify:

- accordion content;
- white-paper content;
- accordion structure;
- section layouts;
- typography;
- existing colour tokens;
- other components.

Run:

```
git diff --check
```

Report the implementation, trigger threshold, positioning, accessibility behaviour, responsive verification, and `git diff --check` result.
