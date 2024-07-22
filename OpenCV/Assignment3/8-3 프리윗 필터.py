import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('img3.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 프리윗 필터 적용 함수 정의
def apply_prewitt_filter(img):
    # 프리윗 필터 적용
    prewitt_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
    prewitt_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
    # 결과 계산
    prewitt = cv.magnitude(prewitt_x, prewitt_y)
    prewitt = cv.normalize(prewitt, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    return prewitt

# 프리윗 필터 적용
lena_gaussian_noise_filtered = apply_prewitt_filter(lena_gaussian_noise_img)
salt_pepper_noise_filtered = apply_prewitt_filter(salt_pepper_noise_img)

# 결과 이미지 표시
cv.imshow('Prewitt Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Prewitt Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()