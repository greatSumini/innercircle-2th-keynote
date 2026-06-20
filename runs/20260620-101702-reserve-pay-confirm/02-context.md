---
run: 20260620-101702-reserve-pay-confirm
stage: context
status: ready
figma_library_available: no
---
# Context pack

쏘카 '예약 확인'(예약·결제 확인) 전체 화면 — 예약 직전 내용 확인 + 결제. 단일 기본 상태.
모바일 포트레이트, 한국어, socarframe 토큰/컴포넌트. 톤: 명료/안심, 금액 가독성 강조.

## Design-system references
- Docs to follow:
  - `color.md` — text/primary/status/background-border-divider semantic 토큰.
  - `typography.md` — heading/title/body/caption 스케일 + Pretendard 빌드 폰트 정책(600 유지).
  - `spacing.md` — spacing-* (4px 그리드), radius-* (카드 radius-300, large 버튼 radius-350).
  - `components-surfaces.md` — TopAppBar, Accordion (요금 세부 펼침/접힘).
  - `components-actions.md` — ActionButton(메인 CTA), TextButton(변경/쿠폰 적용/전액 사용 등 보조 액션).
  - `components-forms.md` — Checkbox/CheckboxGroup(약관), Input(포인트 사용 숫자 입력).
  - `components-feedback.md` — Tag/Badge(쿠폰 적용 라벨·할인 강조, 선택), InfoTip(요금 항목 ⓘ 설명, 선택).
  - `figma-conventions.md` — 프레임/레이어 네이밍, 배치(빈 공간·1행·겹침 금지).
  - `principles.md` — one primary action, 위계/안심 톤 검증.
