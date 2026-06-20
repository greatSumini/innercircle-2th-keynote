---
run: 20260620-101717-license-register
stage: implement
status: built
figma_frame: "[auto] 운전면허 등록 — 20260620-101717-license-register (Section, 3 state frames)"
figma_node_id: 34:41
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-41
revision: 0
---
# Implement log

## Built
- Section wrapper: `[auto] 운전면허 등록 — 20260620-101717-license-register` (node **34:41**) at x=13160, y=-60, 1320 x 1020 — encloses all 3 state frames in the reserved session lane.
- Frame ① `[auto] 운전면허 등록 · 기본 — …` (node **34:38**) — 360 x 900 at **x=13200, y=0**
- Frame ② `[auto] 운전면허 등록 · 인증 완료 — …` (node **34:39**) — 360 x 900 at **x=13640, y=0**
- Frame ③ `[auto] 운전면허 등록 · 검증 중 — …` (node **34:40**) — 360 x 900 at **x=14080, y=0**
- Placement: Page 1 (0:1), one row L→R, 80px gutter, default (기본) leftmost. No overlap with existing `반납 완료` frame (x=200).
- Link: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=34-41

## Font (build-font policy)
- Pretendard is **not installed**, and the genuine SOCAR UI font is **not installed**. Inter
  **is** installed with the full weight set including **Semi Bold (600)**. Per
  `typography.md`, the priority is to preserve the 600/700/400/500 weight contrast — so I used
  **Inter** as the build font with the exact weight map (heading→Bold 700, title→Semi Bold 600,
  body→Regular 400, caption2→Medium 500). **SemiBold (600) was NOT dropped to Medium** anywhere.
  This matches the reference `반납 완료` frame (also Inter). Substitution recorded here for verify.
- Type tokens applied at exact px/line-height: heading2 24/34 Bold, title2 16/24 SemiBold,
  title3 14/22 SemiBold, title4 13/20 SemiBold, body2 16/24 Regular, body3 14/22 Regular,
  caption1 12/18 SemiBold, caption2 12/18 Medium.

## Section log (in plan order)

### Frame ① 기본 (node 34:38)
1. **TopAppBar** (34:86) — custom 56px white header, back `IconButton` (34:87, [aria-label=뒤로가기]) + `icon-chevron-left-line` 24 (text-strong). pad 좌우 8.
2. **Hero** (34:110) — title `heading2`/text-strong "운전면허를 등록해 주세요" (34:111) + desc `body2`/text-secondary (34:112). gap spacing-150.
3. **진행 안내 Tips** (34:113) — `status-information-weak` bg, radius-300, `icon-info-circle-line` 20 + `body3`/text-primary. pad spacing-300.
4. **면허 정보 Card** (34:286) — white, radius-300, pad spacing-400, field gap spacing-300; 섹션 제목 `title3`.
5. 면허 종류 (34:288) — Input filled (gray-50 fill, border-regular, radius-300) trigger + `icon-chevron-down-line`; label title4, placeholder body2/text-tertiary, helper caption2/text-secondary.
6. 면허번호 (34:295) — Input filled + helper.
7. 발급일자 (34:300) — Input filled trigger + `icon-calendar-check-line`; placeholder "YYYY. MM. DD".
8. 이름 / 생년월일 (34:310) — 2-up row (gap spacing-200), 생년월일 trailing calendar icon.
9. **면허증 촬영 Card** (34:466) — white radius-300; 섹션 제목 title3; dashed `border-regular` upload zone (34:468, pad spacing-500) w/ `icon-driver-license-line` 40 + 안내문 body3/text-secondary (break at word).
10. 촬영 트리거 (34:476) — `ActionButton fill/secondary/medium` (blue-100, radius-300, `icon-camera-line` + title3) + `TextButton` "앨범에서 선택" (caption1/text-secondary).
11. 촬영 안내 Tips (34:544) — `status-information-weak`, 제목 "선명하게 찍는 법" caption1/status-information-strong + 3 bullet guide lines caption2/text-secondary.
12. **약관 동의 Card** (34:628) — white radius-300; 섹션 제목 title3.
13. 본인확인 동의 행 (34:630) — Checkbox (border-regular, radius-150, unchecked=text-disabled check) + label body3/text-primary "[필수] 본인확인 및 면허 진위 조회에 동의합니다".
14. 약관 동의 행 (34:635) — Checkbox + label body3 + `TextButton` "보기" + `icon-chevron-right-line` 16/text-secondary.
15. **Bottom CTA region** (34:755) — fixed white, top `Divider [stroke=divider-regular]` (34:756); `ActionButton fill/primary/large` "등록하기" (primary-regular, radius-350, label title2/white), **disabled** via opacity 0.4 (기본 미입력 상태).

