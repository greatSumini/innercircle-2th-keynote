# CLAUDE.md

SOCAR Figma design harness. Given a request to design a SOCAR app screen, it produces a
high-quality Figma design built with the **socarframe** design system, via a five-stage
sub-agent pipeline orchestrated by the `/auto` skill.

## How to use

```
/auto 쏘카 앱의 <화면> 디자인해줘   # e.g. "반납 완료 화면", "쿠폰함", "예약 상세"
```

`/auto` creates a run folder, then runs **clarify → context → plan → implement → verify**,
asking you questions only when something is genuinely blocking, and finishes with a Figma link
and a summary. To inspect or resume reasoning, read the artifacts in `runs/<id>/`.

## Layout

```
.claude/skills/auto/SKILL.md     # orchestrator (the /auto skill)
.claude/agents/socar-*.md        # the 5 stage sub-agents
docs/ARCHITECTURE.md             # the harness contract — read this to understand the flow
docs/socarframe/                 # the design-system style guide (read by every stage)
  README.md                      #   index — start here
  color.md typography.md spacing.md icons.md principles.md
  components-actions.md components-forms.md components-feedback.md components-surfaces.md
runs/<id>/                       # per-run artifacts (00-request … 05-verify)
tools/socarframe_scrape.py       # re-sync docs/socarframe from socarframe.socar.kr
tests/                           # sample design requests to exercise the harness
```

## The pipeline (one writer per artifact, files are the hand-off)

| Stage | Agent | Artifact | Role |
|-------|-------|----------|------|
| 1 | `socar-clarify` | `01-clarify.md` | Understand the request; ask only blocking questions. |
| 2 | `socar-context` | `02-context.md` | List the socarframe tokens/components/screens to reuse. |
| 3 | `socar-plan` | `03-plan.md` | Write the design spec (layout, copy, color, components, states). |
| 4 | `socar-implement` | `04-implement.md` | Build it in Figma via Figma MCP + figma skills. |
| 5 | `socar-verify` | `05-verify.md` | Inspect the result; score it; list fixes; PASS/REVISE. |

The clarify loop (ask user, re-run clarify) and the verify→implement revise loop are owned by
the orchestrator and are bounded (clarify ≤3 rounds, revise ≤2 cycles). See
`docs/ARCHITECTURE.md` for the full contract.

## Working rules for this repo

- **Design-system first.** Always use socarframe **semantic tokens and components by name**
  (`primary-regular`, `text-secondary`, `spacing-400`, `radius-300`, `heading2`,
  `ActionButton fill/primary`). Raw hex/px is a defect the verify stage flags. Match radius px to
  its token (`radius-350`=14px, `radius-300`=12px). Build Figma text in **Pretendard** (full weight
  set) unless the real SOCAR font is installed — never drop SemiBold(600) to Medium(500). The
  source of truth is `docs/socarframe/`.
- **Mobile app screens.** SOCAR (쏘카) is a Korean car-sharing super-app; designs are mobile
  portrait unless stated otherwise. Copy is Korean, in SOCAR's clear/warm/concise voice.
- **Default Figma target:** file key `VuBHVaAnA5ORacxMZ9zcH8`
  (https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled). A request may override it
  with another Figma URL.
- **Figma MCP needs its skills.** Before calling Figma write/JS tools, load `/figma-use` (and
  `/figma-generate-design` for a full screen). The implement/context/verify agents already know
  this; honor it if you touch Figma directly.
- **Artifacts are the interface.** Sub-agents can't see each other's context — everything passes
  through `runs/<id>/`. One agent writes one artifact; never edit another stage's file.
- **Bound every loop and report honestly.** If verify still flags issues after the revise cap,
  say so with specifics rather than claiming success.

## Regenerating the design-system docs

The site is a client-rendered Docusaurus SPA, so `tools/socarframe_scrape.py` renders pages
with headless Chrome (`/Applications/Google Chrome.app`) and converts them to Markdown:

```
python3 tools/socarframe_scrape.py --all      # → /tmp/sf_raw/*.md
# then regenerate docs/socarframe/*.md from the raw files
```
