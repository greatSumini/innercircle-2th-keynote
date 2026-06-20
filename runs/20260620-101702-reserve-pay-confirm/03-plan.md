---
run: 20260620-101702-reserve-pay-confirm
stage: plan
status: ready
frame: 360 x 1180 mobile portrait
---
# Design plan — 예약 확인

## Overview
- Goal / primary job: 차량 예약 직전, 예약 내용·요금·결제수단·약관을 마지막으로 확인하고 결제를 완료해
  예약을 확정하는 **전체 화면(full screen)**. 사용자가 "얼마를, 무엇을, 어떻게 결제하는지"를 한눈에
  확신하고 단 한 번의 동작으로 예약을 끝내게 한다.
- Primary action (emphasized): 하단 sticky의 `결제하고 예약 완료` (ActionButton fill/primary/large).
  화면에서 유일하게 강조되는 핵심 CTA.
- Surface: full screen (스크롤 본문 + 하단 sticky 결제 바). 단일 기본 상태.

## Frame
- Size: **360 x 1180** — SOCAR 모바일 포트레이트 베이스라인 width **360**(레퍼런스 `반납 완료` 360과
  통일). 스크롤 본문이 길어 height는 콘텐츠가 한 프레임에 모두 보이도록 1180으로 확정(레퍼런스 857보다 큼).
