# ====================================
# Part 4. 주요 자료구조 - 리스트 완전정복
# ====================================

# 리스트(List)는 여러 개의 데이터를 순서대로 담을 수 있는 가변(Mutable)형 컨테이너입니다.
# 즉, 생성 후에도 내용물을 자유롭게 추가, 수정, 삭제할 수 있습니다.

# --- 1. Mutable(가변) 특성 확인: 문자열과의 비교 ---
print("--- 1. Mutable(가변) 특성 확인 ---")

# Immutable(불변) 객체인 문자열
my_string = "Hello"
# my_string[0] = 'Y'  # 이 코드는 TypeError를 발생시킵니다. 문자열은 수정이 불가능합니다.

# Mutable(가변) 객체인 리스트
my_list = ['H', 'e', 'l', 'l', 'o']
print(f"수정 전 리스트: {my_list}")
print(f"수정 전 리스트의 메모리 주소(ID): {id(my_list)}")

# 리스트의 첫 번째 요소를 'Y'로 변경합니다.
my_list[0] = 'Y'

print(f"수정 후 리스트: {my_list}")
print(f"수정 후 리스트의 메모리 주소(ID): {id(my_list)}")
# 결과: 리스트의 내용은 바뀌었지만, 메모리 주소는 동일합니다.
# 이는 리스트 객체 자체가 제자리에서 수정되었음을 의미합니다.

# --- 2. 혼합 자료형 저장 ---
print("\n--- 2. 혼합 자료형 저장 ---")
mixed_list = ["파이썬", 101, True, 3.14]
print(f"혼합 자료형 리스트: {mixed_list}")
# 리스트는 숫자, 문자, 불리언 등 어떤 종류의 데이터든 함께 담을 수 있습니다.


# --- 3. 리스트 조작 실습을 위한 쇼핑 리스트 생성 ---
print("\n--- 3. 쇼핑 리스트 실습 ---")
shopping_list = ["우유", "계란"]
print(f"초기 쇼핑 리스트: {shopping_list}")

# --- 4. 인덱싱과 슬라이싱 ---
print("\n--- 4. 인덱싱과 슬라이싱 ---")
print(f"첫 번째 항목 (인덱스 0): {shopping_list[0]}")
print(f"마지막 항목 (인덱스 -1): {shopping_list[-1]}")

# 슬라이싱을 위해 항목 추가
shopping_list.append("빵")
shopping_list.append("사과")
print(f"항목 추가 후 리스트: {shopping_list}")
print(f"처음 두 개 항목 (슬라이싱 [:2]): {shopping_list[:2]}") # 인덱스 0부터 2 직전(1)까지

# --- 5. 요소 추가 메서드 ---
print("\n--- 5. 요소 추가 메서드 ---")

# 5-1. append(): 리스트의 맨 뒤에 요소 하나를 추가합니다.
shopping_list.append("버터")
print(f"append('버터') 후: {shopping_list}")

# 5-2. insert(): 지정한 인덱스 위치에 요소를 삽입합니다.
shopping_list.insert(0, "주스") # 0번 인덱스에 '주스' 삽입
print(f"insert(0, '주스') 후: {shopping_list}")

# 5-3. extend(): 다른 리스트(iterable)의 모든 요소를 현재 리스트 뒤에 추가합니다.
extras = ['과자', '치즈']
shopping_list.extend(extras)
print(f"extend(['과자', '치즈']) 후: {shopping_list}")


# --- 6. 요소 삭제 메서드 ---
print("\n--- 6. 요소 삭제 메서드 ---")

# 6-1. pop(): 특정 인덱스의 요소를 꺼내서 반환하고, 리스트에서는 삭제합니다.
# 인덱스를 지정하지 않으면 마지막 요소를 꺼냅니다.
last_item = shopping_list.pop()
print(f"pop()으로 꺼낸 항목: {last_item}")
print(f"pop() 실행 후 리스트: {shopping_list}")

