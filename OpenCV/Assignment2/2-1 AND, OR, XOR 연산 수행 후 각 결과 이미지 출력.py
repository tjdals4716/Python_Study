import cv2 as cv

# 첫 번째 이미지 읽기
img1 = cv.imread('lena.jpg')

# 두 번째 이미지 읽기
img2 = cv.imread('butterfly.bmp')

# 이미지가 제대로 읽어졌는지 확인
if img1 is None or img2 is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지 사이즈 맞추기
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))

# 이미지를 그레이스케일로 변환
img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2_gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# 비트 AND, OR, XOR 연산 수행
result_and = cv.bitwise_and(img1_gray, img2_gray)
result_or = cv.bitwise_or(img1_gray, img2_gray)
result_xor = cv.bitwise_xor(img1_gray, img2_gray)

# 결과 이미지 출력
cv.imshow('AND : ', result_and)
cv.imshow('OR : ', result_or)
cv.imshow('XOR : ', result_xor)

# 이미지를 화면에 표시
cv.imshow('Image1', img1)
cv.imshow('Image2', img2)
cv.waitKey(0)
cv.destroyAllWindows()