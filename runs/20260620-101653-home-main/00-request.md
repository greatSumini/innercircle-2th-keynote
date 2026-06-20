---
run: 20260620-101653-home-main
stage: request
figma_file_key: VuBHVaAnA5ORacxMZ9zcH8
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled
date: 2026-06-20
---
# Request
쏘카 앱의 '홈(메인)' 화면을 디자인해줘. 앱을 켜면 처음 보는 화면으로, 예약 진입과 현재/예정 이용을 한눈에 보여주는 게 목표야.

구성:
- 상단 바: 현재 위치(또는 자주 가는 목적지) 주소를 보여주고, 우측에 알림 아이콘(읽지 않은 알림이 있으면 dot badge).
- 검색 진입: "어디서 탈까요?" 같은 큰 검색 박스. 누르면 쏘카존/목적지 검색으로 가는 진입점이야.
- 진행 중/예정 예약 카드: 차량 썸네일 + 모델명 + 이용 시간 + 쏘카존, 그리고 바로 '스마트키' 또는 '예약 상세'로 가는 버튼.
- 추천/혜택 배너 carousel: 도트 인디케이터 있는 2~3장(신규 할인, 주행 리워드 등).
- 퀵메뉴: 아이콘 + 라벨 그리드(쏘카플랜, 부름/편도, 쿠폰함, 이벤트 등).

상태: 예약이 있는 버전과 예약이 없는(첫 화면) 버전 두 가지로 보여줘.
톤: 활기차고 깔끔하게, 다음 행동(예약)을 자연스럽게 유도.

## Stated constraints / preferences
- 화면: 홈(메인) — 앱 진입 시 처음 보이는 화면.
- 목표: 예약 진입 + 현재/예정 이용 현황을 한눈에.
- 필수 섹션: ① 상단 바(위치 주소 + 알림 아이콘/dot badge), ② 큰 검색 박스("어디서 탈까요?"), ③ 진행 중/예정 예약 카드(썸네일+모델명+이용시간+쏘카존+스마트키/예약상세 버튼), ④ 혜택 배너 carousel(도트 인디케이터, 2~3장), ⑤ 퀵메뉴 아이콘 그리드(쏘카플랜, 부름/편도, 쿠폰함, 이벤트 등).
- 상태 2종: (A) 예약 있음 버전, (B) 예약 없음(첫 화면) 버전.
- 톤: 활기차고 깔끔, 다음 행동(예약) 자연 유도.
- 디바이스: 모바일 세로(별도 명시 없음 → 기본값).
- 언어: 한국어, SOCAR 보이스.

## Parallel batch note (this session)
- Canvas lane reserved for THIS session: top-level frame(s) start near x=2400, y=0; lay multiple state frames left→right within this lane. Never overlap pre-existing frames.
