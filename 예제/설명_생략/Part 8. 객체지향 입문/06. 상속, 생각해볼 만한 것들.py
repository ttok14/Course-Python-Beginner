# ====================================
# Part8. 상속, 생각해볼 만한 것들
# ====================================

print("--- 1. 상속을 잘못 사용한 설계 (is-a 관계가 불분명한 경우) ---")
print("-" * 50)

class BasicRemote:
    def __init__(self, device_name):
        self.device_name = device_name
        print(f"[{self.device_name} 리모콘 생성]")

    def power(self):
        print(f"{self.device_name}: 전원 On/Off")

    def volume_up(self):
        print(f"{self.device_name}: 볼륨을 높입니다.")

    def channel_up(self):
        print(f"{self.device_name}: 채널을 높입니다.")

class SmartTVRemote(BasicRemote):
    def __init__(self):
        super().__init__("스마트 TV")
    
    def netflix_button(self):
        print("넷플릭스 앱을 켭니다.")

tv_remote = SmartTVRemote()
tv_remote.power()
tv_remote.channel_up()
tv_remote.netflix_button()
print("-" * 20)

class AirConditionerRemote(BasicRemote):
    def __init__(self):
        super().__init__("에어컨")

    def channel_up(self):
        print("경고: 에어컨에는 채널 기능이 없습니다.")
    
    def volume_up(self):
        print("경고: 에어컨에는 볼륨 기능이 없습니다.")

    def temperature_up(self):
        print("에어컨: 온도를 높입니다.")

ac_remote = AirConditionerRemote()
ac_remote.power()
ac_remote.volume_up()
ac_remote.channel_up()
ac_remote.temperature_up()
print("-" * 20)

print("결론: 만능 리모콘 설계 시 다중 상속 문제로 구조가 복잡해지며, 유지보수가 어려워집니다.")
print("\n" * 2)


print("--- 2. 컴포지션을 활용한 유연한 설계 (has-a 관계) ---")
print("-" * 50)

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

class Command:
    def execute(self):
        raise NotImplementedError

class PowerCommand(Command):
    def __init__(self, device):
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

class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, button_name, command):
        self.commands[button_name] = command

    def press_button(self, button_name):
        if button_name in self.commands:
            self.commands[button_name].execute()
        else:
            print(f"알림: '{button_name}' 버튼에 할당된 기능이 없습니다.")

my_tv = TV()
my_ac = AirConditioner()

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
universal_remote.press_button("netflix")
print("-" * 20)

print("결론: 컴포지션은 객체 간의 결합을 느슨하게 하여, 재사용성과 확장성이 높은 유연한 설계를 가능하게 합니다.")
print("\n" * 2)


print("--- 3. 상속 vs 컴포지션 판단 연습 ---")
print("-" * 50)

class Employee:
    def __init__(self, name):
        self.name = name
    def work(self):
        print(f"{self.name}이(가) 출근합니다.")

class Manager(Employee):
    def work(self):
        print(f"{self.name} 매니저가 팀을 관리합니다.")

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
        self.engine = engine

    def start(self):
        print("자동차 키를 돌려 시동을 겁니다...")
        self.engine.start()

gas_car = Car(GasolineEngine())
gas_car.start()

elec_car = Car(ElectricEngine())
elec_car.start()