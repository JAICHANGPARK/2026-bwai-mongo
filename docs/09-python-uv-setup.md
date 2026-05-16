# Python + uv 설치 가이드

[메인 안내로 돌아가기](../README.md)

Python 핸즈온 실습에서는 `uv`로 Python 실행 환경과 패키지를 준비합니다. 행사장 네트워크에서 처음 설치하면 시간이 걸릴 수 있으니, 행사 전에 `uv`와 Python 실행 확인까지 마쳐 주세요.

`uv`는 필요한 Python을 직접 설치하고 관리할 수 있습니다. 이미 Python이 설치되어 있어도 괜찮고, Python이 없어도 아래 절차로 준비할 수 있습니다.

## 대상

- Windows 10 22H2 이상, PowerShell 사용자
- macOS Apple Silicon Mac
- macOS Intel Mac

## 1. 이미 설치되어 있는지 확인

Windows PowerShell 또는 macOS 터미널에서 실행합니다.

```bash
uv --version
uv run python --version
```

두 명령 모두 버전이 출력되면 `uv`와 Python 실행 준비가 된 상태입니다.

## 2. Windows PowerShell 설치

PowerShell에서 실행합니다.

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

설치가 끝나면 PowerShell 창을 닫고 새로 연 뒤 확인합니다.

```powershell
uv --version
uv python install 3.12
uv run --python 3.12 python --version
```

회사/학교 장비에서 스크립트 실행이 막히면 Windows 패키지 관리자인 `winget`으로 설치할 수 있습니다.

```powershell
winget install --id=astral-sh.uv -e
```

`winget`도 막히면 관리자 정책 때문에 설치가 제한된 상태일 수 있으니, 행사 전에 관리자 권한 또는 다른 개인 장비를 확인해 주세요.

## 3. macOS 설치

터미널에서 실행합니다.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

설치가 끝나면 터미널 창을 닫고 새로 열거나 다음 명령으로 셸을 다시 시작합니다.

```bash
exec $SHELL -l
```

그다음 확인합니다.

```bash
uv --version
uv python install 3.12
uv run --python 3.12 python --version
```

Homebrew를 이미 사용한다면 다음 명령으로 설치해도 됩니다.

```bash
brew install uv
```

## 4. 실습용 패키지 설치 확인

아래 명령은 `httpx` 패키지를 임시 실행 환경에 설치해 보고 Python import까지 확인합니다. 행사 전에 네트워크와 Python 패키지 설치가 되는지 확인하는 용도입니다.

```bash
uv run --python 3.12 --with httpx python -c "import httpx; print('uv ok')"
```

`uv ok`가 출력되면 실습용 Python 패키지를 받을 수 있는 상태입니다.

## 5. 자주 생기는 문제

### `uv` 명령을 찾을 수 없다고 나옵니다

- PowerShell 또는 터미널을 완전히 닫고 새로 열어 다시 실행하세요.
- macOS에서는 `exec $SHELL -l`을 실행한 뒤 다시 확인하세요.
- 그래도 안 되면 설치 명령을 한 번 더 실행하세요.

### Python 버전 확인이 실패합니다

먼저 Python 3.12를 명시적으로 설치합니다.

```bash
uv python install 3.12
uv run --python 3.12 python --version
```

### 회사/학교 장비에서 설치가 막힙니다

보안 정책 때문에 인터넷 스크립트 실행, `winget`, Homebrew 설치가 제한될 수 있습니다. 행사 전에 관리자 권한을 확인하거나 개인 장비를 준비해 주세요.
