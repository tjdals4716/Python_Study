
# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Average filter의 사이즈를 3 by 3으로 설정 후 노이즈 제거 결과
'''
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
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Average filter의 사이즈를 7 by 7으로 설정 후 노이즈 제거 결과
'''
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

# Average filter 적용 (7 by 7)
lena_gaussian_noise_filtered = apply_average_filter(lena_gaussian_noise_img, 7)
salt_pepper_noise_filtered = apply_average_filter(salt_pepper_noise_img, 7)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Average filter의 사이즈를 11 by 11으로 설정 후 노이즈 제거 결과
'''
import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
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

# Average filter 적용 (11 by 11)
lena_gaussian_noise_filtered = apply_average_filter(lena_gaussian_noise_img, 11)
salt_pepper_noise_filtered = apply_average_filter(salt_pepper_noise_img, 11)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Average filter의 사이즈를 17 by 17으로 설정 후 노이즈 제거 결과
'''
import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
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

# Average filter 적용 (17 by 17)
lena_gaussian_noise_filtered = apply_average_filter(lena_gaussian_noise_img, 17)
salt_pepper_noise_filtered = apply_average_filter(salt_pepper_noise_img, 17)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Median filter의 사이즈를 3 by 3으로 설정 후 노이즈 제거 결과
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Median filter 적용 함수 정의
def apply_median_filter(img, filter_size):
    # Median 필터 적용
    result = cv.medianBlur(img, filter_size)
    
    return result

# Median filter 적용 (3 by 3)
lena_gaussian_noise_filtered = apply_median_filter(lena_gaussian_noise_img, 3)
salt_pepper_noise_filtered = apply_median_filter(salt_pepper_noise_img, 3)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Median filter의 사이즈를 7 by 7으로 설정 후 노이즈 제거 결과
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Median filter 적용 함수 정의
def apply_median_filter(img, filter_size):
    # Median 필터 적용
    result = cv.medianBlur(img, filter_size)
    
    return result

# Median filter 적용 (7 by 7)
lena_gaussian_noise_filtered = apply_median_filter(lena_gaussian_noise_img, 7)
salt_pepper_noise_filtered = apply_median_filter(salt_pepper_noise_img, 7)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Median filter의 사이즈를 11 by 11으로 설정 후 노이즈 제거 결과
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Median filter 적용 함수 정의
def apply_median_filter(img, filter_size):
    # Median 필터 적용
    result = cv.medianBlur(img, filter_size)
    
    return result

# Median filter 적용 (11 by 11)
lena_gaussian_noise_filtered = apply_median_filter(lena_gaussian_noise_img, 11)
salt_pepper_noise_filtered = apply_median_filter(salt_pepper_noise_img, 11)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''


# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Median filter의 사이즈를 17 by 17으로 설정 후 노이즈 제거 결과
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Median filter 적용 함수 정의
def apply_median_filter(img, filter_size):
    # Median 필터 적용
    result = cv.medianBlur(img, filter_size)
    
    return result

# Median filter 적용 (17 by 17)
lena_gaussian_noise_filtered = apply_median_filter(lena_gaussian_noise_img, 17)
salt_pepper_noise_filtered = apply_median_filter(salt_pepper_noise_img, 17)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Gaussian filter의 사이즈를 3 by 3으로 설정 후 노이즈 제거 결과 (분산값은 1.0으로 설정)
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Gaussian filter 적용 함수 정의
def apply_gaussian_filter(img, filter_size):
    # Gaussian 필터 분산값은 1.0으로 설정
    result = cv.GaussianBlur(img, (filter_size, filter_size), 1.0)
    
    return result

# Gaussian filter 적용 (3 by 3)
lena_gaussian_noise_filtered = apply_gaussian_filter(lena_gaussian_noise_img, 3)
salt_pepper_noise_filtered = apply_gaussian_filter(salt_pepper_noise_img, 3)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Gaussian filter의 사이즈를 7 by 7으로 설정 후 노이즈 제거 결과 (분산값은 1.0으로 설정)
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Gaussian filter 적용 함수 정의
def apply_gaussian_filter(img, filter_size):
    # Gaussian 필터 분산값은 1.0으로 설정
    result = cv.GaussianBlur(img, (filter_size, filter_size), 1.0)
    
    return result

