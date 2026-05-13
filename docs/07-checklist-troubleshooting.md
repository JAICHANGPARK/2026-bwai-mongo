# 최종 체크리스트와 문제 해결

[메인 안내로 돌아가기](../README.md)

## 행사 전 최종 체크리스트

### Windows

- PowerShell에서 `ollama --version` 성공
- `ollama pull gemma4:e2b` 또는 `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `Invoke-RestMethod http://localhost:11434/api/tags` 성공
- 가능하면 전원 어댑터 지참하기

### Apple Silicon Mac

- `uname -m` 결과가 `arm64`
- `ollama --version` 성공
- `ollama pull gemma4:e2b` 또는 `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `curl http://localhost:11434/api/tags` 성공
- 가능하면 전원 어댑터 지참하기

### Intel Mac

- `uname -m` 결과가 `x86_64`
- macOS 14 이상 확인
- `ollama --version` 성공
- `ollama pull gemma4:e2b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `curl http://localhost:11434/api/tags` 성공
- 큰 모델을 무리하게 받지 않기

## 빠른 준비 명령 모음

Windows PowerShell:

```powershell
ollama --version
ollama pull gemma4:e2b
ollama run gemma4:e2b
Invoke-RestMethod http://localhost:11434/api/tags
```

macOS:

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

Windows PowerShell에서도 위 두 줄을 그대로 실행하면 됩니다.

## 자주 생기는 문제

### `ollama` 명령을 찾을 수 없다고 나옵니다

- 터미널이나 PowerShell 창을 새로 열어 다시 실행하세요.
- macOS에서는 Ollama 앱을 한 번 실행하고 CLI 경로 연결 요청을 허용했는지 확인해 주세요.
- 그래도 안 되면 공식 설치 프로그램을 다시 실행하세요.

### 모델 다운로드가 너무 오래 걸립니다

- 정상일 수 있습니다. 모델 파일은 수 GB 이상입니다.
- 행사장 네트워크에서 처음 다운로드하지 마세요.
- 일단 `gemma4:e2b`만 먼저 완료하세요.

### 실행 중 컴퓨터가 너무 느려집니다

- 더 작은 모델을 사용하세요: `gemma4:e4b` 대신 `gemma4:e2b`
- 브라우저 탭, 영상 회의 앱, 무거운 개발 도구를 닫으세요.
- 8GB 장비와 Intel Mac에서는 느릴 수 있습니다.

### API가 연결되지 않습니다

먼저 서버가 떠 있는지 확인합니다.

macOS:

```bash
curl http://localhost:11434/api/tags
```

Windows PowerShell:

```powershell
Invoke-RestMethod http://localhost:11434/api/tags
```

실패하면 Ollama 앱을 실행하거나 `ollama serve`를 별도 터미널에서 실행하세요.

### `gemma4:latest`를 써도 되나요?

가능은 하지만 행사 준비용으로는 권장하지 않습니다. `latest`가 나중에 다른 모델로 바뀔 수 있으므로 `gemma4:e2b`, `gemma4:e4b`처럼 명시적 태그를 사용하세요.
