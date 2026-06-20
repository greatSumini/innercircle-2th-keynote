---
run: 20260620-101713-usage-history-receipt
stage: context
status: ready
figma_library_available: no
---
# Context pack

이용 내역 리스트 + 영수증 상세(+ 리스트 빈 상태) 두 화면이 재사용해야 할 socarframe
토큰/컴포넌트/패턴과, 직접 만들어야 하는 갭을 정리한다. socarframe은 이 파일에 **바운드 라이브러리로
없으므로**(아래 라이브러리 상태 참고) 모든 토큰은 값으로 적용하고 레이어 이름으로 의도를 남긴다
(`docs/figma-conventions.md`). 같은 파일의 기존 `[auto] 반납 완료` 프레임이 거의 동일한
요약/결제 카드 패턴을 이미 구현해 두었으므로, **그 스타일을 그대로 맞춘다.**

## Design-system references
- Docs to follow:
  - `components-surfaces.md` — **TopAppBar**(리스트=general 타이틀, 상세=BasicBackButton+타이틀),
    **Accordion**(영수증 세부 항목 펼침/접힘, `single` 모드)
  - `components-actions.md` — **ActionButton**(「같은 차 다시 예약」 보조 CTA), **TextButton**(「영수증 문의」 링크형),
    **IconButton**(상세 카드 탭/리스트 row chevron, 빈 상태 보조)
  - `components-feedback.md` — **Tag**(리스트 카드 상태/카테고리 라벨, 옵션), 빈 상태는 전용 컴포넌트 없음 → custom
  - `typography.md` — 숫자 가독성 위계(총 결제금액 `heading3`, 항목 금액 `body3`/`title3`)
  - `color.md` — 텍스트/표면/구분선/할인 강조 시맨틱 토큰
  - `spacing.md` — 화면 패딩 `spacing-400`, 카드 radius `radius-300`
  - `figma-conventions.md` — 프레임/레이어 명명, 배치(빈 공간, 한 줄, 80px 거터)
  - `principles.md` — "정확하고 신뢰감" 톤, 한 화면 한 primary 원칙