# 6-2. remove(): 특정 값을 찾아 삭제합니다.
# 동일한 값이 여러 개 있을 경우, 가장 앞에 있는 값 하나만 삭제합니다.
shopping_list.append("빵") # 'remove' 시연을 위해 중복 항목 추가
print(f"중복 항목 '빵' 추가 후: {shopping_list}")
shopping_list.remove("빵")
print(f"remove('빵') 실행 후: {shopping_list}")


# --- 7. 정렬: sort() 메서드 vs sorted() 함수 ---
print("\n--- 7. 정렬 ---")

# 7-1. sorted() 함수: 원본 리스트는 그대로 두고, 정렬된 '새로운' 리스트를 반환합니다.
new_sorted_list = sorted(shopping_list)
print(f"sorted() 함수 사용 후 원본 리스트: {shopping_list}") # 원본은 변경되지 않음
print(f"sorted() 함수가 반환한 새 리스트: {new_sorted_list}")

# 7-2. sort() 메서드: '원본' 리스트 자체를 정렬합니다. 반환 값은 None입니다.
shopping_list.sort()
print(f"sort() 메서드 사용 후 원본 리스트: {shopping_list}") # 원본이 직접 변경됨

# 7-3. reverse() 메서드: 원본 리스트의 순서를 거꾸로 뒤집습니다.
shopping_list.reverse()
print(f"reverse() 메서드 사용 후: {shopping_list}")


# --- 8. 기타 유용한 연산 및 함수 ---
print("\n--- 8. 기타 유용한 연산 및 함수 ---")

# 8-1. 리스트 연결 (+ 연산자): 두 리스트를 합쳐 '새로운' 리스트를 생성합니다.
snacks = ['감자칩', '콜라']
full_list = shopping_list + snacks
print(f"'+' 연산자로 연결한 전체 리스트: {full_list}")

# 8-2. len() 함수: 리스트의 길이(요소의 개수)를 반환합니다.
print(f"전체 항목 개수: {len(full_list)}")

# 8-3. 'in' 연산자: 특정 값이 리스트에 포함되어 있는지 확인합니다. (True/False 반환)
has_milk = "우유" in full_list
print(f"'우유'가 리스트에 있나요? {has_milk}")

# 'in' 연산자는 if 문과 함께 자주 사용됩니다.
if "빵" in full_list:
    print("'빵'을 사야 합니다!")
else:
    print("'빵'은 이미 목록에 없거나 구매했습니다.")


# --- 9. for 문을 이용한 리스트 순회(Iteration) ---
print("\n--- 9. 최종 쇼핑 리스트 항목 순회 ---")
# for 문을 사용하면 리스트의 모든 항목에 대해 반복적으로 작업을 수행할 수 있습니다.
for item in full_list:
    print(f"- {item}")


'''
    - 정리하며
        1. 리스트는 대괄호 `[]`를 사용해 생성하며, '가변(Mutable)' 객체입니다. 즉, 생성 후에도 내용 변경이 가능합니다.
        2. 리스트의 수정(`my_list[0] = ...`)은 원본 객체의 메모리 주소를 바꾸지 않고 내부 값만 변경합니다.
        3. 요소 추가에는 `append()`, `insert()`, `extend()`가 있으며, 각각의 동작 방식에 차이가 있습니다.
        4. 요소 삭제에는 `pop()`(인덱스 기반), `remove()`(값 기반)가 있습니다.
        5. 정렬 시 `sort()` 메서드는 원본을 직접 수정하고, `sorted()` 함수는 정렬된 새 리스트를 반환합니다.
        6. `len()`, `+`, `in` 등 다양한 내장 함수와 연산자를 활용할 수 있습니다.
        7. `for` 반복문을 통해 리스트의 모든 요소를 순차적으로 접근하고 처리하는 것은 매우 중요한 패턴입니다.
'''