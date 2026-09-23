# Hero Artwork Assets

These assets are the approved visual source material for the portfolio hero redesign.

## Files

- `hero-background.svg` — composite reference artwork.
- `hero-gold-strands.svg` — transparent flowing gold strand artwork.
- `dolphin-fan.svg` — silver Dolphin Fan emblem/circle artwork.
- `hero-geometry.svg` — circle, purple vertical line, red rectangle, and black rectangle geometry.

## Intended implementation

Use these assets as the visual source instead of asking an image-generation model to recreate the artwork.

The live hero text and CTA must remain HTML and must not be baked into the artwork.

The approved visual relationship is:

steel-blue background
→ gold strands
→ silver Dolphin Fan / circle
→ purple vertical line behind circle
→ red rectangle `#a34a42`
→ black rectangle `#000000`

The golden strands visually connect into the silver-circle system from both sides.

The silver circle is substantially opaque and luminous; it is not a transparent glass effect.

For production, rasterize/optimize the approved artwork to WebP if the site's performance policy requires WebP. Preserve the SVG files as source artwork.

Do not replace these assets with newly generated artwork.