# Gaussian filter 적용 (7 by 7)
lena_gaussian_noise_filtered = apply_gaussian_filter(lena_gaussian_noise_img, 7)
salt_pepper_noise_filtered = apply_gaussian_filter(salt_pepper_noise_img, 7)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Gaussian filter의 사이즈를 11 by 11으로 설정 후 노이즈 제거 결과 (분산값은 1.0으로 설정)
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Gaussian filter 적용 함수 정의
def apply_gaussian_filter(img, filter_size):
    # Gaussian 필터 분산값은 1.0으로 설정
    result = cv.GaussianBlur(img, (filter_size, filter_size), 1.0)
    
    return result

# Gaussian filter 적용 (11 by 11)
lena_gaussian_noise_filtered = apply_gaussian_filter(lena_gaussian_noise_img, 11)
salt_pepper_noise_filtered = apply_gaussian_filter(salt_pepper_noise_img, 11)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 1. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 Gaussian filter의 사이즈를 17 by 17으로 설정 후 노이즈 제거 결과 (분산값은 1.0으로 설정)
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Gaussian filter 적용 함수 정의
def apply_gaussian_filter(img, filter_size):
    # Gaussian 필터 분산값은 1.0으로 설정
    result = cv.GaussianBlur(img, (filter_size, filter_size), 1.0)
    
    return result

# Gaussian filter 적용 (17 by 17)
lena_gaussian_noise_filtered = apply_gaussian_filter(lena_gaussian_noise_img, 17)
salt_pepper_noise_filtered = apply_gaussian_filter(salt_pepper_noise_img, 17)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Average filter(분산 = 2.0) 적용 결과 이미지
'''
import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Average filter 적용 함수 정의
def apply_average_filter(img, filter_size, variance):
    # 평균 필터 생성
    kernel = np.ones((filter_size, filter_size), np.float32) / (filter_size * filter_size)
    
    # 필터 적용
    result = cv.filter2D(img, -1, kernel)
    
    return result

# Average filter 적용 (5 by 5, 분산 = 2.0)
lena_gaussian_noise_filtered = apply_average_filter(lena_gaussian_noise_img, 5, 2.0)
salt_pepper_noise_filtered = apply_average_filter(salt_pepper_noise_img, 5, 2.0)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Median filter(분산 = 2.0) 적용 결과 이미지
'''
import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Median filter 적용 함수 정의
def apply_median_filter(img, filter_size):
    # Median 필터 적용
    result = cv.medianBlur(img, filter_size)
    
    return result

# Median filter 적용 (5 by 5)
lena_gaussian_noise_filtered = apply_median_filter(lena_gaussian_noise_img, 5)
salt_pepper_noise_filtered = apply_median_filter(salt_pepper_noise_img, 5)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Gaussian filter(분산 = 2.0) 적용 결과 이미지

import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Gaussian filter 적용 함수 정의
def apply_gaussian_filter(img, filter_size, sigma):
    # Gaussian 필터 적용
    result = cv.GaussianBlur(img, (filter_size, filter_size), sigma)
    
    return result

# Gaussian filter 적용 (5 by 5, 분산 = 2.0)
lena_gaussian_noise_filtered = apply_gaussian_filter(lena_gaussian_noise_img, 5, 2.0)
salt_pepper_noise_filtered = apply_gaussian_filter(salt_pepper_noise_img, 5, 2.0)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()




# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Average filter(분산 = 4.0) 적용 결과 이미지
'''
import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
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

# Average filter 적용 (5 by 5)
lena_gaussian_noise_filtered = apply_average_filter(lena_gaussian_noise_img, 5)
salt_pepper_noise_filtered = apply_average_filter(salt_pepper_noise_img, 5)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Median filter(분산 = 4.0) 적용 결과 이미지
'''
import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Median filter 적용 함수 정의
def apply_median_filter(img, filter_size):
    # Median 필터 적용
    result = cv.medianBlur(img, filter_size)
    
    return result

# Median filter 적용 (5 by 5)
lena_gaussian_noise_filtered = apply_median_filter(lena_gaussian_noise_img, 5)
salt_pepper_noise_filtered = apply_median_filter(salt_pepper_noise_img, 5)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Gaussian filter(분산 = 4.0) 적용 결과 이미지

import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Gaussian filter 적용 함수 정의
def apply_gaussian_filter(img, filter_size, sigma):
    # Gaussian 필터 적용
    result = cv.GaussianBlur(img, (filter_size, filter_size), sigma)
    
    return result

