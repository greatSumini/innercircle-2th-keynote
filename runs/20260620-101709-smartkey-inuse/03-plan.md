---
run: 20260620-101709-smartkey-inuse
stage: plan
status: ready
frame: 360 x 800 mobile portrait (SOCAR baseline 360 wide; height fits content + sticky bottom)
---
# Design plan — 이용 중(스마트키)

## Overview
- Goal / primary job: 차량 이용 중, 사용자가 **차 문을 즉시 제어(열기/잠그기)** 하고 **남은 이용 시간을 관리(연장·반납)** 한다. 현재 잠금 상태가 한눈에 보이고, 손이 바쁜 야외 상황에서도 큰 터치 타깃으로 즉각 조작된다.
- Primary action (emphasized): 화면 핵심 컨트롤인 **문 잠그기/열기 토글 타일** (가장 큰 컨트롤, 색+아이콘+라벨 3중 상태 표현). 하단 고정 영역의 단일 CTA는 **반납하기**(`ActionButton fill/primary/large`) — 이 화면의 최종 목적 행동.
- Surface: full screen (TopAppBar + 스크롤 본문 + 하단 고정 액션 영역).
- 상태 2종: 기본 **잠김** + **열림**. 동일 레이아웃, 잠금 상태 표현·문 토글 타일 라벨/색만 토글.

