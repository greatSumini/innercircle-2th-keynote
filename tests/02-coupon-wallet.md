# Test 02 — 쿠폰함 (medium specificity)

PROMPT
쏘카 앱에 '쿠폰함' 화면을 새로 디자인해줘. 사용자가 보유한 쿠폰을 확인하고 사용할 수 있는 전체 화면이야. 사용 가능 쿠폰과 사용 완료/만료 쿠폰을 구분해서 보여주면 좋겠어. 쿠폰이 하나도 없을 때(빈 상태)도 함께 디자인해줘.

EXPECT
- clarify: may proceed on assumptions or ask ≤2 blocking questions (e.g. 탭 vs 세그먼트로 구분? 쿠폰 등록 입력 포함?). Records sensible defaults either way.
- context: Tab or SegmentedControl for 사용 가능/만료 구분, Card/list item, Badge or Tag for 상태, empty-state pattern; tokens.
- plan: two states (default list + empty), Korean copy, token-driven hierarchy.
- implement: builds default + empty state frames.
- verify: checks both states present, component correctness, token usage.
