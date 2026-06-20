# Harness Architecture — SOCAR Figma Design Agent

A Claude Code harness that turns a natural-language request ("design the SOCAR app's
new ___ screen") into a high-quality Figma design built with the **socarframe** design
system. It is triggered by the **`/auto`** skill, which orchestrates five sub-agents that
hand structured artifacts to one another.

```
user ──/auto "<design request>"──▶  auto (orchestrator skill, runs in main context)
                                      │
        ┌─────────────────────────────┼──────────────────────────────────────────┐
        ▼            ▼                 ▼              ▼                ▼            │
   socar-clarify  socar-context   socar-plan   socar-implement   socar-verify     │
        │   ▲         │               │              │                │           │
   01-clarify   02-context       03-plan        04-implement     05-verify        │
        │   │                                                          │           │
        └───┘ (loop: ask user via AskUserQuestion, re-run clarify)     │           │
                                              (loop back if critical)──┘           │
                                                                                   ▼
                                                                  Figma file + run/ artifacts
```

## Components

| Path | Role |
|------|------|
| `.claude/skills/auto/SKILL.md` | **Orchestrator.** Loaded into the main context by `/auto`. Creates the run directory, drives the five stages, owns the user-facing clarify loop, decides retries, and reports the result. |
| `.claude/agents/socar-clarify.md` | Understand the request; surface blocking questions. Idempotent across the ask→answer loop. |
| `.claude/agents/socar-context.md` | List the socarframe tokens, components, patterns, and existing screens this request must reuse. |
| `.claude/agents/socar-plan.md` | Write the design spec: layout, copywriting, color/emphasis, components, states, a11y. |
| `.claude/agents/socar-implement.md` | Build the design in Figma via the Figma MCP + figma skills. |
| `.claude/agents/socar-verify.md` | Inspect the built frame in Figma; score it against plan + design system; list fixes. |
| `docs/socarframe/` | The design-system knowledge base (the "style guide"). Read by every stage. |
| `docs/figma-conventions.md` | Figma **naming & organization** conventions — frame/layer/component/variable names, multi-state frames, canvas placement. Read by plan, implement, verify. |
| `runs/<run-id>/` | Per-run working directory; holds the numbered artifacts below. |
| `tools/socarframe_scrape.py` | Re-syncs `docs/socarframe/` from socarframe.socar.kr (headless-Chrome scraper). |
| `tests/` | Realistic design requests used to exercise the harness. |

## The artifact contract

Sub-agents run in isolated contexts and cannot see each other's conversation. They
communicate **only through files** in `runs/<run-id>/`. The orchestrator passes the run
directory path to each agent; each agent reads its inputs and writes exactly one numbered
artifact. This leaves a fully auditable trail.

| Artifact | Written by | Inputs it reads | Purpose |
|----------|-----------|-----------------|---------|
| `00-request.md` | orchestrator | — | Raw user request + run metadata (Figma target, date). |
| `00-answers-NN.md` | orchestrator | — | User's answers to clarify questions (one file per round). |
| `01-clarify.md` | socar-clarify | `00-*` + docs | Understood spec, assumptions, and `STATUS: READY \| NEEDS_INPUT` with questions. |
| `02-context.md` | socar-context | `00-*`, `01` + docs + Figma | Context pack: reusable components (with keys), tokens, reference screens. |
| `03-plan.md` | socar-plan | `00-02` + docs | The design spec / blueprint. |
| `04-implement.md` | socar-implement | `02`, `03` + Figma | What was built: frame name, node IDs, URL, any deviations. |
| `05-verify.md` | socar-verify | `03`, `04` + Figma | Per-criterion verdict + prioritized fix list + `VERDICT: PASS \| REVISE`. |

Every artifact starts with a small YAML-ish front block (`run`, `stage`, `status`) so the
orchestrator can parse state with a quick `grep` without re-reading the whole file.

## Orchestration flow (what `/auto` does)

1. **Init** — make `runs/<YYYYMMDD-HHMMSS>-<slug>/`, write `00-request.md` (includes the
   default Figma target file).
2. **Clarify loop** — spawn `socar-clarify`. If it returns `NEEDS_INPUT`, ask the user with
   `AskUserQuestion`, save answers to `00-answers-NN.md`, and re-spawn `socar-clarify`.
   Repeat until `READY` (hard cap: 3 rounds, then proceed on stated assumptions).
3. **Context** — spawn `socar-context` → `02-context.md`.
4. **Plan** — spawn `socar-plan` → `03-plan.md`.
5. **Implement** — spawn `socar-implement` → builds in Figma → `04-implement.md`.
6. **Verify** — spawn `socar-verify` → `05-verify.md`. If `VERDICT: REVISE` and the issues
   are fixable, re-spawn `socar-implement` with the fix list (cap: 2 revise cycles).
7. **Report** — summarize to the user: Figma frame link, what was built, residual notes.

## Design principles

- **One writer per artifact.** Each stage owns exactly one file; no stage edits another's.
- **Least context, most signal.** Agents read only the artifacts + doc sections they need.
- **Clarify is conservative.** Ask only blocking questions, batched (≤4), never trivia the
  SOCAR domain or design system already answers.
- **Design-system first.** Plan and implement reference socarframe tokens/components by
  name; raw hex/px values are a smell flagged in verify.
- **Idempotent re-entry.** clarify and implement must behave correctly whether run fresh or
  re-run with new input (answers / fix list).
- **Bounded loops.** Both the clarify and the verify→implement loops have hard caps so a run
  always terminates.

## Default Figma target

Designs are created in the team file:
`https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled` (file key
`VuBHVaAnA5ORacxMZ9zcH8`). The orchestrator records this in `00-request.md`; a request may
override it by supplying a different Figma URL.
