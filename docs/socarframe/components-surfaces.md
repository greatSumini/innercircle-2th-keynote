> Source: https://socarframe.socar.kr/development/components/TopAppBar, https://socarframe.socar.kr/development/components/Tab, https://socarframe.socar.kr/development/components/BottomSheet, https://socarframe.socar.kr/development/components/Accordion, https://socarframe.socar.kr/development/components/Pattern, https://socarframe.socar.kr/development/components/Pattern/Carousel

# Navigation & Surface Components

Design-decision guide for the socarframe navigation and surface components: TopAppBar, Tab, BottomSheet, Accordion, and Pattern (Carousel). Use this when laying out SOCAR app screens in Figma — anatomy, states/detents, tokens, and when-to-use first; props as reference.

---

## TopAppBar

현재 화면의 제목과 주요 액션을 담는 상단 바입니다. Left/Title/Trailing 슬롯과 LoadingBar를 조합해 네비게이션, 상태 표시, 추가 액션을 배치할 수 있습니다.

### When to use
- 화면 상단에 제목과 주요 액션을 고정해 표시할 때.
- 뒤로가기·닫기 등 네비게이션 아이콘이 필요할 때.
- 스크롤에 따라 타이틀이 페이드 인되거나, 페이지 로딩 진행 상태를 표시해야 할 때.

### Anatomy / slots
- **`TopAppBar.LeftSideIconSlot`** — 좌측 영역. 뒤로가기, 닫기 등 네비게이션 아이콘을 배치합니다. 안에 `BasicBackButton`을 배치할 수 있습니다.
- **`TopAppBar.BasicBackButton`** — 기본 뒤로가기 버튼. `window.onClickNavigation`이 있으면 호출하고, 없으면 콘솔에 경고를 남깁니다.
- **`TopAppBar.Title`** — 제목 영역. `type`으로 시각/행동 패턴을 전환합니다. 기본 타입(`general`)로 한 줄 제목을 표시합니다.
- **`TopAppBar.ScrollDetectTitle`** — 스크롤 감지 기준 지점. `type="scroll"` 타이틀과 함께 사용합니다.
- **`TopAppBar.TrailingButtonSlot`** — 우측 액션 영역. 다양한 버튼과 아이콘을 넣을 수 있으며 **최대 3개까지만 허용**됩니다.
- **`TopAppBar.LoadingBar`** — 지정한 `url`의 `fetch` 진행 상태를 노출하는 헤드리스 컴포넌트입니다.

### Title variants
- **`general`** (기본) — 한 줄 제목을 표시합니다.
- **label 타입처럼 활용** — `TextButton`을 조합하여 label 타입처럼 활용할 수 있습니다 (예: 「서울시 강남구 테헤란로」 + 「즐겨찾기한 목적지에 바로 이동하세요.」).
- **`scroll`** — `ScrollDetectTitle`와 함께 사용하면 지정 영역을 지나갈 때 타이틀이 페이드 인됩니다. 하단 컨텐츠 영역을 스크롤하면 타이틀이 나타납니다.
- **이미지 포함 타이틀** — 타이틀 안에 이미지(SVG/IMG)를 넣어 프로필/썸네일을 표시할 수 있습니다. 차량/유저 프로필이나 썸네일을 타이틀과 나란히 노출할 때 사용하세요.

### LoadingBar (headless)
- `LoadingBar`는 전달한 `url`로 `fetch`가 발생하면 자동으로 로딩 프로그레스를 표시합니다.
- children render-props를 넘겨 `isLoading`/`progress` 기반으로 UI를 커스텀할 수 있습니다.

### Design notes / integration
- 컴포넌트 루트에 `data-id="socar-frame-top-app-bar"`가 있어 BottomSheet의 `maxType="topAppBar"` 계산 등에 활용됩니다.

### Props reference

#### TopAppBar.Title

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| type | 'general' \| 'scroll' | general | 타이틀 표현 방식 선택 |
| children | ReactNode | - | 표시할 타이틀 텍스트/노드 |
| onClick | () => void | - | 타이틀 영역 클릭 핸들러 |
| 기타 | React.HTMLAttributes<HTMLHeadingElement> | - | 클래스, 데이터 속성 등 기본 DOM 속성 전달 |

