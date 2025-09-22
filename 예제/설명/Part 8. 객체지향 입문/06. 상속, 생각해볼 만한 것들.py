# ====================================
# Part8. 상속, 생각해볼 만한 것들
# ====================================

# 이번 예제에서는 '상속'의 오용 사례와 이를 '컴포지션'으로 개선하는 방법을 살펴봅니다.
# 리모콘 설계를 통해 is-a 관계와 has-a 관계의 차이점을 이해합니다.

print("--- 1. 상속을 잘못 사용한 설계 (is-a 관계가 불분명한 경우) ---")
print("-" * 50)

# 모든 리모콘의 '부모'가 될 기본 리모콘을 정의합니다.
class BasicRemote:
    """모든 리모콘의 기본 기능을 담은 부모 클래스입니다."""
    def __init__(self, device_name):
        self.device_name = device_name
        print(f"[{self.device_name} 리모콘 생성]")

    def power(self):
        print(f"{self.device_name}: 전원 On/Off")

    def volume_up(self):
        print(f"{self.device_name}: 볼륨을 높입니다.")

    def channel_up(self):
        print(f"{self.device_name}: 채널을 높입니다.")

# 1-1. SmartTVRemote: 상속이 잘 동작하는 것처럼 보입니다.
# '스마트 TV 리모콘'은 '기본 리모콘'의 한 종류(is-a)라고 생각하기 쉽습니다.
class SmartTVRemote(BasicRemote):
    def __init__(self):
        # super()를 통해 부모 클래스의 초기화 메서드를 호출합니다.
        super().__init__("스마트 TV")
    
    def netflix_button(self):
        print("넷플릭스 앱을 켭니다.")

tv_remote = SmartTVRemote()
tv_remote.power()
tv_remote.channel_up()
tv_remote.netflix_button()
print("-" * 20)

# 1-2. AirConditionerRemote: 설계의 문제점이 드러나기 시작합니다.
# '에어컨 리모콘'은 '기본 리모콘'의 한 종류라고 보기 어렵습니다.
# 에어컨에는 '채널'이나 '볼륨' 개념이 없기 때문입니다.
class AirConditionerRemote(BasicRemote):
    def __init__(self):
        super().__init__("에어컨")

    # 불필요한 메서드를 상속받았고, 이를 처리하기 위해 코드를 추가로 작성해야 합니다.
    # 이것은 좋지 않은 설계의 신호입니다.
    def channel_up(self):
        print("경고: 에어컨에는 채널 기능이 없습니다.")
    
    def volume_up(self):
        print("경고: 에어컨에는 볼륨 기능이 없습니다.")

    def temperature_up(self):
        print("에어컨: 온도를 높입니다.")

ac_remote = AirConditionerRemote()
ac_remote.power()
ac_remote.volume_up()  # 어색하지만 상속받은 기능입니다.
ac_remote.channel_up() # 불필요한 기능입니다.
ac_remote.temperature_up()
print("-" * 20)

# 1-3. 만능 리모콘의 문제
# TV와 에어컨을 모두 제어하는 리모콘을 만들려면, SmartTVRemote와 AirConditionerRemote를
# 모두 상속받아야 합니다. 이는 '다중 상속' 문제로 이어지며 코드 구조를 매우 복잡하게 만듭니다.
print("결론: 만능 리모콘 설계 시 다중 상속 문제로 구조가 복잡해지며, 유지보수가 어려워집니다.")
print("\n" * 2)


print("--- 2. 컴포지션을 활용한 유연한 설계 (has-a 관계) ---")
print("-" * 50)

# 컴포지션(Composition): '상속' 대신 필요한 객체를 '소유(has-a)'하여 기능을 조합하는 방식입니다.

# 2-1. 각 기기(Device)의 기능을 명확히 정의합니다.
class TV:
    def toggle_power(self):
        print("TV: 전원 On/Off")
    def change_channel(self):
        print("TV: 채널 변경")

class AirConditioner:
    def toggle_power(self):
        print("에어컨: 전원 On/Off")
    def change_temperature(self):
        print("에어컨: 온도 조절")

# 2-2. '명령(Command)' 객체를 정의합니다. 각 명령은 특정 기기의 동작을 캡슐화합니다.
class Command:
    """모든 명령 클래스가 따를 인터페이스입니다."""
    def execute(self):
        raise NotImplementedError

class PowerCommand(Command):
    def __init__(self, device):
        # 명령이 실행될 대상 기기를 '소유(has-a)'합니다.
        self.device = device

    def execute(self):
        self.device.toggle_power()

