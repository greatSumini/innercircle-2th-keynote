---
run: 20260620-101717-license-register
stage: clarify
status: READY
---
# Clarify

## Understood request
첫 예약 전 온보딩 단계의 **운전면허 등록·인증 화면**(모바일 포트레이트, 풀스크린)을 디자인합니다.
주 사용자는 첫 예약을 앞둔 신규 쏘카 회원이고, 단일 핵심 과업(Primary job)은 *운전면허 정보를
입력·촬영·동의한 뒤 등록·인증을 완료하는 것*입니다. 화면은 위에서부터 타이틀+설명 → 입력 폼 →
면허증 촬영(+Tips) → 동의 → 하단 고정 CTA('등록하기') 순서의 가이드형 단일 폼이며, **2개 필수
상태(① 입력 기본, ② 인증 완료)와 1개 선택 상태(③ 검증 중 로딩)**를 좌→우로 나란히 보여줍니다.

## Scope
- In:
  - TopAppBar(뒤로가기/닫기) + 타이틀 "운전면허를 등록해 주세요" + 한 줄 설명.
  - 입력 폼: 면허 종류(선택), 면허번호(Input), 발급일자(DatePicker 진입), 이름(Input), 생년월일(Input).
  - 면허증 촬영: 카메라 촬영 / 업로드 영역 + 촬영 안내 Tips.
  - 동의: 본인확인 / 약관 체크(Checkbox).
  - 하단 고정 영역: '등록하기' (ActionButton fill/primary, large).
  - 상태 프레임: ① 입력 기본, ② 인증 완료, ③ 검증 중 로딩(선택, 포함).
- Out:
  - 실제 카메라/OCR 캡처 화면, 권한 요청 OS 다이얼로그.
  - 약관 전문 상세 화면, 본인확인(PASS/통신사) 외부 인증 플로우.
  - 이후 단계(결제수단 등록, 첫 예약 흐름)와 마이페이지 진입 경로.
  - 입력 검증 실패/네트워크 에러 상태(요청에 미포함 — 필요 시 plan에서 별도 검토).

## Assumptions (sensible SOCAR / socarframe defaults)
- **풀스크린 단일 폼 + 하단 고정 CTA** — 온보딩 가이드형 흐름이므로 BottomSheet/모달이 아닌 스크롤 가능한 풀스크린으로 둠. 신뢰감·완결성(요청 톤)에 맞음.
- **상단 TopAppBar에 BasicBackButton** — 온보딩 단계 화면이므로 뒤로가기 제공이 일관적 패턴.
- **면허 종류는 선택형 UI** — 옵션 수가 적고 단일 선택이므로 Radio/SegmentedControl 또는 선택 트리거(BottomSheet 진입) 중 plan에서 결정; 기본은 선택값 트리거 Input로 가정.
- **발급일자·생년월일은 DatePicker / 날짜 포맷 Input** — socarframe DatePicker 및 `inputFormatters.date`(YYYY. MM. DD) 사용. 직접 캘린더 그리드는 별도 surface로 진입.
- **면허번호 Input** — 지역별 포맷 차이가 있어 자동 포맷터 없이 일반 Input + helperText 안내로 가정.
- **촬영 영역 안내는 Tips(AccentTip/InfoTip)** — "촬영 Tips"는 socarframe Tips 컴포넌트로 표현(밝기/반사/네 모서리 안내).
- **동의는 Checkbox 2개(본인확인/약관)** — 다중 선택이므로 Checkbox. '약관'에는 보기(>) 링크 행 동반으로 가정.
- **인증 완료 상태(②)** — 입력 필드는 채워진(읽기 전용/확인) 형태 + 완료 배지/성공 피드백, CTA는 '확인' 또는 다음 단계 진행 형태로 가정.
- **검증 중 로딩(③)** — CTA를 ActionButton loading 상태로, 폼은 Skeleton 또는 진행 안내(TopAppBar LoadingBar/dim)로 표현하는 방향으로 가정.
- **토큰·컴포넌트는 socarframe 시맨틱 토큰 사용**, 카피는 한국어 SOCAR 보이스, Pretendard, 모바일 포트레이트(가정 너비 360–375).
- **캔버스 배치** — 이 세션 전용 레인 x=13200, y=0부터 좌→우로 상태 프레임 나열(요청 명시), `[auto] 운전면허 등록 — <run-id> · <state>` 네이밍.

STATUS: READY
