# ====================================
# Part 3. 조건 따라 처리하기
# ====================================

user_id = input("아이디를 입력하세요: ")

if user_id == "admin":
    print("관리자님, 환영합니다.")
else:
    print("아이디가 존재하지 않습니다.")

score_str = input("점수를 입력하세요 (0-100): ")

score = int(score_str)

if score >= 90:
    grade = "A등급"
elif score >= 80:
    grade = "B등급"
elif score >= 70:
    grade = "C등급"
else:
    grade = "D등급"
    
print(f"당신의 등급은 '{grade}' 입니다.")


user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")

if user_id == "admin" and user_pw == "1234":
    print("로그인 성공!")
else:
    print("로그인 실패. 아이디 또는 비밀번호를 확인하세요.")
    
    
user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")

if user_id == "admin":
    if user_pw == "1234":
        print("로그인 성공!")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("존재하지 않는 아이디입니다.")


print("--- 4-1. 불리언 변수 활용 ---")
is_vip = True
if is_vip:
    print("VIP 고객님, 특별 할인이 적용됩니다.")
else:
    print("일반 고객님, 환영합니다.")

print("-" * 20)

print("--- 4-2. Falsy 활용 예시 ---")
user_input_falsy = ""

if user_input_falsy:
    print(f"입력된 내용: {user_input_falsy}")
else:
    print("입력된 내용이 없습니다.")

print("-" * 20)

print("--- 4-3. Truthy 활용 예시 ---")
user_input_truthy = "hello"

if user_input_truthy:
    print(f"입력된 내용: {user_input_truthy}")
else:
    print("입력된 내용이 없습니다.")