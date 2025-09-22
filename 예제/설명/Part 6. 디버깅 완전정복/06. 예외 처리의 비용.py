# ====================================
# Part 6. 예외 처리의 성능 비용
# ====================================

# timeit 모듈은 코드의 실행 시간을 정밀하게 측정하는 데 사용되는 표준 라이브러리입니다.
import timeit

# --- 성능 비교를 위한 세 가지 시나리오의 함수를 정의합니다. ---

# 1. 기본 연산 함수 (비교 기준)
# 예외 처리 없이 간단한 산술 연산만 수행하는 함수입니다. 성능 측정의 기준점이 됩니다.
def plain():
    x = 1 + 1
    return x

# 2. try/except 블록이 있지만 예외가 발생하지 않는 함수
# 파이썬 3.11부터 도입된 'Zero-Cost Exception Handling'의 성능을 확인하기 위한 케이스입니다.
# 예외가 발생하지 않으면 try 블록의 존재가 성능에 거의 영향을 주지 않음을 보여줍니다.
def with_try():
    try:
        x = 1 + 1
        return x
    except:
        return -1

# 3. try/except 블록 내에서 실제로 예외가 발생하는 함수
# 예외가 발생하고, 이를 처리하는 과정에 드는 비용을 측정하기 위한 케이스입니다.
def with_exception():
    try:
        raise ValueError("Some error")  # 의도적으로 예외를 발생시킵니다.
        return 1 # 이 코드는 실행되지 않습니다.
    except:
        return -1

# --- 각 함수의 실행 시간을 측정합니다. ---

# 측정할 반복 횟수를 정의합니다. 숫자가 클수록 측정의 정확도가 높아집니다.
execution_count = 10_000_000

print(f"=== 성능 측정 결과 ({execution_count:,}번 실행) ===")

# timeit.timeit() 함수를 사용하여 각 함수의 실행 시간을 측정합니다.
# stmt: 측정할 코드를 문자열로 전달합니다.
# globals=globals(): timeit 환경에서 현재 파일에 정의된 함수를 찾을 수 있도록 합니다.
# number: stmt를 실행할 횟수입니다.

plain_time = timeit.timeit("plain()", globals=globals(), number=execution_count)
print(f"1. 기본 연산 (plain):                 {plain_time:.6f} 초")

with_try_time = timeit.timeit("with_try()", globals=globals(), number=execution_count)
print(f"2. 예외 없는 try (with_try):         {with_try_time:.6f} 초")

with_exception_time = timeit.timeit("with_exception()", globals=globals(), number=execution_count)
print(f"3. 예외 발생 및 처리 (with_exception): {with_exception_time:.6f} 초")

# --- 결과 분석 ---
# 실행 결과에서 [plain]과 [with_try]의 실행 시간은 거의 비슷하게 측정됩니다.
# 이는 파이썬 3.11 이상에서 예외가 발생하지 않는 한 try 블록의 성능 비용이 거의 없다는 것을 의미합니다. (Zero-Cost Exceptions)

# 반면, [with_exception]의 실행 시간은 현저히 느립니다.
# 이는 예외가 실제로 발생했을 때, 파이썬이 에러 정보를 수집하고(Traceback 생성),
# 적절한 except 블록을 찾는 과정에 상당한 비용이 발생함을 보여줍니다.


'''
    - 정리하며
        1. 파이썬 3.11부터 'Zero-Cost Exception Handling'이 도입되었습니다.
        2. 이로 인해 예외가 '발생하지 않는다면', try-except 블록의 성능 오버헤드는 거의 무시할 수 있는 수준입니다.
        3. 하지만 예외가 '실제로 발생하여 처리'되는 과정은 여전히 상당한 비용이 드는 작업입니다.
        4. 예외 발생 시 비용이 큰 이유는 에러가 발생한 지점까지의 호출 스택(Traceback)을 추적하고 기록하는 과정이 포함되기 때문입니다.
        5. 따라서 try-except는 예상 가능한 예외 상황을 처리하는 데 사용하고, 개발 중 논리적 오류는 디버거, assert 등으로 찾는 것이 바람직합니다.
'''