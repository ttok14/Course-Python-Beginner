# ====================================
# Part 4. 튜플 완전정복
# ====================================

print("--- 1. 튜플의 불변성(Immutability) ---")

my_list = [1, 2, 3]
my_list[0] = 100
print(f"리스트 수정 후: {my_list}")

my_tuple = (1, 2, 3)
# my_tuple[0] = 100
print(f"원본 튜플: {my_tuple}")
print("# 튜플의 요소를 변경하려고 하면 TypeError가 발생합니다.\n")


print("--- 2. 튜플 생성 방법 ---")

tuple1 = (1, 2, 3, 4, 5)
print(f"소괄호 사용: {tuple1}, 타입: {type(tuple1)}")

tuple2 = 6, 7, 8
print(f"소괄호 미사용: {tuple2}, 타입: {type(tuple2)}\n")


print("--- 3. 요소가 하나인 튜플 ---")

not_a_tuple = (10)
print(f"쉼표 없음: {not_a_tuple}, 타입: {type(not_a_tuple)}")

is_a_tuple = (10,)
print(f"쉼표 있음: {is_a_tuple}, 타입: {type(is_a_tuple)}\n")


print("--- 4. 튜플 연산 및 메서드 ---")

print(f"첫 번째 요소: {tuple1[0]}")
print(f"슬라이싱 (2번 인덱스부터 끝까지): {tuple1[2:]}\n")

test_tuple = ('a', 'b', 'c', 'a', 'a')

print(f"'a'의 개수: {test_tuple.count('a')}")

print(f"'c'의 위치: {test_tuple.index('c')}\n")


print("--- 5. 튜플 순회 ---")
for item in tuple1:
    print(item)
print("")


print("--- 6. 패킹과 언패킹 ---")

screen_resolution = (1920, 1080)
print(f"패킹된 튜플: {screen_resolution}")

width, height = screen_resolution
print(f"언패킹 결과 -> 너비: {width}, 높이: {height}\n")


print("--- 7. 튜플의 딕셔너리 키 활용 ---")

skill_cooldowns = {
    ('전사', '베기'): 5,
    ('마법사', '화염구'): 8,
    ('전사', '강타'): 10
}

cooldown = skill_cooldowns[('전사', '베기')]
print(f"전사 '베기' 스킬의 쿨타임: {cooldown}초")

# unhashable_dict = {['전사', '베기']: 5}