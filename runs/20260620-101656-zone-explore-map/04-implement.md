---
run: 20260620-101656-zone-explore-map
stage: implement
status: built
figma_frame: "[auto] 쏘카존 탐색 · 기본 — 20260620-101656-zone-explore-map"
figma_node_id: 34:193
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-193
revision: 1
---
# Implement log

## Built
- Section: `[auto] 쏘카존 탐색 — 20260620-101656-zone-explore-map` (node 34:1339) — wraps both state frames.
- Frame A (default): `[auto] 쏘카존 탐색 · 기본 — 20260620-101656-zone-explore-map` (node **34:193**) — 360×800 @ abs x=4200, y=0.
- Frame B (empty): `[auto] 쏘카존 탐색 · 빈 상태 — 20260620-101656-zone-explore-map` (node **34:1155**) — 360×800 @ abs x=4640, y=0.
- Page: `Page 1` (0:1), active page. No new page created. 80px gutter, shared top edge — no overlap with existing frames (반납 완료 @ x=200; 홈 @ x=2400; 스마트키 @ x=9600; 면허 @ x=13160).
- Link (기본): https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-193
- Link (빈 상태): https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-1155
- Link (section): https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-1339

## Section log (in plan order — 기본 frame)
1. 지도 배경 (custom) — 풀블리드 360×800 placeholder. `background-regular` base + 9 city blocks (`gray-200`), 6 low-contrast roads (`divider-regular`), park hint (`status-positive-weak`) + water hint (`status-information-weak`). node 34:194.
2. 쏘카존 핀 마커 (custom) — 4 default teardrop pins `[fill=location-rental]` + white 2px outline (nodes 34:398, 34:401, 34:404, 34:407); 1 selected pin group `[fill=primary-strong]` enlarged (36px) with white ring + drop shadow + "9,900원~" price bubble `[fill=primary-strong radius=radius-circle]` `caption1`/white (group node 34:410). Built via createNodeFromSvg (teardrop path), fills bound to vars.
3. 내 위치 FAB — `IconButton 내 위치 · medium [aria-label=내 위치]` 44×44, white + `border-regular` 1px + shadow, `radius-circle`, `icon-my-location-line` stroked `text-primary`. node 34:1150.
4. TopAppBar (상단 요약 바) — floating white card `[fill=white radius=radius-300]` + shadow, 16px side inset, 8px top. node 34:490.
   - 4a 뒤로가기: `IconButton 뒤로가기 [aria-label=뒤로가기]` 44×44, `icon-chevron-left-line` stroke `text-primary`.
   - 4b 검색어 줄: "강남역 2번 출구" · `title3` (14 SemiBold) `text-strong`.
   - 4c 이용 일시 줄: "6/20(토) 14:00 ~ 6/21(일) 14:00" · `body4` (13) `text-secondary`, 2px below.
   - 4d 검색 수정: `IconButton 검색 수정 [aria-label=검색 수정]` 40×40, `icon-search-line` stroke `text-secondary`.
5. 필터 Chip 행 (가로 스크롤) — full-bleed HORIZONTAL auto-layout, 16px left inset, 8px gap (`spacing-200`), pill `radius-circle`. Overflows right edge (width 573 > 360) → frame clips → scroll hint. node 34:605.
   - 필터 (leftIcon `icon-filter-line`), 차종 (rightIcon `icon-chevron-down-line`), 경차, SUV, 전기차, 가격 (rightIcon), 즉시예약 (selected).
   - Default chips: white + `border-regular` 1px + `text-secondary` `title4`. Selected 즉시예약: `status-information-weak` fill + `primary-regular` 1px border + `primary-regular` text/`icon-bolt-fill`.
