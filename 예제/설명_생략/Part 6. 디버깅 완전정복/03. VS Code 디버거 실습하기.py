# ====================================
# Part 6. 디버깅 완전정복 - VS Code 디버거 실습하기
# ====================================

def show_greeting(user_name, current_hour):
    time_text = "안녕하세요"

    if current_hour >= 6 and current_hour < 12:
        time_text = "좋은 아침"
    
    if current_hour >= 12 and current_hour < 18: 
        time_text = "활기찬 오후"
    else:
        time_text = "편안한 저녁"

    message = f"{time_text}, {user_name}님! 현재 시각은 {current_hour}시입니다."
    print(message)


print("--- 버그가 있는 코드 실행 결과 ---")
show_greeting("이강원", 10)
print("-" * 30)


def show_greeting_fixed(user_name, current_hour):
    time_text = "안녕하세요"

    if current_hour >= 6 and current_hour < 12:
        time_text = "좋은 아침"
    elif current_hour >= 12 and current_hour < 18:
        time_text = "활기찬 오후"
    else:
        time_text = "편안한 저녁"

    message = f"{time_text}, {user_name}님! 현재 시각은 {current_hour}시입니다."
    print(message)


print("--- 버그를 수정한 코드 실행 결과 ---")
show_greeting_fixed("이강원", 10)
print("-" * 30)