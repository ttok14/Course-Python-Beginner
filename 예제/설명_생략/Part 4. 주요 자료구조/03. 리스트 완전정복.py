# ====================================
# Part 4. 주요 자료구조 - 리스트 완전정복
# ====================================

print("--- 1. Mutable(가변) 특성 확인 ---")

my_string = "Hello"

my_list = ['H', 'e', 'l', 'l', 'o']
print(f"수정 전 리스트: {my_list}")
print(f"수정 전 리스트의 메모리 주소(ID): {id(my_list)}")

my_list[0] = 'Y'

print(f"수정 후 리스트: {my_list}")
print(f"수정 후 리스트의 메모리 주소(ID): {id(my_list)}")

print("\n--- 2. 혼합 자료형 저장 ---")
mixed_list = ["파이썬", 101, True, 3.14]
print(f"혼합 자료형 리스트: {mixed_list}")


print("\n--- 3. 쇼핑 리스트 실습 ---")
shopping_list = ["우유", "계란"]
print(f"초기 쇼핑 리스트: {shopping_list}")

print("\n--- 4. 인덱싱과 슬라이싱 ---")
print(f"첫 번째 항목 (인덱스 0): {shopping_list[0]}")
print(f"마지막 항목 (인덱스 -1): {shopping_list[-1]}")

shopping_list.append("빵")
shopping_list.append("사과")
print(f"항목 추가 후 리스트: {shopping_list}")
print(f"처음 두 개 항목 (슬라이싱 [:2]): {shopping_list[:2]}")

print("\n--- 5. 요소 추가 메서드 ---")

shopping_list.append("버터")
print(f"append('버터') 후: {shopping_list}")

shopping_list.insert(0, "주스")
print(f"insert(0, '주스') 후: {shopping_list}")

extras = ['과자', '치즈']
shopping_list.extend(extras)
print(f"extend(['과자', '치즈']) 후: {shopping_list}")


print("\n--- 6. 요소 삭제 메서드 ---")

last_item = shopping_list.pop()
print(f"pop()으로 꺼낸 항목: {last_item}")
print(f"pop() 실행 후 리스트: {shopping_list}")

shopping_list.append("빵")
print(f"중복 항목 '빵' 추가 후: {shopping_list}")
shopping_list.remove("빵")
print(f"remove('빵') 실행 후: {shopping_list}")


print("\n--- 7. 정렬 ---")

new_sorted_list = sorted(shopping_list)
print(f"sorted() 함수 사용 후 원본 리스트: {shopping_list}")
print(f"sorted() 함수가 반환한 새 리스트: {new_sorted_list}")

shopping_list.sort()
print(f"sort() 메서드 사용 후 원본 리스트: {shopping_list}")

shopping_list.reverse()
print(f"reverse() 메서드 사용 후: {shopping_list}")


print("\n--- 8. 기타 유용한 연산 및 함수 ---")

snacks = ['감자칩', '콜라']
full_list = shopping_list + snacks
print(f"'+' 연산자로 연결한 전체 리스트: {full_list}")

print(f"전체 항목 개수: {len(full_list)}")

has_milk = "우유" in full_list
print(f"'우유'가 리스트에 있나요? {has_milk}")

if "빵" in full_list:
    print("'빵'을 사야 합니다!")
else:
    print("'빵'은 이미 목록에 없거나 구매했습니다.")


print("\n--- 9. 최종 쇼핑 리스트 항목 순회 ---")
for item in full_list:
    print(f"- {item}")