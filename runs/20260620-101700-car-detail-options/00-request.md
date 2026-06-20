---
run: 20260620-101700-car-detail-options
stage: request
figma_file_key: VuBHVaAnA5ORacxMZ9zcH8
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled
date: 2026-06-20
---
# Request
쏘카 앱의 '차량 상세 & 옵션 선택' 화면을 디자인해줘. 차량 한 대를 고른 뒤 보험·옵션을 정하고 예약으로 넘어가기 직전 화면이야.

구성:
- 상단: 차량 이미지 carousel(여러 컷, 도트 인디케이터). 좌측 뒤로가기, 우측 공유/찜 아이콘.
- 차량 정보: 모델명, 번호판·연식, 연료·인승 태그, 쏘카존 위치 한 줄.
- 차량손해면책(보험) 선택: 표준 / 안심 / 완전 3단계를 선택형 박스(또는 라디오)로. 각 항목에 자기부담금과 추가 요금 표기, 선택된 항목 강조.
- 추가 옵션: 하이패스, 충전 등 체크/토글.
- 요금 안내: 대여요금 + 선택한 보험료가 반영된 예상 요금 미리보기.
- 하단 고정 영역: '예약하기'(primary, 가장 강조)와 그 좌측에 총 예상 요금.

상태: 기본(보험은 '안심'이 선택된 상태)만 디자인하면 돼.
톤: 신뢰감 있게, 선택을 어렵지 않게.

## Stated constraints / preferences
- Mobile portrait (SOCAR app screen), Korean copy, SOCAR voice.
- Single state only: default state with insurance "안심(safe)" pre-selected.
- Top: vehicle image carousel with dot indicator; back button (left), share/favorite icons (right).
- Vehicle info: model name, plate number · model year, fuel · seats tags, SOCAR zone location one-liner.
- Insurance (차량손해면책) selection: 표준 / 안심 / 완전 as 3-step selectable boxes/radios. Each shows deductible (자기부담금) + extra fee; selected item emphasized.
- Additional options: 하이패스(toll pass), 충전(charging) etc. as check/toggle.
- Fare info: rental fare + selected insurance fee → estimated fare preview.
- Bottom fixed bar: '예약하기' (primary, strongest emphasis) with total estimated fare to its left.
- Tone: trustworthy; make choices feel easy.
- Parallel batch canvas lane: place top-level frame(s) starting near x=6000, y=0 (this session's reserved lane).
