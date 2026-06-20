# SOCAR Figma Design Harness

Turn a one-line request — *"design the SOCAR app's new ___ screen"* — into a high-quality
Figma design built with the **socarframe** design system.

```
/auto 쏘카 앱의 반납 완료 화면 디자인해줘
```

`/auto` runs a five-stage sub-agent pipeline, each stage leaving an auditable artifact in
`runs/<id>/`, and finishes with a Figma link:

```
clarify → context → plan → implement → verify
   │         │         │        │          │
 01-…     02-…      03-…     04-…       05-…
```

- **clarify** understands the request and asks only blocking questions.
- **context** lists the socarframe tokens/components/screens to reuse.
- **plan** writes the design spec — layout, Korean copy, color/emphasis, components, states.
- **implement** builds it in Figma via the Figma MCP, using design tokens.
- **verify** inspects the result, scores it against the plan + design system, lists fixes.

## Start here

- `docs/ARCHITECTURE.md` — the harness contract (flow, artifacts, loops).
- `docs/socarframe/README.md` — the design-system style guide (colors, type, spacing, icons,
  components, principles) — the single source of truth for tokens.
- `CLAUDE.md` — working rules for this repo.
- `tests/` — sample requests to try (`tests/01-return-complete.md` is headless-safe).

## Requirements

- Claude Code with the **Figma MCP plugin** connected (`/plugin`).
- Headless Chrome (macOS `Google Chrome.app`) only if you re-sync the design-system docs via
  `tools/socarframe_scrape.py`.

Default Figma target: `https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled`
(override by including another Figma URL in the request).
