> Source: https://socarframe.socar.kr/development/components/Alert, https://socarframe.socar.kr/development/components/Snackbar, https://socarframe.socar.kr/development/components/Tips, https://socarframe.socar.kr/development/components/Tips/AccentTip, https://socarframe.socar.kr/development/components/Tips/InfoTip, https://socarframe.socar.kr/development/components/Skeleton, https://socarframe.socar.kr/development/components/Badge, https://socarframe.socar.kr/development/components/Tag

# Feedback & Status Components

이 문서는 SOCAR 앱 화면을 Figma로 디자인할 때 참고하는 socarframe 디자인 시스템의 피드백/상태 표현 컴포넌트(Alert · Snackbar · Tips · Skeleton · Badge · Tag) 가이드입니다. 각 컴포넌트의 용도, variant, 상태, 토큰, props를 정리해 디자인 의사결정을 돕습니다.

---

## Alert

**Purpose**
Alert은 사용자에게 즉각적인 피드백, 확인 요청, 중요한 정보 전달을 제공하는 모달형 컴포넌트입니다. 화면 내 맥락을 유지하면서도 사용자의 주의를 끌어, 적절한 조치를 취하거나 상태 변화를 인지할 수 있도록 돕습니다.

**When to use**
- 즉각적인 피드백을 전달하거나 사용자의 확인을 요청해야 할 때
- 화면 맥락을 유지한 채 사용자의 주의를 끌어 조치를 유도해야 할 때
- `onAction`을 통해 사용자가 누른 버튼 결과로 다음 동작을 분기해야 할 때

**Variants (구성 패턴)**
- **기본 Alert**: 그래픽, 제목, 본문, 링크 버튼, 버튼 슬롯을 모두 포함한 형태입니다.
- **Dialog Alert**: GraphicSlot, Title, Body, ButtonSlot 내 하나의 버튼을 조합한 Dialog 형태입니다.
- **Window Alert**: Title, Body, ButtonSlot을 조합한 window alert 형태입니다.
- **Sequence Alert**: 여러 Alert를 순차적으로 보여주며, 첫 번째 Alert에서 선택한 결과에 따라 두 번째 Alert이 연속으로 열립니다. `Alert.open()`이 Promise를 반환하므로 `await`로 순차 흐름을 구성합니다.
- **Container Portal**: `Alert.PortalProvider`의 `container` prop에 DOM 엘리먼트를 전달하면 `document.body`가 아닌 해당 엘리먼트 내부에 Alert이 렌더됩니다.

**Anatomy (서브 컴포넌트)**

| 컴포넌트 | 설명 |
| --- | --- |
| Alert.GraphicSlot | 아이콘 또는 이미지를 넣는 Slot. graphicHeight 필수 지정 |
| Alert.Title | Alert 제목 |
| Alert.Body | Alert 본문 (최대 2줄 권장) |
| Alert.ButtonSlot | 버튼 영역. ActionButton을 children으로 전달 |
| Alert.LinkButton | 텍스트 링크 버튼 |

**States / 동작**
- `withDim`으로 배경 Dim 처리 여부를 제어합니다(기본 true).
- Haptic Feedback: Alert는 `mount`, `unmount` 시점에 햅틱 피드백을 발생시키도록 설계되었습니다. `hapticConfig`로 웹뷰 내 햅틱 피드백을 설정하며, 서비스에서 상황에 맞춰 disable 설정할 수 있습니다. 기본값:
  - `disable: false`
  - `eventType: "mount"`
  - `type: "ALERT_WARNING"`

**Usage do & don't**
- Do: Alert.Body는 최대 2줄을 권장합니다.
- Do: `container` 사용 시 `wrapperClassName="tw-absolute"`를 함께 전달해야 Alert이 컨테이너 영역 내에서만 렌더됩니다.
- Do: 여러 container에서 각각 간섭 없이 Alert을 띄우려면 `Alert.createScope()`로 독립적인 인스턴스를 생성합니다.

**Props reference**

### Alert

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | ReactNode | - (필수) | GraphicSlot, Title, Body, ButtonSlot 조합 |
| hapticConfig | HapticConfig | ALERT_HAPTIC_CONFIG | Alert mount/unmount 시 햅틱 설정 |
| withDim | boolean | true | 배경 Dim 처리 여부 |

### Alert.PortalProvider

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| container | Element \| null | document.body | Alert이 렌더될 DOM 엘리먼트 |
| wrapperClassName | string | - | AlertWrapper에 추가할 클래스명 (container 사용 시 tw-absolute 권장) |

### 정적 메서드