#### TopAppBar.LoadingBar

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| url | string | - | 로딩을 감지할 fetch URL(포함 여부로 판단) |
| children | (state: { isLoading: boolean; progress: number }) => ReactNode | 기본 로딩바 | 상태 기반으로 커스텀 UI를 렌더링할 때 사용합니다. |

---

## Tab

길거나 많은 콘텐츠를 페이지/섹션 단위로 나눠 탐색할 때 사용합니다.

### When to use
- **`type="slide"`** — 탭과 콘텐츠가 한 화면에서 전환됩니다. 카드 목록, 짧은 설명 등 밀도 높은 영역에 적합합니다.
- **`type="anchor"`** — 탭을 누르면 지정된 `targetId`로 스크롤합니다. 긴 상세 페이지에서 목차처럼 활용합니다.

### Variants / modes
- **Slide Navigation** — 상단 탭과 하단 콘텐츠가 연동되어 전환 애니메이션이 적용됩니다. `value` + `onChange`로 현재 탭을 제어하거나 내부 상태(기본값 `0`)를 그대로 사용할 수 있습니다. 콘텐츠 높이가 탭마다 다르면 `Tab.Content`의 `dynamicHeight`로 컨테이너 높이를 부드럽게 맞출 수 있습니다.
- **Anchor Navigation** — `$root`로 스크롤 컨테이너 element를 지정하여 섹션을 관찰하며, 탭을 클릭하면 해당 `targetId`로 이동합니다. `targetId`를 생략하면 내부에서 자동 ID를 생성하지만, 앵커 스크롤 연동과 접근성 연결을 위해 명시적으로 지정하는 것을 권장합니다. `anchorOffset`으로 활성화 기준선을, `scrollOffset`으로 탭 클릭 시 스크롤 목표 위치를 조정할 수 있습니다.
- **Sticky Navigation** — `Tab`을 상단에 고정하려면 `position: sticky` 스타일을 적용하세요. 탭을 클릭하면 해당 섹션으로 스크롤됩니다.

### Size
- `size`: `'large'`(기본) · `'medium'` · `'small'` — 탭 버튼과 인디케이터 크기.

### Anatomy / slots
- **`Tab.Header` / `HeaderItem`** — 탭 라벨 영역. `HeaderItem.Number`와 `Badge`를 조합하거나 자유롭게 컨텐츠를 넣을 수 있습니다.
- **`Tab.Content` / `ContentItem`** — 슬라이드 또는 앵커에 연결되는 콘텐츠 영역. `type="anchor"`에서는 각 `ContentItem`에 `targetId`를 지정하는 것을 권장합니다.
- **`Tab.Indicator`** — 슬라이드 모드에서 표시되는 인디케이터. 필요 시 스타일 확장 시에 접근할 수 있습니다.

### Example copy (slide)
- 탭 라벨 예시: 「이동」 · 「쏘카 **24**」 · 「카페」 · 「숙박 **7**」
  - 이동: 「지역 기반으로 추천되는 차량을 확인하세요.」
  - 쏘카: 「최신 이벤트와 할인 정보를 모아봤어요.」
  - 카페: 「주변 인기 카페를 추천해 드릴게요.」
  - 숙박: 「숙소 정보를 비교하고 간편하게 예약하세요.」
- 탭 라벨 예시(앵커): 「이동」 · 「여정」 · 「혜택」

### Props reference

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | React.ReactNode | - (필수) | Header, Content 등 서브 컴포넌트를 조합해 레이아웃을 구성합니다. |
| className | string | - | 루트 컨테이너에 추가 클래스 적용 |
| size | 'large' \| 'medium' \| 'small' | 'large' | 탭 버튼과 인디케이터 크기 |
| type | 'slide' \| 'anchor' | 'slide' | 슬라이드 전환 또는 스크롤 앵커 모드 |
| onChange | (index: number) => void | - | 선택된 인덱스 변경 시 호출 |
| value | number | 0 | 제어 모드에서 현재 선택 인덱스 지정 |
| slideAnimated | boolean | true | 슬라이드 모드에서 전환 애니메이션 사용 여부 |
| $root | HTMLElement \| null | - | type="anchor"에서 스크롤을 감지할 루트 엘리먼트 |
| anchorOffset | number | 0 | 앵커 모드에서 활성화 기준선 오프셋 (px) |
| scrollOffset | number | - | 앵커 모드에서 탭 클릭 시 스크롤 목표 위치 오프셋 (px) |

