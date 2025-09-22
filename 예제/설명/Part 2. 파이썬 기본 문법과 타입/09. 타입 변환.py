# ====================================
# Part 2. 타입 변환
# ====================================

# 1. 타입에 따른 '+' 연산 결과 비교
# 파이썬은 값의 타입에 따라 연산자의 동작이 달라집니다.
print("--- 1. 타입에 따른 '+' 연산 결과 비교 ---")

# 숫자(int)에 + 연산자를 사용하면 수학적인 덧셈을 수행합니다.
int_result = 10 + 20
print(f"정수 덧셈 결과: {int_result}")

# 문자열(str)에 + 연산자를 사용하면 두 문자열을 이어 붙이는 연결(concatenation)을 수행합니다.
str_result = '10' + '20'
print(f"문자열 연결 결과: {str_result}")
print("-" * 20)


# 2. input() 함수의 반환 타입 확인
# input() 함수는 사용자로부터 키보드 입력을 받으며, 입력된 값은 항상 문자열(str) 타입입니다.
# 아래 코드 블록은 실행 시 사용자 입력을 기다리므로, 개별적으로 테스트하는 것을 권장합니다.
print("--- 2. input() 함수의 반환 타입 확인 ---")

# 다음 줄의 주석(#)을 제거하고 실행하여 테스트할 수 있습니다.
# user_value = input('아무 숫자나 입력해보세요: ')
# print(f"입력받은 값: {user_value}")
# print(f"입력받은 값의 타입: {type(user_value)}") # 사용자가 숫자를 입력해도 <class 'str'>로 출력됩니다.

print("위 주석 처리된 input() 관련 코드를 해제하여 직접 테스트해볼 수 있습니다.")
print("-" * 20)


# 3. 타입 변환을 이용한 계산 예제
# 사용자로부터 두 숫자를 입력받아 덧셈을 수행하는 프로그램입니다.
print("--- 3. 타입 변환을 이용한 계산 예제 ---")

# 아래 코드들의 주석을 해제하여 테스트할 수 있습니다.
#
# # input()으로 받은 값은 문자열이므로, 그대로 더하면 문자열 연결이 발생합니다.
# num1_str = input('첫 번째 숫자: ')
# num2_str = input('두 번째 숫자: ')
#
# # 문제 상황: 문자열 덧셈
# result_str_concat = num1_str + num2_str
# print(f"문자열 연결 결과: {result_str_concat}") # 예: '10'과 '20'을 입력하면 '1020'이 출력됩니다.
#
# # 해결책: int() 함수로 타입 변환
# # int() 함수를 사용하여 문자열을 정수(int) 타입으로 변환합니다.
# num1_int = int(num1_str)
# num2_int = int(num2_str)
#
# result_int_sum = num1_int + num2_int
# print(f"정수 덧셈 결과: {result_int_sum}") # 예: '10'과 '20'을 입력하면 30이 출력됩니다.
print("위 주석 처리된 input() 관련 코드를 해제하여 직접 테스트해볼 수 있습니다.")
print("-" * 20)


# 4. 다양한 타입 변환 함수
print("--- 4. 다양한 타입 변환 함수 ---")

# int() -> 정수로 변환
str_val = "123"
int_val = int(str_val)
print(f"int('{str_val}') -> {int_val}, 타입: {type(int_val)}")

float_val_to_int = 9.9
int_from_float = int(float_val_to_int)
# float를 int로 변환하면 소수점 이하 부분이 버려집니다. (반올림 아님)
print(f"int({float_val_to_int}) -> {int_from_float}, 타입: {type(int_from_float)}")

# float() -> 소수(부동소수점 수)로 변환
str_float_val = "3.14"
float_val = float(str_float_val)
print(f"float('{str_float_val}') -> {float_val}, 타입: {type(float_val)}")

int_to_float = 100
float_from_int = float(int_to_float)
print(f"float({int_to_float}) -> {float_from_int}, 타입: {type(float_from_int)}")

# str() -> 문자열로 변환
num_val = 500
str_from_num = str(num_val)
print(f"str({num_val}) -> '{str_from_num}', 타입: {type(str_from_num)}")
print("-" * 20)


# 5. 타입 변환 시 발생할 수 있는 오류 (ValueError)
# 논리적으로 변환이 불가능한 경우 ValueError가 발생합니다.
print("--- 5. 타입 변환 시 발생할 수 있는 오류 ---")

invalid_str = "파이썬"
try:
    # '파이썬'이라는 문자열은 숫자로 변환할 수 없습니다.
    print(f"int('{invalid_str}') 시도...")
    int(invalid_str)
except ValueError as e:
    # try-except 구문을 사용하여 프로그램이 비정상 종료되는 것을 방지하고, 에러를 처리합니다.
    print(f"오류 발생: {e}")
    print("숫자로 변환할 수 없는 문자열에 int() 함수를 사용하면 ValueError가 발생합니다.")
print("-" * 20)


'''
    - 정리하며
        1. 파이썬의 모든 값은 고유한 타입을 가지며, 타입에 따라 연산 방식이 달라집니다. (예: 숫자 덧셈 vs 문자열 연결)
        2. 값의 현재 타입은 type() 내장 함수를 사용하여 확인할 수 있습니다.
        3. int(), float(), str() 등의 함수를 사용하여 데이터의 타입을 원하는 형태로 변환할 수 있습니다.
        4. 사용자 입력을 받는 input() 함수는 모든 입력을 문자열(str)로 반환하므로, 숫자 계산이 필요할 경우 반드시 타입 변환이 필요합니다.
        5. 논리적으로 변환할 수 없는 값을 변환하려고 시도하면 ValueError가 발생합니다.
'''