| 메서드 | Type | Description |
| --- | --- | --- |
| Alert.open | (renderer: AlertRenderer) => Promise<string> | Alert을 열고, 사용자 액션 결과를 Promise로 반환 |
| Alert.createScope | () => AlertScope | 독립적인 { open, PortalProvider } 인스턴스를 생성 |

---

## Snackbar

**Purpose**
Snackbar는 화면 하단에서 짧은 메시지로 상태 변화를 알리거나 사용자가 즉시 대응해야 하는 액션을 노출합니다.

**When to use**
- 전역 컨텍스트에 영향을 주지 않고 상태나 알림을 전달할 때
- 짧은 메시지로 상태 변화를 알리거나 즉시 대응해야 하는 액션을 노출할 때
- `handleVisibility`로 표시 상태를 제어하고 `hideAfter`로 자동 숨김 타이밍을 설정할 때

**Variants**

| Variant (`uiType`) | 설명 |
| --- | --- |
| Basic | 텍스트와 아이콘 중심의 기본 안내 타입입니다. 드래그로 닫을 수 있는 `hideWithDrag` 옵션을 제공합니다. |
| Overlay | `Snackbar.GraphicSlot`을 통해 대형 그래픽이나 일러스트와 함께 안내합니다. 드래그로 닫을 수 있는 `hideWithDrag` 옵션을 제공합니다. |
| Action | `Snackbar.Button`을 배치해 즉시 실행 가능한 액션을 노출합니다. |

**Anatomy (Slots)**

| Slot | 설명 |
| --- | --- |
| Snackbar.Text | 메시지 텍스트를 렌더링합니다. |
| Snackbar.IconSlot | 상태 아이콘을 감싸서 강조할 수 있습니다. |
| Snackbar.GraphicSlot | 대형 그래픽 또는 일러스트를 삽입합니다. |
| Snackbar.Button | 액션 버튼을 추가하며, 클릭 시 자동으로 닫힙니다. |

**States / 동작**
- `isVisible`와 `handleVisibility`로 노출 상태를 제어합니다.
- `hideAfter`(기본 3000ms) 시간 경과 후 자동으로 숨겨집니다.
- `hideWithDrag`가 true이면 드래그 제스처로 닫을 수 있습니다(Basic, Overlay).
- `positionType`('top' | 'bottom' | 'center')으로 렌더링 기준 위치를 지정하고, `extraPosition`으로 기본 위치에서 추가 이동(px)합니다.

**Props reference**

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| className | string | - | 추가 스타일을 위한 클래스 |
| children | React.ReactNode | - | Slot 조합으로 구성한 콘텐츠 |
| isVisible | boolean | - (필수) | 스낵바 노출 여부 |
| handleVisibility | (visible: boolean) => void | - (필수) | 표시 상태를 제어하는 콜백 |
| positionType | 'top' \| 'bottom' \| 'center' | - (필수) | 렌더링 기준 위치 |
| uiType | 'Basic' \| 'Overlay' \| 'Action' | - (필수) | 스낵바 UI 타입 선택 |
| hideAfter | number | 3000 | 자동으로 숨기기까지의 시간(ms) |
| hideWithDrag | boolean | false | 드래그 제스처로 닫을 수 있는지 여부 |
| extraPosition | number | 0 | 기본 위치에서 추가로 이동시킬 거리(px) |
| onHideEnd | () => void | - | 숨김 애니메이션 종료 시 호출되는 콜백 |

---

## Tips

**Purpose**
정보성/가이드용 보조 메시지 컴포넌트 묶음입니다. 특정 UI를 강조하거나 간단한 설명을 제공할 때 사용합니다.

**When to use**
- **AccentTip**: 버튼, 링크 등 트리거 주변에 짧은 온보딩/가이드를 띄울 때 사용합니다.
- **InfoTip**: 아이콘과 함께 짧은 설명을 제공하는 인라인 헬프 팁입니다.

### AccentTip

**Purpose**
트리거 주변을 강조해 짧은 온보딩/가이드를 보여주는 툴팁입니다. Portal 버전은 뷰포트 기준 위치를 계산하고, Static 버전은 부모 컨테이너 내에서 고정 배치합니다.

**Variants**
- **Static — 항상 떠 있는 경우**: 부모 요소 기준으로 절대 배치하는 고정 툴팁입니다. `variant="always"`로 지정하면 항상 노출됩니다. 툴팁과 트리거를 감싸는 부모 요소에 `position: relative`를 지정해야 합니다.
- **Static — 일정 시간 뒤에 사라지는 경우**: `variant="disappear"`로 지정하면 일정 시간 뒤 자동으로 사라집니다. 부모 요소에 `position: relative` 지정 필요.
- **Portal — controlled**: 클릭/토글 가능한 트리거와 콘텐츠를 합성합니다. `variant="controlled"`에서 `visible`, `onVisibleChange`로 열림 상태를 제어합니다. `portal`은 디자인 시스템에서 정의된 여백을 자동으로 유지하며 계산됩니다.

