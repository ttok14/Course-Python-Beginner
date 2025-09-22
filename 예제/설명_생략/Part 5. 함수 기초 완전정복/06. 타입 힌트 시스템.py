# ====================================
# Part 5. 타입 힌트 시스템
# ====================================

print("--- 1. 기본 타입 힌트 ---")

def add(a: int, b: int) -> int:
    return a + b

print(f"add(10, 5)의 결과: {add(10, 5)}")
print("-" * 30)


print("--- 2. 'basic'과 'strict' 모드 비교 ---")

def subtract(a: int, b) -> int:
    return a - b

print(f"subtract(10, 5)의 결과: {subtract(10, 5)}")
print("-" * 30)


print("--- 3. 복합 타입 힌트와 자동 완성 ---")

def process_names(names: list[str]) -> None:
    print("참가자 명단:")
    for name in names:
        print(f"- {name.upper()}")

participants: list[str] = ["iron man", "captain america", "thor"]
process_names(participants)
print("-" * 30)

def find_user(key: int | str):
    if isinstance(key, int):
        print(f"ID {key}번으로 사용자를 찾습니다.")
    else:
        print(f"사용자 이름 '{key}'으로 사용자를 찾습니다.")

find_user(101)
find_user("admin")
print("-" * 30)


print("--- 4. 정적 분석 도구 'mypy' ---")

def double(n: int) -> int:
    return n * 2

print("위의 'double(\"hello\")' 코드는 주석 처리되어 있어 에러가 발생하지 않습니다.")
print("mypy를 통해 정적 분석을 테스트해볼 수 있습니다.")
print("-" * 30)