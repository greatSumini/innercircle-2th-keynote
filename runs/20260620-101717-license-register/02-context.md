---
run: 20260620-101717-license-register
stage: context
status: ready
figma_library_available: no
---
# Context pack

Screen: 운전면허 등록·인증 온보딩 (모바일 포트레이트, width 360). 3 state frames left→right
in the session lane: ① 입력 기본, ② 인증 완료, ③ 검증 중 로딩. socarframe is **not** a bound
Figma library in the target file, so every token is applied **by value** and intent is carried by
layer names per `docs/figma-conventions.md` — same approach the existing `반납 완료` frame used.

## Design-system references
- Docs to follow:
  - `components-surfaces.md` → **TopAppBar** (header + back button).
  - `components-forms.md` → **Input** (변형 outlined/filled, states default/filled/error, formatter),
    **SelectionBox** (면허 종류 단일 선택), **Checkbox / CheckboxGroup** (동의), **DatePicker** (발급일자·생년월일 진입).
  - `components-actions.md` → **ActionButton** (하단 CTA, fill/primary/large; loading state for ③),
    **TextButton** (약관 '보기' 링크 행), **IconButton** (TopAppBar back/close).
  - `components-feedback.md` → **Tips / InfoTip / AccentTip** (촬영 안내), **Skeleton** (③ 로딩 placeholder),
    **Badge / Tag** (② 인증 완료 배지), **Snackbar/Alert** (선택, plan에서 결정).
  - `color.md`, `typography.md`, `spacing.md`, `icons.md` → tokens below.
  - `principles.md` → one-primary-action, guided/완결성 tone; `figma-conventions.md` → naming/placement.
