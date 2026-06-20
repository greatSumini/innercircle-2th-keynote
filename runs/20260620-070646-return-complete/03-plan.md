---
run: 20260620-070646-return-complete
stage: plan
status: ready
frame: 360 x 800 mobile portrait
---
# Design plan — 반납 완료 (Return complete) success screen

## Overview
- Goal / primary job: 차량 반납을 막 끝낸 사용자가 "내 반납·결제가 정상 처리됐는지" 한눈에
  확인하고 안심한 뒤 화면을 닫는다. 이용 요약·결제 요약으로 신뢰(Confidence)를 주고, 단일
  primary CTA로 다음 행동을 명확히 한다.
- Primary action (emphasized): 하단 고정 '확인' (ActionButton fill/primary/large) — 화면에서
  유일하게 강조되는 액션.
- Surface: full screen (mobile portrait). 본문은 스크롤, 하단 CTA 영역은 sticky 고정.

## Frame
- Size: 360 x 800 (SOCAR mobile baseline 360 wide). 본문 길이에 따라 세로는 가변이지만 디자인
  기준 높이는 800.
- Background: `background-regular` #F2F3F8 (스크린 전체 바탕).
- TopAppBar: 높이 56px, 좌측 back 없음, 우측에만 닫기(X) IconButton. 좌우 안전영역은 화면
  좌우 패딩 `spacing-400` 16px와 정렬.
- 본문 영역: TopAppBar 아래부터 sticky 하단 영역 위까지. 좌우 패딩 `spacing-400` 16px.
- 하단 고정(sticky) 액션 영역: 화면 하단에 고정. `white` #FFFFFF 배경, 상단 1px
  `divider-regular` #E5E8EF 구분선, 내부 패딩 상하 `spacing-300`/`spacing-400`, 좌우 `spacing-400` 16px.
  하단에는 홈 인디케이터용 safe-area 여백 `spacing-200` 8px(시각적으로는 패딩에 포함).

## Layout (top → bottom)
좌우 기준 패딩은 모두 `spacing-400`(16px). 카드 간 세로 간격은 `spacing-300`(12px).

| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 1 | Top app bar | TopAppBar (general, Trailing slot only — no back) | bg `white` #FFFFFF; height 56px; 좌우 pad `spacing-400` 16px; title 영역 비움 | 좌측 비움, 우측 닫기(X) IconButton |
| 1a | 닫기 버튼 | IconButton (size `medium`, icon `icon-close-line`) | icon `text-strong` #141A24, 24px; 버튼 박스 40x40 터치 영역, bg transparent | 닫기(X) — `aria-label="닫기"` |
| 2 | 성공 히어로 | (custom layout) | 상단 여백 `spacing-800` 32px → 아이콘 → `spacing-400` 16px → 타이틀 → `spacing-150` 6px → 보조문구; 가운데 정렬 | 체크 아이콘 + 타이틀 + 한 줄 보조문구 |
| 2a | 성공 체크 아이콘 | Icon `icon-check-circle-fill` | 아이콘 `status-positive-regular` #04CA81, 56x56px; (선택) `status-positive-weak` #E6FEF0 원형 backdrop 72x72, radius-full | 체크 동그라미 (filled) |
| 2b | 히어로 타이틀 | (text) | `text-strong` #141A24 / `heading2` (24px·Bold·LH34) / 가운데 정렬 | "반납이 완료되었어요" |
| 2c | 히어로 보조문구 | (text) | `text-secondary` #697383 / `body2` (16px·Regular·LH24) / 가운데 정렬 | "안전하게 반납해 주셔서 감사해요. 결제 내역을 확인해 주세요." |
| 3 | 이용 요약 카드 | (custom surface — white rounded card) | bg `white` #FFFFFF; radius 12px(=`radius-300` 상당); 내부 패딩 `spacing-400` 16px; 히어로와의 위 간격 `spacing-600` 24px | 카드 제목 + 4개 라벨–값 행 |
| 3a | 카드 제목 | (text) | `text-strong` #141A24 / `title2` (16px·SemiBold·LH24); 제목↔첫 행 간격 `spacing-300` 12px | "이용 요약" |
| 3b | 행: 차량 | (label–value row) | label `text-secondary` #697383 / `body3` (14px·LH22); value `text-primary` #354153 / `title3` (14px·SemiBold·LH22); 행 높이 자동, 행 간 간격 `spacing-300` 12px | "차량" — "더 뉴 아반떼 (12가 3456)" |
| 3c | 행: 쏘카존 | (label–value row) | 위와 동일 | "쏘카존" — "강남역 2번 출구 공영주차장" |
| 3d | 행: 이용 시간 | (label–value row, value 우측 정렬 2줄 허용) | label `body3`/`text-secondary`; value `title3`/`text-primary`, 우측 정렬 | "이용 시간" — "6월 20일(토) 14:00 ~ 18:00" |
| 3e | 행: 주행 거리 | (label–value row) | 위와 동일 | "주행 거리" — "42km" |
| 4 | 결제 요약 카드 | (custom surface — white rounded card) | bg `white` #FFFFFF; radius 12px; 내부 패딩 `spacing-400` 16px; 이용 요약 카드와의 간격 `spacing-300` 12px | 카드 제목 + 3개 항목 행 + 구분선 + 총액 행 |
| 4a | 카드 제목 | (text) | `text-strong` #141A24 / `title2` (16px·SemiBold·LH24); 제목↔첫 행 `spacing-300` 12px | "결제 요약" |
| 4b | 행: 대여요금 | (label–value row) | label `text-secondary` #697383 / `body3` (14px); value `text-primary` #354153 / `body3` (14px), 우측 정렬; 행 간 `spacing-200` 8px | "대여요금" — "32,000원" |
| 4c | 행: 주행요금 | (label–value row) | 위와 동일 | "주행요금" — "5,460원" |
| 4d | 행: 보험료 | (label–value row) | 위와 동일 | "보험료" — "5,500원" |
| 4e | 구분선 | (divider) | `divider-regular` #E5E8EF, 1px, full-width; 위/아래 간격 `spacing-300` 12px | — |
| 4f | 총 결제금액 행 (강조) | (label–value row, emphasized) | label `text-strong` #141A24 / `title2` (16px·SemiBold); value `text-strong` #141A24 / `heading3` (22px·Bold·LH30), 우측 정렬 | "총 결제금액" — "42,960원" |
| 5 | 하단 고정 CTA 영역 | (custom sticky container) | bg `white` #FFFFFF; 상단 1px `divider-regular` #E5E8EF; 패딩 상 `spacing-300` 12px·하 `spacing-400` 16px·좌우 `spacing-400` 16px; CTA↔TextButton 간격 `spacing-200` 8px; 세로 스택 | primary 버튼 + 보조 텍스트 버튼 |
| 5a | 기본 CTA | ActionButton (`fill` / `primary` / `large`) | bg `primary-regular` #0078FF; label `white` #FFFFFF / `title2` (16px·SemiBold); 패딩 py 16px(`spacing-400`) px 22px(`spacing-550`); radius `radius-350`(=12px); full-width; 높이 ≈56px | "확인" |
| 5b | 보조 액션 | TextButton (`text` / `tertiary` / `medium`) | label `text-secondary` #697383 / `title3` (14px·SemiBold); 가운데 정렬; full-width 터치 영역, 높이 ≈40px; no underline | "이용 내역 보기" |

## Copywriting (verbatim)
화면이 표시하는 모든 텍스트. (역할 / 타입 토큰)
- 닫기 버튼 접근성 라벨 (a11y): "닫기"
- 히어로 타이틀 (heading2, text-strong): "반납이 완료되었어요"
- 히어로 보조문구 (body2, text-secondary): "안전하게 반납해 주셔서 감사해요. 결제 내역을 확인해 주세요."
- 이용 요약 카드 제목 (title2, text-strong): "이용 요약"
  - 라벨 (body3, text-secondary): "차량" → 값 (title3, text-primary): "더 뉴 아반떼 (12가 3456)"
  - 라벨: "쏘카존" → 값: "강남역 2번 출구 공영주차장"
  - 라벨: "이용 시간" → 값: "6월 20일(토) 14:00 ~ 18:00"
  - 라벨: "주행 거리" → 값: "42km"
- 결제 요약 카드 제목 (title2, text-strong): "결제 요약"
  - 라벨 (body3, text-secondary): "대여요금" → 값 (body3, text-primary): "32,000원"
  - 라벨: "주행요금" → 값: "5,460원"
  - 라벨: "보험료" → 값: "5,500원"
  - 총액 라벨 (title2, text-strong): "총 결제금액" → 값 (heading3, text-strong): "42,960원"
- 기본 CTA (title2, white): "확인"
- 보조 액션 (title3, text-secondary): "이용 내역 보기"

> 금액 검산: 32,000 + 5,460 + 5,500 = 42,960원 (총 결제금액과 일치).

## Color & emphasis
- Background: `background-regular` #F2F3F8. 카드/상단바/하단 CTA 영역은 `white` #FFFFFF로
  떠 보이게 하여 정보 그룹을 명확히 분리(Predictability).
