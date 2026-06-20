---
run: 20260620-101656-zone-explore-map
stage: verify
verdict: PASS
score: 9/9 rubric items passing
---
# Verify report (re-verify — revise cycle 1)

## Looked at
- Frame: `[auto] 쏘카존 탐색 · 기본 — 20260620-101656-zone-explore-map` (node 34:193) — screenshot captured: yes (fresh)
- Frame: `[auto] 쏘카존 탐색 · 빈 상태 — 20260620-101656-zone-explore-map` (node 34:1155) — screenshot captured: yes (fresh)
- Inspected: get_metadata (card-list tree 34:1052), get_design_context (card2 34:1071), get_variable_defs (34:193 → 19 vars). Cropped + upscaled the bottom-sheet region to read each card's zone-name wrap directly against the metadata (text-node widths, truncation), not by guessing from the render.

## Revise verification (cycle 1 — prior FAIL was criterion H, P2)
The prior FAIL was criterion **H**: cards 2 & 3 split the noun "쏘카존" mid-token, stranding "존" on its own line. **Confirmed fixed:**
- Card 2 R2 row (34:1080): now VERTICAL (`flex-col gap-[2px]`, h=50) with sub-rows `쏘카존명 행` (38:2) + `도보거리 행` (38:3). Zone name `34:1083` widened to **204px** (was ~145px), `whitespace-nowrap` + `text-ellipsis` (maxLines=1/ENDING). Renders "역삼동 공영주차장 쏘카존" on **one line, 쏘카존 intact**; "도보 6분" on the line below. Inline `·` divider removed.
- Card 3 R2 row (34:1098): same conversion (38:4 / 38:5). Zone name `34:1101` at 204px renders "테헤란로 GS타워 쏘카존" on **one line, intact**; "도보 9분" below. `·` divider removed.
- Card 1 (34:1062): unchanged structure (inline pin + name + `·` + 거리), name `34:1065` got maxLines=1/ENDING as a safety net; "강남역 2번 출구 쏘카존 · 도보 3분" fits on one line.
- No regression elsewhere: 19 color vars still bound to `socarframe` (all resolve to correct semantic hex); Gothic A1 SemiBold(600) preserved on model name & price number, zone name stays Regular; radius tokens match (card rounded-[12px]=radius-300, thumb rounded-[8px]=radius-200, tag/chip/pin/FAB rounded-[999px]=radius-circle); 빈 상태 frame & both frames' reserved-lane positions untouched.

## Rubric
| # | Criterion | Result | Note |
|---|-----------|--------|------|
| A | Plan coverage | PASS | All sections present in plan order: map+pins(선택1)+TopAppBar+chips(즉시예약 selected)+half sheet(헤더 "내 주변 12대"+카드 3장, 1장 강조)+FAB; 빈 상태 frame swaps card list for empty block, keeps map/bar/chips context. |
| B | Component correctness | PASS | Custom gaps built from correct primitives (pins, map, cards, sheet); IconButtons, Chips, Tags, ActionButton/TextButton named to real socarframe components with variants. No hand-drawn lookalikes of available components. |
| C | Token usage | PASS | 19 colors bound to local `socarframe` collection (`color/<token>`), all resolve to correct semantic hex. Radius px match token names (card 12px=radius-300, thumb 8px=radius-200, tag/chip/pin/FAB 999px=radius-circle, sheet radius-400). Font Gothic A1 with SemiBold(600) preserved — no 600→500 downgrade (Pretendard not installed; documented substitution, P3). |
| D | Layout & alignment | PASS | On-grid 16px insets, consistent spacing tokens, proper auto-layout. New vertical R2 stacks (38:2/38:3, 38:4/38:5) align cleanly; card heights re-flowed (112/134/132) with no overlap or clipping. Half sheet at y=352; chip row overflows 360 intentionally as scroll hint; frames in reserved lane w/ 80px gutter. |
| E | Copy & voice | PASS | Copy matches plan verbatim (검색어, 일시, 칩, 헤더, 3 카드, 빈 상태). Natural SOCAR Korean, no placeholder/lorem. |
| F | Accessibility | PASS | 44×44 back/FAB targets; icon-only buttons carry `[aria-label=…]`; status conveyed by text+color (즉시예약/15% 할인/예약 마감임박); core selection in lower half (thumb reach). 검색 수정 is 40×40 per plan spec. |
| G | Polish | PASS | Single emphasis pair reads clearly: selected pin (primary-strong, enlarged, white ring, 9,900원~ bubble) ↔ selected card (primary-regular border). Hierarchy strong/secondary/tertiary holds; the R2 restructure made cards 2/3 read cleaner (name on its own line). No full-width CTA — correct (card tap is the action). |
| H | Line-break naturalness | PASS | All multi-line blocks wrap on meaning units. Cards 1/2/3 keep "쏘카존" whole on one line (no mid-token split, no stranded "존"); distance moved to its own sub-row. Empty-state body wraps on an authored `\n` ("…범위를 넓혀 / 다시 찾아보세요.") — no stranded josa/widow. maxLines=1/ENDING guards a genuinely-long zone name without widowing a syllable. |
| I | Naming & organization | PASS | Frames `[auto] <screen> · <state> — <run-id>`; section wrapper at stem name; layers carry role + token brackets; new sub-rows named by role (`쏘카존명 행` / `도보거리 행`); text nodes carry type token; icon buttons carry aria-label; collection `socarframe` with `color/…` vars. No default names. |

## Issues (prioritized, each with a concrete fix)
- **P3 (nice-to-have):** Build font is Gothic A1 (Pretendard not installed). SemiBold(600) is preserved so hierarchy is intact and the typography.md substitution rule (no weight drop) is honored — non-blocking. Swap to Pretendard if/when it is installed in the Figma environment. Reason recorded in 04-implement.md.
- **P3 (nice-to-have):** 도보거리 라벨(34:1085 "도보 6분", 34:1103 "도보 9분")이 caption1이라 토큰상 SemiBold이다. 쏘카존명(body3/Regular)과 같은 줄에 있던 미세한 위계 역전은 이번 R2 수직 분리로 구조적으로 해소됨(거리가 이름 아래 별도 줄). 추후 정보 위계를 더 낮추고 싶으면 도보거리를 `body4`(Regular)로 내리는 것을 검토 — 선택적.

## What's good
- 지도-리스트 연결 와우 디테일이 의도대로 작동: 선택 핀(확대+화이트 링+9,900원~ 말풍선)과 선택 카드(primary 보더)가 짝을 이뤄 "이 핀 = 이 카드"가 한눈에 읽힘.
- 줄바꿈 수정이 임시방편(폭 강제 1줄 잘림)이 아니라 구조 재설계로 처리됨: R2를 [이름 / 거리] 수직 스택으로 분리해 쏘카존명이 행 전체 폭(204px)을 받고, maxLines=1/ENDING은 초장문 이름에 대한 안전망으로만 작동. 세 카드 모두 "쏘카존" 통째 유지.
- 토큰 위생이 그대로 유지됨: 19개 color가 `socarframe` 로컬 컬렉션에 바인딩되고 모두 정확한 semantic hex로 해석, radius/spacing px가 토큰명과 일치, Gothic A1 SemiBold(600) 보존, 레이어 이름이 역할+토큰을 담아 라이브러리 없이도 완전 추적 가능.

VERDICT: PASS
