# =======================================================
# Part 2. 문자열 실습01 - 생성, 합치기, 포맷팅
# =======================================================

print("--- 1. 문자열 생성과 기본 연산 ---")

first_name = '김민수'
print(f"first_name: {first_name}")

last_name = "님"
print(f"last_name: {last_name}")

full_name = first_name + ' ' + last_name
print(f"full_name (합치기): {full_name}")

repeat_text = 'Hello! ' * 3
print(f"repeat_text (반복): {repeat_text}")
print("-" * 30)


print("\n--- 2. 여러 줄 문자열과 길이 확인 ---")

message = '''안녕하세요!
파이썬 문자열 실습에
오신 것을 환영합니다.'''
print(message)

message_length = len(message)
print(f"message의 길이: {message_length}")
print("-" * 30)


print("\n--- 3. 타입 에러(TypeError)와 형 변환 ---")

age = 25

intro_fixed = "나이: " + str(age)
print(f"str() 함수로 해결: {intro_fixed}")
print("-" * 30)


print("\n--- 4. f-string을 사용한 문자열 포매팅 ---")

name = "이지은"
greeting = f"안녕하세요! 제 이름은 {name}입니다."
print(greeting)

age = 28
info = f"저는 {age}살이고, 내년에는 {age + 1}살이 됩니다."
print(info)

detailed = f"이름: {name}, 나이: {age}, 이름 길이: {len(name)}"
print(detailed)

price = 15000
quantity = 3
total_info = f"상품 가격: {price}원, 수량: {quantity}개, 총액: {price * quantity}원"
print(total_info)
print("-" * 30)
