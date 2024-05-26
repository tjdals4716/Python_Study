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

# 히스토그램 평활화 적용
equalized_img1 = cv.equalizeHist(gray_img1)
equalized_img2 = cv.equalizeHist(gray_img2)

# 히스토그램 평활화 적용 전 이미지 표시
cv.imshow('Lena', gray_img1)
cv.imshow('Mandrill', gray_img2)

# 히스토그램 평활화 적용 후 이미지 표시
cv.imshow('Equalized Lena', equalized_img1)
cv.imshow('Equalized Mandrill', equalized_img2)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()