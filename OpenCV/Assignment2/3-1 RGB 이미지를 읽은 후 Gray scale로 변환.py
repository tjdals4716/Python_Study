import cv2 as cv

# 첫 번째 이미지 읽기
lena_rgb = cv.imread('lena.jpg')

# 두 번째 이미지 읽기
mandrill_rgb = cv.imread('mandrill.jpg')

# 이미지가 제대로 읽어졌는지 확인
if lena_rgb is None or mandrill_rgb is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# RGB 이미지를 Gray scale로 변환
lena_gray = cv.cvtColor(lena_rgb, cv.COLOR_BGR2GRAY)
mandrill_gray = cv.cvtColor(mandrill_rgb, cv.COLOR_BGR2GRAY)

# 이미지 출력
cv.imshow('Lena RGB', lena_rgb)
cv.imshow('Lena Gray', lena_gray)

cv.imshow('Mandrill RGB', mandrill_rgb)
cv.imshow('Mandrill Gray', mandrill_gray)

cv.waitKey(0)
cv.destroyAllWindows()