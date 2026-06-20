---
run: 20260620-101700-car-detail-options
stage: plan
status: ready
frame: 360 x 1180 mobile portrait (scrollable; viewport 360 x 800, content height ~1180)
placement: Page 1, x=6000, y=0 (reserved lane)
---
# Design plan — 차량 상세 & 옵션 선택

## Overview
- **Goal / primary job:** 차량 한 대를 고른 사용자가 차량 정보를 확인하고, 차량손해면책(보험)과 추가 옵션을
  빠르고 신뢰감 있게 정한 뒤, 예상 요금을 보고 예약으로 진행한다.
- **Primary action (emphasized):** 하단 고정 바의 **'예약하기'** (`ActionButton fill/primary/large`) — 화면에서
  유일하게 최강조되는 액션. 그 외 모든 요소는 이 결정을 돕는 보조 역할.
- **Surface:** 풀스크린 (모바일 portrait, 세로 스크롤) + 콘텐츠와 분리된 하단 고정(sticky) 바. BottomSheet/modal 아님.
- **State scope:** 기본 상태 **1종**만 — 보험은 '안심'이 미리 선택(selected)된 상태, 추가 옵션은 미선택.

## Frame
- **Size:** 360 (w) × 1180 (h). SOCAR 모바일 baseline 360px 폭 — 동일 파일의 기준 화면
  `[auto] 반납 완료`(360px)와 폭/거터를 맞춘다. 뷰포트는 360×800로 가정하고, 콘텐츠는 그 아래로 스크롤된다.
- **Placement:** Page 1, **x=6000, y=0** (이번 세션 예약 레인). 기존 프레임(x≤560)과 겹치지 않음. 단일 상태이므로
  Section 래퍼·`· <state>` 접미사 없이 단일 프레임.
