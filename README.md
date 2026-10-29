# mkdocs-blueprint

A drafting-sheet skin for [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Paper-and-ink colours, a 32px blueprint grid, Space Grotesk and Space Mono type, dashed rules, numbered callout bubbles and ruled "drawing schedule" tables. It is one CSS file: no template overrides, no plugins.

Light mode is pale blue paper with navy ink; dark mode is a blue sheet with pale ink. The accent is red-orange (light) or amber (dark).

![Home page](docs/assets/img/home.png)
![A note with a table and table of contents](docs/assets/img/note.png)

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
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle:
        icon: material/weather-night
        name: Switch to light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle:
        icon: material/weather-sunny
        name: Switch to dark mode
  features:
    - navigation.sections   # left rail reads like a drawing index

extra_css:
  - assets/css/blueprint.css
```

Tip: number your folders and files (`01. Intro.md`) and the left rail becomes a sheet index. Drop `navigation.tabs` to keep everything in the rail.

## Customise

All colours are variables at the top of the file (`--bp-paper`, `--bp-ink`, `--bp-red`, `--bp-muted`, `--bp-panel`, `--bp-grid`). Change those for a different ink or paper. Radius and shadows are removed globally with one rule near the top.

Home page cards get numbered bubbles when you use Material's `grid cards` markup:

```markdown
<div class="grid cards" markdown>

- :material-cloud: **[Cloud](cloud.md)**

    Short description.

</div>
```

## Notes

- Tested with Material for MkDocs 9.x. Fonts load from Google Fonts; self-host them if you need no external requests.
- Inspired by the blueprint skin of the author's CV site.

## Licence

MIT. See `LICENSE`.
