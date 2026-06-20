---
run: 20260620-101653-home-main
stage: plan
status: ready
frame: 360 x 800 mobile portrait (×2 states)
---
# Design plan — 홈(메인)

## Overview
- Goal / primary job: 앱 진입 시 처음 보는 홈 화면. 사용자가 **3초 안에** "여기서 차를 예약(검색)한다"를 알게 하고, 진행 중/예정 이용이 있으면 한눈에 확인하고 바로 행동(스마트키/예약 상세)하게 한다.
- Primary action (emphasized): **검색 진입 박스 "어디서 탈까요?"** — 예약(검색) 흐름의 단일 핵심 진입점. `예약 있음` 상태에서는 진행 중 예약 카드의 `스마트키` CTA가 그 맥락 안의 주 행동이고, 화면 전체의 유일한 hero 강조는 검색 박스가 가져간다. (principles: Primary Goal 1개)
- Surface: full screen (스크롤 가능한 단일 풀스크린, 고정 TopAppBar + 고정 BottomNavigation)

## Frame
- Size: **360 x 800** (SOCAR 모바일 portrait 기본; 360 wide는 기존 `[auto] 반납 완료` 레퍼런스 프레임과 동일 폭). 콘텐츠가 길면 800을 넘겨도 무방하나 스펙은 800 viewport 기준으로 above-the-fold를 정의.
- 두 상태 프레임을 만든다(상태 2종이므로 모든 프레임에 상태 세그먼트 부여):
  - `[auto] 홈(메인) · 예약 있음 — 20260620-101653-home-main`  (default, **leftmost**, x=2400 y=0)
  - `[auto] 홈(메인) · 예약 없음 — 20260620-101653-home-main`  (x=2840 y=0 — 2400 + 360 + 80 gutter)
  - 두 프레임을 Figma Section `[auto] 홈(메인) — 20260620-101653-home-main`로 감싼다(상태 세그먼트 없음).
- Safe areas / 고정 영역:
  - **Status bar 영역**: 상단 44px 여백(시간/배터리 자리, 시각 요소만 — 콘텐츠 없음). TopAppBar는 그 아래.
  - **TopAppBar**: 화면 상단 고정, 높이 56px.
  - **Bottom action area**: 화면 하단 고정 **BottomNavigation** 64px + home-indicator 여백 ~20px. 스크롤 콘텐츠는 그 위에서 끝남(마지막 섹션 하단 padding `spacing-600` 확보).
  - 모든 좌우 콘텐츠 인셋: `spacing-400` (16px).

## Layout (top → bottom)

> 순서는 두 상태 공통. ③(예약 카드)만 상태에 따라 교체된다 — 자세한 차이는 `## States` 참고.
> 표의 **Section** 라벨은 figma-conventions의 role 라벨이며 implement가 레이어/프레임 이름으로 재사용한다.

| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 0 | StatusBar (시각용) | — (custom, 비콘텐츠) | bg=`background-regular`; 높이 44 | 시간/신호/배터리 글리프(장식). 접근성 대상 아님. |
| 1 | TopAppBar | TopAppBar (general); LeftSlot=위치 주소, TrailingButtonSlot=알림 IconButton | bg=`white`; 높이 56; 좌우 pad `spacing-400`; 아이템 gap `spacing-100` | 좌측: `icon-location-dot-fill`(primary-regular) + "서울 강남구 역삼동" (`title3`/`text-strong`) + `icon-chevron-down-line`(text-secondary). 우측: 알림 `IconButton` (`icon-bell-line`, medium) + dot Badge(예약 있음 only) |
| 2 | 검색 Hero (검색 진입 박스) | Input anatomy 응용 — **비입력 진입형 surface (custom)** | bg=`white`; `radius-300`; border=`border-regular` 1px; inner pad py `spacing-450`(18) px `spacing-400`(16); 아이콘↔텍스트 gap `spacing-200`; 위 마진 `spacing-300`, 아래 `spacing-500` | `icon-search-line`(primary-regular) + placeholder "어디서 탈까요?" (`body1`/`text-secondary`). 우측 끝 `icon-chevron-right-line`(text-tertiary). hero이므로 살짝 더 큰 surface로 강조. |
| 3 | 진행 중 예약 카드 (예약 있음) / 빈 자리 → 예약 유도 카드 (예약 없음) | **예약 카드 (custom)**: 썸네일 + 텍스트 + Tag(reuse) + ActionButton(reuse); 또는 예약 없음 유도 카드(custom) + ActionButton | card bg=`white`; `radius-300`; pad `spacing-400`; 섹션 아래 `spacing-600` | 상태별로 교체 — `## States` 참고 |
| 4 | 혜택 배너 carousel | Pattern/Carousel 정적 빌드 — **배너 슬라이드 + 도트 (custom)** | slide bg=`status-information-weak`(또는 브랜드 이미지); `radius-400`; pad `spacing-400`; 높이 96; dots row 위 `spacing-200` | 슬라이드(현재 1/3 노출): 타이틀 `title2`/`text-strong` + 서브 `body3`/`text-secondary` + 우측 일러스트 자리. 도트 3개: active=`primary-regular`, inactive=`border-regular`. |
| 5 | 퀵메뉴 그리드 | **아이콘+라벨 4-up 그리드 (custom)** | 타일 bg=`status-information-weak`; `radius-circle`(아이콘 타일 48); 아이콘↔라벨 gap `spacing-150`; 컬럼 gap `spacing-300`; 섹션 위 `spacing-700` 아래 `spacing-600` | 4 항목: 쏘카플랜(`icon-calendar-check-line`) · 부름/편도(`icon-car-line`) · 쿠폰함(`icon-coupon-line`) · 이벤트(`icon-couponset-line`). 라벨 `caption1`/`text-primary`. |
| 6 | BottomNavigation (고정) | **글로벌 탭바 (custom)** | bg=`white`; 상단 `Divider [stroke=divider-regular]`; 높이 64 + home-indicator 20; 아이콘↔라벨 gap `spacing-50` | 4탭: 홈(active `icon-home-fill`/`primary-regular`) · 탐색(`icon-search-line`) · 이용내역(`icon-clock-line`) · 마이(`icon-user-line`). 비활성 아이콘/라벨 `text-tertiary`, 라벨 `caption3`. |

