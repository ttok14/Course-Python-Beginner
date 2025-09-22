# ====================================
# Part 3. 예외 처리하기
# ====================================

# 예외(Exception)는 프로그램 실행 중 발생하는 예상치 못한 오류를 의미합니다.
# 예외 처리는 이러한 오류가 발생해도 프로그램이 중단되지 않고,
# 미리 정해둔 대안적인 코드를 실행하도록 만드는 중요한 기법입니다.

# --- 1. 예외가 발생하는 상황 ---
print("--- 1. 예외가 발생하는 상황 ---")

# 사용자에게 나이를 입력받아 숫자로 변환하는 코드입니다.
# 만약 사용자가 숫자가 아닌 '서른'과 같은 문자를 입력하면,
# int() 함수가 이를 숫자로 변환할 수 없어 ValueError가 발생합니다.
# 예외 처리가 없으면 프로그램은 이 지점에서 즉시 종료됩니다.

# 아래 코드의 주석을 해제하고 '서른'이라고 입력하여 테스트해볼 수 있습니다.
# age_str = input("나이를 숫자로 입력하세요: ")
# age = int(age_str) # 여기서 ValueError 발생 가능성이 있습니다.
# print(f"당신의 나이는 {age}살입니다.")
# print("-" * 20)


# --- 2. 기본적인 예외 처리: try-except ---
print("\n--- 2. 기본적인 예외 처리: try-except ---")

# try 블록: 예외가 발생할 가능성이 있는 코드를 이 안에 넣습니다.
# except 블록: try 블록에서 예외가 발생했을 때 실행할 코드를 넣습니다.
try:
    age_str = input("나이를 숫자로 입력하세요: ")
    age = int(age_str)
    print(f"당신의 나이는 {age}살입니다.")
# ValueError as e: try 블록에서 ValueError가 발생하면 이 블록을 실행합니다.
# 'as e'는 발생한 예외 객체를 변수 e에 저장하여 오류 메시지를 확인할 수 있게 합니다.
except ValueError as e:
    print("오류: 숫자로만 입력해야 합니다.")
    print(f"파이썬이 알려준 오류 메시지: {e}")


# --- 3. 여러 종류의 예외 처리하기 ---
print("\n--- 3. 여러 종류의 예외 처리하기 ---")

# 하나의 try 블록에 여러 종류의 예외가 발생할 수 있습니다.
# 예를 들어, 나눗셈 계산기는 문자를 입력하면 ValueError가, 0으로 나누면 ZeroDivisionError가 발생할 수 있습니다.
# 이 경우, 각 예외에 맞는 별도의 except 블록을 만들어 처리할 수 있습니다.
try:
    num1_str = input("나눌 숫자를 입력하세요: ")
    num2_str = input("나뉠 숫자를 입력하세요: ")
    
    num1 = int(num1_str) # ValueError 발생 가능 지점
    num2 = int(num2_str) # ValueError 발생 가능 지점
    
    result = num1 / num2 # ZeroDivisionError 발생 가능 지점
    
    print(f"결과: {result}")

except ZeroDivisionError as e:
    print(f"0으로 나눌 수 없습니다. (오류: {e})")
except ValueError as e:
    print(f"숫자만 입력해야 합니다. (오류: {e})")


# --- 4. 예외 처리 구조 완성: else와 finally ---
print("\n--- 4. else와 finally ---")

# else: try 블록에서 예외가 발생하지 않았을 때만 실행됩니다.
# finally: 예외 발생 여부와 상관없이 항상 마지막에 실행됩니다.
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
    # 예외가 발생하지 않고 try 블록이 성공적으로 실행되었을 때만 이 코드가 실행됩니다.
    print(f"결과: {result}")
finally:
    # 성공하든, 실패하든 상관없이 항상 실행됩니다.
    # 주로 파일 닫기, 데이터베이스 연결 해제 등 마무리 작업에 사용됩니다.
    print("계산 시도가 완료되었습니다.")


# --- 5. 실용적인 예외 처리 패턴: while 루프와 함께 사용하기 ---
print("\n--- 5. 올바른 값을 입력할 때까지 반복하기 ---")

# while True 무한 루프와 예외 처리를 결합하면,
# 사용자가 올바른 값을 입력할 때까지 계속해서 입력을 요청하는 견고한 코드를 만들 수 있습니다.
while True:
    try:
        age_str = input("나이를 숫자로 입력하세요 (종료하려면 'q'): ")
        
        # 사용자가 'q'를 입력하면 루프를 종료합니다.
        if age_str == 'q':
            break
            
        age = int(age_str) # 여기서 ValueError가 발생하면 except 블록으로 점프합니다.

    except ValueError as e:
        # 오류 발생 시 사용자에게 알리고 continue를 통해 루프의 처음으로 돌아갑니다.
        print(f"오류: {e}. 다시 시도해주세요.")
        continue
    else:
        # 예외 없이 성공적으로 나이를 입력받았을 경우
        print(f"입력하신 나이는 {age}살입니다.")
        break # break를 통해 무한 루프를 탈출합니다.

print("프로그램을 종료합니다.")


'''
    - 정리하며
        1. 예외(Exception)는 프로그램 실행 중에 발생하는 오류로, 처리하지 않으면 프로그램이 비정상적으로 종료됩니다.
        2. 'try-except' 구문은 예외를 '처리'하여 프로그램이 중단되는 것을 막아줍니다.
        3. 'try' 블록에는 예외 발생 가능 코드를, 'except' 블록에는 예외 발생 시 실행할 코드를 작성합니다.
        4. 'except 예외종류 as e' 형태로 작성하면, 특정 예외만 잡아서 처리하고 오류 메시지(e)도 확인할 수 있습니다.
        5. 'else'는 예외가 없을 때, 'finally'는 예외 발생 여부와 상관없이 항상 실행되어야 할 코드를 작성할 때 사용합니다.
        6. [핵심] 예외 처리는 견고하고 사용자 친화적인 프로그램을 만들기 위한 필수적인 설계 요소입니다.
'''