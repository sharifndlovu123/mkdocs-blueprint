# mkdocs-blueprint

A drafting-sheet skin for [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Paper-and-ink colours, a 32px blueprint grid, Space Grotesk and Space Mono type, dashed rules, numbered callout bubbles and ruled "drawing schedule" tables. It is one CSS file plus an optional template for the mega-menu nav. No plugins.

Light is the default: pale blue paper with navy ink. Dark mode is a blue sheet with pale ink, chosen with the toggle. The accent is red-orange (light) or amber (dark).

![Home page](docs/assets/img/home.png)
![A note with a table and table of contents](docs/assets/img/note.png)
![Wide-screen drawing sheet](docs/assets/img/wide.png)
![Mega-menu](docs/assets/img/mega-menu.png)
![Search](docs/assets/img/search.png)

## Use it

1. Copy `docs/assets/css/blueprint.css` into your docs folder (for example `docs/assets/css/`).
2. Point `mkdocs.yml` at it and use the matching fonts and palette:

```yaml
theme:
  name: material
  font:
    text: Space Grotesk
    code: Space Mono
  palette:
    # Light first with no media query = light by default; the toggle remembers the choice
    - scheme: default
      toggle:
        icon: material/weather-night
        name: Switch to dark mode
    - scheme: slate
      toggle:
        icon: material/weather-sunny
        name: Switch to light mode
  features:
    - navigation.tabs        # sections as top tabs
    - navigation.tabs.sticky
    - navigation.sections    # left rail reads like a drawing index

extra_css:
  - assets/css/blueprint.css
```

Tip: number your folders and files (`01. Intro.md`) and the left rail becomes a sheet index.

## Mega-menu nav (optional)

Copy `overrides/partials/tabs.html` into an `overrides/partials/` folder in your project and set `custom_dir`:

```yaml
theme:
  custom_dir: overrides
```

Each top-level section becomes a tab. Hovering (or keyboard focusing) one opens a full-width panel listing its sub-sections and pages in columns. It is CSS-only, with no JavaScript, and long titles wrap.

## Search wording (optional)

`overrides/partials/languages/custom.html` changes the search placeholder and result labels ("7 sheets match"). Enable it with:

```yaml
theme:
  language: custom
```

## Wide screens

From 1600px the page becomes a bordered "drawing sheet" with corner registration marks, tables and code run the full width and prose keeps a readable measure. On very wide screens (2000px) short top-level lists flow into two columns.

## Customise

All colours are variables at the top of the file (`--bp-paper`, `--bp-ink`, `--bp-red`, `--bp-muted`, `--bp-panel`, `--bp-grid`). Change those for a different ink or paper. Radius and shadows are removed globally with one rule near the top.

Home page cards get numbered bubbles when you use Material's `grid cards` markup:

```markdown
<div class="grid cards" markdown>

- :material-cloud: **[Cloud](cloud.md)**

    Short description.

</div>
```

## Accessibility

Checked with WCAG 2.1 AA in mind, in both modes:

- Text and link colours meet **4.5:1** on every surface they sit on (light ink 12.0:1, light link red `#b43b0a` 4.6 to 5.1:1, muted 5.0 to 5.5:1; dark ink 9.6:1, amber 6.3 to 7.6:1). `tools/contrast.py` prints the ratios, so re-run it after changing a colour.
- Code highlighting tokens are set per mode so every token passes AA on the code background.
- Visible focus rings, underlined links, `prefers-reduced-motion` respected, no horizontal scroll at 375px.
- An axe-core scan (WCAG 2 A/AA plus best-practice) came back clean on the home page, a long note, tables and code pages in light and dark.
- `overrides/partials/search.html` and `progress.html` fix two unlabeled widgets in Material; `docs/assets/js/a11y.js` gives each code block's action group a unique name. All three are optional.
- The custom crosshair cursor is plain SVG in CSS, and falls back to the normal cursor on touch screens and in forced-colours mode.

## Notes

- Tested with Material for MkDocs 9.x (the sidebar width tweaks apply only at desktop widths, so the mobile drawer is unaffected). Fonts load from Google Fonts; self-host them if you need no external requests.
- Inspired by the blueprint skin of the author's CV site.

## Licence

MIT. See `LICENSE`.
