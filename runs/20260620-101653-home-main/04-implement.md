---
run: 20260620-101653-home-main
stage: implement
status: built
figma_frame: "[auto] 홈(메인) · 예약 있음 — 20260620-101653-home-main / [auto] 홈(메인) · 예약 없음 — 20260620-101653-home-main"
figma_node_id: 34:44 (예약 있음), 34:926 (예약 없음), section 34:43
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-43
revision: 0
---
# Implement log

## Built
- Page: `Page 1` (`0:1`) — same page as the `[auto] 반납 완료` reference frame (style reference).
- Section wrapper: `[auto] 홈(메인) — 20260620-101653-home-main` (node `34:43`) at x=2360, y=-40, 880×880.
- Frame A: `[auto] 홈(메인) · 예약 있음 — 20260620-101653-home-main` (node `34:44`) — 360×800, at x=2400, y=0 (default, leftmost).
- Frame B: `[auto] 홈(메인) · 예약 없음 — 20260620-101653-home-main` (node `34:926`) — 360×800, at x=2840, y=0 (80px gutter).
- Reserved-lane placement honored (x=2400 lane); no overlap with reference frame (x=200–560).
- Link (Frame A): https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-44
- Link (Frame B): https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-926

## Font (build-font policy)
- Real SOCAR UI font: not installed. **Pretendard: not installed** in this file's font set.
- **Used `Gothic A1`** — a Korean UI sans that ships the full weight set incl. a true **SemiBold (600)**.
  Mapped: Bold(700)→Gothic A1 Bold, SemiBold(600)→Gothic A1 SemiBold, Medium(500)→Gothic A1 Medium,
  Regular(400)→Gothic A1 Regular.
- **Deliberate substitution / improvement over the reference frame:** the reference `반납 완료` frame used
  `Noto Sans KR`, which lacks 600 and therefore dropped SemiBold→Medium (the exact defect the policy warns
  against). Since Pretendard is unavailable, Gothic A1 was chosen specifically because it has 600 — so
  title*/caption1 render at true SemiBold and the 600 vs 700 vs 400 hierarchy is preserved. No weight was
  silently dropped.

## Tokens materialized as variables
- The file already has bound local collections `Color` (40 semantic vars: `text/*`, `primary/*`,
  `status/*`, `background/*`, `border/*`, `divider/*`, `notification/red`, `location/*`…), `Spacing` (20),
  `Radius` (10). **Reused these existing collections** instead of creating a new `socarframe` collection
  (the context pack assumed zero variables; the file actually has them). All fills/strokes are bound to
  `Color` vars; all padding/itemSpacing to `Spacing` vars; all corner radii to `Radius` vars.
- `get_variable_defs(34:44)` returns the bound set (sample): `text-strong`, `text-primary`, `text-secondary`,
  `text-tertiary`, `primary-regular`, `notification-red`, `location-rental`, `status-positive-weak`,
  `status-positive-strong`, `status-information-weak`, `background-regular`, `border-regular`,
  `divider-regular`, `spacing-50/100/150/200/300/400/450/600`, `radius-200/250/300/400/circle`.

## Section log (in plan order)
1. **StatusBar (시각용)** — custom 44px decorative bar (time + status glyphs), transparent over screen bg. Nodes `34:119` (A) / `34:927` (B).
2. **TopAppBar (general)** — white 56px; LeftSlot = `icon-location-dot-fill` [location-rental] + "서울 강남구 역삼동" (title3 / text-strong) + `icon-chevron-down-line`; TrailingButtonSlot = `IconButton 알림` 44×44 [aria-label=알림] with `icon-bell-line` [text-primary] + **dot Badge** [notification-red] (A only). Nodes `34:122` (A) / `34:930` (B).
3. **Search Hero (검색 진입 박스, custom)** — white surface, radius-300, border-regular 1px, py spacing-450 / px spacing-400, gap spacing-200; `icon-search-line` [primary-regular] + "어디서 탈까요?" (body1 / text-secondary) + `icon-chevron-right-line` [text-tertiary]. Nodes `34:218` (A) / `34:942` (B).
4. **Section 3 — 예약 있음:** 진행 중 예약 카드 (custom) — header "이용 중인 차" (title3 / text-strong); white card radius-300 pad spacing-400; thumbnail 64×48 radius-200 + `icon-car-line`; text column: `Tag · capsule/small` [status-positive-weak / status-positive-strong] "이용 중", model "아반떼 CN7" (title2 / text-strong), "오늘 14:00 – 18:00" (body3 / text-secondary); 쏘카존 row with `icon-location-dot-fill` [location-rental] + "강남 더클래스효성 쏘카존" (body3); `Divider [stroke=divider-regular]`; CTA row: `ActionButton · outlined/primary/small` "예약 상세" + `ActionButton · fill/primary/small` "스마트키" (radius-250). Nodes `34:583` / card `34:585`.
   **Section 3 — 예약 없음:** 예약 유도 카드 (custom, empty-state) — centered: `status-information-weak` 56 circle tile + `icon-car-search-line` [primary-regular]; "첫 차를 예약해 볼까요?" (title2 / text-strong); "가까운 쏘카존에서 1분 만에 시작할 수 있어요." (body3 / text-secondary); `ActionButton · fill/primary/medium` "주변 차량 찾기" full-width (radius-300). Node `34:1124`.
