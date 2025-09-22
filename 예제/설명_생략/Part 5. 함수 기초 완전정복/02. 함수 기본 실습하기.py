# ====================================
# Part5. 함수 기본 살펴보기
# ====================================

print("--- 1. 함수가 없을 경우 (코드 중복 발생) ---")

print("프로그램의 여러 지점에서 환영 인사를 출력합니다.")
print("환영합니다!")
print("-" * 20)

print("또 다른 지점에서 다시 환영 인사를 합니다.")
print("환영합니다!")
print("-" * 20)


print("\n--- 2. 함수를 사용한 경우 (코드 재사용) ---")

def greet():
    print("환영합니다!")

print("프로그램의 여러 지점에서 환영 인사를 출력합니다.")
greet()
print("-" * 20)

print("또 다른 지점에서 다시 환영 인사를 합니다.")
greet()
print("-" * 20)


print("\n--- 3. 매개변수와 인자 ---")

def greet_with_name(name):
    print(f"{name}님, 환영합니다!")

greet_with_name("이강원")
greet_with_name("홍길동")


print("\n--- 4. 반환값(Return) ---")

def add(a, b):
    result = a + b
    return result

sum_result = add(10, 20)
print(f"10 + 20의 결과는: {sum_result} 입니다.")

new_result = add(5, 3) * 10
print(f"(5 + 3) * 10의 결과는: {new_result} 입니다.")


print("\n--- 5. 명시적 반환이 없는 함수 ---")

def simple_print():
    print("이 함수는 할 일만 하고 끝납니다.")

simple_print()

return_value = simple_print()
print(f"simple_print() 함수의 반환값: {return_value}")

print_return = print("이 문장의 반환값은 무엇일까요?")
print(f"print() 함수의 반환값: {print_return}")
