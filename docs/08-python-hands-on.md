# Gemma 4 Python 핸즈온 생성 프롬프트

[메인 안내로 돌아가기](../README.md)

40-50분 실습용 Python 핸즈온 생성 프롬프트는 [`hands-on/session-1`](../hands-on/session-1)에 있습니다.

## 실습 흐름

| 순서 | 파일 | 내용 |
| --- | --- | --- |
| 1 | [`.agents/rules/session-1-common-rules.md`](../.agents/rules/session-1-common-rules.md) | Antigravity 공통 rule |
| 2 | [`.agents/workflows/session-1-01-gemini-api.md`](../.agents/workflows/session-1-01-gemini-api.md) | Gemini API 예제 생성 workflow |
| 3 | [`.agents/workflows/session-1-02-ollama-server-api.md`](../.agents/workflows/session-1-02-ollama-server-api.md) | Ollama 서버 API 예제 생성 workflow |
| 4 | [`prompts/01-gemini-api-gemma4-system-prompt.md`](../hands-on/session-1/prompts/01-gemini-api-gemma4-system-prompt.md) | AI Studio용 Gemini API 시스템 프롬프트 |
| 5 | [`prompts/02-ollama-server-api-system-prompt.md`](../hands-on/session-1/prompts/02-ollama-server-api-system-prompt.md) | AI Studio용 Ollama 서버 API 시스템 프롬프트 |
| 6 | `work/` | 생성 코드 위치 |
| 7 | [`reference/`](../hands-on/session-1/reference) | 참고 구현 |

## 가장 짧은 준비와 실행 명령

`uv`가 설치되어 있지 않다면 먼저 [Python + uv 설치 가이드](./09-python-uv-setup.md)를 확인하세요.

먼저 `work/`를 uv 프로젝트로 초기화합니다.

```bash
cd hands-on/session-1/work
uv init --bare --name gemma4-session-1 .
uv venv
uv add google-genai python-dotenv httpx
```

각 Antigravity workflow 또는 AI Studio용 시스템 프롬프트로 코드 생성 후 실행합니다.

API 키는 생성된 `.env.example`을 `.env`로 복사한 뒤 넣는 방식을 권장합니다.

Gemini API:

```bash
cp .env.example .env
uv run python 01_gemini_api_gemma4.py
```

Ollama 서버 API:

```bash
ollama pull gemma4:e2b
ollama serve
uv run python 02_ollama_server_api.py
```

자세한 진행 순서와 옵션은 [`hands-on/session-1/README.md`](../hands-on/session-1/README.md)를 확인하세요.