---

## BottomSheet

화면 하단에서 올라오는 시트 컴포넌트입니다. 드래그로 열고 닫을 수 있으며, 4단계 높이(디텐트)를 지원합니다.

### When to use
- 화면 하단에서 올라오는 보조 콘텐츠(리스트, 입력 폼, 옵션 선택 등)를 드래그 가능한 시트로 노출할 때.
- 전체 화면(viewport) 또는 **특정 컨테이너 안에서만** 동작하는 시트가 필요할 때.

### Anatomy / slots
BottomSheet 내부는 아래 슬롯으로 구성됩니다.

```
<BottomSheet>
  <BottomSheet.Header>            ← 상단 고정 영역
    <BottomSheet.Title>
      <BottomSheet.Label />       ← 제목
      {/* 우측 액션 버튼 등 */}
    </BottomSheet.Title>
    <BottomSheet.Subtitle />      ← 부제목 (선택)
  </BottomSheet.Header>
  <BottomSheet.Content>           ← 스크롤 가능한 본문
    {/* 리스트, 입력 폼 등 자유롭게 배치 */}
  </BottomSheet.Content>
  <BottomSheet.Footer>            ← 하단 고정 액션 영역 (선택)
    {/* 버튼 등 */}
  </BottomSheet.Footer>
</BottomSheet>
```

### Detents (states)
디텐트(detent)는 BottomSheet가 멈추는 높이 단계입니다. `state`/`onChange`로 제어하거나, `defaultState`로 비제어 모드를 사용할 수 있습니다.

| 디텐트 | 설명 | 비고 |
| --- | --- | --- |
| hidden | 완전히 닫힘 | DOM에서 제거됨 |
| tip | Header만 노출 | Content, Footer는 렌더링되지 않음 |
| half | 중간 높이 | 컨텐츠가 작으면 max와 동일한 높이가 될 수 있음 |
| max | 최대 높이 | 컨텐츠가 넘치면 Content 내부에서 스크롤 발생 |

**max 높이 계산 기준 (`maxType`)**
- `"86%"` (기본값) — 뷰포트 높이의 86%
- `"topAppBar"` — TopAppBar 높이를 제외한 나머지 영역

**디텐트 높이 커스터마이징** — `half`, `tip`, `max` prop에 고정값 또는 보정 함수를 전달할 수 있습니다.

```
// 고정값
<BottomSheet half={300} max={500} />

// 기본 계산값에서 보정
<BottomSheet tip={(base) => base + 30} half={(base) => base - 20} />
```

### Usage do & don't
- **주의** — Footer가 있는 경우 `hidden`과 `max` 디텐트만 사용할 수 있습니다. (tip/half 불가) → `hidden` ↔ `max`로만 전환됩니다.
- **주의** — `withoutTip={true}`이면 tip 디텐트가 비활성화되고, tip 요청 시 자동으로 half로 보정됩니다. (`half` ↔ `hidden`만 사용. `setState("tip")`을 호출해도 자동으로 half로 보정.)
- **Container-Aware 모드** — `containerRef`를 전달하면 BottomSheet가 전체 화면(viewport) 대신 특정 컨테이너 안에서만 동작합니다. backdrop, 높이 계산, 드래그 범위 모두 해당 컨테이너를 기준으로 계산됩니다. 컨테이너 요소에는 반드시 `position: relative`(또는 `absolute`/`fixed`)와 `overflow: hidden`이 필요합니다.

### Common option combinations

| 사용 시나리오 | 설정 |
| --- | --- |
| 드래그 없이 버튼으로만 열고 닫기 | showHandlebar={false} |
| tip 없이 half/hidden만 사용 | withoutTip={true} |
| 고정 높이 시트 (높이 변동 없음) | half={300} max={300} |
| 특정 컨테이너 안에서 동작 | containerRef={ref} (컨테이너에 position: relative 필요) |
| TopAppBar 아래 영역을 max로 사용 | maxType="topAppBar" |

