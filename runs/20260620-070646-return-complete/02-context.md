---
run: 20260620-070646-return-complete
stage: context
status: ready
figma_library_available: no
---
# Context pack

## Design-system references
- Docs to follow:
  - `docs/socarframe/color.md` — semantic color tokens (text/primary/status/background/divider).
  - `docs/socarframe/typography.md` — type scale (heading/title/body/caption).
  - `docs/socarframe/spacing.md` — 4px-grid spacing tokens.
  - `docs/socarframe/icons.md` — SOCAR Icon Library names (close, check-circle).
  - `docs/socarframe/components-surfaces.md#topappbar` — TopAppBar anatomy (Left/Title/Trailing slots).
  - `docs/socarframe/components-actions.md` — ActionButton / IconButton / TextButton variants, sizes, type tokens.
  - `docs/socarframe/principles.md` — hierarchy / one-primary-CTA / predictability for emphasizing 총 결제금액.

- Key tokens for this screen (apply by exact value — see "library status" below):
  - **Color**
    - Success hero: `status-positive-regular` #04CA81 for the check icon; optional `status-positive-weak` #E6FEF0 as the icon's circular backdrop.
    - Title text: `text-strong` #141A24 ("반납이 완료되었어요"); hero sub-line + card label rows: `text-secondary` #697383.
    - Card values / item names: `text-primary` #354153; total-amount value emphasized in `text-strong` #141A24 (or `primary-regular` #0078FF if a stronger color accent is wanted — keep one choice, hierarchy via size+weight is enough).
    - Primary CTA '확인': `primary-regular` #0078FF fill, white label.
    - Secondary action '이용 내역 보기' (TextButton): `text-secondary` #697383 (tertiary variant) — must stay visually subordinate to the primary CTA.
    - Surfaces: screen background `background-regular` #F2F3F8; cards on `white` #FFFFFF.
    - Separators: row/section dividers `divider-regular` #E5E8EF; the line above 총 결제금액 uses `divider-regular`.
  - **Type**
    - Hero title: `heading2` (24/34, Bold) — primary screen title. (`heading1` if a larger hero is preferred.)
    - Hero sub-line: `body2` (16/24) or `body3` (14/22).
    - Card section title (이용 요약 / 결제 요약): `title2` (16/24, SemiBold).
    - Card label rows (left labels): `body3` (14/22); row values: `body3` or `title3` for slight emphasis.
    - 총 결제금액 label: `title2`; total value: `heading3` (22/30, Bold) or `title1` — largest in the card to signal the total.
    - Primary CTA label: `title2` (matches ActionButton size=large).
    - Secondary TextButton label: `title3`/`title4` per chosen TextButton size.
  - **Spacing / radius**
    - Screen horizontal padding: `spacing-400` (16px).
    - Section gaps (hero ↔ card ↔ card): `spacing-300`/`spacing-400` (12–16px).
    - Card inner padding: `spacing-400` (16px); label↔value row gaps `spacing-200`/`spacing-300` (8–12px); tight icon↔text `spacing-100`/`spacing-200`.
    - Hero vertical breathing room above title: `spacing-600`/`spacing-800`.
    - Bottom CTA region: inner padding `spacing-400`; gap between CTA and TextButton `spacing-200`.
    - Card radius: ActionButton large = `radius-350`; cards have no explicit token in docs — use a rounded container consistent with surfaces (treat as gap; see Gaps).

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | general title, Trailing slot only (no Left back) | screen header / chrome | components-surfaces.md#topappbar | not in file — build from primitives |
| IconButton | size `medium`, icon `icon-close-line` | trailing close (X) in TopAppBar.TrailingButtonSlot | components-actions.md#iconbutton + icons.md | not in file |
| ActionButton | `fill` / `primary` / `large` (title2, py-400 px-550, radius-350) | primary CTA '확인' | components-actions.md#actionbutton | not in file |
| TextButton | `text` / `tertiary` (or secondary) / `medium` | secondary action '이용 내역 보기' | components-actions.md#textbutton | not in file |
| Icon: `icon-check-circle-fill` | filled, `status-positive-regular` | success hero check | icons.md | not in file (vector) |
| Icon: `icon-close-line` | line | close (X) inside IconButton | icons.md | not in file (vector) |

> No socarframe component keys were returned by the MCP — none can be inserted as library instances. Build each as a token-styled frame/group per the docs.

## Figma library & reference status
- **Library available: no.** `get_libraries` on `VuBHVaAnA5ORacxMZ9zcH8` lists only community kits
  (Material 3 Design Kit, Simple Design System, iOS 18 / iOS&iPadOS 26, watchOS 26, visionOS 26, macOS 26).
  socarframe is **not** subscribed and **not** in libraries_available_to_add.
- `search_design_system` for socarframe components (ActionButton/TopAppBar) and tokens
  (primary-regular/text-secondary/spacing-400/heading2) returned **no socarframe matches** —
  only unrelated generic assets ("LIBRARY" Button/checkbox/TextArea, "Awesome Design System" icon).
  No socarframe **variables or styles** exist in the file (variables/styles arrays empty).
- **Implication for implement:** there are no bound socarframe Figma variables to reference, so the
  implement stage must apply tokens by their **exact values from `docs/socarframe/`** (hex from color.md,
  px/weight from typography.md, px from spacing.md) and name the token in layer names/comments so verify
  can trace intent. Consider creating local variables/styles mirroring the needed tokens for cleanliness,
  but raw values from the docs are the source of truth.
- **Existing frames / placement:** the file has one page (`0:1` "Page 1") that is **empty** — no existing
  frames. Place the new screen as a fresh mobile-portrait frame on Page 1 at the canvas origin. There is
  **no existing SOCAR screen to match**; follow the docs as the single style reference.

## Gaps (needs custom build)
- **Whole screen is custom-built from primitives** — socarframe is not a usable Figma library here,
  so every component below is hand-assembled with token values, not inserted as an instance:
  - **TopAppBar** (general title bar + TrailingButtonSlot with a close IconButton). No back button.
  - **IconButton** (close X) — frame with `icon-close-line` vector + touch padding.
  - **Success hero** — `icon-check-circle-fill` in `status-positive-regular`, optional positive-weak
    circular backdrop, `heading2` title, `body2/body3` sub-line. (Hero block itself is a layout, not a
    socarframe component.)
  - **이용 요약 card** and **결제 요약 card** — socarframe has **no dedicated Card/SummaryCard component**
    in the docs; build as a `white` rounded container (label–value rows) using spacing/divider tokens.
    Card corner radius is not specified by a socarframe token — pick a consistent rounded radius
    (suggest ~`radius-300`/12px equivalent) and flag for verify.
  - **결제 요약 total row** — `divider-regular` line above, then 총 결제금액 emphasized via `heading3`/
    `title1` + `text-strong`. Custom emphasis pattern (no component).
  - **ActionButton / TextButton** — built as token-styled frames (fill/primary/large; text/tertiary).
  - **Bottom fixed CTA region** — a sticky bottom container is a layout pattern, not a socarframe
    component; build with `white` bg, top `divider-weak/regular` if needed, `spacing-400` padding.
  - **Icons** are vectors to draw/import from the SOCAR Icon Library names (no Figma instances available).
- No socarframe BottomSheet/Tab/Accordion/Snackbar/Alert needed — this is a static success screen.
