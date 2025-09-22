# ====================================
# Part 2. 문자열 소개
# ====================================

# 문자열(String)은 문자들의 연속된 묶음(Sequence)입니다.
# 파이썬에서는 텍스트 데이터를 다루기 위해 문자열 타입을 사용합니다.


# --- 1. 문자열 생성하기 ---
print("--- 1. 문자열 생성하기 ---")

# 작은따옴표(') 또는 큰따옴표(")를 사용하여 한 줄 문자열을 생성합니다.
string1 = 'Hello, Python!'
string2 = "Hello, Python!"

# 따옴표 세 개(''' 또는 """)를 사용하여 여러 줄에 걸친 문자열을 생성할 수 있습니다.
multi_line_string = """이것은
여러 줄에 걸쳐 작성된
문자열입니다."""

print("작은따옴표로 생성:", string1)
print("큰따옴표로 생성:", string2)
print("여러 줄 문자열:\n" + multi_line_string) # \n은 줄바꿈을 의미합니다.
print("-" * 20)


# --- 2. 문자열 연산: 연결(+)과 반복(*) ---
print("--- 2. 문자열 연산: 연결(+)과 반복(*) ---")

# '+' 연산자를 사용하여 두 문자열을 이어 붙일 수 있습니다.
greeting = "Hello"
name = "Python"
combined_string = greeting + ", " + name + "!"
print("문자열 연결:", combined_string)

# '*' 연산자를 사용하여 문자열을 여러 번 반복할 수 있습니다.
repeated_string = "Go! " * 3
print("문자열 반복:", repeated_string)
print("-" * 20)


# --- 3. 타입 에러(TypeError)와 타입 변환 ---
print("--- 3. 타입 에러(TypeError)와 타입 변환 ---")

# 문자열은 숫자와 직접 더할 수 없습니다. 이는 TypeError를 발생시킵니다.
age = 20
try:
    # 이 코드는 의도적으로 에러를 발생시킵니다.
    print("I am " + age)
except TypeError as e:
    print("에러 발생:", e)
    print("-> 문자열과 숫자는 직접 더할 수 없습니다.")

# 숫자를 문자열로 변환하려면 str() 함수를 사용해야 합니다.
message = "I am " + str(age)
print("str() 함수 사용:", message)

# f-string을 사용하면 더 간편하게 문자열과 변수를 결합할 수 있습니다.
# 문자열 앞에 'f'를 붙이고, 변수를 {} 안에 넣습니다.
f_string_message = f"I am {age}"
print("f-string 사용:", f_string_message)

# f-string 안에서는 연산도 가능합니다.
price = 1000
quantity = 3
total_price_message = f"총 금액: {price * quantity}원"
print("f-string 연산:", total_price_message)
print("-" * 20)


# --- 4. 인덱싱(Indexing): 특정 위치의 문자 접근 ---
print("--- 4. 인덱싱(Indexing): 특정 위치의 문자 접근 ---")

text = "Python"
# 인덱스는 0부터 시작합니다.
# P  y  t  h  o  n
# 0  1  2  3  4  5

print(f"원본 문자열: {text}")
print("첫 번째 문자 (index 0):", text[0])   # 'P'
print("세 번째 문자 (index 2):", text[2])   # 't'

# 음수 인덱스는 뒤에서부터 위치를 셉니다. -1이 가장 마지막 문자입니다.
print("마지막 문자 (index -1):", text[-1]) # 'n'
print("뒤에서 두 번째 문자 (index -2):", text[-2]) # 'o'
print("-" * 20)


# --- 5. 슬라이싱(Slicing): 원하는 구간 잘라내기 ---
print("--- 5. 슬라이싱(Slicing): 원하는 구간 잘라내기 ---")

# 슬라이싱은 [시작인덱스:끝인덱스] 형식으로 사용합니다.
# 끝인덱스에 해당하는 문자는 포함되지 않습니다.
print(f"원본 문자열: {text}")
print("인덱스 1부터 4 전까지 (1~3):", text[1:4])  # 'yth'

# 시작 인덱스를 생략하면 처음부터 잘라냅니다.
print("처음부터 인덱스 3 전까지 (0~2):", text[:3]) # 'Pyt'

# 끝 인덱스를 생략하면 끝까지 잘라냅니다.
print("인덱스 2부터 끝까지:", text[2:]) # 'thon'
print("-" * 20)


# --- 6. 이스케이프 시퀀스와 Raw String ---
print("--- 6. 이스케이프 시퀀스와 Raw String ---")

# 문자열 내부에 따옴표를 사용하려면 다른 종류의 따옴표로 감싸거나 이스케이프 문자를 사용합니다.
# 이스케이프 문자(\)는 특정 문자의 특별한 기능을 없애고 일반 문자로 취급하게 합니다.
print("작은따옴표 안에 '작은따옴표' 넣기:", '그가 \'안녕\'이라고 말했다.')
print("큰따옴표 안에 '작은따옴표' 넣기:", "그가 '안녕'이라고 말했다.")

# \n: 줄바꿈, \t: 탭, \\: 역슬래시 자체
print("줄바꿈:\n두 줄에 걸쳐 출력됩니다.")
print("탭:\t앞에 탭이 들어갑니다.")
print("역슬래시 출력:", "C:\\Users\\MyFolder")

# Raw String: 문자열 앞 'r'을 붙이면 이스케이프 문자가 동작하지 않고 그대로 출력됩니다.
# 주로 파일 경로를 다룰 때 유용합니다.
raw_path = r"C:\Users\MyFolder\new_file.txt"
print("Raw String 경로:", raw_path)
print("-" * 20)


# --- 7. 자주 사용하는 문자열 함수(메서드) ---
print("--- 7. 자주 사용하는 문자열 함수(메서드) ---")

s = "hello, world!"

# len(): 문자열의 길이를 반환합니다.
print(f"문자열 '{s}'의 길이:", len(s))

# .upper(): 모든 문자를 대문자로 변환한 새 문자열을 반환합니다.
print("대문자로:", s.upper())

# .lower(): 모든 문자를 소문자로 변환한 새 문자열을 반환합니다.
print("소문자로:", "HELLO, WORLD!".lower())

# 원본 문자열은 변경되지 않습니다
print("원본 문자열 확인:", s)
print("-" * 20)


'''
    - 정리하며
        1. 문자열은 순서가 있는 문자들의 묶음이며, '', "", '''''', """"""로 생성합니다.
        2. '+' 연산자로 문자열을 합치고, '*' 연산자로 반복할 수 있습니다.
        3. 숫자와 문자열을 합칠 때는 str() 함수 또는 f-string을 사용해야 합니다. f-string이 더 편리하고 가독성이 좋습니다.
        4. 인덱싱(string[i])으로 한 글자를, 슬라이싱(string[i:j])으로 여러 글자를 추출할 수 있습니다. 인덱스는 0부터 시작합니다.
        5. 이스케이프 문자(\)는 줄바꿈(\n)이나 따옴표(\') 같은 특수 기능을 수행하며, Raw String(r'...')은 이를 무시합니다.
'''
