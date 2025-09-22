# ====================================
# Part 6. Assert 와 Logging 으로 방어력 높이기
# ====================================

# Assert: 코드의 특정 조건이 참임을 단언합니다.
#         만약 조건이 거짓이면 AssertionError를 발생시키며 프로그램을 즉시 중단시킵니다.
#         주로 개발 단계에서 '절대 일어나서는 안 되는' 상황을 검증하는 데 사용됩니다.

# Logging: 프로그램의 실행 상태를 체계적으로 기록하기 위한 모듈입니다.
#          로그 레벨(DEBUG, INFO, WARNING, ERROR, CRITICAL)을 통해 메시지의 중요도를 구분하고,
#          파일로 기록을 남겨 프로그램 실행 후에도 활동을 분석할 수 있게 해줍니다.

import logging
import os # 파일 처리를 위해 os 모듈을 import 합니다.

# --- 1. 기본 장바구니 계산 코드 ---
print("--- 1. 기본 장바구니 계산 코드 ---")

# 상품 정보가 담긴 장바구니 리스트입니다.
my_cart = [
    {'name': '노트북', 'price': 1200000},
    {'name': '마우스', 'price': 30000}
]

def calculate_cart_total(cart):
    """장바구니에 담긴 상품들의 총액을 계산합니다."""
    total_price = 0
    for item in cart:
        total_price += item['price']
    return total_price

total = calculate_cart_total(my_cart)
print(f"정상 데이터 총 합계: {total}원\n")


# --- 2. assert로 가격 유효성 검증하기 ---
print("--- 2. assert로 가격 유효성 검증하기 ---")

# 가격이 음수인 잘못된 데이터가 포함된 장바구니입니다.
my_cart_with_error = [
    {'name': '노트북', 'price': 1200000},
    {'name': '키보드', 'price': -50000}, # 잘못된 데이터
    {'name': '마우스', 'price': 30000}
]

def calculate_cart_with_assert(cart):
    """
    assert를 사용하여 각 아이템의 가격이 양수인지 검증하며 총액을 계산합니다.
    가격이 0 이하일 경우 AssertionError가 발생합니다.
    """
    total_price = 0
    for item in cart:
        # assert 조건, "에러 메시지"
        # item['price']가 0보다 커야 한다는 조건을 단언합니다.
        # 조건이 거짓(False)이면 AssertionError와 함께 지정된 메시지를 출력하며 프로그램이 즉시 중단됩니다.
        assert item['price'] > 0, f"가격 오류: {item['name']}의 가격({item['price']})이 0보다 작거나 같습니다."
        total_price += item['price']
    return total_price

# 아래 코드는 잘못된 데이터를 만나면 AssertionError를 발생시킵니다.
# 스크립트의 나머지 부분이 실행될 수 있도록 try-except 구문으로 감싸서 예외를 처리합니다.
try:
    total = calculate_cart_with_assert(my_cart_with_error)
    print(f"총 합계: {total}원")
except AssertionError as e:
    print("AssertionError가 발생했습니다. 프로그램이 여기서 중단되는 것이 정상입니다.")
    print(f"오류 메시지: {e}\n")


# --- 3. logging 기본 사용 및 레벨 설정 ---
print("--- 3. logging 기본 사용 및 레벨 설정 ---")

# 로깅 기본 설정: level을 DEBUG로 설정하여 모든 레벨의 로그를 확인합니다.
# DEBUG < INFO < WARNING < ERROR < CRITICAL 순으로 심각도가 높습니다.
# force=True 옵션은 스크립트 내에서 로깅 설정을 여러 번 변경할 때 필요합니다. (Python 3.8 이상)
logging.basicConfig(level=logging.DEBUG, force=True)

