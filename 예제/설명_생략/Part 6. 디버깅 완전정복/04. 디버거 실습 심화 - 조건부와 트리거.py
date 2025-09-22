# ====================================
# Part 6. 디버거 실습 심화 - 조건부와 트리거
# ====================================

print("--- 1. 조건부 브레이크 포인트 (Conditional Breakpoint) 실습 ---")

def check_numbers():
    for i in range(1, 11):
        print(f"현재 숫자: {i}")
    print("숫자 확인 완료.")

check_numbers()

print("\n" + "="*50 + "\n")


print("--- 2. 트리거된 브레이크 포인트 (Triggered Breakpoint) 실습 ---")

def prepare_data():
    print("데이터 준비 완료.")

def process_data():
    print("데이터 처리 시작.")

print("첫 번째 호출: prepare_data() 실행 전")
process_data()
print("-" * 20)


print("두 번째 호출: prepare_data() 실행 후")
prepare_data()
process_data()

print("\n실습 완료.")