### Props reference

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | ReactNode | 필수 | 슬롯 컴포넌트 조합 (Header, Content, Footer) |
| state | 'hidden' \| 'tip' \| 'half' \| 'max' | - | 제어 모드에서 현재 디텐트 상태 |
| defaultState | 'hidden' \| 'tip' \| 'half' \| 'max' | - | 비제어 모드 초기 디텐트 상태 |
| onChange | (state) => void | - | 디텐트 변경 시 호출되는 콜백 |
| dimmed | boolean | true | 배경 딤 처리 여부. true이면 배경 스크롤도 차단 |
| showHandlebar | boolean | true | 핸들바 표시 여부. false이면 드래그 불가 |
| withoutTip | boolean | false | tip 디텐트 비활성화. half ↔ hidden만 사용 |
| half | number \| (base) => number | 자동 계산 | half 디텐트 높이 또는 보정 함수 |
| max | number \| (base) => number | 자동 계산 | max 디텐트 높이 또는 보정 함수 |
| tip | number \| (base) => number | Header 높이 | tip 디텐트 높이 또는 보정 함수 |
| maxType | '86%' \| 'topAppBar' | '86%' | max 높이 계산 기준 |
| containerRef | RefObject<HTMLElement> | - | 컨테이너 기준 모드. 지정 시 해당 요소 안에서만 동작 |
| portalContainer | Element \| null | document.body | 포털 렌더링 대상 요소 |
| withShadow | boolean | true | 시트 상단 그림자 표시 여부 |
| className | string | - | 추가 CSS 클래스 |

`HTMLMotionProps<'div'>`도 함께 전달할 수 있습니다 (framer-motion props).

---

## Accordion

여러 섹션을 접고 펼칠 수 있는 아코디언 컴포넌트입니다.

`useAccordion` 훅으로 상태를 제어하며, `single`/`multiple` 옵션에 따라 한 번에 하나만 열거나 여러 개를 동시에 열 수 있습니다. `openValues`/`onOpenChange`를 제공하면 controlled 모드로 동작합니다.

### Variants / behaviors
- **Single (하나만 열기)** — `options="single"`일 때 한 번에 하나만 열 수 있으며, 모두 닫힌 상태도 가능합니다. `defaultOpenValues`로 초기 오픈 상태를 설정할 수 있습니다. `data-open` 속성을 활용해 트리거 아이콘 회전 등 상태별 스타일을 적용할 수 있습니다.
- **Multiple (여러 개 열기)** — `options="multiple"`일 때 여러 아이템을 동시에 열 수 있습니다.
- **Manual (직접 제어)** — `behavior="manual"`로 트리거의 자동 토글을 끄고 원하는 요소에서 `toggleItem`을 호출합니다. 버튼, 아이콘 등 특정 영역만 클릭 가능하도록 구성할 때 사용합니다.

### Anatomy / slots
- **`Accordion`** — 전체 컨테이너
- **`Accordion.Item`** — 개별 아이템
- **`Accordion.Trigger`** — 아이템 헤더 영역
- **`Accordion.Content`** — 펼쳐지는 콘텐츠 영역

**Trigger Slots**
- `Accordion.Trigger.LeadingIconSlot` — 좌측 아이콘 영역
- `Accordion.Trigger.Label` — 타이틀 영역
- `Accordion.Trigger.TrailingCompSlot` — 배지, 버튼 등 보조 요소 영역
- `Accordion.Trigger.TrailingIconSlot` — 우측 아이콘 영역

### Props reference

#### Accordion

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| accordion | AccordionController | - (필수) | useAccordion 반환값 |
| children | ReactNode | - | Accordion.Item 목록 |
| className | string | - | 추가 클래스 |

#### Accordion.Item

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| value | string | - (필수) | 아이템 식별자 |
| children | ReactNode | - | Accordion.Trigger + Content 조합 |
| className | string | - | 추가 클래스 |

#### Accordion.Trigger

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| behavior | 'auto' \| 'manual' | 'auto' | auto는 클릭 시 자동 토글, manual은 직접 제어 |
| children | ReactNode | - | 슬롯 조합 |
| className | string | - | 추가 클래스 |

#### Accordion.Content

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| children | ReactNode | - | 콘텐츠 내용 |
| className | string | - | 추가 클래스 |

#### useAccordion

