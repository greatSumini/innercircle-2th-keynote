---
run: 20260620-101656-zone-explore-map
stage: context
status: ready
figma_library_available: no
---
# Context pack

쏘카존 탐색(map explore): 풀스크린 지도(플레이스홀더) 배경 위에 상단 요약 바 + 가로 스크롤 필터
칩 + half 디텐트 BottomSheet(차량 리스트)가 오버레이된 단일 모바일 포트레이트 화면. 핵심 과업은
"주변 차량을 빠르게 훑어보고 1대를 골라 상세로 진입". 정보 밀도가 높으므로 socarframe 시맨틱 토큰과
기존 컴포넌트 패턴을 최대한 재사용하고, 지도/핀/시트 셸은 primitive로 커스텀 빌드한다.

socarframe은 이 파일에 **바인딩된 Figma 라이브러리가 아니다** (아래 라이브러리 상태 참고). 따라서
모든 토큰은 값으로 적용하고, 의도는 figma-conventions의 레이어 네이밍으로만 추적된다. 동일 파일의
기존 하베스트 프레임 `[auto] 반납 완료`가 이 규칙(360 너비, 토큰 괄호 표기, spacer/divider 명명)을
이미 따르고 있으므로 그 스타일을 그대로 맞춘다.

## Design-system references
- Docs to follow:
  - `color.md` — text-* / primary-* / status-* / background-border-divider / **location-rental·return**
  - `typography.md` — heading*/title*/body*/caption* + Pretendard 빌드 정책(600 유지)
  - `spacing.md` — spacing-400 화면 패딩, 카드 radius-300, 시트 radius-400
  - `components-surfaces.md` — **BottomSheet**(half 디텐트, showHandlebar, dimmed=false), **TopAppBar**(LeftSideIconSlot+BasicBackButton, label형 Title)
  - `components-forms.md` — **Chip**(role=button, size=medium, selected 상태)
  - `components-feedback.md` — **Tag**(상태 태그), 보조로 Badge/Skeleton
  - `components-actions.md` — **IconButton**(뒤로가기/내 위치), TextButton(필터 초기화·전체보기), ActionButton(빈 상태 보조 CTA)
  - `icons.md` — 아이콘 토큰명(아래 표 참조)
  - `principles.md` — 정보 정돈 / one-primary-action / 빠른 선택 톤 점검
