# ====================================
# Part 4.얕은복사와 깊은복사
# ====================================

print("=== 1. immutable 데이터는 복사가 필요없습니다 ===")
my_sister_age = 15
my_brother_age = my_sister_age

print(f"여동생 나이: {my_sister_age}")
print(f"남동생 나이: {my_brother_age}")
print(f"두 변수는 같은 객체를 가리킵니다: id={id(my_sister_age)} == id={id(my_brother_age)}")
print("-" * 20)

my_brother_age = 20

print(f"남동생 나이 변경 후 - 여동생: {my_sister_age}, 남동생: {my_brother_age}")
print(f"이제 두 변수는 다른 객체를 가리킵니다: id={id(my_sister_age)} != id={id(my_brother_age)}")


print("\n=== 2. mutable의 문제점 (복사가 아닌 단순 할당) ===")
monster01_info = ['원거리 미니언', '20']
monster02_info = monster01_info

print(f"원본: {monster01_info}")
print(f"할당본: {monster02_info}")
print(f"두 변수는 같은 객체입니다: {id(monster01_info) == id(monster02_info)}")
print("-" * 20)

monster02_info[0] = '근거리 미니언'

print(f"할당본 수정 후 - 원본: {monster01_info}")
print(f"할당본 수정 후 - 할당본: {monster02_info}")


print("\n=== 3. 얕은 복사 (Shallow Copy) 로 해결하기 ===")
monster01_info = ['원거리 미니언', '20']
monster02_info = monster01_info.copy()

print(f"이제 두 변수는 다른 객체입니다: {id(monster01_info) != id(monster02_info)}")
print("-" * 20)

monster02_info[0] = '근거리 미니언'

print(f"복사본 수정 후 - 원본: {monster01_info}")
print(f"복사본 수정 후 - 복사본: {monster02_info}")


print("\n=== 4. 얕은 복사의 한계 (중첩 구조) ===")
monster01_info = ['원거리 미니언', [20, 10]]
monster02_info = monster01_info.copy()

print(f"바깥 리스트는 다른 객체인가? : {id(monster01_info) != id(monster02_info)}")
print(f"안쪽 리스트는 같은 객체인가? : {id(monster01_info[1]) == id(monster02_info[1])}")
print("-" * 20)

monster02_info[1][0] = 30

print(f"복사본의 내부 리스트만 수정했는데...")
print(f"원본 스탯: {monster01_info}")
print(f"복사본 스탯: {monster02_info}")


print("\n=== 5. 깊은 복사 (Deep Copy) 로 완전히 해결하기 ===")
import copy

monster01_info = ['원거리 미니언', [20, 10]]
monster02_info = copy.deepcopy(monster01_info)

print(f"바깥 리스트는 다른 객체인가?: {id(monster01_info) != id(monster02_info)}")
print(f"안쪽 리스트도 다른 객체인가?: {id(monster01_info[1]) != id(monster02_info[1])}")
print("-" * 20)

monster02_info[0] = '근거리 미니언'
monster02_info[1][0] = 30

print(f"최종 결과:")
print(f"원본: {monster01_info}")
print(f"복사본: {monster02_info}")