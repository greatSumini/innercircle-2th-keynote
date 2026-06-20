# Test 03 — 결제 화면 (intentionally ambiguous — exercises the clarify loop)

PROMPT
쏘카 결제 화면 하나 만들어줘.

EXPECT
- clarify: STATUS NEEDS_INPUT. Should ask ≤4 batched, blocking questions, e.g.:
  - 어떤 결제 단계? (결제수단 선택 / 결제 확인·요약 / 결제 완료)
  - 전체 화면 vs BottomSheet?
  - 핵심으로 보여줄 정보(금액 구성, 결제수단 목록, 쿠폰/포인트 적용 등)?
  - 디자인할 상태(기본만 / 로딩·실패 포함)?
- orchestrator: asks the user via AskUserQuestion, writes 00-answers-01.md, re-runs clarify.
- After answers: clarify returns READY, pipeline proceeds.
- Use this test INTERACTIVELY (not headless) since it requires answering questions.