5. **혜택 배너 carousel (custom)** — slide `status-information-weak` radius-400 pad spacing-400, 96 tall: title (title2 / text-strong) "신규 가입하면 / 첫 대여 30% 할인" + sub (body3 / text-secondary) + `icon-gift-line` illustration on tinted circle; dots row: active [primary-regular] 16×6 pill + 2× inactive [border-regular] circles. Nodes `34:764` (A) / `34:971` (B).
6. **퀵메뉴 그리드 (custom)** — 4-up SPACE_BETWEEN: 쏘카플랜 (`icon-calendar-check-line`) · 부름·편도 (`icon-car-line`) · 쿠폰함 (`icon-coupon-line`) · 이벤트 (`icon-couponset-line`); each = 48 circle tile [status-information-weak / radius-circle, primary-regular icon] + label (caption1 / text-primary), gap spacing-150. Nodes `34:776` (A) / `34:983` (B).
7. **BottomNavigation (고정, custom)** — white 84px, top `Divider [stroke=divider-regular]`; 4 tabs 56×44: 홈 active (`icon-home-fill` filled [primary-regular] + caption3 [primary-regular]); 탐색 (`icon-search-line`), 이용내역 (`icon-clock-line`), 마이 (`icon-user-line`) all inactive [text-tertiary]. Nodes `34:844` (A) / `34:1006` (B).

## Tokens applied
- Color: `text-strong / text-primary / text-secondary / text-tertiary`, `primary-regular`, `status-positive-weak / status-positive-strong`, `status-information-weak`, `background-regular`, `border-regular`, `divider-regular`, `notification-red`, `location-rental` — all bound to the file's `Color` variable collection.
- Type (Gothic A1): `title3`(14/SemiBold) addresses & section headers, `title2`(16/SemiBold) model name & banner & empty-state title, `body1`(18/Reg) search placeholder, `body3`(14/Reg) time/zone/banner-sub, `caption1`(12/SemiBold) tag & quick-menu labels, `title4`(13/SemiBold) card CTA labels, `caption3`(10/SemiBold) bottom-nav labels, `caption1`(12/SemiBold) status-bar time.
- Spacing/Radius: side insets `spacing-400`; section gaps `spacing-600`; card pad `spacing-400`; tight groups `spacing-100/150/200/300`; surfaces `radius-300`, banner `radius-400`, thumbnail `radius-200`, small buttons `radius-250`, medium button `radius-300`, circles `radius-circle` — all bound to `Spacing`/`Radius` collections.

## Deviations from plan (with reason)
- **Font is Gothic A1, not Pretendard** — Pretendard is not installed in this file. Gothic A1 chosen because it
  has a true SemiBold(600), satisfying the policy's hard rule (never drop 600→500). Logged above.
- **Reused existing `Color`/`Spacing`/`Radius` variable collections** instead of creating a new `socarframe`
  collection — context pack said the file had no variables, but it does. Reusing them is strictly better:
  bindings are global, `get_variable_defs` is rich, and token names already mirror socarframe (`primary/regular`,
  `spacing/400`, etc.). Layer-name token brackets retained as redundant traceability per conventions §3/§4.
- **`break-keep` not bindable via plugin API** — Figma's plugin API exposes no `word-break: keep-all` property,
  so the banner title uses a manual newline at a natural word boundary ("신규 가입하면\n첫 대여 30% 할인") to
  keep "할인" intact, achieving the plan's break-keep intent. Other multi-line text (empty-state sub) is short
  enough to wrap without mid-word breaks at 296px.
- StatusBar status glyphs are simple text placeholders (decorative only, not accessibility targets) — matches the plan's "시각 요소만, 콘텐츠 없음".

## Known issues / TODO
- Vehicle thumbnail and banner illustration are placeholders (icon on tinted surface) — no real product imagery
  available to the plugin API (cannot fetch external URLs). Plan allowed this ("이미지 없으면 background-regular 채움 + icon-car").
- Icons are hand-authored SVGs imported as vectors (socarframe Icon Library not present as Figma components),
  named with their socarframe icon tokens for traceability.
- none blocking.