- Key tokens for this screen:
  - **Color**
    - 화면 배경: `background-regular` (#F2F3F8) · 카드/시트 표면: `white`
    - 텍스트 위계: 금액·핵심 `text-strong` / 본문값 `text-primary` / 라벨·메타 `text-secondary` /
      비활성·플레이스홀더 `text-tertiary`
    - 보조 CTA(「같은 차 다시 예약」 outlined/secondary) 보더: `border-regular`
    - 구분선: `divider-regular` (카드 내 합계 위 1px), 섹션 구분 `divider-weak`/`border-regular`
    - **할인 금액 강조**: 음수 금액에 `status-positive-regular`(#04CA81, "할인=혜택" 긍정 신호) 또는
      `primary-regular`. 빨강(`status-negative`)은 환불/실패에만 쓰므로 할인엔 쓰지 말 것.
    - 영수증 문의 TextButton: `primary-regular` 텍스트(또는 tertiary 중립). 리스트 진입 chevron: `text-tertiary`
    - 빈 상태 일러스트/아이콘 영역: `background-regular`/`gray-200` 톤, 본문 `text-secondary`
  - **Type** (숫자 가독성 최우선 — 굵기/크기 위계로 금액을 또렷하게)
    - 화면 타이틀(리스트=「이용 내역」, 상세=「영수증」): `heading2`(24/Bold) — 기존 반납완료 hero와 동일
    - 월 구분 섹션 헤더(「2026년 6월」): `title3`(14/SemiBold) `text-secondary`
    - 리스트 카드 차량 모델: `title2`(16/SemiBold) `text-strong` · 일시·쏘카존 메타: `body3`(14/Regular) `text-secondary`
    - 리스트 카드 결제 금액: `title2`(16/SemiBold) `text-strong`, 우측 정렬
    - 상세 요약 카드 타이틀: `title2` `text-strong` · 라벨 `body3 text-secondary` · 값 `title3 text-primary`
      (기존 반납완료 `이용 요약 card`와 1:1)
    - 결제 항목 라벨/금액: `body3`(14) — 라벨 `text-secondary`, 금액 `text-primary`, 우측 정렬
    - **총 결제 금액(강조)**: 라벨 `title2 text-strong` + 값 `heading3`(22/Bold) `text-strong`
      (기존 반납완료 총 결제금액 row와 동일 위계)
    - 결제수단/승인 일시: 라벨 `body4`/`caption1` `text-secondary`, 값 `body3` `text-primary`
    - 버튼 라벨: large=`title2`, medium=`title3` (ActionButton 사이즈 매핑)
  - **Spacing/radius**
    - 화면 좌우 패딩: `spacing-400`(16px) — 기존 프레임과 동일
    - 카드 내부 패딩: `spacing-400`(16px), 카드 간 간격 `spacing-300`(12px)
    - 행 간 간격(요약/결제 rows): `spacing-300`(12px, 기존 프레임의 row 간격 34px≈22행+12갭과 일치)
    - 월 섹션 헤더 ↔ 카드 그룹: `spacing-200`~`spacing-300`, 섹션 간 `spacing-400`
    - 카드/시트 radius: `radius-300`(12px) · 버튼 radius: large=`radius-350`(14px), medium=`radius-300`(12px)
    - 합계 위 divider 전후 여백: `spacing-300`(12px, 기존 프레임 패턴)

## Components to reuse (socarframe)
| Component | Variant / size | Used for | Doc ref | Figma key/name (if found) |
|-----------|----------------|----------|---------|---------------------------|
| TopAppBar | general 타이틀 (리스트) | 리스트 헤더 「이용 내역」 | components-surfaces.md | 라이브러리 없음 — 값으로 빌드 (기존 `TopAppBar (general / trailing-only)` 패턴 참고) |
| TopAppBar | BasicBackButton + 타이틀 (상세) | 영수증 상세 헤더 「영수증」 (좌측 뒤로가기) | components-surfaces.md | 라이브러리 없음 — 값으로 빌드 |
| Accordion | `single`, Trigger=Label+TrailingComp(금액)+TrailingIcon(chevron) | 결제 항목 세부(대여/주행/보험/할인) 펼침·접힘 | components-surfaces.md | 라이브러리 없음 — 값으로 빌드 (data-open으로 chevron 회전) |
| ActionButton | outlined/secondary, large | 「같은 차 다시 예약」 보조 CTA | components-actions.md | 라이브러리 없음 — 값으로 빌드 |
| ActionButton | outlined/secondary 또는 fill/secondary, medium~large | 빈 상태 「차량 둘러보기」 보조 행동 | components-actions.md | 라이브러리 없음 — 값으로 빌드 |
| TextButton | text, secondary/tertiary, medium, (underline 선택) | 「영수증 문의」 링크형 액션 | components-actions.md | 라이브러리 없음 — 값으로 빌드 |
| IconButton | small, icon=chevron-right-line, aria-label | 리스트 카드 진입 표시(보조) | components-actions.md | 라이브러리 없음 — 값으로 빌드 |
| Tag | soft/neutral, small, capsule (선택) | 리스트 카드 상태/카테고리 라벨(예: 「쏘카플랜」, 「단기」) | components-feedback.md | 라이브러리 없음 — 값으로 빌드 |
| Divider | divider-regular 1px | 결제 합계 위 구분선, 카드 내 섹션 구분 | color.md / figma-conventions.md | n/a (Divider 노드) |

> 아이콘은 `icons.md`의 토큰명으로(`icon-chevron-right-line`, `icon-receipt-*`/`icon-document-line` 등
> 빈 상태용, `icon-arrow-left-line` 뒤로가기). plan/implement에서 실제 토큰명 확정.

## Figma library & reference status
- **Library available: no.** `get_libraries`가 반환한 구독 라이브러리는 Material 3 Design Kit,
  Simple Design System, iOS/iPadOS/watchOS/visionOS/macOS Apple 키트들뿐 — **socarframe 라이브러리는
  추가돼 있지 않고**, `libraries_available_to_add`도 비어 있다. `search_design_system("TopAppBar
  ActionButton Accordion")`은 무관한 "Awesome Design System"의 `button`/`barcode` 컴포넌트만 반환 →
  **재사용 가능한 socarframe Figma 컴포넌트 키 없음.** 모든 컴포넌트는 socarframe 스펙에 맞춰 값으로
  직접 빌드하고, `figma-conventions.md`의 레이어 명명으로 의도를 추적한다. implement는 `socarframe`
  로컬 변수 컬렉션(color/radius/spacing)을 만들어 바인딩한다.
- **Existing frames / placement**
  - 기존 프레임 1개: `[auto] 반납 완료 — 20260620-070646-return-complete` (id `3:2`),
    page `0:1` "Page 1", **x=200 y=0 w=360 h=857**. 끝 x≈560.
  - **신규 배치**: 요청대로 **x=11400, y=0**부터 좌→우 한 줄. 기존 프레임(끝 560)과 멀리 떨어져 **겹침 없음**.
    순서(default leftmost): ① `· 리스트` → ② `· 리스트 빈 상태` → ③ `· 영수증 상세`, 80px 거터, 공유 top edge(y=0).
    프레임 폭은 기존과 동일하게 **360**(필요 시 390) 권장.
  - 프레임 명명(figma-conventions, 3개 프레임이므로 상태 세그먼트 필수):
    `[auto] 이용 내역 · 리스트 — 20260620-101713-usage-history-receipt`,
    `[auto] 이용 내역 · 리스트 빈 상태 — 20260620-101713-usage-history-receipt`,
    `[auto] 이용 내역 · 영수증 상세 — 20260620-101713-usage-history-receipt`.
    가능하면 `[auto] 이용 내역 — <run-id>` Section으로 래핑(불가 시 행 배치로 폴백).
  - **참고(매칭) 스크린**: 위 반납 완료 프레임을 영수증 상세의 **스타일 기준**으로 삼는다 —
    `이용 요약 card`(white, `radius-300`, title2 타이틀, body3 라벨/title3 값 우측정렬),
    `결제 요약 card`(body3 항목 rows + `divider-regular` 1px + `title2`+`heading3` 강조 합계 row),
    `background-regular` 배경, 16px 패딩, 하단 CTA region을 그대로 재현 후 Accordion·결제수단·보조액션을 확장.

## Gaps (needs custom build)
- **이용 내역 리스트 카드**: socarframe에 "내역 카드" 컴포넌트가 없음 → 차량 모델(title2)·일시·쏘카존
  (body3)·결제 금액(title2 우측) 레이아웃을 white surface `radius-300` 카드로 custom 빌드. 탭 가능 행이므로
  우측 chevron(IconButton 또는 아이콘)로 진입 가능성 표시. 이름 `이용 내역 Card (custom)`.
- **월별 구분 섹션 헤더**: 전용 컴포넌트 없음 → `title3 text-secondary` 텍스트 헤더 + 그룹 컨테이너 custom.
- **빈 상태(empty state)**: socarframe에 전용 EmptyState 컴포넌트 없음(Skeleton은 로딩용) →
  아이콘/일러스트 + 안내 문구(`body2 text-secondary`) + 보조 행동(ActionButton) 조합을 custom 빌드.
  이름 `Empty state (custom)`.
- **결제 영수증 항목별 Accordion 콘텐츠**: Accordion 컨테이너는 socarframe 스펙을 따르되,
  Trigger(항목명+금액)·Content(세부 내역 rows)·합계 강조 row는 위 결제 카드 패턴으로 custom 구성.
  Trigger TrailingComp에 금액(body3/title3), TrailingIcon에 chevron, `data-open` 회전.
- **결제수단 + 승인 일시 블록**: 전용 컴포넌트 없음 → 라벨/값 rows(body4·body3) custom 빌드
  (요약 카드와 동일한 row 패턴 재사용).
- **할인 금액 표기 규칙**: socarframe에 음수/할인 전용 토큰 없음 → 본 컨텍스트의 규칙 적용
  (할인은 `status-positive-regular` 또는 `primary-regular`, `−` 부호 + 1,000단위 콤마 + 「원」).
