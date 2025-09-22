# ====================================
# Part 4. 세트 완전정복
# ====================================

# 세트(Set): 중복을 허용하지 않고, 순서가 없는 값들의 모음입니다.
# 수학의 '집합'과 유사하며, 데이터의 포함 여부를 빠르게 확인하는 데 사용됩니다.

# 1. 세트 생성하기
print("--- 1. 세트 생성하기 ---")

# 중괄호 {} 를 사용하여 세트를 생성합니다. 중복된 값은 자동으로 제거됩니다.
numbers = {1, 2, 3, 2, 1, 5}
print(f"중복 값이 있는 초기화: {numbers}")

# list를 set() 함수를 이용해 세트로 변환할 수 있습니다. 이를 통해 리스트의 중복을 쉽게 제거할 수 있습니다.
id_list = ['kim', 'lee', 'park', 'kim', 'lee']
unique_ids = set(id_list)
print(f"리스트로부터 생성된 고유 ID 세트: {unique_ids}")

# [주의] 빈 세트를 만들 때는 반드시 set() 함수를 사용해야 합니다.
# {}는 빈 딕셔너리를 의미합니다.
empty_dict = {}
empty_set = set()
print(f"빈 딕셔너리 타입: {type(empty_dict)}")
print(f"빈 세트 타입: {type(empty_set)}")
print("-" * 20)


# 2. 세트 수정: 추가와 삭제
print("--- 2. 세트 수정: 추가와 삭제 ---")
banned_champions = set() # 밴(Ban)할 챔피언 목록 관리

# .add(): 하나의 요소 추가
banned_champions.add('야스오')
print(f".add() 사용 후: {banned_champions}")

# .update(): 여러 개의 요소 추가 (리스트, 튜플, 세트 등 반복 가능한 객체 사용)
banned_champions.update(['제드', '마스터 이', '티모'])
print(f".update() 사용 후: {banned_champions}")

# .remove(): 특정 요소 삭제. 요소가 없으면 KeyError 발생
banned_champions.remove('제드')
print(f".remove('제드') 사용 후: {banned_champions}")

# .discard(): 특정 요소 삭제. 요소가 없어도 에러가 발생하지 않음 (더 안전한 방법)
banned_champions.discard('티모')
print(f".discard('티모') 사용 후: {banned_champions}")

# 없는 요소를 discard로 삭제 시도
banned_champions.discard('가렌')
print(f".discard('가렌') 시도 후 (변화 없음): {banned_champions}")

# 없는 요소를 remove로 삭제 시도 -> KeyError 발생
# banned_champions.remove('가렌') # 이 코드의 주석을 풀고 실행하면 에러가 발생합니다.
print("-" * 20)


# 3. 세트의 핵심: 집합 연산
print("--- 3. 세트의 핵심: 집합 연산 ---")
# 리그 오브 레전드 챔피언 선택(pick) 예시
team_a_picks = {'야스오', '티모', '이즈리얼', '럭스', '말파이트'}
team_b_picks = {'제드', '티모', '애쉬', '레오나', '말파이트'}

# 합집합 (Union): | 연산자 또는 .union() 메서드
# 두 팀이 선택한 모든 챔피언 (중복 제외)
all_champions = team_a_picks | team_b_picks
print(f"이번 게임에 등장한 모든 챔피언 (합집합): {all_champions}")

# 교집합 (Intersection): & 연산자 또는 .intersection() 메서드
# 두 팀 모두가 선택한 공통 챔피언
common_champions = team_a_picks & team_b_picks
print(f"양 팀에 공통으로 등장한 챔피언 (교집합): {common_champions}")

# 다른 라인 챔피언 목록으로 추가 연산 실습
top_laners = {'가렌', '다리우스', '티모', '말파이트'}
mid_laners = {'야스오', '럭스', '티모', '말파이트'}

# 차집합 (Difference): - 연산자 또는 .difference() 메서드
# 첫 번째 세트에는 있지만, 두 번째 세트에는 없는 요소
# 탑 라인 챔피언 중에서 미드 라인에는 없는 챔피언
only_top_laners = top_laners - mid_laners
print(f"탑에만 가는 챔피언 (차집합): {only_top_laners}")

# 대칭 차집합 (Symmetric Difference): ^ 연산자 또는 .symmetric_difference() 메서드
# 두 세트 중, 한쪽에만 속한 요소들 (합집합 - 교집합)
# 탑 또는 미드 중 한 라인에만 갈 수 있는 챔피언
exclusive_laners = top_laners ^ mid_laners
print(f"한 라인에만 가는 챔피언 (대칭 차집합): {exclusive_laners}")
print("-" * 20)


# 4. 세트 순회하기
print("--- 4. 세트 순회하기 ---")
# 세트는 순서가 없지만 for 문으로 각 요소를 순회할 수 있습니다.
# 출력 순서는 실행할 때마다 다를 수 있습니다.
print("--- 등장 챔피언 목록 (순서 보장 안됨) ---")
for champion in all_champions:
    print(champion)
print("-" * 20)


# 5. 불변형 세트: frozenset
print("--- 5. 불변형 세트: frozenset ---")
# frozenset은 생성 후 요소를 추가하거나 삭제할 수 없는 '얼어붙은' 세트입니다.
# 수정이 불가능(immutable)하므로 딕셔너리의 키로 사용될 수 있습니다.

# 일반 세트는 딕셔너리 키로 사용할 수 없어 TypeError가 발생합니다.
# test_dict = {{'a', 'b'}: 1} # 이 코드의 주석을 풀면 에러가 발생합니다.

# frozenset을 키로 사용하여 챔피언 조합의 티어를 관리하는 딕셔너리
combo_tiers = {
    frozenset(['야스오', '말파이트']): '1티어',
    frozenset(['루시안', '나미']): '2티어'
}

# 순서가 다른 frozenset으로도 동일한 키를 찾을 수 있습니다.
our_combo = frozenset(['말파이트', '야스오'])
print(f"우리 팀 조합({our_combo})의 티어: {combo_tiers[our_combo]}")
print("-" * 20)

'''
    - 정리하며
        1. 세트(Set)는 '중복을 허용하지 않고, 순서가 없는' 데이터 모음입니다.
        2. 데이터의 중복을 제거하거나, 특정 값의 포함 여부를 빠르게 확인할 때 매우 유용합니다.
        3. 빈 세트는 반드시 set() 함수로 생성해야 합니다. ({}는 빈 딕셔너리)
        4. 요소 삭제 시, .remove()는 요소가 없으면 에러를 발생시키지만 .discard()는 발생시키지 않아 더 안전합니다.
        5. 집합 연산자(|, &, -, ^)를 통해 데이터 그룹 간의 관계를 간결하게 표현하고 처리할 수 있습니다.
        6. 수정 불가능한 frozenset은 딕셔너리의 키와 같이 hashable한 객체가 필요한 곳에 사용됩니다.
'''