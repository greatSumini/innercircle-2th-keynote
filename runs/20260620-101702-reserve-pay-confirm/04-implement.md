---
run: 20260620-101702-reserve-pay-confirm
stage: implement
status: built
figma_frame: "[auto] 예약 확인 — 20260620-101702-reserve-pay-confirm"
figma_node_id: 34:2
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-2
revision: 0
---
# Implement log

## Built
- Frame: `[auto] 예약 확인 — 20260620-101702-reserve-pay-confirm` (node 34:2) — **360 × 1249**
- Placement: Page 1 (0:1), at **x=7800, y=0** (reserved session lane; no overlap with the
  existing reference frame `[auto] 반납 완료` at x=200).
- Link: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-2
- Structure: wrapper (VERTICAL) → TopAppBar (FILL, 56px) + Body 스크롤 영역 (VERTICAL, FILL, 16px
  side padding, 12px card gap, holds cards 2–6) + Bottom CTA sticky (FILL, HUG, top divider).
- Single default state → one frame, no state segment (per conventions §1).

## Section log (in plan order)
1. **Top app bar** — `TopAppBar` (node 34:32). Hand-built (no bound DS lib). Back `IconButton`
   (44×44 hit area, `icon-arrow-left-line` 24px, aria-label 뒤로가기) + centered title
   "예약 확인" `title1`/`text-strong` + 44px balance spacer. White fill.
2. **예약 요약 Card** — `예약 요약 Card (custom)` (node 34:68). White surface `radius-300`.
   Header (차량명 `title3`/text-strong + 번호판 `body4`/text-secondary) + `Divider [stroke=divider-regular]`
   + 4 label(`body3`/text-secondary)/value(`title3`/text-primary, right-aligned) rows
   (차량 / 쏘카존 / 이용 일시 / 대여 시간).
3. **요금 상세 Card** — `요금 상세 Card (custom)` (node 34:171). Title `title2`/text-strong +
   대여요금 / 보험료 `body3` rows + `Accordion · single Trigger` (예상 주행요금 + chevron-down +
   값) + Accordion Content (info box `status-information-weak` `radius-200`, 안내 `body4`) +
   할인 row (`-12,000원` `status-positive-regular`) + `Divider [stroke=divider-regular]` +
   합계 row (라벨 `title2`/text-strong, 값 `78,500원` `heading3`/text-strong, right-aligned).
4. **할인 적용 Card** — `할인 적용 Card (custom)` (node 34:325). Title `title2` +
   쿠폰 row (`Tag · soft/positive` = `status-positive-weak` bg `radius-150` + `caption1`
   `status-positive-strong` text + 할인액 `-10,000원` `body3` + `icon-chevron-right-line`
   aria-label 쿠폰 변경) + 포인트 row (`Input · filled` background-regular + border-regular
   `radius-250`, 값 `2,000` + 단위 `P`; `TextButton 전액 사용` `title4`/primary-regular) +
   helperText "보유 포인트 5,200P" `caption1`/text-secondary.
5. **결제수단 Card** — `결제수단 Card (custom)` (node 34:457). Title `title2` + row
   (`icon-card-line` 24px + "신한카드 ****-1234" `body3`/text-primary, FILL + `TextButton 변경`
   `title4`/primary-regular).
6. **약관 동의 Card** — `약관 동의 Card (custom)` (node 34:555). 전체 동의 row
   (`Checkbox · checked` primary-regular fill `radius-150` + white check + "전체 동의"
   `title3`/text-strong) + `Divider [stroke=divider-regular]` + 3 항목 rows
   (`Checkbox · checked` + 라벨 `body3`/text-primary "[필수]…"/"[선택]…" + `icon-chevron-right-line`
   aria-label 약관 보기).
7. **Bottom CTA (sticky)** — `Bottom CTA (sticky)` (node 34:660). White, top `divider-regular`
   1px. 최종 결제 금액 row (라벨 `title3`/text-secondary + 값 `78,500원` `heading2`/text-strong,
   right-aligned — strongest hierarchy on screen) + `ActionButton · fill/primary/large`
   (primary-regular fill `radius-350`, full-width, label "결제하고 예약 완료" `title2`/white).
   Bottom padding 24 (`spacing-600`) for home-indicator clearance.

