> Source: https://socarframe.socar.kr/development/components/Buttons · https://socarframe.socar.kr/development/components/Buttons/ActionButton · https://socarframe.socar.kr/development/components/Buttons/IconButton · https://socarframe.socar.kr/development/components/Buttons/TextButton · https://socarframe.socar.kr/development/components/Haptic

# Action Components — Buttons & Haptic

This guide covers the socarframe action components used to trigger behavior in SOCAR app screens: the three button types (`ActionButton`, `IconButton`, `TextButton`) and the `Haptic` feedback system that backs them.

## Buttons overview / choosing the right button

버튼 컴포넌트를 상황에 맞게 선택하세요. Pick the button type by how much emphasis the action needs and how it is presented:

| Component | When to use |
| --- | --- |
| **ActionButton** | 페이지 내 핵심 행동을 위한 기본 버튼. Text (optionally with icon) actions with selectable emphasis via `styleType` + `variant`. Use for the page's primary and supporting CTAs (예약, 결제, 확인 등). |
| **IconButton** | 아이콘만으로 동작을 표현하는 버튼. Use when an icon alone communicates the action and no label is needed. Background/border colors are fully customizable. |
| **TextButton** | 보조 액션이나 링크성 CTA. Text-only button whose emphasis is tuned with underline, icon, and loading state. |

---

## ActionButton

페이지 내 핵심 행동을 위한 기본 버튼입니다.

`styleType`과 `variant` 옵션을 통해 스타일을 조절하고, 아이콘·로딩 상태를 함께 노출할 수 있습니다.

### Purpose
- 텍스트와 아이콘을 조합해 버튼을 구성합니다.
- `styleType`을 통해 실색(`fill`)과 외곽선(`outlined`) 스타일을 전환합니다.

### When to use
Use for the most important actions on a page — primary CTAs and their supporting actions. Vary `styleType` and `variant` to set the emphasis level (see combination guide below).

### Variants — styleType
`styleType`은 버튼의 배경과 보더 렌더링 방식을 결정합니다.

| styleType | 설명 |
| --- | --- |
| `'fill'` | 배경색이 채워진 스타일. 주요 CTA에 적합합니다. (기본값) |
| `'outlined'` | 배경 없이 외곽선만 표시. 보조 액션에 적합합니다. |

### Variants — variant
`variant`는 버튼의 색상 팔레트를 결정합니다. `styleType`에 따라 사용 가능한 variant가 다릅니다.

**fill 스타일의 variant**

| variant | 설명 |
| --- | --- |
| `'primary'` | 메인 브랜드 컬러(블루) 배경, 흰색 텍스트. 페이지의 가장 중요한 액션에 사용합니다. |
| `'secondary'` | 연한 블루(blue-100) 배경, 진한 텍스트. primary보다 낮은 강조도의 액션에 사용합니다. |
| `'tertiary'` | 연한 그레이(gray-100) 배경, 기본 텍스트 색상. 가장 낮은 강조도의 보조 액션에 사용합니다. |

**outlined 스타일의 variant**

| variant | 설명 |
| --- | --- |
| `'primary'` | 흰색 배경, 브랜드 컬러 보더와 텍스트. 강조되는 외곽선 버튼. |
| `'secondary'` | 흰색 배경, 그레이 보더, 기본 텍스트 색상. 중립적 외곽선 버튼. |

> 주의: `outlined` 스타일에서는 `tertiary` variant를 지원하지 않습니다. `tertiary`를 지정하면 `primary`로 폴백됩니다.

### styleType + variant combination guidance
`variant`는 색상 팔레트를, `size`는 타이포그래피·패딩을 바꿉니다.

| styleType | variant | 사용 시나리오 |
| --- | --- | --- |
| fill | primary | 페이지 핵심 CTA (예약, 결제, 확인) |
| fill | secondary | 보조 액션 (자세히 보기, 옵션 선택) |
| fill | tertiary | 낮은 우선순위 액션 (건너뛰기, 나중에) |
| outlined | primary | 강조되는 보조 액션 (수정, 변경) |
| outlined | secondary | 중립적 보조 액션 (취소, 닫기) |

### Sizes
`size`는 타이포그래피·패딩을 바꿉니다.

| size | 타이포그래피 | 패딩 | border-radius |
| --- | --- | --- | --- |
| large | title2 | py-400 px-550 | radius-350 |
| medium | title3 | py-300 px-450 | radius-300 |
| small | title4 | py-250 px-400 | radius-250 |
| xSmall | caption2 | py-150 px-250 | radius-200 |

### States
- **default** — interactive button rendered per `styleType` / `variant` / `size`.
- **disabled** — `disabled` prop; 비활성화 여부.
- **loading** — `loading` prop. 로딩 중에는 클릭이 비활성화되며 Lottie 로더가 표시됩니다. (활성화 시 버튼 비활성 + Lottie 노출)
- **haptic events** — ActionButton은 `pointerdown`, `pointerup` 이벤트에 반응하도록 설계 되었습니다.

