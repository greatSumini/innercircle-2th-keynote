---
run: 20260620-070646-return-complete
stage: implement
status: built
figma_frame: "[auto] 반납 완료 — 20260620-070646-return-complete"
figma_node_id: 3:2
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=3-2
revision: 0
---
# Implement log

## Built
- Frame: `[auto] 반납 완료 — 20260620-070646-return-complete` (node `3:2`) — 360 x 857
  (planned 360x800; height grown to 857 to fit all content, which the plan explicitly allows —
  "본문 길이에 따라 세로는 가변이지만 디자인 기준 높이는 800").
- Link: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled?node-id=3-2
- Placed in empty canvas space at x=200, y=0 on Page 1 (file was empty — no overlap).

## Section log (in plan order)
1. **Top app bar** (node `3:3`) — custom `white` #FFFFFF bar, 56px, horizontal auto-layout, trailing
   slot only, no back. Side padding `spacing-400` 16px.
1a. **닫기 IconButton** (node `3:4`) — 40x40 transparent touch box, centered. Holds `icon-close-line`
    vector (node `3:5`), 24px, stroke `text-strong` #141A24. Layer named with `aria-label=닫기`.
2. **Success hero** (node `5:15`) — vertical auto-layout, center aligned. paddingTop `spacing-600` 24px
   (trimmed from `spacing-800` 32 to reclaim vertical space — see Deviations), per-item spacing via
   spacer frames (icon→title `spacing-400` 16, title→subline `spacing-150` 6).
2a. **Check icon** (node `5:17`) — `icon-check-circle-fill` SVG vector, 56px, fill `status-positive-regular`
    #04CA81, on a 72x72 `status-positive-weak` #E6FEF0 circular backdrop (node `5:16`, radius-full 36).
2b. **Hero title** (node `5:21`) — "반납이 완료되었어요", `heading2` (24/34, Bold), `text-strong` #141A24, centered.
2c. **Hero subline** (node `5:23`) — "안전하게 반납해 주셔서 감사해요. 결제 내역을 확인해 주세요.",
    `body2` (16/24, Regular), `text-secondary` #697383, centered.
3. **이용 요약 card** (node `6:2`) — `white` #FFFFFF rounded surface, radius 12, inner padding
   `spacing-400` 16px, row gap `spacing-300` 12px. Card title "이용 요약" (node `6:3`, `title2` 16/24, text-strong).
3b–3e. Four label–value rows (nodes `6:4`, `6:7`, `6:10`, `6:13`): SPACE_BETWEEN auto-layout rows,
   label `body3` (14/22) `text-secondary`, value `title3` (14) `text-primary` right-aligned (FILL, wraps).
   차량 / 쏘카존 / 이용 시간 / 주행 거리 with planned values.
4. **결제 요약 card** (node `6:16`) — `white` rounded surface, radius 12, inner padding `spacing-400` 16px,
   fee row gap `spacing-200` 8px (+4 spacers to make title↔first-row and divider gaps `spacing-300` 12px).
   Card title "결제 요약" (node `6:17`, `title2`, text-strong).
4b–4d. Three fee rows (nodes `6:19`, `6:22`, `6:25`): label `body3` text-secondary, value `body3`
   `text-primary` right-aligned. 대여요금 32,000원 / 주행요금 5,460원 / 보험료 5,500원.
4e. **Divider** (node `6:29`) — 1px full-width, `divider-regular` #E5E8EF.
4f. **총 결제금액 total row** (node `6:31`, emphasized) — label "총 결제금액" `title2` text-strong,
    value "42,960원" `heading3` (22/30, Bold) text-strong, right-aligned. Largest type in the card.
    (Sum check: 32,000 + 5,460 + 5,500 = 42,960 ✓.)
5. **Bottom fixed CTA region** (node `6:34`) — `white` sticky container, top 1px `divider-regular`
   #E5E8EF border, padding top `spacing-300` 12 / bottom `spacing-400` 16 / sides `spacing-400` 16,
   item gap `spacing-200` 8.
5a. **확인 ActionButton** (node `6:35`, fill/primary/large) — full-width, bg `primary-regular` #0078FF,
    radius 12 (`radius-350`), py 16 (`spacing-400`) / px 22 (`spacing-550`), ≈56px tall. Label "확인"
    (node `6:36`) `title2` (16/24), `white` #FFFFFF, centered.
5b. **이용 내역 보기 TextButton** (node `6:37`, text/tertiary/medium) — full-width touch, no fill,
    ≈40px tall. Label (node `6:38`) "이용 내역 보기" `title3` (14/22) `text-secondary` #697383, centered.

## Tokens applied
- **Color:** background-regular #F2F3F8 (frame); white #FFFFFF (app bar, cards, CTA region);
  status-positive-regular #04CA81 + status-positive-weak #E6FEF0 (success hero only);
  primary-regular #0078FF (확인 fill); text-strong #141A24 (title, card titles, total, close icon);
  text-primary #354153 (row values); text-secondary #697383 (subline, labels, TextButton);
  divider-regular #E5E8EF (payment divider, CTA top border). white #FFFFFF (CTA label).
- **Type:** heading2 24/34 Bold (hero title); heading3 22/30 Bold (총 결제금액 value); title2 16/24
  (card titles, total label, 확인 label); title3 14/22 (usage-card values, TextButton); body2 16/24
  (subline); body3 14/22 (labels, fee values).
- **Spacing/Radius:** screen side padding spacing-400 16; card inner padding spacing-400 16; card↔card
  gap spacing-300 12; fee-row gap spacing-200 8; hero icon→title spacing-400 16, title→subline
  spacing-150 6; CTA padding spacing-300/400, CTA item gap spacing-200 8; ActionButton py spacing-400
  16 / px spacing-550 22; button radius radius-350 12; card radius 12 (no socarframe token — see issues).

## Deviations from plan (with reason)
- **Font substitution:** SOCAR Korean UI font is not installed in this environment, so I used
  **Noto Sans KR** (a clean Korean UI sans) at the exact px/line-heights from typography.md.
  Noto Sans KR has no SemiBold(600) weight, so all `SemiBold`-role styles (`title2`/`title3`) use
  **Medium(500)**; Bold(700) roles (`heading2`/`heading3`) and Regular(400) roles map exactly.
  Visual hierarchy is preserved; flag for verify if the real font becomes available.
- **Frame height 800 → 857:** all content (incl. the emphasized 총 결제금액) overflowed a fixed 800px
  body by ~77px. The plan permits variable height ("세로는 가변"), so I grew the frame to fit rather
  than crop the most important value. Also trimmed hero paddingTop 32→24 (`spacing-800`→`spacing-600`),
  hero paddingBottom 12→8, and body paddingBottom 24→16 to keep it close to the 800 baseline.
- **Sticky/scroll is approximated:** the body is an overflow=VERTICAL container (scrollable in
  prototype) under a fixed app bar and above the fixed CTA region; in the static frame the full
  height shows everything at once. Figma static design can't truly "stick" without a prototype.

## Known issues / TODO
- **Card corner radius (12px) has no socarframe token** (radius-300 is the assumed equivalent) —
  flagged in plan/context for verify; applied consistently to both cards.
- **No bound design-system variables/styles:** socarframe is not a library in this file (02-context),
  so all tokens are applied by exact value with token names left in layer names for traceability.
  A future improvement is to mirror these as local variables/styles.
- Font substitution (Noto Sans KR / Medium-for-SemiBold) as noted above — replace with SOCAR UI font
  if/when available.
