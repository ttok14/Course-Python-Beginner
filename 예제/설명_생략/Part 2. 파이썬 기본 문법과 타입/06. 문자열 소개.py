# ====================================
# Part 2. 문자열 소개
# ====================================


print("--- 1. 문자열 생성하기 ---")

string1 = 'Hello, Python!'
string2 = "Hello, Python!"

multi_line_string = """이것은
여러 줄에 걸쳐 작성된
문자열입니다."""

print("작은따옴표로 생성:", string1)
print("큰따옴표로 생성:", string2)
print("여러 줄 문자열:\n" + multi_line_string)
print("-" * 20)


print("--- 2. 문자열 연산: 연결(+)과 반복(*) ---")

greeting = "Hello"
name = "Python"
combined_string = greeting + ", " + name + "!"
print("문자열 연결:", combined_string)

repeated_string = "Go! " * 3
print("문자열 반복:", repeated_string)
print("-" * 20)


print("--- 3. 타입 에러(TypeError)와 타입 변환 ---")

age = 20
try:
    print("I am " + age)
except TypeError as e:
    print("에러 발생:", e)
    print("-> 문자열과 숫자는 직접 더할 수 없습니다.")

message = "I am " + str(age)
print("str() 함수 사용:", message)

f_string_message = f"I am {age}"
print("f-string 사용:", f_string_message)

price = 1000
quantity = 3
total_price_message = f"총 금액: {price * quantity}원"
print("f-string 연산:", total_price_message)
print("-" * 20)


print("--- 4. 인덱싱(Indexing): 특정 위치의 문자 접근 ---")

text = "Python"


print(f"원본 문자열: {text}")
print("첫 번째 문자 (index 0):", text[0])
print("세 번째 문자 (index 2):", text[2])

print("마지막 문자 (index -1):", text[-1])
print("뒤에서 두 번째 문자 (index -2):", text[-2])
print("-" * 20)


print("--- 5. 슬라이싱(Slicing): 원하는 구간 잘라내기 ---")

print(f"원본 문자열: {text}")
print("인덱스 1부터 4 전까지 (1~3):", text[1:4])

print("처음부터 인덱스 3 전까지 (0~2):", text[:3])

print("인덱스 2부터 끝까지:", text[2:])
print("-" * 20)


print("--- 6. 이스케이프 시퀀스와 Raw String ---")

print("작은따옴표 안에 '작은따옴표' 넣기:", '그가 \'안녕\'이라고 말했다.')
print("큰따옴표 안에 '작은따옴표' 넣기:", "그가 '안녕'이라고 말했다.")

print("줄바꿈:\n두 줄에 걸쳐 출력됩니다.")
print("탭:\t앞에 탭이 들어갑니다.")
print("역슬래시 출력:", "C:\\Users\\MyFolder")

raw_path = r"C:\Users\MyFolder\new_file.txt"
print("Raw String 경로:", raw_path)
print("-" * 20)


print("--- 7. 자주 사용하는 문자열 함수(메서드) ---")

s = "hello, world!"

print(f"문자열 '{s}'의 길이:", len(s))

print("대문자로:", s.upper())

print("소문자로:", "HELLO, WORLD!".lower())

print("원본 문자열 확인:", s)
print("-" * 20)