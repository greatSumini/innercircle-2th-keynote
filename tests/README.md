# Harness test set

Realistic SOCAR new-screen design requests for exercising the `/auto` harness. Each file has a
`PROMPT` (the request to feed `/auto`) and `EXPECT` notes (what good behavior looks like) so a
run can be judged.

| # | File | Specificity | Exercises |
|---|------|-------------|-----------|
| 01 | `01-return-complete.md` | High (fully specified) | Happy path; clarify should return READY round 1 — safe for headless `claude -p`. |
| 02 | `02-coupon-wallet.md` | Medium | Some assumptions; clarify may ask 1–2 questions or proceed on assumptions. |
| 03 | `03-payment-ambiguous.md` | Low (ambiguous) | The clarify → ask-user loop (run interactively). |

## Run interactively
```
/auto <paste the PROMPT block>
```

## Run headless (deterministic; use a fully-specified prompt like 01)
```
claude -p "/auto $(sed -n '/^PROMPT$/,/^EXPECT$/p' tests/01-return-complete.md)" \
  --permission-mode acceptEdits
```
Headless runs cannot answer clarify questions, so only use prompts specified well enough that
clarify returns `READY` on the first pass (01). Inspect the result in `runs/<id>/` and Figma.
