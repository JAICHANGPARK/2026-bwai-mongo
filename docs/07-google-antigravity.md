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

## Rules, Workflows, Skills 설정

이 저장소를 Antigravity에서 열면 행사 실습용 workspace 설정을 함께 사용할 수 있습니다. 저장소 루트가 아니라 하위 폴더만 열면 `.agents/` 설정을 못 찾을 수 있으니, 가능하면 이 저장소 루트를 그대로 여세요.

```text
.agents/
├── rules/
├── workflows/
└── skills/
```

공식 문서 기준으로 Rules와 Workflows는 Agent 패널 상단의 `...` 메뉴에서 Customizations 패널을 열어 확인하거나 추가할 수 있습니다. 이 저장소의 파일이 자동으로 보이지 않으면 같은 화면에서 Workspace 항목으로 직접 추가하세요.

### Rules

Rules는 Agent가 계속 따라야 하는 제약과 코딩 스타일을 적어 두는 Markdown 파일입니다.

이번 실습에서는 다음 파일을 사용합니다.

```text
.agents/rules/rules.md
.agents/rules/session-1-common-rules.md
```

`rules.md`는 항상 적용할 workspace rule이고, `session-1-common-rules.md`는 UI에서 직접 붙여넣어야 할 때 쓰기 쉬운 사본입니다.

Antigravity 공식 문서는 workspace rules의 기본 위치를 `.agents/rules`로 안내합니다. 이전 `.agent/rules`도 호환될 수 있지만, 이 저장소에서는 새 기본값인 `.agents/rules`를 사용합니다.

모든 workspace에 적용할 개인 규칙은 global rule로 둘 수 있습니다.

```text
~/.gemini/GEMINI.md
```

Rule 활성화 방식은 다음 중 하나를 고를 수 있습니다.

- Manual: Agent 입력창에서 직접 언급했을 때만 사용
- Always On: 항상 적용
- Model Decision: 설명을 보고 모델이 적용 여부 판단
- Glob: `*.py`, `src/**/*.ts` 같은 파일 패턴에 맞을 때 적용

Rules 파일 하나는 12,000자 이내로 유지하세요. 다른 파일을 참고해야 하면 rule 파일 안에서 `@filename` 형태로 연결할 수 있습니다.

### Workflows

Workflows는 반복 작업 절차를 Markdown으로 저장해 두고 Agent 입력창에서 slash command로 실행하는 기능입니다.

이번 실습에서는 다음 workflow를 사용합니다.

```text
.agents/workflows/session-1-01-gemini-api.md
.agents/workflows/session-1-02-adk-gemini-api.md
.agents/workflows/session-1-03-ollama-server-api.md
.agents/workflows/session-1-04-adk-ollama.md
```

Agent 입력창에서는 파일명에서 `.md`를 뺀 이름으로 실행합니다.

```text
/session-1-01-gemini-api
/session-1-02-adk-gemini-api
/session-1-03-ollama-server-api
/session-1-04-adk-ollama
```

Workflow가 보이지 않으면 Customizations 패널의 Workflows에서 Workspace workflow로 직접 추가하고, 파일 내용을 붙여넣으면 됩니다.

Workflow 파일도 12,000자 이내로 유지하세요. 여러 반복 절차가 필요하면 하나의 긴 workflow보다 목적별 workflow로 나누는 편이 좋습니다.

### Skills

Skills는 특정 작업을 잘 처리하기 위한 지식과 절차를 묶어 둔 폴더입니다. workspace skill은 다음 위치에 둡니다.

```text
.agents/skills/<skill-name>/SKILL.md
```

이 저장소에는 Session 1 Python 핸즈온을 위한 skill이 포함되어 있습니다.

```text
.agents/skills/gemma4-python-hands-on/SKILL.md
```

`SKILL.md`에는 YAML frontmatter가 필요합니다. `description`은 필수이며, Agent가 어떤 상황에서 skill을 읽을지 판단하는 힌트가 됩니다.

```markdown
---
name: my-skill
description: Helps with a specific task.
---

# My Skill

Instructions for the agent go here.
```

Global skill은 모든 workspace에서 쓸 수 있지만, 행사 실습에서는 프로젝트별 동작을 맞추기 위해 workspace skill을 권장합니다.

```text
~/.gemini/antigravity/skills/<skill-name>/
```

### 설정 시 주의사항

- 실제 API 키, 토큰, 비밀번호를 rules, workflows, skills에 넣지 마세요.
- 참가자마다 다른 로컬 경로나 계정 정보는 문서에 고정하지 마세요.
- 실습 중 반복할 절차는 workflow에, 장기적으로 지켜야 할 규칙은 rule에, 특정 작업 지식은 skill에 두세요.
- 설정을 수정한 뒤에는 새 Agent 대화를 열거나 workspace를 다시 열어 반영 여부를 확인하세요.

## 행사 전 확인

- Antigravity 앱 실행 성공
- 개인 Gmail 계정 로그인 성공
- 첫 실행 설정 완료
- 행사 자료 폴더 열기 성공
- 터미널 패널 열기 가능 여부 확인
- `.agents/rules`, `.agents/workflows`, `.agents/skills` 인식 확인
- Python 핸즈온 workflow slash command 확인

Antigravity 설치나 로그인이 어렵다면 기존 VS Code 같은 코드 편집기를 준비해도 됩니다. 이 문서의 핵심 준비는 Ollama 설치, Gemma 4 모델 다운로드, API 테스트입니다.

## 공식 참고 링크

- Google Antigravity 다운로드: https://antigravity.google/download
- Google Antigravity Codelab: https://codelabs.developers.google.com/getting-started-google-antigravity
- Google Antigravity Rules / Workflows: https://antigravity.google/docs/rules-workflows
- Google Antigravity Skills: https://antigravity.google/docs/skills
