# ====================================
# Part 5.함수 인자 활용 실습하기
# ====================================

def get_user_info(name, age, city):
    print(f"이름: {name}, 나이: {age}, 사는 곳: {city}")

print("--- 1. 위치 인자 / 키워드 인자 실습 ---")

print("위치 인자 호출:")
get_user_info("박민준", 30, "서울")

print("\n키워드 인자 호출 (순서 변경):")
get_user_info(city="부산", name="이지은", age=25)

print("\n위치/키워드 인자 혼용 호출:")
get_user_info("이강원", city="인천", age=28)

print("\n--- 2. 기본값 매개변수 실습 ---")

def calculate_shipping_fee(weight, destination, method="standard"):
    print(f"무게: {weight}kg, 목적지: {destination}, 배송 방식: {method}")

print("기본값 사용:")
calculate_shipping_fee(5, "서울")

print("\n기본값 덮어쓰기:")
calculate_shipping_fee(5, "서울", method="express")


print("\n--- 3. 가변 위치 인자 (*args) 실습 ---")

def sum_numbers(*args):
    print(f"받은 인자 (튜플): {args}, 타입: {type(args)}")
    total = 0
    for num in args:
        total += num
    return total

result1 = sum_numbers(1, 2, 3)
print(f"합계 (1, 2, 3): {result1}")

result2 = sum_numbers(10, 20, 30, 40, 50)
print(f"합계 (10, 20, 30, 40, 50): {result2}")


print("\n--- 4. 가변 키워드 인자 (**kwargs) 실습 ---")

def print_profile(**kwargs):
    print(f"받은 인자 (딕셔너리): {kwargs}, 타입: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"- {key}: {value}")

print("프로필 1:")
print_profile(name="한상우", job="개발자")

print("\n프로필 2:")
print_profile(name="정다은", age=29, hobbies=['독서', '영화'])


print("\n--- 5. 모든 인자 종류 종합 실습 (피자 주문) ---")

def make_pizza(pizza_name, dough, *toppings, **options):
    print(f"피자: {pizza_name}")
    print(f"도우: {dough}")
    print(f"추가 토핑: {toppings}")
    print(f"추가 옵션: {options}")

make_pizza("페퍼로니 피자", "오리지널", "치즈", "올리브", "버섯", size="L", delivery_time=30)


print("\n--- 6. 키워드 전용 인자 실습 (메시지 전송) ---")

def send_message(recipient, content, *, delivery_method="email", urgent=False):
    print(f"받는 사람: {recipient}")
    print(f"내용: {content}")
    print(f"전송 방식: {delivery_method}")
    print(f"긴급 여부: {urgent}")

print("올바른 호출:")
send_message("홍길동", "안녕하세요", delivery_method="sms", urgent=True)

print("\n잘못된 호출 시도:")
try:
    send_message("홍길동", "안녕하세요", "sms", True)
except TypeError as e:
    print(f"에러 발생: {e}")