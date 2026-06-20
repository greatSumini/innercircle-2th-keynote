---
run: 20260620-101653-home-main
stage: context
status: ready
figma_library_available: no
---
# Context pack

Home(메인) screen — app-entry full screen (mobile portrait, 360px wide to match the existing
`[auto] 반납 완료` reference frame). Two states: (A) 예약 있음, (B) 예약 없음(첫 화면). socarframe is
**not** a bound Figma library in the target file, so every token/component is applied **by value**
and traced through layer names per `docs/figma-conventions.md`. Reuse socarframe components by name;
build only the true gaps (see below) from primitives.

## Design-system references
- Docs to follow:
  - `principles.md` — one primary action per screen; 예약(검색) is THE primary CTA, everything else supports it.
  - `color.md` — semantic tokens only (Text / Primary / Status / Background-Border-Divider / Notification / Location).
  - `typography.md` — type scale + **Pretendard** build-font policy (never drop SemiBold 600 → Medium 500).
  - `spacing.md` — 4px-grid spacing tokens + radius scale (match px to token name).
  - `components-surfaces.md` — TopAppBar (상단 바), Pattern/Carousel (혜택 배너), Tab (BottomNavigation는 별도 글로벌 탭 — DS에는 없음, gap 참고).
  - `components-actions.md` — ActionButton (예약 카드 CTA), IconButton (알림), TextButton (보조 링크).
  - `components-forms.md` — Input (검색 박스 anatomy 참고 — 단, 비입력 진입형이므로 응용).
  - `components-feedback.md` — Badge (알림 dot badge), Tag (예약 카드 상태 라벨 "이용 중"/"예정").
  - `icons.md` — icon tokens (`icon-bell-line`, `icon-search-line`, `icon-chevron-down-line`, mobility/coupon icons for 퀵메뉴).

