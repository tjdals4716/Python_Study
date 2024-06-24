import turtle
import random

# GUI 창 크기 설정
window_size = 800  # 창의 너비와 높이 (800x800 픽셀로 설정)
canvas_width = 800  # 캔버스 너비
canvas_height = 800  # 캔버스 높이


def screenLeftClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)

def screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

def screenMidClick(x, y):
    global r, g, b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

# 초기 설정
pSize = 10
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

# 창 크기와 위치 설정
turtle.setup(window_size, window_size)  # 너비와 높이 설정
turtle.screensize(window_size-100, window_size-100)  # 스크린 사이즈 조정

# 화면 초기 위치 설정 (중앙으로)
turtle.setworldcoordinates(-window_size/2, -window_size/2, window_size/2, window_size/2)

# 이벤트 핸들러 등록
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

# GUI 이벤트 루프 시작
turtle.done()
