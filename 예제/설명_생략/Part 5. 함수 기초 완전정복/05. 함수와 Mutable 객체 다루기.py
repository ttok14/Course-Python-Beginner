# ====================================
# Part 5. 함수와 Mutable 객체 다루기
# ====================================

print("--- 1. 함수의 부작용 (Side Effect) ---")

numbers_original = [10, 20, 30]

def modify_list(a_list):
    print(f"  (함수 안) 수정 전 리스트: {a_list}")
    a_list.append(99)
    print(f"  (함수 안) 수정 후 리스트: {a_list}")

print(f"함수 호출 전 원본: {numbers_original}")
modify_list(numbers_original)
print(f"함수 호출 후 원본: {numbers_original}")

print("\n" + "="*50 + "\n")


print("--- 2. id()로 참조 전달 증명하기 ---")

numbers_for_id_check = [10, 20, 30]

def check_id(a_list):
    print(f"  (함수 안) 전달받은 인자의 ID: {id(a_list)}")

print(f"함수 호출 전 원본의 ID: {id(numbers_for_id_check)}")
check_id(numbers_for_id_check)

print("\n" + "="*50 + "\n")


print("--- 3. 방어적 복사로 부작용 해결하기 ---")

def modify_list_safe(a_list):
    new_list = a_list.copy()
    new_list.append(99)
    return new_list

numbers_to_protect = [10, 20, 30]

print(f"함수 호출 전 원본: {numbers_to_protect}")
result = modify_list_safe(numbers_to_protect)

print(f"함수 호출 후 원본: {numbers_to_protect}")
print(f"함수가 반환한 결과: {result}")

print("\n" + "="*50 + "\n")


print("--- 4. Mutable 기본값의 함정 ---")

def add_to_list_buggy(value, target=[]):
    target.append(value)
    print(f"  ID: {id(target)}, 현재 리스트: {target}")

print("첫 번째 호출:")
add_to_list_buggy(1)

print("-" * 20)

print("두 번째 호출:")
add_to_list_buggy(2)

print("\n" + "="*50 + "\n")


print("--- 5. 올바른 기본값 사용 패턴 (None 패턴) ---")

def add_to_list_safe(value, target=None):
    if target is None:
        target = []
    
    target.append(value)
    print(f"  ID: {id(target)}, 현재 리스트: {target}")

print("첫 번째 호출:")
add_to_list_safe(1)

print("-" * 20)

print("두 번째 호출:")
add_to_list_safe(2)