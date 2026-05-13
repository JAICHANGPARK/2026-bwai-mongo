# Bwai Mongo Ollama + Gemma 4 사전 준비 가이드

Build with AI Mongo 행사 참가자를 위한 Ollama 설치 및 Gemma 4 모델 준비 안내입니다.  
기준 확인일: 2026-05-13

## 매우 중요한 안내

행사 당일에 처음 Ollama를 설치하거나 Gemma 4 모델을 다운로드하지 않는 것을 강하게 권장합니다.

Gemma 4 모델은 작은 모델도 수 GB 수준이고, 현장 네트워크 상황에 따라 다운로드만 오래 걸릴 수 있습니다. 행사 전까지 아래 세 가지를 끝내 주세요.

1. Ollama 설치 완료
2. Gemma 4 모델 다운로드 완료
3. 터미널 실행 테스트와 API 테스트 1회 성공

## 이 문서는 누구를 위한 문서인가요?

- Windows 노트북 사용자
- macOS Apple Silicon 사용자: M1, M2, M3, M4 계열
- macOS Intel Mac 사용자
- Ollama로 로컬 LLM 서버와 API를 준비해야 하는 참가자

Linux, ChromeOS, LM Studio, llama.cpp 같은 다른 경로는 이 문서의 범위에서 제외합니다.

## 빠른 결론

- 모델 선택이 어렵다면 `gemma4:e2b`부터 준비하세요.
- 16GB 이상 Windows 또는 Apple Silicon Mac이면 `gemma4:e4b`까지 준비하면 좋습니다.
- Intel Mac은 CPU 전용 실행이므로 `gemma4:e2b`를 기본으로 준비하세요.
- `gemma4:latest`는 나중에 바뀔 수 있으므로 행사 준비에서는 명시적 태그를 쓰세요.
- Ollama 서버 기본 주소는 `http://localhost:11434`입니다.

## Ollama란 무엇인가요?

Ollama는 로컬 컴퓨터에서 LLM을 다운로드하고 실행할 수 있게 해 주는 도구입니다. 설치하면 터미널에서 `ollama run`, `ollama pull` 같은 명령을 사용할 수 있고, 동시에 로컬 API 서버가 기본적으로 `http://localhost:11434`에서 동작합니다.

이번 행사에서는 Ollama를 아래 용도로 사용합니다.

- Gemma 4 모델을 내 노트북에 미리 다운로드
- 인터넷 없이도 로컬에서 모델 실행
- 터미널에서 간단한 대화 테스트
- 로컬 API 서버를 통해 앱, 스크립트, 에이전트 도구와 연결

자세한 설명은 [Ollama와 Gemma 4 개요](./docs/01-ollama-gemma4-overview.md)를 확인하세요.

## Gemma 4란 무엇인가요?

Gemma 4는 Google DeepMind가 공개한 오픈 모델 계열입니다. Google 공식 블로그 기준으로 Gemma 4는 고급 추론, 에이전트형 워크플로우, 코드 생성, 멀티모달 입력, 긴 컨텍스트를 목표로 설계되었습니다.

이번 행사에서는 Ollama에서 바로 실행 가능한 아래 태그를 기준으로 준비합니다.

| 모델 | Ollama 태그 | 표시 크기 | 컨텍스트 | 권장 환경 |
| --- | --- | ---: | ---: | --- |
| Gemma 4 E2B | `gemma4:e2b` | 7.2GB | 128K | 8GB 또는 Intel Mac 기본 |
| Gemma 4 E4B | `gemma4:e4b` | 9.6GB | 128K | 16GB 이상 기본 |
| Gemma 4 26B A4B | `gemma4:26b` | 18GB | 256K | 32GB 이상, 성능 실험 |
| Gemma 4 31B | `gemma4:31b` | 20GB | 256K | 36GB 이상, 품질 우선 |

`B`는 Billion, 즉 10억 개 파라미터 규모를 뜻합니다. `26B`가 파일 크기 26GB라는 뜻은 아닙니다.

## 내 컴퓨터에서 어떤 모델을 받아야 하나요?

