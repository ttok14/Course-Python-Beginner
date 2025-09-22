# ====================================
# Part4. 컴프리헨션 활용
# ====================================

numbers = [1, 2, 3, 4, 5]
words = ['apple', 'banana', 'cherry', 'kiwi', 'orange']


multiplied_by_10 = [n * 10 for n in numbers]
print("1-1. 각 숫자에 10을 곱한 리스트:", multiplied_by_10)

long_words = [word for word in words if len(word) >= 5]
print("1-2. 길이가 5 이상인 단어:", long_words)

upper_words = [word.upper() for word in words]
print("1-3. 대문자로 변환된 단어:", upper_words)


fruits = ['사과', '바나나', '딸기']
prices = [1500, 3000, 2000]

fruit_price_dict = {f: p for f, p in zip(fruits, prices)}
print("\n2. 과일 가격 딕셔너리:", fruit_price_dict)


numbers_with_duplicates = [1, 3, 2, 4, 3, 2, 1, 5, 5]

even_numbers_set = {n for n in numbers_with_duplicates if n % 2 == 0}
print("\n3. 중복 없는 짝수 세트:", even_numbers_set)


products = [
    {'name': '무선 마우스', 'price': 18000},
    {'name': '블루투스 키보드', 'price': 32000},
    {'name': '모니터 받침대', 'price': 15000},
    {'name': 'USB 허브', 'price': 25000}
]

affordable_product_names = [p['name'] for p in products if p['price'] < 20000]
print("\n4. 2만원 미만 상품:", affordable_product_names)