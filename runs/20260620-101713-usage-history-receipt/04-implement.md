---
run: 20260620-101713-usage-history-receipt
stage: implement
status: built
figma_frame: "[auto] 이용 내역 — 20260620-101713-usage-history-receipt (section); 3 state frames"
figma_node_id: "34:1154 (section) · 34:106 (기본) · 34:441 (빈 상태) · 34:728 (영수증 상세)"
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-1154
revision: 0
---
# Implement log

## Built
- **Section:** `[auto] 이용 내역 — 20260620-101713-usage-history-receipt` (node `34:1154`),
  Page 1 (`0:1`), x=11360 y=−80, 1320×1100 — wraps the three state frames in one row, 80px gutter,
  shared top edge y=0. Existing `[auto] 반납 완료` (x=200) untouched, no overlap.
- **Frame 1 — 이용 내역 · 기본** (node `34:106`) — 360×630 — x=11400 y=0
  - Link: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-106
- **Frame 2 — 이용 내역 · 빈 상태** (node `34:441`) — 360×800 (fixed, content vertically centered) — x=11840 y=0
  - Link: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-441
- **Frame 3 — 이용 내역 · 영수증 상세** (node `34:728`) — 360×961 (height grows to content) — x=12280 y=0
  - Link: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-728

## Section log (in plan order)

### Frame 1 — 이용 내역 리스트 (기본) — node 34:106
1. TopAppBar (general 타이틀) — `34:107`; white surface, "이용 내역" `heading2`/`text-strong`, height 56, side pad `spacing-400`.
2. 안내 캡션 — text `34:109`; "최근 6개월 이용 내역이에요." `body3`/`text-secondary`, top pad `spacing-300`.
3. 월 섹션 헤더 ① — text `34:237`; "2026년 6월" `title3`/`text-secondary`, gaps `spacing-200`.
4. 이용 내역 Card ① (custom) — `34:239`; white `radius-300`, pad `spacing-400`, min-h 72, space-between row.
   모델 "아반떼 CN7" `title2`/`text-strong` · 일시·존 `body3`/`text-secondary` · 금액 "42,800원" `title2`/`text-strong` 우측 · `icon-chevron-right-line` `text-tertiary`.
