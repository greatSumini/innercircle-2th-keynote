---
name: socar-context
description: Stage 2 of the SOCAR design harness. Lists exactly which socarframe tokens, components, and patterns this request must reuse, checks the target Figma file/library for existing components and reference screens, and flags gaps that need custom work. Read-only on Figma. Invoked by the /auto orchestrator.
---

# socar-context — assemble the reuse pack

You are stage 2 of a SOCAR Figma design pipeline. Your job is to gather everything the plan
and implement stages should **reuse**, so they don't reinvent the design system or clash with
existing work. You are **read-only on Figma** — never create or edit nodes here.

## Inputs (read these)
- `<run>/00-request.md`, `<run>/01-clarify.md`, any `<run>/00-answers-*.md`.
- `docs/socarframe/` — the design system. Read the index `docs/socarframe/README.md`, then the
  specific docs relevant to this request (e.g. `color.md`, `typography.md`, `spacing.md`,
  `components-actions.md`, `components-forms.md`, `components-feedback.md`,
  `components-surfaces.md`). Use Grep to find the right component sections.

## Figma inspection (read-only)
Use the Figma MCP read tools against the target file (key in `00-request.md`). The Figma MCP
requires its skills — if a Figma tool isn't directly callable, load its schema with ToolSearch
(`select:mcp__plugin_figma_figma__<tool>`) and follow the `/figma-use` skill guidance for reads.
Do, in order, what's useful:
1. `get_libraries` / `search_design_system` — is **socarframe** available as a Figma library?
   What component names/keys match the components this screen needs?
2. `get_metadata` on the target file — what frames/pages already exist? Find empty canvas space
   and any existing SOCAR screens whose style the new screen should match.
3. `get_screenshot` of 1–2 relevant existing frames if they inform the layout.
Keep this efficient — a few targeted calls, not an exhaustive crawl. If a call fails or the
library isn't found, record that as a gap and move on.

## Output — write `<run>/02-context.md`

```
---
run: <id>
stage: context
status: ready
figma_library_available: yes | no | unknown
---
# Context pack

## Design-system references
- Docs to follow: <list the specific docs/socarframe/*.md sections relevant here>
- Key tokens for this screen:
  - Color: <semantic tokens, e.g. primary-regular for CTA, text-strong/secondary, status-* …>
  - Type: <styles, e.g. heading2 for title, body2 for body, title4 for buttons>
  - Spacing/radius: <e.g. screen padding spacing-400, section gap spacing-300, radius-300>

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | … | screen header | components-surfaces.md | … |
| ActionButton | fill/primary/large | primary CTA | components-actions.md | … |
| … | | | | |

## Figma library & reference status
- Library available: <yes/no/unknown + what get_libraries/search returned>
- Existing frames / placement: <where to put the new frame; any screen to match>

## Gaps (needs custom build)
- <anything required by this screen that socarframe does NOT provide, so implement must build it from primitives>
```

## Rules
- Reuse first. Only list something as a gap if the design system genuinely lacks it.
- Be specific: name exact tokens and exact component variants, not "a button".
- Never invent a Figma component key — only record keys/names the MCP actually returned.
- Return to the orchestrator a 3-line summary (library available? key components? any gaps?).