| Prop | Type | Default | Description |
| --- | --- | --- | --- |
| options | 'single' \| 'multiple' | - (필수) | 동작 방식 선택 |
| defaultOpenValues | string[] | [] | 기본으로 열릴 아이템 목록 |
| openValues | string[] | - | controlled 모드의 열린 아이템 목록 |
| onOpenChange | (values: string[]) => void | - | 열린 아이템 변경 콜백 |

---

## Pattern

페이지 단위 인터랙션을 패턴 형태로 제공합니다.
- **Carousel Pattern** — CarouselEngine으로 슬라이드/배너를 제어하는 패턴
- **Anchor Pattern** — 콘텐츠 섹션 앵커링 패턴 (추가 예정)

### Carousel Pattern

`Pattern` 컴포넌트에 `type="carousel"`을 지정하면 `CarouselEngine`의 포인터 이벤트와 트랜지션을 연결하는 뷰가 렌더링됩니다. `useCarousel` 훅을 이용해 엔진을 React 사이클에 연결하면 슬라이드/배너/상품 카드 등 반복 콘텐츠를 쉽게 배치할 수 있습니다.

#### When to use
- 슬라이드, 배너, 상품 카드 등 반복 콘텐츠를 가로로 넘기며 탐색할 때.
- 드래그/스와이프 제스처, 도트 내비게이션, 자동 재생 배너가 필요할 때.

#### Patterns / capabilities
- **기본 예제: 드래그 + 도트 내비게이션** — `useCarousel`에서 `engine`/`currentIndex`/`move`를 받아서 버튼·도트와 연결합니다. `autoPlay + loop` 조합으로 순환 배너를 만들고, 드래그 제스처는 `draggable` 플래그만 켜면 됩니다. (드래그와 터치 제스처를 지원해 모바일에서 자연스럽게 넘길 수 있습니다.)
- **옵션 제어: loop, gap, animation** — `engine.updateOptions`로 런타임에 gap/loop/autoPlay/animation을 업데이트할 수 있습니다. 옵션을 바꾼 뒤 `engine.syncPosition(true)`를 호출해 새로운 gap/애니메이션을 바로 반영합니다.
- **API 데이터 렌더링** — 외부 API로 가져온 데이터를 슬라이드로 매핑합니다. 로딩/에러 상태에서 Skeleton과 안내 메시지를 노출합니다.
- **커스터마이즈 스타일링** — `Pattern`(`type="carousel"`)은 data-role을 노출합니다: `item-container`, `item-wrapper`, `item`. Tailwind Arbitrary Selector(`&_[data-carousel-role='item']` 등)를 이용해 높이·보더·간격을 자유롭게 커스터마이즈할 수 있습니다.
- **onIndexChange로 상태 연동** — `onIndexChange` 콜백에서 `setState`를 호출해도 엔진/슬라이드 애니메이션은 유지됩니다 (`useCarousel`이 내부 `CarouselEngine` 인스턴스를 `useRef`로 고정해두기 때문).

#### Usage do & don't
- **Don't** — `items` 배열을 매 렌더마다 새로 만들면(예: `map`을 렌더 안에서 실행) 슬라이드가 재구성되며 애니메이션이 초기화될 수 있습니다. `useMemo`/상수로 고정하세요.

#### Customization data-roles
`Pattern`(`type="carousel"`)이 노출하는 data-role: `item-container`, `item-wrapper`, `item`. (예: `data-carousel-role='item'`)

#### Example copy
- 「커스텀 / 외부 제어」 — 「외부에서 move/scrollTo를 호출해 인디케이터, 버튼 등과 연동합니다.」
- 「예약 / 드래그 가능한 슬라이드」 — 「드래그와 터치 제스처를 지원해 모바일에서 자연스럽게 넘길 수 있습니다.」
- 「운영 / 자동 재생」 — 「loop + autoPlay 조합으로 반복 배너나 피처 하이라이트를 만들 수 있습니다.」
- 옵션 제어 라벨: 「Loop — 끝없이 순환하는 배너」 · 「Gap — 슬라이드 간격 조절」 · 「Animation — 이징 프리셋 변경」 (gap: 12px / 현재 인덱스 **1 / 3**)
- API 데이터 예시: 「포인트 / 주행 리워드 — 장거리 100km마다 1,000P 적립」 · 「예약 혜택 / 평일 렌트 할인 — 주중 대여 20% OFF」 · 「신규 / EV 보너스 — 전기차 첫 대여 추가 크레딧」
