# ====================================
# Part 2. 논리 연산
# ====================================

# 논리 연산은 여러 개의 참/거짓(bool) 값을 조합하여
# 하나의 최종 결론을 내리는 방법입니다.
# and, or, not 세 가지 대표적인 논리 연산자가 있습니다.

print("--- 1. and 연산자 (그리고) ---")
# 'and' 연산자는 두 조건이 '모두' True일 때만 최종 결과가 True가 됩니다.
# 마치 로그인을 할 때 아이디와 비밀번호가 둘 다 맞아야만 성공하는 것과 같습니다.

# True와 True를 and로 연결하면 결과는 True입니다.
print("True and True:", True and True)

# 하나라도 False가 포함되면 결과는 False가 됩니다.
print("True and False:", True and False)

# 양쪽 모두 False라면 결과는 당연히 False입니다.
print("False and False:", False and False)


print("\n--- 2. or 연산자 (또는) ---")
# 'or' 연산자는 두 조건 중 '하나라도' True이면 최종 결과가 True가 됩니다.
# 쇼핑몰에서 신용카드 '또는' 계좌이체 중 하나로 결제하는 상황과 같습니다.

# 하나라도 True가 포함되면 결과는 True입니다.
print("True or False:", True or False)

# 양쪽 모두 False일 때만 결과가 False가 됩니다.
print("False or False:", False or False)


print("\n--- 3. not 연산자 (반대) ---")
# 'not' 연산자는 기존의 bool 값을 반대로 뒤집는 역할을 합니다.

# not True는 False가 됩니다.
print("not True:", not True)
print("not False:", not False)

# 비교 연산의 결과에 적용할 수도 있습니다.
# (10 > 5)는 True이므로, not을 붙이면 False가 됩니다.
print("not (10 > 5):", not (10 > 5))


print("\n--- 4. 논리 연산자 활용 예제 ---")
# 변수를 사용하여 좀 더 현실적인 예제를 확인합니다.
age = 25
height = 180

print(f"현재 나이: {age}, 현재 키: {height}")

# 예제 1: 놀이기구 탑승 조건 (나이가 20살 이상 '이고' 키가 160 이상)
can_ride = age >= 20 and height >= 160
print("놀이기구 탑승 가능 여부:", can_ride)

# 예제 2: 할인 조건 (나이가 10살 미만 '이거나' 65살 이상)
is_discounted = age < 10 or age >= 65
print("할인 대상 여부:", is_discounted)


print("\n--- 5. 괄호()와 연산 우선순위 ---")
# 논리 연산은 not, and, or 순서로 계산되지만, 괄호를 사용해 순서를 명확히 하는 것이 좋습니다.

# 괄호가 없는 경우: and가 or보다 먼저 계산됩니다.
# (False and False)가 먼저 계산되어 False가 되고,
# 남은 False or True 는 최종적으로 True가 됩니다.
result1 = False and False or True
print("False and False or True 의 결과:", result1)

# 괄호가 있는 경우: 괄호 안이 먼저 계산됩니다.
# (False or True)가 먼저 계산되어 True가 되고,
# 남은 False and True 는 최종적으로 False가 됩니다.
result2 = False and (False or True)
print("False and (False or True) 의 결과:", result2)

print("=> 괄호의 유무에 따라 결과가 완전히 달라짐을 확인할 수 있습니다.")


'''
    - 정리하며
        1. 'and' 연산자: 연결된 모든 조건이 True일 때만 최종 결과가 True입니다. (모두 참이어야 참)
        2. 'or' 연산자: 연결된 조건 중 하나라도 True이면 최종 결과가 True입니다. (하나라도 참이면 참)
        3. 'not' 연산자: 기존의 bool 값을 반대로 뒤집습니다. (True -> False, False -> True)
        4. 논리 연산자는 비교 연산자와 조합하여 더 복잡하고 현실적인 조건을 만들 수 있습니다.
        5. 연산 순서가 헷갈릴 수 있으므로, 괄호()를 사용하여 계산 순서를 명확히 지정하는 것이 좋은 습관입니다.
'''