### Haptic feedback
Button의 `hapticConfig` prop을 통해 웹뷰 내 햅틱 피드백을 설정할 수 있습니다. 서비스에서 상황에 맞춰 disable 설정을 할 수 있습니다. 기본값:

```ts
export const ACTION_BUTTON_HAPTIC_CONFIG: HapticConfig = {
  disable: true,
  eventType: "pointerup",
  type: "REGULAR",
};
```

### Design tokens used
- Typography: `title2`, `title3`, `title4`, `caption2`
- Padding: `py-400` / `px-550`, `py-300` / `px-450`, `py-250` / `px-400`, `py-150` / `px-250`
- Radius: `radius-350`, `radius-300`, `radius-250`, `radius-200`
- Color references: `blue-100`, `gray-100`

### Props reference

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | string | - | 버튼 안의 텍스트 |
| size | `'large'` \| `'medium'` \| `'small'` \| `'xSmall'` | - | 버튼 크기 |
| styleType | `'fill'` \| `'outlined'` | `'fill'` | 배경/보더 스타일 |
| variant | `'primary'` \| `'secondary'` \| `'tertiary'` | `'primary'` | 색상 테마 |
| leftIcon | ReactElement | - | 텍스트 왼쪽 아이콘 |
| rightIcon | ReactElement | - | 텍스트 오른쪽 아이콘 |
| gap | number | 2 | 아이콘과 텍스트 사이 간격(px) |
| loading | boolean | false | 로딩 상태. 활성화 시 버튼 비활성 + Lottie 노출 |
| disabled | boolean | false | 비활성화 여부 |
| hapticConfig | HapticConfig | ACTION_BUTTON_HAPTIC_CONFIG | 버튼 햅틱 피드백 설정 |
| 기타 | ButtonHTMLAttributes\<HTMLButtonElement> | type="button" | 표준 버튼 속성(onClick, className 등) |

---

## IconButton

아이콘만으로 동작을 표현하는 버튼입니다. 배경/보더 색상을 자유롭게 커스텀할 수 있습니다.

동일한 버튼 크기에서도 아이콘 크기를 조절할 수 있습니다.

### Purpose
- 아이콘 컬러·배경·보더를 조합해 상태를 표현합니다.

### When to use
Use when an icon alone expresses the action and no text label is required. Background and border colors are freely customizable to convey state.

### Sizes / icon size behavior
- `size`를 유지한 채 아이콘 크기만 변경해도 패딩과 터치 영역은 동일하게 유지됩니다.
- Available sizes: `xSmall`, `small`, `medium`, `large`, `xLarge` (see Props).

### States
- **default** — customizable 아이콘 컬러·배경·보더.
- **disabled** — `disabled` 시 배경/보더 커스텀 값을 그대로 두더라도 비활성 색으로 덮어씁니다.
- **haptic events** — IconButton은 `pointerdown`, `pointerup` 이벤트에 반응하도록 설계 되었습니다.

### Haptic feedback
Button의 `hapticConfig` prop을 통해 웹뷰 내 햅틱 피드백을 설정할 수 있습니다. 서비스에서 상황에 맞춰 disable 설정을 할 수 있습니다. 기본값:

```ts
export const ICON_BUTTON_HAPTIC_CONFIG: HapticConfig = {
  disable: true,
  eventType: "pointerup",
  type: "WEAK",
};
```

### Props reference

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| icon | ReactElement | - (필수) | 표시할 아이콘 |
| size | `'xSmall'` \| `'small'` \| `'medium'` \| `'large'` \| `'xLarge'` | - (필수) | 버튼 크기 |
| disabled | boolean | false | 비활성화 여부 |
| hapticConfig | HapticConfig | ICON_BUTTON_HAPTIC_CONFIG | 버튼 햅틱 피드백 설정 |
| 기타 | ButtonHTMLAttributes\<HTMLButtonElement> | type="button" | 표준 버튼 속성(onClick, aria-label, className 등) |

---

## TextButton

보조 액션이나 링크성 CTA에 쓰는 텍스트형 버튼입니다.

밑줄, 아이콘, 로딩 상태를 조합해 강조도를 조절합니다.

### Purpose
- `variant`로 텍스트 색상을, `underline`으로 밑줄 여부를 제어합니다.
- 아이콘 크기는 주입하는 아이콘을 통해 별도 조절하며, 텍스트와 간격은 `gap`과 함께 조절해 균형을 맞춥니다.

### When to use
Use for secondary actions or link-style CTAs where a full filled/outlined button would be too heavy. Adjust emphasis with underline, icon, and loading state.

### Variants — variant
`variant`/`size`를 조합하여 다양한 스타일을 구성할 수 있습니다. Available variants: `primary`, `secondary`, `tertiary` (텍스트 색상 테마). `styleType` is fixed to `'text'`.

