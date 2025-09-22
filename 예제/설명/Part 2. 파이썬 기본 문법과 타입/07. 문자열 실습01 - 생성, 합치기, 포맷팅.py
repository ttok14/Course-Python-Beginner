# =======================================================
# Part 2. 문자열 실습01 - 생성, 합치기, 포맷팅
# =======================================================

# 1. 문자열 생성과 기본 연산
print("--- 1. 문자열 생성과 기본 연산 ---")

# 작은따옴표(')를 사용하여 문자열을 생성합니다.
first_name = '김민수'
print(f"first_name: {first_name}")

# 큰따옴표(")를 사용하여 문자열을 생성할 수 있습니다.
last_name = "님"
print(f"last_name: {last_name}")

# 더하기(+) 연산자로 문자열들을 합쳐 새로운 문자열을 만듭니다.
# 중간에 공백 문자열 ' '을 추가하여 띄어쓰기를 만듭니다.
full_name = first_name + ' ' + last_name
print(f"full_name (합치기): {full_name}")

# 곱하기(*) 연산자로 문자열을 여러 번 반복할 수 있습니다.
repeat_text = 'Hello! ' * 3
print(f"repeat_text (반복): {repeat_text}")
print("-" * 30)


# 2. 여러 줄 문자열과 길이 확인
print("\n--- 2. 여러 줄 문자열과 길이 확인 ---")

# 따옴표 세 개(''' 또는 """)를 사용하여 여러 줄에 걸친 문자열을 생성합니다.
# 이 방식은 코드에 보이는 줄바꿈을 그대로 문자열에 포함시킵니다.
message = '''안녕하세요!
파이썬 문자열 실습에
오신 것을 환영합니다.'''
print(message)

# len() 내장 함수를 사용하여 문자열의 길이를 확인합니다.
# 공백과 줄바꿈 문자(\n)를 포함한 전체 글자 수를 반환합니다.
message_length = len(message)
print(f"message의 길이: {message_length}")
print("-" * 30)


# 3. 타입 에러(TypeError)와 형 변환
print("\n--- 3. 타입 에러(TypeError)와 형 변환 ---")

age = 25

# 문자열(string)과 정수(integer)는 직접 더할 수 없어 TypeError가 발생합니다.
# 아래 코드의 주석을 해제하고 실행하면 에러를 직접 확인할 수 있습니다.
# intro_error = "나이: " + age
# print(intro_error)

# str() 함수를 사용하여 숫자를 문자열로 명시적으로 변환한 후 합쳐야 합니다.
intro_fixed = "나이: " + str(age)
print(f"str() 함수로 해결: {intro_fixed}")
print("-" * 30)


# 4. f-string을 사용한 효율적인 문자열 포매팅
print("\n--- 4. f-string을 사용한 문자열 포매팅 ---")

# f-string은 문자열 앞에 'f'를 붙여 사용합니다.
# 중괄호 {} 안에 변수 이름을 넣어 그 값을 문자열에 쉽게 삽입할 수 있습니다.
name = "이지은"
greeting = f"안녕하세요! 제 이름은 {name}입니다."
print(greeting)

# 중괄호 안에는 변수뿐만 아니라 직접적인 계산식도 넣을 수 있습니다.
age = 28
info = f"저는 {age}살이고, 내년에는 {age + 1}살이 됩니다."
print(info)

# 중괄호 안에서 함수 호출도 가능합니다.
detailed = f"이름: {name}, 나이: {age}, 이름 길이: {len(name)}"
print(detailed)

# f-string을 사용하면 str() 변환 없이도 다양한 타입의 변수를 쉽게 조합할 수 있습니다.
# 또한, 중괄호 안에 직접 연산을 포함시켜 코드를 간결하게 만들 수 있습니다.
price = 15000
quantity = 3
total_info = f"상품 가격: {price}원, 수량: {quantity}개, 총액: {price * quantity}원"
print(total_info)
print("-" * 30)


'''
    - 정리하며
        1. 작은따옴표('')와 큰따옴표("")로 문자열을 만들고, `+`와 `*` 연산자로 합치거나 반복할 수 있습니다.
        2. 따옴표 세 개(\'\'\')를 사용하면 여러 줄로 구성된 문자열을 만들 수 있으며, `len()` 함수로 문자열의 길이를 확인합니다.
        3. 다른 타입(예: 숫자)과 문자열을 `+`로 연결하려면, `str()` 함수를 통해 타입을 문자열로 통일해야 합니다.
        4. f-string (f"...")은 변수, 계산식, 함수 호출 결과를 중괄호 `{}` 안에 넣어 문자열을 만드는 현대적이고 매우 편리한 방법입니다.
'''