| 장비 | 기본 추천 | 추가 선택 | 비고 |
| --- | --- | --- | --- |
| Windows 8GB | `gemma4:e2b` | 없음 | 매우 느릴 수 있습니다. 가능하면 16GB 이상 권장 |
| Windows 16GB | `gemma4:e4b` | `gemma4:e2b` | 실패 시 E2B로 낮추세요 |
| Windows 32GB 이상 | `gemma4:e4b` | `gemma4:26b` | GPU/VRAM도 함께 확인 |
| Apple Silicon Mac 8GB | `gemma4:e2b` | 없음 | 브라우저 탭과 무거운 앱을 줄이세요 |
| Apple Silicon Mac 16GB | `gemma4:e4b` | `gemma4:e2b` | 가장 무난한 준비 |
| Apple Silicon Mac 32GB 이상 | `gemma4:e4b` | `gemma4:26b` 또는 `gemma4:31b` | 큰 모델은 행사 전 반드시 테스트 |
| Intel Mac | `gemma4:e2b` | `gemma4:e4b` | CPU 전용이라 많이 느릴 수 있습니다 |

세부 기준은 [내 컴퓨터에 맞는 Gemma 4 모델 선택](./docs/02-model-selection.md)을 확인하세요.

## 운영체제별 준비 문서

| 사용자 환경 | 설치 문서 | 기본 추천 모델 |
| --- | --- | --- |
| Windows | [Windows 설치 가이드](./docs/03-windows.md) | `gemma4:e2b` 또는 `gemma4:e4b` |
| macOS Apple Silicon | [macOS Apple Silicon 설치 가이드](./docs/04-macos-apple-silicon.md) | `gemma4:e2b` 또는 `gemma4:e4b` |
| macOS Intel Mac | [macOS Intel Mac 설치 가이드](./docs/05-macos-intel.md) | `gemma4:e2b` |

## 빠른 준비 명령

### Windows PowerShell

```powershell
ollama --version
ollama pull gemma4:e2b
ollama run gemma4:e2b
Invoke-RestMethod http://localhost:11434/api/tags
```

16GB 이상 장비에서 E4B까지 준비할 경우:

```powershell
ollama pull gemma4:e4b
ollama run gemma4:e4b
```

### macOS

```bash
ollama --version
ollama pull gemma4:e2b
ollama run gemma4:e2b
curl http://localhost:11434/api/tags
```

16GB 이상 장비에서 E4B까지 준비할 경우:

```bash
ollama pull gemma4:e4b
ollama run gemma4:e4b
```

## Ollama 서버와 API 테스트

Ollama 앱이 실행 중이면 로컬 서버는 보통 자동으로 떠 있습니다.

```text
http://localhost:11434
```

연결이 안 되면 Ollama 앱을 실행하거나 별도 터미널에서 아래 명령을 실행하세요.

```bash
ollama serve
```

행사 전에는 아래 중 하나 이상을 확인하세요.

- 모델 목록 확인: `GET /api/tags`
- Ollama Chat API 테스트: `POST /api/chat`
- OpenAI 호환 API 테스트: `POST /v1/chat/completions`

자세한 예시는 [Ollama 서버 및 API 테스트](./docs/06-server-api-test.md)에 있습니다.

## 행사 전 최종 체크리스트

Windows:

- PowerShell에서 `ollama --version` 성공
- `ollama pull gemma4:e2b` 또는 `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `Invoke-RestMethod http://localhost:11434/api/tags` 성공

Apple Silicon Mac:

- `uname -m` 결과가 `arm64`
- `ollama --version` 성공
- `ollama pull gemma4:e2b` 또는 `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `curl http://localhost:11434/api/tags` 성공

Intel Mac:

- `uname -m` 결과가 `x86_64`
- macOS 14 이상 확인
- `ollama --version` 성공
- `ollama pull gemma4:e2b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `curl http://localhost:11434/api/tags` 성공

문제가 생기면 [행사 전 최종 체크리스트와 문제 해결](./docs/07-checklist-troubleshooting.md)을 확인하세요.

## 문서 목록

1. [Ollama와 Gemma 4 개요](./docs/01-ollama-gemma4-overview.md)
2. [내 컴퓨터에 맞는 Gemma 4 모델 선택](./docs/02-model-selection.md)
3. [Windows 설치 가이드](./docs/03-windows.md)
4. [macOS Apple Silicon 설치 가이드](./docs/04-macos-apple-silicon.md)
5. [macOS Intel Mac 설치 가이드](./docs/05-macos-intel.md)
6. [Ollama 서버 및 API 테스트](./docs/06-server-api-test.md)
7. [행사 전 최종 체크리스트와 문제 해결](./docs/07-checklist-troubleshooting.md)
8. [공식 참고 링크](./docs/08-references.md)

## 공식 참고 링크

- Ollama 다운로드: https://ollama.com/download
- Ollama Gemma 4 모델 페이지: https://ollama.com/library/gemma4
- Ollama API 문서: https://docs.ollama.com/api/introduction
- Ollama OpenAI 호환 API 문서: https://docs.ollama.com/api/openai-compatibility
- Google Gemma 4 출시 글: https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/
