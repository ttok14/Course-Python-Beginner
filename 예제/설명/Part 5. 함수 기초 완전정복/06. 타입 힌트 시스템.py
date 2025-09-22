# ====================================
# Part 5. 타입 힌트 시스템
# ====================================

# 타입 힌트(Type Hint)는 변수, 함수의 매개변수, 반환 값의 타입을 명시적으로 선언하는 기능입니다.
# 파이썬의 동적 타이핑이 가지는 '실행 전에는 타입을 알 수 없는' 한계를 보완해줍니다.
# 힌트는 코드 실행에 직접적인 영향을 주지 않지만, 코드의 가독성과 안정성을 크게 향상시킵니다.

# 1. 기본 타입 힌트와 정적 분석 도구(Pylance)
print("--- 1. 기본 타입 힌트 ---")

# 함수 매개변수 a, b는 정수(int)이며, 반환 값 또한 정수(int)임을 명시합니다.
def add(a: int, b: int) -> int:
    return a + b

# 아래 코드는 타입 힌트를 명백히 위반합니다.
# 파이썬 자체는 이 코드를 실행 시점에 오류(TypeError)로 처리합니다.
# VS Code의 Pylance 같은 정적 분석 도구는 실행 전에 오류를 감지하고 알려줍니다.

# add(10, "hello") # 주석을 해제하고 Pylance의 타입 검사 모드를 켜면 오류가 표시됩니다.

# [참고] VS Code에서 Pylance 타입 검사 활성화 방법:
# 1. (Ctrl+Shift+P) 또는 (Cmd+Shift+P) 로 명령어 팔레트 열기
# 2. 'Open User Settings (UI)' 검색 및 실행
# 3. 검색창에 'Type Checking Mode' 입력
# 4. 설정을 'off'에서 'basic' 또는 'strict'로 변경합니다.

print(f"add(10, 5)의 결과: {add(10, 5)}") # 정상 실행됩니다.
print("-" * 30)


# 2. 'basic' 모드와 'strict' 모드의 차이
print("--- 2. 'basic'과 'strict' 모드 비교 ---")

# 매개변수 b에 타입 힌트가 의도적으로 누락되었습니다.
def subtract(a: int, b) -> int:
    return a - b

# 'basic' 모드: 명백한 타입 '불일치'만 검사하므로, 타입 힌트가 '없는' 경우는 지적하지 않습니다.
# 'strict' 모드: 모든 변수, 매개변수, 반환 값에 타입 힌트를 작성하도록 권장하며, 누락된 경우 알려줍니다.
# Pylance의 타입 검사 모드를 'strict'로 변경하면, 위 함수 'b'에 밑줄이 생기는 것을 확인할 수 있습니다.
print(f"subtract(10, 5)의 결과: {subtract(10, 5)}")
print("-" * 30)


# 3. 자료구조 및 복합 타입 힌트
print("--- 3. 복합 타입 힌트와 자동 완성 ---")

# names: list[str] -> 문자열(str)을 요소로 가지는 리스트(list)임을 의미합니다.
# -> None -> 이 함수는 명시적으로 값을 반환하지 않음을 의미합니다.
def process_names(names: list[str]) -> None:
    print("참가자 명단:")
    for name in names:
        # 타입 힌트 덕분에 개발 도구(IDE)는 'name'이 문자열임을 알고,
        # .upper(), .lower() 등 문자열 관련 메서드를 자동 완성으로 추천해줍니다.
        print(f"- {name.upper()}")

participants: list[str] = ["iron man", "captain america", "thor"]
process_names(participants)
print("-" * 30)

# Python 3.10 버전부터는 파이프(|) 기호를 사용하여 여러 타입을 허용할 수 있습니다.
# key 매개변수는 정수(int) 또는 문자열(str)일 수 있음을 의미합니다.
def find_user(key: int | str):
    if isinstance(key, int):
        print(f"ID {key}번으로 사용자를 찾습니다.")
    else:
        print(f"사용자 이름 '{key}'으로 사용자를 찾습니다.")

find_user(101)
find_user("admin")
print("-" * 30)


# 4. 정적 분석 도구 'mypy' 사용하기
print("--- 4. 정적 분석 도구 'mypy' ---")

# mypy는 Pylance와는 별개로 설치하여 사용하는 강력한 타입 검사기입니다.
# 터미널 설치: pip install mypy

def double(n: int) -> int:
    return n * 2

# 아래 코드는 타입 힌트를 명백히 위반합니다.
# 이 파이썬 스크립트를 직접 실행하면 런타임에 TypeError가 발생합니다.
#
# 실행하는 대신 터미널에서 'mypy <파일명>.py' 명령을 실행하면,
# mypy가 코드를 실행하지 않고도 정적 분석을 통해 아래 코드의 타입 오류를 찾아냅니다.
#
# mypy 실행 결과 예시:
# error: Argument 1 to "double" has incompatible type "str"; expected "int"

# 아래 코드의 주석을 해제하고 실행하면 에러가 발생합니다.
# result = double("hello")
# print(result)
print("위의 'double(\"hello\")' 코드는 주석 처리되어 있어 에러가 발생하지 않습니다.")
print("mypy를 통해 정적 분석을 테스트해볼 수 있습니다.")
print("-" * 30)

'''
    - 정리하며
        1. 타입 힌트는 코드의 가독성을 높여, 미래의 나 자신과 동료가 코드를 쉽게 이해하도록 돕습니다.
        2. 타입 힌트는 파이썬 실행 자체에 영향을 주지 않지만, 코드의 '설명서' 역할을 합니다.
        3. VS Code의 Pylance나 별도로 설치하는 mypy 같은 '정적 분석 도구'는 타입 힌트를 읽어 코드를 실행하기 전에 잠재적인 버그를 찾아줍니다.
        4. 개발 도구(IDE)는 타입 힌트를 기반으로 더 정확한 자동 완성 기능을 제공하여 개발 생산성을 높여줍니다.
        5. 복잡한 프로젝트와 협업 환경에서 타입 힌트는 코드의 안정성과 유지보수성을 높이는 필수적인 요소로 자리 잡고 있습니다.
'''