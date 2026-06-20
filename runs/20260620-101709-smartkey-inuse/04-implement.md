---
run: 20260620-101709-smartkey-inuse
stage: implement
status: built
figma_frame: "[auto] 이용 중(스마트키) · 잠김 — 20260620-101709-smartkey-inuse"
figma_node_id: 34:25
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-25
revision: 0
---
# Implement log

## Built
- Section: `[auto] 이용 중(스마트키) — 20260620-101709-smartkey-inuse` (node 34:843) at x=9560, y=-72, 880×1023 — wraps both state frames.
- Frame A (default, leftmost): `[auto] 이용 중(스마트키) · 잠김 — 20260620-101709-smartkey-inuse` (node **34:25**) — **360 × 911** at x=9600, y=0.
- Frame B: `[auto] 이용 중(스마트키) · 열림 — 20260620-101709-smartkey-inuse` (node **34:666**) — **360 × 911** at x=10040, y=0 (80px gutter: 9600+360+80).
- Page: Page 1 (0:1). Placed in the reserved canvas lane starting x=9600; no overlap with the only pre-existing frame (반납 완료 at x=200).
- Link (잠김 frame): https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-25
- Link (열림 frame): https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-666

## Section log (in plan order)
Built section-by-section in the 잠김 frame (34:25), then cloned to the 열림 frame (34:666) and toggled only the door tile. Auto-layout used throughout; horizontal section padding `spacing-400` (16px) applied via per-section wrappers.

1. **TopAppBar** (node 34:26) — built from primitives. White bg, height 56, paddingX 8. Left: `IconButton 뒤로가기 [aria-label=뒤로가기]` 44×44 with `icon-chevron-left-line` 24 (stroke bound `text/strong`). Center: title "이용 중" `title1` (SemiBold 18/26) `text/strong`, FILL + center-aligned; right 44px balancing spacer keeps title centered.
2. **Hero (custom)** (card node 34:47) — white card `radius-300` (12px), pad `spacing-500` (20px), inner gap 12. 차량 모델명 "쏘나타 디 엣지" `title1` `text/strong`; 번호판 "12가 3456" `body3` `text/secondary`; `Divider [stroke=divider-regular]`; 남은 시간 라벨 "남은 이용 시간" `body3` `text/secondary`; 타이머 값 "02:13" `display2` (Bold 36/44, ls −0.6) `text/strong`; 반납 예정 행 `icon-clock-line` 16 (`text/tertiary`) + "23:40 반납 예정" `body3` `text/secondary`.
3. **Door toggle tile (custom) · 잠김 / 열림** (잠김 tile 34:97, 열림 tile 34:688) — primary control. `radius-400` (16px), pad 20, gap 12, FILL width, HUG height (≈160). **잠김:** bg `status-information-weak`; Tag capsule (white fill, stroke `status-information-regular`, dot + "잠김" `caption1` `status-information-strong`); `icon-lock-fill` 56 (`status-information-regular`); 액션 라벨 "문 열기" `title2` `text/strong`; 보조 안내 "차 문이 잠겨 있어요" `caption1` `text/secondary`. **열림:** bg `status-caution-weak`; Tag stroke + dot + text `status-caution-regular/strong`, "열림"; `icon-lock-open-fill` 56 (`status-caution-regular`); 라벨 "문 잠그기"; 안내 "차 문이 열려 있어요 · 탭하여 잠그기".
4. **제어 버튼 그룹 (custom)** (node 34:225) — 2-up equal tiles, row gap 12. Each tile: white fill + stroke `border-regular` 1px, `radius-300`, pad 16, FILL width. Tile1 `icon-warning-light-fill` 28 (`text/primary`) + "비상등" `caption1` `text/secondary` `[aria-label=비상등 켜기]`. Tile2 `icon-horn-fill` 28 + "경적·차 찾기" `[aria-label=경적 울려 차 찾기]`.
5. **Tips (Info) (custom)** (node 34:417) — bg `status-information-weak`, `radius-300`, pad 12, gap 8. Leading `icon-info-circle-line` 20 (`status-information-regular`) + 본문 "탑승 전 차량 외관을 확인해 주세요. 흠집이 있다면 사진으로 남겨두면 안심돼요." `body3` `text/secondary`, FILL width, wraps to 2 lines.
6. **도움 row (custom)** (node 34:422) — white card `radius-300`. Two FILL TextButtons with leading icons: 좌 `icon-exclamation-triangle-fill` 20 + "사고·고장 신고" `body3` `text/secondary`; vertical `Divider [stroke=divider-regular]`; 우 `icon-phone-fill` 20 + "고객센터".
7. **Bottom CTA [fixed]** (node 34:485) — white bg, top `Divider [stroke=divider-regular]` (strokeTopWeight=1), pad 16 / top 12 / bottom 20 (home-indicator safe area), button gap 8. Pushed to frame bottom via flex spacer (`layoutGrow=1`). 상단(보조) `ActionButton · outlined/secondary/large` "이용 시간 연장" (white fill + `border-regular` stroke, `text/primary` label, `radius-350` 14px, h52). 하단(primary) `ActionButton · fill/primary/large` "반납하기" (`primary-regular` fill, white label, `radius-350`, h52).

