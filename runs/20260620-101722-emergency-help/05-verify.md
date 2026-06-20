---
run: 20260620-101722-emergency-help
stage: verify
verdict: PASS
score: 9/9 rubric items passing
---
# Verify report

## Looked at
- Frame: `[auto] 사고·고장 신고(긴급 도움) — 20260620-101722-emergency-help` (node `34:60`) — screenshot captured: yes
- Cross-checked: `get_metadata` (full tree), `get_variable_defs` (bound token map), `get_design_context` on 긴급 액션 Card (`34:134`) and FAQ Section (`34:644`) for font/weight + wrap.

## Rubric
| # | Criterion | Result | Note |
|---|-----------|--------|------|
| A | Plan coverage | PASS | All 8 sections present and in plan order: TopAppBar → Hero → 긴급 액션 Card → Tips → 상황 선택 → SelectionBox×3 → 차량 Card → FAQ. |
| B | Component correctness | PASS | Hand-built-from-primitives per context pack (no socarframe instances in file); right patterns/variants — fill+outlined ActionButtons, single SelectionBoxGroup ×3, Tips, Tag, Divider, TextButton. Layer names carry component·variant. |
| C | Token usage | PASS | All fills/strokes/radii/spacing bound to local vars w/ correct hex; radius-300=12, radius-350=14 match token names exactly (large buttons=350, cards/Tips/SelectionBox=300). Type tokens applied; Gothic A1 SemiBold(600) preserved (heading2=Bold, title/caption=SemiBold, body=Regular) — no 600→500 downgrade. |
| D | Layout & alignment | PASS | On 4px grid (x=16 gutters, spacing tokens throughout), vertical auto-layout, no overlap/clip. Frame at x=15000 clear of existing frames. |
| E | Copy & voice | PASS | Copy verbatim to plan, natural calm SOCAR Korean ("당황하지 않으셔도 돼요. 바로 도와드릴게요."), no placeholder/lorem; dummy vehicle/FAQ data is in-scope per plan. |
| F | Accessibility | PASS | Back button 48×48 with `[aria-label=뒤로가기]`; large CTAs h=52, SelectionBox rows h=78, FAQ rows ≥56 — all ≥48 targets. White on `status-negative-regular` (#FF3A5B) CTA + phone icon + verb label = not color-only. |
| G | Polish | PASS | Single primary action (red fill CTA) is the clear focus; progressive de-emphasis (outlined → white cards → neutral → text link) reads cleanly. 「이용 중」 Tag recolored to status-information (blue) so red stays reserved for the emergency area. One stranded-syllable wrap (see P2) is the only blemish. |
| H | Line-break naturalness | PASS | Hero, card header/desc, both CTA labels, Tips, all SelectionBox labels/desc, FAQ row 2, and TextButton wrap naturally / single-line. One awkward wrap: FAQ row 1 (`34:648`) breaks 「…어떻게 되나」/「요?」, stranding 「요?」. Awkward-but-readable → P2, not blocking. |
| I | Naming & organization | PASS | Frame name = `[auto] <screen> — <run-id>` exact; single state correctly omits state segment; every node carries role + token bracket (no `Frame 12` defaults); icon button has aria-label; text nodes carry type tokens; tokens bound via local variable collection mirroring socarframe. |

## Issues (prioritized, each with a concrete fix)
- **P2 (should-fix):** FAQ row 1 text node `34:648`「사고가 나면 보험 처리는 어떻게 되나요?」 wraps to 「…어떻게 되나」 / 「요?」, stranding the syllable 「요?」 on a widow line — the container (268px wide, chevron takes the rest) is just barely too narrow for one line. Fix: shorten copy to fit one line, e.g. 「사고 나면 보험 처리는 어떻게 되나요?」 (drop 「가」), **or** author an intentional `\n` at a 구 boundary so it breaks as 「사고가 나면 보험 처리는」 / 「어떻게 되나요?」, **or** reduce the chevron column / row horizontal padding so the full phrase fits. Keep `word-break:keep-all` so 조사 never strands.
- **P3 (nice-to-have):** Tips body `34:216` wraps 「…신고해 주세요. 2차」 / 「사고를 막는 것이 가장 먼저예요.」 — splits 「2차」 from 「사고」 across lines. Readable and at a sentence boundary, but for a cleaner meaning-unit break, author `\n` after 「주세요.」 so the second sentence starts its own line.
- **P3 (nice-to-have):** 차량 정보 행 — 번호판 라벨 「차량번호」 (`34:540`) and value 「12가 3456」 sit on the same row as the thumbnail; fine as-is, but consider `text-secondary`→ confirm label color reads as secondary vs the title3 value for cleaner two-tier emphasis (already differentiated by weight; minor).

## What's good
- Token discipline is excellent: every color/spacing/radius is a **bound local variable** (verified via `get_variable_defs`) with values matching socarframe exactly, and radius px matches its token name — the most common silent defect is absent.
- Emphasis is textbook "One primary action": the red fill CTA owns the visual hierarchy, brand blue is correctly demoted to the FAQ text link, and the 「이용 중」 Tag was deliberately recolored to blue so red stays meaningful.
- Naming/organization is fully traceable per `figma-conventions.md` — frame prefix + run-id, role + token-bracket layer names, aria-label on the icon button, type token on every text node.

VERDICT: PASS