class TVChannelCommand(Command):
    def __init__(self, tv_device):
        self.tv = tv_device

    def execute(self):
        self.tv.change_channel()

class ACTemperatureCommand(Command):
    def __init__(self, ac_device):
        self.ac = ac_device

    def execute(self):
        self.ac.change_temperature()

# 2-3. 리모콘은 이제 구체적인 '기기'가 아닌 추상적인 '명령'을 소유합니다.
class RemoteControl:
    """명령 객체들을 소유하고 실행하는 역할을 담당합니다."""
    def __init__(self):
        # 버튼에 할당될 명령들을 저장할 슬롯을 만듭니다.
        self.commands = {}

    def set_command(self, button_name, command):
        self.commands[button_name] = command

    def press_button(self, button_name):
        if button_name in self.commands:
            self.commands[button_name].execute()
        else:
            print(f"알림: '{button_name}' 버튼에 할당된 기능이 없습니다.")

# 2-4. 필요한 부품(명령)을 '조립'하여 다양한 리모콘을 생성합니다.
my_tv = TV()
my_ac = AirConditioner()

# 만능 리모콘 조립 과정
# 동일한 RemoteControl 클래스를 재사용하여 어떤 종류의 리모콘이든 만들 수 있습니다.
universal_remote = RemoteControl()
universal_remote.set_command("tv_power", PowerCommand(my_tv))
universal_remote.set_command("ac_power", PowerCommand(my_ac))
universal_remote.set_command("tv_channel", TVChannelCommand(my_tv))
universal_remote.set_command("ac_temp", ACTemperatureCommand(my_ac))

print("만능 리모콘 (컴포지션 방식):")
universal_remote.press_button("tv_power")
universal_remote.press_button("ac_power")
universal_remote.press_button("tv_channel")
universal_remote.press_button("ac_temp")
universal_remote.press_button("netflix") # 설정되지 않은 버튼
print("-" * 20)

print("결론: 컴포지션은 객체 간의 결합을 느슨하게 하여, 재사용성과 확장성이 높은 유연한 설계를 가능하게 합니다.")
print("\n" * 2)


print("--- 3. 상속 vs 컴포지션 판단 연습 ---")
print("-" * 50)

# 예제 1: 직원 관리 시스템 (상속이 적절한 경우)
# '매니저는 직원의 한 종류다 (Manager is-a Employee)' -> 명확한 is-a 관계
class Employee:
    def __init__(self, name):
        self.name = name
    def work(self):
        print(f"{self.name}이(가) 출근합니다.")

class Manager(Employee):
    def work(self): # 부모 메서드 오버라이딩
        print(f"{self.name} 매니저가 팀을 관리합니다.")

# 예제 2: 자동차와 엔진 (컴포지션이 더 유연한 경우)
# '자동차는 엔진을 가지고 있다 (Car has-a Engine)' -> has-a 관계
class Engine:
    def start(self):
        raise NotImplementedError

class GasolineEngine(Engine):
    def start(self):
        print("가솔린 엔진이 시동을 겁니다.")

class ElectricEngine(Engine):
    def start(self):
        print("전기 모터가 조용히 작동합니다.")

class Car:
    def __init__(self, engine):
        self.engine = engine # Engine 객체를 '소유'합니다.

    def start(self):
        print("자동차 키를 돌려 시동을 겁니다...")
        self.engine.start()

# GasolineEngine을 부품으로 조립하여 가솔린 자동차를 만듭니다.
gas_car = Car(GasolineEngine())
gas_car.start()

# ElectricEngine을 부품으로 조립하여 전기 자동차를 만듭니다.
elec_car = Car(ElectricEngine())
elec_car.start()


'''
- 정리하며
    1. 상속은 명확한 'is-a' 관계가 성립하고, 부모의 모든 기능이 자식에게도 의미 있을 때 사용해야 합니다.
    2. 컴포지션은 'has-a' 관계를 나타내며, 필요한 기능을 부품처럼 조립하는 유연한 방식입니다.
    3. 컴포지션은 객체 간의 결합도를 낮춰(느슨한 결합), 코드의 재사용성과 확장성을 높여줍니다.
    4. 설계 시 확신이 서지 않을 때는 상속보다 컴포지션을 우선적으로 고려하는 것이 일반적으로 더 안전한 선택입니다.
    5. 좋은 설계는 한 객체의 변경이 다른 객체에 미치는 영향을 최소화하는 것입니다.
'''