### Sizes
Available sizes: `large`, `medium`, `small`, `xSmall` (see Props). `size`는 타이포그래피·패딩을 바꿉니다.

### States
- **default** — text rendered per `variant` / `size`, optional `underline`.
- **disabled** — `disabled` prop; 비활성화 여부.
- **loading** — `loading` prop. 로딩 상태. 활성화 시 버튼 비활성 + Lottie 노출.
- **haptic events** — TextButton은 `pointerdown`, `pointerup` 이벤트에 반응하도록 설계 되었습니다.

### Haptic feedback
Button의 `hapticConfig` prop을 통해 웹뷰 내 햅틱 피드백을 설정할 수 있습니다. 서비스에서 상황에 맞춰 disable 설정을 할 수 있습니다. 기본값:

```ts
export const TEXT_BUTTON_HAPTIC_CONFIG: HapticConfig = {
  disable: true,
  eventType: "pointerup",
  type: "WEAK",
};
```

### Props reference

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| label | string | - (필수) | 버튼 텍스트 |
| size | `'large'` \| `'medium'` \| `'small'` \| `'xSmall'` | - (필수) | 버튼 크기 |
| variant | `'primary'` \| `'secondary'` \| `'tertiary'` | `'primary'` | 텍스트 색상 테마 |
| styleType | `'text'` | `'text'` | 텍스트 버튼 스타일 |
| underline | boolean | false | 밑줄 표시 여부 |
| leftIcon | ReactElement | - | 텍스트 왼쪽 아이콘 |
| rightIcon | ReactElement | - | 텍스트 오른쪽 아이콘 |
| gap | number | 2 | 아이콘과 텍스트 사이 간격(px) |
| loading | boolean | false | 로딩 상태. 활성화 시 버튼 비활성 + Lottie 노출 |
| disabled | boolean | false | 비활성화 여부 |
| hapticConfig | HapticConfig | TEXT_BUTTON_HAPTIC_CONFIG | 버튼 햅틱 피드백 설정 |
| 기타 | ButtonHTMLAttributes\<HTMLButtonElement> | type="button" | 표준 버튼 속성(onClick, className 등) |

---

## Haptic feedback

- 웹뷰 내 햅틱 피드백(Haptic Feedback)을 설정하는 메서드입니다.
- 웹브릿지를 한단계 추상화한 것이므로 앱의 버전에 따라 사용 가능여부가 나뉩니다. (네이티브 버전 미정)

### Usage

```ts
import { haptic } from "@socar-inc/socar-frame-web";

haptic("REGULAR", "interfaceType");
```

### HapticFeedback type

```ts
export type HapticFeedback =
  | "ALERT_WARNING"
  | "HAPTIC_UNSPECIFIED"
  | "REGULAR"
  | "STRONG"
  | "WEAK";
```

### Type guide

| Type (HapticFeedback) | Token | iOS | Android | Usage |
| --- | --- | --- | --- | --- |
| WEAK | haptic-weak | impact: soft, intensity: 0.5 | 지속 시간: 30ms, 진폭: 20 | 작은 피드백 — Text Button 전체 / Icon Button 전체 |
| REGULAR | haptic-regular | impact: soft, intensity: 0.7 | 지속 시간: 30ms, 진폭: 35 | 중간 정도의 피드백 — Action Button: Tertiary, Outlined |
| STRONG | haptic-strong | impact: soft, intensity: 0.9 | 지속 시간: 30ms, 진폭: 50 | 주요한 피드백 — Action Button: Primary, Secondary |
| ALERT_WARNING | haptic-alert-warning | notification: error | step.1 지속 시간: 50ms, 진폭: 255 / step.2 지속 시간: 50ms, 진폭: 255 / step.3 지속 시간: 100ms, 진폭: 255 | 주의 및 오류 피드백 — 오류 및 경고 메시지를 포함한 컴포넌트에 사용 |
| HAPTIC_UNSPECIFIED | - | 플랫폼 기본값 | 플랫폼 기본값 | 사용처에 맞춰 명시적인 타입을 선택하는 것을 권장 |

### Design decisions — which haptic for which button
- **Text Button / Icon Button** → `WEAK` (`haptic-weak`) — matches each component's default `hapticConfig.type: "WEAK"`.
- **Action Button: Tertiary, Outlined** → `REGULAR` (`haptic-regular`) — matches ActionButton's default `hapticConfig.type: "REGULAR"`.
- **Action Button: Primary, Secondary** → `STRONG` (`haptic-strong`).
- **오류/경고를 포함한 컴포넌트** → `ALERT_WARNING` (`haptic-alert-warning`).
- Prefer an explicit type over `HAPTIC_UNSPECIFIED`: 사용처에 맞춰 명시적인 타입을 선택하는 것을 권장.

### Design tokens used
`haptic-weak`, `haptic-regular`, `haptic-strong`, `haptic-alert-warning`
