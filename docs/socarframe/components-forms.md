> Source: https://socarframe.socar.kr/development/components/Input · https://socarframe.socar.kr/development/components/TextArea · https://socarframe.socar.kr/development/components/Checkbox · https://socarframe.socar.kr/development/components/Radio · https://socarframe.socar.kr/development/components/SelectionBox · https://socarframe.socar.kr/development/components/SegmentedControl · https://socarframe.socar.kr/development/components/Chip · https://socarframe.socar.kr/development/components/DatePicker · https://socarframe.socar.kr/development/components/TimePicker

# Socarframe — Form & Selection Components

Design-decision reference for the socarframe form and selection components. Use this when laying out input fields, choices, filters, and date/time pickers in SOCAR app screens. Choose variants, sizes, and states from the values transcribed here — do not introduce token, prop, or copy names that aren't listed.

---

## Input

사용자로부터 단일 행 텍스트를 입력받는 컴포넌트입니다.

**Purpose** — Single-line text entry. Compose `label`, `helperText`, `leading`, `trailing`, `clearable` as props. Use a `formatter` to auto-format values such as phone numbers and dates.

**When to use** — When a user must enter one line of text (name, phone number, code, etc.). For multi-line text, use TextArea instead.

### Variants

Choose with the `variant` prop:

- **Filled** (기본 / default)
- **Outlined**
- **Underlined**

### States

- **Default** — Standard field.
- **Filled** — Holds a `value` / `defaultValue`; when `clearable` is true (default), a clear button appears in the trailing area.
- **Disabled** — `disabled` true.
- **Error** — `isError` true applies error-state styling. Pair with `helperText` to explain the error.

### Formatter

Pass a built-in or custom formatter via the `formatter` prop. Built-in formatters:

| 포맷터 | 설명 | 예시 출력 |
| --- | --- | --- |
| inputFormatters.phone | 전화번호 (3-4-4) | 010-1234-5678 |
| inputFormatters.date | 날짜 (YYYY. MM. DD) | 2025. 03. 16 |
| inputFormatters.dateRange | 날짜 범위 | 2025. 03. 16 ~ 2025. 03. 20 |
| inputFormatters.sequence | 4자리 그룹 (카드번호 등) | 1234 5678 9012 3456 |

Custom formatters follow the type `(value: string, context: InputFormatContext) => string | InputFormatResult`. Example use cases (from source): 휴대폰 번호 (숫자만 입력하면 자동으로 하이픈이 추가됩니다), 초대 코드 (영문/숫자만 허용하며 3-2-3 패턴으로 하이픈이 자동 추가됩니다).

### Anatomy (slots)

- `data-slot="input-root"` — 루트 컨테이너
- `data-slot="input-label"` — 라벨
- `data-slot="input-wrapper"` — 입력 필드 래퍼
- `data-slot="input-leading"` — 좌측 영역
- `data-slot="input-field"` — 실제 `<input>` 요소
- `data-slot="input-trailing"` — 우측 영역 (clear 버튼 포함)
- `data-slot="input-helper"` — 도움말 텍스트

Example copy: label `Label`, helper text `도움말 문구가 여기에 표시됩니다.`

### Props reference

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| className | string | - | 루트 컨테이너에 추가 클래스 적용 |
| clearable | boolean | true | 입력값 삭제 버튼 노출 여부 |
| clearUI | ReactNode | - | 커스텀 clear 버튼 UI |
| defaultValue | string \| number | - | 비제어 모드 초기값 |
| disabled | boolean | false | 비활성 상태 |
| formatter | InputFormatter | - | 입력값 포맷터 |
| helperText | ReactNode | - | 도움말 텍스트 |
| isError | boolean | false | 에러 상태 스타일 적용 |
| label | ReactNode | - | 라벨 |
| leading | ReactNode | - | 입력 필드 좌측 영역 |
| onClear | () => void | - | clear 버튼 클릭 시 콜백 |
| trailing | ReactNode | - | 입력 필드 우측 영역 |
| value | string \| number | - | 제어 모드 값 |
| variant | 'filled' \| 'outlined' \| 'underlined' | 'filled' | 스타일 변형 |

---

## TextArea

사용자로부터 여러 행의 텍스트를 입력받는 컴포넌트입니다.

