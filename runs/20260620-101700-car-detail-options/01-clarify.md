---
run: 20260620-101700-car-detail-options
stage: clarify
status: READY
---
# Clarify

## Understood request
'차량 상세 & 옵션 선택' 화면 — 사용자가 차량 한 대를 고른 뒤, 보험(차량손해면책)과 추가 옵션을 정하고
요금을 확인한 다음 '예약하기'로 넘어가기 직전의 스크롤형 **풀스크린**(모바일 portrait) 화면입니다.
Primary user job은 "보험·옵션을 빠르고 신뢰감 있게 선택하고 예약으로 진행"하는 것이고, primary action은
하단 고정 바의 '예약하기'(primary CTA) 하나입니다. 디자인 대상은 **기본 상태 1종**(보험 '안심' 선택됨)뿐입니다.

## Scope
- In:
  - 상단 차량 이미지 carousel(여러 컷 + 도트 인디케이터), TopAppBar(좌: 뒤로가기 / 우: 공유·찜 아이콘).
  - 차량 정보 블록: 모델명, 번호판·연식, 연료·인승 태그, 쏘카존 위치 한 줄.
  - 차량손해면책(보험) 선택: 표준 / 안심 / 완전 3단계, 각 항목에 자기부담금 + 추가 요금, '안심' 선택 강조.
  - 추가 옵션: 하이패스, 충전 등 체크/토글.
  - 요금 안내: 대여요금 + 선택 보험료 반영 예상 요금 미리보기.
  - 하단 고정 바: 좌측 총 예상 요금 + 우측 '예약하기'(primary, 최강조).
- Out:
  - 기본 외 상태(empty / loading / error / 보험 미선택 / 다른 보험 선택 변형) — 요청상 기본 1종만.
  - 이전(차량 목록·검색) 및 이후(예약 확정·결제) 화면.
  - 실제 인터랙션/애니메이션 동작(carousel 스와이프 로직 등은 정적 표현으로만).

## Assumptions (sensible SOCAR / socarframe defaults)
- **Surface = 스크롤 가능한 풀스크린**, 모바일 portrait — "예약으로 넘어가기 직전 상세 화면"은 BottomSheet가 아니라
  전체 화면이 SOCAR 관례에 맞음. 하단 바는 콘텐츠와 분리된 고정(sticky) 영역.
- **TopAppBar** 사용: `LeftSideIconSlot`에 `BasicBackButton`, `TrailingButtonSlot`에 공유(`share-line`)·찜(`heart-line`)
  IconButton 2개(최대 3개 제한 내). 이미지 위 오버레이 방식으로 배치.
- **이미지 carousel**은 socarframe Carousel Pattern 형태로, 화면 폭 풀블리드 + 하단 도트 인디케이터(현재 1번 활성).
  실제 차량 사진은 플레이스홀더 이미지로 표현.
- **보험 3단계 선택은 `SelectionBoxGroup`(selectionType="single")** + `SelectionBox` — 각 항목에 라벨(표준/안심/완전),
  자기부담금·추가요금 등 리치 콘텐츠가 들어가므로 단순 Radio보다 SelectionBox가 적합. '안심'이 selected 상태(강조).
- **추가 옵션은 `Checkbox`(다중 선택)** 또는 토글 — 하이패스/충전은 독립 on/off라 CheckboxGroup으로. 기본 미선택으로 가정.
- **요금/CTA 텍스트 위계**: 섹션 타이틀 `heading*`/`title*`, 본문 `body*`, 보조정보 `caption*`, 금액 강조는 `text-strong`.
  CTA는 `ActionButton fill/primary`, size `large`(`title2`, `radius-350`). 좌측 총 예상 요금은 강조 금액 + 보조 라벨.
- **컬러/타이포/스페이싱/라디우스는 socarframe 시맨틱 토큰**으로만(선택 강조 = `primary-*` 계열, 표면 `background-regular`,
  구분선 `divider-*`, 화면 패딩 `spacing-400`). 보험 항목 강조 배지가 필요하면 `Tag`/`Badge`(예: '추천') 사용.
- **Copy는 한국어**, SOCAR voice(명확·따뜻·간결). 금액은 원화 `12,000원` 표기. 정확한 카피·수치·간격은 plan 단계에서 확정.
- **Figma 배치**: top-level frame을 이번 세션 예약 레인 x=6000, y=0 부근에 겹치지 않게 배치. 프레임명
  `[auto] 차량 상세 & 옵션 선택 — 20260620-101700-car-detail-options`(단일 상태이므로 `· <state>` 접미사 생략).

STATUS: READY