# Gaussian filter 적용 (5 by 5, 분산 = 4.0)
lena_gaussian_noise_filtered = apply_gaussian_filter(lena_gaussian_noise_img, 5, 4.0)
salt_pepper_noise_filtered = apply_gaussian_filter(salt_pepper_noise_img, 5, 4.0)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()




# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Average filter(분산 = 7.0) 적용 결과 이미지
'''
import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Average filter 적용 함수 정의
def apply_average_filter(img, filter_size, variance):
    # 평균 필터 생성
    kernel = np.ones((filter_size, filter_size), np.float32) / (filter_size * filter_size)
    
    # 필터 적용
    result = cv.filter2D(img, -1, kernel)
    
    return result

# Average filter 적용 (5 by 5, 분산 = 7.0)
lena_gaussian_noise_filtered = apply_average_filter(lena_gaussian_noise_img, 5, 7.0)
salt_pepper_noise_filtered = apply_average_filter(salt_pepper_noise_img, 5, 7.0)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Median filter(분산 = 7.0) 적용 결과 이미지
'''
import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Median filter 적용 함수 정의
def apply_median_filter(img, filter_size):
    # Median 필터 적용
    result = cv.medianBlur(img, filter_size)
    
    return result

# Median filter 적용 (5 by 5)
lena_gaussian_noise_filtered = apply_median_filter(lena_gaussian_noise_img, 5)
salt_pepper_noise_filtered = apply_median_filter(salt_pepper_noise_img, 5)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Gaussian filter(분산 = 7.0) 적용 결과 이미지
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Gaussian filter 적용 함수 정의
def apply_gaussian_filter(img, filter_size, sigma):
    # Gaussian 필터 적용
    result = cv.GaussianBlur(img, (filter_size, filter_size), sigma)
    
    return result

# Gaussian filter 적용 (5 by 5, 분산 = 7.0)
lena_gaussian_noise_filtered = apply_gaussian_filter(lena_gaussian_noise_img, 5, 7.0)
salt_pepper_noise_filtered = apply_gaussian_filter(salt_pepper_noise_img, 5, 7.0)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Average filter(분산 = 10.0) 적용 결과 이미지
'''
import cv2 as cv
import numpy as np

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Average filter 적용 함수 정의
def apply_average_filter(img, filter_size):
    # Average 필터 생성
    kernel = np.ones((filter_size, filter_size), np.float32) / (filter_size * filter_size)
    
    # 필터 적용
    result = cv.filter2D(img, -1, kernel)
    
    return result

# Average filter 적용 (5 by 5, 분산 = 10.0)
lena_gaussian_noise_filtered = apply_average_filter(lena_gaussian_noise_img, 5)
salt_pepper_noise_filtered = apply_average_filter(salt_pepper_noise_img, 5)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''



# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Median filter(분산 = 10.0) 적용 결과 이미지
'''
import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Median filter 적용 함수 정의
def apply_median_filter(img, filter_size):
    # Median 필터 적용
    result = cv.medianBlur(img, filter_size)
    
    return result

# Median filter 적용 (5 by 5, 분산 = 10.0)
lena_gaussian_noise_filtered = apply_median_filter(lena_gaussian_noise_img, 5)
salt_pepper_noise_filtered = apply_median_filter(salt_pepper_noise_img, 5)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''


'''
# 2. Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 대해 필터의 사이즈는 5 by 5로 고정 후 Gaussian filter(분산 = 10.0) 적용 결과 이미지

import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('Copy of Lena-Gaussian-noise.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# Gaussian filter 적용 함수 정의
def apply_gaussian_filter(img, filter_size, sigma):
    # Gaussian 필터 적용
    result = cv.GaussianBlur(img, (filter_size, filter_size), sigma)
    
    return result

# Gaussian filter 적용 (5 by 5, 분산 = 10.0)
lena_gaussian_noise_filtered = apply_gaussian_filter(lena_gaussian_noise_img, 5, 10.0)
salt_pepper_noise_filtered = apply_gaussian_filter(salt_pepper_noise_img, 5, 10.0)

# 결과 이미지 표시
cv.imshow('Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''


'''
# 3. 로버트 크로스 필터를 Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 모두 적용한 결과와 이미지 출력

import cv2 as cv
import numpy as np

