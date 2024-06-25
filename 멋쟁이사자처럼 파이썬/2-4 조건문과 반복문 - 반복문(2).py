# 6-4 조건문과 반복문 - 반복문(2)

# while 반복문
# 콘솔에서 Ctrl + C 를 하면 콘솔에서 실행 중인 실행을 강제로 종료
"""
# 아래를 실행하면 무한히 반복하게 됨
while True:
    print("while loop")
"""

# progress = 0 에서 설정한 초깃값 0부터 1이 더해지면서 100까지 설정한대로 출력
progress = 0

while progress < 100:
    
    progress = progress + 1
    print(f"{progress}% 완료됨")