- **Frame name:** `[auto] 차량 상세 & 옵션 선택 — 20260620-101700-car-detail-options`
- **Frame fill:** `background-regular` (#F2F3F8).
- **Safe areas / 영역 구조:**
  - **TopAppBar** — 캐러셀 이미지 위에 오버레이(투명 배경, 흰색 글리프). 좌 뒤로가기 / 우 공유·찜. 높이 56px,
    좌우 패딩 `spacing-100`(아이콘 터치영역 내장).
  - **스크롤 콘텐츠** — 캐러셀(풀블리드) → 차량 정보 → 보험 → 추가 옵션 → 요금 안내. 좌우 거터 `spacing-400`(16px),
    콘텐츠 폭 328px(캐러셀만 360 풀블리드 예외).
  - **하단 고정 액션 바** — 화면 하단에 sticky. 좌측 총 예상 요금 + 우측 '예약하기' CTA. 콘텐츠 마지막에 바 높이만큼
    여백(spacer)을 둬 가려지지 않게 한다.

## Layout (top → bottom)

좌우 거터는 별도 표기 없으면 `spacing-400`(16px), 콘텐츠 폭 328px. 섹션 카드는 흰색 표면 + `radius-300`(12px).
표면 카드 사이 세로 간격은 `spacing-300`(12px). 이 표가 빌드 순서의 단일 기준(top→bottom)이다.

| Order | Section (role label) | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|----------------------|-------------------------------------|---------------------------------|---------|
| 1 | 이미지 캐러셀 (Carousel) | Pattern(carousel) — 정적 표현 `(custom)` | 풀블리드 360×240; 이미지 placeholder; 하단 dot row gap `spacing-100`; 상단 위→아래 scrim(투명→black 12%) | 차량 사진 placeholder 1컷 + 도트 5개(1번 active) |
| 2 | TopAppBar (캐러셀 오버레이) | TopAppBar — `LeftSideIconSlot` + `TrailingButtonSlot`(2) | 투명 배경; 글리프 `[fill=white]`; 높이 56; 좌우 패딩 `spacing-100` | 좌: 뒤로가기 / 우: 공유·찜 |
| 2a | ↳ 뒤로가기 | IconButton · medium `[aria-label=뒤로가기]` | `icon-arrow-left-line` `[fill=white]` | — |
| 2b | ↳ 공유 | IconButton · medium `[aria-label=공유하기]` | `icon-share-line` `[fill=white]` | — |
| 2c | ↳ 찜 | IconButton · medium `[aria-label=찜하기]` | `icon-heart-line` `[fill=white]` | — |
| 2d | ↳ 페이지 인디케이터 | Pill `(custom)` `[fill=black/40 radius=radius-circle]` | `caption2` `[fill=white]`; 캐러셀 우하단 | "1 / 5" |
| 3 | 차량 정보 (Vehicle info Card) | `(custom)` 카드 | 흰색 표면 `radius-300`; 패딩 `spacing-400`; 카드 상단이 캐러셀과 -`spacing-400` 만큼 겹쳐 올라옴(라운드 상단) | 모델명·메타·태그·위치 |
| 3a | ↳ 모델명 | Text · heading2 | `text-strong` | "아반떼 CN7" |
| 3b | ↳ 번호판·연식 | Text · body3 | `text-secondary`; 모델명과 gap `spacing-100` | "12가 3456 · 2023년식" |
| 3c | ↳ 연료/인승 태그 행 | Tag · soft/small/capsule ×2 | 태그 gap `spacing-150`; `[bg=status-information-weak text=status-information-strong radius=radius-circle]`; 좌측 아이콘 small | "휘발유"(`icon-gas-station-line`) · "5인승"(`icon-users-line`); 모델 메타와 gap `spacing-200` |
| 3d | ↳ 쏘카존 위치 한 줄 | `(custom)` 아이콘+텍스트 행 | `icon-location-dot-line` `[fill=location-rental]` + Text · body3 `text-secondary`; 아이콘-텍스트 gap `spacing-100`; 태그행과 gap `spacing-200` | "강남 테헤란로 쏘카존 · 도보 3분" |
| 4 | 보험 선택 (보험 SelectionBox Group) | SelectionBoxGroup · single, label="차량손해면책" | 그룹 label `title2` `text-strong`; label→박스 gap `spacing-200`; 박스 간 gap `spacing-150` | 표준/안심/완전 3개 |
| 4a | ↳ 표준 (미선택) | SelectionBox · default | 흰색 표면 `radius-300` `[border=border-regular]`; 패딩 `spacing-400`; 라벨 `title3` `text-primary` | "표준" + "자기부담금 50만원" + "기본 포함" |
| 4b | ↳ 안심 (**선택됨**) | SelectionBox · selected/checked | `[border=primary-regular]`(2px) + `[fill=status-information-weak]`; `radius-300`; 우상단 `icon-check-circle-fill` `[fill=primary-regular]`; 라벨 `title3` `text-strong` | "안심" + "추천" Tag + "자기부담금 30만원" + "+5,500원" |
| 4c | ↳ 완전 (미선택) | SelectionBox · default | `[border=border-regular]` `radius-300`; 라벨 `title3` `text-primary` | "완전" + "자기부담금 0원" + "+9,900원" |
| 5 | 추가 옵션 (추가 옵션 Card) | CheckboxGroup, label="추가 옵션" | 흰색 표면 `radius-300`; 패딩 `spacing-400`; label `title2` `text-strong`; label→항목 gap `spacing-200`; 항목 간 gap `spacing-300` | 하이패스·충전 |
| 5a | ↳ 하이패스 (미선택) | Checkbox · default(unchecked) | 라벨 `body3`/`title3` `text-primary`; 우측 금액 `title3` `text-strong`; check box `[border=border-regular radius=radius-100]` | "하이패스" + 설명 `caption1` `text-secondary` "통행료 자동 결제" + "+1,100원" |
| 5b | ↳ 충전 (미선택) | Checkbox · default(unchecked) | 동일 | "충전 케이블" + 설명 "차량 내 비치" + "무료" |
| 6 | 요금 안내 (요금 안내 Card) | `(custom)` 요약 카드 + Divider | 흰색 표면 `radius-300`; 패딩 `spacing-400`; 타이틀 `title2` `text-strong`; row 간 gap `spacing-200` | 대여요금·보험료·옵션·합계 |
| 6a | ↳ 카드 타이틀 + 안내 | Text · title2 + `icon-info-circle-line` | 타이틀 `text-strong`; info 아이콘 `[fill=text-tertiary]` | "요금 안내" |
| 6b | ↳ 대여요금 row | `(custom)` label/value 행 | label `body3` `text-secondary` / value `body3` `text-primary` | "대여요금 (3시간)" — "33,000원" |
| 6c | ↳ 보험료 row | `(custom)` label/value 행 | 동일; 선택된 보험 반영 | "차량손해면책 (안심)" — "+5,500원" |
| 6d | ↳ 구분선 | Divider `[stroke=divider-regular]` | 합계 위 1px; 위아래 gap `spacing-300` | — |
| 6e | ↳ 예상 합계 row | `(custom)` label/value 행 (강조) | label `title3` `text-strong` / value `title2` `text-strong` | "예상 요금" — "38,500원" |
| 6f | ↳ 요금 안내 캡션 | Text · caption1 | `text-tertiary`; 합계와 gap `spacing-200` | "주행거리 요금은 반납 후 정산돼요." |
| 7 | (하단 바 여백) | spacer · spacing-1000 ×2 (≈88px) | 투명; 콘텐츠 끝 → 고정 바에 가리지 않게 | — |
| 8 | 하단 고정 액션 바 (Bottom CTA Bar) | `(custom)` sticky 바 | 흰색 표면 `[fill=white]`; 상단 `Divider [stroke=divider-regular]`; 내부 패딩 상하 `spacing-300`·좌우 `spacing-400`; 좌/우 사이 gap `spacing-300` | 좌 총 예상 요금 + 우 CTA |
| 8a | ↳ 총 예상 요금 (좌) | `(custom)` 라벨+금액 스택 | 라벨 `caption1` `text-secondary` / 금액 `heading3` `text-strong`; 라벨→금액 gap `spacing-25` | "총 예상 요금" / "38,500원" |
| 8b | ↳ 예약하기 CTA (우) | ActionButton · fill/primary/large | `[fill=primary-regular radius=radius-350]`; 텍스트 `title2` `[fill=white]`; 높이 56px; 좌측 금액 스택을 제외한 잔여 폭 채움(약 180px) | "예약하기" |

## Copywriting (verbatim)
모든 텍스트는 한국어, SOCAR voice(명확·따뜻·간결). 금액은 원화 `00,000원` 표기.

**캐러셀 / 헤더**
- 페이지 인디케이터 (caption2): "1 / 5"
- (아이콘 버튼 aria-label) "뒤로가기" / "공유하기" / "찜하기"

**차량 정보**
- 모델명 (heading2): "아반떼 CN7"
- 번호판·연식 (body3): "12가 3456 · 2023년식"
- 연료 태그 (caption1): "휘발유"
- 인승 태그 (caption1): "5인승"
- 쏘카존 위치 (body3): "강남 테헤란로 쏘카존 · 도보 3분"

**보험 선택**
- 그룹 라벨 (title2): "차량손해면책"
- 표준 — 라벨 (title3): "표준" / 자기부담금 (body3): "자기부담금 50만원" / 요금 (title3): "기본 포함"
- 안심 — 라벨 (title3): "안심" / 추천 Tag (caption1): "추천" / 자기부담금 (body3): "자기부담금 30만원" / 추가요금 (title3): "+5,500원"
- 완전 — 라벨 (title3): "완전" / 자기부담금 (body3): "자기부담금 0원" / 추가요금 (title3): "+9,900원"

**추가 옵션**
- 그룹 라벨 (title2): "추가 옵션"
- 하이패스 — 라벨 (title3): "하이패스" / 설명 (caption1): "통행료 자동 결제" / 요금 (title3): "+1,100원"
- 충전 — 라벨 (title3): "충전 케이블" / 설명 (caption1): "차량 내 비치" / 요금 (title3): "무료"

**요금 안내**
- 카드 타이틀 (title2): "요금 안내"
- 대여요금 라벨 (body3): "대여요금 (3시간)" / 값 (body3): "33,000원"
- 보험료 라벨 (body3): "차량손해면책 (안심)" / 값 (body3): "+5,500원"
- 합계 라벨 (title3): "예상 요금" / 값 (title2): "38,500원"
- 안내 캡션 (caption1): "주행거리 요금은 반납 후 정산돼요."

**하단 바**
- 총 예상 요금 라벨 (caption1): "총 예상 요금"
- 총 예상 요금 금액 (heading3): "38,500원"
- CTA (title2): "예약하기"

> 금액 정합성: 대여요금 33,000원 + 안심 보험 5,500원 = **38,500원**. 추가 옵션은 기본 미선택이므로 합계 미반영.
> 요금 안내 카드의 '예상 요금'과 하단 바의 '총 예상 요금'은 동일 값(38,500원)으로 일치시킨다.

## Color & emphasis
- **배경:** 화면 `background-regular`(#F2F3F8); 모든 섹션 카드·SelectionBox·하단 바 표면은 흰색(#FFFFFF).
- **Primary CTA:** '예약하기' = `primary-regular`(#0078FF) fill + 흰색 텍스트, `radius-350`. 화면 유일 최강조.
- **선택 강조(보험 '안심'):** border `primary-regular`(2px) + weak fill `status-information-weak`(#EBF5FF)
  + 우상단 `icon-check-circle-fill`(`primary-regular`). '추천' Tag도 information 계열(약한 파랑)로 같은 신뢰 톤 유지.
- **텍스트 위계:** `text-strong`(모델명·합계·총 예상 요금 금액·선택된 라벨) > `text-primary`(옵션/요금 값·미선택 라벨)
  > `text-secondary`(번호판·연식·위치·요금 row 라벨) > `text-tertiary`(요금 안내 캡션·info 아이콘·도트 비활성).
- **구분/보더:** 미선택 SelectionBox·Checkbox·하단 바 상단선 = `border-regular`/`divider-regular`. 요금 합계 위 = `divider-regular`.
- **무엇을 강조/비강조하나:** 강조는 (1) '예약하기' CTA, (2) 선택된 '안심' 보험, (3) 총/예상 요금 금액 셋뿐.
  미선택 보험 2개와 미선택 옵션은 중립 보더·`text-primary`로 의도적으로 톤을 낮춰 선택 부담을 줄인다(원칙: Affordance,
  "선택을 어렵지 않게"). 상태 색(positive/negative)은 쓰지 않는다 — 금액 강조는 색이 아니라 `text-strong` 위계로 처리.

## States
- **기본 (Default):** 위 레이아웃 그대로. 보험은 **'안심' 선택됨**(primary border + weak fill + check), 표준·완전은 미선택,
  추가 옵션(하이패스·충전)은 모두 미선택, 요금 합계 38,500원, '예약하기' 활성(enabled). — **이 화면이 디자인하는 유일한 상태.**
- 빈 상태 / 로딩 / 에러 / 다른 보험 선택 변형: **out of scope** (요청상 기본 1종만). 프레임은 단일이므로 frame 이름에
  `· 기본` 접미사 없이 빌드.

## Accessibility
- **최소 터치 타깃 44×44px:** TopAppBar IconButton 3개(뒤로가기/공유/찜)는 글리프 24 + 패딩으로 44 이상 확보.
  Checkbox/SelectionBox는 행 전체가 탭 영역(높이 ≥56). 하단 CTA 높이 56px.
- **아이콘 단독 버튼은 aria-label 필수:** "뒤로가기"·"공유하기"·"찜하기"(레이어명에 `[aria-label=…]` 기록).
- **대비(contrast):** 캐러셀 위 흰색 글리프·"1/5" pill은 상단 scrim(투명→black 12%)·black 40% pill 배경으로 AA 가독성 확보.
  선택 강조는 색(파랑)만이 아니라 check 아이콘 + 보더 두께(2px)로도 구분 — 색각 의존 회피. 본문 텍스트는 `text-strong`/
  `text-primary`로 #FFFFFF 대비 AA 충족.
- **위계·식별:** 금액은 굵기(`text-strong`/`heading3`)로 일관 강조해 야외에서도 빠르게 식별(원칙: Context & Safety).
- **신뢰(Confidence):** 예약 직전 화면에서 대여요금·보험료·합계를 모두 노출하고, 주행거리 정산 조건을 캡션으로 명시해
  "행동 전 결과·조건 요약" 원칙을 충족(Trade-off: Confidence > Essentials).

## Out of scope
- 기본 외 상태(빈/로딩/에러, 보험 미선택·다른 보험 선택 변형, 옵션 선택 변형).
- 이전(차량 목록·검색) 및 이후(예약 확정·결제) 화면, 화면 전환.
- 실제 인터랙션/애니메이션(캐러셀 스와이프, 선택 토글 동작 등) — 정적 표현만.
- 실제 차량 사진(placeholder 이미지로 대체).
