# Test 01 — 반납 완료 화면 (fully specified, headless-safe)

PROMPT
쏘카 앱의 '반납 완료' 화면을 디자인해줘. 사용자가 차량 반납을 막 완료한 직후 보는 전체 화면(모바일 포트레이트)이야. 기본(성공) 상태 하나만 디자인하면 돼.

구성:
- 상단 우측에 닫기(X) 아이콘 버튼.
- 성공을 알리는 큰 타이틀("반납이 완료되었어요")과 그 위에 성공 체크 아이콘, 아래 한 줄 보조 문구.
- 이용 요약 카드: 차량 모델명과 쏘카존 이름, 이용 시간(시작~종료 일시), 주행 거리.
- 결제 요약 카드: 대여요금, 주행요금, 보험료, 총 결제금액(강조).
- 하단 고정 영역: 기본 CTA '확인'(primary, 가장 강조), 그 위 또는 아래에 보조 액션 '이용 내역 보기'(텍스트 버튼).
- 톤: 깔끔하고 안심되는 느낌. socarframe 토큰/컴포넌트를 사용해줘.

EXPECT
- clarify: STATUS READY on round 1 (request is unambiguous; no user questions).
- context: identifies TopAppBar/IconButton, ActionButton (fill/primary/large), text + spacing tokens; checks Figma library.
- plan: top→bottom layout table, real Korean copy, semantic tokens (primary-regular CTA, text-strong title, total amount emphasized), 360-wide frame.
- implement: one frame "[auto] 반납 완료 …" built in Figma with tokens; node id + link in artifact.
- verify: rubric mostly PASS; concrete fixes if any; VERDICT PASS or one bounded REVISE.
