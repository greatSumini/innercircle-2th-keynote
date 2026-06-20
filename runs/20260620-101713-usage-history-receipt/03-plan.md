---
run: 20260620-101713-usage-history-receipt
stage: plan
status: ready
frame: 360 x 800 mobile portrait (3 frames; height grows to content)
---
# Design plan — 이용 내역 & 영수증

세 개의 풀스크린 프레임을 설계한다. (1) **이용 내역 리스트**(기본) — 지난 이용을 월별로 묶은
카드 리스트, (2) **이용 내역 리스트 빈 상태** — 내역이 하나도 없을 때, (3) **영수증 상세** — 카드 탭 시
진입하는 결제 영수증. 톤은 정확하고 신뢰감 있게. **숫자(특히 결제 금액) 가독성이 최우선**이며, 금액은
굵기·크기 위계 + 우측 정렬 + 1,000단위 콤마 + 「원」으로 또렷하게 읽히도록 설계한다. 같은 파일의 기존
`[auto] 반납 완료` 프레임의 요약/결제 카드 스타일(white surface · `radius-300` · 16px 패딩 ·
`divider-regular` 합계선 · `title2`+`heading3` 합계 위계)을 그대로 맞춘다.

## Overview
- **Goal / primary job:** 사용자가 "내 지난 이용을 빠르게 훑고 한 건을 골라 결제 내역을 정확히 확인"한다.
  리스트는 스캔·진입, 상세는 신뢰감 있는 금액 확인이 핵심.
- **Primary action (emphasized):**
  - 리스트(기본): **이용 내역 카드 탭 → 영수증 상세 진입**. 카드 자체가 화면의 1차 행동(가장 위쪽 첫 카드가
    primary 진입점). 별도 강조 CTA는 두지 않는다(리스트는 탐색 화면).
  - 빈 상태: **「차량 둘러보기」**(`ActionButton fill/primary/large`) — 화면에서 유일하게 강조된 1차 행동.
  - 영수증 상세: **「같은 차 다시 예약」**(`ActionButton outlined/secondary/large`) 보조 CTA가 하단 고정.
    요청의 "텍스트/보조 버튼" 위계를 따라 primary-fill은 쓰지 않고, 「영수증 문의」는 TextButton(링크형)으로
    한 단계 더 낮춘다. → 화면의 강조 1순위는 **총 결제 금액(heading3)**, 행동 1순위는 「같은 차 다시 예약」.
- **Surface:** 세 프레임 모두 full screen(BottomSheet/모달 아님). 리스트→상세는 페이지 전환.

## Frame
- **Size:** 360 wide × 800 tall (SOCAR 모바일 baseline, 기존 `반납 완료` 프레임 360폭과 동일). 높이는
  콘텐츠에 맞춰 가변(상세는 더 길어질 수 있음, 800 기준 + 하단 CTA 고정 영역).
