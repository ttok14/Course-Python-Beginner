# ====================================
# Part 2. 정수 표현과 산술 연산
# ====================================

print("--- 1. 실습용 변수 선언 ---")
num1 = 15
num2 = 4
print(f"num1: {num1}, num2: {num2}\n")


print("--- 2. 기본 사칙연산 및 거듭제곱 ---")

add_result = num1 + num2
print(f"덧셈 결과 (15 + 4): {add_result}")

subtract_result = num1 - num2
print(f"뺄셈 결과 (15 - 4): {subtract_result}")

multiply_result = num1 * num2
print(f"곱셈 결과 (15 * 4): {multiply_result}")

power_result = 2 ** 5
print(f"거듭제곱 결과 (2 ** 5): {power_result}\n")


print("--- 3. 세 종류의 나눗셈 연산 ---")

division_result = num1 / num2
print(f"일반 나눗셈 결과 (15 / 4): {division_result}")

floor_division_result = num1 // num2
print(f"정수 나눗셈(몫) 결과 (15 // 4): {floor_division_result}")

modulo_result = num1 % num2
print(f"나머지 연산 결과 (15 % 4): {modulo_result}\n")


print("--- 4. 나머지 연산자(%) 활용 ---")

even_num = 100
odd_num = 99

print(f"{even_num}을 2로 나눈 나머지: {even_num % 2}")
print(f"{odd_num}을 2로 나눈 나머지: {odd_num % 2}\n")


print("--- 5. 연산자 우선순위 ---")

result_1 = 10 - 2 * 3
print(f"10 - 2 * 3 의 결과: {result_1}")

result_2 = (10 - 2) * 3
print(f"(10 - 2) * 3 의 결과: {result_2}\n")


print("--- 6. 응용 시나리오 ---")

total_items = 127
party_members = 5

items_per_person = total_items // party_members
print(f"총 아이템 {total_items}개를 {party_members}명이 나눌 때,")
print(f"한 명당 가질 수 있는 아이템 개수: {items_per_person}개")

remaining_items = total_items % party_members
print(f"분배 후 남는 아이템 개수: {remaining_items}개")