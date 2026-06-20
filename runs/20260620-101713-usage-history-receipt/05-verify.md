---
run: 20260620-101713-usage-history-receipt
stage: verify
verdict: PASS
score: 9/9 rubric items passing
---
# Verify report

## Looked at
- Frame: `[auto] 이용 내역 · 기본 — 20260620-101713-usage-history-receipt` (node 34:106) — screenshot captured: yes
- Frame: `[auto] 이용 내역 · 빈 상태 — …` (node 34:441) — screenshot captured: yes (+ zoom of 34:445)
- Frame: `[auto] 이용 내역 · 영수증 상세 — …` (node 34:728) — screenshot captured: yes (+ zoom of 결제 영수증 card 34:888)
- Section wrapper: `[auto] 이용 내역 — …` (node 34:1154), 3 children — screenshot captured: yes
- Also pulled: get_metadata (all 3 frames), get_variable_defs (3 frames), read-only font/weight/radius/fill/wrap audit of 21 key nodes, page-level overlap check.

## Rubric
| # | Criterion | Result | Note |
|---|-----------|--------|------|
| A | Plan coverage | PASS | Every plan section present in plan order across 3 frames: list (caption→월 헤더→4 cards w/ section gaps→bottom pad), empty (badge→title→desc→CTA), receipt (이용 요약→결제 영수증 accordion→총 결제 금액→결제 정보→문의 TextButton→하단 CTA). |
| B | Component correctness | PASS | TopAppBar, BasicBackButton IconButton, ActionButton fill/primary/large + outlined/secondary/large, Tag soft/neutral/small, Accordion single (대여 펼침/나머지 접힘), Divider, TextButton — all built from correct primitives with variants encoded in names. Amounts right-aligned, end-line consistent. |
| C | Token usage | PASS | Colors bound to `socarframe` variable collection (get_variable_defs returns text-strong/primary/secondary, white, status-positive-regular #04ca81, divider/border-regular, primary-regular, background-regular). Radius px matches token (cards=12=radius-300, buttons=14=radius-350, badge/tag=radius-circle). Type sizes/line-heights match typography.md exactly; SemiBold(600)/Bold(700) preserved, not downgraded. |
| D | Layout & alignment | PASS | On 4px grid, spacing via named spacer frames (spacing-200/300/400/500/150/800), 16px side padding throughout, auto-layout rows with space-between. No overlaps/clipping. Section doesn't overlap neighbors (smartkey ends 10440, license starts 13160; section 11360–12680). |
| E | Copy & voice | PASS | Verbatim plan copy, natural SOCAR Korean. Amounts use 1,000-comma + 원; discount uses U+2212 minus + green. Sum reconciles: 33,000+9,300+5,500−5,000 = 42,800 (matches 총 결제 금액). No placeholder/lorem. |
| F | Accessibility | PASS | BasicBackButton 44pt with `[aria-label=뒤로가기]`; list card tap targets 100px (≥72 plan min); accordion triggers 48px; text-strong on white = strong contrast, text-secondary meta legible; discount green paired with `−` so color isn't sole signal. |
| G | Polish | PASS | Single visual peak = 총 결제 금액 heading3/Bold, cleanly separated by divider. Intended hierarchy holds: total > item amounts(title3) > labels(body3/4); inquiry TextButton + outlined CTA correctly de-emphasized vs primary-fill empty-state CTA. Clean fit-and-finish. |
| H | Line-break naturalness | PASS | All datetime/zone/amount strings stay single-line. One blemish: empty-state desc (34:453) wraps "…확인할 수 / 있어요." stranding "있어요." as a one-word widow and splitting the verb phrase 확인할 수 있어요. Awkward-but-readable → P3, not blocking. |
| I | Naming & organization | PASS | Frames `[auto] <screen> · <state> — <run-id>` (· 기본/· 빈 상태/· 영수증 상세); section wrapper stem-named, no state segment; layers carry role + type token + `[token=value]` brackets; icons named by token (icon-chevron-right-line, icon-file-text-line, icon-arrow-left-line, icon-credit-card-line); spacers `spacer · spacing-*`; Divider `[stroke=divider-regular]`; variable collection is `socarframe`. Traceable end to end. |

## Issues (prioritized, each with a concrete fix)
- **P3 (nice-to-have):** Empty-state description (node 34:453) wraps as "…확인할 수 / 있어요.", stranding "있어요." as a one-word widow and breaking the phrase 확인할 수 있어요 across lines. Fix: author an explicit `\n` on a meaning boundary so the verb phrase stays whole — set characters to `첫 쏘카를 이용하면\n여기에서 영수증을 확인할 수 있어요.` (keep textAutoResize=HEIGHT, width 304, centered). This yields two balanced, naturally-broken lines.
- **P3 (nice-to-have):** Corner radius is applied by raw value (12/14/40), not bound to a `radius/*` variable — token intent survives only via the layer-name bracket. Acceptable per conventions (color binding is the required minimum, and it's present), but binding `radius/radius-300` and `radius/radius-350` to the card/button corners would make radius edits global and fully traceable like the colors already are.

## What's good
- Number legibility — the stated #1 priority — is nailed: amounts are right-aligned on a consistent end line, comma-grouped with 원, and 총 결제 금액 (heading3/Bold) is an unmistakable single visual peak separated by a divider.
- Design-system fidelity is high: colors bound to the `socarframe` collection, every radius px matches its token name, and Gothic A1 preserves the full SemiBold(600)/Bold(700)/Regular(400) weight contrast the plan demands — a justified, well-documented substitution for un-installed Pretendard.
- Naming/organization is exemplary: frames, section wrapper, layers, icons, spacers, and dividers all follow `figma-conventions.md`, making the build fully auditable without a bound library.

Judged deviations fairly: (1) Gothic A1 instead of Pretendard is the right call — it keeps SemiBold, which Noto Sans KR would have dropped; weights verified 600/700/400 intact. (2) Empty badge gray-200 vs gray-100 is correct — gray-100 equals background-regular and would render invisible; badge now reads clearly. (3) Bottom CTA as last child of a hugging wrapper (not absolutely pinned) is visually equivalent in a static mock; renders correctly with top divider.

VERDICT: PASS
