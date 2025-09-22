# ====================================
# Part 2. 소수점 표현하기
# ====================================

print("--- 1. float 변수 생성 및 타입 확인 ---")

pi = 3.14
height = 182.5

print("원주율(pi)의 값:", pi)

print("pi 변수의 타입:", type(pi))
print("-" * 20)

print("키(height)의 값:", height)
print("height 변수의 타입:", type(height))
print("-" * 20)


print("--- 2. 정수와 float의 연산 확인 ---")

score = 100
bonus = 0.5

total_score = score + bonus

print("기본 점수(정수):", score)
print("보너스 점수(소수):", bonus)
print("최종 점수:", total_score)
print("최종 점수의 타입:", type(total_score))
print("-" * 20)


print("--- 3. 나눗셈 연산자(/)의 특징 ---")

result1 = 12 / 3
print("12 / 3 의 결과:", result1)
print("12 / 3 의 결과 타입:", type(result1))
print()

result2 = 10 / 3
print("10 / 3 의 결과:", result2)
print("10 / 3 의 결과 타입:", type(result2))
print("-" * 20)


print("--- 4. 실습 예제: 평균 점수 계산하기 ---")

korean = 95
english = 88
math = 92

total = korean + english + math

average = total / 3

print("세 과목의 총점:", total)
print("세 과목의 평균 점수는:", average)
print("-" * 20)