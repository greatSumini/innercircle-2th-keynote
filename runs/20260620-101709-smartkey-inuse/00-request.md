---
run: 20260620-101709-smartkey-inuse
stage: request
figma_file_key: VuBHVaAnA5ORacxMZ9zcH8
figma_url: https://www.figma.com/design/VuBHVaAnA5ORacxMZ9zcH8/Untitled
date: 2026-06-20
---
# Request
쏘카 앱의 '이용 중(스마트키)' 화면을 디자인해줘. 차량을 빌려 이용하는 동안 차 문을 제어하고 시간을 관리하는 화면이야.

구성:
- 상단: 차량 모델 · 번호판, 남은 이용 시간을 크게(반납 예정 시각도 함께).
- 핵심 컨트롤: 문 열기 / 잠그기, 비상등, 경적(차 찾기)을 큰 버튼으로. 지금 잠겨있는지 상태가 보이게.
- 안내 Tips: "탑승 전 차량 외관을 확인해 주세요" 같은 보조 안내.
- 주요 액션: 이용 시간 연장, 반납하기.
- 하단/구석: 사고·고장 신고와 고객센터로 가는 도움 진입.

상태: 기본은 '잠김' 상태. 가능하면 '열림' 상태 버전도.
톤: 안심되고 즉각적이게. 손이 바쁠 수 있으니 터치 타깃을 크게.

## Stated constraints / preferences
- 모바일 포트레이트, 한국어 카피, SOCAR voice (안심되고 즉각적, 명료).
- 상단: 차량 모델 · 번호판 + 남은 이용 시간(크게) + 반납 예정 시각.
- 핵심 컨트롤(큰 버튼): 문 열기/잠그기, 비상등, 경적(차 찾기). 현재 잠금 상태가 시각적으로 보여야 함.
- 보조 안내 Tips 영역 ("탑승 전 차량 외관을 확인해 주세요" 등).
- 주요 액션: 이용 시간 연장, 반납하기.
- 도움 진입: 사고·고장 신고, 고객센터.
- 상태 버전: 기본 '잠김' + (가능하면) '열림' 버전.
- 큰 터치 타깃(손이 바쁜 상황 고려).
- Canvas lane for this parallel session: place top-level frame(s) starting near x=9600, y=0; lay multiple state frames left→right within this lane; never overlap pre-existing frames.
