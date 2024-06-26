from tkinter import *

window = Tk()
photo = PhotoImage(file = '/Users/thdtjdals__/Desktop/데이터 분석 2일차 자료/GIF/cat.gif')
h = photo.height()
w = photo.width()
print('이미지 크기 : ', h, 'x', w)

# RGB의 값을 가져온다
photoR=[ [0 for _ in range(h)] for _ in range(w)]
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

print('[50][50] 위치의 RGB 값 : ', photoR[50][50], photoG[50][50], photoB[50][50] )
