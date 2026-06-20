# Figma naming & organization conventions

How the harness **names and arranges** what it builds in Figma — frames, sections, layers,
component instances, icons, spacers, and the local variable collection. This is the build-side
companion to `docs/socarframe/` (which says *what tokens/components to use*); this doc says *how to
label and lay them out* so a screen is readable on the canvas, auditable by the verify stage, and
easy to clean up.

Read by **plan** (names sections/states with this vocabulary), **implement** (applies it when
creating nodes), and **verify** (audits against it). When this doc and an agent file disagree, this
doc wins for naming/organization; `docs/socarframe/` wins for token/component values.

## Why naming matters here

socarframe is **not a bound Figma library** in the target file, so tokens are applied as values and
intent survives only through **layer names**. Verify reads `get_metadata` and must be able to tell,
from names alone, which socarframe component/token each node represents. Good names are not cosmetic
— they are how the design stays traceable without bound variables.

## Principles

1. **Traceable** — a layer's name says its role and the socarframe token/component it stands for.
2. **Consistent** — same role → same name across runs; the format below is fixed.
3. **Greppable & disposable** — every harness-built top node carries the `[auto]` prefix and the
   `<run-id>`, so generated work is easy to find, match to a run, and remove.
4. **Plan-ordered** — layer order top-to-bottom mirrors the plan's layout table order.

---

## 1. Frame names

Every screen frame the harness builds:

```
[auto] <screen> — <run-id>
```

- `[auto]` — fixed prefix marking a harness-generated frame (never hand-built design).
- `<screen>` — the screen name in Korean, as in the plan title (e.g. `반납 완료`, `쿠폰함`).
- ` — ` — an em dash (` — `, space-emdash-space) before the run id.
- `<run-id>` — the run directory id, e.g. `20260620-070646-return-complete`.

Example: `[auto] 반납 완료 — 20260620-070646-return-complete`

### Multiple states → multiple frames

When the plan calls for more than one state (default + empty/loading/error/success…), build **one
frame per state** and insert the state segment with a middle dot ` · `:

```
[auto] <screen> · <state> — <run-id>
```

