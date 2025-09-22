# ====================================
# Part 5.함수 인자 활용 실습하기
# ====================================

# 이름, 나이, 도시 세 개의 매개변수를 받는 간단한 함수를 정의합니다.
def get_user_info(name, age, city):
    """사용자 정보를 출력하는 함수"""
    print(f"이름: {name}, 나이: {age}, 사는 곳: {city}")

print("--- 1. 위치 인자 / 키워드 인자 실습 ---")

# 가장 기본적인 방식입니다. 정의된 매개변수 순서(name, age, city)에 맞춰 값을 전달합니다.
# 이처럼 순서에 맞춰 값을 전달하는 방식을 '위치 인자(Positional Argument)'라고 합니다.
print("위치 인자 호출:")
get_user_info("박민준", 30, "서울")

# '키워드 인자(Keyword Argument)'는 매개변수 이름을 직접 지정하여 값을 전달합니다.
# 키워드 인자를 사용하면 순서와 상관없이 명확하게 값을 전달할 수 있습니다.
print("\n키워드 인자 호출 (순서 변경):")
get_user_info(city="부산", name="이지은", age=25)

# 위치 인자와 키워드 인자를 함께 사용할 수 있습니다.
# 단, 위치 인자가 키워드 인자보다 항상 먼저 와야 합니다.
print("\n위치/키워드 인자 혼용 호출:")
get_user_info("이강원", city="인천", age=28)

# 파이썬은 인자를 처리할 때 왼쪽에서부터 '위치 인자'를 먼저 처리합니다.
# 키워드 인자가 등장하는 순간부터는 순서가 아닌 '이름(키워드)'으로만 값을 찾습니다.
# 한번 키워드 인자 방식이 시작되면 다시 위치 인자 방식으로 돌아갈 수 없습니다.
# 아래 코드는 키워드 인자 뒤에 위치 인자가 와서 SyntaxError가 발생합니다.
# get_user_info(name="김철수", "대전", 40) # -> SyntaxError: positional argument follows keyword argument

print("\n--- 2. 기본값 매개변수 실습 ---")

# 매개변수에 기본값을 설정할 수 있습니다.
# 기본값이 있는 매개변수는 반드시 기본값이 없는 매개변수들 뒤에 위치해야 합니다.
def calculate_shipping_fee(weight, destination, method="standard"):
    """배송비를 계산하는 함수"""
    print(f"무게: {weight}kg, 목적지: {destination}, 배송 방식: {method}")

# method 인자를 생략하고 호출하면 미리 설정된 기본값 'standard'가 사용됩니다.
print("기본값 사용:")
calculate_shipping_fee(5, "서울")

# method 인자에 'express'라는 값을 직접 전달하면 기본값을 덮어쓰게 됩니다.
print("\n기본값 덮어쓰기:")
calculate_shipping_fee(5, "서울", method="express")


print("\n--- 3. 가변 위치 인자 (*args) 실습 ---")

# 매개변수 앞에 별(*)을 하나 붙이면, 여러 개의 위치 인자를 하나의 '튜플(tuple)'로 묶어서 받습니다.
def sum_numbers(*args):
    """입력된 모든 숫자의 합계를 반환하는 함수"""
    print(f"받은 인자 (튜플): {args}, 타입: {type(args)}")
    total = 0
    for num in args:
        total += num
    return total

# 인자의 개수에 상관없이 유연하게 함수를 호출할 수 있습니다.
result1 = sum_numbers(1, 2, 3)
print(f"합계 (1, 2, 3): {result1}")

result2 = sum_numbers(10, 20, 30, 40, 50)
print(f"합계 (10, 20, 30, 40, 50): {result2}")


print("\n--- 4. 가변 키워드 인자 (**kwargs) 실습 ---")

# 매개변수 앞에 별(**)을 두 개 붙이면, 여러 키워드 인자를 하나의 '딕셔너리(dictionary)'로 묶어서 받습니다.
def print_profile(**kwargs):
    """입력된 키-값 쌍으로 프로필 정보를 출력하는 함수"""
    print(f"받은 인자 (딕셔너리): {kwargs}, 타입: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

# 다양한 키-값 쌍을 자유롭게 전달할 수 있습니다.
print("프로필 1:")
print_profile(name="한상우", job="개발자")

print("\n프로필 2:")
print_profile(name="정다은", age=29, hobbies=['독서', '영화'])


print("\n--- 5. 모든 인자 종류 종합 실습 (피자 주문) ---")

# 위치, 기본값, 가변 위치, 가변 키워드 인자를 모두 사용하는 함수입니다.
# 순서: 위치 매개변수 -> 가변 위치 매개변수(*args) -> 가변 키워드 매개변수(**kwargs)
def make_pizza(pizza_name, dough, *toppings, **options):
    """피자 주문 정보를 종합하여 출력하는 함수"""
    print(f"피자: {pizza_name}")
    print(f"도우: {dough}")
    print(f"추가 토핑: {toppings}") # 튜플로 묶입니다.
    print(f"추가 옵션: {options}")   # 딕셔너리로 묶입니다.

# 함수를 호출하면 각 인자가 종류에 맞게 매개변수에 할당됩니다.
make_pizza("페퍼로니 피자", "오리지널", "치즈", "올리브", "버섯", size="L", delivery_time=30)


print("\n--- 6. 키워드 전용 인자 실습 (메시지 전송) ---")

# 매개변수 목록 중간에 별(*)만 단독으로 쓰면, 그 뒤의 매개변수들은 반드시 키워드로만 전달해야 합니다.
# 이를 '키워드 전용 인자(Keyword-Only Argument)'라고 합니다.
# 중요한 옵션값을 실수로 잘못된 위치에 전달하는 것을 방지해줍니다.
def send_message(recipient, content, *, delivery_method="email", urgent=False):
    """메시지를 전송하는 함수"""
    print(f"받는 사람: {recipient}")
    print(f"내용: {content}")
    print(f"전송 방식: {delivery_method}")
    print(f"긴급 여부: {urgent}")

# 올바른 호출: * 뒤의 인자들을 키워드로 명시하여 전달합니다.
print("올바른 호출:")
send_message("홍길동", "안녕하세요", delivery_method="sms", urgent=True)

# 잘못된 호출: 키워드 전용 인자를 위치 인자처럼 전달하면 TypeError가 발생합니다.
print("\n잘못된 호출 시도:")
try:
    # delivery_method와 urgent를 위치로 전달하려 했기 때문에 에러가 발생합니다.
    send_message("홍길동", "안녕하세요", "sms", True)
except TypeError as e:
    print(f"에러 발생: {e}")


'''
- 정리하며
    1. 위치 인자: 순서에 맞춰 값을 전달하는 기본 방식입니다.
    2. 키워드 인자: '이름=값' 형태로 순서와 상관없이 명확하게 값을 전달하는 방식입니다.
    3. 기본값 매개변수: 인자 입력을 선택적으로 만들어 함수 사용을 편리하게 해줍니다.
    4. 가변 인자 (*args, **kwargs): 정해지지 않은 개수의 인자를 각각 튜플이나 딕셔너리로 받아 처리할 수 있게 해줍니다.
    5. 키워드 전용 인자 (*): 중요한 옵션 값을 사용자가 반드시 이름과 함께 명시하도록 강제하여 실수를 줄여줍니다.
    6. [핵심] 함수의 매개변수 순서는 (위치) -> (*args) -> (키워드 전용) -> (**kwargs) 규칙을 따르며, 이는 코드의 모호함을 없애고 가독성을 높여줍니다.
'''