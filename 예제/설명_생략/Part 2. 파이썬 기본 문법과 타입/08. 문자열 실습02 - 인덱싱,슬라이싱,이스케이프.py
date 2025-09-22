# ==========================================================
# Part 2. 문자열 실습02 - 인덱싱,슬라이싱,이스케이프
# ==========================================================

print("--- 1. 인덱싱(Indexing) ---")

word = 'Python'

print(f"'{word}'의 0번 인덱스: {word[0]}")
print(f"'{word}'의 1번 인덱스: {word[1]}")
print(f"'{word}'의 5번 인덱스: {word[5]}")
print("\n")

print(f"'{word}'의 -1번 인덱스: {word[-1]}")
print(f"'{word}'의 -2번 인덱스: {word[-2]}")
print("\n")

sentence = 'Hello World'
print(f"'{sentence}'의 0번 인덱스: {sentence[0]}")
print(f"'{sentence}'의 6번 인덱스: {sentence[6]}")
print("\n")


print("--- 2. 슬라이싱(Slicing) ---")

text = 'Programming'

print(f"'{text}'[0:4]: {text[0:4]}")
print(f"'{text}'[4:7]: {text[4:7]}")
print("\n")

print(f"'{text}'[:4]: {text[:4]}")
print(f"'{text}'[4:]: {text[4:]}")
print(f"'{text}'[-4:]: {text[-4:]}")
print("\n")


email = 'user@naver.com'

at_index = email.find('@')
print(f"'@' 문자의 위치: {at_index}")

username = email[:at_index]
domain = email[at_index + 1:]

print(f"원본 이메일: {email}")
print(f"사용자 이름: {username}")
print(f"도메인: {domain}")
print("\n")


print("--- 3. 이스케이프와 Raw String ---")

print("Hello\nWorld")

print("첫 번째 줄\n두 번째 줄\t탭으로 들여쓰기")

print('I\'m learning Python.')
print("I'm learning Python.")
print("\n")


file_path1 = 'C:\\Users\\Python\\Documents'
print(f"일반 문자열 경로: {file_path1}")

file_path2 = r'C:\Users\Python\Documents'
print(f"Raw String 경로: {file_path2}")
print("\n")