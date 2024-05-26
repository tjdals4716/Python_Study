import cv2 as cv

# 이미지 파일 읽기
lena_img = cv.imread('lena.jpg')
mandrill_img = cv.imread('mandrill.jpg')

# 이미지가 제대로 읽어졌는지 확인
if lena_img is None or mandrill_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 이미지를 그레이스케일로 변환
lena_gray = cv.cvtColor(lena_img, cv.COLOR_BGR2GRAY)
mandrill_gray = cv.cvtColor(mandrill_img, cv.COLOR_BGR2GRAY)

# 전역 임계값 적용
_, lena_thresh = cv.threshold(lena_gray, 127, 255, cv.THRESH_BINARY)
_, mandrill_thresh = cv.threshold(mandrill_gray, 127, 255, cv.THRESH_BINARY)

# 객체 분할 결과 표시
cv.imshow('Lena Threshold', lena_thresh)
cv.imshow('Mandrill Threshold', mandrill_thresh)

# 원본 이미지도 표시
cv.imshow('Lena Original', lena_img)
cv.imshow('Mandrill Original', mandrill_img)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()