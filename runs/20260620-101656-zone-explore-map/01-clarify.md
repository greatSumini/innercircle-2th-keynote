---
run: 20260620-101656-zone-explore-map
stage: clarify
status: READY
---
# Clarify

## Understood request
쏘카 앱의 '쏘카존 탐색' 화면. 검색 후 풀스크린 지도 위에서 주변 쏘카존과 차량을 비교·선택하는
모바일 포트레이트 화면이다. 주 사용자는 차를 빌리려는 이용자이고, 단일 핵심 과업은 "주변 차량을
빠르게 훑어보고 1대를 골라 상세로 진입"하는 것. 표면은 풀스크린 지도(배경) 위에 상단 요약 바 +
가로 스크롤 필터 칩, 그리고 half 디텐트로 열린 BottomSheet(차량 리스트)가 오버레이된 단일 화면이다.

## Scope
- In:
  - 풀스크린 지도 배경(플레이스홀더 허용) + 쏘카존 핀 마커, 선택된 핀 강조 1개.
  - 상단 바: 뒤로가기 + 검색어 + 이용 날짜·시간 요약(한 줄/두 줄).
  - 필터 영역: 차종(경차/SUV/전기차)·가격·즉시예약 Chip을 가로 스크롤로.
  - BottomSheet (half 디텐트, 핸들바): 헤더 "내 주변 OO대" + 차량 리스트 카드.
  - 카드 필드: 모델명, 쏘카존 이름·도보 거리, 시간당 요금, 상태 태그(Tag). 카드 탭 → 상세 진입.
  - 상태: 기본(차량 리스트 있음) [필수]. '주변에 차량 없음' 빈 상태 [보너스, 여유 시].
- Out:
  - 실제 지도 타일/지오 데이터, 핀 클러스터링 로직.
  - 검색 입력 화면, 날짜·시간 선택 플로우(DatePicker/TimePicker 자체 화면).
  - 차량 상세 화면, 예약/결제 플로우.
  - tip·max 디텐트 인터랙션 명세(시각 상태는 half 1종만).
  - 지도 사용자 위치 추적/내 위치 버튼 동작 로직(아이콘 노출은 plan 재량).

## Assumptions (sensible SOCAR / socarframe defaults)
- 모바일 포트레이트, 한국어 카피, SOCAR 보이스 — CLAUDE.md / 요청 명시.
- 상단 바는 TopAppBar 패턴(LeftSideIconSlot에 BasicBackButton) + 검색어/날짜·시간 요약을 label
  형태로 — 지도 위 오버레이라 흰 배경 바로 시인성 확보. 정확한 요약 카피/줄수는 plan에서 결정.
- 필터는 Chip(role=button, size=medium 기준) 가로 스크롤, 다중 선택 토글 — 차종/가격/즉시예약은
  서로 독립 필터라 토글이 자연스럽고 socarframe Chip의 기본 용도와 일치.
- BottomSheet는 half 디텐트, showHandlebar=true, dimmed=false(지도 상호작용 유지) 가정 —
  지도 탐색과 리스트를 동시에 보는 것이 이 화면의 핵심이므로 배경 딤은 부적합.
- 차량 카드는 모델명/쏘카존·도보거리/시간당 요금/상태 Tag를 한 카드에 정돈한 리스트 아이템 —
  카드 디테일(레이아웃·강조)은 plan에서, 토큰은 spacing/radius/typography 시맨틱 사용.
- 상태 태그는 socarframe Tag 컴포넌트로 표현(예: 즉시예약/할인/만차 등) — 정확한 라벨·색은 plan.
- 빈 상태는 보너스 프레임으로 제작: BottomSheet 안에 안내 일러스트/문구 + 필터 초기화류 보조 액션,
  지도/상단 바/필터는 유지 — '여유 되면'이므로 시간 허용 시 추가.
- 캔버스 배치: top-level 프레임을 x=4200, y=0부터 좌→우로(기본 → 빈 상태) 겹치지 않게 — 요청의
  reserved lane 지시. 프레임명은 figma-conventions의 `[auto] 쏘카존 탐색 — <run-id> · <state>`.
- 색/타입/간격/라운드/아이콘은 socarframe 시맨틱 토큰만 사용, 로(raw) hex/px 금지 — repo 규칙.

## Open questions
(none — 요청이 표면·주요 데이터·상태·과업을 모두 명시하여 합리적 기본값으로 진행 가능)

STATUS: READY
