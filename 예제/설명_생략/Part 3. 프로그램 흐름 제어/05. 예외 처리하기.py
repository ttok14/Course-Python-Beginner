# ====================================
# Part 3. 예외 처리하기
# ====================================

print("--- 1. 예외가 발생하는 상황 ---")

# age_str = input("나이를 숫자로 입력하세요: ")
# age = int(age_str)
# print(f"당신의 나이는 {age}살입니다.")
# print("-" * 20)


print("\n--- 2. 기본적인 예외 처리: try-except ---")

try:
    age_str = input("나이를 숫자로 입력하세요: ")
    age = int(age_str)
    print(f"당신의 나이는 {age}살입니다.")
except ValueError as e:
    print("오류: 숫자로만 입력해야 합니다.")
    print(f"파이썬이 알려준 오류 메시지: {e}")


print("\n--- 3. 여러 종류의 예외 처리하기 ---")

try:
    num1_str = input("나눌 숫자를 입력하세요: ")
    num2_str = input("나뉠 숫자를 입력하세요: ")
    
    num1 = int(num1_str)
    num2 = int(num2_str)
    
    result = num1 / num2
    
    print(f"결과: {result}")

except ZeroDivisionError as e:
    print(f"0으로 나눌 수 없습니다. (오류: {e})")
except ValueError as e:
    print(f"숫자만 입력해야 합니다. (오류: {e})")


print("\n--- 4. else와 finally ---")

try:
    num1_str = input("나눌 숫자를 입력하세요: ")
    num2_str = input("나뉠 숫자를 입력하세요: ")
    
    num1 = int(num1_str)
    num2 = int(num2_str)
    
    result = num1 / num2

except ValueError as e:
    print(f"오류: 숫자만 입력해야 합니다. (오류: {e})")
except ZeroDivisionError as e:
    print(f"오류: 0으로 나눌 수 없습니다. (오류: {e})")
else:
    print(f"결과: {result}")
finally:
    print("계산 시도가 완료되었습니다.")


print("\n--- 5. 올바른 값을 입력할 때까지 반복하기 ---")

while True:
    try:
        age_str = input("나이를 숫자로 입력하세요 (종료하려면 'q'): ")
        
        if age_str == 'q':
            break
            
        age = int(age_str)

    except ValueError as e:
        print(f"오류: {e}. 다시 시도해주세요.")
        continue
    else:
        print(f"입력하신 나이는 {age}살입니다.")
        break

print("프로그램을 종료합니다.")
