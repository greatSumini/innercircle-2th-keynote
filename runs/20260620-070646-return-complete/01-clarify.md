---
run: 20260620-070646-return-complete
stage: clarify
status: READY
---
# Clarify

## Understood request
쏘카 앱의 '반납 완료' 전체 화면(모바일 포트레이트)을 디자인한다. 차량 반납을 막 끝낸 사용자가
보는 성공 결과 화면으로, 사용자의 핵심 job은 "내 반납·결제가 정상 처리됐는지 한눈에 확인하고
안심한 뒤 닫기"이다. 상단 우측 닫기(X) → 성공 히어로(체크 아이콘 + 타이틀 + 보조 문구) →
이용 요약 카드 → 결제 요약 카드 → 하단 고정 CTA('확인' primary + 보조 텍스트 버튼 '이용 내역 보기')의
세로 흐름. 기본(성공) 상태 하나만 디자인한다.

## Scope
- In:
  - 전체 화면 1종, 기본(성공) 상태만.
  - TopAppBar trailing의 닫기(X) IconButton.
  - 성공 히어로: 성공 체크 아이콘 + 타이틀 "반납이 완료되었어요" + 한 줄 보조 문구.
  - 이용 요약 카드: 차량 모델명, 쏘카존 이름, 이용 시간(시작~종료 일시), 주행 거리.
  - 결제 요약 카드: 대여요금, 주행요금, 보험료, 총 결제금액(강조).
  - 하단 고정 영역: '확인'(ActionButton fill/primary, large) + '이용 내역 보기'(TextButton).
- Out:
  - 에러/로딩/empty 등 다른 상태.
  - 결제 수단 변경, 영수증 상세, 쿠폰/포인트 적용 등 별도 플로우.
  - 별점/리뷰, 다음 예약 추천 등 추가 섹션(요청 구성에 없음).

## Assumptions (sensible SOCAR / socarframe defaults)
- 모바일 포트레이트 전체 화면, 한국어 카피, socarframe 시맨틱 토큰/컴포넌트 사용 — 레포 규칙·요청 명시.
- 상단 바는 `TopAppBar`를 쓰고 닫기(X)는 `TopAppBar.TrailingButtonSlot` 안 `IconButton`으로 배치(좌측 back 없음, 종료 흐름이므로 닫기만) — TopAppBar 가이드의 trailing 슬롯 용도와 일치.
- 히어로의 보조 문구는 안심 톤의 한 줄(예: "이용해 주셔서 감사해요. 결제 내역을 확인해 주세요." 류) — 정확한 카피는 plan 단계에서 확정.
- 두 요약 카드는 socarframe surface(카드형) 컨테이너에 라벨–값 행을 나열하는 형태로 구성하고, 카드 간/내부 간격은 spacing 토큰으로 처리 — components-surfaces 및 spacing 토큰 사용.
- 결제 요약의 '총 결제금액'은 구분선 아래에서 더 큰 타이포·강한 색 위계(heading/title 토큰)로 강조하고 항목 행은 본문 위계 — principles의 Predictability/위계 원칙.
- 하단 CTA는 화면 하단 고정 영역에 '확인'을 가장 강한 primary로, '이용 내역 보기'를 그 아래 보조 텍스트 버튼으로 배치(수직 스택) — 단일 primary CTA + 보조 액션 패턴.
- 본문은 카드가 길어질 수 있어 스크롤 가능하되 하단 CTA 영역은 고정(sticky) — 한 손 조작/CTA 접근성 원칙.
- 표시 데이터는 plausible한 샘플 값(차량명, 쏘카존명, 일시, 거리, 금액)으로 채운다 — 목업이므로 실데이터 소스 불필요.

## Open questions
(none — 요청과 디자인 시스템만으로 고품질 설계 가능)

STATUS: READY
