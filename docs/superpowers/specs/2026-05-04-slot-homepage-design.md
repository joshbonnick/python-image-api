# Slot Homepage Design

## Summary

A single-page landing page for Slot, a placeholder image API. Developer audience. Reference-first layout with an interactive URL playground.

## Context

Slot generates SVG placeholder images via URL parameters (size, color, text). Currently the root route returns JSON. The homepage replaces that with an HTML page that documents the API routes and lets developers build URLs interactively.

## Design Foundation

**Scene**: A developer at their desk mid-afternoon, building a layout, needing placeholder image URLs fast. They switch between editor and this page, scanning route patterns, tweaking parameters, copying URLs.

**Theme**: Light. Cool-neutral tinted toward the brand hue. Not stark white, not warm-cream SaaS-doc.

**Color strategy**: Restrained. Tinted neutrals + one accent at <=10% surface.

- Background: `oklch(0.98 0.005 200)`
- Surface: `oklch(0.96 0.005 200)`
- Text primary: `oklch(0.15 0.005 200)`
- Text secondary: `oklch(0.45 0.005 200)`
- Accent (links, route highlights, interactive elements): `oklch(0.55 0.12 200)` — muted teal-cyan
- Code backgrounds: `oklch(0.93 0.008 200)`

**Typography**: System font stack, 65-75ch body measure. Route patterns in monospace at larger scale. Hierarchy through size and weight contrast (>=1.25 ratio).

**Name**: Slot

## Page Structure

Three sections, single column, no nav.

### 1. Header

- Name "Slot" at display size
- One-line description beneath: "Placeholder images via URL parameters"
- No nav links, no CTA button, no logo

### 2. Routes Reference

Each route shown as a prominent code block with:
- HTTP method + path pattern (e.g. `GET /svg/800x600/ff8800?text=hello`)
- Parameter table: name, type, default, notes
- One or two inline example images rendered from the route itself, so the API is demonstrated without leaving the section

Route patterns use monospace at 1.25-1.5x body size. Color swatches next to color parameters.

### 3. Playground

Compact interactive builder:

- Width + height inputs (linked by default for square, unlinkable for custom aspect ratios)
- Color input (text field accepting hex, with a small color preview swatch)
- Text input (optional)
- The constructed URL updates live as inputs change, shown in a read-only code block ready to copy
- A live preview `<img>` renders below the URL, sourcing from the constructed path

No "Generate" button — everything updates on input. One clear copy button next to the URL.

## Implementation

### Files to change

- `pythonimageapi/settings.py`: Add `BASE_DIR / 'pythonimageapi/templates'` to `TEMPLATES[0]['DIRS']` so Django finds the template
- `pythonimageapi/views.py`: Replace `index` JSON response with template render
- `pythonimageapi/templates/home.html`: Full page HTML with inline CSS (no external stylesheet needed for a single page)

### What the view passes to the template

- `routes`: list of route pattern strings extracted from the URL resolver (already computed)
- No other dynamic data needed — the playground runs client-side

### Client-side JS

Minimal vanilla JS for the playground:
- Listen to input changes, construct the URL string, update the code block and preview img src
- Square linking toggle
- Copy-to-clipboard

### No new dependencies

Single template file, inline styles, vanilla JS. No build step, no CSS framework, no JS library.

## Anti-patterns avoided

- No cards (route blocks are plain sections with a code background strip)
- No modals (copy feedback is inline text change)
- No side-stripe borders
- No gradient text
- No glassmorphism
- No hero-metric layout
- No identical card grids
- Em dashes in copy