def calculate_cart_with_logging(cart):
    """
    logging을 사용하여 계산 과정을 기록합니다.
    """
    total_price = 0
    # DEBUG: 개발 단계에서 변수 값 변화 등 상세한 정보를 확인할 때 사용합니다.
    logging.debug(f"계산 시작: 총 {len(cart)}개의 항목이 있습니다.")

    for item in cart:
        assert item['price'] > 0, f"가격 오류: {item['name']}의 가격이 0보다 작거나 같습니다."
        total_price += item['price']

    # INFO: 프로그램의 일반적인 실행 정보(e.g., 작업 완료)를 기록할 때 사용합니다.
    logging.info(f"계산 완료. 총 합계: {total_price}원")
    return total_price

print("# 로그 레벨이 DEBUG일 때의 출력:")
calculate_cart_with_logging(my_cart)
print("") # 줄바꿈


# --- 4. logging 레벨 변경의 효과 ---
print("--- 4. logging 레벨 변경의 효과 ---")
# 로깅 레벨을 INFO로 변경합니다.
# 이제 설정된 레벨(INFO)보다 낮은 심각도의 DEBUG 메시지는 출력되지 않습니다.
logging.basicConfig(level=logging.INFO, force=True)

print("# 로그 레벨이 INFO일 때의 출력 (DEBUG 메시지 생략됨):")
calculate_cart_with_logging(my_cart)
print("") # 줄바꿈


# --- 5. logging 파일로 저장하기 ---
print("--- 5. logging 파일로 저장하기 ---")
log_filename = 'app.log'

# 이제 로그를 터미널이 아닌 'app.log' 파일에 저장합니다.
# filename 인자를 사용하면 출력이 파일로 리디렉션됩니다.
# encoding='utf-8'인코딩으로 한글이 깨지지 않게 합니다.
# filemode='w'는 실행할 때마다 파일을 새로 쓰도록 합니다. (기본값은 'a'로 이어쓰기)
logging.basicConfig(level=logging.INFO,
                    filename=log_filename,
                    filemode='w', # 실행마다 파일을 덮어쓰기 위해 'w' 모드 사용
                    encoding='utf-8',
                    force=True)

print(f"로그를 '{log_filename}' 파일에 기록합니다. 터미널에는 로그가 출력되지 않습니다.")
calculate_cart_with_logging(my_cart)
print(f"'{log_filename}' 파일 생성이 완료되었습니다.")

# 생성된 로그 파일의 내용을 읽어서 확인합니다.
try:
    with open(log_filename, 'r', encoding='utf-8') as f:
        print(f"\n--- '{log_filename}' 파일 내용 ---")
        print(f.read().strip())
        print("--------------------------\n")
except FileNotFoundError:
    print(f"'{log_filename}' 파일이 생성되지 않았습니다.")
finally:
    # 스크립트 실행 후 생성된 로그 파일을 깔끔하게 삭제합니다.
    if os.path.exists(log_filename):
        os.remove(log_filename)


'''
    - 정리하며
        1. assert는 개발 단계에서 코드의 논리적 무결성을 검증하는 '방어 장치'입니다.
           - '절대 일어나서는 안 되는 상황' (e.g., 가격이 음수)을 검증합니다.
           - 조건이 거짓이면 AssertionError를 발생시키고 프로그램을 중단시킵니다.

        2. logging은 프로그램의 모든 활동을 추적하고 분석하기 위한 '기록 도구'입니다.
           - 레벨(DEBUG, INFO, WARNING 등)을 조절하여 상황에 맞는 로그만 필터링할 수 있습니다.
           - 개발 중에는 DEBUG 레벨로 상세 정보를, 운영 중에는 INFO 레벨 이상으로 중요한 정보만 볼 수 있습니다.
           - filename 인자를 사용하여 로그를 파일로 영구 저장할 수 있습니다.

        3. assert는 '검증과 중단'이 목적이고, logging은 '기록과 추적'이 목적입니다.
           - 두 도구를 함께 사용하면 버그 발생 가능성이 낮고, 문제 추적이 용이한 견고한 코드를 작성할 수 있습니다.
'''