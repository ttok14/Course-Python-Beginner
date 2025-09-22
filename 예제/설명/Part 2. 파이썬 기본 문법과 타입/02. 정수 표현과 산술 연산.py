# ====================================
# Part 2. 정수 표현과 산술 연산
# ====================================

# 정수(Integer)는 소수점이 없는 숫자를 의미하며, 파이썬에서는 'int' 타입으로 다룹니다.
# 이번 실습에서는 정수 변수를 선언하고, 여러 산술 연산자를 사용해 계산을 수행합니다.

# 1. 실습용 변수 선언
print("--- 1. 실습용 변수 선언 ---")
num1 = 15
num2 = 4
print(f"num1: {num1}, num2: {num2}\n")


# 2. 기본 사칙연산 및 거듭제곱
print("--- 2. 기본 사칙연산 및 거듭제곱 ---")

# 덧셈 (+)
add_result = num1 + num2
print(f"덧셈 결과 (15 + 4): {add_result}")

# 뺄셈 (-)
subtract_result = num1 - num2
print(f"뺄셈 결과 (15 - 4): {subtract_result}")

# 곱셈 (*)
multiply_result = num1 * num2
print(f"곱셈 결과 (15 * 4): {multiply_result}")

# 거듭제곱 (**)
# 2의 5제곱을 계산합니다.
power_result = 2 ** 5
print(f"거듭제곱 결과 (2 ** 5): {power_result}\n")


# 3. 세 종류의 나눗셈 연산
print("--- 3. 세 종류의 나눗셈 연산 ---")

# 일반 나눗셈 (/)
# 결과가 항상 소수점(float)으로 나옵니다.
division_result = num1 / num2
print(f"일반 나눗셈 결과 (15 / 4): {division_result}")

# 정수 나눗셈 (//)
# 나눗셈의 몫만 정수로 반환합니다. 소수점 이하는 버려집니다.
floor_division_result = num1 // num2
print(f"정수 나눗셈(몫) 결과 (15 // 4): {floor_division_result}")

# 나머지 연산 (%)
# 나눗셈 후 남는 나머지를 반환합니다.
modulo_result = num1 % num2
print(f"나머지 연산 결과 (15 % 4): {modulo_result}\n")


# 4. 나머지 연산자(%) 활용: 짝수/홀수 판별
print("--- 4. 나머지 연산자(%) 활용 ---")

# 어떤 수를 2로 나누었을 때 나머지가 0이면 짝수, 1이면 홀수입니다.
even_num = 100
odd_num = 99

print(f"{even_num}을 2로 나눈 나머지: {even_num % 2}") # 결과: 0 (짝수)
print(f"{odd_num}을 2로 나눈 나머지: {odd_num % 2}\n")   # 결과: 1 (홀수)


# 5. 연산자 우선순위
print("--- 5. 연산자 우선순위 ---")

# 일반적인 수학의 연산 순서와 동일하게 곱셈/나눗셈이 덧셈/뺄셈보다 먼저 계산됩니다.
result_1 = 10 - 2 * 3 # 2 * 3 이 먼저 계산됩니다 (10 - 6).
print(f"10 - 2 * 3 의 결과: {result_1}")

# 괄호()를 사용하면 연산 순서를 강제로 지정할 수 있습니다.
result_2 = (10 - 2) * 3 # (10 - 2) 가 먼저 계산됩니다 (8 * 3).
print(f"(10 - 2) * 3 의 결과: {result_2}\n")


# 6. 응용: 게임 아이템 분배 시나리오
print("--- 6. 응용 시나리오 ---")

total_items = 127
party_members = 5

# 한 명당 몇 개의 아이템을 가질 수 있는가? (몫)
items_per_person = total_items // party_members
print(f"총 아이템 {total_items}개를 {party_members}명이 나눌 때,")
print(f"한 명당 가질 수 있는 아이템 개수: {items_per_person}개")

# 공평하게 나눠주고 남는 아이템은 몇 개인가? (나머지)
remaining_items = total_items % party_members
print(f"분배 후 남는 아이템 개수: {remaining_items}개")


'''
    - 정리하며
        1. 정수(int)는 소수점이 없는 숫자를 표현하는 기본적인 데이터 타입입니다.
        2. 산술 연산자에는 덧셈(+), 뺄셈(-), 곱셈(*), 거듭제곱(**)이 있습니다.
        3. 파이썬의 나눗셈은 세 가지 종류로 나뉩니다.
           - /: 결과를 항상 소수점으로 반환하는 일반 나눗셈입니다.
           - //: 나눗셈의 몫(정수 부분)만 반환하는 정수 나눗셈입니다.
           - %: 나눗셈의 나머지만 반환하는 나머지 연산입니다.
        4. 연산자 우선순위 규칙이 존재하며(곱셈/나눗셈 > 덧셈/뺄셈), 괄호()를 통해 연산 순서를 명확히 지정할 수 있습니다.
'''