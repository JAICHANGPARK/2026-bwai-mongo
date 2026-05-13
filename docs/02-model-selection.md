# 내 컴퓨터에 맞는 Gemma 4 모델 선택

[메인 안내로 돌아가기](../README.md)

## 빠른 결론

모델 선택이 어렵다면 `gemma4:e2b`만 먼저 받아도 됩니다. 행사장에서 안정적으로 따라오는 것이 큰 모델을 무리하게 실행하는 것보다 중요합니다.

| 장비 | 기본 추천 | 추가 선택 | 비고 |
| --- | --- | --- | --- |
| Windows 8GB | `gemma4:e2b` | 없음 | 매우 느릴 수 있습니다. 가능하면 16GB 이상 권장 |
| Windows 16GB | `gemma4:e4b` | `gemma4:e2b` | 실패 시 E2B로 낮추세요 |
| Windows 32GB 이상 | `gemma4:e4b` | `gemma4:26b` | GPU/VRAM도 함께 확인 |
| Apple Silicon Mac 8GB | `gemma4:e2b` | 없음 | 브라우저 탭과 무거운 앱을 줄이세요 |
| Apple Silicon Mac 16GB | `gemma4:e4b` | `gemma4:e2b` | 가장 무난한 준비 |
| Apple Silicon Mac 32GB 이상 | `gemma4:e4b` | `gemma4:26b` 또는 `gemma4:31b` | 큰 모델은 행사 전 반드시 테스트 |
| Intel Mac | `gemma4:e2b` | `gemma4:e4b` | CPU 전용이라 많이 느릴 수 있습니다 |

## 모델별 준비 기준

### `gemma4:e2b`

가장 안전한 기본 모델입니다.

- 8GB 장비
- Intel Mac
- 처음 Ollama를 설치하는 참가자
- 큰 모델 다운로드가 부담되는 참가자

### `gemma4:e4b`

16GB 이상 장비에서 기본으로 권장할 수 있는 모델입니다.

- Windows 16GB 이상
- Apple Silicon Mac 16GB 이상
- E2B보다 조금 더 나은 답변 품질을 기대하는 경우

### `gemma4:26b`

32GB 이상 장비에서 실험할 수 있는 큰 모델입니다.

- 충분한 메모리와 디스크 여유가 있는 경우
- 큰 모델을 행사 전에 이미 테스트할 수 있는 경우
- 성능과 품질을 더 확인하고 싶은 경우

### `gemma4:31b`

36GB 이상 장비에서 품질 우선으로 시도할 수 있는 모델입니다.

- 일반 참가자 기본 준비용으로는 권장하지 않습니다.
- 다운로드와 실행 테스트를 행사 전에 반드시 끝내야 합니다.

## 모델 선택 시 주의

- 행사 당일에 큰 모델을 처음 다운로드하지 마세요.
- 8GB 장비는 작은 모델에서도 속도가 많이 느릴 수 있습니다.
- Intel Mac은 CPU 전용 실행이므로 메모리가 충분해도 Apple Silicon Mac보다 훨씬 느릴 수 있습니다.
- Windows에서 전용 GPU가 있어도 VRAM이 부족하면 큰 모델 실행이 느리거나 실패할 수 있습니다.
- `gemma4:latest` 대신 명시적인 태그를 사용하세요.

## 다음에 볼 문서

- [Windows 설치 가이드](./03-windows.md)
- [macOS Apple Silicon 설치 가이드](./04-macos-apple-silicon.md)
- [macOS Intel Mac 설치 가이드](./05-macos-intel.md)
