---
run: 20260620-101722-emergency-help
stage: plan
status: ready
frame: 360 x 880 mobile portrait
---
# Design plan — 사고·고장 신고(긴급 도움)

## Overview
- Goal / primary job: 이용 중 사고·고장으로 당황한 사용자가 **헤매지 않고 즉시 전화로 도움을 받는 것**. 한 화면에서 "전화 → 상황 선택 → 안전 안내 → 보조 정보" 순으로 한 손에 잡히게 한다.
- Primary action (emphasized): **긴급출동 전화 연결** — 화면 최상단 긴급 카드 안의 full-width 채움 버튼 1개. 위급함을 `status-negative`(빨강) 채움으로 전달하고, 화면 내 강조는 이 영역 하나로 수렴(One primary action).
- Surface: full screen (스크롤 가능한 풀스크린). BottomSheet 아님 — 정보량과 "즉시 행동" 요구상 전체 화면이 적합.

## Frame
- Size: **360 x 880** (SOCAR 모바일 포트레이트 baseline 360px 폭, 레퍼런스 `[auto] 반납 완료` 360×857와 동일 폭). 콘텐츠 세로 합이 800을 약간 넘으므로 880으로 잡아 하단 잘림 없이 한 화면에 담는다(스크롤 전제).
- Placement: 활성 페이지(Page 1, `0:1`), **x ≈ 15000, y = 0**(세션 전용 레인, 기존 프레임 x=200–560과 겹침 없음). 단일 상태이므로 상태 세그먼트 생략.
- Frame name: `[auto] 사고·고장 신고(긴급 도움) — 20260620-101722-emergency-help`
- Safe areas / TopAppBar / bottom: 상단 TopAppBar 56px 고정(뒤로가기). 별도 하단 고정 CTA 바 없음 — 1차 액션(전화)이 상단 긴급 카드에 있어 한 손 도달 우선. 페이지 배경 `background-regular`, 좌우 패딩 `spacing-400`(16px), 본문 상단 여백 `spacing-400`, 하단 안전 여백 `spacing-800`(32px).

## Layout (top → bottom)
좌우 콘텐츠 패딩은 전 섹션 공통 `spacing-400`(16px). 섹션(2~8) 사이 세로 간격 `spacing-400`(16px), 카드 내부 패딩 `spacing-400`.

| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 1 | TopAppBar | TopAppBar (general) · Left=IconButton(뒤로가기) | bg white / 타이틀 생략(또는 `title2`) / 높이 56, 좌우 pad `spacing-400` | 좌측 `icon-arrow-left-line` 뒤로가기(aria-label=뒤로가기). 타이틀 텍스트 없음(히어로가 타이틀 역할) |
| 2 | Hero (안심 헤더) | (custom) 텍스트 블록 | 타이틀 `text-strong`/`heading2`, 부제 `text-secondary`/`body2`, 타이틀↔부제 gap `spacing-150` | 타이틀 「도움이 필요하신가요?」 + 부제 한 줄(아래 Copywriting) |
| 3 | 긴급 액션 Card (최강조) | (custom) Card surface + ActionButton ×2 | 카드 bg `status-negative-weak`, radius `radius-300`, 내부 pad `spacing-400`, 행 gap `spacing-300`; 헤더 텍스트 `status-negative-strong`/`title2`, 설명 `text-secondary`/`body3` | 상단 라벨 「사고가 났거나 차가 멈췄나요?」 + 「24시간 긴급출동·고객센터가 바로 도와드려요.」 / **1차 CTA**: 긴급출동 전화(채움) / **2차**: 고객센터 전화(아웃라인) |
| 3a | — 1차 CTA | ActionButton · fill/(negative)/large, full-width | fill `status-negative-regular`, 라벨/아이콘 white, radius `radius-350`, `title2`, leftIcon `icon-phone-fill` | 「긴급출동 전화하기」 |
| 3b | — 2차 액션 | ActionButton · outlined/primary/large(→negative 톤), full-width | 흰 bg, 보더 `status-negative-regular`, 라벨/아이콘 `status-negative-strong`, radius `radius-350`, `title2`, leftIcon `icon-phone-line` | 「고객센터 전화하기」 |
| 4 | 주의 안내 Tips | Tips (InfoTip/AccentTip 패턴) · caution/static | bg `status-caution-weak`, radius `radius-300`, pad `spacing-300`, 아이콘 `status-caution-regular`, 본문 `text-primary`/`body3`, 아이콘↔텍스트 gap `spacing-150` | leftIcon `icon-exclamation-triangle-fill` + 「안전한 곳으로 이동한 뒤 신고해 주세요. 2차 사고를 막는 것이 가장 먼저예요.」(break-keep) |
| 5 | 상황 선택 헤더 | (custom) 섹션 헤더 텍스트 | `text-strong`/`title2`, 아래 gap `spacing-200` | 「어떤 상황인가요?」 |
| 6 | 상황 선택 리스트 | SelectionBoxGroup (single) · SelectionBox ×3, 카드형 | 카드 bg white, 보더 `border-regular`, radius `radius-300`, 행 높이 pad `spacing-400`, 행간 gap `spacing-200`; 아이콘 backdrop `radius-circle`, 라벨 `text-strong`/`title3`, 설명 `text-tertiary`/`body4`, chevron `text-tertiary` | 3행: 사고 / 고장 / 기타 문의 (각 leftIcon + 라벨 + 보조설명 + `icon-chevron-right-line`) |
| 6a | — 사고 | SelectionBox(아이콘+라벨+chevron) | 아이콘 `icon-exclamation-triangle-fill`, backdrop `status-negative-weak`, 아이콘색 `status-negative-regular` | 「사고가 났어요」 / 「접촉·추돌 등 사고 접수」 |
| 6b | — 고장 | SelectionBox(아이콘+라벨+chevron) | 아이콘 `icon-horn-fill`, backdrop `status-caution-weak`, 아이콘색 `status-caution-regular` | 「차가 고장 났어요」 / 「시동·타이어·배터리 등」 |
| 6c | — 기타 문의 | SelectionBox(아이콘+라벨+chevron) | 아이콘 `icon-question-circle-line`, backdrop `background-regular`, 아이콘색 `text-secondary` | 「그 외 문의가 있어요」 / 「이용·결제 등 일반 문의」 |
| 7 | 현재 이용 차량 Card | (custom) Card surface + Tag | 카드 bg white, radius `radius-300`, 보더 `border-regular`, pad `spacing-400`, 라벨 `text-secondary`/`body4`, 값 `text-strong`/`title3`, 메타 `text-tertiary`/`caption1`; 차량 아이콘 `icon-car-fill`/`text-secondary` | 헤더 「현재 이용 중인 차량」 + 차량명·번호판·이용시간 요약 + 이용중 Tag |
| 8 | FAQ 진입 | (custom) List + TextButton | 행 라벨 `text-primary`/`body2`, chevron `text-tertiary`, divider `divider-regular`, 전체보기 TextButton `primary`/`title3` | 섹션 헤더 「자주 묻는 질문」 + FAQ 행 2개(+ chevron) + 「전체 도움말 보기」 TextButton |

## Copywriting (verbatim)
모든 문자열을 역할·타입 토큰과 함께 나열한다. SOCAR 보이스: 침착·신뢰·명료, 군더더기 없음.

**Hero**
- 타이틀 (heading2, `text-strong`): 「도움이 필요하신가요?」
- 부제 (body2, `text-secondary`, 한 줄): 「당황하지 않으셔도 돼요. 바로 도와드릴게요.」

**긴급 액션 Card**
- 카드 라벨 (title2, `status-negative-strong`): 「사고가 났거나 차가 멈췄나요?」
- 카드 설명 (body3, `text-secondary`): 「24시간 긴급출동과 고객센터가 바로 도와드려요.」
- 1차 CTA (title2, white): 「긴급출동 전화하기」
- 2차 액션 (title2, `status-negative-strong`): 「고객센터 전화하기」

**주의 안내 Tips** (body3, `text-primary`, break-keep)
- 「안전한 곳으로 이동한 뒤 신고해 주세요. 2차 사고를 막는 것이 가장 먼저예요.」

**상황 선택**
- 섹션 헤더 (title2, `text-strong`): 「어떤 상황인가요?」
- 사고 — 라벨 (title3, `text-strong`): 「사고가 났어요」 / 설명 (body4, `text-tertiary`): 「접촉·추돌 등 사고 접수」
- 고장 — 라벨 (title3, `text-strong`): 「차가 고장 났어요」 / 설명 (body4, `text-tertiary`): 「시동·타이어·배터리 등」
- 기타 — 라벨 (title3, `text-strong`): 「그 외 문의가 있어요」 / 설명 (body4, `text-tertiary`): 「이용·결제 등 일반 문의」