- **Safe areas / TopAppBar / bottom action area**
  - 상단: TopAppBar 56px 고정. 리스트·빈 상태는 `general` 타이틀(좌측 정렬, trailing 없음). 상세는
    LeftSideIconSlot에 BasicBackButton(`icon-arrow-left-line`) + `general` 타이틀.
  - 좌우 안전 패딩: `spacing-400`(16px) 일괄.
  - 하단 액션 영역(상세만): 하단 고정 CTA region — white 배경 + 상단 `divider-regular` 1px,
    내부 패딩 `spacing-400`, 「같은 차 다시 예약」 large 버튼 1개. 그 위에 「영수증 문의」 TextButton.
  - 배경: 전 화면 `background-regular`(#F2F3F8), 카드/시트 표면은 `white`.

---

## Frame 1 — 이용 내역 리스트 (기본)
프레임명: `[auto] 이용 내역 & 영수증 — 20260620-101713-usage-history-receipt · 기본`
배치: 레인 시작 **x=11400, y=0**, w=360. (좌측 leftmost)

### Layout (top → bottom)
| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 1 | Top app bar | TopAppBar (general 타이틀, trailing 없음) | bg `white` / 타이틀 `heading2` `text-strong` / 높이 56 · 좌우 pad `spacing-400` | "이용 내역" |
| 2 | 안내 캡션(보조) | 텍스트(custom) | `body3` `text-secondary` / 상단 `spacing-300` 하단 `spacing-200` · 좌우 `spacing-400` | "최근 6개월 이용 내역이에요." |
| 3 | 월 섹션 헤더 ①  | 월 구분 헤더 (custom) | `title3`(14/SemiBold) `text-secondary` / 위 `spacing-200` 아래 `spacing-200` · 좌우 `spacing-400` | "2026년 6월" |
| 4 | 이용 내역 Card ①  | 이용 내역 Card (custom) — white surface `radius-300` | 카드 pad `spacing-400` · 카드 간 `spacing-300` / 모델 `title2` `text-strong` · 메타 `body3` `text-secondary` · 금액 `title2` `text-strong` 우측정렬 · chevron `text-tertiary` | 모델 "아반떼 CN7" · 일시 "6월 14일(토) 14:00–18:30" · 존 "강남역 1번출구 쏘카존" · 금액 "42,800원" · ` icon-chevron-right-line` |
| 5 | 이용 내역 Card ②  | 이용 내역 Card (custom) | 위와 동일 | 모델 "캐스퍼" · "6월 7일(일) 09:00–13:00" · "마포 합정역 쏘카존" · "28,500원" |
| 6 | 월 섹션 헤더 ②  | 월 구분 헤더 (custom) | `title3` `text-secondary` / 위 `spacing-400`(섹션 간) 아래 `spacing-200` | "2026년 5월" |
| 7 | 이용 내역 Card ③  | 이용 내역 Card (custom) | 위와 동일 | 모델 "더 뉴 그랜저" · "5월 24일(토) 10:00–22:00" · "수서역 쏘카존" · "98,000원" |
| 8 | 이용 내역 Card ④  | 이용 내역 Card (custom) | 위와 동일 | 모델 "레이" · "5월 9일(금) 19:00–23:00" · "강남 신논현역 쏘카존" · "31,200원" |
| 9 | 리스트 하단 여백 | spacer (custom) | `spacing-800`(32px) | — |

**이용 내역 Card 내부 구조(custom, row 패턴):**
- 좌측 컬럼(세로 스택, gap `spacing-100`): 모델명(`title2 text-strong`) → 일시(`body3 text-secondary`)
  → 쏘카존(`body3 text-secondary`).
- 우측 컬럼(세로 중앙, gap `spacing-100`): 결제 금액(`title2 text-strong`, 우측 정렬) → 그 아래 작은
  진입 chevron(`icon-chevron-right-line`, `text-tertiary`, 16px). 금액과 chevron은 우측 끝선 정렬.
- 카드 전체가 탭 타깃(최소 높이 72px). 좌/우 컬럼은 좌우 양끝 정렬(space-between), 카드 pad `spacing-400`.
- (옵션) Tag — 카드 우상단 또는 모델명 우측에 `Tag soft/neutral small capsule` 「단기」/「쏘카플랜」.
  기본안에서는 **생략**해 금액·모델에 집중(정보 과밀 방지). 빌드 시 한 카드에만 「쏘카플랜」 데모 가능.

---

## Frame 2 — 이용 내역 리스트 빈 상태
프레임명: `[auto] 이용 내역 & 영수증 — 20260620-101713-usage-history-receipt · 빈 상태`
배치: x = 11400 + 360 + 80 = **11840**, y=0, w=360.

### Layout (top → bottom)
| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 1 | Top app bar | TopAppBar (general 타이틀) | bg `white` / `heading2` `text-strong` / 높이 56 · pad `spacing-400` | "이용 내역" |
| 2 | 상단 여백 | spacer (custom) | `spacing-1000`×~1.5 (콘텐츠 수직 중앙 정렬) | — |
| 3 | 빈 상태 아이콘 | Empty state (custom) — 아이콘 원형 배지 | 배경 원 `gray-100` `radius-circle` 80×80 · 아이콘 `icon-file-text-line` 36px `text-tertiary` / 아래 `spacing-400` | — (문서/영수증 아이콘) |
| 4 | 빈 상태 타이틀 | Empty state (custom) | `title1`(18/SemiBold) `text-strong` 중앙정렬 / 아래 `spacing-150` | "아직 이용 내역이 없어요" |
| 5 | 빈 상태 설명 | Empty state (custom) | `body3`(14) `text-secondary` 중앙정렬 · `break-keep` / 아래 `spacing-500` · 좌우 `spacing-700` | "첫 쏘카를 이용하면 여기에서 영수증을 확인할 수 있어요." |
| 6 | 1차 행동 버튼 | ActionButton (fill/primary/large) | `title2` 라벨 · py `spacing-400` · radius `radius-350` · 폭은 콘텐츠+여유(또는 좌우 `spacing-400` 풀폭) | "차량 둘러보기" |
| 7 | 하단 여백 | spacer (custom) | `spacing-1000`×~1.5 | — |

**구성 의도:** 빈 상태는 화면 수직 중앙에 아이콘→타이틀→설명→버튼을 한 덩어리로 묶어 시선을 모은다.
유일한 강조는 「차량 둘러보기」(fill/primary). 빨강/경고색은 쓰지 않는다(에러가 아니라 정상 빈 상태).

---

## Frame 3 — 영수증 상세
프레임명: `[auto] 이용 내역 & 영수증 — 20260620-101713-usage-history-receipt · 영수증 상세`
배치: x = 11840 + 360 + 80 = **12280**, y=0, w=360. 높이 가변(≈920+, 하단 CTA 고정).

### Layout (top → bottom)
| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 1 | Top app bar | TopAppBar (BasicBackButton + general 타이틀) | bg `white` / 뒤로 `icon-arrow-left-line` `text-strong` · 타이틀 `heading2` `text-strong` / 높이 56 · pad `spacing-400` | back + "영수증" |
| 2 | 이용 요약 Card | 이용 요약 Card (custom) — white `radius-300` | 카드 pad `spacing-400` · 라벨/값 row 간 `spacing-300` / 타이틀 `title2 text-strong` · 라벨 `body3 text-secondary` · 값 `title3 text-primary`(우측) / 카드 위 `spacing-400` 좌우 `spacing-400` | 타이틀 "이용 요약" · 차량 "아반떼 CN7" · 쏘카존 "강남역 1번출구 쏘카존" · 이용 일시 "6월 14일(토) 14:00 – 18:30" · 주행 거리 "62 km" |
| 3 | 결제 영수증 Card | 결제 요약 Card (custom) — white `radius-300` | 카드 pad `spacing-400` · 카드 위 `spacing-300` / 타이틀 `title2 text-strong` 아래 `spacing-300` | 타이틀 "결제 영수증" |
| 3a | └ 대여 요금 행(아코디언) | Accordion `single` · Item(value="rental") · 기본 펼침 | Trigger: Label `body3 text-secondary` + 금액 `title3 text-strong`(우측) + chevron `icon-chevron-down-line` `text-tertiary` (data-open 회전) / Content rows `body3` 라벨 `text-secondary`·값 `text-primary` 우측 · Content 들여쓰기 `spacing-300` | Trigger "대여 요금 · 33,000원" / Content: "기본 요금(4시간 30분) 30,000원" · "심야 할증 3,000원" |
| 3b | └ 주행 요금 행(아코디언) | Accordion Item(value="driving") · 기본 접힘 | 위 Trigger 패턴 동일 | "주행 요금 · 9,300원" / Content: "62km × 150원/km 9,300원" |
| 3c | └ 보험 요금 행(아코디언) | Accordion Item(value="insurance") · 기본 접힘 | 위 Trigger 패턴 동일 | "차량손해면책 · 5,500원" / Content: "일반 면책 상품 5,500원" |
| 3d | └ 할인 행(아코디언) | Accordion Item(value="discount") · 기본 접힘 | Trigger 금액 `title3` `status-positive-regular`(음수, `−`) · Content `body3` | "할인 · −5,000원" / Content: "쏘카 쿠폰(주중 10%) −3,000원" · "포인트 사용 −2,000원" |
| 3e | └ 구분선 | Divider [stroke=divider-regular] 1px | 위아래 여백 `spacing-300` | — |
| 3f | └ 총 결제 금액 행(강조) | 합계 row (custom) | 라벨 `title2 text-strong` + 값 **`heading3`(22/Bold) `text-strong`** 우측 정렬 | "총 결제 금액" · "42,800원" |
| 4 | 결제 정보 Card | 결제수단/승인 블록 (custom) — white `radius-300` | 카드 pad `spacing-400` · 위 `spacing-300` / 라벨 `body4 text-secondary` · 값 `body3 text-primary`(우측) · row 간 `spacing-300` | 타이틀 "결제 정보"(`title2 text-strong`) · 결제수단 "신한카드 (1234)" + `icon-credit-card-line` · 승인 일시 "2026.06.14 18:31" · 승인번호 "30024815" |
| 5 | 보조 액션 — 문의 | TextButton (text/tertiary, medium, underline) | `title3` `text-secondary`(또는 `primary-regular`) · 중앙정렬 / 위 `spacing-400` 아래 `spacing-300` | "영수증이 이상한가요? 문의하기" |
| 6 | 하단 CTA region(고정) | ActionButton (outlined/secondary, large) | bg `white` · 상단 `divider-regular` 1px · pad `spacing-400` / 라벨 `title2` · 보더 `border-regular` · radius `radius-350` · 풀폭 | "같은 차 다시 예약" |

**아코디언 동작:** `single` 모드. 데모에서는 **「대여 요금」만 펼친 상태**로 구조를 드러내고 나머지(주행/보험/할인)는
접힘. Trigger 우측 chevron은 펼침 시 `data-open`으로 위로 회전. 각 Trigger는 항목명(`body3 text-secondary`) +
항목 금액(`title3 text-strong`, 우측) + chevron. 금액은 항상 우측 끝선 정렬해 스캔 가능하게 한다.

**카드 배치 의도:** 이용 요약 → 결제 영수증 → 결제 정보 순으로 "무엇을/얼마에/어떻게 결제했나"를 위에서
아래로 읽히게 한다. 총 결제 금액(heading3)이 시각적 정점이고, 그 외 항목 금액은 `title3`로 한 단계 낮춘다.

---

## Copywriting (verbatim)
모든 금액은 1,000단위 콤마 + 「원」, 할인은 앞에 `−`(U+2212 마이너스).

**공통 / 리스트**
- TopAppBar 타이틀 (heading2): "이용 내역"
- 안내 캡션 (body3): "최근 6개월 이용 내역이에요."
- 월 섹션 헤더 (title3): "2026년 6월" · "2026년 5월"
- 카드 ① 모델 (title2): "아반떼 CN7" / 일시 (body3): "6월 14일(토) 14:00–18:30" / 존 (body3): "강남역 1번출구 쏘카존" / 금액 (title2): "42,800원"
- 카드 ② (title2/body3): "캐스퍼" / "6월 7일(일) 09:00–13:00" / "마포 합정역 쏘카존" / "28,500원"
- 카드 ③: "더 뉴 그랜저" / "5월 24일(토) 10:00–22:00" / "수서역 쏘카존" / "98,000원"
- 카드 ④: "레이" / "5월 9일(금) 19:00–23:00" / "강남 신논현역 쏘카존" / "31,200원"

**빈 상태**
- 타이틀 (title1): "아직 이용 내역이 없어요"
- 설명 (body3, break-keep): "첫 쏘카를 이용하면 여기에서 영수증을 확인할 수 있어요."
- 버튼 (title2 라벨): "차량 둘러보기"

**영수증 상세**
- TopAppBar 타이틀 (heading2): "영수증"
- 이용 요약 — 타이틀 (title2): "이용 요약"
  - 라벨/값 (body3 / title3): "차량" → "아반떼 CN7" · "쏘카존" → "강남역 1번출구 쏘카존" · "이용 일시" → "6월 14일(토) 14:00 – 18:30" · "주행 거리" → "62 km"
- 결제 영수증 — 타이틀 (title2): "결제 영수증"
  - 대여 Trigger: "대여 요금" / 금액 "33,000원" · Content: "기본 요금 (4시간 30분)" → "30,000원" · "심야 할증" → "3,000원"
  - 주행 Trigger: "주행 요금" / 금액 "9,300원" · Content: "62km × 150원/km" → "9,300원"
  - 보험 Trigger: "차량손해면책" / 금액 "5,500원" · Content: "일반 면책 상품" → "5,500원"
  - 할인 Trigger: "할인" / 금액 "−5,000원" · Content: "쏘카 쿠폰 (주중 10%)" → "−3,000원" · "포인트 사용" → "−2,000원"
  - 합계 라벨 (title2): "총 결제 금액" / 값 (heading3): "42,800원"
- 결제 정보 — 타이틀 (title2): "결제 정보"
  - "결제수단" → "신한카드 (1234)" · "승인 일시" → "2026.06.14 18:31" · "승인번호" → "30024815"
- 문의 TextButton: "영수증이 이상한가요? 문의하기"
- 하단 CTA (title2 라벨): "같은 차 다시 예약"

> 검산: 33,000 + 9,300 + 5,500 − 5,000 = **42,800원** (총 결제 금액과 일치). 빌드 시 이 합을 깨지 말 것.

## Color & emphasis
- **Background:** `background-regular`(#F2F3F8). 모든 카드/시트/TopAppBar 표면 `white`.
- **Primary CTA:** 빈 상태만 `ActionButton fill/primary`(=`primary-regular`). 상세의 하단 CTA는 의도적으로
  `outlined/secondary`(중립 보더 `border-regular`, 텍스트 `text-strong`) — 요청의 보조 위계를 지키고, 화면의
  진짜 강조는 **총 결제 금액**에 두기 위함.
- **텍스트 위계:** 금액·합계·모델명·카드 타이틀 `text-strong` > 값/본문 `text-primary` > 라벨·메타·캡션
  `text-secondary` > 진입 chevron·플레이스홀더 `text-tertiary`.
- **숫자 강조(핵심):** 총 결제 금액 `heading3`(22/Bold) `text-strong` — 화면 단일 정점. 항목 금액·요약 값
  `title3`(SemiBold) `text-strong`. 리스트 카드 금액 `title2`(SemiBold) `text-strong`, 우측 끝선 정렬.
- **할인 강조:** 음수 금액은 `status-positive-regular`(#04CA81, "할인=혜택" 긍정 신호) + `−` 부호. **빨강
  (`status-negative`)은 환불/실패 전용이므로 할인에 쓰지 않는다.**
- **구분선:** 합계 위 `divider-regular`(1px). 카드 간 분리는 `background-regular` 갭(`spacing-300`)으로 처리.
- **de-emphasis:** 「영수증 문의」 TextButton(`text-secondary`/tertiary, 중앙)로 가장 낮은 위계. 리스트의
  진입 chevron은 `text-tertiary`로 은은하게 — 카드 자체가 탭 타깃임을 보조만 한다.

## States
- **기본 (Frame 1):** 2개월·4건의 월별 그룹 리스트. 카드 탭 → 영수증 상세 진입. 정상 결제 완료 데이터.
- **빈 상태 (Frame 2):** 내역 0건. 아이콘 + "아직 이용 내역이 없어요" + 설명 + 「차량 둘러보기」. 정상
  빈 상태이므로 에러색/경고 없음.
- **영수증 상세 (Frame 3, 정상 결제 완료):** 이용 요약 + 항목별 결제 영수증(대여 펼침/나머지 접힘) +
  총 결제 금액 강조 + 결제 정보 + 보조 액션. 부분 환불/결제 실패/정산 중 등 변형 상태는 범위 밖(제외).
- (로딩/에러 상태는 이번 요청 범위 밖 — Skeleton/에러 화면은 만들지 않는다.)

## Accessibility
- **최소 터치 타깃 44×44pt 이상:** 리스트 카드 전체(높이 ≥72px) 탭 타깃, 진입 chevron은 시각 표시일 뿐
  카드가 타깃. 아코디언 Trigger 전체가 탭 타깃(높이 ≥48px). BasicBackButton·아이콘 버튼 44pt 보장.
- **숫자 가독성(최우선):** 금액은 굵기·크기 위계 + 우측 끝선 정렬 + 1,000단위 콤마 + 「원」으로 한눈에
  스캔되게. 총 결제 금액은 heading3로 분리 강조. 폰트는 Pretendard 전체 weight(SemiBold 600·Bold 700
  유지, Medium으로 강등 금지) — 600/700/400 대비가 위계를 만든다.
- **대비:** 본문/금액 `text-strong`(#141A24) on white — 충분한 대비. 메타는 `text-secondary`(#697383)로
  4.5:1 이상. 할인 녹색(`status-positive-regular`)은 색만으로 의미를 전달하지 않도록 `−` 부호를 병기.
- **아이콘 only 인터랙티브 aria-label:** BasicBackButton `[aria-label=뒤로가기]`, 카드 chevron은 장식
  (`aria-hidden`, 카드에 접근 이름). 아코디언 chevron 장식 처리.
- **줄바꿈:** 빈 상태 설명·캡션은 `break-keep`으로 단어 중간 분리 방지. 일시 문자열은 한 줄 유지(미들닷/
  하이픈 앞뒤 공백으로 자연 분리).

## Out of scope
- 실제 결제·환불·정정 처리, 영수증 PDF/이메일 발송 화면.
- 「영수증 문의」 진입 후 CS/상담 화면, 「같은 차 다시 예약」 진입 후 예약 플로우.
- 필터·검색·기간 선택 등 부가 탐색 기능.
- 로딩(Skeleton)·에러 화면, 부분 환불/결제 실패/정산 중 등 영수증 변형 상태.
