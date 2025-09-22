# ====================================
# Part 3.조건부 반복과 제어
# ====================================

print("--- 1. break 예제 ---")

for i in range(1, 21):
    if i == 13:
        print("13을 발견했습니다. 반복을 중단합니다.")
        break

    print(i)

print("반복문이 종료되었습니다.\n")


print("--- 2. continue 예제 ---")

for i in range(1, 11):
    if i == 5:
        print("(5는 건너뜁니다.)")
        continue

    print(f"현재 숫자는 {i}입니다.")

print("반복문이 종료되었습니다.\n")


print("--- 3. while True와 break 활용 예제 ---")

# while True:
#     agreement = input("약관에 동의하십니까? (동의하려면 '동의합니다' 입력): ")

#     if agreement == '동의합니다':
#         print("회원가입에 동의하셨습니다. 다음 단계를 진행합니다.")
#         break
#     else:
#         print("약관에 동의해야만 회원가입을 진행할 수 있습니다.")

print("사용자 동의 확인 절차가 끝났습니다. (예제 실행을 위해 코드는 주석 처리됨)\n")


print("--- 4. continue 활용한 데이터 필터링 예제 ---")

scores = [88, 95, 70, -5, 100, 55]
total_score = 0

for score in scores:
    if score < 0 or score > 100:
        print(f"유효하지 않은 점수 발견: {score} (처리하지 않음)")
        continue

    total_score += score
    print(f"현재 점수: {score}, 현재까지 합계: {total_score}")

print(f"\n최종 유효 점수 합계: {total_score}")