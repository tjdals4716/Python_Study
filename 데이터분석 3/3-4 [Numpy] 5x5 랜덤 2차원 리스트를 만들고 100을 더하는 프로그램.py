# 넘파이 : 파이썬에서 배열을 처리할때 사용되는 라이브러리
# 배열 계산에 최적화된 방식과 빠른 처리 속도

import random
## 파이썬 2차원 리스트 생성
SIZE = 5
pythonList = [ [random.randint(0,255) for _ in range(SIZE)] for _ in range(SIZE)]

## 랜덤 기존 리스트를 출력하기
for i in range(SIZE) :
    for k in range(SIZE) :
        print("%3d" % pythonList[i][k], end=' ')
    print()
print()

## 기존 리스트에 100을 더하기
for i in range(SIZE) :
    for k in range(SIZE) :
        pythonList[i][k] += 100

## 기존 리스트에서 100을 더한 리스트를 출력하기
for i in range(SIZE) :
    for k in range(SIZE) :
        print("%3d" % pythonList[i][k], end=' ')
    print()