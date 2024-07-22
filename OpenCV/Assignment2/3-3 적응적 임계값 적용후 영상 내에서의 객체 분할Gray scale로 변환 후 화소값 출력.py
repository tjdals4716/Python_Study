import cv2 as cv

# 이미지 파일 읽기
img1 = cv.imread('lena.jpg')
img2 = cv.imread('mandrill.jpg')

# 이미지가 제대로 읽어졌는지 확인
if img1 is None or img2 is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지를 그레이스케일로 변환
gray_img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
gray_img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

# 적응적 임계값 적용
adaptive_thresh1 = cv.adaptiveThreshold(gray_img1, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
adaptive_thresh2 = cv.adaptiveThreshold(gray_img2, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

# 객체 분할 결과 표시
cv.imshow('Adaptive Threshold Lena', adaptive_thresh1)
cv.imshow('Adaptive Threshold Mandrill', adaptive_thresh2)

cv.imshow('Lena Original', img1)
cv.imshow('Mandrill Original', img2)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()