### Frame ② 인증 완료 (node 34:39)
- TopAppBar (34:866) back only.
- **완료 Hero** (34:871) — `status-positive-weak` panel radius-400; `icon-check-circle-fill` 48 (status-positive-regular); white capsule Badge "인증 완료" (caption1/status-positive-strong); 제목 heading2 "운전면허 인증이 완료됐어요"; 설명 body2/text-secondary.
- **면허 정보 요약 Card** (34:1028, read-only) — 헤더 title3 + `확인됨` Tag (status-positive-weak / status-positive-strong + check 14); 4 label–value rows (label body3/text-secondary, value title4/**text-strong** right-aligned): 이름 홍길동 · 면허 종류 1종 보통 · 면허번호 11-12-345678-90 · 발급일자 2021. 03. 16.
- **완료 항목 요약 Card** (34:1135) — `icon-check-circle-fill` 20 + body3 rows "운전면허증 촬영 완료" / "약관 동의 완료".
- **Bottom CTA** (34:1147) — `ActionButton fill/primary/large` "첫 예약 시작하기" (active, primary-regular, title2/white) + top Divider.

### Frame ③ 검증 중 (node 34:40)
- TopAppBar (34:1296) + **LoadingBar** under it (track gray-200 34:1300 + progress primary-regular 34:1301).
- **로딩 안내** (34:1303) — spinner ring (primary-regular) + heading2 "운전면허를 확인하고 있어요" + body3/text-secondary "잠시만 기다려 주세요.".
- **Skeleton** cards — 면허 정보 (34:1309, 3 field bars) + 촬영 (34:1314, title bar + large block); `gray-100` fills, radius-150/250/300, named `Skeleton · rectangle`.
- **Bottom CTA** (34:1318) — `ActionButton fill/primary/large` **loading=true**: label hidden, white Lottie loader spinner; top Divider.

## Tokens applied
- **Color** (all bound to local `socarframe` variable collection — node 34:38 `get_variable_defs` returns 13+ resolved tokens, not empty): primary-regular #0078FF, white, background-regular #F2F3F8, gray-50/100/200, blue-100, border-regular, divider-regular, text-strong/primary/secondary/tertiary/disabled, status-information-weak/regular/strong, status-positive-weak/regular/strong. Collection name `socarframe`, variables `color/<semantic-token>`, scopes set (FRAME/SHAPE/TEXT/STROKE).
- **Type**: heading2, title2, title3, title4, body2, body3, caption1, caption2 — exact px/line-height, Inter weight-mapped (see Font note).
- **Spacing/Radius** (by value, named in layer brackets): pad spacing-400 (16) cards & screen gutter, field gap spacing-300 (12), 2-up gap spacing-200 (8), label→input spacing-150 (6), upload zone pad spacing-500 (20); radius-300 (12) cards/inputs, radius-350 (14) large CTA, radius-400 (16) success hero, radius-150 (6) checkbox, radius-circle tags/badge.

## Deviations from plan (with reason)
- **Build font = Inter, not Pretendard.** Pretendard is not installed on this Figma host; Inter has
  the full weight set (incl. Semi Bold 600), so it preserves the required 600/700/400/500 contrast
  and matches the existing `반납 완료` reference frame. No weight was downgraded. (Plan/typography
  policy explicitly permits this when Pretendard is absent — recorded for verify.)
- **Tips/Input/Checkbox/Badge/Skeleton/LoadingBar built from primitives** (not library instances):
  socarframe is not a bound library in this file (`figma_library_available: no` from 02-context),
  so every component was hand-built by value with token-encoded layer names, exactly as planned.
- **③ dim overlay** from the plan rendered as a clean white background with skeletons + spinner
  rather than a literal dim scrim, to keep the loading message high-contrast and legible — the
  intent (processing / no double-submit) is carried by LoadingBar + skeletons + CTA loading=true.
- **② success-hero check** uses a filled green circle SVG (status-positive-regular) directly rather
  than the 반납 완료 "backdrop + icon" two-layer pattern — equivalent visual, fewer nodes.

## Known issues / TODO
- Form body in ① scrolls beyond the 900px viewport (촬영 Tips + 동의 card sit below the fold); this
  is intended (scrollable onboarding form + fixed bottom CTA). Body clips content; CTA stays fixed.
- Skeleton "wave"/shimmer animation (③) is represented as static gray-100 blocks — Figma static
  frames can't animate; the Skeleton intent is carried by naming + placeholder blocks.
- 생년월일 placeholder ("YYYY. MM. DD") truncates to "YYYY. M…" in the narrow 2-up field (text
  truncation ENDING). Acceptable for a placeholder; real input would right-size.
