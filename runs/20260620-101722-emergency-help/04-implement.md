---
run: 20260620-101722-emergency-help
stage: implement
status: built
figma_frame: "[auto] 사고·고장 신고(긴급 도움) — 20260620-101722-emergency-help"
figma_node_id: 34:60
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-60
revision: 0
---
# Implement log

## Built
- Frame: `[auto] 사고·고장 신고(긴급 도움) — 20260620-101722-emergency-help` (node `34:60`) — 360 x 1166
  - Vertical auto-layout, page background `background-regular`, `clipsContent=true`.
  - Placed on Page 1 (`0:1`) at **x=15000, y=0** (session-reserved lane; existing frame `3:2` sits at x=200–560 — no overlap).
- Link: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-60

## Build approach
- **socarframe is not a bound Figma *library***, but the target file already contains local variable
  collections that mirror socarframe tokens 1:1 — `Color` (40 semantic tokens, e.g. `text/strong`,
  `status/negative/regular`, `status/caution/weak`), `Spacing` (20), `Radius` (10), `Primitives` (123).
  **I reused and bound to those existing variables** rather than creating a duplicate `socarframe`
  collection — this keeps the design token-driven and traceable, and `get_variable_defs(34:60)` returns
  a full, non-empty token map (see below). No new variable collection was created.
- All socarframe components were **hand-built from primitives by value** (no socarframe instances exist
  in the file), with every fill/stroke bound to a color variable, spacing/padding/gap bound to spacing
  variables, and corner radii bound to radius variables. Layer names carry role + variant + token
  brackets per `docs/figma-conventions.md` §3 so the build is auditable.
- Icons imported as SVG vectors (`createNodeFromSvg`) and recolored by binding stroke/fill to the
  relevant color variable (chevron, phone fill/line, warning triangle, horn, question, car, arrow-left).

## Section log (in plan order)
1. **TopAppBar** (node `34:61`) — custom, height 56, transparent over page bg, left back `IconButton 뒤로가기` (48×48 touch target, `[aria-label=뒤로가기]`) with `icon-arrow-left-line` chevron bound to `text-strong`. Side padding `spacing-200`.
2. **Hero** (node `34:65`) — custom text block. Title 「도움이 필요하신가요?」 `heading2` / `text-strong`; subtitle 「당황하지 않으셔도 돼요. 바로 도와드릴게요.」 `body2` / `text-secondary`; title↔sub gap `spacing-150`, padding `spacing-400`.
3. **긴급 액션 Card** (node `34:134`) — custom surface, `[fill=status-negative-weak radius=radius-300]`, inner pad `spacing-400`, row gap `spacing-300`.
   - Header: label 「사고가 났거나 차가 멈췄나요?」 `title2` / `status-negative-strong`; desc 「24시간 긴급출동과 고객센터가 바로 도와드려요.」 `body3` / `text-secondary`.
   - 3a **Primary CTA** (node `34:138`) — `ActionButton · fill/negative/large` `[fill=status-negative-regular radius=radius-350]`, full-width, h 52, white `title2` label 「긴급출동 전화하기」 + `icon-phone-fill` (white).
   - 3b **Secondary** (node `34:142`) — `ActionButton · outlined/negative/large` `[stroke=status-negative-regular radius=radius-350]`, white bg, `status-negative-strong` label 「고객센터 전화하기」 + `icon-phone-line`.
4. **주의 안내 Tips** (node `34:213`) — `Tips · caution/static` `[fill=status-caution-weak radius=radius-300]`, pad `spacing-300`, `icon-exclamation-triangle-fill` (caution-regular) + body 「안전한 곳으로 이동한 뒤 신고해 주세요. 2차 사고를 막는 것이 가장 먼저예요.」 `body3` / `text-primary`, icon↔text gap `spacing-150`.
5. **상황 선택 헤더** (in section `34:344`) — 「어떤 상황인가요?」 `title2` / `text-strong`, gap to list `spacing-200`.
6. **SelectionBoxGroup · single** (node `34:346`) — 3 card rows, white bg, `[stroke=border-regular radius=radius-300]`, inner pad `spacing-400`, row gap `spacing-200`; each = circular 40px icon backdrop (`radius-circle`) + label (`title3`/`text-strong`) + desc (`body4`/`text-tertiary`) + `icon-chevron-right-line` (text-tertiary).
   - 6a 사고: `icon-exclamation-triangle-fill`, backdrop `status-negative-weak`, icon `status-negative-regular` — 「사고가 났어요」 / 「접촉·추돌 등 사고 접수」.
   - 6b 고장: `icon-horn-fill`, backdrop `status-caution-weak`, icon `status-caution-regular` — 「차가 고장 났어요」 / 「시동·타이어·배터리 등」.
   - 6c 기타: `icon-question-circle-line`, backdrop `background-regular`, icon `text-secondary` — 「그 외 문의가 있어요」 / 「이용·결제 등 일반 문의」.
