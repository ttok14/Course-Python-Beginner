# ====================================
# Part 3. 반복 작업 처리하기
# ====================================

print("--- 1. for 문 기본 ---")
for i in range(5):
    print("환영합니다!")

print("\n--- 반복 변수 i의 값 확인 ---")
for i in range(5):
    print(i)

print("\n--- 2. range() 함수 심화: 시작과 끝 지정 ---")
print("1부터 10까지 출력:")
for i in range(1, 11):
    print(i, end=' ')

print("\n\n0부터 8까지 짝수만 출력:")
for i in range(0, 10, 2):
    print(i, end=' ')
print("\n")

print("\n--- 3. 문자열 한 글자씩 출력 ---")
for char in '파이썬':
    print(char)

print("\n--- 4. 1부터 10까지의 합계 구하기 ---")
total = 0
for i in range(1, 11):
    total = total + i
    print(f"i={i}, 현재 total={total}")

print(f"1부터 10까지의 최종 합계: {total}")

print("\n--- 5. while 문 기본: 카운트다운 ---")
count = 5
while count > 0:
    print(f"카운트다운: {count}")
    count = count - 1

print("발사!")

print("\n--- 6. 숫자 맞추기 게임 ---")
answer = 5
running = True
attempts = 0

while running:
    attempts += 1
    
    guess = int(input(f"시도 {attempts}번째: 1부터 10 사이의 숫자를 맞춰보세요: "))

    if guess == answer:
        print(f"정답입니다! {attempts}번 만에 맞춰내셨네요!")
        running = False
    else:
        print(f"틀렸습니다. 입력하신 숫자: {guess}, 다시 시도하세요.")
