# ====================================
# Part 3. 왈러스(Walrus) 로 간결하게 처리하기
# ====================================

print("--- 1. 왈러스 연산자 기본 동작 ---")

if (x := 10) > 5:
    print(f"x는 {x}이고, 5보다 큽니다.")

print("-" * 20)


print("\n--- 2. while 문 리팩토링 ---")

print("[개선 전 코드]")


print("[개선 후 코드] - 아래 주석을 해제하고 실행해보세요.")

print("-" * 20)


print("\n--- 3. if 문에서 활용하기 ---")

if (age := int(input("나이를 숫자로 입력하세요: "))) >= 19:
    print(f"당신의 나이는 {age}세, 성인입니다.")
else:
    print(f"당신의 나이는 {age}세, 미성년입니다.")

print("-" * 20)


print("\n--- 4. 왈러스 연산자 사용 가이드라인 ---")

text_input = "파이썬은 정말 재미있어요"
print(f"입력된 텍스트: '{text_input}'")
if (text := text_input) and len(text) > 10:
    print(f"입력된 텍스트 '{text}'의 길이는 10을 초과합니다.")
else:
    print("입력된 텍스트의 길이는 10 이하입니다.")

print("-" * 10)

price = 10000
quantity = 2

subtotal = price * quantity
tax = subtotal * 0.1
total = subtotal + tax
print(f"중간 합계: {subtotal}, 세금: {tax}")
print(f"총액 (좋은 예): {total}")
