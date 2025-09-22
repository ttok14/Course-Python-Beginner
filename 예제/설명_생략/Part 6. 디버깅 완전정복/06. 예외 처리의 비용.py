# ====================================
# Part 6. 예외 처리의 성능 비용
# ====================================

import timeit

def plain():
    x = 1 + 1
    return x

def with_try():
    try:
        x = 1 + 1
        return x
    except:
        return -1

def with_exception():
    try:
        raise ValueError("Some error")
        return 1
    except:
        return -1

execution_count = 10_000_000

print(f"=== 성능 측정 결과 ({execution_count:,}번 실행) ===")

plain_time = timeit.timeit("plain()", globals=globals(), number=execution_count)
print(f"1. 기본 연산 (plain):                 {plain_time:.6f} 초")

with_try_time = timeit.timeit("with_try()", globals=globals(), number=execution_count)
print(f"2. 예외 없는 try (with_try):         {with_try_time:.6f} 초")

with_exception_time = timeit.timeit("with_exception()", globals=globals(), number=execution_count)
print(f"3. 예외 발생 및 처리 (with_exception): {with_exception_time:.6f} 초")