6. BottomSheet 셸 (half) — `[fill=white radius=radius-400]` top-rounded (16px), y=352 (≈44% top → half detent), 448px tall, top shadow, dimmed=false. node 34:832.
   - 6a 핸들바: 36×4 pill `[fill=gray-300 radius=radius-circle]`, 12px top pad (`spacing-300`). node 34:834.
   - 6b 시트 헤더: node 34:835.
     - 6b-1 타이틀: "내 주변 12대" · `title1` (18) `text-strong`.
     - 6b-2 정렬 토글: `TextButton 정렬` "거리순" `title4` `text-secondary` + `icon-chevron-down-line`.
     - 6b-3 보조줄: "강남역 반경 1km" · `caption1` (12) `text-tertiary`.
   - 6c 차량 카드 리스트 (scroll content, 12px gap, 16px side pad) — node 34:1052.
     - 카드1 (selected): 더 뉴 아반떼 / `즉시예약` tag (information) / 강남역 2번 출구 쏘카존 · 도보 3분 / 9,900원/시간. white + `primary-regular` 1.5px border `[radius=radius-300]`. node 34:1053.
     - 카드2 (default): 레이 / `15% 할인` tag (positive) / 역삼동 공영주차장 쏘카존 · 도보 6분 / 7,500원/시간. white + `border-regular` 1px. node 34:1071.
     - 카드3 (default): 아이오닉 5 / `예약 마감임박` tag (negative) / 테헤란로 GS타워 쏘카존 · 도보 9분 / 12,000원/시간. node 34:1089.
     - Card anatomy: 64×64 thumbnail `[fill=background-regular radius=radius-200]` + `icon-car-fill` `text-tertiary`; model `title2` `text-strong`; Tag `small/capsule` (status-*-weak bg + status-*-regular text, `caption1`); zone `body3` `text-secondary` + `icon-locationpin-fill` 12px + walk `caption1`; price 숫자 `title2` `text-strong` + "원/시간" `body4` `text-secondary`.

## Section log — 빈 상태 frame (34:1155)
- Cloned from 기본 to preserve map/TopAppBar/chips context. Pins removed (5). FAB kept.
- Sheet header + card list replaced with 빈 상태 블록 (node 34:1323), centered V auto-layout filling sheet:
  - `icon-car-search-line` 56px, stroke `text-tertiary` → spacer `spacing-300`.
  - 제목: "주변에 이용 가능한 차량이 없어요" `title1` `text-strong`, centered → spacer `spacing-200`.
  - 본문: "이용 날짜·시간을 바꾸거나 검색 범위를 넓혀\n다시 찾아보세요." `body2` `text-secondary`, centered, explicit line break (no mid-word break) → spacer `spacing-400`.
  - 보조 CTA: `ActionButton · fill/secondary/medium` "조건 변경하기" — `[fill=status-information-weak radius=radius-300]` + `primary-regular` `title3` label → spacer `spacing-300`.
  - 보조 링크: `TextButton 필터 초기화 · text/tertiary/small` `title4` `text-secondary`.

## Tokens applied
- Color (bound to local `socarframe` variable collection, confirmed via get_variable_defs on 34:193 — 19 vars resolve):
  `background-regular` `gray-200` `gray-300` `divider-regular` `border-regular` `white`
  `text-strong` `text-primary` `text-secondary` `text-tertiary`
  `primary-regular` `primary-strong`
  `location-rental`
  `status-information-weak/regular` `status-positive-weak/regular` `status-negative-weak/regular`.
- Type (exact px/line-height): `title1`(18/26 SB) `title2`(16/24 SB) `title3`(14/22 SB) `title4`(13/20 SB) `body2`(16/24 R) `body3`(14/22 R) `body4`(13/20 R) `caption1`(12/18 SB).
- Spacing/Radius (by value, token-named in layers): side pad `spacing-400`(16); chip gap `spacing-200`(8); card gap `spacing-300`(12); card pad `spacing-400`(16); handlebar top `spacing-300`(12); empty-block spacers 300/200/400. Radius: cards/bar `radius-300`(12); sheet `radius-400`(16); thumbnail `radius-200`(8); chips/tags/pins/FAB/bubble `radius-circle`(pill).
- Font: **Gothic A1** (Regular 400 / Medium 500 / SemiBold 600 / Bold 700). See deviations — Pretendard substitution.