- Key tokens for this screen:
  - **Color**
    - CTA: `primary-regular` (#0078FF) fill, label `white`. Pressed/strong → `primary-strong`.
    - Text hierarchy: title `text-strong`; field labels/body `text-primary`; helper/secondary `text-secondary`;
      placeholder/least `text-tertiary`; disabled (read-only ② fields) `text-disabled`.
    - Surfaces: screen bg `background-regular` (#F2F3F8); cards/field/촬영영역 white; borders `border-regular`;
      dividers `divider-regular`; weak fills `border-weak`/`divider-weak`.
    - Status: 인증 완료 ② → `status-positive-weak` bg + `status-positive-regular` icon/badge (#04CA81).
      촬영 Tips/안내 info → `status-information-weak` bg + `status-information-regular`/`primary-regular`.
      Input error (out of scope but reserve) → `status-negative-regular` (#FF3A5B).
  - **Type** (Pretendard, full weights — keep SemiBold 600, never drop to 500)
    - Screen title "운전면허를 등록해 주세요" → `heading2` (24/34, Bold 700), `text-strong`.
    - One-line description → `body2` (16/24, Regular), `text-secondary`.
    - Section/field group titles → `title2` (16, SemiBold) or `title3` (14, SemiBold), `text-strong`.
    - Field labels → `title4` (13, SemiBold) or `body3` (14); input value text → `body2`; helperText → `caption2` (12).
    - Checkbox/agreement labels → `body3`; CTA button label → `title2` (large ActionButton type).
    - Badge/completion micro-label → `caption1`/`caption2`.
  - **Spacing / radius**
    - Screen horizontal padding → `spacing-400` (16px). Section gaps → `spacing-300`/`spacing-400`;
      tight field-internal gaps → `spacing-100`/`spacing-200`; label→input → `spacing-150`/`spacing-200`.
    - Cards / 촬영 업로드 영역 / surfaces → `radius-300` (12px). Larger panel → `radius-400` (16px).
    - Large ActionButton → `radius-350` (14px). Inputs → `radius-300` (12px) typical.
    - Bottom fixed CTA region height ≈ 56px button + `spacing-300` top/bottom padding (match 반납 완료: 12px pad, 56px btn).
  - **Icons** (SOCAR Icon Library, applied as named vectors/placeholders)
    - Back/close: `icon-chevron-left-line` or `icon-close-line` (24, text-strong).
    - 발급일자/생년월일 trailing: `icon-calendar-check-line`.
    - 면허 종류 select trailing: `icon-chevron-right-line` / `icon-chevron-down-line`.
    - 촬영 영역: `icon-camera-line` / `icon-photo-line` / `icon-driver-license-line` (license-specific!) / `icon-cardscan-line`.
    - Tips: `icon-info-circle-line` (information). 약관 보기 행 trailing: `icon-chevron-right-line`.
    - ② 인증 완료: `icon-check-circle-fill` (status-positive-regular). ③ 로딩: ActionButton Lottie loader.

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | general + LeftSideIconSlot(BasicBackButton) | 화면 헤더 + 뒤로가기 (③ LoadingBar 옵션) | components-surfaces.md | none (build custom; no library) |
| IconButton | medium, `icon-chevron-left-line`/`icon-close-line` [aria-label] | TopAppBar 좌측 네비 | components-actions.md | none |
| Input | outlined or filled; states default/filled/error; clearable | 면허번호, 이름 입력 (+ helperText) | components-forms.md | none |
| Input (trigger) | filled + trailing icon, `formatter` inputFormatters.date | 발급일자·생년월일 (DatePicker 진입, YYYY. MM. DD) | components-forms.md | none |
| DatePicker | range/single grid (별도 surface 진입) | 발급일자·생년월일 캘린더 (정의만; 본 화면은 트리거) | components-forms.md | none |
| SelectionBox / SelectionBoxGroup | single (`selectionType=single`) — 또는 trigger Input | 면허 종류 선택 (1종/2종 등) | components-forms.md | none |
| Checkbox / CheckboxGroup | default/checked | 동의: 본인확인, 약관 동의 | components-forms.md | none |
| TextButton | text/tertiary, small/medium, rightIcon chevron | 약관 '보기 >' 링크 행 | components-actions.md | none |
| Tips (InfoTip / AccentTip) | size small/medium, information | 면허증 촬영 안내 Tips (밝기/반사/네 모서리) | components-feedback.md | none |
| ActionButton | **fill / primary / large** (radius-350, title2, h≈56) | 하단 고정 CTA '등록하기'; ③ `loading=true` | components-actions.md | none |
| Badge / Tag | content/dot or capsule, status-positive | ② 인증 완료 배지(필드/헤더) | components-feedback.md | none |
| Skeleton | rectangle/capsule, radius-300, wave | ③ 검증 중 폼/촬영영역 placeholder (선택) | components-feedback.md | none |

> 모든 컴포넌트는 라이브러리 미존재로 **primitives에서 직접 빌드**하고, 토큰은 값으로 적용 + 레이어명에
> `ComponentName · variant [token=value]` 형식으로 표기(implement). 기존 `반납 완료` 프레임의 레이어 네이밍을 표준 참조로 따른다.

## Figma library & reference status
- **Library available: no.** `get_libraries` lists only community kits (Material 3, Simple Design System,
  iOS/iPadOS/watchOS/visionOS/macOS) — **socarframe is not subscribed and not available to add**.
  `search_design_system` ("TopAppBar/Input/Checkbox/ActionButton" 및 "socarframe 운전면허 DatePicker …")
  returned only unrelated generic assets (`Button/…/CTA`, `toast`, `menucontainer`, `tabList` from a "LIBRARY"
  org library) — **no socarframe components, variables, or styles**. Treat socarframe as value-applied only.
- **Existing frames / placement:**
  - One page only: `Page 1` (id `0:1`).
  - Existing harness frame: **`[auto] 반납 완료 — 20260620-070646-return-complete`** (id `3:2`) at
    **x=200, y=0, w=360, h=857**. Strong style reference — match it: 360 portrait, TopAppBar 56px,
    white cards `radius-300`, ActionButton fill/primary/large 56px in a bottom fixed CTA region,
    token-encoded layer names, Pretendard.
  - **Placement for the new run:** request mandates the session lane at **x=13200, y=0**, lay the 3 state
    frames left→right with an 80px gutter (default `· 기본` leftmost, then `· 인증 완료`, then `· 검증 중`).
    This is well clear of the rightmost existing content (x≈560) → no overlap. Name frames
    `[auto] 운전면허 등록 · <state> — 20260620-101717-license-register`; wrap in a Section of the same stem if possible.

## Gaps (needs custom build)
- **TopAppBar** — no Figma component; build a 56px header frame (back IconButton + optional centered/left title),
  matching the existing 반납 완료 TopAppBar pattern.
- **면허증 촬영/업로드 영역** — socarframe has no dedicated camera/upload/dropzone component. Build a **custom**
  card: white surface `radius-300`, dashed/`border-regular` frame, `icon-camera-line`/`icon-driver-license-line`,
  안내 카피(body3/caption2), and a 촬영/업로드 trigger (ActionButton fill/secondary or TextButton). Mark `(custom)`.
- **면허 종류 "select trigger" Input** — socarframe Input has no native select/dropdown; compose as a filled Input
  with trailing chevron icon acting as a BottomSheet/picker trigger (custom assembly of Input + IconSlot).
- **DatePicker calendar surface** — the assembly-style DatePicker is for a separate calendar surface; on this
  screen use a date-formatted Input trigger (`inputFormatters.date`) — actual grid is out of scope per clarify.
- **인증 완료 상태(②) 성공 표현** — combine `status-positive-*` + `icon-check-circle-fill` + Badge/Tag; the overall
  "완료 hero / read-only filled fields" composition is a **custom layout** (reuse 반납 완료 success-hero pattern).
- **검증 중 로딩(③)** — no full-screen loading component; assemble from ActionButton `loading` + Skeleton +
  optional TopAppBar LoadingBar/dim. Custom composition.
- **약관 동의 행 (Checkbox + '보기 >' 링크)** — compose Checkbox + TextButton(rightIcon chevron) in a row; custom row,
  not a single DS component.
- Note: no error/네트워크 실패 states (out of scope); reserve `status-negative-*` tokens if plan adds them.
