---
run: 20260620-101653-home-main
stage: verify
verdict: PASS
score: 9/9 rubric items passing
---
# Verify report

## Looked at
- Frame A: `[auto] 홈(메인) · 예약 있음 — 20260620-101653-home-main` (node 34:44) — screenshot captured: yes
- Frame B: `[auto] 홈(메인) · 예약 없음 — 20260620-101653-home-main` (node 34:926) — screenshot captured: yes
- Section: `[auto] 홈(메인) — 20260620-101653-home-main` (node 34:43) — metadata + design context inspected
- Variable bindings read via `get_variable_defs(34:44)`; type/weight read via `get_design_context` on cards 34:585 / 34:1124 and banner 34:764.

## Rubric
| # | Criterion | Result | Note |
|---|-----------|--------|------|
| A | Plan coverage | PASS | All sections 0–6 present in plan order in both states; §3 correctly swaps 진행 중 카드 ↔ 유도 카드. Notification dot shown in 예약 있음 (34:132), absent in 예약 없음 — matches `## States`. |
| B | Component correctness | PASS | socarframe Icon Library / ActionButton not bound in file, so gaps built from correct primitives and named after the real components/variants (ActionButton · outlined|fill/primary/small, Tag · capsule/small, IconButton). Small CTAs correctly map to title4 + radius-250. |
| C | Token usage | PASS | All fills/strokes/padding/radius bound to the file's Color/Spacing/Radius vars (semantic names mirror socarframe). Radius↔px all correct: cards radius-300=12, banner radius-400=16, small btn radius-250=10, thumb radius-200=8. Font policy honored — Gothic A1 with true SemiBold(600); no 600→500 drop (Tag/모델명/타이틀/CTA all Gothic_A1:SemiBold). |
| D | Layout & alignment | PASS | 16px (spacing-400) side insets throughout; on the 4px grid; auto-layout sections; fixed TopAppBar/BottomNav, scroll body between; no overlaps or clipping in either render. |
| E | Copy & voice | PASS | Copy is verbatim to plan, natural SOCAR Korean, no placeholder/lorem. 예약 있음 and 예약 없음 copy both correct. |
| F | Accessibility | PASS | Touch targets ≥44 (알림 IconButton 44×44, BottomNav tabs 56×44, CTA buttons 44/48). 알림 carries [aria-label=알림]. text-secondary placeholder on white and text-strong key info give sane contrast; active tab uses fill icon + color (not color-only). |
| G | Polish | PASS | Single clear hero (검색 박스) + one fill/primary action per state (스마트키 / 주변 차량 찾기); 예약 상세 correctly de-emphasized as outlined. Tidy hierarchy, consistent weak-tone secondary surfaces. |
| H | Line-break naturalness | PASS | Banner title authored `\n` at a 구 boundary ("신규 가입하면" / "첫 대여 30% 할인") — "할인" intact, no stranded josa. Empty-state sub fits one line at 296px. No mid-token splits, widows, or clipping in either screenshot. |
| I | Naming & organization | PASS | Frames `[auto] <screen> · <state> — <run-id>` with state segment (2 states); Section wrapper named without state segment; default leftmost, 80px gutter, no overlap with reference frame. Layers carry role + token brackets, text nodes carry type tokens, icons carry icon tokens, divider/spacer named. No default `Frame N` names. |

## Issues (prioritized, each with a concrete fix)
- **P3 (nice-to-have):** Empty-state medium ActionButton label "주변 차량 찾기" (node 34:1134) renders at `title2` (16px). The socarframe ActionButton **medium** size maps to `title3` (14px) per components-actions.md (and the plan asked for title4). Fix: set node 34:1134 type to `title3` (14px / 20px line / SemiBold) and rename it `label · title3` to match the component's size→type mapping. Purely a spec-consistency nit; reads fine visually.
- **P3 (nice-to-have):** Empty-state spacer between sub-copy and CTA is `spacer · spacing-100` (4px, node 34:1133) but its frame is sized 10×4, so the name implies a 4px spacer while the node carries an arbitrary 10px width. Fix: make it a full-width 0-height spacing-300 spacer (or rely on the card's auto-layout gap) so the gap before the primary CTA matches plan's "위 마진 spacing-300" and the name is truthful.
- **P3 (nice-to-have):** Vehicle thumbnail and banner illustration are icon-on-tint placeholders (no product imagery available to the plugin API) — plan explicitly allowed this. Swap to real assets when available; not a defect for this run.

## What's good
- Token discipline is excellent: every color/spacing/radius is bound to a real variable and the radius px all match their token names — the exact area verify most often catches, clean here.
- Font handling is the highlight — the reference frame's Noto Sans KR dropped SemiBold→Medium; this build deliberately switched to Gothic A1 specifically because it ships a true 600, preserving the 600/700/400 hierarchy. Correct call, documented.
- Naming/organization is fully traceable: roles + token brackets + type tokens + aria-label on the icon button, both states labeled, sectioned and placed per conventions — auditable without a bound library.

VERDICT: PASS
