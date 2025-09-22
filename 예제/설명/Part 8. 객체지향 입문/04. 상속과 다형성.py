# ====================================
# Part 8. 객체지향 입문 - 상속과 다형성
# ====================================

# 1. 부모 클래스(Parent Class) 정의
# 모든 몬스터의 기본이 되는 Monster 클래스를 정의합니다.
# 이 클래스는 이름, 체력, 공격력 속성과 상태를 보여주고 공격하는 메서드를 가집니다.
class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power
    
    def show_status(self):
        print(f"이름: {self.name}, 체력: {self.hp}, 공격력: {self.power}")
    
    def attack(self, target):
        # 자식 클래스에서 이 메서드를 오버라이딩할 수 있습니다.
        print(f"{self.name}이(가) 기본 공격을 합니다!")
        target.hp -= self.power

# 2. 자식 클래스(Child Class) 정의 - 기본 상속
# Monster 클래스를 상속받는 Slime 클래스를 정의합니다.
# class 자식클래스(부모클래스): 형태로 작성합니다.
# pass 키워드는 아무 내용도 정의하지 않음을 의미합니다.
class Slime(Monster):
    pass

print("--- 1. 기본 상속 테스트 ---")
# Slime 클래스에 __init__이 없지만, 부모인 Monster의 __init__이 호출됩니다.
slime = Slime('미끈이', 30, 5)
monster = Monster('고블린', 50, 10)

# Slime 클래스에 메서드가 없지만, 부모의 메서드를 사용할 수 있습니다.
slime.show_status()
slime.attack(monster)
monster.show_status()

# isinstance() 함수: 객체가 특정 클래스의 인스턴스인지 확인합니다.
# 자식 클래스의 인스턴스는 부모 클래스의 인스턴스로도 인정됩니다.
print(f"\nslime이 Monster의 인스턴스인가? {isinstance(slime, Monster)}")
print(f"slime이 Slime의 인스턴스인가? {isinstance(slime, Slime)}")


# 3. 자식 클래스 정의 - 기능 확장 및 오버라이딩
# Monster 클래스를 상속받되, 새로운 속성과 메서드를 추가하고, 기존 메서드를 재정의합니다.
class Dragon(Monster):
    def __init__(self, name, hp, power, fly_speed):
        # super()는 부모 클래스를 가리킵니다.
        # 부모 클래스의 __init__ 메서드를 호출하여 이름, 체력, 공격력 초기화를 맡깁니다.
        super().__init__(name, hp, power)
        # Dragon 클래스만의 고유 속성을 추가합니다.
        self.fly_speed = fly_speed
        
    # Dragon 클래스만의 고유 메서드를 추가합니다.
    def fly(self):
        print(f"{self.name}이(가) {self.fly_speed}의 속도로 날아갑니다!")

    # 메서드 오버라이딩(Method Overriding)
    # 부모 클래스로부터 물려받은 attack 메서드를 자식 클래스에 맞게 재정의합니다.
    def attack(self, target):
        print(f"{self.name}이(가) 화염 공격을 합니다!")
        # 공격력을 1.5배로 하여 더 강력한 공격을 구현합니다.
        target.hp -= self.power * 1.5


print("\n--- 2. 기능 확장 및 오버라이딩 테스트 ---")
dragon = Dragon('화룡', 100, 20, 50)

# 부모로부터 물려받은 메서드 호출
dragon.show_status()
# 자식 클래스에서 새로 정의한 메서드 호출
dragon.fly()
# 자식 클래스에서 오버라이딩한 메서드 호출
dragon.attack(monster)
monster.show_status()


# 4. 다형성(Polymorphism)
# '여러 가지 형태를 가진다'는 의미로, 같은 코드(메서드 호출)가
# 객체의 실제 타입에 따라 다르게 동작하는 특성을 말합니다.

# 새로운 몬스터들을 생성합니다.
monster2 = Monster('오크', 60, 12)
slime2 = Slime('젤리', 25, 8)
dragon2 = Dragon('용왕', 120, 25, 60)

# battle 함수는 공격자(attacker)의 실제 타입이 무엇인지 신경쓰지 않습니다.
# 단지 'attack' 메서드를 가지고 있다는 것만 알고 호출합니다.
def battle(attacker, defender):
    print(f"\n--- {attacker.name} vs {defender.name} ---")
    print("공격 전:")
    defender.show_status()
    
    # attacker가 Monster면 Monster의 attack, Dragon이면 Dragon의 attack이 호출됩니다.
    attacker.attack(defender)
    
    print("공격 후:")
    defender.show_status()

print("\n--- 3. 다형성 테스트 (battle 함수) ---")
battle(monster2, slime2) # Monster의 attack 메서드 호출
battle(dragon2, monster2) # Dragon의 오버라이딩된 attack 메서드 호출


# 리스트에 서로 다른 타입의 객체를 담습니다.
# 이 객체들은 모두 Monster를 상속받았다는 공통점이 있습니다.
units = [monster2, slime2, dragon2]
target = Monster('표적', 200, 0)

print("\n--- 4. 다형성 테스트 (for 루프) ---")
# 반복문은 unit의 실제 클래스 타입을 검사할 필요가 없습니다.
# 그냥 attack() 메서드를 호출하면, 각 객체에 맞는 메서드가 실행됩니다.
for unit in units:
    print(f"\n* {unit.name}의 공격 *")
    unit.attack(target)
    print(f"표적의 남은 체력: {target.hp}")


'''
    - 정리하며
        1. 상속(Inheritance): 부모 클래스의 속성과 메서드를 자식 클래스가 물려받는 기능입니다. 코드 재사용성을 높여줍니다.
        2. super(): 자식 클래스에서 부모 클래스를 참조할 때 사용합니다. 주로 부모의 __init__ 메서드를 호출할 때 사용됩니다.
        3. 메서드 오버라이딩(Method Overriding): 부모에게 물려받은 메서드를 자식 클래스의 상황에 맞게 재정의하는 것입니다.
        4. 다형성(Polymorphism): 같은 형태의 코드(예: `unit.attack()`)가 객체의 실제 타입에 따라 다른 행동을 하는 원리입니다. 코드를 유연하고 확장성 있게 만듭니다.
        5. isinstance() 함수를 통해 객체와 클래스 간의 상속 관계를 확인할 수 있습니다.
'''