### Section 3 detail — 예약 있음 (진행 중 예약 카드, custom)
- 헤더 행: "이용 중인 차" (`title3`/`text-strong`) — 카드 위 `spacing-300` 마진.
- 카드 내부(세로 auto-layout, gap `spacing-300`):
  - 상단 행(가로, gap `spacing-300`): 차량 썸네일 64×48 `radius-200`(이미지 없으면 `background-regular` 채움 + `icon-car-line`/`text-tertiary`) | 텍스트 컬럼(gap `spacing-100`): 상태 **Tag** `capsule/small` [bg=`status-positive-weak` text=`status-positive-strong`] "이용 중" → 모델명 "아반떼 CN7" (`title2`/`text-strong`) → 이용 시간 "오늘 14:00 – 18:00" (`body3`/`text-secondary`).
  - 쏘카존 행(가로, gap `spacing-100`): `icon-location-dot-fill`(location-rental 12px) + "강남 더클래스효성 쏘카존" (`body3`/`text-secondary`).
  - `Divider [stroke=divider-regular]` (위아래 `spacing-300`).
  - CTA 행(가로, gap `spacing-200`): **ActionButton** `outlined/primary/small` "예약 상세" (보조) + **ActionButton** `fill/primary/small` "스마트키" (카드 내 주 행동, 행 우측/넓게). 카드당 강조 CTA 1개 = 스마트키.

### Section 3 detail — 예약 없음 (첫 화면 유도 카드, custom)
- 진행 중 카드 자리에 **간결한 유도 카드** 1개(카드 bg=`white`, `radius-300`, pad `spacing-400`, 세로 auto-layout gap `spacing-200`, 가운데 정렬 텍스트):
  - 일러스트/아이콘 자리: `icon-car-search-line`(primary-regular, 32px) on `status-information-weak` 원형 타일 56 `radius-circle`.
  - 타이틀 "첫 차를 예약해 볼까요?" (`title2`/`text-strong`).
  - 서브 "가까운 쏘카존에서 1분 만에 시작할 수 있어요." (`body3`/`text-secondary`, `break-keep`).
  - **ActionButton** `fill/primary/medium` "주변 차량 찾기" — 검색 Hero와 같은 목적지(검색)로 보내는 보조 CTA. 폭 fill, 위 마진 `spacing-300`.
  - 주: 화면 전체 hero 강조는 여전히 검색 박스(②). 이 카드는 빈 상태를 채우는 유도 카드이지 두 번째 primary가 아니다(시각 위계상 검색 박스보다 가볍게).

## Copywriting (verbatim)
모든 텍스트는 SOCAR 보이스(명확·따뜻·간결). 줄바꿈은 `break-keep`로 단어 중간 끊김 방지.

**공통**
- 위치 주소 (title3): `서울 강남구 역삼동`
- 검색 placeholder (body1): `어디서 탈까요?`
- 혜택 섹션 — carousel 슬라이드(현재 1/3, 슬라이드 1):
  - 배너 타이틀 (title2): `신규 가입하면 첫 대여 30% 할인`
  - 배너 서브 (body3): `지금 가입하고 바로 받아보세요.`
  - (스펙상 나머지 2장 카피, 화면엔 도트만 노출)
    - 슬라이드 2 타이틀: `100km 달릴 때마다 1,000P 적립` / 서브: `주행 리워드로 다음 대여가 더 저렴하게.`
    - 슬라이드 3 타이틀: `주중 대여 최대 20% 할인` / 서브: `평일에 더 가볍게 떠나보세요.`
