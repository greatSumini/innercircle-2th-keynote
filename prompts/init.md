❯ 요구사항을 입력받으면, figma mcp를 사용해서 디자인 해주는 harness를 만들고싶다.
이 harness는 orchestrate를 담당하는 'auto'라는 이름의 skill 호출을 통해 trigger되며, 내부적으로 여러 sub agent들이 중간 작업물을 남기고 전달받으며 최종 디자인을 완성한다.

생성되어야할 sub agent 종류는 다음과 같다.

1. clarify: 사용자 요구사항을 명확히 이해하고, 되물어야하는 것이 있다면 되묻는다.
2. context gather: 기존 figma 상의 디자인, 컴포넌트 등 또는 스타일가이드 중 이번 요청에서 참조되어야할 것을 list up한다.
3. plan: 어떻게 디자인되어야할지 레이아웃,카피라이팅,색상,강조방식 등을 포함한 설계문서를 작성한다.
4. implement: figma mcp를 호출해서 필요한 디자인 요소들을 생성한다.
5. verify: figma mcp를 호출해서 완성된 디자인 요소들을 확인하고, 이들이 1, 2, 3 단계에서의 결론을 잘 반영하여 고품질로 완성됐는지 점검하고, 최종 점검 결과 및 개선필요사항(있다면)을 응답한다.

clarify 결과 되물어야할 것이 있다면, 사용자에게 되물은 후 다시 clarify sub agent를 호출한다.
따라서 clarify sub agent의 시스템프롬프트는 최초 요구사항파악 시에도, 질문 답변을 제공받았을 때도 정상작동해야한다.

이 harness는 현업에서 쓸 수 있어야한다. 쏘카에서 사용함을 전제로하고, 아래 제공된 사이트의 socarframe을 기반으로 스타일가이드 및 컴포넌트들을 미리 생성해두자. 사이트 내 관련 문서들을 sub agent들로 탐색하며 빠지는 내용 없이 잘 옮겨야한다.
https://socarframe.socar.kr/development/principle

이 harness를 쓰면, 쏘카 앱의 신규 화면 디자인을 요청받았을 때 figma에 잘 디자인해줄 수 있어야한다.

이제 이 harness에 대한 구현 작업을 시작하자. 다음과 같은 순서로 멈추지말고 쭉 진행해라.

1. 이 repo의 아키텍쳐 구조 정립
2. socarframe 디자인시스템 학습
3. socarframe 관련 스타일 가이드 문서 생성 (docs/ 경로에 적절히)
4. skill 생성
5. 모든 sub agent 생성
6. CLAUDE.md 생성
7. harness 구동 테스트용 테스트셋 생성
8. harness 테스트 (같은 경로에서 claude -p 명령어를 사용해서 호출)
9. figma 디자인 결과 및 각 단계의 산출문서를 보고, harness 개선점 도출
10. harness 개선
11. 최종 브리핑