- Key tokens for this screen:
  - Color:
    - CTA: `primary-regular`(#0078FF) — '결제하고 예약 완료' fill/primary.
    - 텍스트 위계: `text-strong`(제목·최종 결제 금액·합계), `text-primary`(요약 값·요금 값),
      `text-secondary`(라벨·보조 설명·보유 포인트 잔액), `text-tertiary`(아주 약한 메타).
    - 표면/구분: `background-regular`(#F2F3F8 화면 바탕), 카드 fill **white**(#FFFFFF),
      `divider-regular`(합계 위 구분선·항목 구분), `border-regular`(입력/카드 보더).
    - 강조/상태: 할인 금액·쿠폰에 `status-positive-regular`(#04CA81) 또는 `accent-green` /
      `status-information-weak`(쿠폰/안내 배경, 선택). 필수 약관 미동의 안내가 필요할 때만 `status-*`.
    - 금액 가독성: 최종 결제 금액·합계는 `text-strong`, 할인(−) 금액만 positive로 구분.
  - Type:
    - TopAppBar 타이틀 '예약 확인' → `title1`(18 SemiBold) [TopAppBar.Title general].
    - 섹션/카드 타이틀(예약 요약, 요금 상세, 할인 적용, 결제수단, 약관 동의) → `title2`(16 SemiBold).
    - 요약 카드 라벨 → `body3`/`text-secondary`, 값 → `title3`/`text-primary`(반납완료 레퍼런스와 동일).
    - 요금 항목 라벨/값 → `body3`; 합계 라벨 → `title2`/`text-strong`, 합계 값 → `heading3`/`text-strong`.
    - 하단 sticky 최종 결제 금액: 라벨 `title3~title2`/`text-secondary→strong`, 값 `heading2`(24 Bold)
      또는 `heading3`(22 Bold) `text-strong` — 화면에서 가장 강한 위계로 "또렷하게". (plan이 확정)
    - 버튼 라벨: large CTA → `title2`; 보조 TextButton(변경/쿠폰 적용하기/전액 사용) → `title3`/`title4`.
    - 약관 항목 텍스트 → `body3`; '전체 동의' → `title3~body2`(약간 강조).
  - Spacing/radius:
    - 화면 좌우 패딩 `spacing-400`(16px). 섹션(카드) 간 간격 `spacing-300`(12)~`spacing-400`(16).
    - 카드 내부 패딩 `spacing-400`; 행 간 `spacing-300`(12); 타이트 그룹 `spacing-100/150/200`.
    - 카드/표면 radius `radius-300`(12px); 큰 CTA(large) radius `radius-350`(14px);
      입력(Input) radius `radius-250~300`; 쿠폰/포인트 칩성 요소 `radius-circle`(필요 시).

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | general + BasicBackButton(LeftSideIconSlot), Title '예약 확인' | 화면 헤더(뒤로가기 + 타이틀) | components-surfaces.md | 없음 — socarframe 라이브러리 미연결, primitive로 빌드 |
| ActionButton | fill / primary / large | 하단 sticky 메인 CTA '결제하고 예약 완료' | components-actions.md | 없음 |
| TextButton | text / primary(또는 tertiary) / small~medium | '변경'(결제수단), '쿠폰 적용하기', '전액 사용'(포인트) | components-actions.md | 없음 |
| Accordion | options="single", 기본 접힘, Trigger(Label + TrailingIconSlot 회전) | 요금 상세 세부(예: 예상 주행요금) 펼침/접힘 | components-surfaces.md | 없음 |
| Checkbox + CheckboxGroup | default/checked, group label | 약관 동의(전체 동의 + 필수/선택 묶음) | components-forms.md | 없음 |
| Input | filled, 숫자, trailing='원'·clearable, helperText(보유 포인트) | 포인트 사용 입력 | components-forms.md | 없음 |
| IconButton | medium, icon-arrow-left-line/ chevron, aria-label | 뒤로가기, 항목별 보기(>) , 약관 보기(>) | components-actions.md | 없음 |
| Tag | soft/solid, status-positive 또는 accent-green, small | 적용된 쿠폰 라벨·할인액 강조(선택) | components-feedback.md | 없음 |
| InfoTip | trigger(ⓘ) + content | 요금 항목 부가 설명(선택, 톤 보강용) | components-feedback.md | 없음 |
| Divider | divider-regular 1px | 합계 위 구분, 항목/섹션 구분 | figma-conventions.md / color.md | 없음 |

> 모든 socarframe 컴포넌트는 **값 적용(by value) + 레이어 네이밍**으로 직접 빌드. 바인딩된 Figma
> 라이브러리가 없으므로 implement는 figma-conventions.md 네이밍으로 traceable하게 만들어야 함.

## Figma library & reference status
- Library available: **no**. `get_libraries`는 Material 3 Design Kit / Simple Design System /
  iOS·iPadOS·watchOS·visionOS·macOS Apple 키트만 반환 — **socarframe 없음**.
  `search_design_system("ActionButton TopAppBar Accordion Checkbox")`는 무관한 `toast`,
  `Pagination-Module`(generic "LIBRARY")만 반환, socarframe 컴포넌트 키 0건.
  → socarframe 토큰/컴포넌트는 **값으로 직접 빌드**(implement가 local `socarframe` variable collection
  생성 + 레이어 네이밍으로 추적). 컴포넌트 key 인용 금지(존재하지 않음).
- Existing frames / placement:
  - 캔버스(Page 1, id 0:1)에 기존 harness 프레임 **1개**:
    `[auto] 반납 완료 — 20260620-070646-return-complete` (id 3:2, x=200 y=0, 360×857).
  - **레퍼런스로 스타일 일치 대상**(동일 결제·요약 도메인이라 매우 유용):
    - width **360**, 화면 바탕 `background-regular`, 좌우 패딩 16(`spacing-400`).
    - **white 카드 + radius-300**, 카드 타이틀 `title2/text-strong`.
    - 요약 행: 라벨 `body3/text-secondary`(좌), 값 우측 정렬(이용요약=`title3/text-primary`,
      결제요약 항목=`body3`).
    - **합계 강조 행**: 위에 `divider-regular` 1px → 라벨 `title2/text-strong` + 값
      `heading3/text-strong`(우측 정렬). → 우리 '요금 상세' 합계/하단 최종 금액에 동일 패턴 차용.
    - 하단 sticky CTA 영역: full-width `ActionButton fill/primary/large`(56px, blue) + 아래 보조
      `TextButton`. → 우리 '결제하고 예약 완료'에 동일.
  - **새 프레임 배치**: 요청 캔버스 레인대로 **x≈7800, y≈0**(기존 3:2 x=200과 충분히 떨어져 겹침 없음).
    상태 1개 → 프레임 1개, 상태 세그먼트 생략. 프레임명
    `[auto] 예약 확인 — 20260620-101702-reserve-pay-confirm`. (스크롤 본문이 길어 height는 plan이 확정,
    레퍼런스보다 큼.)

## Gaps (needs custom build)
socarframe가 컴포넌트로 직접 제공하지 않아 **primitive 조합으로 빌드**해야 하는 요소:
- **예약 요약 카드** — 차량/쏘카존/이용 일시/대여 시간 행. (DS에 '요약 카드' 컴포넌트 없음;
  레퍼런스 '이용 요약 card' 패턴을 그대로 재사용 = white surface radius-300 + label/value row 빌드.)
- **요금 상세 행 + 합계 강조 블록** — 행은 커스텀, 세부 펼침만 Accordion으로. 합계 강조는
  레퍼런스 '총 결제금액' 패턴(divider + title2/heading3) 차용.
- **할인 적용 섹션** — '쿠폰 선택' 행(적용 쿠폰 Tag 또는 '쿠폰 적용하기' TextButton + chevron) +
  '포인트 사용' 입력 행. SelectionBox/리스트행 컴포넌트가 별도 없어 행 레이아웃은 커스텀, 내부 요소만 DS
  (Input, TextButton, Tag) 재사용.
- **결제수단 행** — 카드사 아이콘 + ****-1234 텍스트 + 우측 '변경' TextButton. 카드 브랜드 아이콘은
  socarframe 아이콘 세트에 없을 수 있어 placeholder/일반 카드 아이콘으로 표현(커스텀).
- **약관 동의 블록** — '전체 동의' 1줄 + 필수/선택 묶음. Checkbox/CheckboxGroup은 DS로 재사용하되,
  각 항목 우측 '보기(>)' chevron + 필수/선택 라벨 레이아웃은 커스텀.
- **하단 sticky 결제 바** — 최종 결제 금액(라벨+값, heading 위계) + primary CTA 묶음. sticky 영역
  컨테이너는 커스텀(레퍼런스 'Bottom fixed CTA region' 패턴 차용), 버튼만 ActionButton.
- **카드 브랜드/일부 결제 아이콘** — socarframe icons.md에 없으면 generic 아이콘 + 텍스트로 대체.

배치 외 위험: 이 화면은 행/섹션이 많아 implement는 figma-conventions.md 네이밍(역할 + 토큰 bracket,
text 노드의 `· <type-token>`)을 일관 적용해야 verify가 토큰을 감사할 수 있음. 라이브러리 미연결이므로
local `socarframe` color/radius/spacing variable collection 생성 권장.