- Key tokens for this screen:
  - **Color:**
    - CTA / brand emphasis: `primary-regular` (#0078FF) — 예약 카드 스마트키 CTA, 검색 박스 강조, carousel active dot, BottomNav active.
    - Text hierarchy: `text-strong` (주소·예약 모델명·큰 제목), `text-primary` (값/본문), `text-secondary` (검색 플레이스홀더·이용시간·라벨), `text-tertiary` (보조/비활성 탭 라벨).
    - Surfaces: `background-regular` (#F2F3F8, 스크린 배경), white(#FFFFFF) surface for cards / search box / quick-menu (matches reference frame).
    - Separators: `divider-regular` / `border-regular` (#E5E8EF) for card/section dividers, search-box border if outlined.
    - Notification dot: `notification-red` (#FF3A5B) — 미읽음 알림 dot badge.
    - Reservation status: `status-positive-*` (이용 중 / 진행 중 — green) or `status-information-*` (예정 — blue). `status-information-weak` (#EBF5FF) as a soft card accent.
    - Location: `location-rental` (#0078FF) for 쏘카존 pin if shown.
    - Carousel inactive dots: `gray-300`/`text-disabled` tone (via border-regular) vs `primary-regular` active.
  - **Type:**
    - 위치 주소 (TopAppBar): `title2` (16) or `title3` (14) SemiBold + `icon-chevron-down`.
    - 검색 박스 플레이스홀더 "어디서 탈까요?": `body1` (18) / `body2` (16) `text-secondary`.
    - 예약 카드 모델명: `title2` (16) `text-strong`; 이용 시간·쏘카존: `body3` (14) `text-secondary`; 상태 Tag 텍스트: `caption1` (12 SemiBold).
    - 예약 카드 CTA(스마트키/예약 상세): `title4` (13) — ActionButton small label.
    - 배너 타이틀: `title2`/`title1`; 서브: `body3`/`caption2`.
    - 섹션 헤더(예: "이런 혜택은 어때요?"): `title1` (18) or `heading3` (22) — keep below the search hero in weight.
    - 퀵메뉴 라벨: `caption1` (12 SemiBold) or `body4` (13) `text-primary`.
    - BottomNav 라벨: `caption3` (10) or `caption2` (12).
  - **Spacing / radius:**
    - 스크린 좌우 패딩 `spacing-400` (16px) — matches reference frame's 16px card insets.
    - 섹션 간 간격 `spacing-500`/`spacing-600` (20–24px); 카드 내부 패딩 `spacing-400` (16px); 타이트 그룹 `spacing-100`/`spacing-200`.
    - 퀵메뉴 아이콘↔라벨 `spacing-100`/`spacing-150`; 그리드 컬럼 gap `spacing-200`/`spacing-300`.
    - 카드 / 검색 박스 / 배너 surface radius `radius-300` (12px); 큰 배너 `radius-400` (16px) optional. Carousel dots `radius-circle`.
    - ActionButton radius by size: small → `radius-250` (10px), medium → `radius-300`, large → `radius-350` (14px). 검색 박스(큰 진입형) `radius-300`/`radius-400`.

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | general; LeftSlot=위치 주소(text+`icon-location`/`icon-chevron-down`), TrailingButtonSlot=알림 IconButton | 상단 바 (① 위치 주소 + 알림) | components-surfaces.md | not found — build by value (matches reference frame's hand-built `TopAppBar (general …)`) |
| IconButton | medium, `icon-bell-line` (또는 `icon-bell-on-line`), aria-label=알림 | 알림 진입 버튼 | components-actions.md | not found — build by value |
| Badge | dot, small, `notification-red` | 미읽음 알림 dot (A 예약 있음 버전, optional B) | components-feedback.md | not found — build by value |
| Input (anatomy ref only) | filled, leading=`icon-search-line` | 큰 검색 박스 "어디서 탈까요?" — **비입력 진입형**으로 응용 (실입력 아님) | components-forms.md | not found — build as custom prominent surface |
| ActionButton | 스마트키: `fill/primary/small`(또는 medium); 예약 상세: `outlined/primary/small` or `fill/secondary/small` | ③ 예약 카드 CTA (카드당 1개) | components-actions.md | not found — build by value (reference frame has `ActionButton (fill / primary / large)`) |
| ActionButton | `fill/primary/large` | B(예약 없음) 검색/예약 유도 CTA (optional, 검색 박스 자체가 진입점이면 생략 가능) | components-actions.md | same |
| Tag | capsule, small/medium, `status-positive-*`(이용 중) / `status-information-*`(예정) | 예약 카드 상태 라벨 | components-feedback.md | not found — build by value |
| Pattern (Carousel) | type=carousel, 도트 인디케이터, 3장, active=`primary-regular` | ④ 혜택 배너 carousel | components-surfaces.md | not found — build static (current slide + dots) |
| TextButton | text/tertiary/small | 섹션 "전체보기" / 보조 링크 | components-actions.md | not found — build by value |
| Icons | `icon-bell-line`, `icon-search-line`, `icon-chevron-down-line`, `icon-location-dot-fill`, `icon-coupon-line`, `icon-car-line`, `icon-calendar-check-line`, `icon-home-fill`(BottomNav), `icon-couponset-line`, mobility set | 퀵메뉴·탭·상단·검색 | icons.md | from SOCAR Icon Library spec — drawn/placed by value |

Note: socarframe component **names are the source of truth** for layer naming, but no socarframe
Figma component keys exist in the file — implement builds each as named auto-layout frames with token
brackets, exactly as the `[auto] 반납 완료` reference frame already does.

## Figma library & reference status
- **Library available: no.** `get_libraries` returned only community kits (Material 3 Design Kit,
  Simple Design System, iOS/iPadOS/watchOS/visionOS/macOS) — **no socarframe library**.
  `search_design_system("TopAppBar ActionButton socarframe")` returned only an unrelated generic
  `Button/…/CTA` and a `toast` from an anonymous "LIBRARY" (not socarframe) and **zero variables/styles**.
  → Apply all tokens by value + materialize a local `socarframe` variable collection (per
  figma-conventions §4); bind at least the color variables this screen uses.
- **Existing frames / placement:**
  - Page 1 (`0:1`) has **one** prior harness frame: `[auto] 반납 완료 — 20260620-070646-return-complete`
    (node `3:2`) at **x=200, y=0, 360×857**. This is the **style reference to match**: 360px portrait,
    `background-regular` screen, white cards at `radius-300`, 16px (`spacing-400`) insets, TopAppBar +
    scroll body + bottom CTA structure, Pretendard-style bold Korean headings, `primary-regular` CTA,
    `title2`/`body3`/`heading3` type usage, semantic tokens baked into every layer name.
  - **Placement for THIS run:** reserved session lane is **x=2400, y=0** (clear of the 200–560 occupied
    range — no overlap). Lay the two state frames left→right in one row, **default(예약 있음) leftmost**
    then **예약 없음(첫 화면)**, 80px gutter, shared y=0. Wrap both in a Figma Section named
    `[auto] 홈(메인) — 20260620-101653-home-main`.
  - Frame names (figma-conventions §1, 2+ states ⇒ state segment on every frame):
    - `[auto] 홈(메인) · 예약 있음 — 20260620-101653-home-main`
    - `[auto] 홈(메인) · 예약 없음 — 20260620-101653-home-main`

## Gaps (needs custom build)
- **Search-entry box ("어디서 탈까요?")** — socarframe `Input` is a real text field; this is a large
  **non-input tap-to-navigate** prominent surface. Build custom: white surface, `radius-300`/`radius-400`,
  leading `icon-search-line`, `body1/body2 text-secondary` placeholder, subtle elevation/border for the
  "활기차고 깔끔" hero emphasis. Reuse Input's leading-icon anatomy as the visual model.
- **진행 중/예정 예약 카드** — no single socarframe "reservation card" component. Compose custom card
  (white surface `radius-300`) from primitives: 차량 썸네일(image/`icon-car`), 모델명(`title2`),
  이용 시간·쏘카존(`body3 text-secondary`), 상태 **Tag**(reuse), CTA **ActionButton small**(reuse).
- **혜택 배너 carousel** — socarframe `Pattern/Carousel` is a runtime engine, not a static Figma
  component. Build custom static carousel: one visible banner slide (`radius-300`/`radius-400`) +
  도트 인디케이터 row (active `primary-regular` / inactive `border-regular`); show 3 slides' worth in
  the spec, render current slide in the frame.
- **퀵메뉴 아이콘 그리드** — no DS grid component. Build custom 4-up (또는 +"전체") icon+label grid:
  circular/rounded icon tile (`background-regular` or `status-information-weak`, `radius-circle`/`radius-300`)
  + `caption1`/`body4` label. Icons from SOCAR Icon Library (쏘카플랜·부름/편도·쿠폰함·이벤트).
- **글로벌 BottomNavigation 탭바** — socarframe `Tab` is a content/anchor tab, **not** an app-level
  bottom nav bar. Build custom fixed bottom bar (홈 active=`primary-regular` `icon-home-fill`, others
  `text-tertiary` line icons, `caption3`/`caption2` labels). Confirm tab items in plan.
- **예약 없음(B) empty treatment** — no DS empty-state for home; handle by omitting the 예약 카드 and
  letting the 검색 박스 + 혜택 carousel carry the 예약 유도 (optional soft guidance copy), per clarify.
