---
run: 20260620-101717-license-register
stage: plan
status: ready
frame: 360 x 900 mobile portrait (3 state frames)
canvas_origin: { x: 13200, y: 0 }   # session lane; lay state frames left→right, 80px gutter
---
# Design plan — 운전면허 등록

## Overview
- Goal / primary job: 첫 예약 전 온보딩 단계에서 사용자가 **운전면허 정보를 입력·촬영·동의한 뒤 등록·인증을 완료**하게 한다. 막힘 없이 끝까지 안내되는 단일 가이드형 폼.
- Primary action (emphasized): 하단 고정 **'등록하기'** (`ActionButton · fill/primary/large`). 화면에 강조되는 액션은 이 하나뿐.
- Surface: **full screen** (스크롤 가능한 풀스크린 + 하단 고정 CTA 영역). BottomSheet/모달 아님 — 온보딩 신뢰감·완결성에 맞춤.

## Frame
- Size: **360 x 900** (SOCAR 모바일 베이스라인 360 wide; 본문이 길어 높이는 800보다 크게 잡되, CTA는 고정 영역으로 항상 보임). 기존 `반납 완료` 프레임(360 x 857)과 같은 폭·구조 계열.
- 3 state frames, all 360 x 900, in the session lane:
  - `[auto] 운전면허 등록 · 기본 — 20260620-101717-license-register` at **x=13200, y=0**
  - `[auto] 운전면허 등록 · 인증 완료 — 20260620-101717-license-register` at **x=13640, y=0** (13200 + 360 + 80 gutter)
  - `[auto] 운전면허 등록 · 검증 중 — 20260620-101717-license-register` at **x=14080, y=0** (13640 + 360 + 80 gutter)
  - Wrap all three in a Figma **Section** `[auto] 운전면허 등록 — 20260620-101717-license-register` (frame stem, no state segment). If Section creation fails, fall back to the row layout above (don't block).
- Safe areas / TopAppBar / bottom action area:
  - **Status bar**: 상단 44px 여백(시스템 영역, 비워둠 — 컨텐츠는 TopAppBar부터).
  - **TopAppBar**: 56px 고정, screen top에 위치. 좌측 back IconButton.
  - **Scroll body**: TopAppBar 아래 ~ Bottom CTA 위까지. 좌우 패딩 `spacing-400` (16px).
  - **Bottom CTA region**: 화면 하단 고정. 흰색 배경, 상단 `Divider [stroke=divider-regular]`, 내부 패딩 상하 `spacing-300`(12px)·좌우 `spacing-400`(16px), 56px 버튼. (기존 `반납 완료` 하단 영역과 동일 규격.)

## Layout (top → bottom)

각 행은 implement가 위→아래 순서 그대로 쌓는 단일 소스. 모든 surface 카드는 white 배경 + `radius-300`(12px), 좌우 `spacing-400` 내부 패딩, 카드 간 세로 간격 `spacing-300`(12px). 섹션 그룹(필드 그룹 vs 촬영 vs 동의) 사이는 `spacing-400`(16px).

| Order | Section | socarframe component (variant/size) | Tokens (color / type / spacing) | Content |
|-------|---------|-------------------------------------|---------------------------------|---------|
| 1 | TopAppBar | TopAppBar (general) + LeftSideIconSlot(IconButton medium, `icon-chevron-left-line`) | bg white / IconButton icon `text-strong` / height 56, pad 좌우 `spacing-400` | 좌측 뒤로가기. 타이틀 비움(타이틀은 본문 Hero에 큼직하게) |
| 2 | Hero 타이틀 영역 | (custom) 텍스트 스택 | title `heading2`/`text-strong`, desc `body2`/`text-secondary` / 상단 `spacing-300`, title→desc `spacing-150`, 좌우 `spacing-400` | 타이틀 "운전면허를 등록해 주세요" + 한 줄 설명 (Copywriting 참조) |
| 3 | 진행 안내 Tips | Tips · InfoTip (information, inline) | bg `status-information-weak` / icon·text `status-information-regular`·`text-primary` / `body3`·`caption2` / radius-300, pad `spacing-300`, 상단 `spacing-400` | `icon-info-circle-line` + "등록 후 약 1~2분 내 인증이 완료돼요. 정보는 안전하게 보호됩니다." |
| 4 | 면허 정보 Card (custom 그룹) | (custom) white card, 내부 필드 스택 | card white / radius-300 / 내부 패딩 `spacing-400`, 필드 간 `spacing-300` | 섹션 제목 "면허 정보" `title3`/`text-strong` + 아래 4개 필드(5~8) |
| 5 | · 면허 종류 (필드) | SelectionBox(트리거 Input) — Input · filled + trailing `icon-chevron-down-line` | label `title4`/`text-strong`, value `body2`/`text-tertiary`(placeholder)·`text-primary`(값), helper `caption2`/`text-secondary` / radius-300, label→input `spacing-150` | label "면허 종류", placeholder "면허 종류를 선택하세요", helper "1종 보통 / 2종 보통 등" (BottomSheet 진입 트리거) |
| 6 | · 면허번호 (필드) | Input · filled, clearable | label `title4`/`text-strong`, value `body2`/`text-primary`, helper `caption2`/`text-secondary` / radius-300 | label "면허번호", placeholder "면허번호를 입력하세요", helper "면허증 앞면에 적힌 번호를 입력해 주세요" |
| 7 | · 발급일자 (필드) | Input · filled (trigger) + trailing `icon-calendar-check-line`, `inputFormatters.date` | label `title4`/`text-strong`, value `body2`/`text-tertiary` placeholder / radius-300 | label "발급일자", placeholder "YYYY. MM. DD" (DatePicker 진입 트리거) |
| 8 | · 이름 / 생년월일 (2필드 행) | Input · filled (이름) + Input · filled (trigger, `icon-calendar-check-line`) | 2-up, 가로 gap `spacing-200`; label `title4`, value `body2`/`text-primary` / radius-300 | 이름 placeholder "홍길동", 생년월일 placeholder "YYYY. MM. DD" |
| 9 | 면허증 촬영 Card (custom) | (custom) 업로드/촬영 영역 | 카드 white / radius-300 / 점선 프레임 `border-regular`, 중앙 정렬, 내부 패딩 `spacing-500`(20px) | 섹션 제목 "운전면허증 촬영" `title3`/`text-strong`; 점선 박스 안 `icon-driver-license-line`(40, `text-tertiary`) + 안내문 `body3`/`text-secondary` + 트리거 버튼 |
| 10 | · 촬영/업로드 트리거 | ActionButton · fill/secondary/medium (`icon-camera-line` leftIcon) | bg `status-information-weak`/blue-100, label `text-primary`·`title3` / radius-300 | "촬영하기" (보조 액션 — primary 아님). 우측에 TextButton "앨범에서 선택" |
| 11 | · 촬영 안내 Tips | Tips · InfoTip (information) | bg `status-information-weak` / icon `status-information-regular` / `caption2`/`text-secondary` / radius-300, 상단 `spacing-300` | `icon-info-circle-line` + 3줄 가이드 (밝기/반사/네 모서리) — Copywriting 참조 |
| 12 | 동의 Card (custom) | (custom) white card, CheckboxGroup | card white / radius-300 / 항목 간 `spacing-300`, 내부 패딩 `spacing-400` | 섹션 제목 "약관 동의" `title3`/`text-strong` + 체크 행 2개(13~14) |
| 13 | · 본인확인 동의 행 | Checkbox · default (label) | label `body3`/`text-primary`, '필수' 태그 `caption1`/`status-information-regular` / 체크 박스 `border-regular`→checked `primary-regular` | "[필수] 본인확인 및 면허 진위 조회에 동의합니다" |
| 14 | · 약관 동의 행 | Checkbox · default + TextButton(rightIcon `icon-chevron-right-line`) | label `body3`/`text-primary`, '보기' TextButton tertiary `caption1`/`text-secondary` | "[필수] 운전면허 등록 약관에 동의합니다" + 우측 "보기 >" |
| 15 | Bottom CTA region | (custom 고정 영역) ActionButton · fill/primary/large | 영역 bg white, 상단 `Divider [stroke=divider-regular]`; 버튼 bg `primary-regular`, label `white`·`title2` / radius-350, 영역 패딩 상하 `spacing-300`·좌우 `spacing-400`, 버튼 h 56 | "등록하기" (기본 상태에선 미입력 시 `disabled` 안내 가능 — States 참조) |

> 면허 정보 Card(4)와 그 안의 필드(5~8)는 한 흰색 카드 안에 묶고, 촬영 Card(9)·동의 Card(12)는 각각 별도 흰색 카드. 화면 배경은 `background-regular`(#F2F3F8)라 카드 경계가 자연스럽게 드러난다.

## Copywriting (verbatim)

화면이 노출하는 모든 텍스트 문자열, 역할과 타입 토큰 포함. (줄바꿈은 `break-keep` 기준 — 단어 중간에서 끊기지 않게.)

- Hero title (`heading2`): **"운전면허를 등록해 주세요"**
- Hero description (`body2`): **"첫 예약 전, 운전면허를 등록하고 인증을 완료해 주세요."**
- 진행 안내 Tips (`body3` 본문 + `caption2` 보조): **"등록 후 약 1~2분 내 인증이 완료돼요. 입력하신 정보는 안전하게 보호됩니다."**
- 섹션 제목 — 면허 정보 (`title3`): **"면허 정보"**
- 필드 라벨 (`title4`):
  - **"면허 종류"** / placeholder (`body2`, `text-tertiary`): **"면허 종류를 선택하세요"** / helper (`caption2`): **"1종 보통, 2종 보통 등에서 선택해 주세요"**
  - **"면허번호"** / placeholder: **"면허번호를 입력하세요"** / helper: **"면허증 앞면에 적힌 번호를 입력해 주세요"**
  - **"발급일자"** / placeholder: **"YYYY. MM. DD"**
  - **"이름"** / placeholder: **"홍길동"**
  - **"생년월일"** / placeholder: **"YYYY. MM. DD"**
- 섹션 제목 — 촬영 (`title3`): **"운전면허증 촬영"**
- 촬영 영역 안내문 (`body3`, `text-secondary`): **"운전면허증 앞면을 촬영하거나 사진을 올려 주세요"**
- 촬영 트리거 버튼 (`title3`): **"촬영하기"** / 보조 TextButton (`caption1`): **"앨범에서 선택"**
- 촬영 안내 Tips 제목 (`caption1`, `status-information-strong`): **"선명하게 찍는 법"**
- 촬영 안내 Tips 항목 (`caption2`, `text-secondary`), 3줄:
  - **"밝은 곳에서 촬영해 주세요"**
  - **"빛 반사 없이 글씨가 잘 보이게 해 주세요"**
  - **"면허증 네 모서리가 모두 보이게 담아 주세요"**
- 섹션 제목 — 동의 (`title3`): **"약관 동의"**
- 본인확인 동의 (`body3`): **"[필수] 본인확인 및 면허 진위 조회에 동의합니다"**
- 약관 동의 (`body3`): **"[필수] 운전면허 등록 약관에 동의합니다"** / 보기 링크 (`caption1`): **"보기"**
- Primary CTA (`title2`): **"등록하기"**

### 상태별 추가 카피
- ② 인증 완료 — 완료 Hero 배지 (`caption1`, `status-positive-strong`): **"인증 완료"**
  - 완료 Hero 제목 (`heading2`): **"운전면허 인증이 완료됐어요"**
  - 완료 Hero 설명 (`body2`, `text-secondary`): **"이제 첫 예약을 시작할 수 있어요."**
  - 완료 카드 요약 라벨/값(`body3`/`title4`): 이름 "홍길동" · 면허 종류 "1종 보통" · 면허번호 "11-12-345678-90" · 발급일자 "2021. 03. 16" (값은 `text-strong`, 라벨 `text-secondary`)
  - ② CTA (`title2`): **"첫 예약 시작하기"**
- ③ 검증 중 — TopAppBar 하단 LoadingBar; CTA loading 상태(라벨 숨김, Lottie); 본문 상단 안내 (`body3`, `text-secondary`): **"운전면허를 확인하고 있어요. 잠시만 기다려 주세요."**

## Color & emphasis
- Background: `background-regular` (#F2F3F8). 카드/필드/촬영영역/하단 CTA 영역: `white`.
- Primary CTA: `primary-regular` (#0078FF) fill + `white` label. 화면에서 가장 강한 색·면적은 이 버튼 하나.
- Text hierarchy: 타이틀 `text-strong` > 섹션 제목·입력값 `text-strong`/`text-primary` > 라벨·동의문 `text-primary` > helper·보조·placeholder `text-secondary`/`text-tertiary`. ② 읽기 전용 필드는 `text-disabled` 톤이 아닌 채워진 값(`text-strong`)으로 신뢰감 유지.
- 강조 / 비강조:
  - **강조**: 하단 '등록하기' (유일한 primary). Hero 타이틀(heading2/text-strong)로 화면 목적을 3초 내 인지.
  - **정보형(중립 강조)**: 진행 안내·촬영 안내 Tips는 `status-information-weak` 배경의 차분한 파랑 — 행동을 막지 않는 보조 안내.
  - **의도적 비강조**: 촬영 '촬영하기'는 `fill/secondary`(연한 블루), '앨범에서 선택'·'보기'는 TextButton — primary와 경쟁하지 않게 한 단계 낮춤. 면허 종류 트리거의 chevron, helper 텍스트도 `text-secondary`/`text-tertiary`로 가라앉힘.
  - ② 성공: `status-positive-weak`(#E6FEF0) 배경 + `icon-check-circle-fill`·`status-positive-regular`(#04CA81) — 완료감만 전달, CTA는 다음 단계(첫 예약)로 자연 전환.
- Error/negative 색은 이 화면 범위 밖(클라리파이 out). `status-negative-*`는 예약만 하고 사용하지 않음.

## States
빌드 대상 3개 프레임. 상태 단어는 figma-conventions 어휘(`기본`, `성공`, `로딩`)에서 프레임명에 매핑: 기본=`기본`, 인증 완료=프레임명 `인증 완료`(성공 계열), 검증 중=`검증 중`(로딩 계열).

- **① 기본 (입력 기본)** — 프레임 `· 기본`. Layout 표 1~15 전체. 모든 입력 필드는 빈/placeholder 상태, 체크박스 미선택. 하단 '등록하기'는 **disabled(연한)** 상태로 두고, 충족되면 활성화됨을 암시(클릭 영역은 존재). 화면 목적·다음 행동이 한눈에 예측 가능해야 함(principles: Predictability).
- **② 인증 완료 (성공)** — 프레임 `· 인증 완료`. 상단 Hero를 **완료 Hero**로 교체: `status-positive-weak` 배경의 둥근 패널(radius-400) + `icon-check-circle-fill`(40, `status-positive-regular`) + "인증 완료" 배지(Badge/Tag, `status-positive-weak`/`status-positive-strong`) + "운전면허 인증이 완료됐어요" + 설명. 그 아래 입력 카드는 **읽기 전용 요약 카드**(라벨–값 행, 값 `text-strong`, 우측 끝에 작은 `icon-check-circle-fill` 또는 "확인됨" 태그). 촬영/동의 영역은 접거나 "촬영 완료"·"동의 완료" 요약 행으로 축약. 하단 CTA는 `primary-regular` **"첫 예약 시작하기"**(활성). 촬영 안내 Tips는 숨김.
- **③ 검증 중 (로딩)** — 프레임 `· 검증 중`. ① 레이아웃을 베이스로: TopAppBar 하단에 **LoadingBar**(진행 표시, `primary-regular`), 본문은 dim 위에 "운전면허를 확인하고 있어요. 잠시만 기다려 주세요." 안내, 입력 카드/촬영 카드 영역은 **Skeleton**(rectangle, radius-300, wave, `white-gray50`)로 일부 치환해 처리 중임을 표현. 하단 CTA는 `ActionButton · fill/primary/large` **loading=true**(라벨 숨김 + Lottie 로더, 클릭 비활성). 중복 제출 방지(principles: Quality).

> Empty/Error 상태는 이 요청 범위 밖(clarify out). Confidence 원칙상 진행/성공/로딩 상태는 모두 커버(③ 포함)했고, 실패 복구는 후속 과제로 명시.

## Accessibility
- **터치 타깃 ≥ 44x44**: TopAppBar back IconButton, 촬영/업로드 트리거, 체크박스 행, 하단 CTA 모두 최소 44pt 높이 확보(CTA 56). 체크박스는 라벨 전체를 탭 영역으로.
- **아이콘 전용 버튼**: back IconButton에 `[aria-label=뒤로가기]`. 촬영 안내 `icon-info-circle-line`은 장식이 아니라 Tips 본문과 함께 읽히도록 텍스트 동반.
- **대비**: 본문/라벨은 `text-primary`(#354153) 이상으로 white/`background-regular` 위 4.5:1 충족. primary CTA `white` on `#0078FF` 충족. placeholder(`text-tertiary`)는 보조 정보로만 쓰고 필수 의미는 라벨/helper(`text-secondary` 이상)에 둠.
- **한 손 조작 / 야외 식별**(principles Context & Safety): 핵심 행동(등록하기)은 하단 고정 영역에 두어 엄지 도달 범위. 야외에서도 Hero 타이틀·CTA가 큰 타입(heading2/title2)·고대비로 식별됨.
- **상태 전달은 색에만 의존하지 않음**: ② 완료는 `status-positive` 색 + `icon-check-circle-fill` + "인증 완료" 텍스트 배지 병행. ③ 로딩은 색 + LoadingBar 모션 + 텍스트 안내 병행.
- **줄바꿈**: Hero 설명·Tips 문구는 `break-keep`으로 단어 중간 줄바꿈 방지. 360 폭에서 한 줄 또는 단어 균형 2줄.

## Out of scope
- 실제 카메라/OCR 캡처 화면, OS 권한 다이얼로그(촬영 트리거까지만).
- DatePicker 캘린더 그리드 surface(본 화면은 날짜 포맷 Input 트리거만; 그리드는 별도 surface).
- 면허 종류 선택 BottomSheet 내부 옵션 리스트(트리거까지만).
- 약관 전문 상세 화면, 본인확인(PASS/통신사) 외부 인증 플로우.
- 입력 검증 실패 / 네트워크 에러 상태(요청 미포함 — `status-negative-*` 토큰만 예약).
- 이후 단계(결제수단 등록, 첫 예약 흐름), 마이페이지 진입 경로.
