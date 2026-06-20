---
run: 20260620-101700-car-detail-options
stage: context
status: ready
figma_library_available: no
---
# Context pack

Screen: 차량 상세 & 옵션 선택 — scrollable full-screen (mobile portrait), single default state with
insurance "안심" pre-selected. socarframe is NOT a bound Figma library in the target file, so every
token/component below is applied **by value** and traced through layer names per
`docs/figma-conventions.md`. There is one prior harness screen in the file
(`[auto] 반납 완료 — 20260620-070646-return-complete`, 360px wide) whose style this screen should match.

## Design-system references
- Docs to follow:
  - `components-surfaces.md` → **TopAppBar** (Left/Trailing slots), **Pattern / Carousel** (image carousel + dot nav).
  - `components-forms.md` → **SelectionBox / SelectionBoxGroup** (single-select insurance), **Checkbox / CheckboxGroup** (options).
  - `components-actions.md` → **ActionButton** (primary CTA), **IconButton** (back/share/heart), **TextButton** (optional "자세히").
  - `components-feedback.md` → **Tag** (insurance "추천" badge on 안심; fuel/seat info tags).
  - `color.md`, `typography.md`, `spacing.md`, `icons.md` → tokens below.
  - `principles.md` → one primary action, trustworthy/easy-to-choose tone.
