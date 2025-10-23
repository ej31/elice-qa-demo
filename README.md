# GitHub Actions CI Demo

이 저장소는 간단한 파이썬 텍스트 분석 모듈과 구구단 2단 출력 프로그램, 그리고 해당 기능들을 검증하는 단위 테스트를 포함한 CI 데모입니다. GitHub에 push 하면 GitHub Actions가 자동으로 테스트를 실행하여 결과를 콘솔 로그에서 확인할 수 있습니다.

## 프로젝트 구조

- `src/text_analyzer.py`: 텍스트를 토큰화하고 통계를 계산하는 핵심 로직.
- `src/gugudan.py`: 구구단 2단을 콘솔에 출력하는 스크립트.
- `tests/`: 각 모듈을 검증하는 `unittest` 기반 단위 테스트.
- `.github/workflows/ci.yml`: push 및 PR 시 테스트를 실행하는 GitHub Actions 워크플로.

## 로컬에서 실행하기

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

### 구구단 2단 스크립트 실행

```bash
python src/gugudan.py
```

실행하면 아래와 같은 결과가 출력됩니다.

```
구구단 2단
2 x 1 = 2
...
2 x 9 = 18
```

## GitHub Actions 확인 방법

1. 이 프로젝트를 GitHub 저장소로 push 합니다. (기본 브랜치는 `main`이어야 합니다.)
2. 리포지토리의 **Actions** 탭으로 이동합니다.
3. `CI Demo` 워크플로 실행이 자동으로 시작되는 것을 확인합니다.
4. 실행 중인 워크플로를 클릭하면 실시간 콘솔 로그에서 테스트 진행 상황을 볼 수 있습니다.

필요에 맞게 테스트나 워크플로 단계를 추가하면서 CI 파이프라인을 확장해보세요.
