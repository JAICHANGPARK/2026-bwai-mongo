# Gemma 4 Python 핸즈온 Session 1

이 세션은 완성 코드를 따라 치는 실습이 아니라, 시스템 프롬프트로 핸즈온 코드를 단계별 생성하는 실습입니다.

## 구성

| 경로 | 용도 |
| --- | --- |
| `.agents/rules/session-1-common-rules.md` | Antigravity workspace rule |
| `.agents/workflows/session-1-01-gemini-api.md` | Antigravity workflow 1 |
| `.agents/workflows/session-1-02-ollama-server-api.md` | Antigravity workflow 2 |
| `prompts/01-gemini-api-gemma4-system-prompt.md` | Gemini API 예제 생성용 시스템 프롬프트 |
| `prompts/02-ollama-server-api-system-prompt.md` | Ollama 서버 API 예제 생성용 시스템 프롬프트 |
| `work/` | 생성 코드 위치 |
| `reference/` | 참고 구현 |

## 진행 시간

| 시간 | 내용 |
| ---: | --- |
| 0-5분 | `uv`, Python, Ollama 준비 확인 |
| 5-10분 | `uv init`, `uv venv`, `uv add`로 프로젝트 준비 |
| 10-22분 | 01 프롬프트로 Gemini API 코드 생성 |
| 22-30분 | Gemini API hosted Gemma 4 실행 |
| 30-40분 | 02 프롬프트로 Ollama 서버 API 코드 생성 |
| 40-48분 | Ollama native API와 OpenAI 호환 API 실행 |
| 48-50분 | hosted API와 로컬 서버 API 차이 정리 |

## 0. 사전 준비

Python, `uv`, Ollama를 확인합니다. `uv`가 설치되어 있지 않다면 먼저 [Python + uv 설치 가이드](../../docs/09-python-uv-setup.md)를 확인하세요.

```bash
uv --version
uv run python --version
ollama --version
```

Ollama 실습 전에는 모델이 미리 다운로드되어 있어야 합니다.

```bash
ollama pull gemma4:e2b
ollama list
```

16GB 이상 장비에서는 `gemma4:e4b`도 사용할 수 있습니다.

macOS/Linux:

```bash
ollama pull gemma4:e4b
export OLLAMA_MODEL=gemma4:e4b
```

Windows PowerShell:

```powershell
ollama pull gemma4:e4b
$env:OLLAMA_MODEL = "gemma4:e4b"
```

## 1. uv 프로젝트 준비

`work/` 폴더를 작은 Python 프로젝트로 초기화합니다.

```bash
cd hands-on/session-1/work
uv init --bare --name gemma4-session-1 .
uv venv
uv add google-genai python-dotenv httpx
```

의존성 역할:

- `google-genai`: Gemini API 호출
- `python-dotenv`: `.env` 파일에서 API 키와 설정 로드
- `httpx`: Ollama 서버 API 호출

## 2. 01 Gemini API 코드 생성

Antigravity를 사용하는 경우 Agent 채팅에서 workspace workflow를 호출합니다.

```text
/session-1-01-gemini-api
시작
```

AI Studio 또는 다른 도구를 사용하는 경우 System Instructions에 다음 파일 전체를 넣습니다.

```text
hands-on/session-1/prompts/01-gemini-api-gemma4-system-prompt.md
```

일반 프롬프트에는 이렇게 입력합니다.

```text
시작
```

AI Studio는 로컬 파일을 직접 만들지 못하므로, 응답에 나온 코드 블록을 아래 경로에 직접 저장합니다.

```text
hands-on/session-1/work/01_gemini_api_gemma4.py
hands-on/session-1/work/.env.example
```

## 3. .env 파일 준비

생성된 `.env.example`을 `.env`로 복사하고 API 키를 넣습니다.

macOS/Linux:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

`.env` 예시:

```dotenv
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemma-4-26b-a4b-it
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma4:e2b
```

## 4. 01 Gemini API 코드 실행

```bash
uv run python -m py_compile 01_gemini_api_gemma4.py
uv run python 01_gemini_api_gemma4.py --help
uv run python 01_gemini_api_gemma4.py
```

thinking 켜기:

```bash
uv run python 01_gemini_api_gemma4.py --thinking
```

## 5. 02 Ollama 서버 API 코드 생성

Antigravity를 사용하는 경우 Agent 채팅에서 두 번째 workflow를 호출합니다.

```text
/session-1-02-ollama-server-api
시작
```

AI Studio 또는 다른 도구를 사용하는 경우 System Instructions를 다음 파일 내용으로 교체합니다.

```text
hands-on/session-1/prompts/02-ollama-server-api-system-prompt.md
```

일반 프롬프트에는 다시 이렇게 입력합니다.

```text
시작
```

AI Studio 응답에 나온 코드 블록을 아래 경로에 저장합니다.

```text
hands-on/session-1/work/02_ollama_server_api.py
```

## 6. 02 Ollama 서버 API 코드 실행

Ollama 앱을 켜거나 별도 터미널에서 서버를 실행합니다.

```bash
ollama serve
```

서버 확인:

```bash
curl http://localhost:11434/api/tags
```

Ollama native API:

```bash
uv run python -m py_compile 02_ollama_server_api.py
uv run python 02_ollama_server_api.py --help
uv run python 02_ollama_server_api.py
```

OpenAI 호환 API:

```bash
uv run python 02_ollama_server_api.py --endpoint openai
```

## 참고 구현

`reference/`에는 각 프롬프트가 만들도록 의도한 최소 구현이 들어 있습니다. 생성 결과가 크게 벗어났을 때 비교용으로 사용하세요.

## Antigravity 수동 설정

Antigravity가 `.agents/` 설정을 자동으로 인식하지 못하는 경우에는 UI에서 직접 추가합니다.

Rules:

```text
.agents/rules/session-1-common-rules.md
```

Workflows:

```text
.agents/workflows/session-1-01-gemini-api.md
.agents/workflows/session-1-02-ollama-server-api.md
```
