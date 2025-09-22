# ====================================
# Part 6. Assert 와 Logging 으로 방어력 높이기
# ====================================

import logging
import os

print("--- 1. 기본 장바구니 계산 코드 ---")

my_cart = [
    {'name': '노트북', 'price': 1200000},
    {'name': '마우스', 'price': 30000}
]

def calculate_cart_total(cart):
    total_price = 0
    for item in cart:
        total_price += item['price']
    return total_price

total = calculate_cart_total(my_cart)
print(f"정상 데이터 총 합계: {total}원\n")


print("--- 2. assert로 가격 유효성 검증하기 ---")

my_cart_with_error = [
    {'name': '노트북', 'price': 1200000},
    {'name': '키보드', 'price': -50000}, 
    {'name': '마우스', 'price': 30000}
]

def calculate_cart_with_assert(cart):
    total_price = 0
    for item in cart:
        assert item['price'] > 0, f"가격 오류: {item['name']}의 가격({item['price']})이 0보다 작거나 같습니다."
        total_price += item['price']
    return total_price

try:
    total = calculate_cart_with_assert(my_cart_with_error)
    print(f"총 합계: {total}원")
except AssertionError as e:
    print("AssertionError가 발생했습니다. 프로그램이 여기서 중단되는 것이 정상입니다.")
    print(f"오류 메시지: {e}\n")


print("--- 3. logging 기본 사용 및 레벨 설정 ---")

logging.basicConfig(level=logging.DEBUG, force=True)

def calculate_cart_with_logging(cart):
    total_price = 0
    logging.debug(f"계산 시작: 총 {len(cart)}개의 항목이 있습니다.")

    for item in cart:
        assert item['price'] > 0, f"가격 오류: {item['name']}의 가격이 0보다 작거나 같습니다."
        total_price += item['price']

    logging.info(f"계산 완료. 총 합계: {total_price}원")
    return total_price

print("# 로그 레벨이 DEBUG일 때의 출력:")
calculate_cart_with_logging(my_cart)
print("")


print("--- 4. logging 레벨 변경의 효과 ---")
logging.basicConfig(level=logging.INFO, force=True)

print("# 로그 레벨이 INFO일 때의 출력 (DEBUG 메시지 생략됨):")
calculate_cart_with_logging(my_cart)
print("")


print("--- 5. logging 파일로 저장하기 ---")
log_filename = 'app.log'

logging.basicConfig(level=logging.INFO,
                    filename=log_filename,
                    filemode='w', 
                    encoding='utf-8',
                    force=True)

print(f"로그를 '{log_filename}' 파일에 기록합니다. 터미널에는 로그가 출력되지 않습니다.")
calculate_cart_with_logging(my_cart)
print(f"'{log_filename}' 파일 생성이 완료되었습니다.")

try:
    with open(log_filename, 'r', encoding='utf-8') as f:
        print(f"\n--- '{log_filename}' 파일 내용 ---")
        print(f.read().strip())
        print("--------------------------\n")
except FileNotFoundError:
    print(f"'{log_filename}' 파일이 생성되지 않았습니다.")
finally:
    if os.path.exists(log_filename):
        os.remove(log_filename)