# ====================================
# Part 2. 참/거짓 표현과 비교 연산
# ====================================

print("--- 1. bool 타입 기본 ---")
is_logged_in = True
has_error = False

print("로그인 상태:", is_logged_in)
print("에러 상태 변수의 타입:", type(has_error))
print("-" * 20)


print("--- 2. 숫자 비교 연산 ---")
print("100 == 100:", 100 == 100)
print("100 != 100:", 100 != 100)
print("50 > 25:", 50 > 25)
print("50 < 25:", 50 < 25)
print("10 >= 10:", 10 >= 10)
print("-" * 20)


print("--- 3. 문자열 비교 연산 ---")
print("'hello' == 'hello':", 'hello' == 'hello')
print("'hello' == 'Hello':", 'hello' == 'Hello')
print("'a' < 'b':", 'a' < 'b')
print("-" * 20)


print("--- 4. 비교 결과 변수에 저장하기 ---")
my_age = 30
adult_age = 20

is_adult = my_age >= adult_age
print("나는 성인인가?", is_adult)
print("-" * 20)


print("--- 5. Truthy와 Falsy ---")
print("bool(10):", bool(10))
print("bool(0):", bool(0))
print("bool(-1):", bool(-1))

print("bool(3.14):", bool(3.14))
print("bool(0.0):", bool(0.0))

print("bool('Python'):", bool('Python'))
print("bool(''):", bool(''))
print("-" * 20)