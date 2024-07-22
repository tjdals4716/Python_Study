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