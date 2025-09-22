# ====================================
# Part 4. 주요 자료구조 - 딕셔너리 완전정복
# ====================================

# 딕셔너리(Dictionary): 키(Key)와 값(Value)을 하나의 쌍으로 묶어 저장하는 자료구조입니다.
# 순서(인덱스)가 아닌 고유한 이름표(키)를 통해 데이터를 관리하며, 데이터의 의미를 명확하게 할 때 유용합니다.

# --- 1. 딕셔너리 생성 및 기본 정보 확인 ---
print("--- 1. 딕셔너리 생성 및 기본 정보 확인 ---")

# 게임 캐릭터 정보를 'character'라는 이름의 딕셔너리로 생성합니다.
# 'name', 'level', 'items'는 키(Key)이고, '전사', 10, ['검', '방패']는 값(Value)입니다.
character = {
    'name': '전사',
    'level': 10,
    'items': ['검', '방패']
}

# 생성된 딕셔너리의 전체 내용을 출력합니다.
print(f"초기 캐릭터 정보: {character}")

# 대괄호[] 안에 키를 넣어 특정 값에 접근할 수 있습니다.
print(f"레벨: {character['level']}")
print("-" * 20)


# --- 2. 딕셔너리 데이터 추가 및 수정 ---
print("--- 2. 딕셔너리 데이터 추가 및 수정 ---")

# 기존에 존재하는 키('level')에 새로운 값을 할당하면, 값이 수정됩니다.
character['level'] = 11
print(f"레벨업 후 정보: {character}")

# 존재하지 않는 키('hp')에 값을 할당하면, 새로운 키-값 쌍이 추가됩니다.
character['hp'] = 200
print(f"체력(hp) 추가 후 정보: {character}")
print("-" * 20)


# --- 3. 안전하게 값에 접근하기: .get() 메서드 ---
print("--- 3. 안전하게 값에 접근하기: .get() 메서드 ---")

# 대괄호[]로 존재하지 않는 키('mp')에 접근하면 KeyError가 발생하고 프로그램이 멈춥니다.
# print(character['mp']) # 이 줄의 주석을 해제하면 오류가 발생합니다.

# .get() 메서드는 키가 존재하지 않아도 오류를 발생시키지 않고 'None'을 반환합니다.
mp_info_none = character.get('mp')
print(f"get()으로 찾은 MP 정보 (키 없음): {mp_info_none}")

# .get() 메서드의 두 번째 인자로 기본값을 지정할 수 있습니다.
# 'mp' 키가 없으므로, 기본값인 0이 반환됩니다.
mp_info_default = character.get('mp', 0)
print(f"get()으로 찾은 MP 정보 (기본값 지정): {mp_info_default}")
print("-" * 20)


# --- 4. 딕셔너리 주요 메서드 활용 (순회) ---
print("--- 4. 딕셔너리 주요 메서드 활용 (순회) ---")

# .keys(): 딕셔너리의 모든 키만 모아서 보여줍니다. 반복문과 함께 자주 사용됩니다.
print(f"캐릭터 속성들 (keys): {character.keys()}")
print("- 속성(key) 목록 -")
for key in character.keys():
    print(key)

print() 

# .values(): 딕셔너리의 모든 값만 모아서 보여줍니다.
print(f"캐릭터 값들 (values): {character.values()}")
print("- 값(value) 목록 -")
for value in character.values():
    print(value)

print() 

# .items(): 키와 값의 쌍(튜플)을 함께 보여줍니다.
# for 반복문에서 키와 값을 동시에 받아 처리할 때 매우 유용합니다.
print(f"캐릭터 정보 쌍 (items): {character.items()}")
print("- 속성: 값 목록 -")
for key, value in character.items():
    print(f"{key}: {value}")
print("-" * 20)


# --- 5. 딕셔너리 데이터 삭제 및 병합 ---
print("--- 5. 딕셔너리 데이터 삭제 및 병합 ---")

# .pop(): 지정한 키의 데이터를 삭제하고, 삭제된 값을 반환합니다.
print(f"삭제 전 캐릭터 정보: {character}")
removed_items = character.pop('items')
print(f"삭제된 아이템 정보: {removed_items}")
print(f"삭제 후 캐릭터 정보: {character}")

print() # 줄바꿈

# .update(): 다른 딕셔너리의 내용을 현재 딕셔너리에 병합(추가/수정)합니다.
extra_stats = {'strength': 15, 'dexterity': 12}
print(f"병합할 추가 스탯: {extra_stats}")

character.update(extra_stats) # extra_stats의 내용이 character에 합쳐집니다.

print(f"최종 캐릭터 정보: {character}")
print("-" * 20)


'''
    - 정리하며
        1. 딕셔너리는 '키(Key)-값(Value)' 쌍으로 데이터를 저장하는 자료구조입니다.
        2. 순서가 아닌 의미 있는 이름(키)으로 데이터를 관리하고 싶을 때 사용합니다.
        3. 데이터 접근은 대괄호 `[]` 또는 `.get()` 메서드를 사용하며, 키가 없을 때 오류를 방지하는 `.get()` 사용을 권장합니다.
        4. 딕셔너리는 수정 가능(Mutable)한 자료구조로, 언제든지 키-값 쌍을 추가, 수정, 삭제할 수 있습니다.
        5. `.keys()`, `.values()`, `.items()`는 딕셔너리의 내용을 순회할 때 사용하는 유용한 도구이며, 주로 for 반복문과 함께 사용됩니다.
        6. 리스트가 데이터를 '줄 세우는' 방식이라면, 딕셔너리는 데이터에 '이름표를 붙여주는' 방식입니다.
'''