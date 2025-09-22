# ====================================
# Part 8. 객체지향 입문 - 객체의 속성과 메서드
# ====================================

# 1. 속성(Attribute)과 메서드(Method)를 포함하는 클래스 정의
# 속성: 객체가 가지는 데이터 (name, hp, power 등)
# 메서드: 객체가 수행할 수 있는 동작(함수)
print("--- 1. 클래스 정의 ---")

class Monster:
    """
    몬스터의 속성과 행동을 정의하는 클래스입니다.
    """
    def __init__(self, name, hp, power):
        """
        몬스터 객체의 초기 속성을 설정합니다.
        name (str): 몬스터의 이름
        hp (int): 몬스터의 체력
        power (int): 몬스터의 공격력
        """
        self.name = name
        self.hp = hp
        self.power = power

    def show_status(self):
        """몬스터의 현재 상태(이름, 체력, 공격력)를 출력합니다."""
        print(f"이름: {self.name}, 체력: {self.hp}, 공격력: {self.power}")

    def take_damage(self, damage):
        """
        몬스터가 피해를 입는 상황을 처리합니다.
        자신의 체력(hp)에서 받은 데미지만큼 감소시킵니다.
        """
        self.hp -= damage
        print(f"{self.name}이(가) {damage}의 피해를 받았습니다. 남은 체력: {self.hp}")

    def attack(self, target, skill_name="기본 공격"):
        """
        대상을 공격하는 메서드입니다.
        skill_name에 따라 다른 데미지를 적용합니다.
        target: 공격 대상 객체
        skill_name (str): 사용할 스킬의 이름 (기본값: "기본 공격")
        """
        damage = self.power
        if skill_name == "파워 스매시":
            # '파워 스매시' 스킬 사용 시 데미지를 2배로 만듭니다.
            damage = self.power * 2
        
        print(f"{self.name}이(가) {skill_name}으로 공격합니다!")
        
        # 공격 대상(target)의 take_damage 메서드를 호출하여 피해를 줍니다.
        target.take_damage(damage)

    def is_alive(self):
        """
        몬스터의 생존 여부를 반환합니다.
        체력(hp)이 0보다 크면 True, 아니면 False를 반환합니다.
        """
        return self.hp > 0

# 2. 객체(인스턴스) 생성 및 초기 상태 확인
print("\n--- 2. 객체 생성 및 초기 상태 확인 ---")
monster1 = Monster("슬라임", 50, 10)
monster2 = Monster("고블린", 70, 15)

monster1.show_status()
monster2.show_status()


# 3. 메서드를 이용한 객체 간의 상호작용 테스트
print("\n--- 3. 전투 시작 ---")

# 첫 번째 공격: monster1이 monster2를 '기본 공격'으로 공격합니다.
print("\n[첫 번째 공격]")
monster1.attack(monster2) # skill_name을 생략하여 기본값 "기본 공격" 사용
monster1.show_status()
monster2.show_status()

# 두 번째 공격: monster1이 monster2를 '파워 스매시' 스킬로 공격합니다.
print("\n[두 번째 공격]")
monster1.attack(monster2, "파워 스매시") # skill_name 인자를 직접 전달
monster1.show_status()
monster2.show_status()


# 4. 값을 반환하는 메서드와 반복문을 활용한 전투 시뮬레이션
print("\n--- 4. 연속 공격 시뮬레이션 ---")

# monster2가 쓰러질 때까지 공격을 반복합니다.
for round_num in range(1, 6):
    print(f"\n{round_num}라운드:")
    
    # monster2가 살아있을 때만 공격을 수행합니다.
    if monster2.is_alive():
        monster1.attack(monster2)
    
    # is_alive() 메서드의 반환값(False)을 확인하여 반복을 중단합니다.
    if not monster2.is_alive():
        print(f"\n{monster2.name}은(는) 쓰러졌다!")
        break

monster1.show_status()
monster2.show_status()

'''
    - 정리하며
        1. 속성(Attribute)은 객체가 가지는 고유한 데이터(값)입니다. (e.g., self.name, self.hp)
        2. 메서드(Method)는 객체가 수행할 수 있는 고유한 행동(기능)이며, 클래스 내부에 정의된 함수입니다.
        3. 메서드의 첫 번째 매개변수 'self'는 메서드를 호출한 객체 자신을 가리키며, 이를 통해 객체의 속성에 접근할 수 있습니다.
        4. 메서드는 일반 함수처럼 매개변수를 받거나(e.g., target, damage), 기본값을 설정할 수 있습니다.
        5. 메서드는 return을 사용하여 특정 계산 결과나 상태 값(True/False 등)을 호출한 곳으로 반환할 수 있습니다.
        6. 객체는 자신의 메서드를 통해 다른 객체의 메서드를 호출하고 속성을 변경하는 등 상호작용이 가능합니다.
'''