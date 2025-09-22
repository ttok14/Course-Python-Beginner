# ====================================
# Part 8. 객체지향 입문 - 상속과 다형성
# ====================================

class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
    
    def show_status(self):
        print(f"이름: {self.name}, 체력: {self.hp}, 공격력: {self.power}")
    
    def attack(self, target):
        print(f"{self.name}이(가) 기본 공격을 합니다!")
        target.hp -= self.power

class Slime(Monster):
    pass

print("--- 1. 기본 상속 테스트 ---")
slime = Slime('미끈이', 30, 5)
monster = Monster('고블린', 50, 10)

slime.show_status()
slime.attack(monster)
monster.show_status()

print(f"\nslime이 Monster의 인스턴스인가? {isinstance(slime, Monster)}")
print(f"slime이 Slime의 인스턴스인가? {isinstance(slime, Slime)}")


class Dragon(Monster):
    def __init__(self, name, hp, power, fly_speed):
        super().__init__(name, hp, power)
        self.fly_speed = fly_speed
        
    def fly(self):
        print(f"{self.name}이(가) {self.fly_speed}의 속도로 날아갑니다!")

    def attack(self, target):
        print(f"{self.name}이(가) 화염 공격을 합니다!")
        target.hp -= self.power * 1.5


print("\n--- 2. 기능 확장 및 오버라이딩 테스트 ---")
dragon = Dragon('화룡', 100, 20, 50)

dragon.show_status()
dragon.fly()
dragon.attack(monster)
monster.show_status()


monster2 = Monster('오크', 60, 12)
slime2 = Slime('젤리', 25, 8)
dragon2 = Dragon('용왕', 120, 25, 60)

def battle(attacker, defender):
    print(f"\n--- {attacker.name} vs {defender.name} ---")
    print("공격 전:")
    defender.show_status()
    
    attacker.attack(defender)
    
    print("공격 후:")
    defender.show_status()

print("\n--- 3. 다형성 테스트 (battle 함수) ---")
battle(monster2, slime2)
battle(dragon2, monster2)


units = [monster2, slime2, dragon2]
target = Monster('표적', 200, 0)

print("\n--- 4. 다형성 테스트 (for 루프) ---")
for unit in units:
    print(f"\n* {unit.name}의 공격 *")
    unit.attack(target)
    print(f"표적의 남은 체력: {target.hp}")