## Tokens applied
- **Color (bound to existing local `Color` collection variables; `get_variable_defs` on 34:25 resolves):** `text/strong`, `text/primary`, `text/secondary`, `text/tertiary`, `primary/regular`, `status/information/weak`, `status/information/regular`, `status/information/strong`, `status/caution/weak`, `status/caution/regular`, `status/caution/strong`, `background/regular`, `border/regular`, `divider/regular`. (White `#FFFFFF` used directly for card/tile surfaces — no semantic white token exists in the collection.)
- **Type:** `display2` (Bold 36/44, ls −0.6) timer · `title1` (SemiBold 18/26) titles/model · `title2` (SemiBold 16/24) door label + CTA labels · `body3` (Regular 14/22) plate/label/Tips/help · `caption1` (SemiBold 12/18) Tag + control captions + door helper.
- **Spacing/Radius (by value, token names encoded in layer-name brackets):** padX `spacing-400` (16), card pad `spacing-500` (20), inner gaps `spacing-300`/`spacing-200` (12/8); card/control/tip `radius-300` (12), door tile `radius-400` (16), ActionButton `radius-350` (14).
- **Variables:** reused the file's existing local collections (`Color`, `Spacing`, `Radius`) established by the reference frame — color fills/strokes bound to `Color` variables. Did **not** create a duplicate `socarframe` collection (the existing `Color`/`Spacing`/`Radius` collections already hold the full semantic token set bound to primitives; reusing keeps the file consistent and traceable).

## Deviations from plan (with reason)
- **Build font = Gothic A1, not Pretendard.** Pretendard is **not installed** in this environment and no genuine SOCAR UI font is present. The reference 반납 완료 frame used Noto Sans KR — but **Noto Sans KR has no SemiBold (600)** (styles: Thin/Light/DemiLight/Regular/Medium/Bold/Black), which would force the forbidden SemiBold→Medium drop for every `title*`/`caption1` style. **Gothic A1** is an installed Korean UI sans with the full weight set incl. **SemiBold (600)** (Regular 400 / Medium 500 / SemiBold 600 / Bold 700 all present), so it preserves the 400/600/700 hierarchy contrast the type scale requires. Per typography.md policy ("if a font lacks Semi Bold, switch to a font that has it; never silently drop to Medium"). Exact px / line-height / letter-spacing from typography.md applied.
- **Frame height 911px, not 800px.** Plan baseline was 360×800 with a fixed bottom CTA; the full content (7 sections + safe-area pad) is genuinely ~911px tall, so an 800px frame clipped the CTA. Plan explicitly allows vertical extension ("본문이 길어지면 세로 확장 가능"). Frame set to 360×911 so the fixed bottom CTA + 20px home-indicator pad are fully visible. Bottom CTA still pinned to the frame bottom via a `layoutGrow` spacer.
- **Reused existing `Color`/`Spacing`/`Radius` variable collections** instead of creating a new collection literally named `socarframe`. The existing collections already carry the identical semantic token set (`text/strong`, `status/caution/weak`, `radius/300`, …) bound to primitives; creating a parallel `socarframe` collection would duplicate and fragment intent. Names follow the `color/… radius/… spacing/…`-equivalent grouping the conventions doc intends.

## Known issues / TODO
- Tag capsule uses a white fill + colored 1px stroke + leading dot (rather than a tinted `*-weak` fill) so the "잠김"/"열림" label reads clearly against the same-tone tile background; matches the plan's color+text intent. Verify may prefer a tinted fill — low priority.
- Icons are hand-built from inline SVG vectors (no bound SOCAR Icon Library exists in the file); shapes approximate the named socarframe icons (`icon-lock-fill`, `icon-lock-open-fill`, `icon-warning-light-fill`, `icon-horn-fill`, `icon-info-circle-line`, `icon-clock-line`, `icon-exclamation-triangle-fill`, `icon-phone-fill`, `icon-chevron-left-line`). Icon fills/strokes are bound to the correct color variables; glyph fidelity is approximate.
- Bottom CTA is laid out as a normal bottom section (pinned via flex spacer), not a true sticky overlay (Figma static frame has no scroll); visually equivalent at this frame height.
