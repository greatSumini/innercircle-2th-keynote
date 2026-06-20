# socarframe — Figma library (built in-file)

A full socarframe design-system library was built **inside the team file**
`VuBHVaAnA5ORacxMZ9zcH8` (https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled) via the
Figma MCP. This is the bridge that lets the harness bind **real variables** and drop **component
instances** instead of pasting raw hex/px.

> The assets are **local to the file**. They work immediately for designs built in this file. To
> reuse them across *other* files/teams, a human must click **Publish** (see
> [Publishing](#publishing) — there is no API/MCP for that step).

## What was built

**Variable collections** (193 variables, all scoped + `var(--token)` code syntax):

| Collection | Mode | Count | Contents |
|-----------|------|-------|----------|
| `Primitives` | Value | 123 | Full palette — `white`/`black` + `gray/50…1000` + 11 hue families `…/50…900` |
| `Color` | Light | 40 | Semantic tokens **aliased** to primitives — `text/*`, `primary/*`, `status/*`, `accent/*`, `service/*`, `background`·`border`·`divider`, `notification/red`, `location/*` |
| `Spacing` | Value | 20 | `spacing/000 … spacing/1000` (px, 4px grid) |
| `Radius` | Value | 10 | `radius/100 … radius/600`, `radius/circle` |

**Text styles** (16): `display1 display2 heading1 heading2 heading3 title1–4 body1–4 caption1–3`.

**Components** (24 component sets/components across 4 pages). `Haptic` from the design system is a
non-visual behavior spec — documented in `docs/socarframe/components-actions.md`, not a Figma component.

| Page (id) | Components (node id) |
|-----------|----------------------|
| `🔘 Actions` (15:3) | ActionButton (16:12), IconButton (17:8), TextButton (17:15) |
| `📝 Forms` (15:4) | Input (19:22), TextArea (19:38), Checkbox (20:12), Radio (20:22), Chip (21:8), SegmentedControl (21:9), SelectionBox (22:12), DatePicker (24:2), TimePicker (25:17) |
| `💬 Feedback` (15:5) | Alert (26:2), Snackbar (26:10), AccentTip (27:2), InfoTip (27:6), Skeleton (27:10), Badge (28:5), Tag (28:16) |
| `🧭 Surfaces` (15:6) | TopAppBar (29:9), Tab (29:16), BottomSheet (30:2), Accordion (31:16), Carousel (31:17) |
| `📐 Foundations` (15:2) | Color / Typography / Spacing&Radius specimen boards |

## Naming convention (Figma ↔ socarframe token)

- A socarframe token `a-b-c` is the Figma variable **`a/b/c`** (slash groups), e.g.
  `status-positive-regular` → variable `status/positive/regular`.
- Each variable's **WEB code syntax** is the canonical token: `var(--status-positive-regular)`.
- Text styles are named by the exact token (`title2`, `heading2`, …).
- Components are named by the socarframe component; variants use `Prop=Value` (e.g.
  `Style=Fill, Variant=Primary`).

## Font (important)

Built in **Noto Sans KR** — the only Korean UI font installed on this machine. Noto Sans KR has
**no SemiBold (600)**, so the `title*` / `caption1` / `caption3` styles (spec: SemiBold) currently
use **Medium (500)**. Bold(700) and Regular(400) roles map exactly.

To upgrade fidelity: install **Pretendard** (has 600), then re-point the 16 text styles to
Pretendard with the spec weights — a one-shot change (set `fontName` on each text style; everything
using the styles updates automatically). See `docs/socarframe/typography.md`.

## How the harness uses it

Once present in the file, `socar-context` will find these via `get_libraries` /
`search_design_system` / local variables, and `socar-implement` should:
1. **Bind colors/spacing/radius to the variables** (by the names above) instead of pasting hex/px.
2. **Instance the components** (TopAppBar, ActionButton, …) instead of hand-building lookalikes.
3. Apply the **text styles** by token name.

## Publishing

Publishing shares these assets with *other* files — **not required** for designs built in this file.
It is a manual Figma UI action (no API/MCP):

1. Move the file into a **Team project** if it's in your Drafts (libraries publish only from team files).
2. Open the **Assets** panel → **book icon (Libraries)** → find this file → **Publish**.
3. Choose the components/variables/styles to publish → **Publish**.
4. In any other file, **enable** this library from the same Libraries dialog.

Your plan (`pro/Full`) supports team-library publishing.

## Rebuild / extend

The build is deterministic and resumable. State ledger: `/tmp/dsb-state-dsb-socarframe-20260620.json`
(collection/page/component node IDs). To extend, load the `figma-generate-library` + `figma-use`
skills, read the ledger, and add components in dependency order (variables already exist).