**States / 동작**
- `variant`: `'always'`(항상 노출) / `'controlled'`(제어형) / `'disappear'`(지연 후 자동 숨김).
- `direction`('top' | 'bottom' | 'left' | 'right')으로 트리거 기준 정렬 방향을 지정하고, `tooltipOffset`/`triangleOffset`(Static에서는 `offset`/`tipOffset`)으로 위치를 미세 조정합니다.
- 반응형: 부모 요소의 크기에 따라 툴팁의 최대 너비가 동적으로 조정됩니다(예: clamp로 30px~120px).

**Usage do & don't**
- Static 사용 시 툴팁과 트리거를 감싸는 부모 요소에 `position: relative`를 반드시 지정합니다.
- Don't: Portal을 활용하는 다른 컴포넌트와 호환되지 않을 수 있으므로, 필요 시 variant `static`으로 대체합니다.
- Don't: 단일 viewStack이 아닌 다중 viewStack 환경에서는 의도한 대로 동작하지 않을 수 있습니다. (예: 모달 내부에서 Portal AccentTip 사용 시 모달 외부에 렌더링된 툴팁이 모달 뒤에 가려질 수 있음 / 슬라이드 타입 탭에서 각 탭이 별도 viewStack을 가지면 탭 전환 시 의도한 위치에 렌더링되지 않을 수 있음)

**Props reference**

#### Portal AccentTip

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | ReactNode | - | AccentTip.Trigger, AccentTip.Content 조합 |
| size | 'large' \| 'medium' \| 'small' \| 'xSmall' | (필수) | 툴팁 크기 |
| variant | 'always' \| 'controlled' \| 'disappear' | 'always' | 표시 방식 (항상 노출/제어형/지연 후 자동 숨김) |
| direction | 'top' \| 'bottom' \| 'left' \| 'right' | 'bottom' | 트리거 기준 정렬 방향 |
| tooltipOffset | { x?: number \| string; y?: number \| string } | {} | 콘텐츠 위치 보정 |
| triangleOffset | { x?: number \| string; y?: number \| string } | {} | 삼각형 위치 보정 |
| disappearInterval | number | 2000 | variant="disappear" 시 자동 숨김 대기(ms) |
| visible | boolean | - | variant="controlled" 또는 초기 노출 제어 |
| onVisibleChange | (next: boolean) => void | - | 제어형에서 열림 상태 변경 콜백 |
| maxWidth | number | 320 | 최대 너비(px), direction이 left일 때 동적으로 조정 |
| useOverflow | boolean | true | viewport/컨테이너 경계에 맞춰 위치를 보정 |
| containerRef | RefObject<HTMLElement> | - | 포털 위치 계산 기준 컨테이너 |
| withShadow | boolean | true | 그림자 표시 여부 |
| zIndex | number | 0 | 포털 컨텐츠 z-index |

#### AccentTipStatic

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | ReactNode | - | 툴팁에 표시할 텍스트/노드 |
| size | 'large' \| 'medium' \| 'small' \| 'xSmall' | (필수) | 툴팁 크기 |
| direction | 'top' \| 'bottom' \| 'left' \| 'right' | 'bottom' | 트리거 기준 정렬 방향 |
| offset | { x?: number \| string; y?: number \| string } | { x:0, y:0 } | 툴팁 위치 보정 |
| tipOffset | { x?: number \| string; y?: number \| string } | {} | 삼각형 위치 보정 |
| variant | 'always' \| 'controlled' \| 'disappear' | 'always' | 노출 방식 |
| visible | boolean | true | 초기 노출 여부 (variant="controlled"에서 외부 제어) |
| disappearInterval | number | 2000 | variant="disappear" 자동 숨김 시간(ms) |
| onVisibleChange | (next: boolean) => void | - | 가시성 변경 시 콜백 |
| withShadow | boolean | true | 그림자 표시 여부 |
| withTip | boolean | true | 삼각형 표시 여부 |
| zIndex | number | 0 | 절대 배치된 툴팁 z-index |

### InfoTip

**Purpose**
`ⓘ 아이콘` 등 작은 트리거 주변에 짧은 설명을 띄우는 정보 팁입니다. `Portal`로 렌더링되며 방향은 현재 디자인 기준 `bottom` 고정, tip(삼각형) 없이 배경 패널만 표시됩니다.

