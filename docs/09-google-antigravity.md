# Google Antigravity 설치 가이드

[메인 안내로 돌아가기](../README.md)

## 이 문서는 언제 보면 되나요?

- 행사 중 코드를 직접 열어보고 수정할 가능성이 있을 때
- 기존 VS Code 대신 Google Antigravity를 써 보고 싶을 때
- agent-first 개발 환경을 미리 설치해 보고 싶을 때

Ollama와 Gemma 4 실행 자체에는 Antigravity가 필수는 아닙니다. 코드 편집기가 이미 준비되어 있다면 기존 편집기를 사용해도 됩니다.

## Google Antigravity란 무엇인가요?

Google Antigravity는 Google의 agent-first 개발 환경입니다. Google Codelab은 Antigravity를 IDE를 에이전트 중심 시대로 확장하는 개발 플랫폼으로 설명합니다. 일반 코드 편집기처럼 파일을 열고 수정할 수 있고, Agent Manager, Editor, Browser 같은 기능을 통해 에이전트 기반 작업 흐름을 지원합니다.

현재 Codelab 기준으로 Antigravity는 preview로 제공되며, 개인 Gmail 계정으로 시작하는 흐름을 안내합니다. 회사/학교 계정이나 관리형 장비에서는 로그인 또는 설치 정책 때문에 막힐 수 있으니 행사 전에 반드시 한 번 실행해 보세요.

## 공통 준비

1. 공식 다운로드 페이지로 이동합니다.

```text
https://antigravity.google/download
```

2. 본인 운영체제에 맞는 설치 파일을 다운로드합니다.
3. 설치 후 앱을 실행합니다.
4. 첫 실행 설정을 완료합니다.
5. 개인 Gmail 계정으로 로그인할 수 있는지 확인합니다.
6. 행사 자료 폴더를 열 수 있는지 확인합니다.

## Windows 설치

1. https://antigravity.google/download 로 이동합니다.
2. Windows용 설치 파일을 다운로드합니다.
3. 다운로드한 설치 프로그램을 실행합니다.
4. 설치가 끝나면 Antigravity를 실행합니다.
5. 첫 실행 화면에서 설정을 진행합니다.
6. 개인 Gmail 계정으로 로그인합니다.
7. 행사 자료 폴더를 열어 봅니다.

회사/학교 장비에서는 설치 프로그램 실행이나 로그인 단계가 보안 정책으로 막힐 수 있습니다. 이 경우 행사 전에 관리자 권한 또는 다른 개인 장비를 확인해 주세요.

## macOS Apple Silicon 설치

1. https://antigravity.google/download 로 이동합니다.
2. Apple Silicon Mac에 맞는 macOS 설치 파일을 다운로드합니다.
3. 다운로드한 DMG 파일을 엽니다.
4. Antigravity 앱을 `Applications` 폴더로 옮깁니다.
5. `Applications` 폴더에서 Antigravity를 실행합니다.
6. macOS 보안 확인 창이 나오면 신뢰할 수 있는 공식 다운로드인지 확인한 뒤 열기를 진행합니다.
7. 개인 Gmail 계정으로 로그인합니다.
8. 행사 자료 폴더를 열어 봅니다.

## macOS Intel Mac 설치

1. https://antigravity.google/download 로 이동합니다.
2. Intel Mac에 맞는 macOS 설치 파일을 다운로드합니다.
3. 다운로드한 DMG 파일을 엽니다.
4. Antigravity 앱을 `Applications` 폴더로 옮깁니다.
5. `Applications` 폴더에서 Antigravity를 실행합니다.
6. 개인 Gmail 계정으로 로그인합니다.
7. 행사 자료 폴더를 열어 봅니다.

Intel Mac에서는 Ollama/Gemma 4 실행이 CPU 전용이라 느릴 수 있지만, Antigravity 같은 코드 편집기 실행 자체는 별도 문제입니다. 다만 메모리가 8GB라면 Ollama 실행과 편집기를 동시에 켰을 때 전체 시스템이 느려질 수 있습니다.

## 첫 실행 설정

첫 실행에서는 다음 항목이 나올 수 있습니다.

- 기존 VS Code 또는 Cursor 설정 가져오기
- 새 설정으로 시작하기
- 편집기 테마 선택
- Agent 사용 방식 설정
- 확장 프로그램 설치 여부 선택

처음 준비하는 경우에는 새 설정으로 시작해도 됩니다. 이미 VS Code 설정을 많이 쓰고 있다면 가져오기를 선택해도 됩니다.

## 행사 전 확인

- Antigravity 앱 실행 성공
- 개인 Gmail 계정 로그인 성공
- 첫 실행 설정 완료
- 행사 자료 폴더 열기 성공
- 터미널 패널 열기 가능 여부 확인

Antigravity 설치나 로그인이 어렵다면 기존 VS Code 같은 코드 편집기를 준비해도 됩니다. 이 문서의 핵심 준비는 Ollama 설치, Gemma 4 모델 다운로드, API 테스트입니다.

## 공식 참고 링크

- Google Antigravity 다운로드: https://antigravity.google/download
- Google Antigravity Codelab: https://codelabs.developers.google.com/getting-started-google-antigravity
