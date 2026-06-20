> Source: https://socarframe.socar.kr/development/foundation/Spacing
> Radius scale derived from the published SOCARFRAME stylesheet (`rounded-radius-*` utilities).

# Spacing & Radius

The SOCAR Frame spacing scale — named spacing tokens with their exact px and base-unit multiplier values — plus the corner-radius scale.

**Base unit: 1 unit = 4px.** Every token is a multiple of this 4px base unit.

| Token | px | Multiplier |
|---|---|---|
| `spacing-000` | 0px | 0x |
| `spacing-25` | 1px | 0.25x |
| `spacing-50` | 2px | 0.50x |
| `spacing-100` | 4px | 1x |
| `spacing-150` | 6px | 1.50x |
| `spacing-200` | 8px | 2x |
| `spacing-250` | 10px | 2.50x |
| `spacing-300` | 12px | 3x |
| `spacing-350` | 14px | 3.50x |
| `spacing-400` | 16px | 4x |
| `spacing-450` | 18px | 4.50x |
| `spacing-500` | 20px | 5x |
| `spacing-550` | 22px | 5.50x |
| `spacing-600` | 24px | 6x |
| `spacing-650` | 26px | 6.50x |
| `spacing-700` | 28px | 7x |
| `spacing-750` | 30px | 7.50x |
| `spacing-800` | 32px | 8x |
| `spacing-900` | 36px | 9x |
| `spacing-1000` | 40px | 10x |

## How to use

Use these tokens by name for all spacing decisions — padding, margins, and gaps — so layouts stay on the 4px base grid and remain consistent across screens.

- **Component padding** — apply a spacing token for inner padding of buttons, cards, and inputs; smaller tokens for tight controls, larger tokens for roomier containers.
- **Gaps between elements** — use a token for the gap between adjacent items in a list, row, or stack.
- **Gaps between sections** — use a larger token to separate distinct content sections on a screen.

Prefer adjacent steps on the scale for related spacing, and reserve the larger tokens for higher-level layout separation.

## Radius scale

Corner-radius tokens. Use these **by name** — never an arbitrary radius. (Values transcribed
from the SOCARFRAME `rounded-radius-*` utility classes.)

| Token | px |
|---|---|
| `radius-100` | 4px |
| `radius-150` | 6px |
| `radius-200` | 8px |
| `radius-250` | 10px |
| `radius-300` | 12px |
| `radius-350` | 14px |
| `radius-400` | 16px |
| `radius-500` | 20px |
| `radius-600` | 24px |
| `radius-circle` | 50% (pill / full circle) |

**How to use**

- **Cards / surfaces / summary containers** → `radius-300` (12px) is the default surface radius.
  Larger cards or sheets may use `radius-400` (16px). Use one radius consistently per surface type.
- **Buttons** follow the ActionButton size mapping — `large` → `radius-350` (14px), `medium` →
  `radius-300` (12px), `small` → `radius-250` (10px), `xSmall` → `radius-200` (8px). See
  [components-actions.md](./components-actions.md).
- **Pills / avatars / fully-rounded chips** → `radius-circle` (50%).
- Match the exact px to the token name — e.g. `radius-350` is **14px, not 12px**. Mixing them up
  is a common, easy-to-miss defect the verify stage checks for.
