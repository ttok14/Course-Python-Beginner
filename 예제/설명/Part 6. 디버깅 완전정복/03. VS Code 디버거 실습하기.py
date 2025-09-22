# ====================================
# Part 6. 디버깅 완전정복 - VS Code 디버거 실습하기
# ====================================

# VS Code 디버거의 주요 기능을 실습하기 위한 예제 코드입니다.
# 이 코드는 의도적으로 버그를 포함하고 있으며,
# 디버거를 사용하여 버그의 원인을 찾아 수정하는 과정을 학습합니다.


# 1. 버그가 포함된 함수 정의
# 이 함수는 시간에 따라 다른 인사말을 출력하는 것을 목표로 합니다.
# 10시를 전달했으므로, "좋은 아침"이 출력되어야 정상입니다.
def show_greeting(user_name, current_hour):
    """
    시간에 따라 적절한 인사말을 생성하여 출력하는 함수입니다.
    
    - 6시 ~ 11시: "좋은 아침"
    - 12시 ~ 17시: "활기찬 오후"
    - 그 외: "편안한 저녁"
    """
    # 기본 인사말을 설정합니다.
    time_text = "안녕하세요"

    # [버그 원인]
    # 첫 번째 if문이 참이 되어도, 두 번째 if문이 독립적으로 실행됩니다.
    # 이로 인해 current_hour가 12보다 작으면 항상 else 구문이 실행됩니다.
    if current_hour >= 6 and current_hour < 12:
        time_text = "좋은 아침"
    
    # 이 부분은 'elif'가 되어야 올바른 논리가 완성됩니다.
    if current_hour >= 12 and current_hour < 18: 
        time_text = "활기찬 오후"
    else:
        time_text = "편안한 저녁"

    message = f"{time_text}, {user_name}님! 현재 시각은 {current_hour}시입니다."
    print(message)


# 2. 디버깅 실습 시작점
# 아래 함수 호출문에 브레이크포인트(Breakpoint)를 설정하고 디버깅을 시작합니다. (F9로 설정, F5로 시작)
# - Step Into(F11): 함수 내부로 진입합니다.
# - Step Over(F10): 코드를 한 줄씩 실행하며 '변수(Variables)' 패널에서 time_text 값의 변화를 관찰합니다.
# - 조사식(Watch): 'current_hour >= 6 and current_hour < 12' 와 같은 표현식을 등록하여 실시간으로 결과를 확인할 수 있습니다.
# - 변수 수정 & Jump to Cursor: 디버깅 중 변수 값을 바꾸고 실행 위치를 강제로 옮겨 다른 시나리오를 테스트할 수 있습니다.
# - Step Out(Shift+F11): 현재 함수의 실행을 마치고 함수를 호출한 지점으로 돌아갑니다.
# - Continue(F5): 다음 브레이크포인트까지 실행을 계속합니다.
print("--- 버그가 있는 코드 실행 결과 ---")
show_greeting("이강원", 10) # 예상 결과: "좋은 아침", 실제 결과: "편안한 저녁"
print("-" * 30)


# 3. 버그를 수정한 함수
# if-if-else 구조를 if-elif-else로 수정하여 조건문이 올바르게 동작하도록 합니다.
def show_greeting_fixed(user_name, current_hour):
    """
    버그가 수정된 버전의 인사말 출력 함수입니다.
    """
    time_text = "안녕하세요"

    # [수정된 부분]
    # if-elif-else 구조를 사용하여, 하나의 조건이 참이면 나머지 조건은 검사하지 않습니다.
    if current_hour >= 6 and current_hour < 12:
        time_text = "좋은 아침"
    elif current_hour >= 12 and current_hour < 18:
        time_text = "활기찬 오후"
    else:
        time_text = "편안한 저녁"

    message = f"{time_text}, {user_name}님! 현재 시각은 {current_hour}시입니다."
    print(message)


# 4. 수정된 코드 실행 확인
# 디버거 없이 실행(Ctrl+F5)하여 정상적인 결과가 출력되는지 확인합니다.
print("--- 버그를 수정한 코드 실행 결과 ---")
show_greeting_fixed("이강원", 10)
print("-" * 30)


'''
    - 정리하며
        1. 브레이크포인트(Breakpoint): 코드 실행을 특정 지점에서 일시 중지시키는 기능입니다. (F9)
        2. Step Into (F11): 함수 호출문에서 함수 내부로 진입하여 코드를 한 줄씩 살펴볼 때 사용합니다.
        3. Step Over (F10): 현재 줄을 실행하고 다음 줄로 넘어갑니다. 함수 호출이 있어도 내부로 들어가지 않습니다.
        4. 변수(Variables) 패널: 현재 범위(Scope) 내의 변수들과 그 값들을 실시간으로 보여줍니다. 디버깅 중 값을 직접 수정할 수도 있습니다.
        5. 조사식(Watch) 패널: 특정 변수나 표현식의 값을 지속적으로 관찰할 때 유용합니다.
        6. 호출 스택(Call Stack) 패널: 함수 호출의 순서와 현재 실행 위치를 보여줍니다.
        7. Step Out (Shift+F11): 현재 함수의 남은 부분을 모두 실행하고, 함수를 빠져나갑니다.
        8. 디버깅은 버그의 원인을 논리적으로 추적하고 찾아내는 가장 기본적이고 핵심적인 개발 기술입니다.
'''