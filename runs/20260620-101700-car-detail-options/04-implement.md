---
run: 20260620-101700-car-detail-options
stage: implement
status: built
figma_frame: "[auto] 차량 상세 & 옵션 선택 — 20260620-101700-car-detail-options"
figma_node_id: 34:85
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-85
revision: 0
---
# Implement log

## Built
- Frame: `[auto] 차량 상세 & 옵션 선택 — 20260620-101700-car-detail-options` (node `34:85`) — **360 × 1182**
- Placement: Page 1 (`0:1`), **x=6000, y=0** (reserved lane). No overlap — the only other top-level frame
  (`[auto] 반납 완료`, `3:2`) ends at x=560. Single state → no `· <state>` suffix, no Section wrapper.
- Link: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-85

## Structure
Wrapper is vertical auto-layout, fill `background-regular`, holding 3 stacked children:
`Carousel (custom)` (full-bleed 360×240) → `Content Column` (gutter 16, gap 12) → `Bottom CTA Bar (custom)`.
The "sticky" bottom bar is represented as the last full-width child (with a top divider); a
`spacer · spacing-1000` closes the scroll content so the bar reads as a separated fixed region.

## Section log (in plan order)
1. **이미지 캐러셀** (`Carousel (custom)`, node `34:146`) — full-bleed 360×240 image placeholder
   `[fill=image-placeholder gray]`, top `[fill=black-gradient]` scrim, dot row (5 dots, idx 1 active,
   gap `spacing-100`), page pill `1 / 5` `[fill=black/40 radius=radius-circle]` `caption2 white`.
2. **TopAppBar** (overlay, node `34:149`) — transparent, 56px, left `IconButton 뒤로가기` (`icon-chevron-left-line`),
   trailing slot `공유하기`(`icon-share-line`) + `찜하기`(`icon-heart-line`), all white glyphs; 44×44 touch targets,
   `[aria-label=…]` on each. Icons imported as SVG vectors (no DS icon components in file).
3. **차량 정보** (`차량 정보 Card (custom)`, node `34:377`) — white `radius-300`, padding `spacing-400`:
   모델명 `heading2 text-strong` "아반떼 CN7"; 번호판·연식 `body3 text-secondary`; 연료/인승 `Tag · soft/small/capsule`
   ×2 (`[fill=status-information-weak]`, label `caption1 status-information-strong`, leading icon); 쏘카존 위치 행
   (`icon-location-dot-line [fill=location-rental]` + `body3 text-secondary`).
4. **보험 선택** (`SelectionBoxGroup · single [차량손해면책]`, node `34:501`) — group label `title2 text-strong`;
   3 boxes gap `spacing-150`:
   - 표준 (`34:504`) `SelectionBox · default` `[border=border-regular radius=radius-300]`, label `title3 text-primary`,
     "자기부담금 50만원" `body3 text-secondary`, "기본 포함" `title3 text-primary`.
   - **안심 (`34:510`) `SelectionBox · selected/checked`** — `[border=primary-regular]` 2px + `[fill=status-information-weak]`,
     label `title3 text-strong`, "추천" Tag, "자기부담금 30만원", "+5,500원" `title3 text-strong`, `icon-check-circle-fill [fill=primary-regular]`.
   - 완전 (`34:521`) `SelectionBox · default`, "자기부담금 0원", "+9,900원" `text-strong`.
5. **추가 옵션** (`추가 옵션 Card (CheckboxGroup)`, node `34:740`) — white `radius-300`; label `title2 text-strong`;
   2 `Checkbox · default(unchecked)` rows (`[border=border-regular radius=radius-100]`): "하이패스" + "통행료 자동 결제"
   `caption1 text-secondary` + "+1,100원" `title3 text-strong`; "충전 케이블" + "차량 내 비치" + "무료".
6. **요금 안내** (`요금 안내 Card (custom)`, node `34:799`) — title `title2 text-strong` + `icon-info-circle-line [fill=text-tertiary]`;
   대여요금 (3시간) — 33,000원; 차량손해면책 (안심) — +5,500원; `Divider [stroke=divider-regular]`; **예상 요금 — 38,500원**
   (label `title3 text-strong` / value `title2 text-strong`); caption `caption1 text-tertiary` "주행거리 요금은 반납 후 정산돼요."