**현재 이용 차량 Card**
- 섹션 헤더 (title3, `text-strong`): 「현재 이용 중인 차량」
- 이용중 Tag (caption1): 「이용 중」
- 차량명 값 (title3, `text-strong`): 「아반떼 CN7」
- 번호판 라벨/값 (body4 `text-secondary` / title3 `text-strong`): 「차량번호」 · 「12가 3456」
- 이용시간 메타 (caption1, `text-tertiary`): 「6월 20일 09:00 ~ 18:00 이용 중」

**FAQ**
- 섹션 헤더 (title3, `text-strong`): 「자주 묻는 질문」
- 행 1 (body2, `text-primary`): 「사고가 나면 보험 처리는 어떻게 되나요?」
- 행 2 (body2, `text-primary`): 「긴급출동 비용은 누가 부담하나요?」
- 전체보기 TextButton (title3, `primary-regular`): 「전체 도움말 보기」

## Color & emphasis
- Background: `background-regular`(페이지). 카드 표면은 white(차량·FAQ)와 `status-negative-weak`(긴급), `status-caution-weak`(Tips).
- **Primary CTA = `status-negative-regular` 채움 버튼**(긴급출동 전화). 브랜드 `primary-regular`(블루)는 이 화면의 1차 강조로 쓰지 않고 FAQ 전체보기 TextButton 같은 보조 링크에만 사용 — 위급 영역으로 강조를 수렴한다(One primary action).
- 강조(emphasized): 긴급 액션 Card — 화면 최상단, `status-negative-weak` 배경의 색면 + 가장 큰 채움 버튼으로 시선이 즉시 도달. 야외·당황 상황에서도 빨강이 "여기를 누르면 도움받는다"를 즉시 전달.
- 2단계 de-emphasis: 고객센터(아웃라인) < 상황 선택(white 카드) < 차량 정보(중립 카드) < FAQ(텍스트 링크). 점진적으로 강조도가 낮아져 위계가 한눈에 읽힌다.
- Status 색은 **액션·경고 영역에만 절제해서** 사용(긴급=negative, 주의=caution). 상황 선택 아이콘 backdrop의 약한 status 색은 의미 단서일 뿐 면적이 작아 화면을 빨갛게 물들이지 않는다.
- 텍스트 위계: 타이틀 `text-strong` > 본문/값 `text-primary`/`text-strong` > 부제/라벨 `text-secondary` > 메타/보조 `text-tertiary`.

## States
- **기본**: 위 레이아웃 전체가 채워진 기본 상태(요청대로 1종만). 모든 데이터(차량 정보·FAQ)는 실제 더미 카피로 채워진 상태로 표현한다. 빈 상태/로딩/에러는 이 화면 범위 밖(전화 연결 이후·신고 플로우에서 다룸).

## Accessibility
- **터치 타깃 ≥ 48×48**: 모든 CTA(large 버튼), SelectionBox 행(pad `spacing-400`로 높이 확보), TopAppBar IconButton, FAQ 행이 최소 타깃을 만족 — 한 손·당황 상황에서 오탭 최소화(release checklist "한 손 조작" 충족).
- **아이콘-only 버튼은 aria-label 필수**: 뒤로가기 `aria-label=뒤로가기`.
- **대비/야외 식별**: 1차 CTA는 `status-negative-regular`(#FF3A5B) 위 white 텍스트, 본문은 `text-strong`/`text-primary`로 강한 대비. 위급 정보가 색 하나에만 의존하지 않도록 아이콘(`icon-phone-fill`)+명확한 동사 라벨「긴급출동 전화하기」를 함께 제공(색각 보조).
- **타이포 가독성**: Pretendard 풀 weight, heading2(24)·body2(16)로 작은 글씨 없이 핵심 정보 식별. SemiBold(600) 유지(Medium으로 다운하지 않음).
- **One primary action**: 강조 버튼 1개로 "무엇을 먼저 할지" 고민 없이 행동 유도(Affordance).

## Out of scope
- 전화 연결 이후 흐름, 사고 접수/신고 입력 폼, 위치 공유·지도 상세.
- 빈 상태/로딩/에러/성공 등 추가 상태(기본 1종만).
- 실제 전화번호·보험 약관·법적 고지 문구 확정(더미 카피).
- 차량 정보 실데이터 연동(placeholder 카피로 표현).