- 퀵메뉴 라벨 (caption1): `쏘카플랜` · `부름·편도` · `쿠폰함` · `이벤트`
- BottomNavigation 라벨 (caption3): `홈` · `탐색` · `이용내역` · `마이`

**예약 있음 상태 (③ 진행 중 예약 카드)**
- 섹션 헤더 (title3): `이용 중인 차`
- 상태 Tag (caption1): `이용 중`
- 모델명 (title2): `아반떼 CN7`
- 이용 시간 (body3): `오늘 14:00 – 18:00`
- 쏘카존 (body3): `강남 더클래스효성 쏘카존`
- CTA — 보조 (title4): `예약 상세`
- CTA — 주 (title4): `스마트키`

**예약 없음 상태 (③ 유도 카드)**
- 타이틀 (title2): `첫 차를 예약해 볼까요?`
- 서브 (body3): `가까운 쏘카존에서 1분 만에 시작할 수 있어요.`
- CTA (title4 — medium 버튼): `주변 차량 찾기`

## Color & emphasis
- Background: `background-regular`(#F2F3F8) 스크린 / `white` surface(검색 박스·카드·퀵메뉴 타일 바탕은 weak 톤). TopAppBar·BottomNavigation은 `white`.
- Primary CTA / 브랜드 강조: `primary-regular`(#0078FF) — 검색 아이콘, 진행 중 카드 `스마트키`(`fill/primary`), 예약 없음 `주변 차량 찾기`, carousel active dot, BottomNav `홈` active. **화면 전체 fill/primary 강조 표면은 검색 Hero + (상태별) 단 1개의 fill/primary 버튼**으로 제한.
- Text hierarchy: `text-strong`(주소·모델명·섹션 헤더·배너 타이틀) > `text-primary`(퀵메뉴 라벨) > `text-secondary`(검색 placeholder·이용 시간·쏘카존·배너 서브) > `text-tertiary`(검색 chevron·비활성 탭).
- Status: 진행 중 Tag = `status-positive-weak`/`status-positive-strong`(이용 중 = 진행 중, green). 쏘카존 핀 = `location-rental`. 알림 dot = `notification-red`. 배너/유도 카드 약한 배경 = `status-information-weak`.
- **강조하는 것**: 검색 Hero(가장 큰 surface + primary 아이콘) → 진행 중이면 스마트키 CTA. **의도적으로 de-emphasize**: 혜택 carousel·퀵메뉴(보조 surface, 약한 톤·작은 타이포), `예약 상세`(outlined로 스마트키보다 낮은 강조), BottomNav 비활성 탭(text-tertiary).

## States
- **기본 (예약 있음)** — `[auto] 홈(메인) · 예약 있음`. ③ = 진행 중 예약 카드("이용 중" Tag + 스마트키 CTA). TopAppBar 알림 dot Badge **노출**(notification-red). above-the-fold: TopAppBar → 검색 Hero → 진행 중 카드까지 보이게.
- **빈 상태 (예약 없음, 첫 화면)** — `[auto] 홈(메인) · 예약 없음`. ③ = 유도 카드("첫 차를 예약해 볼까요?" + 주변 차량 찾기). 진행 중 카드/섹션 헤더 없음. 알림 dot Badge **미노출**(깔끔한 첫 화면). 나머지(검색 Hero·carousel·퀵메뉴·BottomNav)는 예약 있음과 동일.
- (로딩/에러/성공은 이 요청 범위 밖 — Out of scope.)

## Accessibility
- **최소 터치 타깃 44×44**: 알림 IconButton, BottomNav 각 탭, 퀵메뉴 각 항목, 카드 CTA 버튼 모두 ≥44px 높이 확보(small 버튼도 터치 영역은 44 유지).
- **아이콘 전용 인터랙티브에 aria-label**: 알림 `IconButton 알림 [aria-label=알림]`. dot Badge는 "읽지 않은 알림 있음"을 의미(미읽음 시에만 노출).
- **대비**: hero placeholder는 `text-secondary`(#697383) on white — 본문 충분 대비. 위치 주소·모델명은 `text-strong`로 야외 시인성 확보(principles: 야외 환경 핵심 정보 식별). active dot/탭은 색만이 아니라 채움 아이콘(`icon-home-fill`)으로도 구분.
- **한 손 조작**: 핵심 행동(검색 Hero, 카드 CTA)을 화면 중상단~중단에 배치, BottomNav는 thumb-zone 하단 고정.
- **타이포 위계 보존**: Pretendard 풀 weight — SemiBold(600) 자리에 Medium(500) 폴백 금지(title*/caption1은 600, heading은 700, body는 400).

## Out of scope
- 검색 결과/지도/쏘카존 목록, 알림함, 스마트키, 예약 상세, 쿠폰함·이벤트 등 진입 후 목적지 화면(진입점만 디자인).
- 로딩/에러/성공 상태, 다건 예약 스택(진행 중 1건 기준), 다크 모드/테마.
- 실제 검색 입력 동작(비입력 tap-to-navigate 진입형).