# 로버트 크로스 필터 정의
roberts_cross_v = np.array([[1, 0], [0, -1]])
roberts_cross_h = np.array([[0, 1], [-1, 0]])

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('img3.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 로버트 크로스 필터 적용 함수 정의
def apply_roberts_cross_filter(img):
    # 수직 방향 필터 적용
    vertical_edges = cv.filter2D(img, -1, roberts_cross_v)
    # 수평 방향 필터 적용
    horizontal_edges = cv.filter2D(img, -1, roberts_cross_h)
    # 결과 계산
    result = cv.addWeighted(vertical_edges, 0.5, horizontal_edges, 0.5, 0)
    return result

# 로버트 크로스 필터 적용
lena_gaussian_noise_filtered = apply_roberts_cross_filter(lena_gaussian_noise_img)
salt_pepper_noise_filtered = apply_roberts_cross_filter(salt_pepper_noise_img)

# 결과 이미지 표시
cv.imshow('Roberts Cross Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Roberts Cross Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''


'''
# 3. 소벨 필터를 Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 모두 적용한 결과와 이미지 출력

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

# 소벨 필터 적용 함수 정의
def apply_sobel_filter(img):
    # 소벨 필터 적용
    sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
    sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
    # 결과 계산
    sobel = cv.magnitude(sobel_x, sobel_y)
    sobel = cv.normalize(sobel, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    return sobel

# 소벨 필터 적용
lena_gaussian_noise_filtered = apply_sobel_filter(lena_gaussian_noise_img)
salt_pepper_noise_filtered = apply_sobel_filter(salt_pepper_noise_img)

# 결과 이미지 표시
cv.imshow('Sobel Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Sobel Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''


'''
# 3. 프리윗 필터를 Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 모두 적용한 결과와 이미지 출력

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
'''


'''
# 3. 캐니 필터를 Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 모두 적용한 결과와 이미지 출력

import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('img3.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 캐니 필터 적용 함수 정의
def apply_canny_filter(img):
    # 캐니 필터 적용
    canny = cv.Canny(img, 100, 200)
    return canny

# 캐니 필터 적용
lena_gaussian_noise_filtered = apply_canny_filter(lena_gaussian_noise_img)
salt_pepper_noise_filtered = apply_canny_filter(salt_pepper_noise_img)

# 결과 이미지 표시
cv.imshow('Canny Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Canny Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''


'''
# 3. 라플라시안 필터를 Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 모두 적용한 결과와 이미지 출력

import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('img3.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 라플라시안 필터 적용 함수 정의
def apply_laplacian_filter(img):
    # 그레이스케일 변환
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 라플라시안 필터 적용
    laplacian = cv.Laplacian(gray, cv.CV_64F)
    # 결과 이미지 정규화
    laplacian = cv.normalize(laplacian, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    return laplacian

# 라플라시안 필터 적용
lena_gaussian_noise_filtered = apply_laplacian_filter(lena_gaussian_noise_img)
salt_pepper_noise_filtered = apply_laplacian_filter(salt_pepper_noise_img)

# 결과 이미지 표시
cv.imshow('Laplacian Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('Laplacian Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''


'''
# 3. 라플라시안 오브 가우시안(LOG) 필터를 Copy of Lena-Gaussian-noise.jpg 이미지와 salt pepper noise.bmp 이미지에 모두 적용한 결과와 이미지 출력

import cv2 as cv

# Copy of Lena-Gaussian-noise.jpg 이미지 읽기
lena_gaussian_noise_img = cv.imread('img3.jpg')

# salt pepper noise.bmp 이미지 읽기
salt_pepper_noise_img = cv.imread('salt pepper noise.bmp')

# 두 이미지가 제대로 읽혔는지 확인
if lena_gaussian_noise_img is None or salt_pepper_noise_img is None:
    print('이미지를 읽을 수 없습니다')
    exit()

# 라플라시안 오브 가우시안(LOG) 필터 적용 함수 정의
def apply_log_filter(img):
    # 그레이스케일 변환
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 가우시안 블러 필터 적용
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    # 라플라시안 필터 적용
    laplacian = cv.Laplacian(blurred, cv.CV_64F)
    # 결과 이미지 정규화
    log = cv.normalize(laplacian, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)
    return log

# 라플라시안 오브 가우시안(LOG) 필터 적용
lena_gaussian_noise_filtered = apply_log_filter(lena_gaussian_noise_img)
salt_pepper_noise_filtered = apply_log_filter(salt_pepper_noise_img)

# 결과 이미지 표시
cv.imshow('LOG Filtered Lena Gaussian Noise', lena_gaussian_noise_filtered)
cv.imshow('LOG Filtered Salt Pepper Noise', salt_pepper_noise_filtered)

# 이미지를 화면에 표시
cv.waitKey(0)
cv.destroyAllWindows()
'''