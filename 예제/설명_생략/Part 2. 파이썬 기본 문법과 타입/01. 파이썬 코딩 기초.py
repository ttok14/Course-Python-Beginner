# ====================================
# Part 2. 파이썬 기본 문법과 타입 - 파이썬 코딩 기초
# ====================================

print("--- 1. 변수와 할당 ---")

score = 100
level = 5

print(score)
print(level)

print("\n--- 변수 값 변경 ---")
score = 80
print(score)

score = 95
print(score)


print("\n--- 2. 변수 이름 규칙 ---")

player_level = 10
user_name = "python_user"
player1_score = 100
_private_data = "비밀 정보"

print(player_level)
print(user_name)


print("\n--- 3. 주석 ---")

player_name = "Alice"
print(player_name)


print("\n--- 4. 들여쓰기 ---")

if 10 > 5:
    print("if 구문 안쪽: 10은 5보다 큽니다.")
    print("if 구문 안쪽: 이 줄도 같은 수준으로 들여쓰기 되었습니다.")

if 10 > 5:
    print("첫 번째 줄은 들여쓰기가 4칸입니다.")

print("들여쓰기 예시가 끝났습니다.")