## Frame
- Size: **360 × 800** (SOCAR mobile portrait baseline 360px wide). 본문이 길어지면 세로 확장 가능 — 하단 액션 영역은 화면 하단 고정.
- Page background: `background-regular` (#F2F3F8). 카드/타일은 white(#FFFFFF).
- TopAppBar: 상단 고정, 높이 56px, 좌우 패딩 `spacing-400`(16px). LeftSideIconSlot 뒤로가기.
- Bottom action area: 화면 하단 고정 영역, 패딩 `spacing-400`(16px) 좌우 + 상하, white 배경 + 상단 `Divider [stroke=divider-regular]`. 한 손 도달 위해 주요 액션(연장·반납) 하단 배치.
- Safe area: 하단 고정 영역 아래 home-indicator 여백 `spacing-200`(8px) 가산.

## Layout (top → bottom)
프레임 양쪽 가로 패딩은 전 섹션 공통 `spacing-400`(16px). 섹션 간 간격은 기본 `spacing-400`(16px), 큰 블록 사이는 `spacing-500`(20px). 아래 표가 구조의 단일 소스이며 implement는 순서대로 빌드한다.

| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 1 | TopAppBar | TopAppBar (general title + LeftSideIconSlot back) — build from primitives | bg white / title `title1` `text-strong` / back icon `icon-chevron-left-line` 24 `text-strong` / pad `spacing-400`, height 56 | 좌: 뒤로가기 IconButton (aria-label "뒤로가기"). 중앙: 제목 "이용 중" |
| 2 | Hero — 차량 식별 + 남은 시간 Card (custom) | Card (custom) | white card, `radius-300`(12px), pad `spacing-500`(20px), 내부 gap `spacing-300`(12px) / 섹션 상단 마진 `spacing-400` | 차량 모델 `title1` `text-strong` + 번호판 `body3` `text-secondary`; "남은 이용 시간" 라벨 `body3` `text-secondary`; 타이머 값 `display2`(36px) `text-strong`; 반납 예정 시각 행 `body3` `text-secondary` (leading `icon-clock-line` 16 `text-tertiary`) |
| 3 | 잠금 상태 + 문 제어 토글 타일 (custom, primary control) | Door toggle tile (custom) — primary IconButton 역할 | **잠김:** 타일 bg `status-information-weak`(#EBF5FF), `icon-lock-fill` 56 `status-information-regular`, 라벨 `text-strong`, Tag bg `status-information-weak`/text `status-information-strong`. **열림:** 타일 bg `status-caution-weak`(#FFF8E6), `icon-lock-open-fill` 56 `status-caution-regular`, Tag bg `status-caution-weak`/text `status-caution-strong`. 공통: `radius-400`(16px), pad `spacing-500`(20px), 높이 ≥120, 내부 gap `spacing-300` | 상단 Tag(상태 라벨) "잠김"/"열림"; 큰 자물쇠 아이콘; 액션 라벨 `title2` (잠김="문 열기" / 열림="문 잠그기"); 보조 안내 `caption1` `text-secondary` (잠김="차 문이 잠겨 있어요" / 열림="차 문이 열려 있어요 · 탭하여 잠그기") |
| 4 | 차량 제어 버튼 그룹 (비상등 · 경적/차 찾기) (custom) | 2-up large IconButton tiles row | 각 타일 white bg + `border-regular` 1px, `radius-300`(12px), 터치 타깃 ≥64×88, pad `spacing-400`, row gap `spacing-300`(12px) / 아이콘 28 `text-primary` / 캡션 `caption1` `text-secondary` | 타일1: `icon-warning-light-fill` + "비상등" (aria-label "비상등 켜기"). 타일2: `icon-horn-fill` + "경적·차 찾기" (aria-label "경적 울려 차 찾기") |
| 5 | 안내 Tips (Info) (custom) | InfoTip / Tips inline (Info tone) | bg `status-information-weak`(#EBF5FF), `radius-300`(12px), pad `spacing-300`(12px), leading `icon-info-circle-line` 20 `status-information-regular`, gap `spacing-200` / 본문 `body3` `text-secondary` | "탑승 전 차량 외관을 확인해 주세요. 흠집이 있다면 사진으로 남겨두면 안심돼요." (break-keep, 2줄) |
| 6 | 도움 진입 row — 사고·고장 신고 / 고객센터 (custom) | 2개 TextButton (text/secondary, medium) with leading icon | white bg row 또는 카드 분리, `radius-300`, pad `spacing-400`, 중앙 `Divider [stroke=divider-regular]` vertical / 라벨 `body3` `text-secondary` / 아이콘 20 `text-secondary` | 좌: `icon-exclamation-triangle-fill` + "사고·고장 신고". 우: `icon-phone-fill` + "고객센터" |
| 7 | Bottom CTA (fixed) | ActionButton ×2 | white bg, 상단 `Divider [stroke=divider-regular]`, pad `spacing-400`, 버튼 사이 gap `spacing-200`(8px) | 상단(보조): **이용 시간 연장** `ActionButton outlined/secondary/large` (`text-primary` 텍스트, `border-regular`). 하단(primary): **반납하기** `ActionButton fill/primary/large` (`primary-regular` bg, white 텍스트) |

> 참고(가독성/스택): 비상등·경적은 1행 2칼럼 동급 보조 컨트롤. 도움 진입은 저강조. Bottom CTA는 세로 스택(반납하기가 시각적으로 아래·primary로 최종 행동) — 한 손 엄지 도달 영역.

## Copywriting (verbatim)
화면이 노출하는 모든 텍스트(역할 · 타입 토큰 · 문자열). 더미 데이터는 대표값.

- TopAppBar 제목 (title1): "이용 중"
- 차량 모델명 (title1): "쏘나타 디 엣지"
- 번호판 (body3): "12가 3456"
- 남은 시간 라벨 (body3): "남은 이용 시간"
- 남은 시간 값 (display2): "02:13"
- 반납 예정 시각 (body3): "23:40 반납 예정"
- 상태 Tag — 잠김 (caption1): "잠김"
- 상태 Tag — 열림 (caption1): "열림"
- 문 토글 액션 라벨 — 잠김 (title2): "문 열기"
- 문 토글 액션 라벨 — 열림 (title2): "문 잠그기"
- 문 토글 보조 안내 — 잠김 (caption1): "차 문이 잠겨 있어요"
- 문 토글 보조 안내 — 열림 (caption1): "차 문이 열려 있어요 · 탭하여 잠그기"
- 비상등 캡션 (caption1): "비상등"
- 경적 캡션 (caption1): "경적·차 찾기"
- Tips 본문 (body3): "탑승 전 차량 외관을 확인해 주세요. 흠집이 있다면 사진으로 남겨두면 안심돼요."
- 도움 — 신고 (body3): "사고·고장 신고"
- 도움 — 고객센터 (body3): "고객센터"
- 보조 CTA (title2): "이용 시간 연장"
- Primary CTA (title2): "반납하기"

aria-labels (icon-only interactives): 뒤로가기 → "뒤로가기"; 비상등 타일 → "비상등 켜기"; 경적 타일 → "경적 울려 차 찾기".

## Color & emphasis
- Background: `background-regular`(#F2F3F8). 카드/타일: white(#FFFFFF).
- Primary CTA(반납하기): `primary-regular`(#0078FF) bg + white 텍스트. pressed 단계 `primary-strong`.
- Text hierarchy: 타이머 값·제목·차량명 = `text-strong`; 본문 값 = `text-primary`; 라벨/안내·도움 = `text-secondary`; 캡션/저강조 = `text-tertiary`.
- **잠금 상태 = 색 + 아이콘 + 라벨 3중 표현** (Safety & Context > All):
  - 잠김(안정): `status-information-weak` 배경 + `status-information-regular`/`strong` 강조 + `icon-lock-fill` + Tag "잠김". 차분한 블루 = 안전·정상.
  - 열림(주의 환기): `status-caution-weak`(#FFF8E6) 배경 + `status-caution-regular`(#FF8800)/`strong` 강조 + `icon-lock-open-fill` + Tag "열림". 오렌지 = 경고 아닌 주의 환기.
- 비상등·경적 보조 컨트롤: 중립 white + `border-regular`, 아이콘 `text-primary` — 동급·저강조로 문 토글보다 약하게.
- Tips: `status-information-weak` 배경 Info 톤 (강한 경고 아님 → Alert 아님).
- 도움(신고·고객센터): `text-secondary`/`text-tertiary` 저강조 진입점.
- **강조 1개 원칙:** 화면 최대 강조는 타이머 값(`display2`) 1곳 + 문 토글 타일(가장 큰 컨트롤). 하단 단일 primary CTA는 반납하기 1개. 나머지는 모두 이를 보조.
- **의도적 de-emphasis:** 도움 진입(신고·고객센터)은 빈도 낮은 보조 — 텍스트 링크 수준 저강조. 비상등·경적은 중립 surface로 문 토글에 양보.

## States
- **기본 (잠김):** 문 토글 타일 = `status-information-weak` 배경 + `icon-lock-fill` + Tag "잠김" + 액션 라벨 "문 열기". 안정 색. 좌측 프레임(레인 leftmost).
- **열림:** 동일 레이아웃, 문 토글 타일만 토글 → `status-caution-weak` 배경 + `icon-lock-open-fill` + Tag "열림" + 액션 라벨 "문 잠그기" + 보조 안내 "차 문이 열려 있어요 · 탭하여 잠그기". 주의 환기 오렌지. 우측 프레임.
- (로딩/에러/성공 전이 상태 = scope out — clarify 확정. 스마트키 BLE 연결중/실패 전용 프레임 미포함.)

## Accessibility
- **터치 타깃:** 문 토글 타일 높이 ≥120px(전폭), 비상등·경적 타일 ≥64×88px, ActionButton large(py-400, 높이 ≥52px), TopAppBar 뒤로가기 ≥44×44px, 도움 TextButton ≥44px 높이. 손이 바쁜 야외 한 손 조작 전제로 모두 large.
- **잠금 상태 시인성:** 색만이 아니라 아이콘(자물쇠 채움/열림) + 텍스트 라벨("잠김"/"열림")을 함께 노출 → 색각·야외 직사광에서도 식별. (색 단독 의존 금지.)
- **대비:** 타이머/제목 `text-strong`(#141A24) on white = 고대비. Primary CTA white on `primary-regular`(#0078FF) ≥ 4.5:1. 열림 강조 텍스트는 `status-caution-strong`로 대비 확보(weak 배경 위 regular 단독 사용 금지).
- **텍스트 가독성:** 타이머 `display2`로 야외에서도 즉시 식별. 본문 최소 `caption1`(12px) 이상. break-keep으로 단어 중간 줄바꿈 방지.
- **한 손 도달:** 주요 액션(연장·반납)·핵심 컨트롤(문 토글)을 화면 하단/중앙에 배치 — 엄지 도달 영역.
- aria-label: 모든 icon-only 인터랙티브에 부여(위 Copywriting 참고).

## Out of scope
- 연장/반납/신고/고객센터의 **후속(다음) 화면** — 진입점만 표현.
- 차량 외관 점검 촬영 플로우, 결제·요금 상세, 예약/검색/지도.
- 로딩/에러/성공 등 전이 상태 전용 프레임 (스마트키 BLE 연결중/실패 포함).
- 지도·차량 위치 표시(경적·차 찾기는 버튼 진입점만).

## Figma naming & placement (per docs/figma-conventions.md)
- Run section wrapper: `[auto] 이용 중(스마트키) — 20260620-101709-smartkey-inuse` (생성 가능 시).
- Frames (2-state → 상태 세그먼트 포함, 둘 다 라벨):
  - `[auto] 이용 중(스마트키) · 잠김 — 20260620-101709-smartkey-inuse`
  - `[auto] 이용 중(스마트키) · 열림 — 20260620-101709-smartkey-inuse`
- **Placement:** active page, 예약된 캔버스 레인 **x=9600, y=0** 부터 좌→우. 잠김 leftmost(x=9600), 열림(x=9600+360+80=**x=10040**), 80px gutter, 공통 top y=0. 기존 프레임(x=200)과 무겹침.
- Layer 이름: 섹션은 역할(`TopAppBar`, `Hero`, `Door toggle tile (custom)`, `제어 버튼 그룹 (custom)`, `Tips`, `도움 row (custom)`, `Bottom CTA`), 컴포넌트 인스턴스는 `ActionButton · fill/primary/large` 식, 텍스트는 `<role> · <type-token>`, 아이콘은 토큰명(`icon-lock-fill`), 토큰 by-value는 브래킷(`[fill=status-caution-weak radius=radius-400]`).
- Local variable collection `socarframe` 생성·바인딩: 최소 사용 color 토큰 (`color/background-regular`, `color/primary-regular`, `color/text-strong`, `color/text-secondary`, `color/status-information-weak`, `color/status-information-regular`, `color/status-information-strong`, `color/status-caution-weak`, `color/status-caution-regular`, `color/status-caution-strong`, `color/border-regular`, `color/divider-regular`) + `radius/radius-300`, `radius/radius-350`, `radius/radius-400` + `spacing/spacing-200`, `spacing/spacing-300`, `spacing/spacing-400`, `spacing/spacing-500`.
