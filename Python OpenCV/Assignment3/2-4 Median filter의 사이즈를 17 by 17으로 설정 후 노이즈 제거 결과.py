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