**When to use**
- 아이콘 등 작은 트리거 옆에 짧은 설명을 인라인으로 제공할 때

**Anatomy**
- `children`은 `InfoTip.Trigger`, `InfoTip.Title?`, `InfoTip.Content` 조합으로 구성합니다.

**States / 동작**
- 트리거 클릭 또는 패널의 닫기 버튼으로 열림/닫힘을 토글합니다. 별도 controlled prop은 없으며 내부 상태로 동작합니다.
- `infoTipOffset`으로 트리거 기준 위치를 추가 보정하고, `maxWidth`로 폭을 제한합니다.

**Usage do & don't**
- Do: tip(삼각형)이 없으므로 배경색 대비를 확보하고 주변 요소와 겹치지 않도록 `infoTipOffset`을 조정합니다.
- Do: 방향 변경이나 controlled 동작이 필요하면 AccentTip 사용 또는 컴포넌트 확장을 검토합니다.
- Do: Tabs 내에서 사용 시 Portal이 탭 컨텐츠 외부에 렌더링되므로, 탭 전환 시 위치가 어긋날 수 있습니다. 이 경우 Tab 이동이 감지되면 InfoTip을 닫도록 구현합니다.

**Props reference**

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | ReactNode | - | InfoTip.Trigger, InfoTip.Title?, InfoTip.Content 조합 |
| className | string | - | 패널 스타일 커스터마이즈용 클래스 |
| infoTipOffset | { x?: number \| string; y?: number \| string } | { x: 0, y: 0 } | 트리거 기준 추가 오프셋 |
| maxWidth | number | 320 | 말풍선 최대 너비(px) |
| zIndex | number | 10 | Portal 컨텐츠 z-index |

---

## Skeleton

**Purpose**
콘텐츠 로딩 중 형태와 영역을 보여주는 플레이스홀더입니다. 카드·프로필·텍스트 영역 등 다양한 형태로 배치해 레이아웃 점프를 줄입니다.

**When to use**
- 콘텐츠 로딩 중 영역과 형태를 미리 보여주어 레이아웃 점프를 줄여야 할 때
- 카드 레이아웃을 구성할 때 썸네일, 텍스트, 태그 등 여러 타입의 Skeleton을 조합

**Variants / Anatomy**
- **형태별 Skeleton (`shape`)**: `rectangle` / `circle` / `capsule`. 도형과 radius, size를 조합해 필요한 로딩 영역과 최대한 유사하게 보여줍니다. (Rectangle, Circle(size), Capsule, Rounded rectangle 등)
- 카드 레이아웃: 썸네일, 텍스트, 태그 등 여러 타입의 Skeleton을 조합해 구성합니다.

**States / 동작 (로딩 애니메이션)**
- `animation`('none' | 'pulsate' | 'wave')으로 로딩 애니메이션 타입을 선택합니다. 기본값은 `isActive ? 'wave' : 'none'`.
- `isActive` 토글로 애니메이션을 중지/재개할 수 있습니다(animation 지정 시 무시). 백엔드 응답에 맞춰 애니메이션을 끄거나 유지할 때 활용합니다.

**Design tokens used (배경 타입)**
`bgType`으로 배경 타입에 맞춘 스켈레톤 컬러를 지정합니다(기본 `white-gray50`).
- `white-gray50`
- `gray100-gray500`
- `gray600-black`

**Props reference**

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| shape | 'rectangle' \| 'circle' \| 'capsule' | - | 형태. 미지정 시 일반 사각형이며 shape="rectangle"에서 radius가 적용됩니다. |
| size | number \| string | - | 원형/정사각형을 한 번에 지정할 때 사용 (width/height와 병행 불가) |
| width | number \| string | - | 가로 길이 (size를 사용하지 않는 경우) |
| height | number \| string | - | 세로 길이 (size를 사용하지 않는 경우) |
| radius | number \| string | 14 (shape="rectangle"일 때) | 모서리 둥글기 |
| animation | 'none' \| 'pulsate' \| 'wave' | isActive ? 'wave' : 'none' | 애니메이션 타입 |
| bgType | 'white-gray50' \| 'gray100-gray500' \| 'gray600-black' | 'white-gray50' | 배경 타입에 맞춘 스켈레톤 컬러 지정 |
| isActive | boolean | true | 기본 애니메이션 사용 여부 (animation 지정 시 무시) |
| 기타 | HTMLAttributes<HTMLDivElement> | - | className, style 등 기본 DOM 속성 |

