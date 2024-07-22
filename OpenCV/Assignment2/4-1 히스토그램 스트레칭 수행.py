import cv2 as cv
import numpy as np

# 이미지 파일 읽기
lena_img = cv.imread('lena.jpg')
mandrill_img = cv.imread('mandrill.jpg')

# 이미지가 제대로 읽어졌는지 확인
if lena_img is None or mandrill_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 그레이스케일로 변환
lena_gray = cv.cvtColor(lena_img, cv.COLOR_BGR2GRAY)
mandrill_gray = cv.cvtColor(mandrill_img, cv.COLOR_BGR2GRAY)

# 히스토그램 스트레칭 적용 전 그레이스케일 이미지
cv.imshow('Lena', lena_gray)
cv.imshow('Mandrill', mandrill_gray)

# 히스토그램 스트레칭 함수 정의
def histogram_stretching(img):
    # 최솟값과 최댓값 계산
    min_val = np.min(img)
    max_val = np.max(img)
    
    # 히스토그램 스트레칭 적용
    stretched_img = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    
    return stretched_img

# 히스토그램 스트레칭 적용
lena_stretched = histogram_stretching(lena_gray)
mandrill_stretched = histogram_stretching(mandrill_gray)

# 히스토그램 스트레칭 적용 후 그레이스케일 이미지
cv.imshow('Stretching Lena', lena_stretched)
cv.imshow('Stretching Mandrill', mandrill_stretched)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()