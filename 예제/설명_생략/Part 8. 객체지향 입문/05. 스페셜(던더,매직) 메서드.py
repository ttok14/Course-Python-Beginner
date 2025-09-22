# ====================================
# Part 8. 스페셜(던더,매직) 메서드
# ====================================

class Dog:
    def __init__(self, name, breed, weight):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.__secret_note = "이 강아지는 사실 천재다."

    def __str__(self):
        return f"이름: {self.name}, 품종: {self.breed}, 몸무게: {self.weight}kg"

    def __len__(self):
        return self.weight

    def __del__(self):
        print(f"{self.name} 객체가 소멸됩니다.")


print("--- 1. __str__ 메서드 테스트 ---")
poppy = Dog("뽀삐", "말티즈", 5)

print(poppy)
print("\n")


print("--- 2. __len__ 메서드 테스트 ---")
try:
    pass
except TypeError as e:
    print(f"에러 발생: {e}")

print(f"강아지의 길이(몸무게): {len(poppy)}")
print("\n")


print("--- 3. 이름 맹글링(Name Mangling) 테스트 ---")
try:
    print(poppy.__secret_note)
except AttributeError as e:
    print(f"에러 발생: {e}")

print(f"변경된 이름으로 접근: {poppy._Dog__secret_note}")
print("\n")


print("--- 4. __del__ 메서드 테스트 ---")
print("poppy 변수 삭제 시도...")
del poppy
print("poppy 변수가 삭제되었습니다.")
print("\n")

print("--- 삭제된 변수 접근 시도 ---")
try:
    print(poppy)
except NameError as e:
    print(f"에러 발생: {e}")