# Harness shakedown — test run findings & improvements

First end-to-end run of the harness, used to harden it. Recorded here so the evolution is auditable.

## The run

- **Request:** `tests/01-return-complete.md` — 쏘카 "반납 완료" success screen.
- **Invocation:** `claude -p "$(cat tests/.run-01.txt)" --permission-mode bypassPermissions` from the
  repo root (headless), exit 0.
- **Result:** real Figma frame built — `runs/20260620-070646-return-complete/` (`00-request` →
  `05-verify`, screenshot in `artifacts/result.png`). Verify: **PASS, 7/7** rubric.

## What worked (keep)

- The five-stage artifact hand-off worked cleanly headlessly — each stage read its predecessors and
  wrote exactly one artifact; no shared-context coupling.
- `socar-clarify` returned `READY` on round 1 for a well-specified request (no user prompt needed —
  headless-safe), with strong SOCAR/socarframe default assumptions.
- `socar-context` did **real** Figma inspection and surfaced a decisive fact: **socarframe is not a
  bound Figma library** in the target file (only community kits), the page was empty, and there is
  **no documented Card component** — then routed implement to build from primitives with token values.
- `socar-plan` produced a complete, buildable spec (layout table, verbatim Korean copy with a price
  sanity-check, single-emphasis color strategy, WCAG-AA notes).
- `socar-implement` built faithfully and **logged its deviations honestly** rather than hiding them.
- `socar-verify` inspected the real screenshot + metadata and graded fairly.

## Findings → fixes applied

The agents faithfully followed the docs, so the defects were mostly **gaps in the design-system
docs** that turned into design gaps. All fixed:

| # | Finding (from the run) | Fix |
|---|------------------------|-----|
| 1 | **Radius tokens were undocumented.** Implement used the token `radius-350` for the button but applied **12px**, when `radius-350` = **14px**; and the card radius was flagged as "no token." | Added the full **radius scale** (`radius-100`…`radius-600`, `radius-circle`) with exact px to `spacing.md` (now "Spacing & Radius"), pulled from the published stylesheet. Cards default to `radius-300` (12px). Cross-referenced in README, plan, implement, verify, CLAUDE.md. |
| 2 | **No build-font policy.** SOCAR's UI font wasn't installed → fell back to Noto Sans KR → **SemiBold(600) silently became Medium(500)**, flattening hierarchy. | Added a **build-font policy** to `typography.md`: use **Pretendard** (Regular/Medium/SemiBold/Bold) unless the real SOCAR font is installed; never drop a weight. Wired into implement (set the font), verify (check it), and CLAUDE.md. |
| 3 | **No bound Figma variables.** Tokens were applied as raw values (`get_variable_defs` = `{}`), so intent was only traceable via layer names. | `socar-implement` now **materializes a local `socarframe` variable collection** (at least the colors it uses) and binds to it when the library isn't bound. Verify credits bound variables. |
| 4 | **Awkward Korean line-wrap** on the hero subline (word split across two lines). | `socar-plan` now keeps multi-line strings short / word-balanced (`break-keep`), not split mid-word. |
| 5 | Headless `claude -p` printed a `no stdin data` warning. | `tests/README.md` documents redirecting `< /dev/null`. |

## Still open (intentional / future)

- **socarframe as a real Figma library.** The cleanest long-term fix is to publish socarframe (or run
  a one-time bootstrap that materializes *all* tokens + components as Figma variables/components in the
  team file) so implement inserts instances instead of rebuilding. Fix #3 is the lightweight interim.
- **Card / SummaryCard component** is absent from the published design system; screens needing cards
  build them from primitives (`white` surface + `radius-300` + spacing tokens) until the DS adds one.
