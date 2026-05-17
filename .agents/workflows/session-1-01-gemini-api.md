---
description: Session 1 01 Gemini API Gemma 4
---

# Session 1 01 Gemini API Gemma 4

Python 초보자용 핸즈온 코드를 생성하세요. 추가 질문을 하지 말고 바로 작업하세요.

목표는 Gemini API로 hosted Gemma 4를 호출하는 Python 파일 하나를 만드는 것입니다.

생성할 파일:

```text
hands-on/session-1/work/01_gemini_api_gemma4.py
```

선택적으로 `.env.example`이 없다면 다음 파일도 만드세요.

```text
hands-on/session-1/work/.env.example
```

전제:

- 참가자는 이미 `hands-on/session-1/work`에서 `uv init --bare --name gemma4-session-1 .`를 실행했습니다.
- 참가자는 이미 `uv venv`를 실행했습니다.
- 참가자는 이미 `uv add google-genai google-adk python-dotenv httpx`를 실행했습니다.
- Python 파일에 PEP 723 inline script metadata를 넣지 마세요.
- 실행 방식은 `uv run python 01_gemini_api_gemma4.py`입니다.

코드 요구사항:

- Python 3.10 이상 기준으로 작성하세요.
- `argparse`를 사용하세요.
- `.env` 파일을 `python-dotenv`의 `load_dotenv()`로 읽으세요.
- Gemini API 키는 `GEMINI_API_KEY` 또는 `GOOGLE_API_KEY` 환경 변수에서 읽히게 하세요.
- 기본 모델은 `gemma-4-26b-a4b-it`입니다.
- 모델은 `--model` 옵션 또는 `GEMINI_MODEL` 환경 변수로 바꿀 수 있게 하세요.
- `--prompt` 옵션을 제공하세요.
- `--system` 옵션을 제공하고 `types.GenerateContentConfig(system_instruction=...)`를 사용하세요.
- `--thinking` 옵션을 제공하고, 켜면 `types.ThinkingConfig(thinking_level="high")`를 사용하세요.
- `google.genai` import는 런타임 코드 안에서 수행하세요. 의존성 설치 전에도 `python 01_gemini_api_gemma4.py --help`가 동작해야 합니다.
- API 키가 없으면 한국어로 `.env` 설정 방법을 안내하고 종료하세요.
- 출력에는 모델명, 프롬프트, 응답 텍스트가 잘 보이게 하세요.
- 코드는 초보자가 읽기 쉽도록 짧게 유지하세요.

`.env.example` 내용:

```dotenv
GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemma-4-26b-a4b-it
ADK_GEMINI_MODEL=gemma-4-31b-it
OLLAMA_HOST=http://localhost:11434
OLLAMA_API_BASE=http://localhost:11434
OLLAMA_MODEL=gemma4:e2b
ADK_OLLAMA_MODEL=gemma4:e2b
```

생성 후 가능하면 다음 검사를 실행하세요.

```bash
cd hands-on/session-1/work
uv run python -m py_compile 01_gemini_api_gemma4.py
uv run python 01_gemini_api_gemma4.py --help
```

Gemini API 실제 호출은 API 키가 설정되어 있고 사용자가 명시적으로 요청할 때만 실행하세요.