**Purpose** — Multi-line text entry. Compose `label`, `helperText`, `aside`, `trailing`, `clearable` as props. Control height behavior with `resizeType` (`fixed` | `flexible`).

**When to use** — When a user enters multiple lines of free text (memos, hashtags, comments). For a single line, use Input.

### Variants

Choose with the `variant` prop:

- **Filled** (default)
- **Outlined**
- **Underlined**

### Sizes / height behavior

Control with `resizeType`:

- **fixed** (default) — Fixed height.
- **flexible** — `resizeType="flexible"` 설정하면 입력량에 따라 높이가 자동으로 늘어납니다. (Auto-grows with content.)

### States

- **Default** — Standard field.
- **Filled** — Holds a value; supports a character counter (example: `0/200`) and, when `clearable` is true, a clear button in the aside area.
- **Disabled** — `disabled` true.

### Formatter

Uses the same `InputFormatter` type as Input, so custom formatters apply here too. Example: 해시태그 입력 (줄마다 자동으로 # 이 붙습니다).

### Anatomy (slots)

- `data-slot="textarea-root"` — 루트 컨테이너
- `data-slot="textarea-label"` — 라벨
- `data-slot="textarea-wrapper"` — 입력 필드 래퍼
- `data-slot="textarea-field"` — 실제 `<textarea>` 요소
- `data-slot="textarea-aside"` — 우측 상단 액션 영역 (clear 버튼 포함)
- `data-slot="textarea-trailing"` — 하단 trailing 영역
- `data-slot="textarea-helper"` — 도움말 텍스트

Example copy: label `Label`, 자동 높이 조절.

### Props reference

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| aside | ReactNode | - | 우측 상단 액션 영역 |
| className | string | - | 루트 컨테이너에 추가 클래스 적용 |
| clearable | boolean | false | 입력값 삭제 버튼 노출 여부 |
| clearUI | ReactNode | - | 커스텀 clear 버튼 UI |
| defaultValue | string \| number | - | 비제어 모드 초기값 |
| disabled | boolean | false | 비활성 상태 |
| formatter | InputFormatter | - | 입력값 포맷터 |
| helperText | ReactNode | - | 도움말 텍스트 |
| label | ReactNode | - | 라벨 |
| onClear | () => void | - | clear 버튼 클릭 시 콜백 |
| resizeType | 'fixed' \| 'flexible' | 'fixed' | 높이 동작 방식 |
| trailing | ReactNode | - | 하단 trailing 영역 |
| value | string \| number | - | 제어 모드 값 |
| variant | 'filled' \| 'outlined' \| 'underlined' | 'filled' | 스타일 변형 |

---

## Checkbox

여러 항목을 동시에 선택해야 하는 경우 사용합니다.

**Purpose** — Multi-select control for selecting several items at once.

**When to use** — When a user may select more than one option simultaneously. Use `CheckboxGroup` to build the group layout easily. (For single-choice, use Radio.)

### States

- **Default** — Unchecked.
- **Checked** — `checked` (controlled) or `defaultChecked` true.
- **Disabled** — `disabled` true (example label: 비활성 옵션).

### Usage examples (from source)

- 기본: 약관 동의, 비활성 옵션.
- 그룹 선택: 차량 타입 — 세단 / SUV / 전기차.

### Props reference — Checkbox

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | ReactNode | - | 체크박스 텍스트 |
| checked | boolean | - | 제어 모드 체크 여부 |
| defaultChecked | boolean | false | 기본 체크 여부 |
| disabled | boolean | false | 비활성화 여부 |
| onChange | (event: ChangeEvent<HTMLInputElement>) => void | - | 체크 변경 이벤트 |
| name | string | - | 폼에서 사용할 이름 |
| value | string | - | 체크값 |
| className | string | - | 스타일 확장을 위한 클래스 |
| 기타 | InputHTMLAttributes<HTMLInputElement> | - | 기본 input 속성 |

### Props reference — CheckboxGroup

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | ReactNode | - | 그룹 제목 |
| ariaLabel | string | - | label이 없을 때 접근성 레이블 |
| ariaLabelledBy | string | - | label이 없을 때 접근성 레이블 |
| className | string | - | 스타일 확장을 위한 클래스 |
| 기타 | FieldsetHTMLAttributes<HTMLFieldSetElement> | - | 기본 fieldset 속성 |

---

## Radio

여러 항목 중 하나만 선택해야 하는 경우 사용합니다.

**Purpose** — Single-select control: choose exactly one item from a set.

**When to use** — When only one option may be selected at a time. Use `RadioGroup` to bind radios sharing the same `name`. (For multi-select, use Checkbox.)

### States

- **Default** — Unselected.
- **Checked** — `checked` (controlled) or `defaultChecked` true.
- **Disabled** — `disabled` true.

### Anatomy / customization

- `data-slot="radio-ui"` and `data-slot="radio-label"` let you customize the radio UI and label colors.
- `::after` can change the inner circle color.

### Usage examples (from source)

- 기본: 차량 타입 — 세단 / SUV / 전기차.
- 그룹 선택: 요금제 — 기본 / 할인 / 멤버십.

### Props reference — Radio

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | ReactNode | - | 라디오 텍스트 |
| checked | boolean | - | 제어 모드 체크 여부 |
| defaultChecked | boolean | false | 기본 체크 여부 |
| disabled | boolean | false | 비활성화 여부 |
| onChange | (event: ChangeEvent<HTMLInputElement>) => void | - | 체크 변경 이벤트 |
| name | string | - | 폼에서 사용할 이름 |
| value | string | - | 체크값 |
| className | string | - | 스타일 확장을 위한 클래스 |
| 기타 | InputHTMLAttributes<HTMLInputElement> | - | 기본 input 속성 |

### Props reference — RadioGroup

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | ReactNode | - | 그룹 제목 |
| ariaLabel | string | - | label이 없을 때 접근성 레이블 |
| ariaLabelledBy | string | - | label이 없을 때 접근성 레이블 |
| className | string | - | 스타일 확장을 위한 클래스 |
| 기타 | FieldsetHTMLAttributes<HTMLFieldSetElement> | - | 기본 fieldset 속성 |

---

## SelectionBox

카드형 레이아웃을 선택형 UI로 구성할 때 사용합니다.

**Purpose** — Turn a card-style layout into a selectable UI. Use with `SelectionBoxGroup` to build single- or multi-select sets easily.

**When to use** — When each choice needs richer content than a checkbox/radio label — text, badges, prices, supplementary info — laid out as a selectable card.

### Variants (selection type)

Set with `selectionType`:

- **single** (단일 선택)
- **multiple** (다중 선택)

On `SelectionBox` alone, `selectionType` defaults to `'single'`. On `SelectionBoxGroup`, `selectionType` is required.

### States

- **Default** — Unselected.
- **Selected (checked)** — `checked` true (controlled) or via group `value` / `defaultValue`.
- **Disabled** — `disabled` true (on box or group).

### Usage examples (from source)

- 단일 선택: 차량 타입 — 세단 (편안한 승차감) / SUV (넓은 적재 공간) / 전기차 (친환경 차량).
- 다중 선택: 옵션 — 보험 포함 / 연비 우수 / 즉시 출발.
- 복합 레이아웃: combine text, badge (Best, Eco, New), price (e.g. 12,000 / 1h), and tags (연비 좋음, 쉬운 주차 …).

### Props reference — SelectionBox

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | ReactNode | - (필수) | 카드 내부 콘텐츠 |
| value | string | - | 그룹 선택값으로 사용할 값 |
| selectionType | 'single' \| 'multiple' | 'single' | 단독 사용 시 입력 타입 지정 |
| checked | boolean | - | 제어 모드에서 체크 여부 |
| disabled | boolean | false | 비활성화 여부 |
| onChange | (event: ChangeEvent<HTMLInputElement>) => void | - | 체크 상태 변경 이벤트 |
| name | string | - | 폼에서 사용할 이름 |
| className | string | - | 스타일 확장을 위한 클래스 |
| 기타 | InputHTMLAttributes<HTMLInputElement> | - | 기본 input 속성 |

### Props reference — SelectionBoxGroup

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| selectionType | 'single' \| 'multiple' | - (필수) | 단일/다중 선택 타입 |
| label | ReactNode | - | 그룹 제목 |
| ariaLabel | string | - | label이 없을 때 접근성 레이블 |
| ariaLabelledBy | string | - | label이 없을 때 접근성 레이블 |
| name | string | - | 그룹 입력 name |
| value | string \| string[] | - | 제어 모드 선택 값 |
| defaultValue | string \| string[] | - | 비제어 모드 기본 값 |
| onChange | (value: string \| string[]) => void | - | 선택 값 변경 이벤트 |
| disabled | boolean | false | 그룹 비활성화 여부 |
| className | string | - | 스타일 확장을 위한 클래스 |
| 기타 | FieldsetHTMLAttributes<HTMLFieldSetElement> | - | 기본 fieldset 속성 |

---

## SegmentedControl

동일 화면 안에서 짧은 필터·보기 전환을 빠르게 제공할 때 사용합니다.

**Purpose** — Quick in-screen filter / view switching. Compose label content from `HeaderItem.Title`, `Number`, `Badge`; place `ContentItem`s in the same order to auto-switch with the selected index.

**When to use** — Best for up to 4–5 short labels where content swaps immediately just below the tab bar. With `type="anchor"` it can also act as a scroll anchor (like Tab).

### Variants (type)

Set with `type`:

- **slide** (default) — Drag or tap switches content left/right. When tab heights differ, apply `dynamicHeight` on `SegmentedControl.Content` so the container height transitions naturally.
- **anchor** — Tab click scrolls to the given `targetId`; suited to long pages acting as a table of contents. Omitting `targetId` auto-generates an ID, but specifying it explicitly is recommended for anchor-scroll linkage and accessibility.

### Sizes

Set with `size`:

- **large**
- **medium** (default)
- **small**

### Sticky behavior

To pin to the top, apply `position: sticky`. For `type="anchor"`, tune the active baseline with `anchorOffset` and the scroll target on tab click with `scrollOffset`.

### Anatomy (slots)

- `SegmentedControl.Header` / `HeaderItem` — 라벨 영역. Combine `Title`, `Number`, `Badge`, or place free content as needed.
- `SegmentedControl.Content` / `ContentItem` — 탭 전환 시 함께 교체되는 영역. For `type="anchor"`, set `targetId` to scroll to that section.

### Usage examples (from source)

- Slide: 내 쿠폰 (badge 9+) / 쿠폰 받기 / 만료 임박 (badge 3); or 내 쿠폰 / 추천 / 가이드.
- Anchor: 탭1 (badge 9+) / 탭2 / 탭3 / 탭4 / 탭5 → 컨텐츠1…5. "탭을 클릭하면 해당 섹션으로 스크롤됩니다."

### Props reference

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | React.ReactNode | - (필수) | Header와 Content 슬롯을 조합해 UI를 구성합니다. |
| className | string | - | 루트 컨테이너에 추가 클래스 적용 |
| size | 'large' \| 'medium' \| 'small' | 'medium' | 라벨 및 콘텐츠 레이아웃 크기 |
| type | 'slide' \| 'anchor' | 'slide' | 슬라이드 전환 또는 스크롤 앵커 모드 |
| onChange | (index: number) => void | - | 선택된 인덱스가 변경될 때 호출 |
| value | number | undefined | 제어 모드에서 선택 인덱스를 지정 |
| $root | HTMLElement \| null | - | type="anchor"에서 스크롤을 감지할 루트 엘리먼트 |
| anchorOffset | number | 0 | 앵커 모드에서 활성화 기준선 오프셋 (px) |
| scrollOffset | number | - | 앵커 모드에서 탭 클릭 시 스크롤 목표 위치 오프셋 (px) |

---

## Chip

텍스트와 아이콘 조합으로 상태를 나타내는 Selection Chip 컴포넌트입니다.

**Purpose** — Selection chip that conveys state via text + icon. Use the `selected` state and `role` (`button` / `option`) for a toggle button or an option list.

**When to use** — For toggle filters or selectable option lists where each choice is a compact text/icon pill. Supports single-select and multi-select patterns.

### Variants (role)

Set with `role`:

- **button** (default) — Toggle button.
- **option** — Item in an option list.

### Sizes

Set with `size` (required) — adjusts height, padding, and font size:

- **medium**
- **small**
- **xsmall**

### States

- **Default** — Unselected.
- **Selected** — `selected` true (managed externally).
- **Disabled** — `disabled` true; text/background switch to disabled tokens and interaction is blocked.

### Do & don't

- **Do** — Customize with `className`; outside the `disabled` state no styles are forced, so it is meant to be extended.
- **Don't** — Rely on built-in styling for the disabled look — `disabled` is the one state with enforced (disabled-token) styling and blocked interaction.

### Design tokens used

- When `disabled`, 텍스트/배경이 비활성 토큰으로 변경 (text/background switch to disabled tokens).

### Anatomy

- `label` (required) — chip text.
- `leftIcon` / `rightIcon` — optional leading/trailing icons.

### Props reference

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | ReactNode | - (필수) | Chip에 표시되는 텍스트 |
| size | 'medium' \| 'small' \| 'xsmall' | - (필수) | 높이, 패딩, 폰트 크기 조정 |
| className | string | - | 커스텀 스타일 적용 |
| disabled | boolean | false | 비활성 상태 |
| hapticType | HapticFeedback | 'REGULAR' | 햅틱 피드백 타입 |
| leftIcon | ReactNode | - | 좌측 아이콘 |
| rightIcon | ReactNode | - | 우측 아이콘 |
| role | 'button' \| 'option' | 'button' | ARIA role (토글 vs 옵션) |
| selected | boolean | - | 선택 상태 (외부에서 관리) |

---

## DatePicker

`DateManager` 클래스로 날짜 범위를 제어하고, `WeekGroup`/`DayCell`로 그리드를 렌더링하는 조립형 DatePicker입니다.

**Purpose** — Assembly-style date picker: control date ranges with the `DateManager` class and render the grid with `WeekGroup` / `DayCell`. Compose label policies to build flows (rental/return, holidays, overlapping selection, etc.).

**When to use** — When you need a calendar with range selection and policy control: selectable window limits, disabled days (holidays / manual blocks), max range length, and custom day labels. Supports multi-month scrolling and split-viewport summary panels.

### Configuration patterns (from source)

- **기본 범위 선택** — `DateManager.setMonthCount` sets how many months to show from today; `setSelectableRange` / `setPastSelectionDisable` limit the selectable window; `setCustomLabel` injects default labels (`start`, `end`, `today`, `start-end`) plus custom ones. Example header: 대여 ~ 반납, 2026. 6.
- **라벨 · 비활성화 · 정책** — Combine holidays, manual disabling, and max selection days. `LabelConfig.policy.className` customizes how the DayCell exposes content. Example: 최대 범위 10일, 06.20~08.04 내에서만 선택 가능, 공휴일·차단일 표시.
- **스크롤 헤더 싱크** — Track `data-calendar-month` sections so the top header follows the current month while scrolling multiple months.
- **Viewport Split Calendar** — Drag the divider between calendar and summary panel to resize heights; reuse the `WeekGroup` / `DateManager` combo and place any info below (e.g. 요금 정책, 체크리스트).

### Anatomy / building blocks

- **DateManager** — Class that generates date data, manages label/disable policies, and holds selection-range state.
- **useDateManager(manager, initialSetting?)** — Hook syncing React lifecycle with DateManager's view; returns `calendarMap`, `handleSelect`, `selectedRange`, etc.
- **WeekGroup / Week / DayCell** — View components rendering the date grid; used together with `DayOfWeek`, `Title`.

### DateManager 주요 메서드

| Method | Description |
| --- | --- |
| setMonthCount(prev, next) | 오늘 기준 이전/이후 월을 생성해 calendarMap을 갱신합니다. |
| setCustomLabel([{ date?, labelConfig }]) | 라벨 타입/정책을 날짜에 연결합니다. 날짜를 생략하면 전역 라벨로 적용됩니다. |
| setSelectableRange(start, end) | 선택 가능한 날짜 구간을 한정합니다. |
| setPastSelectionDisable(boolean) | 오늘 이전 날짜를 모두 비활성화합니다. |
| setHolidays(dates) / setManualDisabledDates(dates) | 공휴일/수동 차단일을 등록합니다. |
| setMaxRangeDays(number \| null) | 최대 선택 길이를 제한합니다. |
| select(date) / selects(start, end) | 단일/범위 선택을 갱신하고 구독자에게 알립니다. |

### useDateManager 반환값

| Key | Description |
| --- | --- |
| calendarMap | Map<monthKey, WeekType[]> 형태의 렌더링 데이터 |
| handleSelect(date) | DateManager.select에 위임되는 선택 핸들러 |
| selectedRange | [startNode \| null, endNode \| null] |
| monthKeys | 현재 렌더링 중인 월 키 배열 |

### WeekGroup props

| Prop | Type | Description |
| --- | --- | --- |
| weeks | WeekType[] | useDateManager가 반환한 주차 데이터 |
| edge | MonthEdge | 월의 시작/끝 주차 메타 (라운딩/보더 처리) |
| handleSelect | (date: Date) => void | 셀 선택 시 호출되는 콜백 |
| className / selectionBarClassName | string | 추가 스타일 오버라이드 |

---

## TimePicker

드래그, 터치, 마우스 휠, 키보드로 시·분을 맞추는 시간 선택 컴포넌트입니다.

**Purpose** — List-based time picker for setting hour/minute via drag, touch, mouse wheel, or keyboard. Fast even in short flows.

**When to use** — When a user picks an hour and minute (e.g. 대여 / 반납 times). Compose `TimePicker.List` and `TimePicker.Separator`. Use `disabledItems` + `onDisabledSelect` to signal unavailable ranges.

### Variants / state

- **isExpand** — Render the list expanded (default true). When false, taps/clicks fire `onClickWhenCollapse` (use for a collapsed entry point).
- **isBlockingWhenAnimating** — When on, blocks input during animation to prevent mis-operation.
- **Disabled items** — Values in `disabledItems` are not selectable; pressing one fires `onDisabledSelect`. Arrow/Page navigation auto-skips disabled items.

### Anatomy (slots)

- `TimePicker.List` — hour/minute list (`items` = `'hour'` | `'minute'` | `string[]`).
- `TimePicker.Separator` — separator between lists.
- `selectedItemClassName` — customize the selected cell style.

Example copy: 대여 / 반납, 선택된 대여 시간 `10시 40분`, 선택된 반납 시간 `10시 30분`.

### Interactions

| 입력 방식 | 동작 | 비고 |
| --- | --- | --- |
| 터치 드래그 | 리스트를 위아래로 스크롤, 놓으면 가장 가까운 값으로 snap | 관성(inertia) 적용 |
| 마우스 드래그 | 터치 드래그와 동일 | - |
| 마우스 휠 | deltaY만큼 리스트 이동, 휠 멈추면 snap | 페이지 스크롤 차단 |
| ArrowUp / ArrowDown | 한 칸씩 이동 | disabled 아이템 자동 건너뜀 |
| PageUp / PageDown | 5칸씩 이동 | disabled 아이템 자동 건너뜀 |
| Home / End | 첫 번째 / 마지막 활성 아이템으로 이동 | - |

### Props reference — TimePicker

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | ReactNode | - (필수) | TimePicker.List, TimePicker.Separator 조합 |
| isExpand | boolean | true | 리스트를 확장된 상태로 렌더링할지 여부 |
| isBlockingWhenAnimating | boolean | false | 애니메이션 중 상호작용을 차단할지 여부 |
| onClickWhenCollapse | () => void | - | isExpand이 false일 때 터치/클릭 시 실행되는 핸들러 |
| selectedItemClassName | string | - | 선택된 셀에 적용할 커스텀 클래스 |
| 기타 | HTMLMotionProps<'div'> | - | className, style 등 기본 속성 전달 가능 |

### Props reference — TimePicker.List

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| items | 'hour' \| 'minute' \| string[] | - (필수) | 렌더링할 항목 집합 |
| value | string | - (필수) | 현재 선택된 값 |
| onChange | (value: string) => void | - (필수) | 값이 바뀔 때 호출되는 콜백 |
| disabledItems | string[] | [] | 선택을 막을 값 목록 |
| onDisabledSelect | (value: string) => void | - | 막힌 값을 눌렀을 때 호출되는 콜백 |
| isExpand | boolean | - | 상위 TimePicker에서 전달되는 확장 여부 |
| isBlockingWhenAnimating | boolean | - | 애니메이션 중 상호작용 차단 여부 |
| onAnimateChange | (isAnimating: boolean) => void | - | 애니메이션 시작/종료 시 호출되는 콜백 |
| selectedItemClassName | string | - | 선택된 셀 스타일을 커스터마이즈할 때 사용하는 클래스 |
| className | string | - | 리스트 컨테이너 커스텀 클래스 |
| 기타 | HTMLAttributes<HTMLDivElement> | - | 표준 div 속성 |