- Key tokens for this screen:
  - **Color:**
    - CTA / selected emphasis: `primary-regular` (#0078FF). Selected SelectionBox border/accent = `primary-regular`; its weak fill (if used) = `status-information-weak` (#EBF5FF, same blue-50 family).
    - Text hierarchy: `text-strong` (model name, total fare amount, selected labels), `text-primary` (values/body), `text-secondary` (labels, sub-info, plate·year), `text-tertiary` (carousel dot inactive / least-important meta).
    - Surfaces: page `background-regular` (#F2F3F8); cards/section surfaces white (#FFFFFF). Separators `divider-regular`; control borders `border-regular` (unselected SelectionBox), selected = `primary-regular`.
    - Status/recommend accent: `status-information-*` (blue) for the "추천" emphasis on 안심; reserve `status-positive-*` only if a "포함" success cue is needed. Fare amounts are emphasis via `text-strong`, not a status color.
    - Carousel overlay icons (back/share/heart sit over photo): use white icon glyphs over a subtle scrim; record as `[fill=white]` since there is no semantic "on-image" token.
  - **Type:**
    - Vehicle model name (screen-level title): `heading2` (24/34, Bold). Plate·year sub-line: `body3`/`caption1`.
    - Section titles (보험 선택 / 추가 옵션 / 요금 안내): `title2` (16, SemiBold) — matches the 반납 완료 card titles.
    - SelectionBox option label (표준/안심/완전): `title3` or `title2`; deductible/extra-fee detail: `body3`/`caption1` `text-secondary`; price `+N,000원` emphasis: `title3`/`text-strong`.
    - Body / fare rows: `body3` label + `body3`/`title3` value (mirror 반납 완료 결제 요약 rows).
    - Bottom bar total fare amount: `heading3` (22, Bold) `text-strong`; its "총 예상 요금" label: `caption1`/`body3` `text-secondary`.
    - CTA "예약하기": `title2` (the `large` ActionButton type token), white.
    - Tags / dot caption: `caption1`/`caption2`.
  - **Spacing/radius:**
    - Screen horizontal padding `spacing-400` (16px) — same gutter as 반납 완료 (x=16, 328px content).
    - Section gap `spacing-400`/`spacing-300`; intra-group gaps `spacing-150`/`spacing-200`; tight label/value `spacing-100`.
    - Cards / SelectionBox / section surfaces: `radius-300` (12px). CTA (large): `radius-350` (14px). Tags/pills: `radius-circle` or `radius-200`.
    - Carousel: full-bleed (edge-to-edge, no side padding); dot indicator gap `spacing-100`.
    - Bottom bar inner padding ≈ `spacing-300`/`spacing-400`; CTA height ~56px (matches 반납 완료 ActionButton).

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | general; `LeftSideIconSlot` + `TrailingButtonSlot` (≤3) | screen header, overlaid on carousel | components-surfaces.md | not in library — build by value |
| TopAppBar.BasicBackButton / IconButton | medium, `icon-arrow-left-line` (or `icon-chevron-left-line`) | back, left slot | components-surfaces.md / components-actions.md | not in library |
| IconButton | medium, `icon-share-line` | share, right slot | components-actions.md | not in library |
| IconButton | medium, `icon-heart-line` | favorite (찜), right slot | components-actions.md | not in library |
| Pattern (Carousel) | `type="carousel"`, drag + dot nav, index 1/N active | vehicle image carousel (static repr.) | components-surfaces.md | not in library — placeholder image + dots |
| Tag | small/medium, `capsule`, neutral/soft | 연료·인승 tags (e.g. 휘발유 / 5인승); optional 쏘카존 pin | components-feedback.md | not in library |
| SelectionBoxGroup | `selectionType="single"`, label="차량손해면책" | insurance 3-step group; 안심 = selected | components-forms.md | not in library |
| SelectionBox | single; default ×2, **selected/checked** ×1 (안심) | 표준 / 안심 / 완전 cards w/ 자기부담금 + 추가요금 | components-forms.md | not in library |
| Tag | small, soft, `status-information` | "추천" badge inside 안심 SelectionBox | components-feedback.md | not in library |
| CheckboxGroup | default unchecked | 추가 옵션 group (하이패스 / 충전) | components-forms.md | not in library |
| Checkbox | default (unchecked) | 하이패스, 충전 each on/off | components-forms.md | not in library |
| ActionButton | **fill / primary / large** (`title2`, `radius-350`, ~56px) | bottom-bar "예약하기" primary CTA | components-actions.md | not in library |
| TextButton | text / tertiary or secondary, small/medium | optional "보험 자세히 보기" / "요금 상세" link | components-actions.md | not in library |
| Divider | `divider-regular`, 1px | fare-row → total separator (as in 반납 완료) | color.md | not in library |

Icons needed (from `icons.md`, all confirmed present): `icon-arrow-left-line` / `icon-chevron-left-line`,
`icon-share-line`, `icon-heart-line`, `icon-location-dot-line` (쏘카존 location pin),
`icon-gas-station-line` / `icon-charging-line` (fuel · EV), `icon-users-line` (인승),
`icon-check-line` / `icon-check-circle-fill` (SelectionBox/Checkbox selected mark),
`icon-info-circle-line` (요금/보험 info), `icon-chevron-right-line` (detail affordance).

## Figma library & reference status
- **Library available: no.** `get_libraries` returns only community/org UI kits (Material 3, Simple Design
  System, iOS/iPadOS/watchOS/visionOS/macOS Apple kits) — **socarframe is not subscribed**.
  `search_design_system` for `SelectionBox`, `ActionButton TopAppBar`, etc. returns only unrelated
  generic components (a `LIBRARY` button/checkbox, IONIcon) — **no socarframe components or variables and
  no usable component keys**. So implement must build every component from primitives + bind a local
  `socarframe` variable collection (per figma-conventions.md §4) and trace tokens via layer names.
- **Existing frames / placement:**
  - One prior harness screen: `[auto] 반납 완료 — 20260620-070646-return-complete` (id `3:2`) at x=200, y=0,
    **360×857**. Same Page 1 (`0:1`). This is the **style reference**: 360px frame on `background-regular`,
    white cards at `radius-300`, `heading2` title, `title2` card titles, `body3` label / `title3`-`body3`
    value rows, `divider-regular` before the emphasized total, full-width `ActionButton fill/primary/large`
    + sticky bottom region. Match these exactly; only the new sections (carousel, vehicle info, insurance
    SelectionBox group, option checkboxes, fare preview) are net-new.
  - **Placement for the new frame:** this session's reserved lane is **x=6000, y=0** — well clear of the
    only existing frame (ends at x=560), so no overlap. Place the single state frame there on Page 1.
    Frame name: `[auto] 차량 상세 & 옵션 선택 — 20260620-101700-car-detail-options` (single state → no `· <state>`
    segment, no Section wrapper needed). Suggested frame width 360 to match the reference; height per content.

## Gaps (needs custom build)
- **Everything is "custom" in the literal sense** (no bound library) — but the following map cleanly to
  socarframe specs and are reused-by-name, not invented: TopAppBar, Carousel, SelectionBox(Group),
  Checkbox(Group), ActionButton, Tag, IconButton, Divider.
- **True gaps (no dedicated socarframe component — assemble from primitives + tokens):**
  - **Image carousel with dot indicator** — socarframe Carousel is a behavioral *pattern* (CarouselEngine),
    not a static Figma component. Build a full-bleed image placeholder + a row of dot glyphs (active =
    `primary-regular` or `text-strong`, inactive = `text-tertiary`/border) as a `(custom)` node; static
    representation only (no swipe logic).
  - **Vehicle info block** (model name + plate·year + fuel/seat Tags + 쏘카존 one-liner with location icon) —
    a `(custom)` composition; Tags reuse the Tag component, location uses `icon-location-dot-line` +
    `text-secondary`. No single DS "vehicle header" component exists.
  - **Insurance SelectionBox rich content** — SelectionBox supports rich children, but the internal layout
    (label + 자기부담금 line + 추가요금 +N,000원 + "추천" Tag) is composed by hand inside each box; verify the
    selected (안심) box uses `primary-regular` border/accent + check mark.
  - **요금 안내 / 예상 요금 preview card** — reuse the 반납 완료 "결제 요약" card pattern (label/value rows +
    `divider-regular` + emphasized total) as a `(custom)` card; no DS "fare summary" component, but the
    pattern is already proven in this file.
  - **Bottom fixed bar with total-fare + CTA side by side** — a `(custom)` sticky region: left = total
    예상 요금 (label `caption1`/`body3` `text-secondary` + amount `heading3` `text-strong`), right =
    `ActionButton fill/primary/large` "예약하기". The 반납 완료 bottom region is full-width CTA only, so the
    two-column layout is net-new here.
  - **Local `socarframe` variable collection** must be (re)materialized/bound by implement — color vars at
    minimum (`color/primary-regular`, `color/text-strong|primary|secondary|tertiary`,
    `color/background-regular`, `color/border-regular`, `color/divider-regular`,
    `color/status-information-weak`), plus `radius/*` and `spacing/*` where practical.
