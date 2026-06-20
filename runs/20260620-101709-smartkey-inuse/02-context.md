---
run: 20260620-101709-smartkey-inuse
stage: context
status: ready
figma_library_available: no
---
# Context pack

Screen: **'이용 중(스마트키)'** — full-screen 차량 제어/시간 관리 화면. Two state frames: 기본 **'잠김'** + **'열림'**.
socarframe is **not** a bound Figma library here → apply all tokens **by value** and encode intent in
layer names per `docs/figma-conventions.md`. Match the visual language of the one existing harness
screen (반납 완료) — 360px frame, `background-regular` page, white cards `radius-300`, label/value rows,
sticky bottom CTA region (primary ActionButton + tertiary TextButton).

## Design-system references
- Docs to follow:
  - `docs/socarframe/components-surfaces.md` → **TopAppBar** (general title + LeftSideIconSlot back).
  - `docs/socarframe/components-actions.md` → **ActionButton** (size/variant table), **IconButton**
    (large/xLarge for the big door/lights/horn controls), **TextButton** (help entry points), Haptic.
  - `docs/socarframe/components-feedback.md` → **Tips/InfoTip** (안내 Tips), **Tag** (잠금 상태 라벨), **Badge** (dot, optional).
  - `docs/socarframe/color.md` → semantic color tokens (lock-state, status, text, surface).
  - `docs/socarframe/typography.md` → type scale (남은 시간 크게 = display/heading).
  - `docs/socarframe/spacing.md` → spacing + radius scale.
  - `docs/socarframe/icons.md` → lock / horn / warning-light icon names.
  - `docs/socarframe/principles.md` → Safety & Context priority (lock-state visibility, large targets).
