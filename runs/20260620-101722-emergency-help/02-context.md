---
run: 20260620-101722-emergency-help
stage: context
status: ready
figma_library_available: no
---
# Context pack

SOCAR '사고·고장 신고(긴급 도움)' 풀스크린(기본 상태 1종). 1차 과업 = 당황한 사용자가 즉시
전화로 도움받기. 위급함은 status 색으로 절제해서 전달(긴급 액션=negative, 주의 안내=caution),
브랜드 primary는 보조에만. socarframe은 바인딩된 Figma 라이브러리가 아니므로 모든 토큰은
값으로 적용하고 레이어 이름으로 추적성 확보(아래 placement 규칙).

## Design-system references
- Docs to follow:
  - `principles.md` — One primary action / 위계, release checklist(한 손 조작·야외 식별·당황 최소화).
  - `color.md` — semantic tokens, 특히 `status-*`(negative/caution) 선택 가이드, text 위계.
  - `typography.md` — `heading*`/`title*`/`body*`/`caption*`, Pretendard build-font 정책(600 유지).
  - `spacing.md` — spacing(4px grid) + radius 토큰(px↔token 매핑).
  - `icons.md` — `icon-phone-fill`, `icon-car-*`, `icon-warning-*`, `icon-exclamation-*` 등.
  - `components-surfaces.md` — TopAppBar(Left/Title/Trailing).
  - `components-actions.md` — ActionButton(fill/primary·secondary), IconButton, TextButton, Haptic.
  - `components-forms.md` — SelectionBox / SelectionBoxGroup(single, 아이콘+카드), Chip(보조).
  - `components-feedback.md` — Tips(InfoTip/AccentTip 패턴), Tag/Badge(차량 식별·상태 라벨).