7. **하단 바 여백** — `spacer · spacing-1000` (`34:879`).
8. **하단 고정 액션 바** (`Bottom CTA Bar (custom)`, node `34:880`) — white, top `Divider [stroke=divider-regular]`,
   inner padding `spacing-300`/`spacing-400`: left `총 예상 요금 스택` (label `caption1 text-secondary` / amount `heading3 text-strong`
   "38,500원"); right `ActionButton · fill/primary/large [예약하기]` (`34:886`) `[fill=primary-regular radius=radius-350]`,
   `title2` white, 56px, fills remaining width.

## Tokens applied
- **Bound to existing file variable collections** (`Color`/`Spacing`/`Radius` — already present in the file from the
  반납 완료 run; reused rather than duplicating a new `socarframe` collection). `get_variable_defs` on the frame resolves:
  - Color: `primary-regular` #0078FF, `status-information-weak` #EBF5FF, `status-information-strong` #0069FF,
    `text-strong` #141A24, `text-primary` #354153, `text-secondary` #697383, `text-tertiary` #99A1B1,
    `background-regular` #F2F3F8, `border-regular` / `divider-regular` #E5E8EF. (`location-rental` bound on the pin too.)
  - Type: heading2 (24/34 Bold), heading3 (22/30 Bold), title2 (16/24 SemiBold), title3 (14/22 SemiBold),
    body3 (14/22 Regular), caption1 (12/18 SemiBold), caption2 (12/18 Medium) — applied as exact px/line-height,
    type token recorded in every text-node name.
  - Spacing: `spacing-25/100/150/200/300/400/1000` (bound to itemSpacing/padding). Radius: `radius-100/300/350/circle` (bound).

## Deviations from plan (with reason)
- **Font = `IBM Plex Sans KR`** (Regular 400 / Medium 500 / **SemiBold 600** / Bold 700), NOT Pretendard.
  Pretendard is not installed in this environment, and the genuine SOCAR font is not installed either. Among installed
  Korean UI sans families, only `IBM Plex Sans KR` and `Gothic A1` carry a **true SemiBold (600)**. Per the build-font
  policy ("never silently drop SemiBold to Medium"), I chose IBM Plex Sans KR so the 400/500/600/700 contrast is preserved
  faithfully. Note: the prior 반납 완료 frame used Noto Sans KR, which has **no** SemiBold — so matching it would have violated
  the weight policy; IBM Plex Sans KR is the policy-correct choice here.
- **Carousel image is a neutral-gray placeholder** with a "차량 이미지" label (plan explicitly allows placeholder; the
  use_figma API cannot fetch external photos and no image existed in-file to reuse).
- **Reused the file's existing `Color`/`Spacing`/`Radius` variable collections** instead of creating a fresh `socarframe`
  collection (context pack assumed "no variables", but the file already had them bound to socarframe token names). This is
  strictly better — avoids duplicate collections and keeps the new screen consistent with the 반납 완료 reference. Variable
  *names* use `text/strong` etc. (the file's existing grouping); `get_variable_defs` resolves them to the socarframe tokens.
- **"추천" Tag** rendered as a solid info-blue pill with white text (rather than weak-fill) so it stays legible on top of
  the already light-blue (`status-information-weak`) selected 안심 box. Same information/blue trust family as planned.
- **Card-over-carousel -16px overlap** (plan 3, the rounded card pulling up over the photo) was **not** applied — auto-layout
  doesn't support negative margins, and forcing absolute positioning would make the scroll column fragile. Cards sit directly
  below the carousel instead. Purely cosmetic; structure & spacing otherwise match.

## Known issues / TODO
- The bottom bar is built as the last stacked child (static representation of a sticky bar) — correct for a static mock,
  but it is not a true viewport-pinned sticky element (out of scope: no interaction/scroll behavior).
- Tag/checkbox/SelectionBox/ActionButton are hand-built from primitives + bound tokens (no socarframe component library is
  subscribed in this file), named by socarframe component + variant so the intent is traceable.
