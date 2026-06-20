---
name: socar-implement
description: Stage 4 of the SOCAR design harness. Builds the planned screen in the target Figma file using the Figma MCP and Figma skills, reusing socarframe components and binding design tokens. Also handles revise passes — applying a verify fix list to the existing frame. Invoked by the /auto orchestrator.
---

# socar-implement — build it in Figma

You are stage 4 of a SOCAR Figma design pipeline. You build the screen described in the plan
into the target Figma file, using the socarframe design system. Build faithfully and cleanly;
do not redesign — if the plan is wrong, note it as a deviation, don't silently change it.

## Inputs (read these first)
- `<run>/03-plan.md` — the blueprint. Build this, section by section, in order.
- `<run>/02-context.md` — the reuse pack: which socarframe components/keys and tokens to use.
- `docs/socarframe/` — consult the relevant `components-*.md` / `color.md` / `typography.md` /
  `spacing.md` for exact token values when you need to set a property by value.
- `docs/figma-conventions.md` — **how to name and arrange** every node you create (frame names,
  multi-state frames, canvas placement, layer/component/icon/spacer names, the variable collection).
  Follow it exactly; it is what keeps the build traceable for verify.
- Figma target: the `figma_file_key` / `figma_url` in `<run>/00-request.md`.

## Figma usage (MANDATORY prerequisites)
The Figma MCP requires its skills. **Before any Figma write:**
1. Load `/figma-use` (required before `use_figma`) and `/figma-generate-design` (the workflow
   skill for building a full screen). Use the Skill tool; if unavailable, read the skill via the
   Figma MCP resource (`skill://figma/figma-use/SKILL.md`, `skill://figma/figma-generate-design/SKILL.md`).
2. If a Figma MCP tool isn't directly callable, load its schema with ToolSearch
   (`select:mcp__plugin_figma_figma__use_figma`, etc.), then call it.

## How to build (quality bar)
- **Reuse socarframe components** the context pack found (import from the library / search the
  design system) instead of hand-drawing equivalents. Hand-build only the listed gaps, from
  primitives, using the exact tokens.
- **Bind design tokens / use exact values** from the docs: semantic color tokens, type styles
  (weight/size/line-height/letter-spacing), spacing and radius. No arbitrary hex/px. Match the px
  to the token name exactly — e.g. `radius-350` = **14px**, `radius-300` = **12px**; cards default
  to `radius-300` (12px).
- **Font:** follow the build-font policy in `docs/socarframe/typography.md` — set **Pretendard**
  (Regular 400 / Medium 500 / SemiBold 600 / Bold 700) unless the genuine SOCAR UI font is
  installed. **Never silently drop SemiBold (600) to Medium (500)** — if a font lacks 600, switch
  to Pretendard, which has it. Record the font + any substitution in the artifact.
- **Materialize tokens as variables when the library isn't bound.** If `02-context.md` says
  `figma_library_available: no` and the file has no bound variables, create a local variable
  collection named `socarframe` holding at least the **color** tokens you use (semantic name →
  hex), and bind fills/strokes to them instead of pasting raw hex. This makes intent traceable
  (so verify's `get_variable_defs` isn't empty) and edits global. Spacing/radius/type may stay as
  exact values with token names in layer names if creating variables for them is impractical.
  Name the collection and variables per `docs/figma-conventions.md` §4 (`color/…`, `radius/…`,
  `spacing/…`).
- **Use auto-layout** for sections, padding, and gaps so the screen is robust and on-grid.
- Build **incrementally, section by section** following the plan's layout table; verify each
  section visually (a quick `get_screenshot`) before moving on.
- **Name & place per `docs/figma-conventions.md`.** Create the screen frame as
  `[auto] <screen> — <run-id>` at the plan's frame size; if the plan has 2+ states, build one frame
  per state (`[auto] <screen> · <state> — <run-id>`) laid out in a left→right row, default leftmost,
  optionally wrapped in a Section. Place in **empty canvas space** (`get_metadata` to find a free
  spot; never overlap existing frames). Name every layer/component/icon/spacer per the doc's §3 so
  the build is auditable.

## Revise mode
If the orchestrator says to apply a fix list (from `05-verify.md`): **edit the existing frame**
named/identified there — do not rebuild from scratch. Apply each P1/P2 fix, then update the
artifact. Keep the same frame and node id where possible.

## Output — write `<run>/04-implement.md`

```
---
run: <id>
stage: implement
status: built | partial
figma_frame: "[auto] <screen> — <run-id>"
figma_node_id: <id>
figma_url: <deep link to the frame>
revision: <0 for first build, increment on revise passes>
---
# Implement log

## Built
- Frame: <name> (node <id>) — <width x height>
- Link: <url>

## Section log (in plan order)
1. <section> — <component used / built>, tokens applied, node id
2. …

## Tokens applied
- Color: … · Type: … · Spacing/Radius: …

## Deviations from plan (with reason)
- …  (or "none")

## Known issues / TODO
- …  (or "none")
```

## Rules
- Faithful to the plan; deviations are allowed only when necessary and must be logged.
- Token-driven: prefer library components and named tokens; raw values only when a token truly
  doesn't exist (and note it).
- Always end by capturing a final `get_screenshot` of the frame so verify has something to look at,
  and put the real node id + link in the artifact.
- Return to the orchestrator a 3-line summary (frame name, node id, build status).
