---
run: 20260620-101702-reserve-pay-confirm
stage: verify
verdict: PASS
score: 8/9 rubric items passing
---
# Verify report

## Looked at
- Frame: `[auto] 예약 확인 — 20260620-101702-reserve-pay-confirm` (node 34:2) — screenshot captured: yes
- Also inspected per-section: 예약 요약 (34:68), 요금 상세 (34:171), 할인 적용 (34:325),
  결제수단 (34:457), 약관 동의 (34:555), Bottom CTA (34:660) via screenshot + get_design_context;
  bound variables via get_variable_defs.
- Note: the first `get_screenshot` URL returned a stale/cached render of an unrelated frame
  (a "도움이 필요하신가요?" help screen). Re-fetching returned the correct 예약 확인 render that
  matches the metadata structure. The build at 34:2 is the reservation-confirm screen as planned.

## Rubric
| # | Criterion | Result | Note |
|---|-----------|--------|------|
| A | Plan coverage | PASS | All 7 sections present and in plan order: TopAppBar → 예약 요약 → 요금 상세 → 할인 적용 → 결제수단 → 약관 동의 → Bottom CTA. |
| B | Component correctness | PASS | No bound DS library in file; gaps built from correct primitives & named for their socarframe role/variant (`ActionButton · fill/primary/large`, `Tag · soft/positive`, `Input · filled`, `Checkbox · checked`, `TextButton · text/primary`, `Accordion · single Trigger`). |
| C | Token usage | PASS | Colors/radii bound to file variables (`var(--text-strong)`, `var(--status-positive-regular)`, `var(--primary-regular)`, etc.). Radii match names: cards radius-300=12, CTA radius-350=14, info box radius-200=8, input radius-250=10, Tag/Checkbox radius-150=6. Font policy honored — SemiBold roles promoted to Bold(700), not dropped to Medium(500). |
| D | Layout & alignment | PASS | 360 width, 16px side pad, 12px card gap, on-grid; all amounts right-aligned in their value column; no overlap/clipping; sticky bar pinned with top divider + 24px home-indicator clearance. |
| E | Copy & voice | PASS | Copy verbatim to plan; natural, warm SOCAR Korean; no lorem/placeholder. 안심 tone reads (할인 in green, 안내 info box). |
| F | Accessibility | PASS | Back/약관/쿠폰 icon-only controls carry aria-labels; back button 44×44 hit area; 최종 결제 금액 & CTA highest-contrast (text-strong on white / white on #0078FF). |
| G | Polish | PASS | Single primary action (blue CTA) is the only saturated element; clean hierarchy; 금액 가독성 strong (heading2 24px for 최종 결제 금액, heading3 22px for 합계). |
| H | Line-break naturalness | FAIL | Accordion 안내 (34:185) wraps mid-word: line 1 ends "…금액이에요. 실" / line 2 begins "제 주행거리에…" — splits 실제 and strands a single syllable. Every other multi-line/long block is single-line and clean. |
| I | Naming & organization | PASS | Frame name = `[auto] <screen> — <run-id>`; single state, no segment (correct); placed x=7800 with no overlap; layers carry role + type-token + `[token=…]`/`[aria-label=…]`. Minor: balance node `spacer · 44` uses a literal px, not a spacing token (it's a 44px hit-area mirror — acceptable, noted P3). |

## Issues (prioritized, each with a concrete fix)
- **P2 (should-fix):** Accordion 안내 text (node **34:185**, 요금 상세 card) breaks the word **실제**
  across lines ("…예상한 금액이에요. 실" / "제 주행거리에 따라 반납 시 정산돼요."). A word split mid-token
  is the exact H failure mode. **Fix:** author a hard break — set the string to
  `"주행거리 1km당 170원으로 예상한 금액이에요.\n실제 주행거리에 따라 반납 시 정산돼요."` so line 2 starts at
  the natural 구 boundary "실제". (Alternatively, set this text node's line-break/word-break to
  `keep-all`/break-keep so Korean never splits inside an 어절. Authored `\n` is preferred since it
  also pins the intended two-line shape.)
- **P3 (nice-to-have):** Font fidelity gap — Pretendard/SOCAR UI font not installed, so SemiBold(600)
  title roles and Bold(700) heading roles both render as Noto Sans KR Bold; the 600-vs-700 tier the
  type scale intends is not visible (size still separates them). Correctly handled per policy
  (promoted, not dropped). **Fix when possible:** install Pretendard (or the real SOCAR font) and
  rebind title1–4/caption1 to weight 600 to restore the tier. No re-layout needed.
- **P3 (nice-to-have):** Accordion is shown **expanded** (plan default = collapsed) to make the 안내
  copy reviewable in a static frame. Intentional, flagged by implement. **Fix (optional):** if the
  delivered artifact should mirror the true default, collapse 34:184 and rotate the chevron back to
  down/right; otherwise leave for reviewability. (Becomes moot once the P2 break fix is applied with
  the accordion expanded.)
- **P3 (nice-to-have):** Balance spacer node named `spacer · 44` (34:37) uses a literal px instead of
  a `spacing-<token>`. It mirrors the 44px back-button hit area, so a token doesn't apply cleanly —
  acceptable, but rename to e.g. `spacer · 44 (balance)` for clarity if touched.

## What's good
- Token discipline is excellent: real Figma variables are bound (not raw hex/px), radii match their
  token names exactly, and every layer is traceable by name — this build would audit cleanly even
  without the source library.
- 금액 가독성 / 안심 tone landed: amounts are uniformly right-aligned, 최종 결제 금액 is the strongest
  type on screen (heading2), discounts and the coupon Tag are positive-green, and the single blue CTA
  owns the only strong emphasis.
- Copy is verbatim-faithful to the plan and reads as natural SOCAR Korean, with full a11y labeling on
  every icon-only control.

VERDICT: PASS