- Use the state segment **only when there are 2+ frames**. A single-state screen omits it.
- When 2+ frames exist, label every frame — including the main one as ` · 기본`.
- State vocabulary (Korean, match the plan's `## States`): `기본`, `빈 상태`, `로딩`, `에러`,
  `성공`, `선택됨`, `잠김`, `열림`, … Use the plan's exact state word.

Examples (a two-state 쿠폰함 run):
`[auto] 쿠폰함 · 기본 — <run-id>` · `[auto] 쿠폰함 · 빈 상태 — <run-id>`

---

## 2. Canvas organization & placement

- **Stay on the active page.** Don't create new pages unless the request asks for it.
- **Never overlap.** Call `get_metadata` first, find empty canvas space, and place there.
- **One run = one row.** Lay a run's frames left → right in a single row, **default/primary
  leftmost**, then empty/loading/error…, with a consistent **80px gutter** between frames and a
  shared top edge (same `y`).
- **Wrap a multi-frame run in a Figma Section** named exactly like the frame stem:
  `[auto] <screen> — <run-id>` (no state segment). This keeps the run tidy and movable as a unit.
  If a Section can't be created, fall back to the row layout above — don't block on it.
- Record the placement (page, x/y, section) in `04-implement.md`.

---

## 3. Layer (node) names

Format, in priority order of what's present:

```
<Role or ComponentName> · <variant> [<token=value …> | <aria-label=…>]
```

- **Role / ComponentName** — human-readable. socarframe component → its real name (`TopAppBar`,
  `ActionButton`, `Chip`). Section/container → its job (`Hero`, `이용 요약 Card`, `Bottom CTA`).
  Korean role labels are fine.
- **` · <variant>`** — for component instances, append the variant/size:
  `ActionButton · fill/primary/large`, `Tab · slide/large`, `Badge · dot/small`.
- **`[ … ]` token bracket** — when a token is applied **by value** (no bound variable), encode it so
  verify can audit it. Keep it short; multiple keys space-separated:
  `[fill=primary-regular]`, `[radius=radius-300]`, `[fill=status-positive-weak radius=radius-circle]`.
- **`[aria-label=…]`** — required on every icon-only interactive (its accessible name):
  `IconButton 닫기 [aria-label=닫기]`.

### Specific node types

| Node | Name it | Example |
|------|---------|---------|
| Screen section / container | role | `TopAppBar`, `Hero`, `결제 요약 Card`, `Bottom CTA` |
| socarframe component instance | component `· variant` | `ActionButton · fill/primary/large` |
| Hand-built gap (no DS component) | role + `(custom)` | `SummaryCard (custom)`, `Card (custom)` |
| Text node | `<role> · <type-token>` | `Hero title · heading2`, `총 결제금액 value · heading3` |
| Icon | the socarframe icon token | `icon-close-line`, `icon-check-circle-fill` |
| Icon-only button | `IconButton <role> [aria-label=…]` | `IconButton 닫기 [aria-label=닫기]` |
| Spacer frame | `spacer · <spacing-token>` | `spacer · spacing-150` |
| Divider | `Divider [stroke=<token>]` | `Divider [stroke=divider-regular]` |

- **Text nodes always carry their type token** (`· body2`, `· title2`) — this is how verify checks
  typography without reading every font property.
- Don't leave default names (`Frame 12`, `Rectangle 3`, `Text`). An unnamed node is a verify finding.

---

## 4. Local variable collection

When socarframe isn't a bound library (the usual case), implement materializes a local collection so
intent is traceable via `get_variable_defs` and edits are global.

- **Collection name:** `socarframe` — single default mode (add `light`/`dark` modes only if the
  request needs theming).
- **Variable names mirror the token names**, grouped with `/` so Figma nests them:
  - Color → `color/<semantic-token>` — e.g. `color/primary-regular`, `color/text-strong`,
    `color/status-positive-regular`.
  - Radius → `radius/<token>` — e.g. `radius/radius-300`.
  - Spacing → `spacing/<token>` — e.g. `spacing/spacing-400`.
- **Bind** fills/strokes (and radius/spacing where practical) to these variables instead of pasting
  raw hex/px. At minimum create + bind the **color** variables the screen uses.
- The bracket token notation in layer names (§3) stays even when bound — it's cheap redundancy that
  keeps names self-describing.

### Text styles (optional)

If you create text styles, name them exactly by type token — `heading2`, `title2`, `body2`,
`caption1` — mirroring `docs/socarframe/typography.md`. Otherwise rely on the `· <type-token>`
suffix in text-node names.

---

## 5. Revise mode

When implement applies a verify fix list, **edit the existing frame in place** — keep the same frame
name, node id, section, and placement. Don't append `(v2)` or rebuild beside the original. The
`revision` counter in `04-implement.md` records the pass; the canvas stays stable.

---

## Cheat sheet

| Thing | Convention |
|-------|-----------|
| Screen frame | `[auto] <screen> — <run-id>` |
| State frame (2+ states) | `[auto] <screen> · <state> — <run-id>` |
| Run section wrapper | `[auto] <screen> — <run-id>` |
| Placement | active page, empty space, one row L→R, 80px gutter, default leftmost |
| Section/container layer | role: `TopAppBar`, `Hero`, `… Card`, `Bottom CTA` |
| Component instance | `ComponentName · variant` (e.g. `ActionButton · fill/primary/large`) |
| Custom (gap) | `<role> (custom)` |
| Text | `<role> · <type-token>` |
| Icon / icon button | `icon-<name>-<fill\|line>` / `IconButton <role> [aria-label=…]` |
| Spacer / divider | `spacer · <spacing-token>` / `Divider [stroke=<token>]` |
| Applied-by-value token | bracket: `[fill=<token>]`, `[radius=<token>]` |
| Variable collection | `socarframe`; vars `color/… radius/… spacing/…` |
| Revise | edit in place; same name/id; bump `revision` |