---

## Badge

**Purpose**
새로운 알림이 있음을 표현하는 상태 표시 컴포넌트입니다. backgroundColor, textColor, borderColor로 색상을 커스텀할 수 있습니다(borderColor는 hasBorder가 true일 때 적용).

**When to use**
- **Content Badge**: 새로운 알림이 있음을 표현하며, `content`를 통해 알림 개수나 내용 등을 표현할 때
- **Dot Badge**: 새로운 알림이 있음을 점으로 표현할 때

**Variants**

| Variant | 설명 |
| --- | --- |
| content | 알림 개수나 내용 등을 `content`로 표시 |
| dot | 새로운 알림을 점으로 표시 |

크기(`size`): `medium` / `small` (필수).

**Design tokens used (Color Customization)**
- `backgroundColor`: 배경 색상 토큰 키 (keyof theme.colors)
- `textColor`: 텍스트 색상 토큰 키 (content 뱃지에 적용, keyof theme.colors)
- `borderColor`: 테두리 색상 토큰 키 (hasBorder=true일 때 적용, keyof theme.colors)
- `hasBorder=true`로 설정하면 border 1px white

**States / 동작**
- `visible`로 렌더링 여부를 제어합니다(기본 true).

**Props reference**

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| variant | 'content' \| 'dot' | - (필수) | badge 종류 |
| size | 'medium' \| 'small' | - (필수) | 컴포넌트 크기 |
| content | number \| string | - | variant="content" 일 때 표시할 내용 |
| children | ReactNode | - | 감쌀 대상(아이콘 등). variant="dot"에서 점 뱃지를 덮어씌울 때 사용 |
| backgroundColor | keyof theme.colors | - | 배경 색상 토큰 키 |
| textColor | keyof theme.colors | - | 텍스트 색상 토큰 키 (content 뱃지에 적용) |
| borderColor | keyof theme.colors | - | 테두리 색상 토큰 키 (hasBorder=true일 때 적용) |
| hasBorder | boolean | false | border 사용 여부. true 로 설정하면 border 1px white |
| visible | boolean | true | 렌더링 여부 |
| className | string | - | 스타일링 확장을 위한 추가적인 class |
| style | React.CSSProperties | - | 인라인 스타일 |

---

## Tag

**Purpose**
콘텐츠를 구분하거나 상태를 표시할 때 사용하는 짧은 레이블 컴포넌트입니다. 색상·아이콘·너비를 조합해 정보 밀도를 높일 수 있습니다. `Tag.Divider`를 사용해 태그를 그룹으로 표현할 수 있습니다.

**When to use**
- 콘텐츠를 구분하거나 상태를 표시할 때
- 색상·아이콘·너비를 조합해 정보 밀도를 높일 때
- `Tag.Divider`로 여러 태그를 그룹으로 묶을 때

**Variants / 구성 옵션 (예시에 나타난 조합)**
- 스타일: Neutral, Solid, Soft, Outlined
- 아이콘: With Icon (Medium Icon / Small Icon)
- 너비: 가변(내용 길이에 맞춰 자동 확장) / 고정(`width` 지정)
- 크기(`size`): `large` / `medium` / `small` / `xsmall` (필수)
- 형태(`shape`): `capsule` / `rectangle` (필수)

**Design tokens used**
- `backgroundColor`: 배경 색상 토큰 키 (keyof theme.colors, 필수)
- `textColor`: 텍스트 색상 토큰 키 (keyof theme.colors, 필수)
- `borderColor`: 테두리 색상 토큰 키 (keyof theme.colors)

**States / 동작**
- `width` 미지정 시 내용 길이에 맞춰 자동 확장됩니다.
- `기타` props로 className, onClick 등 기본 속성 전달이 가능합니다.

**Props reference**

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| backgroundColor | keyof theme.colors | - (필수) | 배경 색상 토큰 키 |
| textColor | keyof theme.colors | - (필수) | 텍스트 색상 토큰 키 |
| borderColor | keyof theme.colors | - | 테두리 색상 토큰 키 |
| size | 'large' \| 'medium' \| 'small' \| 'xsmall' | - (필수) | 크기 |
| shape | 'capsule' \| 'rectangle' | - (필수) | 형태 |
| leftIcon | ReactElement | - | 좌측 아이콘 |
| width | number \| string | - | 너비. 미지정 시 내용 길이에 맞춰 자동 확장 |
| children | string | - (필수) | 표시할 텍스트 |
| 기타 | HTMLAttributes<HTMLDivElement> | - | className, onClick 등 기본 속성 전달 가능 |