## Deviations from plan (with reason)
- **Build font = Gothic A1, not Pretendard.** Pretendard is NOT installed in this Figma environment, and the genuine SOCAR UI font is not installed either. Noto Sans KR (the next obvious Korean sans) lacks SemiBold (600) — using it would have silently dropped 600→500, which the font policy explicitly forbids. Gothic A1 is an installed Korean UI sans with the full weight set (Regular/Medium/**SemiBold**/Bold), so it preserves the 600 vs 700 vs 400 contrast the SOCAR scale needs. Recorded per typography.md build-font rule.
- **Reused the existing local `socarframe` variable collection** (id VariableCollectionId:34:3, created by a concurrent batch session) instead of creating a duplicate. Added the 5 color vars it was missing for this screen (`primary-heavy`, `status-negative-weak`, `status-negative-regular`, `location-rental`, `gray-300`). Avoids two `socarframe` collections polluting the shared file. Collection/variable naming still matches figma-conventions §4 (`color/<token>`).
- **Frames wrapped in a Section** `[auto] 쏘카존 탐색 — …` at the run stem name; section background is a neutral light fill. Frame absolute positions remain exactly the reserved lane (기본 4200,0 / 빈 상태 4640,0), 80px gutter — verified via absoluteBoundingBox.

## Known issues / TODO
- Map/pins/sheet are a single visual "half" detent state (no drag interaction / tip·max detents) — per plan scope.

## Revise pass — revision 1 (2026-06-20)
Applied the fix list from `05-verify.md` (verdict REVISE; the only FAIL was criterion **H — line-break naturalness**, P2). Edited the existing 기본 frame (node 34:193) in place; the 빈 상태 frame (34:1155) and reserved-lane placement (기본 x=4200 / 빈 상태 x=4640) were not touched.

**P2 (criterion H) — "쏘카존" no longer splits mid-word in cards 2 & 3.**
- Root cause: each card's `쏘카존+도보 행` was a single HORIZONTAL row packing `[pin · 쏘카존명(FILL) · 구분점 · 도보거리]` into 220px, leaving the name only ~145px — too narrow for the 12-char names, which char-wrapped and stranded "존".
- Fix (verify option a): converted the R2 row to a **VERTICAL stack** (itemSpacing 2) with two sub-rows — `쏘카존명 행` `[pin + 쏘카존명]` and `도보거리 행` `[도보거리]`. The zone name now spans the full row width (204px) and reads on **one line, "쏘카존" intact**. Dropped the now-redundant inline `·` divider from cards 2 & 3.
- Safety net: set the zone-name text nodes to `maxLines = 1` + `textTruncation = ENDING` so a genuinely-long name would ellipsis-truncate rather than widow a syllable. Applied the same `maxLines=1`/ENDING protection to card 1's name (no layout change — it already fit on one line with its `·`+거리 inline).
- Verified visually: card 1 "강남역 2번 출구 쏘카존 · 도보 3분" (1 line), card 2 "역삼동 공영주차장 쏘카존" + "도보 6분" below, card 3 "테헤란로 GS타워 쏘카존" + "도보 9분" below — all 쏘카존 whole, h=22 single-line for each name.

**Nodes touched (all inside 기본 frame 34:193):**
- Card 2 R2: row `34:1080` (HORIZONTAL→VERTICAL), name `34:1083` (FILL/maxLines=1/ENDING, now 1 line), 도보거리 `34:1085` (reparented). Removed `·` divider `34:1084`. Created sub-rows `38:2` (쏘카존명 행), `38:3` (도보거리 행).
- Card 3 R2: row `34:1098` (HORIZONTAL→VERTICAL), name `34:1101` (FILL/maxLines=1/ENDING, now 1 line), 도보거리 `34:1103` (reparented). Removed `·` divider `34:1102`. Created sub-rows `38:4` (쏘카존명 행), `38:5` (도보거리 행).
- Card 1: name `34:1065` — added maxLines=1 + ENDING (layout unchanged).

**Not changed:** all `socarframe` color variable bindings, radius/spacing tokens, Gothic A1 fonts (incl. SemiBold 600), layer naming convention (new sub-rows named by role: `쏘카존명 행` / `도보거리 행`), the 빈 상태 frame, and both frames' absolute positions. P3 items (Gothic A1 vs Pretendard substitution; caption1 SemiBold on 도보거리) left as-is — non-blocking; the distance now sits on its own line below the Regular name so the earlier perceived weight-inversion is resolved structurally.