- Background: `background-regular`(#F2F3F8). 카드/표면은 white.
- TopAppBar: 상단 56px 고정 영역(general + BasicBackButton). 좌우 패딩 `spacing-400`(16).
- 본문: TopAppBar 아래부터 하단 sticky 바 위까지 세로 스크롤. 화면 좌우 패딩 `spacing-400`(16),
  섹션(카드) 간 간격 `spacing-300`(12).
- 하단 action area: **sticky 결제 바**(최종 결제 금액 + primary CTA). 본문 위에 고정, 상단에
  `divider-regular` 1px 경계. 내부 패딩 좌우 `spacing-400`(16), 상하 `spacing-400`(16), 홈 인디케이터
  여백 `spacing-200`(8) 추가.
- 캔버스 배치: 신규 top-level 프레임 1개를 **x≈7800, y≈0**(요청 캔버스 레인; 기존 `반납 완료`
  x=200과 겹침 없음). 상태 1개 → 프레임 1개, 상태 세그먼트 생략.

## Layout (top → bottom)

| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 1 | Top app bar | TopAppBar (general + BasicBackButton in LeftSideIconSlot) | title 색 `text-strong` / `title1` / 높이 56, 좌우 pad `spacing-400`, 아이콘 24 | 뒤로가기(IconButton, icon-arrow-left-line) + 가운데 타이틀 "예약 확인" |
| 2 | 예약 요약 Card (custom) | white surface `radius-300` | 카드 fill white / 카드 pad `spacing-400` / 행 간 `spacing-300` | 차량명·번호판 헤더 + 차량/쏘카존/이용 일시/대여 시간 라벨·값 행 4개 |
| 3 | 요금 상세 Card (custom) + Accordion (single, 기본 접힘) | white surface `radius-300`; 합계 위 `Divider [stroke=divider-regular]` | 카드 fill white / 섹션 타이틀 `title2`·`text-strong` / 항목 라벨·값 `body3` / 합계 라벨 `title2`·`text-strong`, 값 `heading3`·`text-strong` / pad `spacing-400`, 행 간 `spacing-300` | 섹션 타이틀 "요금 상세" + 대여요금·보험료·예상 주행요금(Accordion Trigger, chevron 회전) 행 + 펼침 콘텐츠(주행요금 산정 안내) + Divider + 합계 강조 행 |
| 4 | 할인 적용 Card (custom) | white surface `radius-300` | 카드 fill white / 섹션 타이틀 `title2`·`text-strong` / 라벨 `body3`·`text-secondary` / pad `spacing-400`, 행 간 `spacing-300` | 섹션 타이틀 "할인 적용" + 쿠폰 행(적용 쿠폰 Tag soft/positive + 할인액, 우측 변경용 chevron) + 포인트 사용 행(Input filled 숫자 + 우측 TextButton "전액 사용", helperText 보유 포인트) |
| 5 | 결제수단 Card (custom) | white surface `radius-300` | 카드 fill white / 섹션 타이틀 `title2`·`text-strong` / 카드정보 `body3`·`text-primary` / pad `spacing-400` | 섹션 타이틀 "결제수단" + 카드 아이콘(icon-card-line) + "신한카드 ****-1234" + 우측 TextButton "변경" |
| 6 | 약관 동의 Card (custom) + Checkbox/CheckboxGroup | white surface `radius-300`; 항목 구분 `Divider [stroke=divider-regular]` | 카드 fill white / 전체 동의 `title3`·`text-strong` / 항목 `body3`·`text-primary` / 필수·선택 라벨 `caption1`·`text-secondary` / pad `spacing-400`, 행 간 `spacing-250` | "전체 동의" 1줄(checked) + Divider + 필수 항목 2개(체크, "[필수]" 라벨, 우측 보기 chevron) + 선택 항목 1개("[선택]", 우측 보기 chevron) |
| 7 | Bottom CTA (sticky, custom) | ActionButton fill/primary/large | 컨테이너 fill white, 상단 `Divider [stroke=divider-regular]` / 라벨 `title3`·`text-secondary`, 금액 `heading2`·`text-strong` / CTA `radius-350`, py `spacing-400` px `spacing-550` / 내부 pad `spacing-400` | 좌측 "최종 결제 금액" 라벨 + 우측 금액 "78,500원"(가장 강한 위계) / full-width CTA "결제하고 예약 완료" |

## Copywriting (verbatim)

**Top app bar**
- 타이틀 (title1, text-strong): "예약 확인"

**예약 요약 Card**
- 카드 헤더 차량명 (title3, text-strong): "아반떼 CN7"
- 카드 헤더 번호판 (body4, text-secondary): "12가 3456"
- 라벨 "차량" (body3, text-secondary) · 값 (title3, text-primary): "아반떼 CN7 · 가솔린"
- 라벨 "쏘카존" (body3, text-secondary) · 값 (title3, text-primary): "강남구청역 3번 출구"
- 라벨 "이용 일시" (body3, text-secondary) · 값 (title3, text-primary): "6월 22일(월) 오후 2:00 ~ 6:00"
- 라벨 "대여 시간" (body3, text-secondary) · 값 (title3, text-primary): "4시간"

**요금 상세 Card**
- 섹션 타이틀 (title2, text-strong): "요금 상세"
- 항목 라벨 "대여요금" (body3, text-primary) · 값 (body3, text-primary): "44,000원"
- 항목 라벨 "보험료" (body3, text-primary) · 값 (body3, text-primary): "9,000원"
- Accordion Trigger 라벨 "예상 주행요금" (body3, text-primary) · 값 (body3, text-primary): "8,500원"
- Accordion 펼침 콘텐츠 (body4, text-secondary): "주행거리 1km당 170원으로 예상한 금액이에요. 실제 주행거리에 따라 반납 시 정산돼요."
- 할인 행 라벨 "쿠폰·포인트 할인" (body3, text-primary) · 값 (body3, status-positive-regular): "-12,000원"
- 합계 라벨 "합계" (title2, text-strong) · 값 (heading3, text-strong): "78,500원"

**할인 적용 Card**
- 섹션 타이틀 (title2, text-strong): "할인 적용"
- 쿠폰 행 라벨 "쿠폰" (body3, text-secondary)
- 적용 쿠폰 Tag (caption1, status-positive-strong on status-positive-weak): "신규회원 1만원 할인"
- 쿠폰 할인액 (body3, text-primary): "-10,000원"
- 쿠폰 변경 안내 (icon-chevron-right-line, aria-label "쿠폰 변경")
- 포인트 행 라벨 "포인트" (body3, text-secondary)
- 포인트 Input placeholder/value (body3, text-primary): "2,000" · trailing 단위 (body3, text-secondary): "P"
- 포인트 보조 액션 TextButton (title4, primary): "전액 사용"
- 포인트 helperText (caption1, text-secondary): "보유 포인트 5,200P"

**결제수단 Card**
- 섹션 타이틀 (title2, text-strong): "결제수단"
- 카드 정보 (body3, text-primary): "신한카드 ****-1234"
- 변경 TextButton (title4, primary): "변경"

**약관 동의 Card**
- 전체 동의 (title3, text-strong): "전체 동의"
- 필수 항목 1 (body3, text-primary): "[필수] 예약·결제 서비스 이용약관"
- 필수 항목 2 (body3, text-primary): "[필수] 개인정보 수집·이용 동의"
- 선택 항목 1 (body3, text-primary): "[선택] 마케팅 정보 수신 동의"
- (각 항목 우측 보기 chevron, icon-chevron-right-line, aria-label "약관 보기")

**Bottom CTA (sticky)**
- 라벨 "최종 결제 금액" (title3, text-secondary)
- 금액 (heading2, text-strong): "78,500원"
- CTA 라벨 (title2, white): "결제하고 예약 완료"

## Color & emphasis
- Background: `background-regular`; 모든 카드 표면 white + `radius-300`. 카드 보더 없음(배경 대비로 구분),
  필요 행 구분만 `divider-regular` 1px.
- Primary CTA: `primary-regular`(#0078FF) fill, 흰색 라벨 — 화면 유일의 강조 액션.
- 텍스트 위계: `text-strong`(타이틀·합계·최종 결제 금액) > `text-primary`(요약 값·요금 값·카드/약관 본문)
  > `text-secondary`(라벨·보조 설명·보유 포인트·하단 금액 라벨) > `text-tertiary`(미사용 수준의 약한 메타).
- 금액 가독성(톤 핵심): 화면 내 모든 금액은 **우측 정렬**로 통일. 합계는 `heading3`/`text-strong`,
  하단 최종 결제 금액은 `heading2`(24 Bold)/`text-strong` — 화면에서 가장 강한 타이포 위계로 "또렷하게".
- 할인 강조: 할인(−) 금액만 `status-positive-regular`(#04CA81), 적용 쿠폰 Tag는
  `status-positive-weak` 배경 + `status-positive-strong` 텍스트로 "이득"을 안심되게 신호.
- 보조 액션 de-emphasis: '변경'·'전액 사용'·'쿠폰 적용하기'·약관 보기(>)는 TextButton/chevron으로
  낮은 강조 — primary CTA와 경쟁하지 않게.

## States
- 기본(default = 결제 가능 상태): 폼이 대표 값으로 채워진 화면. 쿠폰 1개 적용, 기본 카드 등록됨,
  전체 동의 + 필수 약관 모두 체크됨, 포인트 2,000P 입력됨, 요금 Accordion은 기본 **접힘**.
  하단 CTA는 **enabled**(눌러서 결제 가능). 단일 상태이므로 빈 상태/로딩/에러/성공은 out.

## Accessibility
- 최소 터치 타깃: 뒤로가기 IconButton·변경/전액 사용 TextButton·약관 chevron·체크박스는 모두 44x44pt
  이상 히트 영역 확보(시각 아이콘 24, 패딩으로 확장). 아이콘-only 요소엔 aria-label 부여
  (뒤로가기 "뒤로가기", 쿠폰 변경 "쿠폰 변경", 약관 보기 "약관 보기").
- 대비: 최종 결제 금액·합계는 `text-strong`(#141A24) on white로 최고 대비. CTA는 #0078FF on white
  라벨로 4.5:1 이상. 야외 가독성 위해 핵심 금액·CTA는 최대 위계 유지(principles Context & Safety).
- 텍스트 legibility: 본문 최소 `body4`(13px)/`caption1`(12px) 유지, 그 이하 사용 금지. 다국어/긴 값은
  `break-keep`로 단어 중간 줄바꿈 방지. 이용 일시 등 긴 값은 한 줄 우선, 넘치면 단어 단위 2줄.
- one primary action: CTA 1개만 강조(principles Action). 비활성 사유는 별도 상태라 out(기본은 enabled).

## Out of scope
- 기본 외 상태(로딩 / 결제 실패·에러 / 빈 쿠폰 / 결제 완료 후 화면).
- 쿠폰 선택 시트·결제수단 변경 화면·약관 상세 등 연결 화면의 내부.
- 실데이터 연동·금액 계산 로직(대표 더미 값으로 표현).
- 카드 브랜드 정밀 아이콘(generic `icon-card-line` + 텍스트로 대체).
