---
run: 20260620-101656-zone-explore-map
stage: request
figma_file_key: VuBHVaAnA5ORacxMZ9zcH8
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled
date: 2026-06-20
---
# Request
쏘카 앱의 '쏘카존 탐색' 화면을 디자인해줘. 검색 후 지도에서 주변 쏘카존과 차량을 골라보는 화면이야.

구성:
- 배경: 풀스크린 지도. 쏘카존 핀 마커들이 찍혀 있고 선택된 핀은 강조. (지도 자체는 플레이스홀더로 둬도 돼)
- 상단: 뒤로가기 + 현재 검색어와 이용 날짜·시간을 요약해 보여주는 바.
- 필터: 차종(경차/SUV/전기차), 가격, 즉시예약 같은 Chip을 가로 스크롤로.
- 하단 바텀시트(중간 높이로 열려 있는 상태): "내 주변 OO대" 헤더 아래 차량 리스트 카드들 — 모델명, 쏘카존 이름·도보 거리, 시간당 요금, 상태 태그. 카드 누르면 상세로.

상태: 기본(차량 리스트가 있는 상태). 여유 되면 '주변에 차량 없음' 빈 상태도.
톤: 정보가 많아도 정돈되게, 차를 빠르게 고르도록.

## Stated constraints / preferences
- 풀스크린 지도 배경 (지도 자체는 플레이스홀더 허용), 쏘카존 핀 마커 + 선택된 핀 강조.
- 상단 바: 뒤로가기 + 검색어/이용 날짜·시간 요약.
- 필터: 차종(경차/SUV/전기차), 가격, 즉시예약 Chip을 가로 스크롤로.
- 하단 바텀시트는 중간 높이(half-expanded)로 열린 상태. 헤더 "내 주변 OO대" + 차량 리스트 카드(모델명, 쏘카존 이름·도보 거리, 시간당 요금, 상태 태그). 카드 → 상세 진입.
- 필수 상태: 기본(차량 리스트). 여유되면 '주변에 차량 없음' 빈 상태도.
- 톤: 정보 밀도가 높아도 정돈되게, 차를 빠르게 고르도록.
- 모바일 포트레이트, 한국어 카피, SOCAR voice.
- Parallel batch canvas lane: place top-level frame(s) starting at x=4200, y=0 (this session's reserved lane), lay multiple state frames left→right.