5. 이용 내역 Card ② (custom) — `34:250`; "캐스퍼" + Tag「쏘카플랜」(soft/neutral capsule `gray-100`/`text-secondary`, plan's optional demo tag) · "28,500원".
6. 월 섹션 헤더 ② — text `34:263`; "2026년 5월", section gap `spacing-400`.
7. 이용 내역 Card ③ (custom) — `34:265`; "더 뉴 그랜저" · "98,000원".
8. 이용 내역 Card ④ (custom) — `34:276`; "레이" · "31,200원".
9. 리스트 하단 여백 — Content `paddingBottom` `spacing-800` (32px).
   Card 간 간격 `spacing-300` via spacer frames (named `spacer · spacing-300`).

### Frame 2 — 이용 내역 빈 상태 — node 34:441
1. TopAppBar — `34:442`; "이용 내역" `heading2`/`text-strong`.
2. Empty state region — `34:444` (FILL height) centers the block vertically + horizontally.
3. Empty state (custom) — `34:445`:
   - 아이콘 배지 — `34:446`; 80×80 circle `radius-circle`, `gray-200` fill (see deviation), `icon-file-text-line` 36 `text-tertiary` (`34:447`).
   - 타이틀 — `34:451`; "아직 이용 내역이 없어요" `title1`/`text-strong` 중앙, gap below `spacing-400`.
   - 설명 — `34:453`; "첫 쏘카를 이용하면 여기에서 영수증을 확인할 수 있어요." `body3`/`text-secondary` 중앙, side pad `spacing-700`, gap above `spacing-150`.
   - 1차 행동 버튼 — `34:455`; ActionButton fill/primary/large「차량 둘러보기」, `primary-regular` fill, `radius-350`, py `spacing-400` px `spacing-550`, label `title2` `white`, gap above `spacing-500`.

### Frame 3 — 영수증 상세 — node 34:728
1. TopAppBar (BasicBackButton + general 타이틀) — `34:729`; back IconButton 44pt `[aria-label=뒤로가기]` (`34:730`) with `icon-arrow-left-line` `text-strong`; 타이틀 "영수증" `heading2`/`text-strong`.
2. 이용 요약 Card (custom) — `34:818`; white `radius-300`, pad `spacing-400`, row gap `spacing-300`.
   타이틀 "이용 요약" `title2`/`text-strong`; 4 rows 라벨 `body3`/`text-secondary` + 값 `title3`/`text-primary` 우측 (차량/쏘카존/이용 일시/주행 거리).
3. 결제 영수증 Card (custom) — `34:888`; 타이틀 "결제 영수증" `title2`. Accordion `single` (`34:890`):
   - 3a 대여 요금 (value=rental, `[data-open]` 펼침) `34:891` — Trigger 라벨 `body3` + 금액 "33,000원" `title3`/`text-strong` 우측 + `icon-chevron-down-line [data-open]` (up). Content rows "기본 요금 (4시간 30분) 30,000원" · "심야 할증 3,000원" `body3`, 들여쓰기 `spacing-300`.
   - 3b 주행 요금 (driving, 접힘) `34:904` — "9,300원".
   - 3c 차량손해면책 (insurance, 접힘) `34:910` — "5,500원".
   - 3d 할인 (discount, 접힘) `34:916` — "−5,000원" `title3`/`status-positive-regular` (U+2212 마이너스).
   - 3e Divider `[stroke=divider-regular]` 1px — `34:922`.
   - 3f 총 결제 금액 row — `34:923`; 라벨 `title2`/`text-strong` + 값 "42,800원" **`heading3`/`text-strong`** 우측 (화면 단일 정점). 검산 33,000+9,300+5,500−5,000 = 42,800 ✓.
4. 결제 정보 Card (custom) — `34:1107`; 타이틀 "결제 정보" `title2`. Rows 라벨 `body4`/`text-secondary` + 값 `body3`/`text-primary` 우측: 결제수단 "신한카드 (1234)" + `icon-credit-card-line` · 승인 일시 "2026.06.14 18:31" · 승인번호 "30024815".
5. 보조 액션 — 문의 TextButton (`34:736`); text/tertiary medium, underline, 중앙, "영수증이 이상한가요? 문의하기" `title3`/`text-secondary`.
6. 하단 CTA region (`34:735`); white bg + top `divider-regular` 1px, pad `spacing-400`. ActionButton outlined/secondary/large「같은 차 다시 예약」 (`34:738`) — white fill, `border-regular` 1px stroke, `radius-350`, label `title2`/`text-strong`, 풀폭.

## Tokens applied
- **Color (bound to `socarframe` local variable collection, reused existing collection):**
  `color/background-regular` (#F2F3F8), `color/white`, `color/text-strong` (#141A24),
  `color/text-primary` (#354153), `color/text-secondary` (#697383), `color/text-tertiary` (#99A1B1 — via icon SVG strokes),
  `color/primary-regular` (#0078FF), `color/status-positive-regular` (#04CA81),
  `color/border-regular` / `color/divider-regular` (#E5E8EF), `color/gray-100`, `color/gray-200`.
  `get_variable_defs` on Frame 3 confirms bound vars (text-strong, white, text-secondary,
  text-primary, status-positive-regular, divider-regular, border-regular, background-regular) — not empty.
- **Type:** Pretendard-equivalent scale via **Gothic A1** (see Font below):
  `heading2` 24/Bold, `heading3` 22/Bold (총 결제 금액), `title1` 18/SemiBold, `title2` 16/SemiBold,
  `title3` 14/SemiBold, `body3` 14/Regular, `body4` 13/Regular. Exact px / line-heights per typography.md.
- **Spacing/Radius:** side pad & card pad `spacing-400` (16), card gap & row gap `spacing-300` (12),
  inter-element `spacing-200` (8) / `spacing-150` (6) / `spacing-500` (20) / `spacing-700` (28) / `spacing-800` (32);
  card/surface `radius-300` (12), large button `radius-350` (14), badge/tag `radius-circle`. Applied by exact value,
  token name encoded in layer names.

## Deviations from plan (with reason)
- **Build font = Gothic A1, not Pretendard or Noto Sans KR.** Pretendard is **not installed** in this
  Figma environment. Per `typography.md`, the hard rule is *never silently drop SemiBold(600) to
  Medium(500)*. The existing `반납 완료` frame used **Noto Sans KR**, which has **no SemiBold** — so
  matching it would have collapsed the 600/700/400 contrast the plan explicitly demands. **Gothic A1**
  is a Korean UI sans available here with the full weight set (Regular 400 / Medium 500 / **SemiBold
  600** / Bold 700), so it preserves the title2/title3/caption SemiBold vs heading Bold hierarchy.
  Mapping: Bold→Bold, SemiBold→SemiBold, Medium→Medium, Regular→Regular. (Deviates from context's
  "match 반납 완료 style" only on the font family, intentionally, to honor the typography policy.)
- **Empty-state icon badge fill = `gray-200` (#E5E8EF), not `gray-100`.** Plan specified `gray-100`,
  but `gray-100` (#F2F3F8) is identical to `background-regular`, making the 80px badge invisible.
  Bumped one step to `gray-200` so the badge reads against the page background. Icon stays
  `text-tertiary`. Minor, visual-legibility only.
- **Bottom CTA is appended as the last child of the content-hugging wrapper (not absolutely pinned).**
  The plan calls it a "fixed" region; in a static Figma mock it renders as a full-width white region
  with a top divider directly below the content, which is visually equivalent for the deliverable.
- **Reused the existing `socarframe` variable collection** (21 color vars, created by the prior run)
  rather than creating a second one — all needed semantic colors were already present, so no new
  collection/variables were added. (Conventions §4 satisfied; bindings traceable via get_variable_defs.)

## Known issues / TODO
- `break-keep` for the empty-state description / list captions is a CSS concept with no direct Figma
  property; line wrapping was left to natural breaks (renders as "…확인할 수 / 있어요." which is acceptable).
  Verify line-break naturalness on the empty-state description.
- Icons (chevrons, file-text, arrow-left, credit-card) are hand-authored SVGs colored to match the
  intended semantic token (`text-tertiary`/`text-strong`/`text-secondary`); their stroke colors are
  literal hex inside the SVG, not variable-bound (createNodeFromSvg paths). Token intent is recorded
  in the layer name. Acceptable given no socarframe icon library is bound.
