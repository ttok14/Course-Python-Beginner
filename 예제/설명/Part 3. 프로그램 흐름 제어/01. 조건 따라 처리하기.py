# ====================================
# Part 3. 조건 따라 처리하기
# ====================================

# 조건문은 특정 조건의 결과(True/False)에 따라 프로그램의 실행 흐름을 제어하는 구문입니다.
# 파이썬에서는 if, elif, else 키워드를 사용하여 조건문을 작성합니다.


# --- 1. 기본 if-else문 실습 ---
# input() 함수는 사용자로부터 텍스트를 입력받아 문자열로 반환합니다.
user_id = input("아이디를 입력하세요: ")

# user_id 변수의 값이 "admin"과 같은지 비교합니다.
if user_id == "admin":
    # 조건이 참(True)일 때 실행되는 코드 블록입니다.
    print("관리자님, 환영합니다.")
else:
    # if의 조건이 거짓(False)일 때 실행되는 코드 블록입니다.
    print("아이디가 존재하지 않습니다.")

#--- 2. if-elif-else문 실습 ---
score_str = input("점수를 입력하세요 (0-100): ")

# input()으로 받은 문자열을 숫자 비교를 위해 int() 함수로 정수형으로 변환합니다.
score = int(score_str)

# 조건을 순차적으로 검사하며, 가장 먼저 참이 되는 블록 하나만 실행됩니다.
if score >= 90:
    # 첫 번째 조건: 90점 이상
    grade = "A등급"
elif score >= 80:
    # 두 번째 조건: 90점 미만, 80점 이상
    grade = "B등급"
elif score >= 70:
    # 세 번째 조건: 80점 미만, 70점 이상
    grade = "C등급"
else:
    # 위의 모든 조건이 거짓일 경우 실행됩니다.
    grade = "D등급"
    
# f-string을 사용하여 변수와 문자열을 함께 출력합니다.
print(f"당신의 등급은 '{grade}' 입니다.")


#--- 3. 논리 연산자 및 중첩 if문 실습 ---

# 3-1) and 연산자 활용
# and 연산자는 양쪽의 조건이 모두 참(True)일 때만 전체를 True로 판단합니다.
user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")

if user_id == "admin" and user_pw == "1234":
    print("로그인 성공!")
else:
    print("로그인 실패. 아이디 또는 비밀번호를 확인하세요.")
    
    
# 3-2) 중첩 if문 활용

# if문 내부에 또 다른 if문을 사용하여 조건을 단계적으로 검사합니다.
# 이를 통해 더 구체적인 피드백을 제공할 수 있습니다.
user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")

if user_id == "admin":
    # 첫 번째 조건(아이디)이 참일 때, 내부 블록으로 진입합니다.
    if user_pw == "1234":
        # 두 번째 조건(비밀번호)도 참일 때 실행됩니다.
        print("로그인 성공!")
    else:
        # 두 번째 조건이 거짓일 때 실행됩니다.
        print("비밀번호가 틀렸습니다.")
else:
    # 첫 번째 조건이 거짓일 때 실행됩니다.
    print("존재하지 않는 아이디입니다.")


# --- 4. 불리언 및 Truthy/Falsy 활용 ---

# 4-1) 불리언(Boolean) 변수 활용
print("--- 4-1. 불리언 변수 활용 ---")
# is_vip 변수에 직접 True 또는 False를 할당하여 조건문에서 사용할 수 있습니다.
is_vip = True
if is_vip:  # 'is_vip == True' 와 동일한 의미입니다.
    print("VIP 고객님, 특별 할인이 적용됩니다.")
else:
    print("일반 고객님, 환영합니다.")

print("-" * 20)

# 4-2) Falsy 활용 예시
print("--- 4-2. Falsy 활용 예시 ---")
# 내용이 없는 빈 문자열('')은 Falsy 값으로 취급되어, 조건문에서 False로 평가됩니다.
# 'if user_input_falsy == ""' 보다 간결한 코드입니다.
user_input_falsy = ""

if user_input_falsy:
    # 이 블록은 user_input_falsy에 내용이 있을 때(Truthy)만 실행됩니다.
    print(f"입력된 내용: {user_input_falsy}")
else:
    # user_input_falsy가 비어있으므로(Falsy), 이 블록이 실행됩니다.
    print("입력된 내용이 없습니다.")

print("-" * 20)

# 4-3) Truthy 활용 예시
print("--- 4-3. Truthy 활용 예시 ---")
# 내용이 있는 문자열은 Truthy 값으로 취급되어, 조건문에서 True로 평가됩니다.
user_input_truthy = "hello"

if user_input_truthy:
    # user_input_truthy에 내용이 있으므로(Truthy), 이 블록이 실행됩니다.
    print(f"입력된 내용: {user_input_truthy}")
else:
    # 이 블록은 실행되지 않습니다.
    print("입력된 내용이 없습니다.")

'''
    - 정리하며
        1. 조건문은 특정 조건의 결과(True/False)에 따라 프로그램의 실행 흐름을 다르게 제어하는 구문입니다.
        2. 'if'는 조건이 참일 때, 'else'는 앞선 조건이 모두 거짓일 때, 'elif'는 여러 조건을 순서대로 검사할 때 사용합니다.
        3. 'if 조건식:' 과 같이 콜론(:)을 반드시 사용해야 하며, 콜론 다음의 코드 블록은 반드시 들여쓰기를 해야 합니다.
        4. 조건식에는 비교/논리 연산자 뿐만 아니라, Truthy(참 같은 값)와 Falsy(거짓 같은 값)를 활용하여 코드를 간결하게 만들 수 있습니다.
        5. Falsy 값의 대표적인 예로는 숫자 0, 빈 문자열(""), 빈 리스트([]) 등이 있으며, '비어있는 것은 거짓이다'로 기억하면 유용합니다.
'''