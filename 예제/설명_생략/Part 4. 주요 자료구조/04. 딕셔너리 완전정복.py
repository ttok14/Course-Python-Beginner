# ====================================
# Part 4. 주요 자료구조 - 딕셔너리 완전정복
# ====================================

print("--- 1. 딕셔너리 생성 및 기본 정보 확인 ---")

character = {
    'name': '전사',
    'level': 10,
    'items': ['검', '방패']
}

print(f"초기 캐릭터 정보: {character}")

print(f"레벨: {character['level']}")
print("-" * 20)


print("--- 2. 딕셔너리 데이터 추가 및 수정 ---")

character['level'] = 11
print(f"레벨업 후 정보: {character}")

character['hp'] = 200
print(f"체력(hp) 추가 후 정보: {character}")
print("-" * 20)


print("--- 3. 안전하게 값에 접근하기: .get() 메서드 ---")

mp_info_none = character.get('mp')
print(f"get()으로 찾은 MP 정보 (키 없음): {mp_info_none}")

mp_info_default = character.get('mp', 0)
print(f"get()으로 찾은 MP 정보 (기본값 지정): {mp_info_default}")
print("-" * 20)


print("--- 4. 딕셔너리 주요 메서드 활용 (순회) ---")

print(f"캐릭터 속성들 (keys): {character.keys()}")
print("- 속성(key) 목록 -")
for key in character.keys():
    print(key)

print() 

print(f"캐릭터 값들 (values): {character.values()}")
print("- 값(value) 목록 -")
for value in character.values():
    print(value)

print() 

print(f"캐릭터 정보 쌍 (items): {character.items()}")
print("- 속성: 값 목록 -")
for key, value in character.items():
    print(f"{key}: {value}")
print("-" * 20)


print("--- 5. 딕셔너리 데이터 삭제 및 병합 ---")

print(f"삭제 전 캐릭터 정보: {character}")
removed_items = character.pop('items')
print(f"삭제된 아이템 정보: {removed_items}")
print(f"삭제 후 캐릭터 정보: {character}")

print() 

extra_stats = {'strength': 15, 'dexterity': 12}
print(f"병합할 추가 스탯: {extra_stats}")

character.update(extra_stats)

print(f"최종 캐릭터 정보: {character}")
print("-" * 20)