- Key tokens for this screen:
  - **Color**
    - Surface/bg: `background-regular` (#F2F3F8) page, white (`#FFFFFF`) cards.
    - Borders/dividers: `border-regular`, `divider-regular`.
    - Text: `text-strong` (남은 시간/제목 강조), `text-primary` (본문 값), `text-secondary` (라벨/안내),
      `text-tertiary` (캡션/저강조), `text-disabled`.
    - Primary CTA: `primary-regular` (#0078FF); pressed/active step `primary-strong` / `primary-heavy`.
    - **Lock-state (3중 표현: 색+아이콘+라벨)** —
      - 잠김(안정): neutral/secondary — `status-information-weak`/`status-information-regular` 또는 중립 그레이
        계열 + `icon-lock-fill` + "잠김".
      - 열림(주의 환기): `status-caution-weak` (#FFF8E6) 배경 / `status-caution-regular` (#FF8800) 강조
        + `icon-lock-open-fill` + "열림". (negative 아님 — 경고가 아니라 주의 환기.)
    - 비상등/경적 보조 컨트롤: 중립 surface (`background-regular` 또는 white + `border-regular`),
      아이콘 `text-primary`; 활성화 시 `status-caution-*`(비상등) 가능.
    - Tips 안내: `status-information-weak` 배경 + `status-information-regular`/`text-secondary` 텍스트 (Info 톤).
    - 도움(신고/고객센터) 진입: 저강조 `text-secondary`/`text-tertiary`.
  - **Type**
    - 남은 이용 시간(크게): `display2` (36px) 또는 `heading1` (26px) — 화면 최대 강조 1곳.
    - 차량 모델명: `title1`/`title2`; 번호판·반납 예정 시각: `body2`/`body3` + `text-secondary`.
    - 컨트롤 버튼 라벨: `title2`(large) / `title3`; 보조 컨트롤 캡션: `caption1`/`caption2`.
    - Tips 본문: `body3`/`body4`; 도움 링크: `body3`/`title4`.
    - 잠금 상태 Tag 라벨: `caption1`/`title4`.
  - **Spacing/radius**
    - 화면 좌우 패딩: `spacing-400` (16px). 섹션 간격: `spacing-400`/`spacing-500`. 그룹 내부: `spacing-200`/`spacing-300`.
    - 카드/컨트롤 surface radius: `radius-300` (12px), 큰 컨트롤 타일은 `radius-400` (16px) 가능.
    - 큰 IconButton 컨트롤 터치 타깃: 64px+ 권장, 충분한 내부 패딩 `spacing-400`+.
    - ActionButton large: padding `py-400`/`px-550`, radius `radius-350` (14px).

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | general title + LeftSideIconSlot(back) | 화면 헤더 (제목 "이용 중", 뒤로/닫기) | components-surfaces.md | not in library — build from primitives (ref frame 3:3) |
| ActionButton | fill/primary/large | 하단 단일 primary CTA — **반납하기** | components-actions.md | not in library — build from primitives (ref frame 6:35) |
| ActionButton | fill/secondary or outlined/secondary, large | 보조 액션 — **이용 시간 연장** | components-actions.md | not in library — build from primitives |
| IconButton | large / xLarge | 핵심 컨트롤 — **문 열기/잠그기**(primary 토글), **비상등**, **경적(차 찾기)** | components-actions.md | not in library — build from primitives |
| TextButton | text/tertiary or secondary, small/medium | 도움 진입 — **사고·고장 신고**, **고객센터** | components-actions.md | not in library (ref frame 6:37) |
| Tag | capsule, small/medium, color-customized | 잠금 상태 라벨 "잠김"/"열림" (색+텍스트) | components-feedback.md | not in library — build from primitives |
| InfoTip / Tips (Info) | inline, status-information tone | 보조 안내 Tips ("탑승 전 차량 외관을 확인해 주세요") | components-feedback.md | not in library — build from primitives |
| Icons (from SOCAR Icon Library) | 24/fill | `icon-lock-fill`, `icon-lock-open-fill`, `icon-warning-light-fill` (비상등), `icon-horn-fill` (경적/차 찾기), `icon-car-search-fill` (차 찾기 대안), `icon-info-circle-line` (Tips), `icon-exclamation-triangle-fill`/`icon-message-question-line` (신고/고객센터), `icon-phone-fill` (고객센터), `icon-chevron-left-line` (back) | 핵심 컨트롤·상태·안내 아이콘 | icons.md | names verified in icons.md list; draw as vectors (no bound lib) |

Notes on the control hierarchy (from clarify assumptions, to confirm in plan):
- **One primary per screen.** 문 열기/잠그기 = 가장 큰 primary 토글 컨트롤(상단 핵심 컨트롤 영역).
  비상등·경적은 그 아래 동급 보조 IconButton 2종.
- 하단 고정 영역 single primary CTA = **반납하기** (`ActionButton fill/primary/large`);
  **이용 시간 연장**은 그 위/옆 secondary(`fill/secondary` 또는 `outlined/secondary`).
- 잠금 상태는 색·아이콘·라벨 3중 표현. 열림 = `status-caution-*`(주의 환기) + `icon-lock-open-fill`.

## Figma library & reference status
- **Library available: no.** `get_libraries` on the target file lists only community kits
  (Material 3, Simple Design System, Apple iOS/iPadOS/watchOS/visionOS/macOS) — **socarframe is not
  added or available to add**. `search_design_system("ActionButton")` returned only unrelated
  components ("Awesome Design System / button", "LIBRARY / Button…") — **no socarframe component keys
  exist to bind.** Build everything from primitives and apply tokens by value; materialize a local
  `socarframe` variable collection (color/spacing/radius) per `figma-conventions.md` §4.
- **Existing frames / placement:**
  - One harness frame exists: `[auto] 반납 완료 — 20260620-070646-return-complete` (node 3:2) at
    x=200, y=0, 360×857 on Page 1 (0:1). **Use it as the style reference** — it establishes: 360px
    portrait frame, `background-regular` page, white cards `radius-300`, label/value summary rows,
    TopAppBar with icon button + `aria-label`, sticky **Bottom fixed CTA region** holding a full-width
    `ActionButton fill/primary/large` + a tertiary `TextButton` below it, and the exact layer-naming
    convention (e.g. `ActionButton (fill / primary / large) — 확인`, `icon-…-line (24, <token>)`).
  - **Placement for this run:** request assigns canvas lane **x=9600, y=0**, lay the two state frames
    left→right within the lane (잠김 leftmost, then 열림), 80px gutter, shared top y=0. This is far
    from the only existing frame (x=200) → **no overlap**. Wrap the two frames in a Figma Section
    named `[auto] 이용 중(스마트키) — 20260620-101709-smartkey-inuse` if creatable.
  - Frame name stems: `[auto] 이용 중(스마트키) · 잠김 — 20260620-101709-smartkey-inuse` and
    `[auto] 이용 중(스마트키) · 열림 — 20260620-101709-smartkey-inuse`.

## Gaps (needs custom build)
socarframe is not bound, so **every** component above is hand-built from primitives — but each maps to
a named socarframe component/token (reuse-by-name, not a true gap). The following are genuine design
gaps where socarframe provides **no dedicated component**, so implement must compose from primitives:
- **Big door-control toggle (잠김↔열림)** — no socarframe "lock toggle" / segmented vehicle-control
  component. Compose a custom large control tile (white/`status-*` surface, `radius-400`,
  `icon-lock-fill`/`icon-lock-open-fill` 56–64px, `title2` 라벨) acting as a primary IconButton.
  Lock state must read via **color + icon + text** simultaneously.
- **Vehicle-control button group (비상등 · 경적/차 찾기)** — no DS "control grid". Compose two equal
  large IconButton tiles in a row with caption labels under each icon.
- **차량 식별 + 남은 시간 hero block** — no DS "ride timer" component. Compose from text tokens
  (`display2`/`heading1` for the timer, `title1` model, `body3` plate + 반납 예정 시각) on a card.
- **사고·고장 신고 / 고객센터 도움 진입 row** — no DS "help row"; compose low-emphasis TextButtons /
  small IconButtons with leading icons (`icon-exclamation-triangle-fill`, `icon-phone-fill`/`icon-message-question-line`).
- **Status caution surface for 열림 state** — use `status-caution-weak/regular` tokens directly
  (no dedicated "open lock alert" component); not an Alert (요청은 강한 경고 아님, 주의 환기 수준).
- Note: a real "스마트키 BLE 연결중/실패" 전이 상태는 scope out (clarify) — Skeleton/Snackbar 미사용.
