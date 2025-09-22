# ====================================
# Part 4. 세트 완전정복
# ====================================

print("--- 1. 세트 생성하기 ---")

numbers = {1, 2, 3, 2, 1, 5}
print(f"중복 값이 있는 초기화: {numbers}")

id_list = ['kim', 'lee', 'park', 'kim', 'lee']
unique_ids = set(id_list)
print(f"리스트로부터 생성된 고유 ID 세트: {unique_ids}")

empty_dict = {}
empty_set = set()
print(f"빈 딕셔너리 타입: {type(empty_dict)}")
print(f"빈 세트 타입: {type(empty_set)}")
print("-" * 20)


print("--- 2. 세트 수정: 추가와 삭제 ---")
banned_champions = set()

banned_champions.add('야스오')
print(f".add() 사용 후: {banned_champions}")

banned_champions.update(['제드', '마스터 이', '티모'])
print(f".update() 사용 후: {banned_champions}")

banned_champions.remove('제드')
print(f".remove('제드') 사용 후: {banned_champions}")

banned_champions.discard('티모')
print(f".discard('티모') 사용 후: {banned_champions}")

banned_champions.discard('가렌')
print(f".discard('가렌') 시도 후 (변화 없음): {banned_champions}")

print("-" * 20)


print("--- 3. 세트의 핵심: 집합 연산 ---")
team_a_picks = {'야스오', '티모', '이즈리얼', '럭스', '말파이트'}
team_b_picks = {'제드', '티모', '애쉬', '레오나', '말파이트'}

all_champions = team_a_picks | team_b_picks
print(f"이번 게임에 등장한 모든 챔피언 (합집합): {all_champions}")

common_champions = team_a_picks & team_b_picks
print(f"양 팀에 공통으로 등장한 챔피언 (교집합): {common_champions}")

top_laners = {'가렌', '다리우스', '티모', '말파이트'}
mid_laners = {'야스오', '럭스', '티모', '말파이트'}

only_top_laners = top_laners - mid_laners
print(f"탑에만 가는 챔피언 (차집합): {only_top_laners}")

exclusive_laners = top_laners ^ mid_laners
print(f"한 라인에만 가는 챔피언 (대칭 차집합): {exclusive_laners}")
print("-" * 20)


print("--- 4. 세트 순회하기 ---")
print("--- 등장 챔피언 목록 (순서 보장 안됨) ---")
for champion in all_champions:
    print(champion)
print("-" * 20)


print("--- 5. 불변형 세트: frozenset ---")

combo_tiers = {
    frozenset(['야스오', '말파이트']): '1티어',
    frozenset(['루시안', '나미']): '2티어'
}

our_combo = frozenset(['말파이트', '야스오'])
print(f"우리 팀 조합({our_combo})의 티어: {combo_tiers[our_combo]}")
print("-" * 20)