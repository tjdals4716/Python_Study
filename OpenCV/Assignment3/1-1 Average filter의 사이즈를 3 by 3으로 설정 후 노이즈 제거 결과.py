import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽어졌는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Average filter 적용 함수 정의
def apply_average_filter(img, filter_size):
    # 평균 필터 생성
    kernel = np.ones((filter_size, filter_size), np.float32) / (filter_size * filter_size)
    
    # 필터 적용
    result = cv.filter2D(img, -1, kernel)
    
    return result

# Average filter 적용 (3 by 3)
lena_gaussian_noise_filtered = apply_average_filter(lena_gaussian_noise_img, 3)
salt_pepper_noise_filtered = apply_average_filter(salt_pepper_noise_img, 3)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

cv.imshow('a', lena_gaussian_noise_img)
cv.imshow('b', salt_pepper_noise_img)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()