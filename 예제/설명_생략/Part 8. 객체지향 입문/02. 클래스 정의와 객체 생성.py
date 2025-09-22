# ====================================
# Part 8. 클래스 정의와 객체 생성
# ====================================

print("--- 1. 가장 간단한 클래스 정의하기 ---")

class House:
    pass

house01 = House()
house02 = House()

print("house01 인스턴스의 정보:", house01)
print("house02 인스턴스의 정보:", house02)
print("-" * 20)


print("\n--- 2. 초기화 메서드 __init__ 활용하기 ---")

class Monster:
    def __init__(self, name, hp):
        print(f"새로운 몬스터 '{name}'이(가) 생성되었습니다.")
        self.name = name
        self.hp = hp

monster1 = Monster("슬라임", 30)
monster2 = Monster("고블린", 50)

print(f"첫 번째 몬스터: {monster1.name}, 체력: {monster1.hp}")
print(f"두 번째 몬스터: {monster2.name}, 체력: {monster2.hp}")
print("-" * 20)


print("\n--- 3. 인스턴스의 독립성 확인하기 ---")

print(f"'{monster1.name}'의 체력을 10으로 변경합니다.")
monster1.hp = 10

print(f"첫 번째 몬스터 정보: {monster1.name}, 체력: {monster1.hp}")
print(f"두 번째 몬스터 정보: {monster2.name}, 체력: {monster2.hp}")
print("-" * 20)


print("\n--- 4. 응용: Player 클래스 만들어보기 ---")

class Player:
    def __init__(self, name, job):
        self.name = name
        self.job = job

player1 = Player("김민수", "전사")
player2 = Player("이지은", "마법사")

print(f"플레이어1: {player1.name}, 직업: {player1.job}")
print(f"플레이어2: {player2.name}, 직업: {player2.job}")