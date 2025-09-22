# ====================================
# Part 2. 논리 연산
# ====================================

print("--- 1. and 연산자 (그리고) ---")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and False:", False and False)


print("\n--- 2. or 연산자 (또는) ---")
print("True or False:", True or False)
print("False or False:", False or False)


print("\n--- 3. not 연산자 (반대) ---")
print("not True:", not True)
print("not False:", not False)
print("not (10 > 5):", not (10 > 5))


print("\n--- 4. 논리 연산자 활용 예제 ---")
age = 25
height = 180

print(f"현재 나이: {age}, 현재 키: {height}")

can_ride = age >= 20 and height >= 160
print("놀이기구 탑승 가능 여부:", can_ride)

is_discounted = age < 10 or age >= 65
print("할인 대상 여부:", is_discounted)


print("\n--- 5. 괄호()와 연산 우선순위 ---")
result1 = False and False or True
print("False and False or True 의 결과:", result1)

result2 = False and (False or True)
print("False and (False or True) 의 결과:", result2)

print("=> 괄호의 유무에 따라 결과가 완전히 달라짐을 확인할 수 있습니다.")