- 성공 신호: 히어로 체크 아이콘만 `status-positive-regular` #04CA81(선택 backdrop
  `status-positive-weak` #E6FEF0). 초록은 이 한 곳에만 써서 "성공"을 단일하게 신호한다.
- 텍스트 위계: 타이틀·카드 제목·총액 = `text-strong` #141A24 / 값(항목명·금액) = `text-primary`
  #354153 / 라벨·보조문구 = `text-secondary` #697383. (descending prominence)
- Primary CTA '확인'만 `primary-regular` #0078FF 채움 + 흰색 라벨로 강조 → 화면에서 유일한
  강조 색면. 보조 '이용 내역 보기'는 색면 없는 TextButton(`text-secondary`)으로 명확히 종속.
- 총 결제금액 강조: 색이 아니라 위계로 강조. 위 `divider-regular` 구분선 → 라벨 `title2`,
  값 `heading3`(22px·Bold)로 카드 내 최대 타이포. 색은 다른 강조 텍스트와 같은 `text-strong`로
  유지해 "성공=초록, 행동=파랑" 외에 색을 추가하지 않는다(Consistency, 단일 강조 원칙).
- 구분선: 카드 내 항목/총액 사이 1px `divider-regular` #E5E8EF; 하단 CTA 영역 상단 1px
  `divider-regular`. 카드끼리는 간격(`spacing-300`)으로 분리하므로 별도 선 없음.

## States
- Default (성공): 위 레이아웃 그대로. 요청대로 성공 상태 단일 화면.
- Empty / Loading / Error / Success: 해당 없음 — 이 화면은 반납 완료 직후의 성공 결과 화면이며
  로딩/에러/빈 상태는 범위 밖(01-clarify Out, 00-request 명시). 추가하지 않는다.

## Accessibility
- 터치 타깃: 닫기 IconButton 최소 40x40(권장 48x48 터치 영역). primary CTA 높이 ≈56px,
  보조 TextButton 터치 높이 ≈40px — 최소 44px 가이드 충족(보조는 full-width로 폭 확보).
- 대비: text-strong #141A24·text-primary #354153·text-secondary #697383 모두 흰/연회색
  배경에서 WCAG AA(4.5:1) 충족. primary CTA 흰색 라벨 on #0078FF 대비 충족. 성공 초록
  #04CA81은 의미 전달을 색에만 의존하지 않도록 체크 아이콘 형태 + "완료" 텍스트로 이중 신호.
- 가독성/한 손 조작: 핵심 정보(타이틀·총액)는 큰 타이포로 야외 시인성 확보(Context & Safety).
  primary CTA는 화면 하단 고정으로 엄지 도달 범위에 배치, 중복 실행 방지를 위해 단일 강조 CTA.
- 스크롤: 본문이 길어지면 본문만 스크롤되고 하단 CTA는 항상 보이도록 sticky 고정.
- 라벨링: 닫기 버튼은 텍스트가 없으므로 `aria-label="닫기"`. 금액 값은 "원" 단위까지 읽히도록
  텍스트로 표기(스크린리더 호환).

## Out of scope
- 에러/로딩/empty 등 다른 상태.
- 결제 수단 변경, 영수증 상세, 쿠폰/포인트 적용 등 별도 플로우.
- 별점/리뷰, 다음 예약 추천, 푸시/스낵바 등 추가 섹션.
- 좌측 back 네비게이션(종료 흐름이므로 우측 닫기만).

## Notes for implement (library not bound)
socarframe 라이브러리는 이 Figma 파일에 바인딩되어 있지 않다(02-context: figma_library_available: no).
모든 컴포넌트를 primitive 프레임으로 직접 조립하고, **토큰을 정확한 값으로 적용**하되 레이어
이름/주석에 토큰명을 남겨 verify가 의도를 추적할 수 있게 한다.
- 색: 위 표의 hex 그대로(color.md 기준). 폰트: SOCAR Korean UI font, 위 px/weight/LH(typography.md).
- spacing: 표의 px는 모두 spacing 토큰 매핑값(4px 그리드).
- radius: ActionButton large = `radius-350`(12px). 카드 radius는 socarframe 토큰 미지정 →
  일관되게 12px(`radius-300` 상당)로 적용하고 verify에 플래그.
- 아이콘은 라이브러리 인스턴스가 없으므로 `icon-check-circle-fill`, `icon-close-line`을 벡터로
  그리거나 import. 색/크기는 위 표 값 적용.
