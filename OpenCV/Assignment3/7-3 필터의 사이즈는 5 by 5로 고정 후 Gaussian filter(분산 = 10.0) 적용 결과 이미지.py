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