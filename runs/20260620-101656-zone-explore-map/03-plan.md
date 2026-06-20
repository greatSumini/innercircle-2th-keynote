---
run: 20260620-101656-zone-explore-map
stage: plan
status: ready
frame: 360 x 800 mobile portrait
---
# Design plan — 쏘카존 탐색

## Overview
- Goal / primary job: 검색 결과 지역의 풀스크린 지도 위에서 주변 쏘카존·차량을 빠르게 훑어보고
  1대를 골라 상세로 진입한다. 정보 밀도가 높아도 위계로 정돈해 "빠른 선택"을 돕는 것이 핵심.
- Primary action (emphasized): **차량 리스트 카드 탭 → 차량 상세 진입.** 이 화면의 단일 핵심 행동은
  버튼이 아니라 "카드 한 장을 고르는 것"이므로, 강조는 (a) 지도에서 선택된 핀 1개와
  (b) 그에 대응하는 BottomSheet 최상단 카드(`primary-regular` 1px 보더 + 가벼운 강조)로 표현한다.
  (전역 풀폭 CTA 버튼은 두지 않는다 — 선택 자체가 다음 화면을 여는 행동.)
- Surface: full screen (풀스크린 지도) + 그 위에 오버레이된 TopAppBar(상단 요약 바) · 가로 스크롤
  필터 칩 · half 디텐트 BottomSheet(차량 리스트). 단일 화면, 모달 아님.

## Frame
- Size: **360 x 800** (SOCAR 모바일 베이스라인 360 너비. 동일 파일 `[auto] 반납 완료` 프레임
  360×857 컨벤션과 맞추되, 지도 풀블리드+half 시트 비율을 위해 높이 800으로 확정.)
- 풀블리드 지도 배경: 프레임 (0,0)~(360,800) 전체를 지도 placeholder가 덮는다(상태바·여백 없이
  edge-to-edge). 상단 바/필터/시트는 모두 지도 위 오버레이.
- TopAppBar(상단 요약 바): 지도 위 floating, 좌우 `spacing-400`(16) 인셋, 상단에서 `spacing-200`(8)
  띄운 흰 카드형 바. 높이 약 56(1줄)~64(검색어+일시 2줄). 시인성 위해 white 표면 + 약한 그림자.
- 필터 Chip 행: TopAppBar 아래 `spacing-300`(12) 간격, 좌우 풀블리드(좌측 인셋 `spacing-400`),
  가로 스크롤(잘림 암시 위해 우측 칩 일부 노출).
- 내 위치 FAB(IconButton): 시트 상단선 바로 위 우측, 우측 인셋 `spacing-400`, 시트와 `spacing-300` 간격.
- BottomSheet(half 디텐트): 화면 하단에 고정, 상단 라운드 `radius-400`(16). half 높이 = 프레임의
  약 56%(상단 y≈352, 하단 800까지 ≈448px). 핸들바 + 헤더는 고정, 카드 리스트는 시트 안에서 스크롤
  (시각적으로 2.5장 노출되어 "더 있음"을 암시). dimmed=false — 지도 상호작용 유지.
- Safe areas: 하단 시트가 홈 인디케이터 영역까지 채우므로 시트 콘텐츠 하단 패딩 `spacing-400` 확보.

## Layout (top → bottom)

| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 1 | 지도 배경 (custom) | — (gap: 풀스크린 지도 placeholder) | fill `background-regular`(#F2F3F8) 베이스 + 저대비 도로/구획 stroke `divider-regular`; 물/공원 면은 `status-positive-weak`/`status-information-weak` 옅게 / 풀블리드 | 도로 격자·블록 면을 암시하는 지도 placeholder. raw hex 금지, 토큰만. |
| 2 | 쏘카존 핀 마커들 (custom) | — (gap: 지도 핀, IconButton 아님) | 기본 핀 fill `location-rental`(#0078FF) + white 외곽 2px; 선택 핀 fill `primary-strong`(#0069FF) 확대(1.4x)+white 링+그림자, 가격 말풍선 / 핀 라운드 `radius-circle` | 지도 위 5개 핀(`icon-locationpin-fill` 형태). 그중 1개는 선택 강조 + "₩9,900~" pill 라벨. 나머지 4개 기본. |
| 3 | 내 위치 FAB | IconButton · medium [aria-label=내 위치] | white 표면 + `border-regular` 1px + 그림자 / 아이콘 `text-primary` / `radius-circle` / 44x44 | `icon-my-location-line`. 지도 우하단(시트 위) 떠 있는 원형 버튼. |
| 4 | TopAppBar (상단 요약 바) | TopAppBar · general (LeftSideIconSlot + BasicBackButton, Title은 label형 2줄) | 표면 white + `radius-300` + 그림자 / 내부 패딩 좌우 `spacing-400` 상하 `spacing-200` / 좌우 화면 인셋 `spacing-400` | 좌: 뒤로가기 IconButton. 가운데(좌측 정렬 label): 1줄 검색어(굵게) + 2줄 이용 일시(보조). 우: 검색 재진입 IconButton(`icon-search-line`). |
| 4a | ↳ 뒤로가기 | IconButton · medium [aria-label=뒤로가기] | 아이콘 `text-primary` / 투명 배경 / 44x44 터치 | `icon-chevron-left-line`. |
| 4b | ↳ 검색어 줄 (text) | text · title3 | `text-strong` / `title3`(14, SemiBold) | "강남역 2번 출구" |
| 4c | ↳ 이용 일시 줄 (text) | text · body4 | `text-secondary` / `body4`(13) / 검색어와 `spacing-50`(2) 간격 | "6/20(토) 14:00 ~ 6/21(일) 14:00" |
| 4d | ↳ 검색 재진입 | IconButton · medium [aria-label=검색 수정] | 아이콘 `text-secondary` / 투명 배경 / 40x40 | `icon-search-line`. |
| 5 | 필터 Chip 행 (가로 스크롤) | Chip · role=button/size=medium (선택/기본) ×4~5 | 칩 간격 `spacing-200`(8) / 행 좌측 인셋 `spacing-400`, 상하 `spacing-300`(12) / pill `radius-circle` | 좌→우: [전체 필터], [차종 ▾], [경차], [SUV], [전기차], [가격 ▾], [즉시예약]. 선택된 칩 1개 강조. |
| 5a | ↳ 전체 필터 Chip | Chip · button/medium [leftIcon=icon-filter-line] | white 표면 + `border-regular` / `text-secondary` / `title4` | "필터" (아이콘 칩, 전체 필터 진입). |
| 5b | ↳ 즉시예약 Chip (selected) | Chip · button/medium · selected [leftIcon=icon-bolt-fill] | 선택: `status-information-weak`(#EBF5FF) 표면 + `primary-regular` 1px 보더 + `primary-regular` 텍스트/아이콘 / `title4` | "즉시예약" (이 화면에서 선택된 필터 1개). |
| 5c | ↳ 기본 Chip들 | Chip · button/medium (default) | white 표면 + `border-regular` 1px / `text-secondary` / `title4` | "차종", "경차", "SUV", "전기차", "가격". (▾ 칩은 `icon-chevron-down-line` rightIcon) |
| 6 | BottomSheet 셸 (half) | BottomSheet · half (showHandlebar, dimmed=false, withShadow) | 표면 white / 상단 라운드 `radius-400`(16) / 상단 그림자 / 좌우 콘텐츠 패딩 `spacing-400` | half 디텐트 고정. 핸들바 + Header + 스크롤 Content. |
| 6a | ↳ 핸들바 | — (custom, BottomSheet.Handlebar) | fill `gray-300`(#CBD1DC, divider급) / pill `radius-circle` / 36x4 / 상단 패딩 `spacing-300`(12) | 시트 상단 중앙 드래그 핸들. |
| 6b | ↳ 시트 헤더 (BottomSheet.Header) | BottomSheet.Header / Title(Label) + Subtitle | 헤더↔리스트 `spacing-300`(12) / 핸들바↔헤더 `spacing-200`(8) | 좌: "내 주변 12대" (대수 강조). 우: "거리순 ▾" 정렬 TextButton. 아래 보조줄: "강남역 반경 1km". |
| 6b-1 | ↳↳ 헤더 타이틀 (text) | text · title1 | `text-strong` / `title1`(18) — 숫자 "12"는 동일 스타일 유지 | "내 주변 **12**대" |
| 6b-2 | ↳↳ 정렬 토글 | TextButton · text/tertiary/small [rightIcon=icon-chevron-down-line] | `text-secondary` / `title4` | "거리순" |
| 6b-3 | ↳↳ 헤더 보조줄 (text) | text · caption1 | `text-tertiary` / `caption1`(12) / 타이틀과 `spacing-50` | "강남역 반경 1km" |
| 6c | ↳ 차량 카드 리스트 (BottomSheet.Content, scroll) | 차량 카드 (custom) ×N | 카드 간 세로 간격 `spacing-300`(12) | 선택 강조 1장 + 일반 카드들. 첫 카드는 선택 핀과 대응(강조). |
| 6c-1 | ↳↳ 차량 카드 · 선택됨 (custom) | 차량 카드 (custom) · selected | white 표면 + `primary-regular`(#0078FF) 1px 보더 + `radius-300`(12) / 내부 패딩 `spacing-400`(16) | 강조 카드 (지도 선택 핀과 1:1). 아래 카드 anatomy 참조. |
| 6c-2 | ↳↳ 차량 카드 (custom) | 차량 카드 (custom) · default | white 표면 + `border-regular` 1px + `radius-300`(12) / 내부 패딩 `spacing-400`(16) | 일반 카드. 동일 anatomy. |

### 차량 카드 (custom) anatomy — 한 카드 내부 (좌→우, 위→아래)
| Sub | 요소 | type / color | spacing |
|-----|------|--------------|---------|
| L | 차량 썸네일 (custom, placeholder) | 64x64 사각, `background-regular` 면 + `icon-car-fill` `text-tertiary` 중앙 / `radius-200`(8) | 썸네일↔텍스트 `spacing-300`(12) |
| R1 | 모델명 + 상태 Tag (행) | 모델명 `title2`(16) `text-strong`; Tag는 우측 정렬 | 모델명↔Tag `spacing-200`(8), 행 하단 `spacing-100`(4) |
| R2 | 쏘카존 이름 + 도보 거리 (행) | 쏘카존명 `body3`(14) `text-secondary` · 구분점 `text-tertiary` · 도보거리 `caption1`(12) `text-secondary` (leftIcon `icon-locationpin-fill` 12px) | 행 하단 `spacing-150`(6) |
| R3 | 시간당 요금 (행) | 숫자 `title2`(16) `text-strong` + 단위 "원/시간" `body4`(13) `text-secondary` | — |

상태 Tag 매핑 (Tag · size=small, shape=capsule):
- 즉시예약/추천 → `status-information-weak`(#EBF5FF) 배경 + `status-information-regular`(#0078FF) 텍스트. "즉시예약"
- 할인 → `status-positive-weak`(#E6FEF0) 배경 + `status-positive-regular`(#04CA81) 텍스트. "15% 할인"
- 만차/마감임박 → `status-negative-weak`(#FFF0F3) 배경 + `status-negative-regular`(#FF3A5B) 텍스트. "예약 마감임박"
- Tag 텍스트는 `caption1`(12, SemiBold).

## Copywriting (verbatim)
모든 텍스트는 SOCAR 보이스(명확·따뜻·간결). 줄바꿈은 break-keep으로 단어 중간 분리 금지.

상단 요약 바
- 검색어 (title3): "강남역 2번 출구"
- 이용 일시 (body4): "6/20(토) 14:00 ~ 6/21(일) 14:00"

필터 칩 (title4)
- "필터" · "차종" · "경차" · "SUV" · "전기차" · "가격" · "즉시예약"

시트 헤더
- 타이틀 (title1): "내 주변 12대"
- 정렬 토글 (title4): "거리순"
- 보조줄 (caption1): "강남역 반경 1km"

차량 카드 (기본 상태 — 3장)
- 카드1 (선택됨)
  - 모델명 (title2): "더 뉴 아반떼"
  - 상태 Tag (caption1): "즉시예약"
  - 쏘카존 (body3): "강남역 2번 출구 쏘카존"
  - 도보 거리 (caption1): "도보 3분"
  - 요금 (title2 + body4): "9,900원/시간"
- 카드2
  - 모델명 (title2): "레이"
  - 상태 Tag (caption1): "15% 할인"
  - 쏘카존 (body3): "역삼동 공영주차장 쏘카존"
  - 도보 거리 (caption1): "도보 6분"
  - 요금 (title2 + body4): "7,500원/시간"
- 카드3
  - 모델명 (title2): "아이오닉 5"
  - 상태 Tag (caption1): "예약 마감임박"
  - 쏘카존 (body3): "테헤란로 GS타워 쏘카존"
  - 도보 거리 (caption1): "도보 9분"
  - 요금 (title2 + body4): "12,000원/시간"

지도
- 선택 핀 가격 말풍선 (caption1, white text): "9,900원~"

빈 상태 (별도 프레임)
- 일러스트/아이콘: `icon-car-search-line` (`text-tertiary`)
- 제목 (title1): "주변에 이용 가능한 차량이 없어요"
- 본문 (body2): "이용 날짜·시간을 바꾸거나 검색 범위를 넓혀\n다시 찾아보세요." (break-keep, 단어 중간 분리 금지)
- 보조 CTA (ActionButton): "조건 변경하기"
- 보조 링크 (TextButton): "필터 초기화"

## Color & emphasis
- Background: 지도 베이스 `background-regular`(#F2F3F8); 모든 표면(상단 바·시트·카드·FAB) white.
- 텍스트 위계: 모델명·시트 타이틀·요금 숫자 `text-strong` > 쏘카존명 `text-secondary` >
  도보거리·보조줄 `text-tertiary`. 위계로 "정보 많아도 정돈됨"을 만든다.
- 강조 (정확히 하나의 핵심):
  - **선택 핀 1개** — `primary-strong` + 확대 + white 링 + 그림자 + 가격 말풍선.
  - **선택된 카드 1장** — `primary-regular` 1px 보더(나머지 카드는 `border-regular` 중립).
  - 이 둘이 시각적으로 짝을 이뤄 "지도-리스트 연결"을 보여주는 와우 디테일.
- 보조 강조: 필터 선택 칩 1개(`status-information-weak` + `primary-regular` 보더), 상태 Tag는
  `status-*-weak` 배경이라 카드를 압도하지 않음.
- 의도적 디엠퍼시스: 지도 도로/구획선은 `divider-regular`로 저대비 — 핀과 시트가 주인공.
  요금 강조에 브랜드색을 쓰지 않고 `text-strong`만 사용(브랜드색 남용 금지, 선택 강조와 충돌 방지).
- 정렬 토글·정렬 라벨 등 보조 컨트롤은 `text-secondary`로 낮춘다.

## States
- **기본** (`[auto] 쏘카존 탐색 · 기본 — 20260620-101656-zone-explore-map`):
  지도+핀(선택 1)+상단 바+필터 칩+half 시트(헤더 "내 주변 12대" + 카드 3장, 첫 카드 선택 강조).
  카드 탭 → 차량 상세(스코프 외 화면).
- **빈 상태** (`[auto] 쏘카존 탐색 · 빈 상태 — 20260620-101656-zone-explore-map`):
  지도·상단 바·필터 칩은 동일 유지(맥락 보존), 지도 핀은 0개(또는 흐린 빈 지도). half 시트 안에서
  헤더는 "내 주변 0대"로 두지 않고 빈-상태 블록으로 대체:
  - 중앙 정렬 `icon-car-search-line`(`text-tertiary`, 56px) → `spacing-300`
  - 제목 `title1`(`text-strong`): "주변에 이용 가능한 차량이 없어요" → `spacing-200`
  - 본문 `body2`(`text-secondary`, 2줄, break-keep): "이용 날짜·시간을 바꾸거나 검색 범위를 넓혀
    다시 찾아보세요." → `spacing-400`
  - 보조 CTA `ActionButton · fill/secondary/medium`(`title3`, `radius-300`): "조건 변경하기"
    (빈 상태에서 회복 경로 = 보조 강조. fill/secondary로 두어 전역 화면 톤과 충돌 없음)
  - 그 아래 `TextButton · text/tertiary/small`(`text-secondary`): "필터 초기화"
  - 시트 콘텐츠 세로 중앙 정렬, 좌우 패딩 `spacing-400`.
- Loading/Error: 이번 스코프 외(clarify Out). 빌드하지 않음.

## Accessibility
- 최소 터치 타깃 44x44: 뒤로가기·검색·내 위치 IconButton, 칩, 카드 전체(탭 타깃), 정렬 토글.
- 아이콘 단독 버튼은 모두 `[aria-label=…]` 부여(뒤로가기/내 위치/검색 수정).
- 대비: 지도(밝은 배경) 위 핵심 정보는 white 표면 카드/바 위에 `text-strong`/`text-primary`로 올려
  야외 시인성 확보(Context & Safety 원칙). 선택 핀은 white 링으로 지도 위 대비 보강.
- 텍스트 가독성: 본문 최소 `caption1`(12) 이상, 모델명/요금은 `title2`(16)로 한 손 스캔 용이.
- 색만으로 상태 전달하지 않음: 상태 Tag는 색 + 텍스트 라벨("즉시예약"/"할인"/"마감임박") 병기.
- 한 손 조작: 핵심 선택 영역(시트 카드)이 화면 하단 절반에 위치 — 엄지 도달 범위.

## Figma placement (parallel batch lane)
- Page: 활성 페이지 `Page 1`. **새 페이지 만들지 않음.**
- Reserved lane: top-level 프레임을 **x=4200, y=0**부터 좌→우로 배치, **80px 거터**, 공유 top edge(y=0).
  - `[auto] 쏘카존 탐색 · 기본 — 20260620-101656-zone-explore-map` @ x=4200, y=0 (360×800, leftmost).
  - `[auto] 쏘카존 탐색 · 빈 상태 — 20260620-101656-zone-explore-map` @ x=4640, y=0 (4200 + 360 + 80).
- 가능하면 두 프레임을 Section `[auto] 쏘카존 탐색 — 20260620-101656-zone-explore-map`으로 감싼다
  (불가 시 행 배치 폴백). 기존 `[auto] 반납 완료`(x≈200) 및 다른 배치 세션과 겹침 없음.
- Local variable collection `socarframe` 생성 후 이 화면이 쓰는 color(특히 `location-rental`,
  `primary-regular/strong`, `status-information/positive/negative-weak·regular`, `text-strong/
  secondary/tertiary`, `background-regular`, `border-regular`, `divider-regular`) + radius/spacing
  변수를 만들고 최소 color를 바인딩. 폰트는 Pretendard 전체 weight(600 유지).

## Out of scope
- 실제 지도 타일/지오 데이터·핀 클러스터링(placeholder만).
- 검색 입력 화면, 날짜·시간 선택(DatePicker/TimePicker) 플로우.
- 차량 상세·예약·결제 화면.
- BottomSheet tip/max 디텐트 전환, 실시간 드래그 인터랙션(시각 상태 half 1종만).
- 로딩/에러 상태 프레임.
- 지도 사용자 위치 추적 로직(내 위치 FAB는 시각 노출만).
