# ====================================
# Part 2. 타입 변환
# ====================================

print("--- 1. 타입에 따른 '+' 연산 결과 비교 ---")

int_result = 10 + 20
print(f"정수 덧셈 결과: {int_result}")

str_result = '10' + '20'
print(f"문자열 연결 결과: {str_result}")
print("-" * 20)


print("--- 2. input() 함수의 반환 타입 확인 ---")

# user_value = input('아무 숫자나 입력해보세요: ')
# print(f"입력받은 값: {user_value}")
# print(f"입력받은 값의 타입: {type(user_value)}")

print("위 주석 처리된 input() 관련 코드를 해제하여 직접 테스트해볼 수 있습니다.")
print("-" * 20)


print("--- 3. 타입 변환을 이용한 계산 예제 ---")

# num1_str = input('첫 번째 숫자: ')
# num2_str = input('두 번째 숫자: ')
#
# result_str_concat = num1_str + num2_str
# print(f"문자열 연결 결과: {result_str_concat}")
#
# num1_int = int(num1_str)
# num2_int = int(num2_str)
#
# result_int_sum = num1_int + num2_int
# print(f"정수 덧셈 결과: {result_int_sum}")
print("위 주석 처리된 input() 관련 코드를 해제하여 직접 테스트해볼 수 있습니다.")
print("-" * 20)


print("--- 4. 다양한 타입 변환 함수 ---")

str_val = "123"
int_val = int(str_val)
print(f"int('{str_val}') -> {int_val}, 타입: {type(int_val)}")

float_val_to_int = 9.9
int_from_float = int(float_val_to_int)
print(f"int({float_val_to_int}) -> {int_from_float}, 타입: {type(int_from_float)}")

str_float_val = "3.14"
float_val = float(str_float_val)
print(f"float('{str_float_val}') -> {float_val}, 타입: {type(float_val)}")

int_to_float = 100
float_from_int = float(int_to_float)
print(f"float({int_to_float}) -> {float_from_int}, 타입: {type(float_from_int)}")

num_val = 500
str_from_num = str(num_val)
print(f"str({num_val}) -> '{str_from_num}', 타입: {type(str_from_num)}")
print("-" * 20)


print("--- 5. 타입 변환 시 발생할 수 있는 오류 ---")

invalid_str = "파이썬"
try:
    print(f"int('{invalid_str}') 시도...")
    int(invalid_str)
except ValueError as e:
    print(f"오류 발생: {e}")
    print("숫자로 변환할 수 없는 문자열에 int() 함수를 사용하면 ValueError가 발생합니다.")
print("-" * 20)