- Key tokens for this screen:
  - **Color**
    - 화면 배경(지도 아래/시트 영역): `background-regular` (#F2F3F8)
    - 표면(상단 바·시트·카드): `white` 표면 + `border-regular`/`divider-regular` 구분선
    - 텍스트 위계: 모델명·헤더 `text-strong`, 본문/값 `text-primary`, 라벨·도보거리 `text-secondary`, 보조 `text-tertiary`
    - 요금 강조(시간당 요금 숫자): `text-strong` (브랜드색 남용 금지)
    - 핀 마커: 기본 핀 `location-rental` (#0078FF) — 쏘카존/대여 위치 의미와 일치. 선택 핀은 `primary-strong`/`primary-heavy`로 강조 + 확대 + white 외곽.
    - 필터 Chip 선택 상태: 강조는 `primary-regular` 계열(텍스트/보더), 비선택은 white 표면 + `border-regular` + `text-secondary`
    - 상태 Tag 색: 즉시예약/추천 → `status-information-weak`+`status-information-regular`(파랑) 또는 `accent-*`; 할인 → `status-positive-weak`+`status-positive-regular`; 만차/마감 → `status-negative-weak`+`status-negative-regular` (정확 매핑은 plan)
    - 내 위치/필터 아이콘 버튼: white 표면 + `text-primary` 아이콘
  - **Type**
    - 시트 헤더 "내 주변 OO대" → `title1`(18) 또는 `heading3`(22)는 plan 판단 / 강조 숫자 동일 스타일
    - 상단 바 검색어(주요 줄) → `title3`(14, SemiBold) / 날짜·시간 요약(보조 줄) → `body4` 또는 `caption1`
    - 차량 카드: 모델명 `title2`(16) · 쏘카존명 `body3`(14) · 도보거리/부가정보 `caption1`(12) · 시간당 요금 숫자 `title2`/`title1` + "/시간" 단위는 `caption1`/`body4`
    - 필터 Chip 라벨 → medium size 기본 타이포(요청 토큰 표기는 `body3`/`title4` 대조 사용)
    - 상태 Tag 텍스트 → `caption1`(12, SemiBold) 권장
    - 빈 상태 안내 제목 `title1`·본문 `body2 text-secondary`
  - **Spacing / radius**
    - 화면 좌우 패딩 `spacing-400`(16); 시트 콘텐츠 좌우도 `spacing-400`
    - 필터 Chip 간 간격 `spacing-200`(8), Chip 행 상하 패딩 `spacing-300`(12)
    - 카드 간 세로 간격 `spacing-300`(12), 카드 내부 패딩 `spacing-400`(16)
    - 카드 내 텍스트 그룹 간 `spacing-100`/`spacing-150`, 행 간 `spacing-200`
    - 시트 핸들바 영역 상단 패딩 `spacing-300`, 헤더↔리스트 `spacing-300`/`spacing-400`
    - 카드/표면 라운드 `radius-300`(12px); BottomSheet 상단 라운드 `radius-400`(16px); Chip/Tag/핀 = `radius-circle`(pill); 내 위치 FAB = `radius-circle`

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | general / LeftSideIconSlot + BasicBackButton, Title은 label형(검색어+날짜·시간 2줄) | 상단 요약 바(뒤로가기+검색어/이용 일시) | components-surfaces.md | 없음 — DS 라이브러리 미바인딩, primitive로 빌드 (기존 `[auto] 반납 완료`의 `TopAppBar (general …)` 패턴 따라) |
| IconButton | medium / icon-chevron-left-line (또는 icon-arrow-left-line) | 뒤로가기 (aria-label=뒤로가기) | components-actions.md | 없음 — 커스텀 빌드 (기존 프레임의 `IconButton (medium / …) · aria-label=…` 패턴 재사용) |
| IconButton | medium / icon-my-location-line | 지도 위 '내 위치' FAB (노출 plan 재량) | components-actions.md | 없음 — 커스텀 빌드 |
| Chip | role=button, size=medium, selected/default | 필터(차종 경차·SUV·전기차 / 가격 / 즉시예약) 가로 스크롤 | components-forms.md | 없음 — 커스텀 빌드 (pill, white/선택 강조) |
| BottomSheet | half 디텐트, showHandlebar=true, dimmed=false, radius-400 상단 라운드, Header+Content | 하단 차량 리스트 시트(셸) | components-surfaces.md | 없음 — 커스텀 빌드 (실시간 드래그 X, 시각적 half 상태 1종) |
| Tag | size=small/xsmall, shape=capsule, status-* 색 | 차량 카드 상태 태그(즉시예약/할인/만차 등) | components-feedback.md | 없음 — 커스텀 빌드 |
| TextButton | text / tertiary or primary / small | 필터 '초기화'·시트 '전체 보기'·빈 상태 '필터 초기화' | components-actions.md | 없음 — 커스텀 빌드 (기존 프레임 `TextButton (text / tertiary / medium)` 패턴) |
| ActionButton | fill / primary or secondary / medium | 빈 상태 보조 CTA(예: '조건 변경하기') — 보너스 프레임에서만 | components-actions.md | 없음 — 커스텀 빌드 (기존 프레임 `ActionButton (fill / primary / large)` 패턴) |
| Skeleton | (옵션) capsule/rectangle | 로딩 표현이 필요하면 — scope상 out, 참고만 | components-feedback.md | 없음 |
| Icons | icon-chevron-left-line, icon-my-location-line, icon-locationpin-fill / icon-location-shape-fill (핀), icon-car-fill, icon-clock-line, icon-search-line, icon-bolt-fill(전기차/즉시), icon-filter-line | 상단/지도/카드/필터 | icons.md | SOCAR Icon Library 미바인딩 — 벡터로 커스텀 작도, 토큰명으로 레이어 명명 |

> 주: 위 컴포넌트는 모두 socarframe **사양상 재사용 대상**이지만, 이 파일에 socarframe이 바인딩되어
> 있지 않으므로 implement는 instance가 아니라 **사양에 맞춰 primitive로 빌드**하고, 레이어명에
> `ComponentName · variant [token=value]` 표기로 추적성을 확보한다 (figma-conventions §3).

## Figma library & reference status
- **Library available: no.** `get_libraries`(file VuBHVaAnA5ORacxMZ9zcH8) 결과 구독된 라이브러리는
  Material 3 Design Kit, Simple Design System, iOS/iPadOS 18·26, watchOS/visionOS/macOS 26뿐 —
  **socarframe / SOCAR Icon Library 없음.** `libraries_available_to_add`도 비어 있음.
- **search_design_system("BottomSheet TopAppBar Chip Tag card map pin")** 결과: socarframe 자산
  0건. 외부 라이브러리의 무관한 항목만 반환됨(`IONIcon/P/pin/sharp` @ Awesome Design System,
  `ConfirmDialog` @ LIBRARY). 변수/스타일 매칭 0건. → **socarframe 컴포넌트 키를 쓸 수 없음.**
- **Existing frames / placement:**
  - 활성 페이지 `0:1 Page 1`에 기존 하베스트 프레임 1개:
    `[auto] 반납 완료 — 20260620-070646-return-complete` (id 3:2) @ x=200, y=0, **360×857**.
    그 외 다른 페이지/프레임 없음.
  - **참고(스타일 매칭) 스크린:** 위 반납 완료 프레임. 확인된 스타일 컨벤션 — 360 너비 모바일 프레임,
    `background-regular` 화면 배경, white 카드 + `radius-300`, `heading2` 제목 / `body2 text-secondary`
    본문 / `title2`·`title3` 라벨·값, `primary-regular` 풀폭 CTA, 토큰을 레이어명 괄호로 표기
    (`(status-positive-weak, radius-full)`, `(heading2 / text-strong)`), spacer 프레임/divider를
    토큰명으로 명명. 새 화면도 동일 컨벤션·360 너비·동일 톤으로 맞춘다.
  - **권장 배치(figma-conventions §2 + 요청 reserved lane 준수):** 활성 페이지 `Page 1`에 새 프레임을
    요청 지정 lane **x=4200, y=0**부터 좌→우로: `기본`(leftmost) → `빈 상태`, **80px 거터**, 동일
    top edge(y=0). 기존 반납 완료(x=200~560)와 멀리 떨어져 **겹침 없음**. 2개 상태이므로 둘 다 상태
    세그먼트 라벨(`· 기본`, `· 빈 상태`)을 붙이고, 가능하면 두 프레임을 Section
    `[auto] 쏘카존 탐색 — 20260620-101656-zone-explore-map`으로 감싼다(불가 시 행 배치로 폴백).
  - 프레임명: `[auto] 쏘카존 탐색 · 기본 — 20260620-101656-zone-explore-map`,
    `[auto] 쏘카존 탐색 · 빈 상태 — 20260620-101656-zone-explore-map`.
  - 프레임 크기: 360×780~812 권장(지도 풀블리드 + 하단 시트). 정확 높이는 plan/implement에서 확정.
- **Local variable collection:** implement는 `socarframe` 로컬 컬렉션을 만들어 이 화면이 쓰는
  color(특히 `location-rental`, `primary-*`, `status-*`, `text-*`, `background-regular`,
  `border/divider-regular`) + radius/spacing 변수를 생성·바인딩(최소 color)할 것 (figma-conventions §4).

## Gaps (needs custom build — socarframe가 제공하지 않음)
- **풀스크린 지도 배경(플레이스홀더).** DS에 지도 컴포넌트 없음 → 커스텀. `background-regular`/연한 톤
  사각형 + 도로/구획 라인 암시(저대비 stroke)로 지도 placeholder를 빌드. raw hex 금지, 토큰 사용.
- **쏘카존 핀 마커 + 선택 강조.** DS에 지도 핀 컴포넌트 없음(아이콘 `icon-locationpin-fill`/
  `icon-location-shape-fill`/`icon-spot-fill`은 있으나 마커 컴포넌트는 없음) → 커스텀 핀:
  기본 핀(`location-rental` 채움, white 외곽), 선택 핀(확대 + `primary-strong/heavy` + 그림자/라벨
  말풍선로 강조 1개). 가격/대수 라벨 핀이 필요하면 pill 핀도 커스텀.
- **BottomSheet 셸(half 디텐트, 핸들바, dimmed=false).** socarframe BottomSheet는 React 컴포넌트
  사양만 제공 — Figma 인스턴스 없음 → 시각 셸 커스텀: 상단 `radius-400` 라운드, white 표면, 핸들바
  바(작은 pill, `border-regular`/`gray-300`톤), 상단 그림자, half 높이로 고정. 드래그/디텐트 전환은
  시각 1종(half)만.
- **차량 리스트 카드 (custom).** DS에 '차량 카드' 컴포넌트 없음(SelectionBox/Tag/Chip 조립 가능하나
  전용 카드 없음) → primitive 카드: white 표면 `radius-300`, 좌측 차량 썸네일(placeholder), 모델명
  `title2` / 쏘카존명·도보거리 `body3·caption1 text-secondary` / 시간당 요금 강조 / 상태 Tag, 탭 타깃.
  레이어명 `차량 카드 (custom)` + 토큰 표기.
- **상단 요약 바의 검색어+날짜·시간 2줄 레이아웃.** TopAppBar는 셸로 빌드하고 그 안의 label형
  타이틀(검색어 줄 + 날짜·시간 줄)은 커스텀 조립.
- **아이콘 자산.** SOCAR Icon Library 미바인딩 → 필요한 아이콘은 벡터로 커스텀 작도하고
  `icon-<name>-<fill|line>` 토큰명으로 레이어 명명(기존 반납 완료 프레임과 동일 방식).
- (참고) 빈 상태 일러스트: DS에 전용 일러스트 없음 → 간단한 안내 그래픽/아이콘(`icon-car-search-line`
  등)으로 커스텀. 보너스 프레임 한정.
