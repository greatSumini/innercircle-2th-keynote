> Source: https://socarframe.socar.kr/development/foundation/Typography

# Typography

The SOCAR Frame type scale — every text style with its token name and exact values for use in Figma.

The base font is SOCAR's Korean UI font. All styles below are defined on that font.

### Build font (Figma)

When building in Figma, the real SOCAR UI font is often not installed. **Use `Pretendard` as the
standard substitute** — it is a Korean UI sans with the full weight set this scale needs, so the
weights map cleanly:

| Role in this scale | Weight | Pretendard family |
|---|---|---|
| Bold | 700 | Pretendard Bold |
| Semi Bold | 600 | Pretendard SemiBold |
| Medium | 500 | Pretendard Medium |
| Regular | 400 | Pretendard Regular |

Rules:
- **Never silently drop a weight.** If a font lacks Semi Bold (600), do **not** fall back to
  Medium (500) — switch to Pretendard, which has 600. Preserving the 600 vs 700 vs 400 contrast is
  what makes the hierarchy read correctly.
- If the genuine SOCAR UI font *is* installed, prefer it; otherwise use Pretendard at the exact
  px / line-height / letter-spacing below.
- Record the font actually used (and any weight substitution) in the implement artifact so verify
  can check it.

| Style | Token | Font Weight | Font Size | Line-Height | Letter Spacing |
|---|---|---|---|---|---|
| Display 1 | `display1` | Bold (700) | 40px | 50px (1.25) | -0.6px |
| Display 2 | `display2` | Bold (700) | 36px | 44px (1.22) | -0.6px |
| Heading 1 | `heading1` | Bold (700) | 26px | 36px (1.38) | 0px |
| Heading 2 | `heading2` | Bold (700) | 24px | 34px (1.42) | 0px |
| Heading 3 | `heading3` | Bold (700) | 22px | 30px (1.36) | 0px |
| Title 1 | `title1` | Semi Bold (600) | 18px | 26px (1.44) | 0px |
| Title 2 | `title2` | Semi Bold (600) | 16px | 24px (1.50) | 0px |
| Title 3 | `title3` | Semi Bold (600) | 14px | 22px (1.57) | 0px |
| Title 4 | `title4` | Semi Bold (600) | 13px | 20px (1.54) | 0px |
| Body 1 | `body1` | Regular (400) | 18px | 26px (1.44) | 0px |
| Body 2 | `body2` | Regular (400) | 16px | 24px (1.50) | 0px |
| Body 3 | `body3` | Regular (400) | 14px | 22px (1.57) | 0px |
| Body 4 | `body4` | Regular (400) | 13px | 20px (1.54) | 0px |
| Caption 1 | `caption1` | Semi Bold (600) | 12px | 18px (1.50) | 0px |
| Caption 2 | `caption2` | Medium (500) | 12px | 18px (1.50) | 0px |
| Caption 3 | `caption3` | Semi Bold (600) | 10px | 16px (1.60) | 0px |

## How to choose

Pick a style by the role of the text, using the style names as the guide:

- **Largest screen titles / hero text** → `display1`, `display2` (Display). The biggest, boldest styles for top-level emphasis.
- **Screen title** → `heading1` (or `heading2` / `heading3` for slightly smaller titles). Headings are the bold styles for primary screen and page titles.
- **Section header / subsection title** → `title1`–`title4` (Title). Semi-bold styles that label sections and group content; step down the number for smaller, nested headers.
- **Body text** → `body1`–`body4` (Body). Regular-weight styles for paragraphs and running content; choose the size to match the surrounding context.
- **Captions / supporting labels** → `caption1`–`caption3` (Caption). The smallest styles for metadata, helper text, and labels.
