# Ollama 서버 및 API 테스트

[메인 안내로 돌아가기](../README.md)

## Ollama 서버 확인

Ollama 앱이 실행 중이면 서버는 보통 자동으로 떠 있습니다. 기본 주소는 아래와 같습니다.

```text
http://localhost:11434
```

연결이 안 되면 Ollama 앱을 실행하거나, 별도 터미널에서 아래 명령을 실행하세요.

macOS:

```bash
ollama serve
```

Windows PowerShell:

```powershell
ollama serve
```

이미 서버가 떠 있으면 포트가 사용 중이라는 메시지가 나올 수 있습니다. 이 경우는 보통 문제가 아닙니다.

## 1. 로컬 모델 목록 확인

macOS:

```bash
curl http://localhost:11434/api/tags
```

Windows PowerShell:

```powershell
Invoke-RestMethod http://localhost:11434/api/tags
```

다운로드한 `gemma4:e2b` 또는 `gemma4:e4b`가 보이면 모델 준비가 된 상태입니다.

## 2. Ollama Chat API 테스트

macOS:

```bash
curl http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e2b",
    "messages": [
      {
        "role": "user",
        "content": "Bwai Mongo 행사 준비 테스트입니다. 한 문장으로 답해 주세요."
      }
    ],
    "stream": false
  }'
```

Windows PowerShell:

```powershell
$body = @{
  model = "gemma4:e2b"
  messages = @(
    @{
      role = "user"
      content = "Bwai Mongo 행사 준비 테스트입니다. 한 문장으로 답해 주세요."
    }
  )
  stream = $false
} | ConvertTo-Json -Depth 5

Invoke-RestMethod `
  -Uri http://localhost:11434/api/chat `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

## 3. OpenAI 호환 API 테스트

일부 도구는 OpenAI 스타일 API 주소를 요구합니다. 이 경우 base URL은 아래처럼 씁니다.

```text
http://localhost:11434/v1
```

macOS:

```bash
curl http://localhost:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemma4:e2b",
    "messages": [
      {
        "role": "user",
        "content": "Say this is a local Ollama test."
      }
    ],
    "stream": false
  }'
```

Windows PowerShell:

```powershell
$body = @{
  model = "gemma4:e2b"
  messages = @(
    @{
      role = "user"
      content = "Say this is a local Ollama test."
    }
  )
  stream = $false
} | ConvertTo-Json -Depth 5

Invoke-RestMethod `
  -Uri http://localhost:11434/v1/chat/completions `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

도구 설정에서 API 키를 요구하면 임의 값으로 `ollama`를 넣으면 되는 경우가 많습니다. Ollama의 로컬 OpenAI 호환 API에서는 보통 이 값이 실제 인증에 쓰이지 않습니다.

## 다음 확인

API 테스트까지 성공했다면 [행사 전 최종 체크리스트와 문제 해결](./07-checklist-troubleshooting.md)을 확인하세요.