- Key tokens for this screen:
  - Color
    - 긴급 액션 카드(최강조): 배경 `status-negative-weak`(#FFF0F3), 포인트/아이콘 `status-negative-regular`(#FF3A5B), 강조 텍스트 `status-negative-strong`(#F51441). 주: status는 액션/경고 영역에만 절제.
    - 전화 CTA 버튼: **`status-negative-regular` 채움 버튼**(위급함 전달). ActionButton primary(브랜드 블루)는 이 화면의 1차 강조로 쓰지 않음 — 1차 강조는 위급 영역으로 수렴(One primary action).
    - 보조 액션(고객센터 2차): `status-negative` outlined 또는 `secondary`(blue-100 배경)로 한 단계 낮춤.
    - 주의 안내 Tips: 배경 `status-caution-weak`(#FFF8E6), 아이콘/포인트 `status-caution-regular`(#FF8800), 텍스트 `text-primary`.
    - 상황 선택 SelectionBox: 카드 `background-regular`/white 표면 + `border-regular`(#E5E8EF), 아이콘 `text-secondary`, 라벨 `text-strong`.
    - 차량 정보 카드: white 표면, 라벨 `text-secondary`, 값 `text-strong`, 식별 Tag는 `accent-*`/`text` 토큰.
    - 텍스트 위계: 타이틀 `text-strong`, 부제/설명 `text-secondary`, 메타 `text-tertiary`.
    - 표면/배경: 페이지 `background-regular`, 카드 white, 구분선 `divider-regular`.
  - Type
    - 화면 타이틀 「도움이 필요하신가요?」 → `heading2`(24/34, Bold).
    - 안심 부제 한 줄 → `body2`(16/24, Regular) `text-secondary`.
    - 섹션 헤더(상황 선택·차량 정보·FAQ) → `title2`(16/24, SemiBold).
    - 긴급 카드 타이틀/전화 라벨 → `title2`/`title3`; 보조 설명 → `body3`(14/22).
    - 버튼 라벨: large 버튼 → `title2`; medium → `title3`.
    - Tips 본문 → `body3`/`caption1`; FAQ 항목 → `body2`/`title3`; 메타·번호판 → `caption1`/`body4`.
  - Spacing/radius
    - 화면 좌우 패딩 `spacing-400`(16px). 섹션 간 간격 `spacing-300`~`spacing-400`(12–16px).
    - 카드 내부 패딩 `spacing-400`; 카드 내 행 간격 `spacing-200`~`spacing-300`.
    - 아이콘↔텍스트 `spacing-100`~`spacing-200`; 타이틀↔부제 `spacing-150`.
    - Radius: 카드/Tips/SelectionBox 표면 `radius-300`(12px). large 버튼 `radius-350`(14px),
      medium 버튼 `radius-300`(12px). 원형 아이콘 백드롭 `radius-circle`. (px↔token 정확히 매칭)

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | general · Left=BasicBackButton(뒤로가기) 또는 Trailing 닫기 | 화면 헤더(뒤로가기/닫기) | components-surfaces.md | 라이브러리 없음 — 값으로 빌드 (참조: 기존 `[auto] 반납 완료` 3:3 TopAppBar 패턴) |
| IconButton | medium · `icon-arrow-left-line`(뒤로) / `icon-close-line`(닫기) [aria-label] | 헤더 네비 아이콘 | components-actions.md | 없음 — 값으로 빌드 (참조 IconButton 3:4) |
| ActionButton | fill / **negative** / large — 전화 CTA(긴급출동/전화 연결) | 1차 긴급 액션(최강조) | components-actions.md | 없음 — fill을 `status-negative-regular`로 채워 빌드. leftIcon=`icon-phone-fill` |
| ActionButton | outlined/secondary 또는 fill/secondary / large — 고객센터 전화 | 2차 보조 액션 | components-actions.md | 없음 — 값으로 빌드 |
| SelectionBox + SelectionBoxGroup | selectionType=single, 아이콘+라벨 카드 리스트(사고/고장/기타 문의) | 상황 선택(진입점) | components-forms.md | 없음 — 카드형 selectable 빌드. 각 행 leftIcon + 라벨 + `icon-chevron-right-line` |
| Tips (InfoTip/AccentTip 패턴) | caution 톤, static · 「안전한 곳으로 이동한 뒤 신고해 주세요」 | 주의 안내 배너 | components-feedback.md | 없음 — `status-caution-weak` 배경 + `icon-exclamation-triangle-fill` 인라인 배너로 빌드 |
| Card (surface) | white, `radius-300`, 라벨/값 행 | 현재 이용 중 차량 정보 요약 | (figma-conventions) | 없음 — `(custom)` 표면. 참조 `이용 요약 card` 6:2 패턴 재사용 |
| Tag | soft/neutral, small/medium, capsule | 번호판/차량 식별·이용중 상태 라벨 | components-feedback.md | 없음 — 값으로 빌드 |
| TextButton 또는 List row | text/tertiary 또는 리스트 행 + `icon-chevron-right-line` | FAQ 진입(1~3개 + 전체 보기) | components-actions.md | 없음 — 값으로 빌드 (참조 TextButton 6:37) |
| Divider | `divider-regular`, 1px | 카드 내/섹션 구분 | (figma-conventions) | 없음 — 값으로 빌드 (참조 divider 6:29) |

아이콘 후보(icons.md, SOCAR Icon Library): `icon-phone-fill`(전화/긴급출동·1차), `icon-headset` 없음 →
고객센터는 `icon-message-dots-line`/`icon-phone-line` 사용, `icon-car-line`/`icon-car-fill`(차량 정보),
`icon-exclamation-triangle-fill`/`icon-warning-light-line`(사고·주의), `icon-horn-fill`(고장/경적),
`icon-message-question-line`/`icon-question-circle-line`(기타 문의·FAQ), `icon-chevron-right-line`(리스트 이동),
`icon-arrow-left-line`/`icon-close-line`(헤더).

## Figma library & reference status
- Library available: **no.** `get_libraries` 반환 라이브러리는 Material 3 Design Kit, Simple
  Design System, iOS/iPadOS/watchOS/visionOS/macOS Apple 키트뿐 — **socarframe 없음**.
  `search_design_system("ActionButton TopAppBar SelectionBox Tips")` 결과도 socarframe 컴포넌트/
  변수/스타일 0건(무관한 `toast`, `Pagination-Module`만). → 모든 토큰·컴포넌트는 **값으로 적용**,
  레이어 이름에 역할+토큰 표기로 추적성 확보(figma-conventions §3). 색 변수는 implement가 로컬
  `socarframe` 컬렉션(`color/…`)으로 materialize 권장.
- Existing frames / placement:
  - Page 1(`0:1`)에 기존 harness 프레임 1개: `[auto] 반납 완료 — 20260620-070646-return-complete`
    (`3:2`, x=200 y=0, 360×857, 우측 끝 x≈560). **이 화면이 스타일 레퍼런스** — 360px 포트레이트,
    페이지 배경 `background-regular`, white 카드 `radius-300`+옅은 그림자, 헤더 닫기 아이콘,
    중앙 hero(아이콘 원형 백드롭 + `heading2` 타이틀 + `body2` 부제), 라벨/값 요약 카드,
    하단 고정 CTA(full-width ActionButton + 아래 TextButton). 새 화면은 이 레이아웃 DNA를
    따르되 success(green) 대신 **urgency(status-negative/caution)** 팔레트로 전환.
  - **Placement for the new frame:** 요청의 세션 전용 레인대로 **x≈15000, y≈0**에서 시작
    (기존 프레임 x=200–560과 충분히 떨어져 겹침 없음). 단일 상태이므로 상태 세그먼트 생략한
    프레임명 `[auto] 사고·고장 신고(긴급 도움) — 20260620-101722-emergency-help`. 360px 폭 권장
    (레퍼런스와 동일), 한 행에 배치, 한 프레임이라 Section 래퍼는 선택.

## Gaps (needs custom build)
- **socarframe가 바인딩 라이브러리로 없음** → TopAppBar / ActionButton / SelectionBox / Tips /
  Tag / IconButton 전부 socarframe 인스턴스가 아닌 **프리미티브로 값 빌드**. 토큰은 레이어 이름
  브래킷 표기(`[fill=status-negative-regular]` 등)로 추적성 확보. implement는 로컬 `socarframe`
  변수 컬렉션(최소 색)을 만들고 바인딩 권장.
- **긴급출동 전용 컴포넌트/패턴 없음** — 사고·고장 긴급 신고 전용 카드(전화 1차 + 고객센터 2차)는
  도메인 특화 UI. ActionButton + 카드 표면 + status-negative 토큰으로 조합 빌드(custom),
  「One primary action」 위계 유지.
- **status-negative 채움 ActionButton** — socarframe ActionButton fill variant는 primary/
  secondary/tertiary(블루/그레이)만 정의. 위급 전달용 빨강 채움 버튼은 fill을
  `status-negative-regular`로 적용한 **변형 빌드**(문서상 표준 variant 아님 — 의도적 도메인 적용).
- **차량 정보 요약 카드 데이터** — 차량명/번호판은 placeholder(실데이터 소스 out of scope, plan에서
  더미 카피 확정). 표면 자체는 레퍼런스 `이용 요약 card` 패턴 재사용.
- **헤드셋/상담원 아이콘 부재** — SOCAR Icon Library에 전용 고객센터 아이콘 없음 →
  `icon-phone-line` 또는 `icon-message-dots-line`로 대체.
