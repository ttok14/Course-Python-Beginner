# ====================================
# Part 4.얕은복사와 깊은복사
# ====================================

# 1. immutable 데이터 타입의 경우
# immutable 데이터는 값을 변경할 수 없으므로, 복사라는 개념이 사실상 필요 없습니다.
# 한 변수의 값을 변경해도 다른 변수에 영향을 주지 않습니다.
print("=== 1. immutable 데이터는 복사가 필요없습니다 ===")
my_sister_age = 15
my_brother_age = my_sister_age # my_sister_age가 가리키는 15라는 객체를 함께 가리킵니다.

print(f"여동생 나이: {my_sister_age}")
print(f"남동생 나이: {my_brother_age}")
print(f"두 변수는 같은 객체를 가리킵니다: id={id(my_sister_age)} == id={id(my_brother_age)}")
print("-" * 20)

# 남동생의 나이를 변경하면, 새로운 정수 객체 20이 생성되고 my_brother_age가 그것을 가리킵니다.
my_brother_age = 20

print(f"남동생 나이 변경 후 - 여동생: {my_sister_age}, 남동생: {my_brother_age}")
print(f"이제 두 변수는 다른 객체를 가리킵니다: id={id(my_sister_age)} != id={id(my_brother_age)}")


# 2. mutable 데이터 타입의 문제점
# mutable 데이터를 단순 할당하면, 같은 객체를 가리키는 이름표만 늘어나는 셈입니다.
# 이는 복사가 아니며, 한쪽에서 수정하면 다른 쪽에도 영향을 미칩니다.
print("\n=== 2. mutable의 문제점 (복사가 아닌 단순 할당) ===")
monster01_info = ['원거리 미니언', '20'] # [이름, 공격력]
monster02_info = monster01_info  # 이것은 복사가 아니라, 같은 리스트 객체를 가리키는 것입니다.

print(f"원본: {monster01_info}")
print(f"할당본: {monster02_info}")
print(f"두 변수는 같은 객체입니다: {id(monster01_info) == id(monster02_info)}")
print("-" * 20)

# 할당본의 값을 변경해봅니다.
monster02_info[0] = '근거리 미니언'

# 원본까지 함께 변경되는 문제가 발생합니다.
print(f"할당본 수정 후 - 원본: {monster01_info}")
print(f"할당본 수정 후 - 할당본: {monster02_info}")


# 3. 얕은 복사 (Shallow Copy)
# .copy() 메서드를 사용하면, 객체 자체는 복사되지만 내부의 객체는 공유합니다.
print("\n=== 3. 얕은 복사 (Shallow Copy) 로 해결하기 ===")
monster01_info = ['원거리 미니언', '20'] # 원본 리스트를 다시 초기화합니다.
monster02_info = monster01_info.copy() # .copy() 메서드로 얕은 복사를 수행합니다.

# 이제 두 변수는 서로 다른 리스트 객체를 가리킵니다.
print(f"이제 두 변수는 다른 객체입니다: {id(monster01_info) != id(monster02_info)}")
print("-" * 20)

# 복사본의 값을 변경합니다.
monster02_info[0] = '근거리 미니언'

# 원본은 영향을 받지 않습니다. 이것이 우리가 원했던 복사입니다.
print(f"복사본 수정 후 - 원본: {monster01_info}")
print(f"복사본 수정 후 - 복사본: {monster02_info}")


# 4. 얕은 복사의 한계 (중첩 구조)
# 리스트 안에 또 다른 mutable 객체(리스트 등)가 있을 경우, 얕은 복사는 한계를 보입니다.
# 바깥쪽 리스트는 복사되지만, 안쪽 리스트는 여전히 같은 객체를 공유합니다.
print("\n=== 4. 얕은 복사의 한계 (중첩 구조) ===")
# [이름, [공격력, 방어력]]
monster01_info = ['원거리 미니언', [20, 10]]
monster02_info = monster01_info.copy() # 얕은 복사

print(f"바깥 리스트는 다른 객체인가? : {id(monster01_info) != id(monster02_info)}")
print(f"안쪽 리스트는 같은 객체인가? : {id(monster01_info[1]) == id(monster02_info[1])}")
print("-" * 20)

# 복사본의 '안쪽 리스트'의 값을 수정해봅니다.
monster02_info[1][0] = 30 # 복사본의 공격력을 30으로 변경

# 얕은 복사 시 내부 객체는 공유되므로, 원본의 내부 리스트 값도 함께 변경됩니다.
print(f"복사본의 내부 리스트만 수정했는데...")
print(f"원본 스탯: {monster01_info}")
print(f"복사본 스탯: {monster02_info}")


# 5. 깊은 복사 (Deep Copy)
# copy 모듈의 deepcopy() 함수는 내부의 모든 객체까지 재귀적으로 복사하여
# 완전히 독립적인 새로운 객체를 만들어줍니다.
print("\n=== 5. 깊은 복사 (Deep Copy) 로 완전히 해결하기 ===")
import copy # copy 모듈을 불러옵니다.

monster01_info = ['원거리 미니언', [20, 10]]  # 다시 원본을 설정합니다.
monster02_info = copy.deepcopy(monster01_info)  # 깊은 복사를 수행합니다.

# 이제 바깥쪽 리스트와 안쪽 리스트 모두 다른 객체가 됩니다.
print(f"바깥 리스트는 다른 객체인가?: {id(monster01_info) != id(monster02_info)}")
print(f"안쪽 리스트도 다른 객체인가?: {id(monster01_info[1]) != id(monster02_info[1])}")
print("-" * 20)

# 복사본의 값을 마음껏 수정합니다.
monster02_info[0] = '근거리 미니언'  # 이름 수정
monster02_info[1][0] = 30  # 공격력 수정

# 깊은 복사를 통해 완전히 독립된 객체가 되었으므로 원본은 전혀 영향을 받지 않습니다.
print(f"최종 결과:")
print(f"원본: {monster01_info}")
print(f"복사본: {monster02_info}")


'''
- 정리하며
    1. 복사의 목적: 원본에 영향을 주지 않는 독립적인 객체를 만들기 위함입니다.
    2. 얕은 복사(.copy()): 객체 자체만 복사하고, 내부의 중첩된 객체는 주소값만 복사하여 공유합니다.
    3. 깊은 복사(copy.deepcopy()): 객체 내부의 모든 중첩된 객체까지 재귀적으로 복사하여 완전히 새로운 객체를 만듭니다.
    4. 언제 무엇을 써야 하는가?
        - 리스트 내부에 리스트, 딕셔너리 등 다른 mutable 객체가 없다면 얕은 복사로 충분합니다.
        - 중첩된 구조를 가지며 완전한 독립성을 보장해야 할 때는 반드시 깊은 복사를 사용해야 합니다.
    5. id() 함수를 통해 두 변수가 같은 객체를 참조하는지 확인할 수 있습니다.
'''