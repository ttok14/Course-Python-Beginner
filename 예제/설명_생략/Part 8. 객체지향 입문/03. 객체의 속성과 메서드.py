# ====================================
# Part 8. 객체지향 입문 - 객체의 속성과 메서드
# ====================================

print("--- 1. 클래스 정의 ---")

class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def show_status(self):
        print(f"이름: {self.name}, 체력: {self.hp}, 공격력: {self.power}")

    def take_damage(self, damage):
        self.hp -= damage
        print(f"{self.name}이(가) {damage}의 피해를 받았습니다. 남은 체력: {self.hp}")

    def attack(self, target, skill_name="기본 공격"):
        damage = self.power
        if skill_name == "파워 스매시":
            damage = self.power * 2
        
        print(f"{self.name}이(가) {skill_name}으로 공격합니다!")
        
        target.take_damage(damage)

    def is_alive(self):
        return self.hp > 0

print("\n--- 2. 객체 생성 및 초기 상태 확인 ---")
monster1 = Monster("슬라임", 50, 10)
monster2 = Monster("고블린", 70, 15)

monster1.show_status()
monster2.show_status()


print("\n--- 3. 전투 시작 ---")

print("\n[첫 번째 공격]")
monster1.attack(monster2)
monster1.show_status()
monster2.show_status()

print("\n[두 번째 공격]")
monster1.attack(monster2, "파워 스매시")
monster1.show_status()
monster2.show_status()


print("\n--- 4. 연속 공격 시뮬레이션 ---")

for round_num in range(1, 6):
    print(f"\n{round_num}라운드:")
    
    if monster2.is_alive():
        monster1.attack(monster2)
    
    if not monster2.is_alive():
        print(f"\n{monster2.name}은(는) 쓰러졌다!")
        break

monster1.show_status()
monster2.show_status()