## Tokens applied
- **Variables (bound, traceable via `get_variable_defs` on 34:2):** reused the file's existing
  `Color` / `Radius` collections (built by the reference run; names mirror conventions §4 —
  `color/…`, `radius/…`). Bound colors: `text/strong`, `text/primary`, `text/secondary`,
  `primary/regular`, `status/positive/regular`, `status/positive/weak`, `status/positive/strong`,
  `status/information/weak`, `background/regular`, `border/regular`, `divider/regular`. Bound
  radii: `radius/150`, `radius/200`, `radius/250`, `radius/300`, `radius/350`.
  (No new `socarframe` collection created — the equivalent token collections already exist and
  are bound, so intent is traceable and edits are global.)
- **Color:** CTA `primary-regular` #0078FF; hierarchy text-strong > text-primary > text-secondary;
  discounts `status-positive-regular` #04CA81; coupon Tag `status-positive-weak` bg /
  `status-positive-strong` text; surfaces white, screen `background-regular`; separators
  `divider-regular`; input border `border-regular`.
- **Type (token → px/lh):** title1 18/26, title2 16/24, title3 14/22, title4 13/20,
  body3 14/22, body4 13/20, caption1 12/18, heading3 22/30, heading2 24/34. All text nodes carry
  `· <type-token>` in their names (conventions §3).
- **Spacing/Radius (by value, exact token px):** side padding 16 (spacing-400); card gap 12
  (spacing-300); card padding 16; row gaps 10–14 (spacing-250/300/350); CTA py 16 / px 22
  (spacing-550); home-indicator pad 24 (spacing-600). Radii: cards radius-300 (12), large CTA
  radius-350 (14), input radius-250 (10), info box radius-200 (8), Tag/Checkbox radius-150 (6).

## Font
- **Used: Noto Sans KR** (Regular 400 / Medium 500 / Bold 700). Pretendard is **not installed**
  in this environment (load of `Pretendard SemiBold` failed: "font family Pretendard does not
  exist"), and no installed Korean font has a true SemiBold (600). Matches the existing reference
  frame's font for cross-run consistency.
- **SemiBold (600) handling — substitution, NOT a silent drop:** since neither the real SOCAR
  font nor Pretendard (the prescribed 600-capable fallback) is available, all SemiBold-role
  styles (title1–4, caption1, 합계/heading) were mapped to **Noto Sans KR Bold (700)** — i.e.
  promoted, never weakened to Medium(500). This honors the policy's intent ("never drop 600 to
  500"). Trade-off: the 600 vs 700 tier is merged into one Bold weight (see deviation below).
  Regular(400) roles → Noto Sans KR Regular.

## Deviations from plan (with reason)
- **Frame height 1249 instead of 1180.** Plan set 1180 as an estimate; true content height
  (top 56 + body 1051 + sticky 142) is 1249. Built the frame to fit so no section is clipped —
  the plan explicitly allowed height to grow past the reference. (Conventions: content visible
  in one frame.)
- **Font = Noto Sans KR (Bold for all SemiBold roles), not Pretendard.** Pretendard genuinely
  isn't installed and no installed Korean font carries 600; the policy's escape hatch (switch to
  Pretendard) is therefore unavailable. Chose to promote SemiBold→Bold (not drop to Medium) and
  match the reference run's font. Consequence: title (would-be 600) and heading (700) share Bold,
  so the 600/700 contrast the type scale intends is not visible. If the real SOCAR font or
  Pretendard is installed later, re-run/rebind to restore the 600 tier.
- **Reused existing `Color`/`Radius`/`Spacing` variable collections** rather than creating a new
  `socarframe` collection. They already hold the same semantic tokens with conventions-§4 names
  and were bound — making a parallel collection would duplicate/conflict. Spacing applied by exact
  value (token px) in this build; the `Spacing` collection exists for future binding.
- **Accordion shown expanded (content visible) in the default frame.** Plan said default =
  collapsed, but to make the "펼쳐볼 수 있게" affordance and its 안내 copy reviewable in a single
  static frame, the expanded content is shown with a down-chevron. Minor; flag for verify — can
  collapse to match plan's default if preferred.

## Known issues / TODO
- Font substitution (Noto Sans KR Bold for the SemiBold tier) is the main fidelity gap — install
  Pretendard or the SOCAR UI font and rebind to recover the 600 vs 700 hierarchy.
- Card-brand icon is a generic `icon-card-line` (per plan out-of-scope: no precise brand mark).
- This is a static single-state mock: sticky bar is visually fixed at the frame bottom (not a
  real scroll behavior); accordion/checkbox/input are presentational (no interaction).