7. **현재 이용 차량 Card** (node `34:528`) — custom, white `[radius=radius-300 stroke=border-regular]`, pad `spacing-400`. Header 「현재 이용 중인 차량」 `title3` + **Tag 「이용 중」** `caption1` (`status-information-weak` bg / `status-information-regular` text — see deviation). Body: `icon-car-fill` thumbnail (`background-regular`/`radius-200`) + 「아반떼 CN7」 `title3`, 차량번호 「12가 3456」, `Divider [stroke=divider-regular]`, meta 「6월 20일 09:00 ~ 18:00 이용 중」 `caption1` / `text-tertiary`.
8. **FAQ** (section `34:644`) — header 「자주 묻는 질문」 `title3`; white list card `[radius=radius-300 stroke=border-regular]` with 2 rows (`body2` / `text-primary` + chevron, `Divider` between) — 「사고가 나면 보험 처리는 어떻게 되나요?」 / 「긴급출동 비용은 누가 부담하나요?」; `TextButton · text/primary` 「전체 도움말 보기」 `title3` / `primary-regular` + chevron. Bottom safe padding `spacing-800`.

## Tokens applied
- **Color** (all bound to local `Color` variables — confirmed via `get_variable_defs`): `text-strong`,
  `text-primary`, `text-secondary`, `text-tertiary`, `status-negative-weak/regular/strong`,
  `status-caution-weak/regular`, `status-information-weak/regular`, `background-regular`,
  `border-regular`, `divider-regular`, `primary-regular`, plus white for fill-button label / card surfaces.
- **Type** (Gothic A1, see Font): `heading2`(24/34 Bold), `title2`(16/24 SemiBold), `title3`(14/22 SemiBold),
  `body2`(16/24 Regular), `body3`(14/22 Regular), `body4`(13/20 Regular), `caption1`(12/18 SemiBold).
  Exact px / line-height per `typography.md`. SemiBold(600) preserved everywhere — never dropped to Medium.
- **Spacing/Radius** (bound to local `Spacing`/`Radius` variables): padding/gaps `spacing-100/150/200/300/400/800`;
  radii `radius-300`(cards/Tips/SelectionBox, 12px), `radius-350`(large buttons, 14px), `radius-200`(thumbnail, 8px),
  `radius-circle`(icon backdrops + Tag).

## Font
- **Gothic A1** used as the Pretendard substitute. **Pretendard is NOT installed** in this environment
  (`listAvailableFontsAsync` returned no Pretendard styles). Per `typography.md`, the substitute must have
  the full weight set so SemiBold(600) is never dropped to Medium(500): Gothic A1 ships
  Regular(400) / Medium(500) / **SemiBold(600)** / Bold(700), so the 400 / 600 / 700 hierarchy is preserved.
  (Noto Sans KR was rejected — it lacks SemiBold.) Substitution recorded here for verify.

## Deviations from plan (with reason)
- **Frame height 880 → 1166.** Plan specced 360×880 "스크롤 전제" (scroll assumed). Actual content stacks
  to 1166px. Rather than clip the FAQ section out of view at 880, the frame height was set to HUG the full
  content (1166px) so the whole screen is visible for review/verify — i.e. the design canvas shows the full
  scrollable surface. Width unchanged (360). Layout/spacing/order otherwise exactly per plan.
- **「이용 중」 Tag color: plan didn't fix a color** (called it just "이용중 Tag (caption1)"; context pack
  suggested `accent-*`/`text`). Initially built with `status-negative-weak` (red), which read like an alert.
  Recolored to **`status-information`** (calm blue) so red stays reserved for the emergency area — directly
  honors the plan's "status 색 절제 / One primary action" intent. Caption1 type unchanged.

## Known issues / TODO
- socarframe components are hand-built primitives (no bound socarframe instances exist in the file), as the
  context pack established; intent is preserved via bound local variables + token-bracketed layer names.
- Vehicle data (아반떼 CN7 / 12가 3456 / time) and FAQ rows are dummy copy per plan (실데이터 연동 out of scope).
- Custom `status-negative` *fill* ActionButton is an intentional domain variant (socarframe's standard
  ActionButton fill set is primary/secondary/tertiary only) — flagged in context as deliberate, not a defect.
